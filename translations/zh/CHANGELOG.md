<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T11:40:46+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "zh"
}
-->
# 更新日志

记录了所有与 EdgeAI for Beginners 相关的重要更新。本项目采用基于日期的条目记录，并遵循 Keep a Changelog 风格（新增、变更、修复、移除、文档、移动）。

## 2025-09-18

### 新增
- 模块 08：Microsoft Foundry Local – 完整开发者工具包
  - 六个课程：设置、Azure AI Foundry 集成、开源模型、前沿演示、多代理和模型即工具
  - 可运行示例位于 `Module08/samples/01`–`06`，附带 Windows cmd 指令
    - `01` REST 快速聊天 (`chat_quickstart.py`)
    - `02` SDK 快速入门，支持 OpenAI/Foundry Local 和 Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI 列表与基准测试 (`list_and_bench.cmd`)
    - `04` Chainlit 演示 (`app.py`)
    - `05` 多代理编排 (`python -m samples.05.agents.coordinator`)
    - `06` 模型即工具路由器 (`router.py`)
- Session 2 SDK 示例新增 Azure OpenAI 支持，支持通过环境变量配置
- `.vscode/settings.json` 指向 `Module08/.venv`，提升 Python 分析解析能力
- `.env` 文件添加 `PYTHONPATH` 提示，增强 VS Code/Pylance 的识别能力

### 变更
- 默认模型更新为 `phi-4-mini`，覆盖模块 08 的文档和示例；移除模块 08 中剩余的 `phi-3.5` 提及
- 路由器 (`Module08/samples/06/router.py`) 改进：
  - 通过 `foundry service status` 和正则表达式解析进行端点发现
  - 启动时进行 `/v1/models` 健康检查
  - 环境变量可配置的模型注册表 (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- 依赖更新：`Module08/requirements.txt` 现在包括 `openai`（以及 `requests`, `chainlit`）
- Chainlit 示例指导更清晰，并新增故障排除；通过工作区设置解决导入问题

### 修复
- 解决了导入问题：
  - 路由器不再依赖不存在的 `utils` 模块；相关函数已内联
  - 协调器使用相对导入 (`from .specialists import ...`)，通过模块路径调用
  - VS Code/Pylance 配置解决了 `chainlit` 和包导入问题
- 修正了 `STUDY_GUIDE.md` 中的一个小拼写错误，并新增模块 08 的覆盖内容

### 移除
- 删除了未使用的 `Module08/infra/obs.py`，并移除了空的 `infra/` 目录；文档中保留了可选的可观测性模式

### 移动
- 将模块 08 的演示整合到 `Module08/samples` 中，并按课程编号创建文件夹
  - 将 Chainlit 应用移至 `samples/04`
  - 将代理移至 `samples/05`，并新增 `__init__.py` 文件以支持包解析

### 文档
- 模块 08 的课程文档和所有示例 README 增加了 Microsoft Learn 和可信供应商的参考资料
- 更新了 `Module08/README.md`，新增示例概览、路由器配置和验证提示
- 验证了 `Module07/README.md` 中的 Windows Foundry Local 部分与 Learn 文档的一致性
- 更新了 `STUDY_GUIDE.md`：
  - 在概览、时间表和进度追踪中新增模块 08
  - 增加了全面的参考部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 历史记录（摘要）
- 建立了课程架构和模块（模块 01–07）
- 内容逐步现代化、格式标准化，并新增案例研究
- 扩展了优化框架的覆盖范围（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未发布 / 待办事项（建议）
- 为每个示例新增可选的烟雾测试，以验证 Foundry Local 的可用性
- 审核翻译内容以确保模型引用（如 `phi-4-mini`）的一致性
- 如果团队偏好工作区范围的严格性，新增最小的 pyright 配置

---

