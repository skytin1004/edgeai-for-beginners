<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1b3c0fecfd713c2df903a0633249dc9",
  "translation_date": "2025-10-09T14:24:31+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "da"
}
-->
# Session 4: Udforsk Banebrydende Modeller – LLMs, SLMs & On-Device Inference

## Resumé

Sammenlign Large Language Models (LLMs) og Small Language Models (SLMs) i lokale vs cloud-baserede inferensscenarier. Lær implementeringsmønstre ved hjælp af ONNX Runtime-acceleration, WebGPU-eksekvering og hybride RAG-oplevelser. Inkluderer en Chainlit RAG-demo med en lokal model samt en valgfri udforskning af OpenWebUI. Du vil tilpasse en WebGPU-inferensstarter og evaluere Phi vs GPT-OSS-20B med hensyn til kapabilitet og omkostnings-/ydelsesafvejninger.

## Læringsmål

- **Sammenlign** SLM og LLM med hensyn til latenstid, hukommelse og kvalitet
- **Implementer** modeller med ONNXRuntime og (hvor understøttet) WebGPU
- **Kør** browserbaseret inferens (privatlivsbevarende interaktiv demo)
- **Integrer** en Chainlit RAG-pipeline med en lokal SLM-backend
- **Evaluer** ved hjælp af lette kvalitets- og omkostningsheuristikker

## Forudsætninger

- Sessioner 1–3 gennemført
- `chainlit` installeret (allerede i `requirements.txt` for Module08)
- WebGPU-kompatibel browser (seneste version af Edge / Chrome på Windows 11)
- Foundry Local kørende (`foundry status`)

### Bemærkninger om platforme

Windows forbliver det primære målsystem. For macOS-udviklere, der venter på native binære filer:
1. Kør Foundry Local i en Windows 11 VM (Parallels / UTM) ELLER på en fjern Windows-arbejdsstation.
2. Eksponer tjenesten (standardport 5273) og indstil på macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Brug de samme Python-virtuelle miljøtrin som i tidligere sessioner.

Installation af Chainlit (begge platforme):
```bash
pip install chainlit
```

## Demo-forløb (30 min)

### 1. Sammenlign Phi (SLM) vs GPT-OSS-20B (LLM) (6 min)

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

Spor: svardybde, faktuel nøjagtighed, stilistisk rigdom, latenstid.

### 2. ONNX Runtime-acceleration (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   set BENCH_MODELS=phi-4-mini
#   python Workshop\samples\session03\benchmark_oss_models.py
```

Observer ændringer i gennemløb efter aktivering af GPU vs kun CPU.

### 3. WebGPU-inferens i browser (6 min)

Tilpas starteren `04-webgpu-inference` (opret `samples/04-cutting-edge/webgpu_demo.html`):

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

Åbn filen i en browser; observer lav-latenstid lokal rundtur.

### 4. Chainlit RAG Chat App (7 min)

Minimal `samples/04-cutting-edge/chainlit_app.py`:

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

Kør:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Starterprojekt: Tilpas `04-webgpu-inference` (6 min)

Leverancer:
- Erstat pladsholder-fetch-logik med streaming tokens (brug `stream=True` endpoint-variant, når den er aktiveret)
- Tilføj latenstidsdiagram (klientside) for phi vs gpt-oss-20b skift
- Indlejre RAG-kontekst inline (tekstområde til referencedokumenter)

## Evalueringsheuristikker

| Kategori | Phi-4-mini | GPT-OSS-20B | Observation |
|----------|------------|-------------|-------------|
| Latenstid (kold) | Hurtig | Langsommere | SLM varmer hurtigt op |
| Hukommelse | Lav | Høj | Enhedens gennemførlighed |
| Kontekstoverholdelse | God | Stærk | Større model kan være mere ordrig |
| Omkostninger (lokalt) | Minimal | Højere (ressourcer) | Energi-/tidsafvejning |
| Bedste anvendelse | Edge-apps | Dybdegående ræsonnement | Hybrid pipeline mulig |

## Validering af miljø

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python Workshop\samples\session03\benchmark_oss_models.py
```

## Fejlfinding

| Symptom | Årsag | Handling |
|---------|-------|--------|
| Websidehentning mislykkes | CORS eller tjeneste nede | Brug `curl` til at verificere endpoint; aktiver CORS-proxy, hvis nødvendigt |
| Chainlit blank | Miljø ikke aktivt | Aktivér venv & geninstaller afhængigheder |
| Høj latenstid | Model netop indlæst | Varm op med lille promptsekvens |

## Referencer

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG-evaluering (Ragas): https://docs.ragas.io

---

**Sessionens varighed**: 30 min  
**Sværhedsgrad**: Avanceret

## Eksempelscenarie & Workshop-kortlægning

| Workshop-artefakter | Scenarie | Mål | Data / Prompt-kilde |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Arkitekturteam, der evaluerer SLM vs LLM til generering af ledelsesresuméer | Kvantificer forskelle i latenstid + tokenforbrug | Enkelt `COMPARE_PROMPT` miljøvariabel |
| `chainlit_app.py` (RAG-demo) | Prototype på intern vidensassistent | Underbyg korte svar med minimal leksikal retrieval | Indlejret `DOCS`-liste i filen |
| `webgpu_demo.html` | Fremtidig on-device browser-inferensforhåndsvisning | Vis lav-latenstid lokal rundtur + UX-fortælling | Kun live bruger-prompt |

### Scenariefortælling
Produktorganisationen ønsker en generator til ledelsesbriefinger. En letvægts-SLM (phi‑4‑mini) udarbejder resuméer; en større LLM (gpt‑oss‑20b) kan kun forfine højprioritetsrapporter. Sessionscripts indfanger empiriske latenstids- og tokenmålinger for at retfærdiggøre et hybridt design, mens Chainlit-demoen illustrerer, hvordan grounded retrieval holder små modelsvar faktuelle. WebGPU-konceptet giver en vision for fuldt klientbaseret behandling, når browseracceleration modnes.

### Minimal RAG-kontekst (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hybrid Udkast→Forfiningsflow (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Spor begge latenstidskomponenter for at rapportere gennemsnitlige blandede omkostninger.

### Valgfrie forbedringer

| Fokus | Forbedring | Hvorfor | Implementeringshint |
|-------|------------|---------|---------------------|
| Sammenligningsmetrikker | Spor tokenforbrug + første-token-latenstid | Holistisk præstationsoversigt | Brug forbedret benchmark-script (Session 3) med `BENCH_STREAM=1` |
| Hybrid pipeline | SLM-udkast → LLM-forfining | Reducer latenstid & omkostninger | Generer med phi-4-mini, forfin resumé med gpt-oss-20b |
| Streaming-UI | Bedre UX i Chainlit | Trinvis feedback | Brug `stream=True`, når lokal streaming er eksponeret; akkumuler bidder |
| WebGPU-caching | Hurtigere JS-initialisering | Reducer genkompileringsoverhead | Cache kompilerede shader-artefakter (fremtidig runtime-funktionalitet) |
| Determineret QA-sæt | Retfærdig model-sammenligning | Fjern variation | Fast promptliste + `temperature=0` til evalueringskørsler |
| Outputscoring | Struktureret kvalitetslinse | Gå ud over anekdoter | Simpel rubric: sammenhæng / faktualitet / kortfattethed (1–5) |
| Energi-/ressourcenoter | Klasseværelsesdiskussion | Vis afvejninger | Brug OS-overvågning (`foundry system info`, Task Manager, `nvidia-smi`) + benchmark-scriptuddata |
| Omkostningsefterligning | Forudgående cloud-berettigelse | Planlæg skalering | Kortlæg tokens til hypotetisk cloud-prisfastsættelse for TCO-fortælling |
| Latenstidsnedbrydning | Identificer flaskehalse | Målrettede optimeringer | Mål promptforberedelse, forespørgselssending, første token, fuld færdiggørelse |
| RAG + LLM-backup | Kvalitetssikkerhedsnet | Forbedr vanskelige forespørgsler | Hvis SLM-svarlængde < tærskel eller lav tillid → eskaler |

#### Eksempel på hybrid udkast/forfiningsmønster

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Skitse af latenstidsnedbrydning

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Brug konsistente målingsrammer på tværs af modeller for retfærdige sammenligninger.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.