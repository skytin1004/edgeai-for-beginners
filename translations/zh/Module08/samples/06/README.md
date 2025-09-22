<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T11:48:55+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "zh"
}
-->
# 第6节示例：将模型作为工具使用

此示例实现了一个最简化的路由器和工具注册表，根据用户提示选择模型，并调用 Foundry Local 的 OpenAI 兼容端点。

## 文件
- `router.py`：简单的注册表和启发式路由；端点发现和健康检查。

## 运行（cmd.exe）
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## 注意事项
- 路由器使用简单的关键词启发式方法，在 `general`、`reasoning` 和 `code` 工具之间进行选择，并在启动时打印 `/v1/models`。
- 可通过环境变量进行配置：
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-distill-qwen-7b"},"code":{"model":"qwen2.5-7b-instruct"}}
```

## 参考资料
- Foundry Local（学习）：https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- 与推理 SDK 集成：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

