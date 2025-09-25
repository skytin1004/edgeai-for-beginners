<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "562ac0eae12d808c9f45fbb77eb5c84f",
  "translation_date": "2025-09-25T01:14:26+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "hu"
}
-->
# Minta 04: Termelési Chat Alkalmazások Chainlit-tel

Egy átfogó minta, amely bemutatja a termelésre kész chat alkalmazások különböző megközelítéseit a Microsoft Foundry Local segítségével, modern webes felületekkel, streaming válaszokkal és legújabb böngészőtechnológiákkal.

## Tartalom

- **🚀 Chainlit Chat Alkalmazás** (`app.py`): Termelésre kész chat alkalmazás streaming funkcióval
- **🌐 WebGPU Demó** (`webgpu-demo/`): Böngészőalapú AI következtetés hardvergyorsítással
- **🎨 Open WebUI Integráció** (`open-webui-guide.md`): Professzionális ChatGPT-szerű felület
- **📚 Oktatási Jegyzetfüzet** (`chainlit_app.ipynb`): Interaktív tananyagok

## Gyorsindítás

### 1. Chainlit Chat Alkalmazás

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Elérhető itt: `http://localhost:8080`

### 2. WebGPU Böngésző Demó

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Elérhető itt: `http://localhost:5173`

### 3. Open WebUI Beállítás

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Elérhető itt: `http://localhost:3000`

## Architektúra Minták

### Helyi vs Felhő Döntési Mátrix

| Forgatókönyv | Ajánlás | Indoklás |
|--------------|---------|----------|
| **Adatvédelem érzékeny adatokkal** | 🏠 Helyi (Foundry) | Az adatok nem hagyják el az eszközt |
| **Komplex érvelés** | ☁️ Felhő (Azure OpenAI) | Nagyobb modellek elérése |
| **Valós idejű chat** | 🏠 Helyi (Foundry) | Alacsonyabb késleltetés, gyorsabb válaszok |
| **Dokumentum elemzés** | 🔄 Hibrid | Helyi kinyeréshez, felhő elemzéshez |
| **Kódgenerálás** | 🏠 Helyi (Foundry) | Adatvédelem + speciális modellek |
| **Kutatási feladatok** | ☁️ Felhő (Azure OpenAI) | Széleskörű tudásbázis szükséges |

### Technológiai Összehasonlítás

| Technológia | Használati eset | Előnyök | Hátrányok |
|-------------|-----------------|---------|-----------|
| **Chainlit** | Python fejlesztők, gyors prototípus készítés | Könnyű beállítás, streaming támogatás | Csak Python |
| **WebGPU** | Maximális adatvédelem, offline forgatókönyvek | Böngészőalapú, nincs szükség szerverre | Korlátozott modellméret |
| **Open WebUI** | Termelési telepítés, csapatok | Professzionális UI, felhasználókezelés | Docker szükséges |

## Előfeltételek

- **Foundry Local**: Telepítve és futtatva ([Letöltés](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ virtuális környezettel
- **Modell**: Legalább egy betöltve (`foundry model run phi-4-mini`)
- **Böngésző**: Chrome/Edge WebGPU támogatással a demókhoz
- **Docker**: Open WebUI-hoz (opcionális)

## Telepítés és Beállítás

### 1. Python Környezet Beállítása

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local Beállítása

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

## Minta Alkalmazások

### Chainlit Chat Alkalmazás

**Funkciók:**
- 🚀 **Valós idejű Streaming**: A tokenek azonnal megjelennek, ahogy generálódnak
- 🛡️ **Robusztus Hibakezelés**: Zökkenőmentes degradáció és helyreállítás
- 🎨 **Modern UI**: Professzionális chat felület alapértelmezés szerint
- 🔧 **Rugalmas Konfiguráció**: Környezeti változók és automatikus felismerés
- 📱 **Reszponzív Design**: Asztali és mobil eszközökön is működik

**Gyorsindítás:**
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

### WebGPU Böngésző Demó

**Funkciók:**
- 🌐 **Böngészőalapú AI**: Nincs szükség szerverre, teljesen böngészőben fut
- ⚡ **WebGPU Gyorsítás**: Hardvergyorsítás, ha elérhető
- 🔒 **Maximális Adatvédelem**: Az adatok soha nem hagyják el az eszközt
- 🎯 **Telepítés Nélkül**: Bármely kompatibilis böngészőben működik
- 🔄 **Zökkenőmentes Visszaesés**: CPU-ra vált, ha WebGPU nem elérhető

**Futtatás:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Integráció

**Funkciók:**
- 🎨 **ChatGPT-szerű Felület**: Professzionális, ismerős UI
- 👥 **Többfelhasználós Támogatás**: Felhasználói fiókok és beszélgetési előzmények
- 📁 **Fájlkezelés**: Dokumentumok feltöltése és elemzése
- 🔄 **Modellváltás**: Könnyű váltás különböző modellek között
- 🐳 **Docker Telepítés**: Termelésre kész konténeres beállítás

**Gyors Beállítás:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Konfigurációs Referencia

### Környezeti Változók

| Változó | Leírás | Alapértelmezett | Példa |
|---------|--------|-----------------|-------|
| `MODEL` | Használt modell alias | `phi-4-mini` | `qwen2.5-7b-instruct` |
| `BASE_URL` | Foundry Local végpont | Automatikusan felismerve | `http://localhost:51211` |
| `API_KEY` | API kulcs (opcionális helyi használathoz) | `""` | `your-api-key` |

## Hibakeresés

### Gyakori Problémák

**Chainlit Alkalmazás:**

1. **Szolgáltatás nem elérhető:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Port ütközések:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python környezeti problémák:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU Demó:**

1. **WebGPU nem támogatott:**
   - Frissítsen Chrome/Edge 113+ verzióra
   - Engedélyezze a WebGPU-t: `chrome://flags/#enable-unsafe-webgpu`
   - Ellenőrizze a GPU állapotát: `chrome://gpu`
   - A demó automatikusan CPU-ra vált

2. **Modell betöltési hibák:**
   - Biztosítsa az internetkapcsolatot a modell letöltéséhez
   - Ellenőrizze a böngésző konzolját CORS hibákért
   - Győződjön meg róla, hogy HTTP-n keresztül szolgáltat (nem file://)

**Open WebUI:**

1. **Kapcsolat megtagadva:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modellek nem jelennek meg:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Érvényesítési Ellenőrzőlista

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

## Haladó Használat

### Teljesítményoptimalizálás

**Chainlit:**
- Használjon streaminget a jobb észlelt teljesítmény érdekében
- Valósítson meg kapcsolat poolingot nagy egyidejűséghez
- Cache-elje a modell válaszait ismétlődő lekérdezésekhez
- Figyelje a memóriahasználatot nagy beszélgetési előzményeknél

**WebGPU:**
- Használja a WebGPU-t a maximális adatvédelem és sebesség érdekében
- Valósítson meg modell kvantálást kisebb modellekhez
- Használjon Web Worker-eket háttérfeldolgozáshoz
- Cache-elje a lefordított modelleket a böngésző tárolójában

**Open WebUI:**
- Használjon tartós köteteket a beszélgetési előzményekhez
- Konfigurálja az erőforrás-korlátokat a Docker konténerhez
- Valósítson meg biztonsági mentési stratégiákat a felhasználói adatokhoz
- Állítson be fordított proxy-t az SSL végrehajtásához

### Integrációs Minták

**Hibrid Helyi/Felhő:**
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

**Multi-Modális Folyamat:**
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

## Termelési Telepítés

### Biztonsági Szempontok

- **API Kulcsok**: Használjon környezeti változókat, soha ne kódolja be
- **Hálózat**: Használjon HTTPS-t termelésben, fontolja meg VPN használatát csapat hozzáféréshez
- **Hozzáférés-vezérlés**: Valósítson meg hitelesítést az Open WebUI-hoz
- **Adatvédelem**: Ellenőrizze, hogy mely adatok maradnak helyben, és melyek kerülnek a felhőbe
- **Frissítések**: Tartsa naprakészen a Foundry Local-t és a konténereket

### Felügyelet és Karbantartás

- **Egészségügyi Ellenőrzések**: Valósítson meg végpont monitorozást
- **Naplózás**: Centralizálja az összes komponens naplóit
- **Metrikák**: Kövesse nyomon a válaszidőket, hibaarányokat, erőforrás-használatot
- **Biztonsági Mentés**: Rendszeres biztonsági mentés a beszélgetési adatokhoz és konfigurációkhoz

## Referenciák és Források

### Dokumentáció
- [Chainlit Dokumentáció](https://docs.chainlit.io/) - Teljes keretrendszer útmutató
- [Foundry Local Dokumentáció](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Hivatalos Microsoft dokumentáció
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU integráció
- [Open WebUI Dokumentáció](https://docs.openwebui.com/) - Haladó konfiguráció

### Minta Fájlok
- [`app.py`](../../../../../Module08/samples/04/app.py) - Termelési Chainlit alkalmazás
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Oktatási jegyzetfüzet
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Böngészőalapú AI következtetés
- [`open-webui-guide.md`](./open-webui-guide.md) - Teljes Open WebUI beállítás

### Kapcsolódó Minták
- [4. Szekció Dokumentáció](../../04.CuttingEdgeModels.md) - Teljes szekció útmutató
- [Foundry Local Minták](https://github.com/microsoft/foundry-local/tree/main/samples) - Hivatalos minták

---

