# 🧭 JD 雷达 jd-radar

**中国求职者的 JD 决策雷达 —— 跑在你自己的 Claude Code / Codex 里。**

贴一段 Boss 直聘 / 猎聘 / 公众号里的 JD,90 秒拿到一张决策卡:该不该聊、哪里有坑、还差什么信息、下一句话怎么问。分析与建议,永不代投。

> **jd-radar** — A local-first job-decision agent for the Chinese job market, running inside your own AI coding CLI (Claude Code / Codex / Cursor / OpenCode). Evaluate JDs with evidence-backed decision cards, detect China-specific scam patterns (培训贷 / 外包壳 / 虚假双休), and converge scores as you chat with HR. Analysis only — it never auto-applies.

## 它做什么

- **三层决策卡**:🛡 安全层(培训贷/收费/扣证件/签约主体不一致等硬风险,附命中原文与求助路径)→ 🧭 判断层(资格、偏好、最大未知项)→ 🎯 行动层(下一步 + 一条追问话术 + 开场白草稿)
- **动态评分**:JD 没写的绝不猜——报「信息完整度」和波动区间;和 HR 聊完把记录粘回来(`/update`),分数随信源升级收敛,全程留轨迹
- **信源分级**:JD 自述 < HR 确认 < 社区实测 < 官方文件。JD 写「双休」只算 L1 未验证——虚假 JD 骗不动一个不轻信的系统
- **中国语境规则库**:[坑位红旗库](docs/redflags.md)(依据五部门风险提示与平台官方案例)、[JD 黑话表](docs/jd-slang.md)、[三阶段追问话术](docs/asking-playbook.md)(初聊怎么问双休不被已读不回)
- **公开 evals**:[标注集 + 分项指标](evals/README.md),每轮规则迭代都重跑——不准就是下一轮的输入

## 为什么不直接问豆包 / ChatGPT?

一次性看一个岗位,聊天软件确实更方便。但你在求职战役里要处理几十上百个 JD 时:聊天每次都是随机标准的即兴回答,50 个岗位问出 50 种「还不错」;聊天 AI 默认顺着你说「很匹配」;没有档案、没有同一把尺子的排序、没有追问-回填闭环、更不知道该替你警惕培训贷和签约主体。Excel 早就存在,会计软件依然是行业——**「通用工具能做到」和「有一套固化的专业流程替你做对」是两回事。**

## 快速开始(3 分钟)

前提:任意 agent CLI(Claude Code / Codex / Cursor / OpenCode)。

```bash
git clone https://github.com/<you>/jd-radar.git
cd jd-radar
claude   # 或 codex / cursor / opencode
```

然后对它说:

```text
/quickstart
```

粘贴一个 JD,回答 4 个问题(方向/城市/薪资底线/两条红线),拿到第一张决策卡。完整建档用 `/setup`,多岗对比用 `/compare`,聊完 HR 回填用 `/update`。看看[真实样例报告](examples/sample-report-001-tonghuashun.md)。

## 隐私与数据流(诚实版)

- 本项目**没有服务器、不收集任何数据**;档案与报告保存在本目录。
- **本地保存 ≠ 本地处理**:分析时,JD 与你的简历内容会发送给你所选模型的服务商(Anthropic / OpenAI 等)处理——这由你与服务商的协议约束,与本项目无关。
- 各命令数据流:`/quickstart` `/setup`(简历→模型服务商)· `/eval`(JD→模型服务商;链接抓取仅限官网/猎聘等公开页)· `/update`(你粘贴的聊天记录→模型服务商)。
- `profile/profile.yaml` 与 `reports/` 已被 .gitignore 覆盖。**不要把含真实档案的仓库公开**(公开仓库无法私有 fork——建私有仓库、把本仓库设为 upstream)。

## 边界(明确不做)

❌ 自动投递 / 自动回复 HR ❌ 批量抓取平台 / 绕过验证码 ❌ 虚构经历(简历定制=选材与措辞)❌ 对企业下结论性定性(只呈现证据与线索,含申诉机制)。Boss 直聘链接的登录态读取属**实验功能**:默认关闭,需显式开启+专用浏览器 Profile,平台条款与账号风险自担;默认路径是复制 JD 文本粘贴,零风险。

⚠️ 本工具承诺的是**系统性降低被骗与错配的概率**,不是识破一切谎言;所有输出仅供参考,决定权永远在你。

## 路线图

- **P0(当前)**:/quickstart /setup /eval /compare /update + 安全门 + 追问话术 + evals
- **P1**:/tailor 定制简历(JSON Resume 数据层 + HTML/typst 双引擎,PDF+长图)· /deep 团队级背调 · /batch · 公司登记表与 /scan 隐藏岗位雷达
- **P2**:/track 投递漏斗 · /prep 面试准备包

## 贡献

最有价值的三种 PR:[黑话表](docs/jd-slang.md)补条目(附出处)、[公司登记表](companies/README.md)加公司(带元数据)、[标注集](evals/README.md)加样本(带 persona)。

## 致谢与许可

形态与工作流受 [career-ops](https://github.com/santifer/career-ops) 与 [ai-job-search](https://github.com/MadsLorentzen/ai-job-search) 启发;登录态读取路线参考 [boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper);社区公司数据的文化先例来自 [955.WLB](https://github.com/formulahendry/955.WLB) 与 996.ICU。代码与规则文件:MIT;`companies/` 数据:CC BY-SA 4.0。
