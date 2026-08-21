# JD 雷达(jd-radar)

先完整阅读 [AGENTS.md](AGENTS.md) 并严格遵守其中全部规则——那是本项目的行为总规范(安全边界、信源分级、命令定义、输出规范)。

Claude Code 补充说明:

- 用户输入 `/quickstart` `/setup` `/eval` `/compare` `/update` 时,按 AGENTS.md 中对应命令的流程执行(这些是本项目的对话约定,不是已注册的斜杠命令;用户直接用自然语言说"帮我分析这个 JD"时同样进入 /eval 流程)。
- 截图输入直接用视觉能力读取,不需要 OCR 工具。
- 分析流程只读:除 `profile/profile.yaml` 与 `reports/` 目录外,不写任何文件;不执行 shell 命令。
