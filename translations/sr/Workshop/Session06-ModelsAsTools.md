<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-08T14:18:40+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "sr"
}
-->
# Сесија 6: Foundry Local – Модели као алати

## Апстракт

Третирајте моделе као састављиве алате у локалном AI оперативном слоју. Ова сесија показује како да повежете више специјализованих SLM/LLM позива, селективно усмеравате задатке и изложите јединствену SDK површину апликацијама. Направићете лагани рутер модела + планер задатака, интегрисати га у скрипту апликације и описати пут скалирања ка Azure AI Foundry за производне радне оптерећења.

## Циљеви учења

- **Концептуализујте** моделе као атомске алате са декларисаним способностима
- **Усмерите** захтеве на основу намере / хеуристичког оцењивања
- **Повежите** излазе кроз задатке у више корака (разложи → реши → усаврши)
- **Интегришите** јединствени клијентски API за апликације
- **Скалирајте** дизајн ка облаку (исти OpenAI-компатибилан уговор)

## Предуслови

- Завршене сесије 1–5
- Више локалних модела кеширано (нпр. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Унакрсна платформа – исечак окружења

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

Доступ са удаљеног/VM сервиса са macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстрациони ток (30 мин)

### 1. Декларација способности алата (5 мин)

Направите `samples/06-tools/models_catalog.py`:

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


### 2. Детекција намере и усмеравање (8 мин)

Направите `samples/06-tools/router.py`:

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


### 3. Повезивање задатака у више корака (7 мин)

Направите `samples/06-tools/pipeline.py`:

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


### 4. Почетни пројекат: Адаптирајте `06-models-as-tools` (5 мин)

Унапређења:
- Додајте подршку за стримовање токена (прогресивно ажурирање UI)
- Додајте оцењивање поверења: лексичко преклапање или рубрика упита
- Извезите JSON траг (намера → модел → кашњење → употреба токена)
- Имплементирајте поновну употребу кеша за поновљене подзадатке

### 5. Пут скалирања ка Azure (5 мин)

| Слој | Локално (Foundry) | Облак (Azure AI Foundry) | Стратегија транзиције |
|------|-------------------|--------------------------|------------------------|
| Усмеравање | Хеуристички Python | Трајни микросервис | Контејнеризујте и распоредите API |
| Модели | Кеширани SLM-ови | Управљане инсталације | Мапирајте локална имена на ID-ове инсталација |
| Опсервабилност | CLI статистика/мануелно | Централно логовање и метрике | Додајте структурисане догађаје трага |
| Безбедност | Само локални хост | Azure аутентификација / мрежа | Уведите Key Vault за тајне |
| Трошкови | Ресурси уређаја | Наплата по потрошњи | Додајте ограничења буџета |

## Контролна листа за валидацију

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Очекујте избор модела на основу намере и коначан усавршен излаз.

## Решавање проблема

| Проблем | Узрок | Решавање |
|---------|-------|---------|
| Сви задаци усмерени на исти модел | Слаба правила | Обогатите INTENT_RULES regex сет |
| Пипелина не успева на средини корака | Недостаје учитани модел | Покрените `foundry model run <model>` |
| Ниска кохезија излаза | Нема фазе усавршавања | Додајте корак сумирања/валидације |

## Референце

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry документација: https://learn.microsoft.com/azure/ai-foundry
- Шаблони квалитета упита: Погледајте Сесију 2

---

**Трајање сесије**: 30 мин  
**Тежина**: Експерт

## Пример сценарија и мапирање радионице

| Скрипте радионице / Бележнице | Сценарио | Циљ | Извор података / каталога |
|-------------------------------|----------|-----|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Асистент за програмере који обрађује мешовите упите (рефактор, сумирање, класификација) | Хеуристичко усмеравање намере → алијас модела са употребом токена | Уграђени `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Планирање и усавршавање у више корака за сложени задатак помоћи кодирању | Разложи → специјализовано извршење → корак усавршавања сумирања | Исти `CATALOG`; кораци изведени из излаза плана |

### Наратив сценарија

Алат за продуктивност инжењера прима хетерогене задатке: рефакторисање кода, сумирање архитектонских белешки, класификација повратних информација. Да би се минимизирало кашњење и употреба ресурса, мали општи модел планира и сумира, модел специјализован за код обрађује рефакторисање, а лагани модел способан за класификацију означава повратне информације. Скрипта пипелине демонстрира повезивање + усавршавање; скрипта рутера изолује адаптивно усмеравање једног упита.

### Снимак каталога

```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Пример тест упита

```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Проширење трага (опционо)

Додајте JSON линије трага по кораку за `models_pipeline.py`:

```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Хеуристика ескалације (идеја)

Ако план садржи кључне речи као што су "оптимизуј", "безбедност", или дужина корака > 280 карактера → ескалирајте на већи модел (нпр. `gpt-oss-20b`) само за тај корак.

### Опциона унапређења

| Област | Унапређење | Вредност | Савет |
|--------|------------|----------|-------|
| Кеширање | Поновна употреба менаџера + клијентских објеката | Мање кашњење, мањи трошкови | Користите `workshop_utils.get_client` |
| Метрике употребе | Снимање токена и кашњења по кораку | Профилисање и оптимизација | Измерите сваки позив рутера; сачувајте у листи трага |
| Адаптивно усмеравање | Свесно поверења / трошкова | Бољи однос квалитета и трошкова | Додајте оцењивање: ако упит > N карактера или regex одговара домену → ескалирајте на већи модел |
| Динамички регистар способности | Хот релоад каталога | Без поновног покретања распоређивања | Учитајте `catalog.json` у време извршења; пратите временски жиг датотеке |
| Стратегија резерве | Робусност у случају неуспеха | Већа доступност | Пробајте примарни → у случају изузетка резервни алијас |
| Стримовање пипелине | Рани повратни одговор | Побољшање UX-а | Стримујте сваки корак и баферујте коначни улаз за усавршавање |
| Векторске намере | Нежније усмеравање | Већа тачност намере | Угради упит, кластеризуј и мапирај центроид → способност |
| Извоз трага | Аудитабилни ланац | Усклађеност/извештавање | Емитујте JSON линије: корак, намера, модел, кашњење_ms, токени |
| Симулација трошкова | Процена пре облака | Планирање буџета | Доделите номинални трошак/токен по моделу и агрегирајте по задатку |
| Детерминистички режим | Репродуктивна репродуктивност | Стабилно бенчмаркирање | Окружење: `temperature=0`, фиксни број корака |

#### Пример структуре трага

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Скица адаптивне ескалације

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Хот релоад каталога модела

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


Постепено унапређујте—избегавајте претерано компликовање раних прототипа.

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.