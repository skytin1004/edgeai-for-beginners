<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T09:34:06+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "zh"
}
-->
# 更新日志

记录了所有与 EdgeAI for Beginners 相关的重要更新。本项目采用基于日期的条目记录，并遵循 Keep a Changelog 风格（新增、变更、修复、移除、文档、迁移）。

## 2025-09-23

### 变更 - 模块 08 重大现代化更新
- **全面对齐 Microsoft Foundry-Local 仓库模式**
  - 更新所有代码示例以使用现代化的 `FoundryLocalManager` 和 OpenAI SDK 集成
  - 用正确的 SDK 替换已弃用的手动 `requests` 调用
  - 实现模式与官方 Microsoft 文档和示例保持一致

- **05.AIPoweredAgents.md 现代化**：
  - 更新多代理编排以使用现代 SDK 模式
  - 使用高级功能（反馈循环、性能监控）增强协调器实现
  - 添加全面的错误处理和服务健康检查
  - 正确引用本地示例文件（`samples/05/multi_agent_orchestration.ipynb`）
  - 更新函数调用示例以使用现代 `tools` 参数替代已弃用的 `functions`
  - 添加生产级模式，包括监控和统计跟踪

- **06.ModelsAsTools.md 完全重写**：
  - 用智能模型路由器实现替代基础工具注册表
  - 添加基于关键词的模型选择，用于不同任务类型（通用、推理、代码、创意）
  - 集成基于环境的配置，支持灵活的模型分配
  - 增强服务健康监控和错误处理功能
  - 添加生产部署模式，包括请求监控和性能跟踪
  - 与本地实现保持一致（`samples/06/router.py` 和 `samples/06/model_router.ipynb`）

- **文档结构改进**：
  - 添加概述部分，突出现代化和 SDK 对齐
  - 使用表情符号和更好的格式提升可读性
  - 在文档中正确引用本地示例文件
  - 包括生产级实现指导和最佳实践

### 新增
- 模块 08 文件中添加全面的概述部分，突出现代 SDK 集成
- 架构亮点，展示高级功能（多代理系统、智能路由）
- 直接引用本地示例实现，提供实践体验
- 生产部署指导，包括监控和错误处理模式
- 交互式 Jupyter notebook 示例，包含高级功能和基准测试

### 修复
- 修复文档与实际示例实现之间的对齐问题
- 修复模块 08 中过时的 SDK 使用模式
- 添加对全面本地示例库的引用
- 修复不同部分之间实现方法的不一致问题

---

## 2025-09-18

### 新增
- 模块 08：Microsoft Foundry Local – 完整开发者工具包
  - 六个课程：设置、Azure AI Foundry 集成、开源模型、前沿演示、代理和模型作为工具
  - 可运行示例位于 `Module08/samples/01`–`06`，附带 Windows cmd 指令
    - `01` REST 快速聊天（`chat_quickstart.py`）
    - `02` SDK 快速入门，支持 OpenAI/Foundry Local 和 Azure OpenAI（`sdk_quickstart.py`）
    - `03` CLI 列表和基准测试（`list_and_bench.cmd`）
    - `04` Chainlit 演示（`app.py`）
    - `05` 多代理编排（`python -m samples.05.agents.coordinator`）
    - `06` 模型作为工具路由器（`router.py`）
- Session 2 SDK 示例中新增 Azure OpenAI 支持，使用环境变量配置
- `.vscode/settings.json` 指向 `Module08/.venv`，提升 Python 分析解析能力
- `.env` 文件中添加 `PYTHONPATH` 提示，支持 VS Code/Pylance 识别

### 变更
- 模块 08 文档和示例中默认模型更新为 `phi-4-mini`；移除剩余的 `phi-3.5` 提及
- 路由器（`Module08/samples/06/router.py`）改进：
  - 通过 `foundry service status` 使用正则表达式解析进行端点发现
  - 启动时进行 `/v1/models` 健康检查
  - 环境可配置的模型注册表（`GENERAL_MODEL`、`REASONING_MODEL`、`CODE_MODEL`、`TOOL_REGISTRY` JSON）
- 需求更新：`Module08/requirements.txt` 现在包括 `openai`（以及 `requests`、`chainlit`）
- Chainlit 示例指导得到明确说明，并添加故障排除；通过工作区设置解决导入问题

### 修复
- 解决导入问题：
  - 路由器不再依赖不存在的 `utils` 模块；相关函数已内联
  - 协调器使用相对导入（`from .specialists import ...`），通过模块路径调用
  - VS Code/Pylance 配置解决 `chainlit` 和包导入问题
- 修正 `STUDY_GUIDE.md` 中的一个小拼写错误，并添加模块 08 的覆盖内容

### 移除
- 删除未使用的 `Module08/infra/obs.py`，并移除空的 `infra/` 目录；文档中保留可选的可观测性模式

### 迁移
- 将模块 08 演示整合到 `Module08/samples` 中，按课程编号分文件夹
  - 将 Chainlit 应用迁移到 `samples/04`
  - 将代理迁移到 `samples/05`，并添加 `__init__.py` 文件以支持包解析

### 文档
- 模块 08 课程文档和所有示例 README 文件丰富了 Microsoft Learn 和可信供应商的参考资料
- 更新 `Module08/README.md`，添加示例概述、路由器配置和验证提示
- 验证 `Module07/README.md` 中的 Windows Foundry Local 部分与 Learn 文档一致
- 更新 `STUDY_GUIDE.md`：
  - 添加模块 08 到概述、时间表和进度追踪器
  - 添加全面的参考部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 历史记录（摘要）
- 建立课程架构和模块（模块 01–07）
- 内容迭代现代化、格式标准化，并添加案例研究
- 扩展优化框架覆盖范围（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未发布 / 待办事项（建议）
- 为每个示例添加可选的冒烟测试，以验证 Foundry Local 可用性
- 审核翻译以对齐模型引用（例如 `phi-4-mini`）
- 如果团队偏好工作区范围的严格性，添加最小的 pyright 配置

---

