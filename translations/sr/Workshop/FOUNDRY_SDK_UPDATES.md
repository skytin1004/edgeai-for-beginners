<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T13:58:26+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "sr"
}
-->
# Ажурирања Foundry Local SDK

## Преглед

Ажурирани су Workshop бележници и алати како би правилно користили **званични Foundry Local Python SDK**, пратећи шаблоне из:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Измењене датотеке

### 1. `Workshop/samples/workshop_utils.py`

**Промене:**
- ✅ Додато руковање грешкама приликом увоза пакета `foundry-local-sdk`
- ✅ Побољшана документација са званичним SDK шаблонима
- ✅ Унапређено логовање са Unicode симболима (✓, ✗, ⚠)
- ✅ Додати свеобухватни docstring-ови са примерима
- ✅ Боље поруке о грешкама које упућују на CLI команде
- ✅ Ажурирани коментари у складу са званичном SDK документацијом

**Кључна побољшања:**

#### Руковање грешкама приликом увоза
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Унапређена функција `get_client()`
- Додата детаљна документација о шаблону иницијализације SDK-а
- Објашњено да `FoundryLocalManager` аутоматски покреће сервис
- Разјашњено решавање алијаса модела на хардверски оптимизоване варијанте
- Побољшано логовање са информацијама о крајњој тачки
- Боље поруке о грешкама са предлозима за решавање проблема

#### Унапређена функција `chat_once()`
- Додат свеобухватан docstring са примерима употребе
- Разјашњена компатибилност са OpenAI SDK-ом
- Документована подршка за стриминг (преко kwargs)
- Побољшане поруке о грешкама са предлозима CLI команди
- Додате напомене о провери доступности модела

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Промене:**
- ✅ Ажуриране све markdown ћелије са референцама на SDK
- ✅ Побољшани коментари у коду са објашњењима SDK шаблона
- ✅ Унапређена документација и објашњења у ћелијама
- ✅ Додате смернице за решавање проблема
- ✅ Ажуриран каталог модела (замењен 'gpt-oss-20b' са 'phi-3.5-mini')
- ✅ Боље форматирање излазних података са визуелним индикаторима
- ✅ Додати SDK линкови и референце кроз целу бележницу

**Ажурирања по ћелијама:**

#### Ћелија 1 (Наслов)
- Додати линкови на SDK документацију
- Референцирани званични GitHub репозиторијуми

#### Ћелија 2 (Сценарио)
- Преформатирано са нумерисаним корацима
- Разјашњен шаблон рутирања заснован на намери
- Истакнуте предности локалног извршавања

#### Ћелија 3 (Инсталација зависности)
- Додато објашњење шта сваки пакет пружа
- Документоване могућности SDK-а (решавање алијаса, хардверска оптимизација)

#### Ћелија 4 (Подешавање окружења)
- Побољшани docstring-ови функција
- Додати коментари у коду који објашњавају SDK шаблоне
- Документована структура каталога модела
- Разјашњено подударање приоритета/способности

#### Ћелија 5 (Провера каталога)
- Додати визуелни знаци (✓)
- Боље форматиран излаз

#### Ћелија 6 (Тест детекције намере)
- Преформатиран излаз у стилу табеле
- Приказује и намеру и изабрани модел

#### Ћелија 7 (Функција рутирања)
- Свеобухватно објашњење SDK шаблона
- Документован ток иницијализације
- Наведене све функције (поновни покушај, праћење, грешке)
- Додат линк на SDK референцу

#### Ћелија 8 (Демо у серији)
- Побољшано објашњење шта се може очекивати
- Додат одељак за решавање проблема
- Укључене CLI команде за отклањање грешака
- Боље форматиран приказ излаза

### 3. `Workshop/notebooks/session06_README.md` (Нова датотека)

**Креирана свеобухватна документација која покрива:**

1. **Преглед**: Дијаграм архитектуре и објашњење компоненти
2. **Интеграција SDK-а**: Примери кода који прате званичне шаблоне
3. **Предуслови**: Упутства за подешавање корак по корак
4. **Употреба**: Како покренути и прилагодити бележник
5. **Алијаси модела**: Објашњење хардверски оптимизованих варијанти
6. **Решавање проблема**: Уобичајени проблеми и решења
7. **Проширење**: Како додати намере, моделе и прилагођену логику
8. **Савети за перформансе**: Најбоље праксе за употребу у продукцији
9. **Ресурси**: Линкови на званичну документацију и заједницу

## Имплементација SDK шаблона

### Званични шаблон (из Foundry Local документације)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Наша имплементација (у workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Предности нашег приступа:**
- ✅ Тачно прати званични SDK шаблон
- ✅ Додаје кеширање како би се избегла поновљена иницијализација
- ✅ Укључује логику поновног покушаја за робусност у продукцији
- ✅ Подржава праћење употребе токена
- ✅ Пружа боље поруке о грешкама
- ✅ Остаје компатибилан са званичним примерима

## Промене у каталогу модела

### Пре
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### После
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Разлог:** Замењен 'gpt-oss-20b' (нестандардни алијас) са 'phi-3.5-mini' (званични Foundry Local алијас).

## Зависности

### Ажурирани requirements.txt

Workshop requirements.txt већ укључује:
```
foundry-local-sdk
openai>=1.30.0
```

Ово су једини пакети потребни за интеграцију Foundry Local-а.

## Тестирање ажурирања

### 1. Проверите да ли Foundry Local ради

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Проверите доступне моделе

```bash
foundry model ls
```

Уверите се да су ови модели доступни или ће се аутоматски преузети:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Покрените бележник

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Или га отворите у VS Code-у и покрените све ћелије.

### 4. Очекујано понашање

**Ћелија 1 (Инсталација):** Успешно инсталира пакете  
**Ћелија 2 (Подешавање):** Нема грешака, увози раде  
**Ћелија 3 (Провера):** Приказује ✓ са списком модела  
**Ћелија 4 (Тест намере):** Приказује резултате детекције намере  
**Ћелија 5 (Рутер):** Приказује ✓ функција рутирања спремна  
**Ћелија 6 (Извршење):** Рутира упите ка моделима, приказује резултате  

### 5. Решавање проблема са грешкама у вези

Ако видите `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Променљиве окружења

Подржане су следеће променљиве окружења:

| Променљива | Подразумевано | Опис |
|------------|---------------|------|
| `SHOW_USAGE` | `0` | Поставите на `1` да бисте приказали употребу токена |
| `RETRY_ON_FAIL` | `1` | Омогућите логику поновног покушаја |
| `RETRY_BACKOFF` | `1.0` | Почетно кашњење поновног покушаја (секунде) |
| `FOUNDRY_LOCAL_ENDPOINT` | Ауто | Замена крајње тачке сервиса |

### Примери употребе

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Миграција са старог шаблона

Ако имате постојећи код који користи директне API позиве, ево како да мигрирате:

### Пре (Директни API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### После (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Предности миграције
- ✅ Аутоматско управљање сервисом
- ✅ Резолуција алијаса модела
- ✅ Избор хардверске оптимизације
- ✅ Боље руковање грешкама
- ✅ Компатибилност са OpenAI SDK-ом
- ✅ Подршка за стриминг

## Референце

### Званична документација
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK извор**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI референца**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Решавање проблема**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop ресурси
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Пример бележника**: `Workshop/notebooks/session06_models_router.ipynb`

### Заједница
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Следећи кораци

1. **Прегледајте промене**: Прочитајте ажуриране датотеке  
2. **Тестирајте бележник**: Покрените session06_models_router.ipynb  
3. **Проверите SDK**: Уверите се да је foundry-local-sdk инсталиран  
4. **Проверите сервис**: Потврдите да Foundry Local ради  
5. **Истражите документацију**: Прочитајте нови session06_README.md  

## Резиме

Ова ажурирања осигуравају да Workshop материјали прате **званичне Foundry Local SDK шаблоне** тачно онако како су документовани у GitHub репозиторијуму. Сви примери кода, документација и алати сада су усклађени са препорученим најбољим праксама Microsoft-а за локално распоређивање AI модела.

Промене побољшавају:
- ✅ **Тачност**: Користи званичне SDK шаблоне  
- ✅ **Документацију**: Свеобухватна објашњења и примери  
- ✅ **Руковање грешкама**: Боље поруке и смернице за решавање проблема  
- ✅ **Одрживост**: Прати званичне конвенције  
- ✅ **Корисничко искуство**: Јаснија упутства и помоћ при отклањању грешака  

---

**Ажурирано:** 8. октобар 2025.  
**Верзија SDK-а:** foundry-local-sdk (најновија)  
**Workshop грана:** Reactor  

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.