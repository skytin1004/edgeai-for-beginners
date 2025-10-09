<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-09T06:54:02+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "ru"
}
-->
# Сессия 3: Модели с открытым исходным кодом в Foundry Local

## Аннотация

Узнайте, как интегрировать модели Hugging Face и другие модели с открытым исходным кодом в Foundry Local. Изучите стратегии выбора, рабочие процессы сообщества, методологию сравнения производительности и способы расширения Foundry с помощью регистрации пользовательских моделей. Эта сессия соответствует еженедельным темам "Model Mondays" и поможет вам оценивать и внедрять модели с открытым исходным кодом локально перед масштабированием на Azure.

## Цели обучения

К концу сессии вы сможете:

- **Открывать и оценивать**: Находить подходящие модели (mistral, gemma, qwen, deepseek), учитывая баланс качества и ресурсов.
- **Загружать и запускать**: Использовать Foundry Local CLI для загрузки, кэширования и запуска моделей сообщества.
- **Проводить тестирование**: Применять согласованные эвристики для оценки задержки, пропускной способности токенов и качества.
- **Расширять**: Регистрировать или адаптировать пользовательский обертку модели, следуя совместимым с SDK шаблонам.
- **Сравнивать**: Создавать структурированные сравнения для выбора между SLM и средними LLM.

## Предварительные требования

- Завершенные сессии 1 и 2
- Среда Python с установленным `foundry-local-sdk`
- Не менее 15 ГБ свободного диска для кэширования нескольких моделей
- Опционально: включенное ускорение GPU/WebGPU (`foundry config list`)

### Быстрый старт в кроссплатформенной среде

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

При тестировании на macOS с использованием хост-сервиса Windows установите:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстрационный процесс (30 минут)

### 1. Загрузка моделей Hugging Face через CLI (8 минут)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Запуск и быстрая проверка (5 минут)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Скрипт для тестирования производительности (8 минут)

Создайте `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Запустите:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Сравнение производительности (5 минут)

Обсудите компромиссы: время загрузки, объем памяти (наблюдайте через Task Manager / `nvidia-smi` / монитор ресурсов ОС), качество вывода против скорости. Используйте Python-скрипт для тестирования производительности (Сессия 3) для оценки задержки и пропускной способности; повторите после включения ускорения GPU.

### 5. Начальный проект (4 минуты)

Создайте генератор отчетов о сравнении моделей (расширьте скрипт тестирования производительности с экспортом в markdown).

## Начальный проект: Расширение `03-huggingface-models`

Улучшите существующий пример, добавив:

1. Агрегацию результатов тестирования + вывод в CSV/Markdown.
2. Реализацию простого качественного оценивания (набор пар запросов + файл для ручной аннотации).
3. Введение JSON-конфигурации (`models.json`) для подключаемого списка моделей и набора запросов.

## Контрольный список для проверки

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Все целевые модели должны появляться и отвечать на запросы в чате.

## Пример сценария и соответствие воркшопу

| Скрипт воркшопа | Сценарий | Цель | Источник запросов / набора данных |
|-----------------|----------|------|----------------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Команда платформы Edge выбирает стандартный SLM для встроенного инструмента суммаризации | Провести сравнение задержки + p95 + токенов/сек среди кандидатов | Встроенная переменная `PROMPT` + список `BENCH_MODELS` из окружения |

### Описание сценария

Инженеры продукта должны выбрать стандартную легковесную модель суммаризации для функции офлайн заметок о встречах. Они проводят контролируемые детерминированные тесты (temperature=0) на фиксированном наборе запросов (см. пример ниже) и собирают метрики задержки и пропускной способности с включенным и отключенным ускорением GPU.

### Пример JSON-набора запросов (расширяемый)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Циклически обрабатывайте каждый запрос для каждой модели, фиксируйте задержку на запрос, чтобы вычислить метрики распределения и выявить выбросы.

## Рамки выбора модели

| Параметр | Метрика | Почему это важно |
|----------|--------|------------------|
| Задержка | среднее / p95 | Стабильность пользовательского опыта |
| Пропускная способность | токенов/сек | Масштабируемость для пакетов и потоков |
| Память | объем резидентной памяти | Соответствие устройству и параллельность |
| Качество | запросы по рубрике | Пригодность для задачи |
| Объем | кэш на диске | Распространение и обновления |
| Лицензия | разрешение на использование | Соответствие коммерческим требованиям |

## Расширение с пользовательской моделью

Общий шаблон (псевдокод):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Обратитесь к официальному репозиторию для актуальных интерфейсов адаптеров:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Устранение неполадок

| Проблема | Причина | Решение |
|----------|--------|---------|
| OOM на mistral-7b | Недостаточно RAM/GPU | Остановите другие модели; попробуйте меньший вариант |
| Медленный первый ответ | Холодная загрузка | Поддерживайте активность с помощью периодического легкого запроса |
| Загрузка зависает | Нестабильность сети | Повторите попытку; предзагрузите в непиковое время |

## Ссылки

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Продолжительность сессии**: 30 минут (+ опциональное углубление)  
**Сложность**: Средний уровень

### Дополнительные улучшения

| Улучшение | Преимущество | Как реализовать |
|-----------|--------------|-----------------|
| Задержка первого токена в потоке | Оценка воспринимаемой отзывчивости | Запустите тест с `BENCH_STREAM=1` (улучшенный скрипт в `Workshop/samples/session03`) |
| Детерминированный режим | Стабильные регрессионные сравнения | `temperature=0`, фиксированный набор запросов, сохранение JSON-выводов под версионным контролем |
| Оценка по рубрике качества | Добавляет качественное измерение | Поддерживайте `prompts.json` с ожидаемыми аспектами; аннотируйте оценки (1–5) вручную или с помощью вторичной модели |
| Экспорт в CSV / Markdown | Удобный для обмена отчет | Расширьте скрипт для записи `benchmark_report.md` с таблицей и основными моментами |
| Теги возможностей модели | Помогает автоматической маршрутизации в будущем | Поддерживайте `models.json` с `{alias: {capabilities:[], size_mb:..}}` |
| Фаза прогрева кэша | Снижение смещения холодного старта | Выполните один прогревочный цикл перед основным тестированием (уже реализовано) |
| Точность по процентилям | Надежная задержка хвоста | Используйте numpy percentile (уже в переработанном скрипте) |
| Приблизительная стоимость токенов | Экономическое сравнение | Приблизительная стоимость = (токенов/сек * среднее количество токенов на запрос) * энергетическая эвристика |
| Автоматическое пропускание неудачных моделей | Устойчивость в пакетных запусках | Оберните каждый тест в try/except и отметьте статус в поле |

#### Минимальный фрагмент для экспорта в Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Пример детерминированного набора запросов

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Циклически обрабатывайте статический список вместо случайных запросов для сопоставимых метрик между коммитами.

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.