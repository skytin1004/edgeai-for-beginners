<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "562ac0eae12d808c9f45fbb77eb5c84f",
  "translation_date": "2025-09-24T22:49:53+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "sv"
}
-->
# Exempel 04: Produktionsklara chattapplikationer med Chainlit

Ett omfattande exempel som visar flera metoder för att bygga produktionsklara chattapplikationer med Microsoft Foundry Local, inklusive moderna webbgränssnitt, strömmande svar och avancerade webbläsarteknologier.

## Vad som ingår

- **🚀 Chainlit Chattapp** (`app.py`): Produktionsklar chattapplikation med strömmande svar
- **🌐 WebGPU Demo** (`webgpu-demo/`): AI-inferens i webbläsaren med hårdvaruacceleration
- **🎨 Open WebUI Integration** (`open-webui-guide.md`): Professionellt gränssnitt likt ChatGPT
- **📚 Utbildningsanteckningsbok** (`chainlit_app.ipynb`): Interaktiva lärmaterial

## Snabbstart

### 1. Chainlit Chattapplikation

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Öppnas på: `http://localhost:8080`

### 2. WebGPU Webbläsardemo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Öppnas på: `http://localhost:5173`

### 3. Open WebUI Installation

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Öppnas på: `http://localhost:3000`

## Arkitekturmönster

### Lokal vs Moln Beslutsmatris

| Scenario | Rekommendation | Orsak |
|----------|----------------|-------|
| **Integritetskänsliga data** | 🏠 Lokal (Foundry) | Data lämnar aldrig enheten |
| **Komplexa resonemang** | ☁️ Moln (Azure OpenAI) | Tillgång till större modeller |
| **Realtidschatt** | 🏠 Lokal (Foundry) | Lägre latens, snabbare svar |
| **Dokumentanalys** | 🔄 Hybrid | Lokal för extraktion, moln för analys |
| **Kodgenerering** | 🏠 Lokal (Foundry) | Integritet + specialiserade modeller |
| **Forskningsuppgifter** | ☁️ Moln (Azure OpenAI) | Kräver bred kunskapsbas |

### Teknologijämförelse

| Teknologi | Användningsområde | Fördelar | Nackdelar |
|-----------|-------------------|----------|-----------|
| **Chainlit** | Python-utvecklare, snabb prototypframtagning | Enkel installation, stöd för strömning | Endast Python |
| **WebGPU** | Maximal integritet, offline-scenarier | Webbläsarbaserad, ingen server behövs | Begränsad modellstorlek |
| **Open WebUI** | Produktionsdistribution, team | Professionellt gränssnitt, användarhantering | Kräver Docker |

## Förutsättningar

- **Foundry Local**: Installerad och igång ([Ladda ner](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ med virtuellt miljö
- **Modell**: Minst en laddad (`foundry model run phi-4-mini`)
- **Webbläsare**: Chrome/Edge med WebGPU-stöd för demo
- **Docker**: För Open WebUI (valfritt)

## Installation & Konfiguration

### 1. Python-miljöinställning

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local Konfiguration

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

## Exempelapplikationer

### Chainlit Chattapplikation

**Funktioner:**
- 🚀 **Realtidsströmning**: Tokens visas medan de genereras
- 🛡️ **Robust felhantering**: Smidig nedgradering och återhämtning
- 🎨 **Modernt gränssnitt**: Professionellt chattgränssnitt direkt
- 🔧 **Flexibel konfiguration**: Miljövariabler och automatisk upptäckt
- 📱 **Responsiv design**: Fungerar på både dator och mobila enheter

**Snabbstart:**
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

### WebGPU Webbläsardemo

**Funktioner:**
- 🌐 **Webbläsarbaserad AI**: Ingen server krävs, körs helt i webbläsaren
- ⚡ **WebGPU-acceleration**: Hårdvaruacceleration när tillgängligt
- 🔒 **Maximal integritet**: Ingen data lämnar din enhet
- 🎯 **Ingen installation**: Fungerar i alla kompatibla webbläsare
- 🔄 **Smidig fallback**: Faller tillbaka till CPU om WebGPU inte är tillgängligt

**Körning:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Integration

**Funktioner:**
- 🎨 **Gränssnitt likt ChatGPT**: Professionellt och välbekant UI
- 👥 **Stöd för flera användare**: Användarkonton och konversationshistorik
- 📁 **Filbearbetning**: Ladda upp och analysera dokument
- 🔄 **Modellväxling**: Enkel växling mellan olika modeller
- 🐳 **Docker-distribution**: Produktionsklar containerbaserad installation

**Snabbinstallation:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Konfigurationsreferens

### Miljövariabler

| Variabel | Beskrivning | Standard | Exempel |
|----------|-------------|----------|---------|
| `MODEL` | Modellalias att använda | `phi-4-mini` | `qwen2.5-7b-instruct` |
| `BASE_URL` | Foundry Local-endpunkt | Automatisk upptäckt | `http://localhost:51211` |
| `API_KEY` | API-nyckel (valfritt för lokal) | `""` | `your-api-key` |

## Felsökning

### Vanliga problem

**Chainlit-applikation:**

1. **Tjänsten är inte tillgänglig:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Portkonflikter:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problem med Python-miljö:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU Demo:**

1. **WebGPU stöds inte:**
   - Uppdatera till Chrome/Edge 113+
   - Aktivera WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Kontrollera GPU-status: `chrome://gpu`
   - Demo faller automatiskt tillbaka till CPU

2. **Fel vid modellinläsning:**
   - Kontrollera internetanslutning för modellnedladdning
   - Kontrollera webbläsarkonsolen för CORS-fel
   - Verifiera att du serverar via HTTP (inte file://)

**Open WebUI:**

1. **Anslutning nekad:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modeller visas inte:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Valideringschecklista

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

## Avancerad användning

### Prestandaoptimering

**Chainlit:**
- Använd strömning för bättre upplevd prestanda
- Implementera anslutningspooler för hög samtidighet
- Cacha modellens svar för upprepade frågor
- Övervaka minnesanvändning med stora konversationshistoriker

**WebGPU:**
- Använd WebGPU för maximal integritet och hastighet
- Implementera modellkvantisering för mindre modeller
- Använd Web Workers för bakgrundsprocesser
- Cacha kompilerade modeller i webbläsarens lagring

**Open WebUI:**
- Använd persistenta volymer för konversationshistorik
- Konfigurera resursbegränsningar för Docker-container
- Implementera backupstrategier för användardata
- Ställ in omvänd proxy för SSL-terminering

### Integrationsmönster

**Hybrid Lokal/Moln:**
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

**Multimodal Pipeline:**
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

## Produktionsdistribution

### Säkerhetsöverväganden

- **API-nycklar**: Använd miljövariabler, hårdkoda aldrig
- **Nätverk**: Använd HTTPS i produktion, överväg VPN för teamåtkomst
- **Åtkomstkontroll**: Implementera autentisering för Open WebUI
- **Dataintegritet**: Granska vilken data som stannar lokalt vs. skickas till molnet
- **Uppdateringar**: Håll Foundry Local och containrar uppdaterade

### Övervakning och underhåll

- **Hälsokontroller**: Implementera övervakning av slutpunkter
- **Loggning**: Centralisera loggar från alla komponenter
- **Mätvärden**: Spåra svarstider, felprocent, resursanvändning
- **Backup**: Regelbunden backup av konversationsdata och konfigurationer

## Referenser och resurser

### Dokumentation
- [Chainlit Dokumentation](https://docs.chainlit.io/) - Komplett ramverksguide
- [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Officiell Microsoft-dokumentation
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU-integration
- [Open WebUI Dokumentation](https://docs.openwebui.com/) - Avancerad konfiguration

### Exempelfiler
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produktionsklar Chainlit-applikation
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Utbildningsanteckningsbok
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - AI-inferens i webbläsaren
- [`open-webui-guide.md`](./open-webui-guide.md) - Komplett Open WebUI-installation

### Relaterade exempel
- [Session 4 Dokumentation](../../04.CuttingEdgeModels.md) - Komplett sessionsguide
- [Foundry Local Exempel](https://github.com/microsoft/foundry-local/tree/main/samples) - Officiella exempel

---

