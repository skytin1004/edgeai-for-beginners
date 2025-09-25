<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "562ac0eae12d808c9f45fbb77eb5c84f",
  "translation_date": "2025-09-25T02:44:10+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "lt"
}
-->
# Pavyzdys 04: Produkcijos pokalbių programos su Chainlit

Išsamus pavyzdys, parodantis įvairius būdus, kaip kurti produkcijai paruoštas pokalbių programas naudojant Microsoft Foundry Local, įskaitant modernias interneto sąsajas, srautinį atsakymų pateikimą ir pažangias naršyklės technologijas.

## Kas įtraukta

- **🚀 Chainlit pokalbių programa** (`app.py`): Produkcijai paruošta pokalbių programa su srautiniu atsakymų pateikimu
- **🌐 WebGPU demonstracija** (`webgpu-demo/`): AI apdorojimas naršyklėje su aparatūros pagreitinimu
- **🎨 Open WebUI integracija** (`open-webui-guide.md`): Profesionali sąsaja, panaši į ChatGPT
- **📚 Mokomasis užrašų knygelė** (`chainlit_app.ipynb`): Interaktyvios mokymosi medžiagos

## Greitas startas

### 1. Chainlit pokalbių programa

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Atidaroma adresu: `http://localhost:8080`

### 2. WebGPU naršyklės demonstracija

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Atidaroma adresu: `http://localhost:5173`

### 3. Open WebUI nustatymas

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Atidaroma adresu: `http://localhost:3000`

## Architektūros modeliai

### Vietinis vs debesų sprendimų matrica

| Scenarijus | Rekomendacija | Priežastis |
|------------|---------------|------------|
| **Privatūs duomenys** | 🏠 Vietinis (Foundry) | Duomenys niekada nepalieka įrenginio |
| **Sudėtingas mąstymas** | ☁️ Debesys (Azure OpenAI) | Prieiga prie didesnių modelių |
| **Realaus laiko pokalbiai** | 🏠 Vietinis (Foundry) | Mažesnė delsė, greitesni atsakymai |
| **Dokumentų analizė** | 🔄 Hibridinis | Vietinis ištraukimas, debesų analizė |
| **Kodo generavimas** | 🏠 Vietinis (Foundry) | Privatumas + specializuoti modeliai |
| **Tyrimų užduotys** | ☁️ Debesys (Azure OpenAI) | Reikalinga plati žinių bazė |

### Technologijų palyginimas

| Technologija | Naudojimo atvejis | Privalumai | Trūkumai |
|--------------|-------------------|------------|----------|
| **Chainlit** | Python programuotojams, greitas prototipavimas | Lengvas nustatymas, srautinė parama | Tik Python |
| **WebGPU** | Maksimalus privatumas, neprisijungus | Naršyklės integracija, nereikia serverio | Ribotas modelio dydis |
| **Open WebUI** | Produkcijos diegimas, komandos | Profesionali sąsaja, vartotojų valdymas | Reikalingas Docker |

## Reikalavimai

- **Foundry Local**: Įdiegta ir veikia ([Atsisiųsti](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ su virtualia aplinka
- **Modelis**: Bent vienas įkeltas (`foundry model run phi-4-mini`)
- **Naršyklė**: Chrome/Edge su WebGPU palaikymu demonstracijoms
- **Docker**: Open WebUI (neprivaloma)

## Diegimas ir nustatymas

### 1. Python aplinkos nustatymas

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local nustatymas

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

## Pavyzdinės programos

### Chainlit pokalbių programa

**Funkcijos:**
- 🚀 **Realaus laiko srautas**: Žodžiai rodomi, kai jie generuojami
- 🛡️ **Patikima klaidų tvarkyba**: Sklandus veikimas ir atkūrimas
- 🎨 **Moderni sąsaja**: Profesionali pokalbių sąsaja iš karto
- 🔧 **Lankstus konfigūravimas**: Aplinkos kintamieji ir automatinis aptikimas
- 📱 **Prisitaikantis dizainas**: Veikia tiek kompiuteryje, tiek mobiliajame įrenginyje

**Greitas startas:**
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

### WebGPU naršyklės demonstracija

**Funkcijos:**
- 🌐 **AI naršyklėje**: Nereikia serverio, veikia tik naršyklėje
- ⚡ **WebGPU pagreitinimas**: Aparatūros pagreitinimas, kai įmanoma
- 🔒 **Maksimalus privatumas**: Duomenys niekada nepalieka įrenginio
- 🎯 **Nereikia diegti**: Veikia bet kurioje suderinamoje naršyklėje
- 🔄 **Sklandus atsarginis variantas**: Pereina prie CPU, jei WebGPU nepasiekiamas

**Paleidimas:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI integracija

**Funkcijos:**
- 🎨 **ChatGPT tipo sąsaja**: Profesionali, pažįstama sąsaja
- 👥 **Daugelio vartotojų palaikymas**: Vartotojų paskyros ir pokalbių istorija
- 📁 **Failų apdorojimas**: Įkelkite ir analizuokite dokumentus
- 🔄 **Modelių keitimas**: Lengvas perjungimas tarp skirtingų modelių
- 🐳 **Docker diegimas**: Produkcijai paruoštas konteinerizuotas nustatymas

**Greitas nustatymas:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Konfigūracijos nuoroda

### Aplinkos kintamieji

| Kintamasis | Aprašymas | Numatytasis | Pavyzdys |
|------------|-----------|-------------|----------|
| `MODEL` | Naudojamas modelio alias | `phi-4-mini` | `qwen2.5-7b-instruct` |
| `BASE_URL` | Foundry Local adresas | Automatiškai aptinkamas | `http://localhost:51211` |
| `API_KEY` | API raktas (neprivalomas vietiniam) | `""` | `your-api-key` |

## Trikčių šalinimas

### Dažnos problemos

**Chainlit programa:**

1. **Paslauga nepasiekiama:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Portų konfliktai:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python aplinkos problemos:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU demonstracija:**

1. **WebGPU nepalaikoma:**
   - Atnaujinkite į Chrome/Edge 113+
   - Įjunkite WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Patikrinkite GPU statusą: `chrome://gpu`
   - Demonstracija automatiškai pereis prie CPU

2. **Modelio įkėlimo klaidos:**
   - Užtikrinkite interneto ryšį modelio atsisiuntimui
   - Patikrinkite naršyklės konsolę dėl CORS klaidų
   - Įsitikinkite, kad naudojate HTTP (ne file://)

**Open WebUI:**

1. **Ryšys atmestas:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modeliai nerodomi:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Patikros sąrašas

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

## Pažangus naudojimas

### Našumo optimizavimas

**Chainlit:**
- Naudokite srautą geresniam našumo įspūdžiui
- Įgyvendinkite ryšio telkinį dideliam vartotojų skaičiui
- Talpinkite modelio atsakymus pakartotiniams užklausoms
- Stebėkite atminties naudojimą su didelėmis pokalbių istorijomis

**WebGPU:**
- Naudokite WebGPU maksimaliai privatumui ir greičiui
- Įgyvendinkite modelio kvantavimą mažesniems modeliams
- Naudokite Web Workers foniniam apdorojimui
- Talpinkite kompiliuotus modelius naršyklės saugykloje

**Open WebUI:**
- Naudokite nuolatinius tomus pokalbių istorijai
- Konfigūruokite resursų limitus Docker konteineriui
- Įgyvendinkite duomenų atsargines kopijas
- Nustatykite atvirkštinį proxy SSL užtikrinimui

### Integracijos modeliai

**Hibridinis vietinis/debesų:**
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

**Daugiarūšis vamzdynas:**
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

## Produkcijos diegimas

### Saugumo aspektai

- **API raktai**: Naudokite aplinkos kintamuosius, niekada nekoduokite
- **Tinklas**: Naudokite HTTPS produkcijoje, apsvarstykite VPN komandos prieigai
- **Prieigos kontrolė**: Įgyvendinkite autentifikaciją Open WebUI
- **Duomenų privatumas**: Audituokite, kurie duomenys lieka vietiniai, o kurie keliauja į debesį
- **Atnaujinimai**: Nuolat atnaujinkite Foundry Local ir konteinerius

### Stebėjimas ir priežiūra

- **Sveikatos patikros**: Įgyvendinkite galinių taškų stebėjimą
- **Žurnalai**: Centralizuokite visų komponentų žurnalus
- **Metrijos**: Stebėkite atsakymo laikus, klaidų dažnį, resursų naudojimą
- **Atsarginės kopijos**: Reguliariai kurkite pokalbių duomenų ir konfigūracijų atsargines kopijas

## Nuorodos ir ištekliai

### Dokumentacija
- [Chainlit dokumentacija](https://docs.chainlit.io/) - Išsamus sistemos vadovas
- [Foundry Local dokumentacija](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Oficialūs Microsoft dokumentai
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU integracija
- [Open WebUI dokumentacija](https://docs.openwebui.com/) - Pažangus konfigūravimas

### Pavyzdiniai failai
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produkcijos Chainlit programa
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Mokomasis užrašų knygelė
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - AI apdorojimas naršyklėje
- [`open-webui-guide.md`](./open-webui-guide.md) - Pilnas Open WebUI nustatymas

### Susiję pavyzdžiai
- [4 sesijos dokumentacija](../../04.CuttingEdgeModels.md) - Pilnas sesijos vadovas
- [Foundry Local pavyzdžiai](https://github.com/microsoft/foundry-local/tree/main/samples) - Oficialūs pavyzdžiai

---

