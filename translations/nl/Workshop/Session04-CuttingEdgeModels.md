<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1b3c0fecfd713c2df903a0633249dc9",
  "translation_date": "2025-10-09T16:40:02+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "nl"
}
-->
# Sessie 4: Verken Geavanceerde Modellen – LLMs, SLMs & On-Device Inference

## Samenvatting

Vergelijk Large Language Models (LLMs) en Small Language Models (SLMs) voor lokale versus cloud-inferentiescenario's. Leer implementatiepatronen met ONNX Runtime-versnelling, WebGPU-uitvoering en hybride RAG-ervaringen. Inclusief een Chainlit RAG-demo met een lokaal model en een optionele verkenning van OpenWebUI. Je past een WebGPU-inferentiestarter aan en evalueert Phi versus GPT-OSS-20B op capaciteiten en afwegingen tussen kosten en prestaties.

## Leerdoelen

- **Vergelijk** SLM en LLM op het gebied van latentie, geheugen en kwaliteit
- **Implementeer** modellen met ONNXRuntime en (waar ondersteund) WebGPU
- **Voer uit** browsergebaseerde inferentie (privacyvriendelijke interactieve demo)
- **Integreer** een Chainlit RAG-pijplijn met een lokale SLM-backend
- **Evalueer** met behulp van lichte kwaliteits- en kostenheuristieken

## Vereisten

- Sessies 1–3 voltooid
- `chainlit` geïnstalleerd (al opgenomen in `requirements.txt` voor Module08)
- WebGPU-compatibele browser (Edge / Chrome nieuwste versie op Windows 11)
- Foundry Local actief (`foundry status`)

### Cross-platform opmerkingen

Windows blijft de primaire doelomgeving. Voor macOS-ontwikkelaars die wachten op native binaries:
1. Voer Foundry Local uit in een Windows 11 VM (Parallels / UTM) OF een externe Windows-werkstation.
2. Stel de service bloot (standaardpoort 5273) en configureer op macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Gebruik dezelfde stappen voor de Python-virtuele omgeving als in eerdere sessies.

Chainlit-installatie (beide platforms):
```bash
pip install chainlit
```

## Demo Flow (30 min)

### 1. Vergelijk Phi (SLM) versus GPT-OSS-20B (LLM) (6 min)

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

Volg: diepte van antwoorden, feitelijke nauwkeurigheid, stilistische rijkdom, latentie.

### 2. ONNX Runtime-versnelling (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   set BENCH_MODELS=phi-4-mini
#   python Workshop\samples\session03\benchmark_oss_models.py
```

Observeer doorvoerveranderingen na het inschakelen van GPU versus alleen CPU.

### 3. WebGPU-inferentie in browser (6 min)

Pas starter `04-webgpu-inference` aan (maak `samples/04-cutting-edge/webgpu_demo.html`):

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

Open het bestand in een browser; observeer de lokale ronde met lage latentie.

### 4. Chainlit RAG Chat App (7 min)

Minimaal `samples/04-cutting-edge/chainlit_app.py`:

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

Voer uit:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Starterproject: Pas `04-webgpu-inference` aan (6 min)

Resultaten:
- Vervang tijdelijke fetch-logica door streaming tokens (gebruik `stream=True` endpointvariant zodra ingeschakeld)
- Voeg een latentiekaart toe (client-side) voor Phi versus GPT-OSS-20B schakelingen
- Embed RAG-context inline (tekstvak voor referentiedocumenten)

## Evaluatieheuristieken

| Categorie | Phi-4-mini | GPT-OSS-20B | Observatie |
|-----------|------------|-------------|------------|
| Latentie (koud) | Snel | Langzamer | SLM warmt snel op |
| Geheugen | Laag | Hoog | Geschiktheid voor apparaat |
| Contextnauwkeurigheid | Goed | Sterk | Groter model kan meer uitgebreid zijn |
| Kosten (lokaal) | Minimaal | Hoger (resources) | Afweging energie/tijd |
| Beste gebruiksscenario | Edge-apps | Diepgaand redeneren | Hybride pijplijn mogelijk |

## Validatie van omgeving

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python Workshop\samples\session03\benchmark_oss_models.py
```

## Probleemoplossing

| Symptoom | Oorzaak | Actie |
|----------|---------|-------|
| Webpagina ophalen mislukt | CORS of service niet actief | Gebruik `curl` om endpoint te verifiëren; schakel CORS-proxy in indien nodig |
| Chainlit leeg | Omgeving niet actief | Activeer venv en installeer afhankelijkheden opnieuw |
| Hoge latentie | Model net geladen | Warm op met een kleine promptreeks |

## Referenties

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG Evaluatie (Ragas): https://docs.ragas.io

---

**Sessieduur**: 30 min  
**Moeilijkheidsgraad**: Geavanceerd

## Voorbeeldscenario & Workshopmapping

| Workshopartefacten | Scenario | Doelstelling | Data / Promptbron |
|--------------------|----------|--------------|-------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Architectuurteam evalueert SLM versus LLM voor generator van samenvattingen voor leidinggevenden | Kwantificeer latentie + tokengebruikverschillen | Enkele `COMPARE_PROMPT` omgevingsvariabele |
| `chainlit_app.py` (RAG-demo) | Prototype interne kennisassistent | Onderbouw korte antwoorden met minimale lexicale opvraging | Inline `DOCS` lijst in bestand |
| `webgpu_demo.html` | Futuristische on-device browser-inferentie preview | Toon lokale ronde met lage latentie + UX-verhaal | Alleen live gebruikersprompt |

### Scenarioverhaal
De productorganisatie wil een generator voor samenvattingen voor leidinggevenden. Een lichte SLM (phi‑4‑mini) maakt concepten; een grotere LLM (gpt‑oss‑20b) kan alleen prioritaire rapporten verfijnen. Sessiescripts leggen empirische latentie- en tokenstatistieken vast om een hybride ontwerp te rechtvaardigen, terwijl de Chainlit-demo illustreert hoe onderbouwde opvraging kleine modelantwoorden feitelijk houdt. De WebGPU-conceptpagina biedt een toekomstvisie voor volledig client-side verwerking wanneer browseracceleratie volwassen wordt.

### Minimale RAG-context (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hybride Concept→Verfijn Flow (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Volg beide latentiecomponenten om een gemiddelde gecombineerde kostprijs te rapporteren.

### Optionele verbeteringen

| Focus | Verbetering | Waarom | Implementatiehint |
|-------|------------|-------|-------------------|
| Vergelijkende statistieken | Volg tokengebruik + latentie van eerste token | Holistisch prestatieoverzicht | Gebruik verbeterd benchmarkscript (Sessie 3) met `BENCH_STREAM=1` |
| Hybride pijplijn | SLM concept → LLM verfijnen | Verminder latentie en kosten | Genereer met phi-4-mini, verfijn samenvatting met gpt-oss-20b |
| Streaming UI | Betere UX in Chainlit | Incrementele feedback | Gebruik `stream=True` zodra lokale streaming beschikbaar is; verzamel chunks |
| WebGPU-caching | Snellere JS-initialisatie | Verminder hercompileeroverhead | Cache gecompileerde shaderartefacten (toekomstige runtimecapaciteit) |
| Deterministische QA-set | Eerlijke modelvergelijking | Verwijder variatie | Vaste promptlijst + `temperature=0` voor evaluatieruns |
| Outputscoring | Gestructureerde kwaliteitslens | Verder dan anekdotes | Eenvoudige rubric: samenhang / feitelijkheid / beknoptheid (1–5) |
| Energie / Resource-opmerkingen | Klassikale discussie | Toon afwegingen | Gebruik OS-monitors (`foundry system info`, Taakbeheer, `nvidia-smi`) + benchmarkscriptuitvoer |
| Kostenemulatie | Pre-cloud rechtvaardiging | Plan schaalvergroting | Map tokens naar hypothetische cloudprijzen voor TCO-verhaal |
| Latentieontleding | Identificeer knelpunten | Richt optimalisaties | Meet promptvoorbereiding, verzoekverzending, eerste token, volledige voltooiing |
| RAG + LLM fallback | Kwaliteitsvangnet | Verbeter moeilijke vragen | Als SLM-antwoordsnelheid < drempel of lage zekerheid → escaleren |

#### Voorbeeld Hybride Concept/Verfijn Patroon

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Latentieontledingsschets

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Gebruik consistente meetstructuren over modellen heen voor eerlijke vergelijkingen.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.