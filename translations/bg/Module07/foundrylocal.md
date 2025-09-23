<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-23T01:22:45+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "bg"
}
-->
# Foundry Local на Windows (Проверено)

Това ръководство ви помага да инсталирате, стартирате и интегрирате Microsoft Foundry Local на Windows. Всички стъпки и команди са проверени спрямо документацията на Microsoft Learn.

- Започнете: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Архитектура: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Референция: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Интегриране на SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Компилиране на HF модели (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Локално срещу облачно: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Инсталиране / Актуализиране на Windows

- Инсталиране:
```cmd
winget install Microsoft.FoundryLocal
```
- Актуализиране:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Проверка на версията:
```cmd
foundry --version
```

## 2) Основи на CLI (Три категории)

- Модел:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Услуга:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Кеш:
```cmd
foundry cache --help
foundry cache list
```

Бележки:
- Услугата предоставя REST API, съвместим с OpenAI. Портът на крайната точка се задава динамично; използвайте `foundry service status`, за да го откриете.
- Използвайте SDKs за удобство; те автоматично откриват крайни точки, където е възможно.

## 3) Откриване на локалната крайна точка (Динамичен порт)

Foundry Local задава динамичен порт всеки път, когато услугата стартира:
```cmd
foundry service status
```
Използвайте докладвания `http://localhost:<PORT>` като ваш `base_url` със съвместими с OpenAI пътища (например, `/v1/chat/completions`).

## 4) Бърз тест чрез OpenAI Python SDK

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
Референции:
- Интеграция на SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Донесете свой собствен модел (Компилиране с Olive)

Ако ви е необходим модел, който не е в каталога, компилирайте го в ONNX за Foundry Local, използвайки Olive.

Общ преглед на процеса (вижте документацията за стъпки):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Документация:
- Компилиране на BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Отстраняване на проблеми

- Проверка на статус и логове на услугата:
```cmd
foundry service status
foundry service diag
```
- Изчистване или преместване на кеша:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Актуализиране до последната предварителна версия:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Свързано с Windows Developer Experience

- Избор между локално и облачно AI на Windows, включително Foundry Local и Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit с Foundry Local (използвайте `foundry service status`, за да получите URL на крайна точка за чат):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

