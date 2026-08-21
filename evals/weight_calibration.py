#!/usr/bin/env python3
"""权重默认值试算:用 8 个典型场景验证默认权重的排序是否符合求职直觉。

画像(试算基准):3 年互联网产品经验、目标转 AI 产品、坐标杭州,
期望到手 15k(底线 12k),必须双休(可偶尔加班),红线:外包、单休。

每个场景的六个维度分(0-10)是"假设 agent 已正确评估"的输入,
本脚本只验证:不同权重方案下,总分排序是否符合人工预期排序。
"""

DIMS = ["方向", "技能", "年限", "薪资", "工时", "通勤"]

WEIGHTS = {
    "W1 默认(方向技能主导)": [0.25, 0.25, 0.15, 0.15, 0.10, 0.10],
    "W2 六维均权":           [1/6] * 6,
    "W3 技能极重":           [0.15, 0.40, 0.10, 0.15, 0.10, 0.10],
}

# (场景, 六维分, 特殊标记)
CASES = [
    ("A 大厂AI产品·全面匹配",          [9, 8, 8, 8, 8, 8], None),
    ("B 方向完美·薪资仅达底线",        [9, 8, 8, 5, 8, 8], None),
    ("C 技能强匹配·但是传统电商PM",     [4, 9, 8, 8, 8, 8], None),
    ("D 初创AI产品·工时未知",          [8, 8, 7, 7, None, 8], "完整度83%"),
    ("E 方向匹配·通勤55分钟",          [9, 8, 8, 8, 8, 4], None),
    ("F 各维平庸",                     [6, 6, 6, 6, 6, 6], None),
    ("G 高薪但单休",                   [9, 8, 8, 9, 1, 8], "红线冲突:单休→置顶警示,不参与排序"),
    ("H 方向匹配·要求5-10年经验",      [9, 8, 2, 8, 8, 8], "资格风险:年限硬伤→判断层提示"),
]

# 人工预期排序(不含被红线剔除的 G;H 参与排序但带资格风险标记)。
# B 与 E 为「合理平局」:薪资敏感者 B 在前,通勤敏感者 E 在前,
# 取决于画像——这正是权重必须用户可调的实证。分差 <0.15 视为同档。
EXPECTED = [["A"], ["B", "E"], ["D"], ["H"], ["C"], ["F"]]
TIE_EPS = 0.15


def matches_expected(order_names, scores):
    i = 0
    for group in EXPECTED:
        got = sorted(order_names[i:i + len(group)])
        if got != sorted(group):
            return False
        i += len(group)
    return True


def score(dims, weights):
    """未知维度不猜:按已知维度归一化权重计分,另报完整度。"""
    known = [(d, w) for d, w in zip(dims, weights) if d is not None]
    wsum = sum(w for _, w in known)
    total = sum(d * w for d, w in known) / wsum
    completeness = wsum / sum(weights)
    return round(total, 2), round(completeness * 100)


def interval(dims, weights):
    """未知维度按 0 分和 10 分分别代入,得波动区间。"""
    lo = [d if d is not None else 0 for d in dims]
    hi = [d if d is not None else 10 for d in dims]
    f = lambda ds: round(sum(d * w for d, w in zip(ds, weights)), 2)
    return f(lo), f(hi)


for wname, weights in WEIGHTS.items():
    print(f"\n=== {wname} ===")
    rows = []
    for name, dims, note in CASES:
        s, comp = score(dims, weights)
        tag = ""
        if note and "红线" in note:
            tag = "  ⛔ " + note
        elif note and "资格" in note:
            tag = "  ⚠️ " + note
        elif None in dims:
            lo, hi = interval(dims, weights)
            tag = f"  (完整度{comp}%,区间 {lo}~{hi})"
        rows.append((name, s, tag, note))
    ranked = [r for r in rows if not (r[3] and "红线" in r[3])]
    ranked.sort(key=lambda r: -r[1])
    for name, s, tag, _ in ranked:
        print(f"  {s:5.2f}  {name}{tag}")
    order = [r[0].split()[0] for r in ranked]
    scores = {r[0].split()[0]: r[1] for r in ranked}
    exp = " > ".join("≈".join(g) for g in EXPECTED)
    ok = matches_expected(order, scores)
    print(f"  排序: {' > '.join(order)}   预期: {exp}   "
          f"{'✅ 符合(含同档平局)' if ok else '❌ 偏离'}")
