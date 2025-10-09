<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-09T06:40:43+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ru"
}
-->
# Краткое руководство по началу работы с воркшопом

## Предварительные требования

### 1. Установите Foundry Local

Следуйте официальному руководству по установке:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Установите зависимости Python

Из директории воркшопа:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Запуск примеров воркшопа

### Сессия 01: Базовый чат

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**Переменные окружения:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Сессия 02: RAG Pipeline

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**Переменные окружения:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Сессия 02: Оценка RAG (Ragas)

```bash
python rag_eval_ragas.py
```

**Примечание**: Требуются дополнительные зависимости, установленные через `requirements.txt`

### Сессия 03: Бенчмаркинг

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**Переменные окружения:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Вывод**: JSON с метриками задержки, пропускной способности и времени первого токена

### Сессия 04: Сравнение моделей

```bash
cd Workshop/samples/session04
python model_compare.py
```

**Переменные окружения:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Сессия 05: Оркестрация мульти-агентов

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**Переменные окружения:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Сессия 06: Маршрутизатор моделей

```bash
cd Workshop/samples/session06
python models_router.py
```

**Тестирует логику маршрутизации** для нескольких намерений (код, резюмирование, классификация)

### Сессия 06: Конвейер

```bash
python models_pipeline.py
```

**Сложный многоэтапный конвейер** с планированием, выполнением и уточнением

## Скрипты

### Экспорт отчета о бенчмарке

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Вывод**: Таблица в формате Markdown + метрики в формате JSON

### Проверка CLI шаблонов в Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Цель**: Обнаружение устаревших CLI шаблонов в документации

## Тестирование

### Smoke-тесты

```bash
cd Workshop
python -m tests.smoke
```

**Тесты**: Основная функциональность ключевых примеров

## Устранение неполадок

### Сервис не запущен

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Ошибки импорта модулей

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Ошибки подключения

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Модель не найдена

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Справочник переменных окружения

### Основная конфигурация
| Переменная | Значение по умолчанию | Описание |
|------------|-----------------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Различается | Псевдоним модели для использования |
| `FOUNDRY_LOCAL_ENDPOINT` | Авто | Переопределение конечной точки сервиса |
| `SHOW_USAGE` | `0` | Показ статистики использования токенов |
| `RETRY_ON_FAIL` | `1` | Включение логики повторных попыток |
| `RETRY_BACKOFF` | `1.0` | Начальная задержка перед повторной попыткой (в секундах) |

### Для конкретных сессий
| Переменная | Значение по умолчанию | Описание |
|------------|-----------------------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Модель для создания эмбеддингов |
| `RAG_QUESTION` | См. пример | Тестовый вопрос для RAG |
| `BENCH_MODELS` | Различается | Список моделей через запятую |
| `BENCH_ROUNDS` | `3` | Количество итераций бенчмарка |
| `BENCH_PROMPT` | См. пример | Запрос для бенчмарка |
| `BENCH_STREAM` | `0` | Измерение задержки первого токена |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Основная модель агента |
| `AGENT_MODEL_EDITOR` | Primary | Модель агента-редактора |
| `SLM_ALIAS` | `phi-4-mini` | Модель малого языка |
| `LLM_ALIAS` | `qwen2.5-7b` | Модель большого языка |
| `COMPARE_PROMPT` | См. пример | Запрос для сравнения |

## Рекомендуемые модели

### Разработка и тестирование
- **phi-4-mini** - Сбалансированное качество и скорость
- **qwen2.5-0.5b** - Очень быстрая для классификации
- **gemma-2-2b** - Хорошее качество, умеренная скорость

### Производственные сценарии
- **phi-4-mini** - Универсальная модель
- **deepseek-coder-1.3b** - Генерация кода
- **qwen2.5-7b** - Высококачественные ответы

## Документация SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Получение помощи

1. Проверьте статус сервиса: `foundry service status`  
2. Просмотрите логи: Проверьте логи сервиса Foundry Local  
3. Ознакомьтесь с документацией SDK: https://github.com/microsoft/Foundry-Local  
4. Изучите примеры кода: Все примеры содержат подробные комментарии

## Следующие шаги

1. Пройдите все сессии воркшопа по порядку  
2. Экспериментируйте с различными моделями  
3. Модифицируйте примеры под свои задачи  
4. Ознакомьтесь с `SDK_MIGRATION_NOTES.md` для изучения сложных шаблонов

---

**Последнее обновление**: 08.01.2025  
**Версия воркшопа**: Последняя  
**SDK**: Foundry Local Python SDK  

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.