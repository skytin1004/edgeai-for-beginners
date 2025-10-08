<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-08T14:22:20+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "sr"
}
-->
# Примери за радионицу - Резиме ажурирања Foundry Local SDK

## Преглед

Сви Python примери у директоријуму `Workshop/samples` су ажурирани да прате најбоље праксе Foundry Local SDK-а и обезбеде конзистентност кроз радионицу.

**Датум**: 8. октобар 2025.  
**Обухват**: 9 Python датотека кроз 6 сесија радионице  
**Примарни фокус**: Обрада грешака, документација, SDK обрасци, корисничко искуство

---

## Ажуриране датотеке

### Сесија 01: Почетак рада
- ✅ `chat_bootstrap.py` - Основни примери за ћаскање и стриминг

### Сесија 02: RAG решења
- ✅ `rag_pipeline.py` - RAG имплементација са уграђивањем
- ✅ `rag_eval_ragas.py` - RAG евалуација са RAGAS метрикама

### Сесија 03: Модели отвореног кода
- ✅ `benchmark_oss_models.py` - Бенчмаркинг више модела

### Сесија 04: Најсавременији модели
- ✅ `model_compare.py` - Поређење SLM и LLM модела

### Сесија 05: Агенти засновани на вештачкој интелигенцији
- ✅ `agents_orchestrator.py` - Координација више агената

### Сесија 06: Модели као алати
- ✅ `models_router.py` - Рутање засновано на намери
- ✅ `models_pipeline.py` - Вишестепени рутирани процес

### Подршка инфраструктури
- ✅ `workshop_utils.py` - Већ прати најбоље праксе (нису потребне измене)

---

## Кључна побољшања

### 1. Побољшана обрада грешака

**Пре:**
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
  
**Предности:**
- Елегантна обрада грешака са јасним порукама
- Практични савети за решавање проблема
- Правилни излазни кодови за скриптовање

### 2. Боље управљање увозом

**Пре:**
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
  
**Предности:**
- Јасна упутства када недостају зависности
- Спречава нејасне грешке при увозу
- Кориснички пријатељска упутства за инсталацију

### 3. Свеобухватна документација

**Додато у све примере:**
- Документација о променљивим окружења у docstring-овима
- Линкови ка SDK референцама
- Примери употребе
- Детаљна документација функција/параметара
- Типске назнаке за бољу подршку у IDE-у

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
  

### 4. Побољшана повратна информација корисника

**Додато информативно логовање:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```
  
**Индикатори напретка:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```
  
**Структурисани излаз:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```
  

### 5. Робусно бенчмаркирање

**Побољшања у сесији 03:**
- Обрада грешака по моделу (наставља се након неуспеха)
- Детаљно извештавање о напретку
- Правилно извршавање загревања
- Подршка за мерење кашњења првог токена
- Јасна подела фаза

### 6. Конзистентне типске назнаке

**Додато свуда:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```
  
**Предности:**
- Боља аутоматска допуна у IDE-у
- Рано откривање грешака
- Самодокументујући код

### 7. Побољшан рутер модела

**Побољшања у сесији 06:**
- Свеобухватна документација детекције намере
- Објашњење алгоритма за избор модела
- Детаљни логови рутирања
- Форматирање тест излаза
- Опоравак од грешака у групном тестирању

### 8. Оркестрација више агената

**Побољшања у сесији 05:**
- Извештавање о напретку по фазама
- Обрада грешака по агенту
- Јасна структура процеса
- Боља документација управљања меморијом

---

## Контролна листа за тестирање

### Предуслови
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```
  

### Тестирајте сваки пример

#### Сесија 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```
  
#### Сесија 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```
  
#### Сесија 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```
  
#### Сесија 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```
  
#### Сесија 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```
  
#### Сесија 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```
  

---

## Референца променљивих окружења

### Глобално (сви примери)
| Променљива | Опис | Подразумевано |
|------------|------|---------------|
| `FOUNDRY_LOCAL_ALIAS` | Алијас модела који се користи | Разликује се по примеру |
| `FOUNDRY_LOCAL_ENDPOINT` | Замена за сервисни крајњи тачку | Аутоматски детектовано |
| `SHOW_USAGE` | Приказ потрошње токена | `0` |
| `RETRY_ON_FAIL` | Омогући логику поновног покушаја | `1` |
| `RETRY_BACKOFF` | Почетно кашњење при поновном покушају | `1.0` |

### Специфично за пример
| Променљива | Користи | Опис |
|------------|---------|------|
| `EMBED_MODEL` | Сесија 02 | Назив модела за уграђивање |
| `RAG_QUESTION` | Сесија 02 | Тест питање за RAG |
| `BENCH_MODELS` | Сесија 03 | Модели за бенчмаркирање, раздвојени зарезом |
| `BENCH_ROUNDS` | Сесија 03 | Број рунди бенчмаркирања |
| `BENCH_PROMPT` | Сесија 03 | Тест упит за бенчмаркирање |
| `BENCH_STREAM` | Сесија 03 | Мерење кашњења првог токена |
| `SLM_ALIAS` | Сесија 04 | Мали језички модел |
| `LLM_ALIAS` | Сесија 04 | Велики језички модел |
| `COMPARE_PROMPT` | Сесија 04 | Тест упит за поређење |
| `AGENT_MODEL_PRIMARY` | Сесија 05 | Примарни модел агента |
| `AGENT_MODEL_EDITOR` | Сесија 05 | Модел агента уредника |
| `AGENT_QUESTION` | Сесија 05 | Тест питање за агенте |
| `PIPELINE_TASK` | Сесија 06 | Задатак за процес |

---

## Промене које прекидају рад

**Нема** - Све промене су уназад компатибилне.

Постојећи скриптови ће наставити да раде. Нове функције су:
- Опционалне променљиве окружења
- Побољшане поруке о грешкама (не прекидају функционалност)
- Додатно логовање (може се потиснути)
- Боље типске назнаке (нема утицаја на време извршавања)

---

## Примењене најбоље праксе

### 1. Увек користите Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```
  
### 2. Правилан образац за обраду грешака
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```
  
### 3. Информативно логовање
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```
  
### 4. Типске назнаке
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```
  
### 5. Свеобухватни docstring-ови
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
  
### 6. Подршка за променљиве окружења
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```
  
### 7. Елегантна деградација
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

## Уобичајени проблеми и решења

### Проблем: Грешке при увозу
**Решење:** Инсталирајте недостајуће зависности  
```bash
pip install sentence-transformers ragas datasets numpy
```
  

### Проблем: Грешке при повезивању
**Решење:** Уверите се да Foundry Local ради  
```bash
foundry service status
foundry model run phi-4-mini
```
  

### Проблем: Модел није пронађен
**Решење:** Проверите доступне моделе  
```bash
foundry model ls
foundry model download <alias>
```
  

### Проблем: Спор рад
**Решење:** Користите мање моделе или прилагодите параметре  
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```
  

---

## Следећи кораци

### 1. Тестирајте све примере
Прођите кроз контролну листу за тестирање изнад да бисте проверили да ли сви примери раде исправно.

### 2. Ажурирајте документацију
- Ажурирајте markdown датотеке сесија са новим примерима
- Додајте секцију за решавање проблема у главни README
- Направите брзи водич за референцу

### 3. Направите интеграционе тестове
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```
  

### 4. Додајте бенчмарке перформанси
Пратите побољшања перформанси од побољшања обраде грешака.

### 5. Повратна информација корисника
Прикупите повратне информације од учесника радионице о:
- Јасноћи порука о грешкама
- Комплетности документације
- Лакоћи употребе

---

## Ресурси

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Брза референца**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **Белешке о миграцији**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **Главни репозиторијум**: https://github.com/microsoft/Foundry-Local  

---

## Одржавање

### Додавање нових примера
Пратите ове обрасце приликом креирања нових примера:

1. Користите `workshop_utils` за управљање клијентима
2. Додајте свеобухватну обраду грешака
3. Укључите подршку за променљиве окружења
4. Додајте типске назнаке и docstring-ове
5. Обезбедите информативно логовање
6. Укључите примере употребе у docstring
7. Линкујте на SDK документацију

### Преглед ажурирања
Приликом прегледа ажурирања примера, проверите:
- [ ] Обрада грешака на свим I/O операцијама
- [ ] Типске назнаке на јавним функцијама
- [ ] Свеобухватни docstring-ови
- [ ] Документација променљивих окружења
- [ ] Информативна повратна информација корисника
- [ ] Линкови ка SDK референцама
- [ ] Конзистентан стил кода

---

**Резиме**: Сви Python примери радионице сада прате најбоље праксе Foundry Local SDK-а са побољшаном обрадом грешака, свеобухватном документацијом и унапређеним корисничким искуством. Нема промена које прекидају рад - сва постојећа функционалност је очувана и побољшана.

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.