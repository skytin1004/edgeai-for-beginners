<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1b3c0fecfd713c2df903a0633249dc9",
  "translation_date": "2025-10-09T14:25:12+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "fi"
}
-->
# Istunto 4: Tutustu huippumalleihin – LLM:t, SLM:t ja laitepohjainen päättely

## Tiivistelmä

Vertaa suuria kielimalleja (LLM:t) ja pieniä kielimalleja (SLM:t) paikallisen ja pilvipohjaisen päättelyn skenaarioissa. Opi käyttöönoton malleja hyödyntäen ONNX Runtime -kiihdytystä, WebGPU-suoritusta ja hybridisiä RAG-kokemuksia. Sisältää Chainlit RAG -demon paikallisella mallilla sekä valinnaisen OpenWebUI-tutkimuksen. Mukautat WebGPU-päättelyn aloitusprojektin ja arvioit Phi:n ja GPT-OSS-20B:n kyvykkyyttä sekä kustannus/suorituskyky -vaihtokauppoja.

## Oppimistavoitteet

- **Vertaa** SLM:ää ja LLM:ää viiveen, muistin ja laadun osalta
- **Ota käyttöön** malleja ONNXRuntime:lla ja (missä tuettu) WebGPU:lla
- **Suorita** selaimen kautta tapahtuva päättely (yksityisyyttä säilyttävä interaktiivinen demo)
- **Integroi** Chainlit RAG -putki paikallisen SLM-taustajärjestelmän kanssa
- **Arvioi** kevyillä laatu- ja kustannusheuristiikoilla

## Esivaatimukset

- Istunnot 1–3 suoritettu
- `chainlit` asennettuna (jo mukana `requirements.txt`-tiedostossa Module08:lle)
- WebGPU-yhteensopiva selain (Edge / Chrome uusin versio Windows 11:ssä)
- Foundry Local käynnissä (`foundry status`)

### Alustojen väliset huomiot

Windows on ensisijainen kohdeympäristö. macOS-kehittäjille, jotka odottavat natiivibinaareja:
1. Aja Foundry Local Windows 11 -virtuaalikoneessa (Parallels / UTM) TAI etä-Windows-työasemalla.
2. Avaa palvelu (oletusportti 5273) ja aseta macOS:ssä:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Käytä samoja Python-virtuaaliympäristön vaiheita kuin aiemmissa istunnoissa.

Chainlit-asennus (molemmilla alustoilla):
```bash
pip install chainlit
```

## Demon kulku (30 min)

### 1. Vertaa Phi (SLM) ja GPT-OSS-20B (LLM) (6 min)

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

Seuraa: vastausten syvyyttä, faktatarkkuutta, tyylillistä rikkautta, viivettä.

### 2. ONNX Runtime -kiihdytys (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   set BENCH_MODELS=phi-4-mini
#   python Workshop\samples\session03\benchmark_oss_models.py
```

Tarkkaile läpimenomuutoksia GPU:n ja vain CPU:n käytön välillä.

### 3. WebGPU-päättely selaimessa (6 min)

Mukauta aloitusprojektia `04-webgpu-inference` (luo `samples/04-cutting-edge/webgpu_demo.html`):

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

Avaa tiedosto selaimessa; tarkkaile matalan viiveen paikallista kierrosta.

### 4. Chainlit RAG -chat-sovellus (7 min)

Minimaalinen `samples/04-cutting-edge/chainlit_app.py`:

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

Suorita:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Aloitusprojekti: Mukauta `04-webgpu-inference` (6 min)

Toimitettavat:
- Korvaa paikkamerkkien hakulogiikka suoratoistotokenilla (käytä `stream=True` -päätepistevarianttia, kun se on käytössä)
- Lisää viivekaavio (asiakaspuolella) Phi:n ja GPT-OSS-20B:n vaihtamiseksi
- Upota RAG-konteksti suoraan (tekstialue viitedokumenteille)

## Arviointiheuristiikat

| Kategoria | Phi-4-mini | GPT-OSS-20B | Havainto |
|-----------|------------|-------------|----------|
| Viive (kylmä) | Nopea | Hitaampi | SLM lämpenee nopeasti |
| Muisti | Matala | Korkea | Laitteen toteutettavuus |
| Kontekstin noudattaminen | Hyvä | Vahva | Suurempi malli voi olla sanallisesti rikkaampi |
| Kustannus (paikallinen) | Vähäinen | Korkeampi (resurssi) | Energia/aika -vaihtokauppa |
| Paras käyttötapaus | Reuna-sovellukset | Syvä päättely | Hybridiputki mahdollinen |

## Ympäristön validointi

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python Workshop\samples\session03\benchmark_oss_models.py
```

## Vianetsintä

| Oire | Syy | Toimenpide |
|------|-----|-----------|
| Verkkosivun haku epäonnistuu | CORS tai palvelu alhaalla | Käytä `curl` varmistaaksesi päätepisteen; ota käyttöön CORS-välityspalvelin tarvittaessa |
| Chainlit tyhjä | Ympäristö ei aktiivinen | Aktivoi venv ja asenna riippuvuudet uudelleen |
| Korkea viive | Malli juuri ladattu | Lämmitä pienellä kehotussekvenssillä |

## Viitteet

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit-dokumentaatio: https://docs.chainlit.io
- RAG-arviointi (Ragas): https://docs.ragas.io

---

**Istunnon kesto**: 30 min  
**Vaikeustaso**: Edistynyt

## Esimerkkiskenaario ja työpajan kartoitus

| Työpajan artefaktit | Skenaario | Tavoite | Data / Kehotuslähde |
|---------------------|----------|---------|---------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Arkkitehtitiimi arvioi SLM:ää ja LLM:ää johtoryhmän tiivistelmägeneraattorille | Kvantifioi viive + tokenien käyttöero | Yksi `COMPARE_PROMPT` ympäristömuuttuja |
| `chainlit_app.py` (RAG-demo) | Sisäinen tietämyksen avustajaprototyyppi | Perusta lyhyet vastaukset minimaaliseen leksikaaliseen hakuun | Tiedoston sisäinen `DOCS`-lista |
| `webgpu_demo.html` | Tulevaisuuden laitepohjainen selaimen päättelyesikatselu | Näytä matalan viiveen paikallinen kierros + UX-narratiivi | Vain käyttäjän live-kehotus |

### Skenaarion narratiivi
Tuoteorganisaatio haluaa johtoryhmän tiivistelmägeneraattorin. Kevyt SLM (phi‑4‑mini) luonnostelee tiivistelmät; suurempi LLM (gpt‑oss‑20b) voi viimeistellä vain korkean prioriteetin raportit. Istunnon skriptit tallentavat empiiriset viive- ja tokenimittarit hybridisuunnittelun perustelemiseksi, kun taas Chainlit-demo havainnollistaa, kuinka perusteltu haku pitää pienen mallin vastaukset faktapohjaisina. WebGPU-konseptisivu tarjoaa vision täysin asiakaspuolen prosessoinnille, kun selaimen kiihdytys kehittyy.

### Minimaalinen RAG-konteksti (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hybridiluonnos→Viimeistelyvirtaus (Pseudokoodi)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Seuraa molempia viivekomponentteja raportoidaksesi yhdistetyn keskimääräisen kustannuksen.

### Valinnaiset parannukset

| Painopiste | Parannus | Miksi | Toteutusvinkki |
|------------|----------|-------|----------------|
| Vertailumetriikat | Seuraa tokenien käyttöä + ensimmäisen tokenin viivettä | Kokonaisvaltainen suorituskykykuva | Käytä parannettua vertailuskriptiä (Istunto 3) `BENCH_STREAM=1` kanssa |
| Hybridiputki | SLM luonnos → LLM viimeistely | Vähennä viivettä ja kustannuksia | Luo phi-4-mini:llä, viimeistele tiivistelmä gpt-oss-20b:llä |
| Suoratoisto-UI | Parempi UX Chainlitissä | Jatkuva palaute | Käytä `stream=True`, kun paikallinen suoratoisto on käytössä; kerää osia |
| WebGPU-välimuisti | Nopeampi JS-initialisointi | Vähennä uudelleenkääntämisen ylikuormitusta | Välimuisti käännetyille shader-artefakteille (tuleva runtime-ominaisuus) |
| Deterministinen QA-sarja | Reilu mallivertailu | Poista vaihtelu | Kiinteä kehotuslista + `temperature=0` arviointiajoille |
| Tulosten pisteytys | Rakenteellinen laatulinssi | Siirry anekdooteista eteenpäin | Yksinkertainen rubriikki: johdonmukaisuus / faktapohjaisuus / tiiviys (1–5) |
| Energia / resurssihuomiot | Luokkahuonekeskustelu | Näytä vaihtokaupat | Käytä OS-monitoreita (`foundry system info`, Tehtävienhallinta, `nvidia-smi`) + vertailuskriptin tuloksia |
| Kustannusemulointi | Pilven perustelu etukäteen | Suunnittele skaalaus | Kartta tokenit hypoteettiseen pilvihinnoitteluun TCO-narratiiville |
| Viiveen erittely | Tunnista pullonkaulat | Kohdista optimoinnit | Mittaa kehotuksen valmistelu, pyynnön lähetys, ensimmäinen token, täydellinen suoritus |
| RAG + LLM-varajärjestelmä | Laadun turvaverkko | Paranna vaikeita kyselyitä | Jos SLM-vastaus on lyhyt tai matala luottamus → eskaloi |

#### Esimerkki hybridiluonnos/viimeistelymallista

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Viiveen erittelyluonnos

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Käytä johdonmukaista mittauskehystä mallien välillä reilujen vertailujen varmistamiseksi.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.