<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T06:39:19+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "ru"
}
-->
# Обновления локального SDK Foundry

## Обзор

Обновлены блокноты Workshop и утилиты для корректного использования **официального локального Python SDK Foundry** в соответствии с шаблонами из:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Измененные файлы

### 1. `Workshop/samples/workshop_utils.py`

**Изменения:**
- ✅ Добавлена обработка ошибок импорта для пакета `foundry-local-sdk`
- ✅ Улучшена документация с использованием шаблонов официального SDK
- ✅ Улучшен логгинг с использованием Unicode-символов (✓, ✗, ⚠)
- ✅ Добавлены подробные docstrings с примерами
- ✅ Улучшены сообщения об ошибках с ссылками на команды CLI
- ✅ Обновлены комментарии в соответствии с документацией официального SDK

**Основные улучшения:**

#### Обработка ошибок импорта
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Улучшенная функция `get_client()`
- Добавлена подробная документация о шаблоне инициализации SDK
- Уточнено, что `FoundryLocalManager` автоматически запускает сервис
- Объяснено разрешение псевдонимов моделей на оптимизированные для оборудования варианты
- Улучшен логгинг с информацией об эндпоинте
- Улучшены сообщения об ошибках с предложениями по устранению неполадок

#### Улучшенная функция `chat_once()`
- Добавлен подробный docstring с примерами использования
- Уточнена совместимость с SDK OpenAI
- Задокументирована поддержка потоковой передачи (через kwargs)
- Улучшены сообщения об ошибках с предложениями команд CLI
- Добавлены примечания о проверке доступности моделей

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Изменения:**
- ✅ Обновлены все markdown ячейки с ссылками на SDK
- ✅ Улучшены комментарии к коду с объяснением шаблонов SDK
- ✅ Улучшена документация и пояснения в ячейках
- ✅ Добавлены рекомендации по устранению неполадок
- ✅ Обновлен каталог моделей (заменен 'gpt-oss-20b' на 'phi-3.5-mini')
- ✅ Улучшено форматирование вывода с визуальными индикаторами
- ✅ Добавлены ссылки и упоминания SDK

**Обновления по ячейкам:**

#### Ячейка 1 (Заголовок)
- Добавлены ссылки на документацию SDK
- Упомянуты официальные репозитории GitHub

#### Ячейка 2 (Сценарий)
- Переформатировано с использованием пронумерованных шагов
- Уточнен шаблон маршрутизации на основе намерений
- Подчеркнуты преимущества локального выполнения

#### Ячейка 3 (Установка зависимостей)
- Добавлено объяснение, что предоставляет каждый пакет
- Задокументированы возможности SDK (разрешение псевдонимов, оптимизация оборудования)

#### Ячейка 4 (Настройка окружения)
- Улучшены docstrings функций
- Добавлены встроенные комментарии, объясняющие шаблоны SDK
- Задокументирована структура каталога моделей
- Уточнено соответствие приоритетов/возможностей

#### Ячейка 5 (Проверка каталога)
- Добавлены визуальные галочки (✓)
- Улучшено форматирование вывода

#### Ячейка 6 (Тестирование определения намерений)
- Переформатирован вывод в виде таблицы
- Показаны как намерения, так и выбранные модели

#### Ячейка 7 (Функция маршрутизации)
- Подробное объяснение шаблонов SDK
- Задокументирован процесс инициализации
- Перечислены все функции (повтор, отслеживание, ошибки)
- Добавлена ссылка на SDK

#### Ячейка 8 (Демонстрация пакетной обработки)
- Улучшено объяснение ожидаемых результатов
- Добавлен раздел устранения неполадок
- Включены команды CLI для отладки
- Улучшено отображение вывода

### 3. `Workshop/notebooks/session06_README.md` (Новый файл)

**Создана подробная документация, охватывающая:**

1. **Обзор**: Диаграмма архитектуры и объяснение компонентов
2. **Интеграция SDK**: Примеры кода с использованием официальных шаблонов
3. **Предварительные условия**: Пошаговые инструкции по настройке
4. **Использование**: Как запустить и настроить блокнот
5. **Псевдонимы моделей**: Объяснение оптимизированных для оборудования вариантов
6. **Устранение неполадок**: Распространенные проблемы и их решения
7. **Расширение**: Как добавить намерения, модели и пользовательскую логику
8. **Советы по производительности**: Лучшие практики для использования в продакшене
9. **Ресурсы**: Ссылки на официальную документацию и сообщество

## Реализация шаблонов SDK

### Официальный шаблон (из документации Foundry Local)

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

### Наша реализация (в workshop_utils)

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

**Преимущества нашего подхода:**
- ✅ Точно следует официальному шаблону SDK
- ✅ Добавляет кэширование для предотвращения повторной инициализации
- ✅ Включает логику повторов для надежности в продакшене
- ✅ Поддерживает отслеживание использования токенов
- ✅ Предоставляет улучшенные сообщения об ошибках
- ✅ Остается совместимым с официальными примерами

## Изменения каталога моделей

### До
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

**Причина:** Замена 'gpt-oss-20b' (неофициальный псевдоним) на 'phi-3.5-mini' (официальный псевдоним Foundry Local).

## Зависимости

### Обновленный requirements.txt

Файл requirements.txt Workshop уже включает:
```
foundry-local-sdk
openai>=1.30.0
```

Это единственные пакеты, необходимые для интеграции Foundry Local.

## Тестирование обновлений

### 1. Убедитесь, что Foundry Local запущен

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Проверьте доступные модели

```bash
foundry model ls
```

Убедитесь, что эти модели доступны или будут автоматически загружены:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Запустите блокнот

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Или откройте в VS Code и выполните все ячейки.

### 4. Ожидаемое поведение

**Ячейка 1 (Установка):** Успешная установка пакетов  
**Ячейка 2 (Настройка):** Без ошибок, импорт работает  
**Ячейка 3 (Проверка):** Показывает ✓ с списком моделей  
**Ячейка 4 (Тест намерений):** Показывает результаты определения намерений  
**Ячейка 5 (Маршрутизатор):** Показывает ✓ Функция маршрутизации готова  
**Ячейка 6 (Выполнение):** Маршрутизирует запросы к моделям, показывает результаты  

### 5. Устранение ошибок подключения

Если вы видите `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Переменные окружения

Поддерживаются следующие переменные окружения:

| Переменная | Значение по умолчанию | Описание |
|------------|-----------------------|----------|
| `SHOW_USAGE` | `0` | Установите `1`, чтобы выводить использование токенов |
| `RETRY_ON_FAIL` | `1` | Включить логику повторов |
| `RETRY_BACKOFF` | `1.0` | Начальная задержка повтора (в секундах) |
| `FOUNDRY_LOCAL_ENDPOINT` | Авто | Переопределить эндпоинт сервиса |

### Примеры использования

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Миграция с устаревшего шаблона

Если у вас есть существующий код, использующий прямые вызовы API, вот как выполнить миграцию:

### До (Прямой API)
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

### Преимущества миграции
- ✅ Автоматическое управление сервисом
- ✅ Разрешение псевдонимов моделей
- ✅ Выбор оптимизации оборудования
- ✅ Улучшенная обработка ошибок
- ✅ Совместимость с SDK OpenAI
- ✅ Поддержка потоковой передачи

## Ссылки

### Официальная документация
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Исходный код Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Справочник CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Устранение неполадок**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Ресурсы Workshop
- **README для сессии 06**: `Workshop/notebooks/session06_README.md`
- **Утилиты Workshop**: `Workshop/samples/workshop_utils.py`
- **Пример блокнота**: `Workshop/notebooks/session06_models_router.ipynb`

### Сообщество
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Следующие шаги

1. **Просмотрите изменения**: Ознакомьтесь с обновленными файлами  
2. **Протестируйте блокнот**: Запустите session06_models_router.ipynb  
3. **Проверьте SDK**: Убедитесь, что foundry-local-sdk установлен  
4. **Проверьте сервис**: Убедитесь, что Foundry Local запущен  
5. **Изучите документацию**: Прочитайте новый session06_README.md  

## Резюме

Эти обновления гарантируют, что материалы Workshop полностью соответствуют **официальным шаблонам SDK Foundry Local**, как указано в репозитории GitHub. Все примеры кода, документация и утилиты теперь соответствуют рекомендованным Microsoft лучшим практикам для локального развертывания моделей ИИ.

Изменения улучшают:
- ✅ **Точность**: Использование официальных шаблонов SDK  
- ✅ **Документацию**: Подробные объяснения и примеры  
- ✅ **Обработку ошибок**: Улучшенные сообщения и рекомендации по устранению неполадок  
- ✅ **Поддерживаемость**: Следование официальным соглашениям  
- ✅ **Удобство использования**: Более понятные инструкции и помощь в отладке  

---

**Обновлено:** 8 октября 2025  
**Версия SDK:** foundry-local-sdk (последняя)  
**Ветка Workshop:** Reactor  

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.