<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T06:59:57+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ru"
}
-->
# Примеры для мастерской - Обновление Foundry Local SDK

## Обзор

Все примеры на Python в каталоге `Workshop/samples` были обновлены в соответствии с лучшими практиками Foundry Local SDK, чтобы обеспечить единообразие в рамках мастерской.

**Дата**: 8 октября 2025  
**Объем**: 9 файлов на Python в 6 сессиях мастерской  
**Основной акцент**: Обработка ошибок, документация, шаблоны SDK, удобство использования

---

## Обновленные файлы

### Сессия 01: Начало работы
- ✅ `chat_bootstrap.py` - Основные примеры чата и потоковой передачи

### Сессия 02: Решения RAG
- ✅ `rag_pipeline.py` - Реализация RAG с использованием эмбеддингов
- ✅ `rag_eval_ragas.py` - Оценка RAG с метриками RAGAS

### Сессия 03: Модели с открытым исходным кодом
- ✅ `benchmark_oss_models.py` - Бенчмаркинг нескольких моделей

### Сессия 04: Передовые модели
- ✅ `model_compare.py` - Сравнение SLM и LLM

### Сессия 05: Агенты на базе ИИ
- ✅ `agents_orchestrator.py` - Координация нескольких агентов

### Сессия 06: Модели как инструменты
- ✅ `models_router.py` - Маршрутизация моделей на основе намерений
- ✅ `models_pipeline.py` - Многошаговый маршрутизированный конвейер

### Вспомогательная инфраструктура
- ✅ `workshop_utils.py` - Уже соответствует лучшим практикам (изменений не требуется)

---

## Основные улучшения

### 1. Улучшенная обработка ошибок

**До:**
```python
manager, client, model_id = get_client(alias)
```
  
**После:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```
  
**Преимущества:**
- Элегантная обработка ошибок с понятными сообщениями
- Подсказки для устранения неполадок
- Корректные коды выхода для скриптов

### 2. Улучшенное управление импортами

**До:**
```python
from sentence_transformers import SentenceTransformer
```
  
**После:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```
  
**Преимущества:**
- Четкие инструкции при отсутствии зависимостей
- Предотвращение непонятных ошибок импорта
- Удобные инструкции по установке

### 3. Полная документация

**Добавлено ко всем примерам:**
- Документация переменных окружения в docstrings
- Ссылки на SDK
- Примеры использования
- Подробная документация функций/параметров
- Подсказки типов для поддержки IDE

**Пример:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```
  

### 4. Улучшенная обратная связь для пользователя

**Добавлено информативное логирование:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```
  
**Индикаторы прогресса:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```
  
**Структурированный вывод:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```
  

### 5. Надежный бенчмаркинг

**Улучшения для сессии 03:**
- Обработка ошибок для каждой модели (продолжение при сбое)
- Подробная отчетность о прогрессе
- Корректное выполнение этапов прогрева
- Поддержка измерения задержки первого токена
- Четкое разделение этапов

### 6. Единообразные подсказки типов

**Добавлено повсеместно:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```
  
**Преимущества:**
- Улучшенная автозаполняемость в IDE
- Раннее обнаружение ошибок
- Самодокументируемый код

### 7. Улучшенный маршрутизатор моделей

**Улучшения для сессии 06:**
- Полная документация по обнаружению намерений
- Объяснение алгоритма выбора модели
- Подробные журналы маршрутизации
- Форматирование тестового вывода
- Восстановление после ошибок при пакетном тестировании

### 8. Оркестрация нескольких агентов

**Улучшения для сессии 05:**
- Отчетность о прогрессе по этапам
- Обработка ошибок для каждого агента
- Четкая структура конвейера
- Улучшенная документация по управлению памятью

---

## Контрольный список тестирования

### Предварительные условия
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```
  

### Тестирование каждого примера

#### Сессия 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```
  
#### Сессия 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```
  
#### Сессия 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```
  
#### Сессия 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```
  
#### Сессия 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```
  
#### Сессия 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```
  

---

## Справочник переменных окружения

### Глобальные (для всех примеров)
| Переменная | Описание | Значение по умолчанию |
|------------|----------|-----------------------|
| `FOUNDRY_LOCAL_ALIAS` | Псевдоним модели для использования | Зависит от примера |
| `FOUNDRY_LOCAL_ENDPOINT` | Переопределение конечной точки сервиса | Автоопределение |
| `SHOW_USAGE` | Показать использование токенов | `0` |
| `RETRY_ON_FAIL` | Включить логику повторных попыток | `1` |
| `RETRY_BACKOFF` | Начальная задержка повторной попытки | `1.0` |

### Специфичные для примеров
| Переменная | Используется в | Описание |
|------------|---------------|----------|
| `EMBED_MODEL` | Сессия 02 | Название модели эмбеддинга |
| `RAG_QUESTION` | Сессия 02 | Тестовый вопрос для RAG |
| `BENCH_MODELS` | Сессия 03 | Модели для бенчмаркинга (через запятую) |
| `BENCH_ROUNDS` | Сессия 03 | Количество раундов бенчмаркинга |
| `BENCH_PROMPT` | Сессия 03 | Тестовый запрос для бенчмаркинга |
| `BENCH_STREAM` | Сессия 03 | Измерение задержки первого токена |
| `SLM_ALIAS` | Сессия 04 | Маленькая языковая модель |
| `LLM_ALIAS` | Сессия 04 | Большая языковая модель |
| `COMPARE_PROMPT` | Сессия 04 | Тестовый запрос для сравнения |
| `AGENT_MODEL_PRIMARY` | Сессия 05 | Основная модель агента |
| `AGENT_MODEL_EDITOR` | Сессия 05 | Модель агента-редактора |
| `AGENT_QUESTION` | Сессия 05 | Тестовый вопрос для агентов |
| `PIPELINE_TASK` | Сессия 06 | Задача для конвейера |

---

## Изменения, нарушающие совместимость

**Отсутствуют** - Все изменения совместимы с предыдущими версиями.

Существующие скрипты продолжат работать. Новые функции включают:
- Дополнительные переменные окружения
- Улучшенные сообщения об ошибках (не нарушают функциональность)
- Дополнительное логирование (можно отключить)
- Улучшенные подсказки типов (не влияют на выполнение)

---

## Реализованные лучшие практики

### 1. Всегда используйте Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```
  
### 2. Корректная обработка ошибок
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```
  
### 3. Информативное логирование
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```
  
### 4. Подсказки типов
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```
  
### 5. Полные docstrings
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```
  
### 6. Поддержка переменных окружения
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```
  
### 7. Плавная деградация
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```
  

---

## Частые проблемы и их решения

### Проблема: Ошибки импорта
**Решение:** Установите отсутствующие зависимости  
```bash
pip install sentence-transformers ragas datasets numpy
```
  

### Проблема: Ошибки подключения
**Решение:** Убедитесь, что Foundry Local запущен  
```bash
foundry service status
foundry model run phi-4-mini
```
  

### Проблема: Модель не найдена
**Решение:** Проверьте доступные модели  
```bash
foundry model ls
foundry model download <alias>
```
  

### Проблема: Низкая производительность
**Решение:** Используйте более компактные модели или измените параметры  
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```
  

---

## Следующие шаги

### 1. Тестирование всех примеров
Пройдите контрольный список тестирования выше, чтобы убедиться, что все примеры работают корректно.

### 2. Обновление документации
- Обновите файлы сессий с новыми примерами
- Добавьте раздел устранения неполадок в основной README
- Создайте краткий справочник

### 3. Создание интеграционных тестов
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```
  

### 4. Добавление бенчмарков производительности
Отслеживайте улучшения производительности благодаря улучшенной обработке ошибок.

### 5. Обратная связь от пользователей
Соберите отзывы участников мастерской о:
- Понятности сообщений об ошибках
- Полноте документации
- Удобстве использования

---

## Ресурсы

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Краткий справочник**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **Примечания по миграции**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **Основной репозиторий**: https://github.com/microsoft/Foundry-Local  

---

## Обслуживание

### Добавление новых примеров
Следуйте этим шаблонам при создании новых примеров:

1. Используйте `workshop_utils` для управления клиентами
2. Добавьте полную обработку ошибок
3. Включите поддержку переменных окружения
4. Добавьте подсказки типов и docstrings
5. Обеспечьте информативное логирование
6. Включите примеры использования в docstrings
7. Ссылки на документацию SDK

### Проверка обновлений
При проверке обновлений примеров убедитесь, что:
- [ ] Обработка ошибок реализована для всех операций ввода/вывода
- [ ] Подсказки типов добавлены для публичных функций
- [ ] Docstrings полные и информативные
- [ ] Документированы переменные окружения
- [ ] Обратная связь для пользователя информативна
- [ ] Ссылки на SDK включены
- [ ] Стиль кода единообразен

---

**Итог**: Все примеры на Python для мастерской теперь соответствуют лучшим практикам Foundry Local SDK с улучшенной обработкой ошибок, полной документацией и улучшенным пользовательским опытом. Изменений, нарушающих совместимость, нет - вся существующая функциональность сохранена и улучшена.

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.