---
paths:
  - ".claude/commands/**/*"
---

# claude-compatibility

项目按需指南。代码路径与命令均以项目根目录为基准；原有边界和例外继续适用。

# JD 雷达(jd-radar)

本项目的行为总规范(安全边界、信源分级、命令定义、输出规范)在 `AGENTS.md`:

# JD 雷达(jd-radar)

规则入口：[AGENTS.md](../../AGENTS.md)

# JD 雷达(jd-radar)

Claude Code 补充说明:

# JD 雷达(jd-radar)

- `/quickstart` `/setup` `/eval` `/compare` `/update` 已注册为项目级斜杠命令(.claude/commands/),可直接使用;用户不带斜杠输入 `quickstart`,或用自然语言说"帮我分析这个 JD"时,同样按 AGENTS.md 对应命令的流程执行。
- 截图输入直接用视觉能力读取,不需要 OCR 工具。
- 分析与报告保存边界统一遵循 `AGENTS.md`。
