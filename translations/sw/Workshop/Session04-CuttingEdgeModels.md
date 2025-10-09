<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1b3c0fecfd713c2df903a0633249dc9",
  "translation_date": "2025-10-09T21:08:23+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "sw"
}
-->
# Kipindi cha 4: Kuchunguza Miundo ya Kisasa – LLMs, SLMs & Utoaji wa Nadharia Kwenye Kifaa

## Muhtasari

Linganisheni Large Language Models (LLMs) na Small Language Models (SLMs) kwa hali za nadharia za ndani dhidi ya wingu. Jifunze mifumo ya kupelekwa kwa kutumia kasi ya ONNX Runtime, utekelezaji wa WebGPU, na uzoefu wa mseto wa RAG. Inajumuisha demo ya Chainlit RAG na modeli ya ndani pamoja na chaguo la kuchunguza OpenWebUI. Utarekebisha mwanzo wa nadharia ya WebGPU na kutathmini uwezo wa Phi dhidi ya GPT-OSS-20B na biashara ya gharama/utendaji.

## Malengo ya Kujifunza

- **Linganisheni** SLM dhidi ya LLM kwa viwango vya ucheleweshaji, kumbukumbu, na ubora
- **Pelekwa** modeli kwa ONNXRuntime na (pale inapowezekana) WebGPU
- **Endesha** nadharia inayotegemea kivinjari (demo ya maingiliano inayohifadhi faragha)
- **Unganisha** bomba la Chainlit RAG na mfumo wa nyuma wa SLM wa ndani
- **Tathmini** kwa kutumia viashiria vya ubora + gharama vyepesi

## Mahitaji ya Awali

- Vipindi 1–3 vimekamilika
- `chainlit` imewekwa (tayari kwenye `requirements.txt` kwa Module08)
- Kivinjari chenye uwezo wa WebGPU (Edge / Chrome ya hivi karibuni kwenye Windows 11)
- Foundry Local inafanya kazi (`foundry status`)

### Vidokezo vya Msalaba wa Majukwaa

Windows inabaki kuwa mazingira lengwa. Kwa watengenezaji wa macOS wanaosubiri binaries asilia:
1. Endesha Foundry Local kwenye VM ya Windows 11 (Parallels / UTM) AU workstation ya mbali ya Windows.
2. Fungua huduma (bandari ya chaguo-msingi 5273) na weka kwenye macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Tumia hatua sawa za mazingira ya kawaida ya Python kama vipindi vya awali.

Usakinishaji wa Chainlit (majukwaa yote):
```bash
pip install chainlit
```

## Mtiririko wa Demo (Dakika 30)

### 1. Linganisha Phi (SLM) dhidi ya GPT-OSS-20B (LLM) (Dakika 6)

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

Fuatilia: kina cha majibu, usahihi wa ukweli, utajiri wa mtindo, ucheleweshaji.

### 2. Kasi ya ONNX Runtime (Dakika 5)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   set BENCH_MODELS=phi-4-mini
#   python Workshop\samples\session03\benchmark_oss_models.py
```

Angalia mabadiliko ya kasi baada ya kuwezesha GPU dhidi ya CPU pekee.

### 3. Nadharia ya WebGPU Kwenye Kivinjari (Dakika 6)

Rekebisha mwanzo `04-webgpu-inference` (unda `samples/04-cutting-edge/webgpu_demo.html`):

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

Fungua faili kwenye kivinjari; angalia mzunguko wa ndani wa ucheleweshaji mdogo.

### 4. Programu ya Mazungumzo ya Chainlit RAG (Dakika 7)

`samples/04-cutting-edge/chainlit_app.py` ya msingi:

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

Endesha:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Mradi wa Mwanzo: Rekebisha `04-webgpu-inference` (Dakika 6)

Vitu vya kutolewa:
- Badilisha mantiki ya kuchukua nafasi na tokeni za kutiririsha (tumia `stream=True` toleo la mwisho mara tu linapowezeshwa)
- Ongeza chati ya ucheleweshaji (upande wa mteja) kwa Phi dhidi ya GPT-OSS-20B
- Weka muktadha wa RAG moja kwa moja (eneo la maandishi kwa nyaraka za marejeleo)

## Viashiria vya Tathmini

| Jamii | Phi-4-mini | GPT-OSS-20B | Uchunguzi |
|-------|------------|-------------|-----------|
| Ucheleweshaji (baridi) | Haraka | Polepole | SLM huwaka haraka |
| Kumbukumbu | Chini | Juu | Uwezekano wa kifaa |
| Uzingatiaji wa muktadha | Nzuri | Imara | Modeli kubwa inaweza kuwa verbose zaidi |
| Gharama (ndani) | Kidogo | Juu (rasilimali) | Biashara ya nishati/muda |
| Matumizi bora | Programu za ukingoni | Ufikiri wa kina | Bomba la mseto linawezekana |

## Kuhakiki Mazingira

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python Workshop\samples\session03\benchmark_oss_models.py
```

## Utatuzi wa Matatizo

| Dalili | Sababu | Hatua |
|--------|--------|-------|
| Kifaa cha wavuti hakifanyi kazi | CORS au huduma imezimwa | Tumia `curl` kuthibitisha endpoint; wezesha wakala wa CORS ikiwa inahitajika |
| Chainlit tupu | Mazingira hayajawashwa | Washa venv & weka tena utegemezi |
| Ucheleweshaji wa juu | Modeli imepakiwa tu | Washa na mlolongo mdogo wa maelezo |

## Marejeleo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- Tathmini ya RAG (Ragas): https://docs.ragas.io

---

**Muda wa Kipindi**: Dakika 30  
**Ugumu**: Juu

## Mfano wa Hali & Ulinganishaji wa Warsha

| Vifaa vya Warsha | Hali | Lengo | Chanzo cha Data / Maelezo |
|------------------|------|-------|--------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Timu ya usanifu inatathmini SLM dhidi ya LLM kwa jenereta ya muhtasari wa watendaji | Pima tofauti ya ucheleweshaji + matumizi ya tokeni | Kigezo cha mazingira `COMPARE_PROMPT` |
| `chainlit_app.py` (demo ya RAG) | Kielelezo cha msaidizi wa maarifa wa ndani | Jibu fupi zilizo na urejeshaji wa leksika mdogo | Orodha ya `DOCS` moja kwa moja kwenye faili |
| `webgpu_demo.html` | Muonekano wa nadharia ya kivinjari kwenye kifaa cha siku zijazo | Onyesha mzunguko wa ndani wa ucheleweshaji mdogo + hadithi ya UX | Maelezo ya mtumiaji wa moja kwa moja pekee |

### Hadithi ya Hali
Idara ya bidhaa inataka jenereta ya muhtasari wa watendaji. SLM nyepesi (phi‑4‑mini) huandika muhtasari; LLM kubwa (gpt‑oss‑20b) inaweza kuboresha ripoti za kipaumbele cha juu pekee. Script za kipindi zinakamata metrik za ucheleweshaji wa kimajaribio & tokeni ili kuhalalisha muundo wa mseto, wakati demo ya Chainlit inaonyesha jinsi urejeshaji ulioimarishwa unavyohakikisha majibu ya modeli ndogo ni ya ukweli. Ukurasa wa dhana wa WebGPU unatoa njia ya maono kwa usindikaji wa upande wa mteja kikamilifu wakati kasi ya kivinjari inakua.

### Muktadha wa RAG wa Kima cha Chini (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Mtiririko wa Mseto Rasimu→Kuboresha (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Fuatilia vipengele vyote vya ucheleweshaji ili kuripoti gharama ya wastani ya mchanganyiko.

### Uboreshaji wa Hiari

| Lengo | Uboreshaji | Sababu | Kidokezo cha Utekelezaji |
|-------|-----------|--------|-------------------------|
| Metrik za Kulinganisha | Fuatilia matumizi ya tokeni + ucheleweshaji wa tokeni ya kwanza | Mtazamo wa utendaji wa jumla | Tumia script ya benchmark iliyoboreshwa (Kipindi cha 3) na `BENCH_STREAM=1` |
| Bomba la Mseto | Rasimu ya SLM → Kuboresha na LLM | Punguza ucheleweshaji & gharama | Tengeneza na phi-4-mini, boresha muhtasari na gpt-oss-20b |
| UI ya Kutiririsha | UX bora katika Chainlit | Maoni ya hatua kwa hatua | Tumia `stream=True` mara tu kutiririsha kwa ndani kunapowezeshwa; kusanya vipande |
| Caching ya WebGPU | Mwanzo wa JS haraka | Punguza mzigo wa kuandaa tena | Hifadhi vifaa vya shader vilivyotayarishwa (uwezo wa runtime ya siku zijazo) |
| Seti ya QA ya Kiamua | Kulinganisha modeli kwa haki | Ondoa tofauti | Orodha ya maelezo ya kudumu + `temperature=0` kwa majaribio ya tathmini |
| Upimaji wa Matokeo | Lenzi ya ubora iliyopangwa | Pita maoni ya kawaida | Rubric rahisi: ushirikiano / ukweli / ufupi (1–5) |
| Vidokezo vya Nishati / Rasilimali | Majadiliano ya darasani | Onyesha biashara | Tumia vionyeshi vya OS (`foundry system info`, Task Manager, `nvidia-smi`) + matokeo ya script ya benchmark |
| Uigaji wa Gharama | Uhalalishaji wa kabla ya wingu | Panga upanuzi | Panga tokeni kwa bei ya wingu ya dhahania kwa hadithi ya TCO |
| Uchanganuzi wa Ucheleweshaji | Tambua vikwazo | Lenga uboreshaji | Pima maandalizi ya maelezo, kutuma ombi, tokeni ya kwanza, kukamilika kamili |
| RAG + LLM Fallback | Mtandao wa usalama wa ubora | Boresha maswali magumu | Ikiwa urefu wa jibu la SLM < kizingiti au ujasiri mdogo → panda |

#### Mfano wa Mtiririko wa Rasimu/Kuboresha wa Mseto

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Mchoro wa Uchanganuzi wa Ucheleweshaji

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Tumia muundo wa kipimo thabiti kwenye modeli zote kwa kulinganisha kwa haki.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.