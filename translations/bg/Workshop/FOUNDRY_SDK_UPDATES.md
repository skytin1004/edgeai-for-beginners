<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T13:57:53+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "bg"
}
-->
# Актуализации на Foundry Local SDK

## Преглед

Обновени са работните тетрадки и помощните инструменти, за да използват правилно **официалния Foundry Local Python SDK**, следвайки моделите от:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Променени файлове

### 1. `Workshop/samples/workshop_utils.py`

**Промени:**
- ✅ Добавено обработване на грешки при импортиране на пакета `foundry-local-sdk`
- ✅ Подобрена документация с официални модели на SDK
- ✅ Подобрено логване с Unicode символи (✓, ✗, ⚠)
- ✅ Добавени подробни docstrings с примери
- ✅ По-добри съобщения за грешки с препратки към CLI команди
- ✅ Актуализирани коментари, за да съответстват на официалната документация на SDK

**Основни подобрения:**

#### Обработване на грешки при импортиране
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Подобрена функция `get_client()`
- Добавена подробна документация за модела на инициализация на SDK
- Обяснено, че `FoundryLocalManager` автоматично стартира услугата
- Разяснено разрешаването на псевдоними на модели към хардуерно оптимизирани варианти
- Подобрено логване с информация за крайни точки
- По-добри съобщения за грешки с предложения за отстраняване на проблеми

#### Подобрена функция `chat_once()`
- Добавен подробен docstring с примери за употреба
- Разяснена съвместимост с OpenAI SDK
- Документирана поддръжка за стрийминг (чрез kwargs)
- Подобрени съобщения за грешки с предложения за CLI команди
- Добавени бележки за проверка на наличността на модели

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Промени:**
- ✅ Актуализирани всички markdown клетки с препратки към SDK
- ✅ Подобрени коментари в кода с обяснения за моделите на SDK
- ✅ Подобрена документация и обяснения в клетките
- ✅ Добавени насоки за отстраняване на проблеми
- ✅ Актуализиран каталог на модели (заменен 'gpt-oss-20b' с 'phi-3.5-mini')
- ✅ По-добро форматиране на изхода с визуални индикатори
- ✅ Добавени препратки и връзки към SDK в целия текст

**Актуализации по клетки:**

#### Клетка 1 (Заглавие)
- Добавени връзки към документацията на SDK
- Препратки към официалните GitHub хранилища

#### Клетка 2 (Сценарий)
- Преформатирано с номерирани стъпки
- Разяснен модел за маршрутизация, базиран на намерения
- Подчертани предимствата на локалното изпълнение

#### Клетка 3 (Инсталиране на зависимости)
- Добавено обяснение за това какво предоставя всеки пакет
- Документирани възможностите на SDK (разрешаване на псевдоними, хардуерна оптимизация)

#### Клетка 4 (Настройка на среда)
- Подобрени docstrings на функциите
- Добавени коментари в кода, обясняващи моделите на SDK
- Документирана структурата на каталога на модели
- Разяснено съвпадение на приоритети/възможности

#### Клетка 5 (Проверка на каталога)
- Добавени визуални отметки (✓)
- По-добро форматиране на изхода

#### Клетка 6 (Тест за откриване на намерения)
- Преформатиран изход в стил таблица
- Показва както намерението, така и избрания модел

#### Клетка 7 (Функция за маршрутизация)
- Подробно обяснение на модела на SDK
- Документиран потокът на инициализация
- Изброени всички функции (повторен опит, проследяване, грешки)
- Добавена връзка към SDK

#### Клетка 8 (Демо на партида)
- Подобрено обяснение за очакваните резултати
- Добавен раздел за отстраняване на проблеми
- Включени CLI команди за дебъгване
- По-добро форматиране на изхода

### 3. `Workshop/notebooks/session06_README.md` (Нов файл)

**Създадена подробна документация, обхващаща:**

1. **Преглед**: Диаграма на архитектурата и обяснение на компонентите
2. **Интеграция на SDK**: Примери за код, следващи официалните модели
3. **Предварителни условия**: Стъпка по стъпка инструкции за настройка
4. **Употреба**: Как да стартирате и персонализирате тетрадката
5. **Псевдоними на модели**: Обяснение на хардуерно оптимизирани варианти
6. **Отстраняване на проблеми**: Чести проблеми и решения
7. **Разширяване**: Как да добавите намерения, модели и персонализирана логика
8. **Съвети за производителност**: Най-добри практики за използване в продукция
9. **Ресурси**: Връзки към официалната документация и общността

## Имплементация на модела на SDK

### Официален модел (от документацията на Foundry Local)

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

### Нашата имплементация (в workshop_utils)

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

**Предимства на нашия подход:**
- ✅ Следва точно официалния модел на SDK
- ✅ Добавя кеширане за избягване на повторна инициализация
- ✅ Включва логика за повторен опит за по-голяма надеждност
- ✅ Поддържа проследяване на използването на токени
- ✅ Осигурява по-добри съобщения за грешки
- ✅ Остава съвместим с официалните примери

## Промени в каталога на модели

### Преди
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### След
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Причина:** Заменен 'gpt-oss-20b' (неофициален псевдоним) с 'phi-3.5-mini' (официален псевдоним на Foundry Local).

## Зависимости

### Актуализиран requirements.txt

Файлът requirements.txt на Workshop вече включва:
```
foundry-local-sdk
openai>=1.30.0
```

Това са единствените пакети, необходими за интеграция с Foundry Local.

## Тестване на актуализациите

### 1. Проверете дали Foundry Local работи

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Проверете наличните модели

```bash
foundry model ls
```

Уверете се, че тези модели са налични или ще се изтеглят автоматично:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Стартирайте тетрадката

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Или я отворете в VS Code и стартирайте всички клетки.

### 4. Очаквано поведение

**Клетка 1 (Инсталиране):** Успешно инсталира пакети  
**Клетка 2 (Настройка):** Няма грешки, импортирането работи  
**Клетка 3 (Проверка):** Показва ✓ с списък на модели  
**Клетка 4 (Тест за намерения):** Показва резултати от откриване на намерения  
**Клетка 5 (Маршрутизатор):** Показва ✓ Функцията за маршрутизация е готова  
**Клетка 6 (Изпълнение):** Маршрутизира подканите към модели, показва резултати  

### 5. Отстраняване на грешки при връзка

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

## Променливи на средата

Поддържат се следните променливи на средата:

| Променлива | По подразбиране | Описание |
|------------|----------------|----------|
| `SHOW_USAGE` | `0` | Задайте на `1`, за да отпечатате използването на токени |
| `RETRY_ON_FAIL` | `1` | Активира логика за повторен опит |
| `RETRY_BACKOFF` | `1.0` | Начално закъснение при повторен опит (в секунди) |
| `FOUNDRY_LOCAL_ENDPOINT` | Автоматично | Презаписва крайна точка на услугата |

### Примери за употреба

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Миграция от стар модел

Ако имате съществуващ код, използващ директни API извиквания, ето как да мигрирате:

### Преди (Директен API)
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

### След (SDK)
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

### Предимства на миграцията
- ✅ Автоматично управление на услугата
- ✅ Разрешаване на псевдоними на модели
- ✅ Избор на хардуерна оптимизация
- ✅ По-добро обработване на грешки
- ✅ Съвместимост с OpenAI SDK
- ✅ Поддръжка за стрийминг

## Ресурси

### Официална документация
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK Source**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Ресурси за Workshop
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Примерна тетрадка**: `Workshop/notebooks/session06_models_router.ipynb`

### Общност
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Следващи стъпки

1. **Прегледайте промените**: Прочетете актуализираните файлове  
2. **Тествайте тетрадката**: Стартирайте session06_models_router.ipynb  
3. **Проверете SDK**: Уверете се, че foundry-local-sdk е инсталиран  
4. **Проверете услугата**: Уверете се, че Foundry Local работи  
5. **Разгледайте документацията**: Прочетете новия session06_README.md  

## Обобщение

Тези актуализации гарантират, че материалите на Workshop следват **официалните модели на Foundry Local SDK**, точно както са документирани в GitHub хранилището. Всички примери за код, документация и помощни инструменти вече са в съответствие с препоръчаните най-добри практики на Microsoft за локално разгръщане на AI модели.

Промените подобряват:
- ✅ **Точност**: Използват официални модели на SDK  
- ✅ **Документация**: Подробни обяснения и примери  
- ✅ **Обработване на грешки**: По-добри съобщения и насоки за отстраняване на проблеми  
- ✅ **Поддръжка**: Следват официални конвенции  
- ✅ **Потребителско изживяване**: По-ясни инструкции и помощ при дебъгване  

---

**Актуализирано:** 8 октомври 2025 г.  
**Версия на SDK:** foundry-local-sdk (последна)  
**Клон на Workshop:** Reactor

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.