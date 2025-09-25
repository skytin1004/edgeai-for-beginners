<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "562ac0eae12d808c9f45fbb77eb5c84f",
  "translation_date": "2025-09-25T01:05:15+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "sw"
}
-->
# Mfano 04: Programu za Gumzo za Uzalishaji na Chainlit

Mfano wa kina unaoonyesha mbinu mbalimbali za kujenga programu za gumzo zinazofaa kwa uzalishaji kwa kutumia Microsoft Foundry Local, zikiwa na miingiliano ya kisasa ya wavuti, majibu ya mtiririko, na teknolojia za kisasa za kivinjari.

## Yaliyomo

- **🚀 Chainlit Chat App** (`app.py`): Programu ya gumzo inayofaa kwa uzalishaji na mtiririko wa majibu
- **🌐 WebGPU Demo** (`webgpu-demo/`): Utoaji wa AI kupitia kivinjari na kasi ya vifaa
- **🎨 Ujumuishaji wa Open WebUI** (`open-webui-guide.md`): Muonekano wa kitaalamu kama ChatGPT
- **📚 Daftari la Elimu** (`chainlit_app.ipynb`): Vifaa vya kujifunza vya maingiliano

## Kuanza Haraka

### 1. Programu ya Gumzo ya Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Fungua: `http://localhost:8080`

### 2. Demo ya WebGPU Kivinjari

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Fungua: `http://localhost:5173`

### 3. Usanidi wa Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Fungua: `http://localhost:3000`

## Mifumo ya Usanifu

### Uamuzi wa Kati ya Local na Cloud

| Hali | Pendekezo | Sababu |
|------|-----------|--------|
| **Data Nyeti ya Faragha** | 🏠 Local (Foundry) | Data haiondoki kwenye kifaa |
| **Uchambuzi Mgumu** | ☁️ Cloud (Azure OpenAI) | Ufikiaji wa mifano mikubwa zaidi |
| **Gumzo la Wakati Halisi** | 🏠 Local (Foundry) | Ucheleweshaji mdogo, majibu ya haraka |
| **Uchambuzi wa Nyaraka** | 🔄 Mseto | Local kwa uchimbaji, cloud kwa uchambuzi |
| **Uzalishaji wa Nambari** | 🏠 Local (Foundry) | Faragha + mifano maalum |
| **Kazi za Utafiti** | ☁️ Cloud (Azure OpenAI) | Hifadhidata pana ya maarifa inahitajika |

### Ulinganisho wa Teknolojia

| Teknolojia | Matumizi | Faida | Hasara |
|------------|----------|-------|-------|
| **Chainlit** | Watengenezaji wa Python, prototyping ya haraka | Usanidi rahisi, msaada wa mtiririko | Python pekee |
| **WebGPU** | Faragha ya juu, hali za nje ya mtandao | Asili ya kivinjari, hakuna seva inayohitajika | Ukubwa wa mfano mdogo |
| **Open WebUI** | Utekelezaji wa uzalishaji, timu | UI ya kitaalamu, usimamizi wa watumiaji | Inahitaji Docker |

## Mahitaji

- **Foundry Local**: Imewekwa na inafanya kazi ([Pakua](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ na mazingira ya kawaida
- **Mfano**: Angalau mmoja umepakiwa (`foundry model run phi-4-mini`)
- **Kivinjari**: Chrome/Edge na msaada wa WebGPU kwa maonyesho
- **Docker**: Kwa Open WebUI (hiari)

## Usanidi na Kuweka

### 1. Usanidi wa Mazingira ya Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Usanidi wa Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Programu za Mfano

### Programu ya Gumzo ya Chainlit

**Vipengele:**
- 🚀 **Mtiririko wa Wakati Halisi**: Tokeni zinaonekana zinapozalishwa
- 🛡️ **Ushughulikiaji wa Makosa Imara**: Kushuka kwa neema na urejeshaji
- 🎨 **UI ya Kisasa**: Muonekano wa kitaalamu wa gumzo moja kwa moja
- 🔧 **Usanidi Rahisi**: Vigezo vya mazingira na utambuzi wa kiotomatiki
- 📱 **Muundo wa Kujibika**: Inafanya kazi kwenye desktop na vifaa vya mkononi

**Kuanza Haraka:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b-instruct
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### Demo ya WebGPU Kivinjari

**Vipengele:**
- 🌐 **AI Asilia ya Kivinjari**: Hakuna seva inayohitajika, inafanya kazi kabisa kwenye kivinjari
- ⚡ **Uharakishaji wa WebGPU**: Kasi ya vifaa inapopatikana
- 🔒 **Faragha ya Juu**: Data haiondoki kwenye kifaa chako
- 🎯 **Hakuna Usanidi**: Inafanya kazi kwenye kivinjari chochote kinachofaa
- 🔄 **Urejeshaji wa Neema**: Inarudi kwa CPU ikiwa WebGPU haipatikani

**Kuendesha:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Ujumuishaji wa Open WebUI

**Vipengele:**
- 🎨 **Muonekano kama ChatGPT**: UI ya kitaalamu, inayofahamika
- 👥 **Msaada wa Watumiaji Wengi**: Akaunti za watumiaji na historia ya mazungumzo
- 📁 **Usindikaji wa Faili**: Pakia na uchambue nyaraka
- 🔄 **Kubadilisha Mfano**: Kubadilisha kwa urahisi kati ya mifano tofauti
- 🐳 **Utekelezaji wa Docker**: Usanidi wa uzalishaji uliofungashwa

**Usanidi Haraka:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Marejeleo ya Usanidi

### Vigezo vya Mazingira

| Kigezo | Maelezo | Chaguo-msingi | Mfano |
|--------|---------|--------------|-------|
| `MODEL` | Jina la mfano wa kutumia | `phi-4-mini` | `qwen2.5-7b-instruct` |
| `BASE_URL` | Endpoint ya Foundry Local | Inatambuliwa kiotomatiki | `http://localhost:51211` |
| `API_KEY` | API key (hiari kwa local) | `""` | `your-api-key` |

## Utatuzi wa Matatizo

### Masuala ya Kawaida

**Programu ya Chainlit:**

1. **Huduma haipatikani:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Migongano ya Port:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Masuala ya mazingira ya Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Demo ya WebGPU:**

1. **WebGPU haijaungwa mkono:**
   - Sasisha hadi Chrome/Edge 113+
   - Washa WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Angalia hali ya GPU: `chrome://gpu`
   - Demo itarudi kwa CPU kiotomatiki

2. **Makosa ya kupakia mfano:**
   - Hakikisha muunganisho wa intaneti kwa kupakua mfano
   - Angalia console ya kivinjari kwa makosa ya CORS
   - Hakikisha unatumia kupitia HTTP (sio file://)

**Open WebUI:**

1. **Muunganisho umekataliwa:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Mifano haionekani:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Orodha ya Uthibitishaji

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Matumizi ya Juu

### Uboreshaji wa Utendaji

**Chainlit:**
- Tumia mtiririko kwa utendaji bora unaoonekana
- Tekeleza pooling ya muunganisho kwa ushirikiano wa juu
- Hifadhi majibu ya mfano kwa maswali yanayojirudia
- Fuata matumizi ya kumbukumbu na historia kubwa ya mazungumzo

**WebGPU:**
- Tumia WebGPU kwa faragha na kasi ya juu
- Tekeleza quantization ya mfano kwa mifano midogo
- Tumia Web Workers kwa usindikaji wa nyuma
- Hifadhi mifano iliyosanikwa kwenye hifadhi ya kivinjari

**Open WebUI:**
- Tumia volumes za kudumu kwa historia ya mazungumzo
- Sanidi mipaka ya rasilimali kwa kontena la Docker
- Tekeleza mikakati ya kuhifadhi nakala kwa data ya watumiaji
- Sanidi proxy ya nyuma kwa kumaliza SSL

### Mifumo ya Ujumuishaji

**Mseto Local/Cloud:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Njia ya Multi-Modal:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Utekelezaji wa Uzalishaji

### Masuala ya Usalama

- **API Keys**: Tumia vigezo vya mazingira, usiwahi kuweka moja kwa moja
- **Mtandao**: Tumia HTTPS katika uzalishaji, fikiria VPN kwa ufikiaji wa timu
- **Udhibiti wa Ufikiaji**: Tekeleza uthibitishaji kwa Open WebUI
- **Faragha ya Data**: Kagua data inayobaki local dhidi ya inayokwenda cloud
- **Sasisho**: Weka Foundry Local na kontena zikiwa zimesasishwa

### Ufuatiliaji na Matengenezo

- **Ukaguzi wa Afya**: Tekeleza ufuatiliaji wa endpoint
- **Kumbukumbu**: Kumbukumbu za kati kutoka kwa vipengele vyote
- **Metriki**: Fuata nyakati za majibu, viwango vya makosa, matumizi ya rasilimali
- **Hifadhi Nakala**: Hifadhi nakala mara kwa mara ya data ya mazungumzo na usanidi

## Marejeleo na Rasilimali

### Nyaraka
- [Chainlit Documentation](https://docs.chainlit.io/) - Mwongozo kamili wa mfumo
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Nyaraka rasmi za Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Ujumuishaji wa WebGPU
- [Open WebUI Documentation](https://docs.openwebui.com/) - Usanidi wa hali ya juu

### Faili za Mfano
- [`app.py`](../../../../../Module08/samples/04/app.py) - Programu ya Chainlit ya uzalishaji
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Daftari la elimu
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Utoaji wa AI kupitia kivinjari
- [`open-webui-guide.md`](./open-webui-guide.md) - Usanidi kamili wa Open WebUI

### Sampuli Zinazohusiana
- [Session 4 Documentation](../../04.CuttingEdgeModels.md) - Mwongozo kamili wa kikao
- [Foundry Local Samples](https://github.com/microsoft/foundry-local/tree/main/samples) - Sampuli rasmi

---

