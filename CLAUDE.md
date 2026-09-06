# JD 雷达(jd-radar)

本项目的行为总规范(安全边界、信源分级、命令定义、输出规范)在 `AGENTS.md`:

@AGENTS.md

Claude Code 补充说明:

- `/quickstart` `/setup` `/eval` `/compare` `/update` 已注册为项目级斜杠命令(.claude/commands/),可直接使用;用户不带斜杠输入 `quickstart`,或用自然语言说"帮我分析这个 JD"时,同样按 AGENTS.md 对应命令的流程执行。
- 截图输入直接用视觉能力读取,不需要 OCR 工具。
- 分析流程只读:除 `profile/profile.yaml` 与 `reports/` 目录外,不写任何文件;不执行 shell 命令。
