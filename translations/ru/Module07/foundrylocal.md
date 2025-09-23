<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T14:26:33+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "ru"
}
-->
# Foundry Local на Windows (Проверено)

Этот гид поможет вам установить, запустить и интегрировать Microsoft Foundry Local на Windows. Все шаги и команды проверены в документации Microsoft Learn.

- Начало работы: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Архитектура: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Справочник CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Интеграция SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Компиляция моделей HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Локально vs Облако: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Установка / Обновление на Windows

- Установка:
```cmd
winget install Microsoft.FoundryLocal
```
- Обновление:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Проверка версии:
```cmd
foundry --version
```

## 2) Основы CLI (Три категории)

- Модель:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Сервис:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Кэш:
```cmd
foundry cache --help
foundry cache list
```

Примечания:
- Сервис предоставляет REST API, совместимый с OpenAI. Порт конечной точки выделяется динамически; используйте `foundry service status`, чтобы узнать его.
- Для удобства используйте SDK; они автоматически определяют конечную точку там, где это поддерживается.

## 3) Определение локальной конечной точки (Динамический порт)

Foundry Local выделяет динамический порт каждый раз при запуске сервиса:
```cmd
foundry service status
```
Используйте указанный `http://localhost:<PORT>` как ваш `base_url` с путями, совместимыми с OpenAI (например, `/v1/chat/completions`).

## 4) Быстрая проверка через OpenAI Python SDK

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
Ссылки:
- Интеграция SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Использование собственной модели (Компиляция с Olive)

Если вам нужна модель, которой нет в каталоге, скомпилируйте её в ONNX для Foundry Local с помощью Olive.

Общий процесс (см. документацию для шагов):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Документация:
- Компиляция BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Устранение неполадок

- Проверка статуса сервиса и логов:
```cmd
foundry service status
foundry service diag
```
- Очистка или перемещение кэша:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Обновление до последней версии:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Связанный опыт разработки на Windows

- Выбор между локальным и облачным AI на Windows, включая Foundry Local и Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- AI Toolkit для VS Code с Foundry Local (используйте `foundry service status`, чтобы получить URL конечной точки для чата):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

