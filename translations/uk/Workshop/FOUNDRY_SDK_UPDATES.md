<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T11:57:12+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "uk"
}
-->
# Оновлення локального SDK Foundry

## Огляд

Оновлено блокноти Workshop та утиліти для правильного використання **офіційного локального Python SDK Foundry**, дотримуючись шаблонів із:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Змінені файли

### 1. `Workshop/samples/workshop_utils.py`

**Зміни:**
- ✅ Додано обробку помилок імпорту для пакету `foundry-local-sdk`
- ✅ Покращено документацію з використанням офіційних шаблонів SDK
- ✅ Поліпшено логування за допомогою Unicode-символів (✓, ✗, ⚠)
- ✅ Додано детальні docstrings із прикладами
- ✅ Покращено повідомлення про помилки з посиланнями на CLI-команди
- ✅ Оновлено коментарі відповідно до офіційної документації SDK

**Основні покращення:**

#### Обробка помилок імпорту
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Покращена функція `get_client()`
- Додано детальну документацію про шаблон ініціалізації SDK
- Уточнено, що `FoundryLocalManager` автоматично запускає сервіс
- Пояснено розв'язання псевдонімів моделей для апаратно оптимізованих варіантів
- Поліпшено логування з інформацією про кінцеву точку
- Покращено повідомлення про помилки з пропозиціями щодо усунення проблем

#### Покращена функція `chat_once()`
- Додано детальний docstring із прикладами використання
- Уточнено сумісність із SDK OpenAI
- Задокументовано підтримку потокової передачі (через kwargs)
- Покращено повідомлення про помилки з пропозиціями CLI-команд
- Додано примітки про перевірку доступності моделей

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Зміни:**
- ✅ Оновлено всі markdown-комірки з посиланнями на SDK
- ✅ Покращено коментарі до коду з поясненнями шаблонів SDK
- ✅ Поліпшено документацію комірок та пояснення
- ✅ Додано рекомендації щодо усунення проблем
- ✅ Оновлено каталог моделей (замість 'gpt-oss-20b' використано 'phi-3.5-mini')
- ✅ Покращено форматування виводу з візуальними індикаторами
- ✅ Додано посилання на SDK та рекомендації

**Оновлення по комірках:**

#### Комірка 1 (Заголовок)
- Додано посилання на документацію SDK
- Згадано офіційні репозиторії GitHub

#### Комірка 2 (Сценарій)
- Переформатовано у вигляді пронумерованих кроків
- Уточнено шаблон маршрутизації на основі намірів
- Підкреслено переваги локального виконання

#### Комірка 3 (Встановлення залежностей)
- Додано пояснення, що забезпечує кожен пакет
- Задокументовано можливості SDK (розв'язання псевдонімів, апаратна оптимізація)

#### Комірка 4 (Налаштування середовища)
- Покращено docstrings функцій
- Додано коментарі в коді з поясненням шаблонів SDK
- Задокументовано структуру каталогу моделей
- Уточнено відповідність пріоритетів/можливостей

#### Комірка 5 (Перевірка каталогу)
- Додано візуальні галочки (✓)
- Покращено форматування виводу

#### Комірка 6 (Тестування визначення намірів)
- Переформатовано вивід у вигляді таблиці
- Показує як намір, так і вибрану модель

#### Комірка 7 (Функція маршрутизації)
- Детальне пояснення шаблону SDK
- Задокументовано процес ініціалізації
- Перелічено всі функції (повторна спроба, відстеження, помилки)
- Додано посилання на SDK

#### Комірка 8 (Демонстрація пакетної обробки)
- Покращено пояснення очікуваних результатів
- Додано розділ усунення проблем
- Включено CLI-команди для налагодження
- Покращено форматування виводу

### 3. `Workshop/notebooks/session06_README.md` (Новий файл)

**Створено детальну документацію, яка охоплює:**

1. **Огляд**: Діаграма архітектури та пояснення компонентів
2. **Інтеграція SDK**: Приклади коду за офіційними шаблонами
3. **Попередні вимоги**: Покрокові інструкції з налаштування
4. **Використання**: Як запустити та налаштувати блокнот
5. **Псевдоніми моделей**: Пояснення апаратно оптимізованих варіантів
6. **Усунення проблем**: Поширені проблеми та їх вирішення
7. **Розширення**: Як додати наміри, моделі та власну логіку
8. **Поради щодо продуктивності**: Найкращі практики для використання у виробництві
9. **Ресурси**: Посилання на офіційну документацію та спільноту

## Реалізація шаблону SDK

### Офіційний шаблон (з документації Foundry Local)

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

### Наша реалізація (у workshop_utils)

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

**Переваги нашого підходу:**
- ✅ Точно відповідає офіційному шаблону SDK
- ✅ Додає кешування для уникнення повторної ініціалізації
- ✅ Включає логіку повторних спроб для надійності у виробництві
- ✅ Підтримує відстеження використання токенів
- ✅ Забезпечує кращі повідомлення про помилки
- ✅ Залишається сумісним із офіційними прикладами

## Зміни в каталозі моделей

### До
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Після
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Причина:** Заміна 'gpt-oss-20b' (нестандартний псевдонім) на 'phi-3.5-mini' (офіційний псевдонім Foundry Local).

## Залежності

### Оновлений файл requirements.txt

Файл requirements.txt для Workshop вже включає:
```
foundry-local-sdk
openai>=1.30.0
```

Це єдині пакети, необхідні для інтеграції Foundry Local.

## Тестування оновлень

### 1. Перевірте, чи працює Foundry Local

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Перевірте доступні моделі

```bash
foundry model ls
```

Переконайтеся, що ці моделі доступні або будуть автоматично завантажені:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Запустіть блокнот

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Або відкрийте у VS Code і запустіть усі комірки.

### 4. Очікувана поведінка

**Комірка 1 (Встановлення):** Успішно встановлює пакети  
**Комірка 2 (Налаштування):** Без помилок, імпорт працює  
**Комірка 3 (Перевірка):** Показує ✓ зі списком моделей  
**Комірка 4 (Тест намірів):** Показує результати визначення намірів  
**Комірка 5 (Маршрутизатор):** Показує ✓ Функція маршрутизації готова  
**Комірка 6 (Виконання):** Маршрутизує запити до моделей, показує результати  

### 5. Усунення проблем із помилками з'єднання

Якщо ви бачите `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Змінні середовища

Підтримуються наступні змінні середовища:

| Змінна | За замовчуванням | Опис |
|--------|------------------|------|
| `SHOW_USAGE` | `0` | Встановіть `1`, щоб друкувати використання токенів |
| `RETRY_ON_FAIL` | `1` | Увімкнути логіку повторних спроб |
| `RETRY_BACKOFF` | `1.0` | Початкова затримка повторної спроби (секунди) |
| `FOUNDRY_LOCAL_ENDPOINT` | Авто | Перевизначити кінцеву точку сервісу |

### Приклади використання

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Міграція зі старого шаблону

Якщо у вас є існуючий код із прямими викликами API, ось як мігрувати:

### До (Прямий API)
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

### Після (SDK)
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

### Переваги міграції
- ✅ Автоматичне управління сервісом
- ✅ Розв'язання псевдонімів моделей
- ✅ Вибір апаратної оптимізації
- ✅ Краще оброблення помилок
- ✅ Сумісність із SDK OpenAI
- ✅ Підтримка потокової передачі

## Ресурси

### Офіційна документація
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Джерело Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Довідка CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Усунення проблем**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Ресурси Workshop
- **README для сесії 06**: `Workshop/notebooks/session06_README.md`
- **Утиліти Workshop**: `Workshop/samples/workshop_utils.py`
- **Приклад блокнота**: `Workshop/notebooks/session06_models_router.ipynb`

### Спільнота
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Наступні кроки

1. **Перегляньте зміни**: Ознайомтеся з оновленими файлами  
2. **Тестуйте блокнот**: Запустіть session06_models_router.ipynb  
3. **Перевірте SDK**: Переконайтеся, що foundry-local-sdk встановлено  
4. **Перевірте сервіс**: Переконайтеся, що Foundry Local працює  
5. **Ознайомтеся з документацією**: Прочитайте новий session06_README.md  

## Підсумок

Ці оновлення забезпечують, що матеріали Workshop точно відповідають **офіційним шаблонам SDK Foundry Local**, як задокументовано в репозиторії GitHub. Усі приклади коду, документація та утиліти тепер відповідають рекомендованим найкращим практикам Microsoft для локального розгортання моделей штучного інтелекту.

Зміни покращують:
- ✅ **Точність**: Використання офіційних шаблонів SDK  
- ✅ **Документацію**: Детальні пояснення та приклади  
- ✅ **Обробку помилок**: Кращі повідомлення та рекомендації щодо усунення проблем  
- ✅ **Підтримуваність**: Дотримання офіційних конвенцій  
- ✅ **Зручність для користувача**: Чіткі інструкції та допомога в налагодженні  

---

**Оновлено:** 8 жовтня 2025 року  
**Версія SDK:** foundry-local-sdk (остання)  
**Гілка Workshop:** Reactor

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.