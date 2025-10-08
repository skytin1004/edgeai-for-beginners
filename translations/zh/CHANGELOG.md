<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T15:59:45+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "zh"
}
-->
# 更新日志

记录了所有与 EdgeAI for Beginners 项目相关的重要更新。本项目采用基于日期的条目记录，并遵循 Keep a Changelog 风格（新增、变更、修复、移除、文档、迁移）。

## 2025-10-08

### 新增 - 工作坊全面更新
- **工作坊 README.md 完整重写**：
  - 增加了全面介绍，阐述 Edge AI 的价值主张（隐私、性能、成本）
  - 创建了 6 个核心学习目标及详细能力要求
  - 添加了学习成果表，包括交付物和能力矩阵
  - 包含了行业相关的职业技能部分
  - 增加了快速入门指南，包括前置条件和三步设置流程
  - 创建了 Python 示例资源表（8 个文件及运行时间）
  - 添加了 Jupyter notebooks 表（8 个笔记本及难度评级）
  - 创建了文档表（7 个关键文档及“使用场景”指导）
  - 提供了针对不同技能水平的学习路径推荐

- **工作坊验证和测试基础设施**：
  - 创建了 `scripts/validate_samples.py` - 用于语法、导入和最佳实践的全面验证工具
  - 创建了 `scripts/test_samples.py` - 用于所有 Python 示例的冒烟测试运行器
  - 在 `scripts/README.md` 中添加了验证文档

- **全面文档**：
  - 创建了 `SAMPLES_UPDATE_SUMMARY.md` - 400+ 行的详细指南，涵盖所有改进
  - 创建了 `UPDATE_COMPLETE.md` - 更新完成的执行摘要
  - 创建了 `QUICK_REFERENCE.md` - 工作坊的快速参考卡片

### 变更 - 工作坊 Python 示例现代化
- **所有 8 个 Python 示例更新为最佳实践**：
  - 增强了所有 I/O 操作的错误处理，添加了 try-except 块
  - 添加了类型提示和全面的文档字符串
  - 实现了统一的 [INFO]/[ERROR]/[RESULT] 日志模式
  - 为可选导入添加了安装提示保护
  - 改进了所有示例中的用户反馈

- **session01/chat_bootstrap.py**：
  - 增强了客户端初始化，提供全面的错误信息
  - 改进了流式错误处理，增加了块验证
  - 添加了服务不可用的更好异常处理

- **session02/rag_pipeline.py**：
  - 为 sentence-transformers 添加了导入保护及安装提示
  - 增强了嵌入和生成操作的错误处理
  - 改进了输出格式，提供结构化结果

- **session02/rag_eval_ragas.py**：
  - 为可选导入（ragas、datasets）添加了用户友好的错误信息保护
  - 添加了评估指标的错误处理
  - 改进了评估结果的输出格式

- **session03/benchmark_oss_models.py**：
  - 实现了优雅降级（在模型失败时继续运行）
  - 添加了详细的进度报告和每个模型的错误处理
  - 增强了统计计算，提供全面的错误恢复

- **session04/model_compare.py**：
  - 添加了类型提示（元组返回类型）
  - 改进了输出格式，提供结构化 JSON 结果
  - 实现了每个模型的错误处理及恢复

- **session05/agents_orchestrator.py**：
  - 增强了 Agent.act()，添加了全面的文档字符串
  - 添加了管道错误处理，提供分阶段日志记录
  - 改进了内存管理和状态跟踪

- **session06/models_router.py**：
  - 增强了所有路由组件的函数文档
  - 在 route() 函数中添加了详细日志记录
  - 改进了测试输出，提供结构化结果

- **session06/models_pipeline.py**：
  - 为 chat() 辅助函数添加了错误处理
  - 在 pipeline() 中增强了阶段日志记录和进度报告
  - 在 main() 中改进了全面的错误恢复

### 文档 - 工作坊文档增强
- 更新了主 README.md，突出工作坊部分，强调动手学习路径
- 增强了 STUDY_GUIDE.md，添加了全面的工作坊部分，包括：
  - 学习目标和学习重点领域
  - 自我评估问题
  - 动手练习及时间估算
  - 集中学习和兼职学习的时间分配
  - 在进度跟踪模板中添加了工作坊
- 将时间分配指南从 20 小时更新为 30 小时（包括工作坊）
- 在 README 中添加了工作坊示例描述和学习成果

### 修复
- 解决了工作坊示例中不一致的错误处理模式
- 修复了可选依赖导入错误，添加了适当的保护
- 修正了关键函数中缺失的类型提示
- 解决了错误场景中用户反馈不足的问题
- 修复了验证问题，提供了全面的测试基础设施

---

## 2025-09-23

### 变更 - 模块 08 重大现代化
- **全面对齐 Microsoft Foundry-Local 仓库模式**：
  - 更新了所有代码示例，采用现代 `FoundryLocalManager` 和 OpenAI SDK 集成
  - 用正确的 SDK 使用替换了已弃用的手动 `requests` 调用
  - 实现模式与官方 Microsoft 文档和示例对齐

- **05.AIPoweredAgents.md 现代化**：
  - 更新了多代理编排，采用现代 SDK 模式
  - 增强了协调器实现，添加高级功能（反馈循环、性能监控）
  - 添加了全面的错误处理和服务健康检查
  - 正确引用了本地示例文件（`samples/05/multi_agent_orchestration.ipynb`）
  - 更新了函数调用示例，使用现代 `tools` 参数替代已弃用的 `functions`
  - 添加了生产就绪模式，提供监控和统计跟踪

- **06.ModelsAsTools.md 完整重写**：
  - 用智能模型路由器实现替换了基本工具注册表
  - 添加了基于关键词的模型选择，用于不同任务类型（通用、推理、代码、创意）
  - 集成了基于环境的配置，提供灵活的模型分配
  - 增强了全面的服务健康监控和错误处理
  - 添加了生产部署模式，提供请求监控和性能跟踪
  - 与本地实现对齐（`samples/06/router.py` 和 `samples/06/model_router.ipynb`）

- **文档结构改进**：
  - 添加了概述部分，突出现代化和 SDK 对齐
  - 增强了表情符号和更好的格式，提升可读性
  - 在文档中正确引用了本地示例文件
  - 包含生产就绪实现指导和最佳实践

### 新增
- 模块 08 文件中添加了全面的概述部分，突出现代 SDK 集成
- 架构亮点，展示高级功能（多代理系统、智能路由）
- 直接引用本地示例实现，提供动手体验
- 生产部署指导，包含监控和错误处理模式
- 交互式 Jupyter notebook 示例，包含高级功能和基准测试

### 修复
- 解决了文档与实际示例实现之间的对齐问题
- 修复了模块 08 中过时的 SDK 使用模式
- 补充了对全面本地示例库的引用
- 解决了不同部分之间实现方法的不一致问题

---

## 2025-09-18

### 新增
- 模块 08：Microsoft Foundry Local – 完整开发者工具包
  - 六个会话：设置、Azure AI Foundry 集成、开源模型、前沿演示、代理和模型作为工具
  - 可运行示例位于 `Module08/samples/01`–`06`，附带 Windows cmd 指令
    - `01` REST 快速聊天（`chat_quickstart.py`）
    - `02` SDK 快速入门，支持 OpenAI/Foundry Local 和 Azure OpenAI（`sdk_quickstart.py`）
    - `03` CLI 列表和基准测试（`list_and_bench.cmd`）
    - `04` Chainlit 演示（`app.py`）
    - `05` 多代理编排（`python -m samples.05.agents.coordinator`）
    - `06` 模型作为工具路由器（`router.py`）
- 在会话 2 SDK 示例中支持 Azure OpenAI，提供环境变量配置
- `.vscode/settings.json` 指向 `Module08/.venv`，改进 Python 分析解析
- `.env` 提供 `PYTHONPATH` 提示，支持 VS Code/Pylance 识别

### 变更
- 默认模型更新为 `phi-4-mini`，覆盖模块 08 文档和示例；移除了模块 08 中剩余的 `phi-3.5` 提及
- 路由器（`Module08/samples/06/router.py`）改进：
  - 通过 `foundry service status` 和正则解析进行端点发现
  - 启动时进行 `/v1/models` 健康检查
  - 环境可配置的模型注册表（`GENERAL_MODEL`、`REASONING_MODEL`、`CODE_MODEL`、`TOOL_REGISTRY` JSON）
- 更新了依赖项：`Module08/requirements.txt` 现在包括 `openai`（以及 `requests`、`chainlit`）
- 明确了 Chainlit 示例指导并添加了故障排除；通过工作区设置解决导入问题

### 修复
- 解决了导入问题：
  - 路由器不再依赖不存在的 `utils` 模块；函数已内联
  - 协调器使用相对导入（`from .specialists import ...`），通过模块路径调用
  - VS Code/Pylance 配置解决了 `chainlit` 和包导入问题
- 修正了 `STUDY_GUIDE.md` 中的轻微拼写错误，并添加了模块 08 覆盖内容

### 移除
- 删除了未使用的 `Module08/infra/obs.py`，并移除了空的 `infra/` 目录；可选的可观察性模式保留在文档中

### 迁移
- 将模块 08 演示整合到 `Module08/samples` 中，按会话编号文件夹分类
  - 将 Chainlit 应用移至 `samples/04`
  - 将代理移至 `samples/05`，并添加了 `__init__.py` 文件以支持包解析

### 文档
- 模块 08 会话文档和所有示例 README 增强了 Microsoft Learn 和可信供应商参考
- 更新了 `Module08/README.md`，添加了示例概述、路由器配置和验证提示
- 验证了 `Module07/README.md` 中的 Windows Foundry Local 部分，确保与 Learn 文档一致
- 更新了 `STUDY_GUIDE.md`：
  - 在概述、时间表、进度跟踪器中添加了模块 08
  - 添加了全面的参考部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 历史记录（摘要）
- 建立了课程架构和模块（模块 01–07）
- 内容迭代现代化、格式标准化，并添加了案例研究
- 扩展了优化框架覆盖范围（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未发布 / 待办事项（建议）
- 可选的每个示例冒烟测试以验证 Foundry Local 可用性
- 审核翻译以对齐模型引用（例如 `phi-4-mini`）
- 如果团队偏好工作区范围的严格性，添加最小的 pyright 配置

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。