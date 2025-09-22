<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T11:48:33+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "zh"
}
-->
# 第1节示例：通过REST进行快速聊天

使用Python `requests`向Foundry Local发送一个最小化的聊天请求。

## 前提条件
- Foundry Local服务运行一个模型（例如，`phi-4-mini`）
- `pip install -r ../../requirements.txt`

## 运行（cmd.exe）
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## 参考资料
- Foundry Local（学习）：https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI兼容API概述：https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

