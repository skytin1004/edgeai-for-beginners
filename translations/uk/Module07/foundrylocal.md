<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-23T01:23:37+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "uk"
}
-->
# Foundry Local на Windows (Перевірено)

Цей посібник допоможе вам встановити, запустити та інтегрувати Microsoft Foundry Local на Windows. Усі кроки та команди перевірені відповідно до документації Microsoft Learn.

- Початок роботи: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Архітектура: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Довідка CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Інтеграція SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Компіляція моделей HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Локально vs Хмара: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Встановлення / Оновлення на Windows

- Встановлення:
```cmd
winget install Microsoft.FoundryLocal
```
- Оновлення:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Перевірка версії:
```cmd
foundry --version
```

## 2) Основи CLI (Три категорії)

- Модель:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Сервіс:
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

Примітки:
- Сервіс надає REST API, сумісний з OpenAI. Порт для доступу виділяється динамічно; використовуйте `foundry service status`, щоб дізнатися його.
- Використовуйте SDK для зручності; вони автоматично визначають кінцеву точку там, де це підтримується.

## 3) Визначення локальної кінцевої точки (Динамічний порт)

Foundry Local призначає динамічний порт кожного разу, коли сервіс запускається:
```cmd
foundry service status
```
Використовуйте вказаний `http://localhost:<PORT>` як ваш `base_url` із шляхами, сумісними з OpenAI (наприклад, `/v1/chat/completions`).

## 4) Швидкий тест через OpenAI Python SDK

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
Посилання:
- Інтеграція SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Використання власної моделі (Компілірування за допомогою Olive)

Якщо вам потрібна модель, якої немає в каталозі, скомпілюйте її в ONNX для Foundry Local за допомогою Olive.

Загальний процес (див. документацію для деталей):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Документація:
- Компіляція BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Вирішення проблем

- Перевірка статусу сервісу та журналів:
```cmd
foundry service status
foundry service diag
```
- Очищення або переміщення кешу:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Оновлення до останньої попередньої версії:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Супутній досвід розробника на Windows

- Вибір між локальним та хмарним AI на Windows, включаючи Foundry Local та Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- AI Toolkit для VS Code із Foundry Local (використовуйте `foundry service status`, щоб отримати URL кінцевої точки для чату):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

