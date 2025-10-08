<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-08T14:24:17+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "sr"
}
-->
# Напомене о миграцији Foundry Local SDK

## Преглед

Сви Python фајлови у фасцикли Workshop ажурирани су да прате најновије обрасце из званичног [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Резиме промена

### Основна инфраструктура (`workshop_utils.py`)

#### Побољшане функције:
- **Подршка за замену крајње тачке**: Додата подршка за променљиву окружења `FOUNDRY_LOCAL_ENDPOINT`
- **Побољшано руковање грешкама**: Боље управљање изузецима са детаљним порукама о грешкама
- **Побољшано кеширање**: Кључеви кеша сада укључују крајњу тачку за сценарије са више крајњих тачака
- **Експоненцијално поновно покретање**: Логика поновног покушаја сада користи експоненцијално поновно покретање за бољу поузданост
- **Анотације типова**: Додате свеобухватне анотације типова за бољу подршку у IDE-у

#### Нове могућности:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Пример апликација

#### Сесија 01: Покретање ћаскања (`chat_bootstrap.py`)
- Ажуриран подразумевани модел са `phi-3.5-mini` на `phi-4-mini`
- Додата подршка за замену крајње тачке
- Побољшана документација са референцама на SDK

#### Сесија 02: RAG Платформа (`rag_pipeline.py`)
- Ажурирано да користи `phi-4-mini` као подразумевани модел
- Додата подршка за замену крајње тачке
- Побољшана документација са детаљима о променљивим окружења

#### Сесија 02: Оцена RAG-а (`rag_eval_ragas.py`)
- Ажурирани подразумевани модели
- Додата конфигурација крајње тачке
- Побољшано руковање грешкама

#### Сесија 03: Бенчмаркинг (`benchmark_oss_models.py`)
- Ажурирана подразумевана листа модела да укључује `phi-4-mini`
- Додата свеобухватна документација о променљивим окружења
- Побољшана документација функција
- Додата подршка за замену крајње тачке

#### Сесија 04: Поређење модела (`model_compare.py`)
- Ажуриран подразумевани LLM са `gpt-oss-20b` на `qwen2.5-7b`
- Додата конфигурација крајње тачке
- Побољшана документација

#### Сесија 05: Оркестрација више агената (`agents_orchestrator.py`)
- Додате анотације типова (промењено `str | None` у `Optional[str]`)
- Побољшана документација класе Agent
- Додата подршка за замену крајње тачке
- Побољшан образац иницијализације

#### Сесија 06: Рутер модела (`models_router.py`)
- Додата конфигурација крајње тачке
- Побољшана документација детекције намере
- Побољшана документација логике рутирања

#### Сесија 06: Платформа (`models_pipeline.py`)
- Додата свеобухватна документација функција
- Побољшана документација корак по корак
- Побољшано руковање грешкама

### Скрипте

#### Извоз бенчмарка (`export_benchmark_markdown.py`)
- Додата подршка за замену крајње тачке
- Ажурирани подразумевани модели
- Побољшана документација функција
- Побољшано руковање грешкама

#### CLI Линтер (`lint_markdown_cli.py`)
- Додате референце на SDK
- Побољшана документација о коришћењу

### Тестови

#### Smoke тестови (`smoke.py`)
- Додата подршка за замену крајње тачке
- Побољшана документација
- Побољшана документација тест случајева
- Боље извештавање о грешкама

## Променљиве окружења

Сви примери сада подржавају ове променљиве окружења:

### Основна конфигурација
- `FOUNDRY_LOCAL_ALIAS` - Алијас модела који се користи (подразумевано зависи од примера)
- `FOUNDRY_LOCAL_ENDPOINT` - Замена крајње тачке услуге (опционо)
- `SHOW_USAGE` - Приказ статистике коришћења токена (подразумевано: "0")
- `RETRY_ON_FAIL` - Омогућавање логике поновног покушаја (подразумевано: "1")
- `RETRY_BACKOFF` - Почетно кашњење поновног покушаја у секундама (подразумевано: "1.0")

### Специфично за пример
- `EMBED_MODEL` - Модел за уграђивање за RAG примере
- `BENCH_MODELS` - Модели одвојени зарезом за бенчмаркинг
- `BENCH_ROUNDS` - Број рунди бенчмаркинга
- `BENCH_PROMPT` - Тестни упит за бенчмаркове
- `BENCH_STREAM` - Мерење кашњења првог токена
- `RAG_QUESTION` - Тестно питање за RAG примере
- `AGENT_MODEL_PRIMARY` - Примарни модел агента
- `AGENT_MODEL_EDITOR` - Модел агента уредника
- `SLM_ALIAS` - Алијас за мали језички модел
- `LLM_ALIAS` - Алијас за велики језички модел

## Примењене најбоље праксе SDK-а

### 1. Правилна иницијализација клијента
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Преузимање информација о моделу
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Руковање грешкама
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Логика поновног покушаја са експоненцијалним поновним покретањем
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Подршка за стриминг
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Водич за миграцију прилагођених примера

Ако креирате нове примере или ажурирате постојеће:

1. **Користите помоћне функције из `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Подржите замену крајње тачке**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Додајте свеобухватну документацију**:
   - Променљиве окружења у docstring
   - Референца на SDK
   - Примери коришћења

4. **Користите анотације типова**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Примените правилно руковање грешкама**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Тестирање

Сви примери могу се тестирати са:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
python Workshop/samples/session01/chat_bootstrap.py "Test question"
python Workshop/samples/session02/rag_pipeline.py

# Run benchmark
python Workshop/samples/session03/benchmark_oss_models.py

# Run smoke tests
python -m Workshop.tests.smoke
```

## Референце за документацију SDK-а

- **Главни репозиторијум**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API документација**: Погледајте SDK репозиторијум за најновију документацију API-ја

## Промене које прекидају компатибилност

### Ниједна није очекивана
Све промене су уназад компатибилне. Ажурирања углавном:
- Додају нове опционе функције (замена крајње тачке)
- Побољшавају руковање грешкама
- Унапређују документацију
- Ажурирају подразумевана имена модела на тренутне препоруке

### Опционална побољшања
Можда ћете желети да ажурирате свој код да користи:
- `FOUNDRY_LOCAL_ENDPOINT` за експлицитну контролу крајње тачке
- `SHOW_USAGE=1` за видљивост коришћења токена
- Ажуриране подразумеване моделе (`phi-4-mini` уместо `phi-3.5-mini`)

## Уобичајени проблеми и решења

### Проблем: "Неуспешна иницијализација клијента"
**Решење**: Уверите се да је Foundry Local услуга покренута:
```bash
foundry service start
foundry model run phi-4-mini
```

### Проблем: "Модел није пронађен"
**Решење**: Проверите доступне моделе:
```bash
foundry model list
```

### Проблем: Грешке у повезивању са крајњом тачком
**Решење**: Проверите крајњу тачку:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Следећи кораци

1. **Ажурирајте Module08 примере**: Примените сличне обрасце на Module08/samples
2. **Додајте интеграционе тестове**: Креирајте свеобухватан сет тестова
3. **Бенчмаркинг перформанси**: Упоредите перформансе пре и после
4. **Ажурирање документације**: Ажурирајте главни README са новим обрасцима

## Упутства за допринос

Када додајете нове примере:
1. Користите `workshop_utils.py` за конзистентност
2. Пратите образац у постојећим примерима
3. Додајте свеобухватне docstring-ове
4. Укључите референце на SDK
5. Подржите замену крајње тачке
6. Додајте одговарајуће анотације типова
7. Укључите примере коришћења у docstring

## Компатибилност верзија

Ова ажурирања су компатибилна са:
- `foundry-local-sdk` (најновија верзија)
- `openai>=1.30.0`
- Python 3.8+

---

**Последње ажурирање**: 2025-01-08  
**Одговоран**: EdgeAI Workshop тим  
**Верзија SDK-а**: Foundry Local SDK (најновија 0.7.117+67073234e7)

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.