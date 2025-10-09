<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-09T06:56:57+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "ru"
}
-->
# Сессия 6: Foundry Local – Модели как инструменты

## Аннотация

Рассматривайте модели как составные инструменты внутри локального операционного слоя ИИ. В этой сессии вы узнаете, как связывать несколько специализированных вызовов SLM/LLM, избирательно направлять задачи и предоставлять унифицированный интерфейс SDK для приложений. Вы создадите легковесный маршрутизатор моделей + планировщик задач, интегрируете его в скрипт приложения и наметите путь масштабирования до Azure AI Foundry для рабочих нагрузок в производстве.

## Цели обучения

- **Понять концепцию** моделей как атомарных инструментов с заявленными возможностями
- **Маршрутизировать** запросы на основе намерений / эвристической оценки
- **Связывать** результаты для выполнения многошаговых задач (разложение → решение → уточнение)
- **Интегрировать** унифицированный клиентский API для приложений
- **Масштабировать** дизайн в облако (с тем же контрактом, совместимым с OpenAI)

## Предварительные требования

- Завершены сессии 1–5
- Кэшировано несколько локальных моделей (например, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Фрагмент для кроссплатформенной среды

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Удаленный доступ/доступ к виртуальной машине с macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстрационный процесс (30 минут)

### 1. Объявление возможностей инструмента (5 минут)

Создайте файл `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Определение намерений и маршрутизация (8 минут)

Создайте файл `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Связывание многошаговых задач (7 минут)

Создайте файл `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Стартовый проект: адаптация `06-models-as-tools` (5 минут)

Улучшения:
- Добавьте поддержку потоковой передачи токенов (постепенное обновление интерфейса)
- Добавьте оценку уверенности: лексическое совпадение или рубрика подсказок
- Экспортируйте JSON трассировки (намерение → модель → задержка → использование токенов)
- Реализуйте повторное использование кэша для повторяющихся подзадач

### 5. Путь масштабирования до Azure (5 минут)

| Уровень | Локально (Foundry) | Облако (Azure AI Foundry) | Стратегия перехода |
|---------|---------------------|---------------------------|--------------------|
| Маршрутизация | Эвристика на Python | Устойчивый микросервис | Контейнеризация и развертывание API |
| Модели | Кэшированные SLM | Управляемые развертывания | Сопоставление локальных имен с ID развертываний |
| Наблюдаемость | CLI статистика/вручную | Централизованный логгинг и метрики | Добавление структурированных событий трассировки |
| Безопасность | Только локальный хост | Аутентификация Azure / сеть | Введение хранилища ключей для секретов |
| Стоимость | Ресурсы устройства | Оплата за использование | Добавление ограничений бюджета |

## Контрольный список для проверки

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Ожидается выбор модели на основе намерений и окончательный уточненный результат.

## Устранение неполадок

| Проблема | Причина | Решение |
|----------|---------|---------|
| Все задачи направляются в одну и ту же модель | Слабые правила | Расширьте набор регулярных выражений INTENT_RULES |
| Сбой конвейера на промежуточном этапе | Модель не загружена | Выполните `foundry model run <model>` |
| Низкая согласованность вывода | Отсутствует этап уточнения | Добавьте этап суммирования/валидации |

## Ссылки

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Документация Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Шаблоны качества подсказок: см. Сессию 2

---

**Продолжительность сессии**: 30 минут  
**Сложность**: Эксперт

## Пример сценария и соответствие воркшопу

| Скрипты / ноутбуки воркшопа | Сценарий | Цель | Источник данных / каталог |
|-----------------------------|----------|------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Помощник разработчика, обрабатывающий запросы с разными намерениями (рефакторинг, суммирование, классификация) | Эвристическое определение намерений → маршрутизация по псевдонимам моделей с учетом использования токенов | Встроенный `CATALOG` + регулярные выражения `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Многошаговое планирование и уточнение для сложной задачи помощи в кодировании | Разложение → специализированное выполнение → этап уточнения суммирования | Тот же `CATALOG`; шаги выведены из результата планирования |

### Описание сценария
Инструмент для повышения производительности разработчиков получает разнородные задачи: рефакторинг кода, суммирование архитектурных заметок, классификация отзывов. Чтобы минимизировать задержки и использование ресурсов, небольшая общая модель планирует и суммирует, специализированная модель для кода выполняет рефакторинг, а легковесная модель для классификации помечает отзывы. Скрипт конвейера демонстрирует связывание + уточнение; скрипт маршрутизатора изолирует адаптивную маршрутизацию для одного запроса.

### Снимок каталога
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Примеры тестовых запросов
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Расширение трассировки (опционально)
Добавьте строки JSON трассировки для каждого шага в `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Эвристика эскалации (идея)
Если план содержит ключевые слова, такие как "оптимизация", "безопасность", или длина шага > 280 символов → эскалация до более крупной модели (например, `gpt-oss-20b`) только для этого шага.

### Дополнительные улучшения

| Область | Улучшение | Ценность | Подсказка |
|---------|-----------|----------|-----------|
| Кэширование | Повторное использование объектов менеджера и клиента | Снижение задержек, меньше накладных расходов | Используйте `workshop_utils.get_client` |
| Метрики использования | Захват токенов и задержки на каждом шаге | Профилирование и оптимизация | Измеряйте время каждого вызова маршрута; сохраняйте в список трассировки |
| Адаптивная маршрутизация | Учет уверенности / стоимости | Лучший баланс качества и стоимости | Добавьте оценку: если запрос > N символов или регулярное выражение совпадает с доменом → эскалация до более крупной модели |
| Динамический реестр возможностей | Горячая перезагрузка каталога | Без перезапуска и повторного развертывания | Загружайте `catalog.json` во время выполнения; отслеживайте временную метку файла |
| Стратегия резервирования | Устойчивость при сбоях | Более высокая доступность | Попробуйте основную модель → при исключении используйте резервный псевдоним |
| Потоковый конвейер | Ранний отклик | Улучшение UX | Потоковая передача каждого шага и буферизация входных данных для окончательного уточнения |
| Векторные встраивания намерений | Более точная маршрутизация | Более высокая точность намерений | Встраивайте запрос, группируйте и сопоставляйте центроид → возможность |
| Экспорт трассировки | Аудит цепочки | Соответствие/отчетность | Выводите строки JSON: шаг, намерение, модель, задержка_ms, токены |
| Симуляция стоимости | Оценка перед переходом в облако | Планирование бюджета | Назначьте условную стоимость/токен для каждой модели и агрегируйте по задаче |
| Детерминированный режим | Воспроизводимость | Стабильное тестирование | Env: `temperature=0`, фиксированное количество шагов |

#### Пример структуры трассировки

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Эскиз адаптивной эскалации

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Горячая перезагрузка каталога моделей

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```


Итеративно улучшайте — избегайте излишней сложности на ранних этапах прототипирования.

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.