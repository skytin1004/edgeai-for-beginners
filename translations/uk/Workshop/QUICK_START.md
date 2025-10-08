<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-08T11:58:38+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "uk"
}
-->
# Швидкий старт для воркшопу

## Попередні умови

### 1. Встановіть Foundry Local

Скористайтеся офіційним посібником з установки:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Встановіть залежності Python

З каталогу воркшопу:

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

## Запуск прикладів воркшопу

### Сесія 01: Базовий чат

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**Змінні середовища:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Сесія 02: RAG Pipeline

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**Змінні середовища:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Сесія 02: Оцінка RAG (Ragas)

```bash
python rag_eval_ragas.py
```

**Примітка**: Потребує додаткових залежностей, встановлених через `requirements.txt`

### Сесія 03: Бенчмаркінг

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**Змінні середовища:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Вихідні дані**: JSON з метриками затримки, пропускної здатності та першого токена

### Сесія 04: Порівняння моделей

```bash
cd Workshop/samples/session04
python model_compare.py
```

**Змінні середовища:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Сесія 05: Оркестрація мультиагентів

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**Змінні середовища:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Сесія 06: Маршрутизатор моделей

```bash
cd Workshop/samples/session06
python models_router.py
```

**Тестує логіку маршрутизації** для кількох намірів (код, резюмування, класифікація)

### Сесія 06: Конвеєр

```bash
python models_pipeline.py
```

**Складний багатокроковий конвеєр** з плануванням, виконанням і вдосконаленням

## Скрипти

### Експорт звіту бенчмаркінгу

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Вихідні дані**: Таблиця Markdown + JSON метрики

### Перевірка CLI шаблонів у Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Призначення**: Виявлення застарілих CLI шаблонів у документації

## Тестування

### Smoke Tests

```bash
cd Workshop
python -m tests.smoke
```

**Тести**: Основна функціональність ключових прикладів

## Вирішення проблем

### Сервіс не працює

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Помилки імпорту модулів

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Помилки з'єднання

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Модель не знайдена

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Довідник змінних середовища

### Основна конфігурація
| Змінна | За замовчуванням | Опис |
|--------|------------------|------|
| `FOUNDRY_LOCAL_ALIAS` | Змінюється | Псевдонім моделі для використання |
| `FOUNDRY_LOCAL_ENDPOINT` | Авто | Перевизначення кінцевої точки сервісу |
| `SHOW_USAGE` | `0` | Показати статистику використання токенів |
| `RETRY_ON_FAIL` | `1` | Увімкнути логіку повторних спроб |
| `RETRY_BACKOFF` | `1.0` | Початкова затримка повторної спроби (секунди) |

### Специфічні для сесій
| Змінна | За замовчуванням | Опис |
|--------|------------------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Модель для вбудовування |
| `RAG_QUESTION` | Див. приклад | Тестове питання для RAG |
| `BENCH_MODELS` | Змінюється | Моделі через кому |
| `BENCH_ROUNDS` | `3` | Ітерації бенчмаркінгу |
| `BENCH_PROMPT` | Див. приклад | Підказка для бенчмаркінгу |
| `BENCH_STREAM` | `0` | Вимірювання затримки першого токена |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Основна модель агента |
| `AGENT_MODEL_EDITOR` | Основна | Модель редактора агента |
| `SLM_ALIAS` | `phi-4-mini` | Мала мовна модель |
| `LLM_ALIAS` | `qwen2.5-7b` | Велика мовна модель |
| `COMPARE_PROMPT` | Див. приклад | Підказка для порівняння |

## Рекомендовані моделі

### Розробка та тестування
- **phi-4-mini** - Збалансована якість і швидкість
- **qwen2.5-0.5b** - Дуже швидка для класифікації
- **gemma-2-2b** - Хороша якість, помірна швидкість

### Виробничі сценарії
- **phi-4-mini** - Універсальна модель
- **deepseek-coder-1.3b** - Генерація коду
- **qwen2.5-7b** - Високоякісні відповіді

## Документація SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Отримання допомоги

1. Перевірте статус сервісу: `foundry service status`
2. Перегляньте логи: Перевірте логи сервісу Foundry Local
3. Ознайомтеся з документацією SDK: https://github.com/microsoft/Foundry-Local
4. Перегляньте приклади коду: Усі приклади мають детальні коментарі

## Наступні кроки

1. Завершіть усі сесії воркшопу по порядку
2. Експериментуйте з різними моделями
3. Модифікуйте приклади для ваших потреб
4. Ознайомтеся з `SDK_MIGRATION_NOTES.md` для складних шаблонів

---

**Останнє оновлення**: 2025-01-08  
**Версія воркшопу**: Остання  
**SDK**: Foundry Local Python SDK

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.