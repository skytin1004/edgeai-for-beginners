<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T16:57:11+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "mo"
}
-->
# 第六節範例：模型作為工具

此範例實現了一個簡單的路由器和工具註冊表，根據使用者的提示選擇模型，並調用 Foundry Local 的 OpenAI 兼容端點。

## 文件
- `router.py`：簡單的註冊表和啟發式路由；端點發現和健康檢查。

## 執行 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## 注意事項
- 路由器使用簡單的關鍵字啟發式方法在 `general`、`reasoning` 和 `code` 工具之間進行選擇，並在啟動時打印 `/v1/models`。
- 通過環境變數進行配置：
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

## 參考資料
- Foundry Local (學習)：https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- 與推理 SDK 整合：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

