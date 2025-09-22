<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T11:49:36+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "zh"
}
-->
# Foundry Local 在 Windows 上的使用指南（已验证）

本指南帮助您在 Windows 上安装、运行和集成 Microsoft Foundry Local。所有步骤和命令均已根据 Microsoft Learn 文档验证。

- 入门指南: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- 架构概述: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI 参考: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- 集成 SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- 编译 HF 模型 (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: 本地与云对比: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) 在 Windows 上安装 / 升级

- 安装:
```cmd
winget install Microsoft.FoundryLocal
```
- 升级:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- 版本检查:
```cmd
foundry --version
```

## 2) CLI 基础知识（三大类别）

- 模型:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- 服务:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- 缓存:
```cmd
foundry cache --help
foundry cache list
```

注意事项:
- 服务提供了一个兼容 OpenAI 的 REST API。端口是动态分配的，可使用 `foundry service status` 来查询。
- 推荐使用 SDKs，它们会自动处理端点发现（在支持的情况下）。

## 3) 查询本地端点（动态端口）

Foundry Local 每次启动服务时都会分配一个动态端口:
```cmd
foundry service status
```
使用报告的 `http://localhost:<PORT>` 作为您的 `base_url`，并结合 OpenAI 兼容路径（例如 `/v1/chat/completions`）。

## 4) 使用 OpenAI Python SDK 快速测试

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
参考资料:
- SDK 集成: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) 自定义模型（使用 Olive 编译）

如果需要使用目录中没有的模型，可以使用 Olive 将其编译为 ONNX 格式以供 Foundry Local 使用。

高层流程（具体步骤请参考文档）:
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
文档:
- BYOM 编译: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) 故障排除

- 检查服务状态和日志:
```cmd
foundry service status
foundry service diag
```
- 清除或移动缓存:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- 更新到最新预览版:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) 相关的 Windows 开发体验

- Windows 本地与云 AI 选择，包括 Foundry Local 和 Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI 工具包与 Foundry Local 集成（使用 `foundry service status` 获取聊天端点 URL）:
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

