<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1b3c0fecfd713c2df903a0633249dc9",
  "translation_date": "2025-10-08T14:00:50+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "sr"
}
-->
# Сесија 4: Истражите најсавременије моделе – LLM, SLM и инференцију на уређају

## Апстракт

Упоредите велике језичке моделе (LLM) и мале језичке моделе (SLM) за сценарије инференције на локалном уређају и у облаку. Научите обрасце за имплементацију уз коришћење ONNX Runtime убрзања, WebGPU извршавања и хибридних RAG искустава. Укључује Chainlit RAG демонстрацију са локалним моделом и опционално истраживање OpenWebUI. Прилагодићете WebGPU инференцијални стартер и проценити Phi у односу на GPT-OSS-20B у погледу способности и односа трошкова/перформанси.

## Циљеви учења

- **Упоредите** SLM и LLM у погледу кашњења, меморије и квалитета
- **Имплементирајте** моделе уз ONNXRuntime и (где је подржано) WebGPU
- **Покрените** инференцију у прегледачу (интерактивна демонстрација која чува приватност)
- **Интегришите** Chainlit RAG процес са локалним SLM позадинским системом
- **Процените** користећи лагане хеуристике за квалитет и трошкове

## Предуслови

- Завршене сесије 1–3
- Инсталиран `chainlit` (већ у `requirements.txt` за Module08)
- Прегледач који подржава WebGPU (Edge / Chrome најновији на Windows 11)
- Покренут Foundry Local (`foundry status`)

### Напомене за више платформи

Windows остаје примарно циљано окружење. За macOS програмере који чекају на нативне бинарне датотеке:
1. Покрените Foundry Local у Windows 11 виртуелној машини (Parallels / UTM) ИЛИ на удаљеној Windows радној станици.
2. Изложите услугу (подразумевани порт 5273) и подесите на macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Користите исте кораке за Python виртуелно окружење као у претходним сесијама.

Инсталација Chainlit (обе платформе):
```bash
pip install chainlit
```

## Ток демонстрације (30 мин)

### 1. Упоредите Phi (SLM) и GPT-OSS-20B (LLM) (6 мин)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Пратите: дубину одговора, тачност чињеница, стилску богатост, кашњење.

### 2. Убрзање уз ONNX Runtime (5 мин)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   set BENCH_MODELS=phi-4-mini
#   python Workshop\samples\session03\benchmark_oss_models.py
```

Посматрајте промене у пропусности након омогућавања GPU у односу на само CPU.

### 3. WebGPU инференција у прегледачу (6 мин)

Прилагодите стартер `04-webgpu-inference` (креирајте `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Отворите датотеку у прегледачу; посматрајте локалну рунду са ниским кашњењем.

### 4. Chainlit RAG апликација за ћаскање (7 мин)

Минимални `samples/04-cutting-edge/chainlit_app.py`:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Покрените:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Стартер пројекат: Прилагодите `04-webgpu-inference` (6 мин)

Испоруке:
- Замените логику за преузимање са стриминг токенима (користите `stream=True` варијанту ендпоинта када буде омогућена)
- Додајте графикон кашњења (на страни клијента) за Phi у односу на GPT-OSS-20B прекидаче
- Уградите RAG контекст унутар (текстуално поље за референтне документе)

## Хеуристике за процену

| Категорија | Phi-4-mini | GPT-OSS-20B | Опсервација |
|------------|------------|-------------|-------------|
| Кашњење (хладно) | Брзо | Спорије | SLM се брзо загрева |
| Меморија | Ниска | Висока | Изводљивост на уређају |
| Придржавање контекста | Добро | Јако | Већи модел може бити опширнији |
| Трошак (локално) | Минималан | Виши (ресурси) | Трговина енергије/времена |
| Најбољи случај употребе | Апликације на ивици | Дубоко резоновање | Могућа хибридна архитектура |

## Валидација окружења

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python Workshop\samples\session03\benchmark_oss_models.py
```

## Решавање проблема

| Симптом | Узрок | Акција |
|---------|-------|--------|
| Неуспех преузимања веб странице | CORS или услуга није доступна | Користите `curl` за проверу ендпоинта; омогућите CORS прокси ако је потребно |
| Chainlit празан | Окружење није активно | Активирајте venv и поново инсталирајте зависности |
| Високо кашњење | Модел је управо учитан | Загрејте са малом секвенцом упита |

## Референце

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit документација: https://docs.chainlit.io
- RAG процена (Ragas): https://docs.ragas.io

---

**Трајање сесије**: 30 мин  
**Тежина**: Напредно

## Пример сценарија и мапирање радионице

| Артефакти радионице | Сценарио | Циљ | Извор података / упита |
|---------------------|----------|-----|------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Тим за архитектуру који процењује SLM и LLM за генератор резимеа за извршне извештаје | Квантификујте разлику у кашњењу и употреби токена | Једна `COMPARE_PROMPT` променљива окружења |
| `chainlit_app.py` (RAG демонстрација) | Прототип интерног асистента за знање | Утемељите кратке одговоре уз минимално лексичко преузимање | Уграђена `DOCS` листа у датотеци |
| `webgpu_demo.html` | Преглед футуристичке инференције у прегледачу на уређају | Прикажите локалну рунду са ниским кашњењем + наратив корисничког искуства | Само упит уживо корисника |

### Наратив сценарија
Продукт организација жели генератор резимеа за извршне извештаје. Лагани SLM (phi‑4‑mini) прави нацрте резимеа; већи LLM (gpt‑oss‑20b) може да преради само извештаје високог приоритета. Скрипте сесије бележе емпиријске метрике кашњења и токена како би оправдале хибридни дизајн, док Chainlit демонстрација илуструје како утемељено преузимање одржава одговоре малог модела чињенично тачним. Концептна страница WebGPU пружа визију за потпуно процесирање на страни клијента када убрзање прегледача сазри.

### Минимални RAG контекст (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Хибридни ток Нацрт→Прерада (Псеудо)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Пратите обе компоненте кашњења како бисте пријавили просечне трошкове.

### Опционална побољшања

| Фокус | Побољшање | Зашто | Савет за имплементацију |
|-------|-----------|-------|-------------------------|
| Упоредне метрике | Пратите употребу токена + кашњење првог токена | Холистички поглед на перформансе | Користите побољшану скрипту за бенчмарк (Сесија 3) са `BENCH_STREAM=1` |
| Хибридна архитектура | Нацрт SLM → Прерада LLM | Смањите кашњење и трошкове | Генеришите са phi-4-mini, прерадите резиме уз gpt-oss-20b |
| Стриминг корисничког интерфејса | Боље корисничко искуство у Chainlit | Инкрементални фидбек | Користите `stream=True` када локални стриминг буде доступан; акумулирајте делове |
| WebGPU кеширање | Бржа JS иницијализација | Смањите трошкове поновне компилације | Кеширајте компилиране артефакте шедера (будућа могућност рунтайма) |
| Детерминистички QA сет | Праведно поређење модела | Уклоните варијансу | Фиксна листа упита + `temperature=0` за евалуационе рунде |
| Оцењивање излазних резултата | Структурирана перспектива квалитета | Превазиђите анегдоте | Једноставна рубрика: кохерентност / чињеничност / концизност (1–5) |
| Напомене о енергији / ресурсима | Дискусија у учионици | Прикажите трговине | Користите OS мониторе (`foundry system info`, Task Manager, `nvidia-smi`) + излазне резултате скрипте за бенчмарк |
| Емулација трошкова | Оправдање пре облака | Планирајте скалирање | Мапирајте токене на хипотетичне цене облака за TCO наратив |
| Декомпозиција кашњења | Идентификујте уска грла | Циљајте оптимизације | Мерите припрему упита, слање захтева, први токен, комплетно завршење |
| RAG + LLM резервна опција | Безбедносна мрежа за квалитет | Побољшајте тешке упите | Ако је дужина одговора SLM < праг или ниска поузданост → ескалирајте |

#### Пример хибридног обрасца Нацрт/Прерада

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Скица декомпозиције кашњења

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Користите доследну структуру мерења за све моделе ради праведног поређења.

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.