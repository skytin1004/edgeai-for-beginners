<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "562ac0eae12d808c9f45fbb77eb5c84f",
  "translation_date": "2025-09-24T23:32:35+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "fi"
}
-->
# Esimerkki 04: Tuotantovalmiit Chat-sovellukset Chainlitillä

Kattava esimerkki, joka esittelee useita lähestymistapoja tuotantovalmiiden chat-sovellusten rakentamiseen Microsoft Foundry Localin avulla. Mukana modernit verkkokäyttöliittymät, suoratoistovastaukset ja uusimmat selainteknologiat.

## Mitä sisältyy

- **🚀 Chainlit Chat -sovellus** (`app.py`): Tuotantovalmiit chat-sovellukset suoratoistolla
- **🌐 WebGPU-demo** (`webgpu-demo/`): Selaimessa toimiva tekoälylaskenta laitteistokiihdytyksellä
- **🎨 Open WebUI -integraatio** (`open-webui-guide.md`): Ammattimainen ChatGPT-tyylinen käyttöliittymä
- **📚 Opetuksellinen muistikirja** (`chainlit_app.ipynb`): Interaktiiviset oppimateriaalit

## Pika-aloitus

### 1. Chainlit Chat -sovellus

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Avaa osoitteessa: `http://localhost:8080`

### 2. WebGPU-selain-demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Avaa osoitteessa: `http://localhost:5173`

### 3. Open WebUI -asennus

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Avaa osoitteessa: `http://localhost:3000`

## Arkkitehtuurimallit

### Paikallinen vs. pilvipohjainen päätösmatriisi

| Tilanne | Suositus | Perustelu |
|---------|----------|-----------|
| **Yksityiset tiedot** | 🏠 Paikallinen (Foundry) | Tiedot eivät poistu laitteelta |
| **Monimutkainen päättely** | ☁️ Pilvi (Azure OpenAI) | Pääsy suurempiin malleihin |
| **Reaaliaikainen chat** | 🏠 Paikallinen (Foundry) | Alhaisempi viive, nopeammat vastaukset |
| **Dokumenttianalyysi** | 🔄 Hybridi | Paikallinen tiedon poimintaan, pilvi analyysiin |
| **Koodin generointi** | 🏠 Paikallinen (Foundry) | Yksityisyys + erikoistuneet mallit |
| **Tutkimustehtävät** | ☁️ Pilvi (Azure OpenAI) | Laaja tietopohja tarpeen |

### Teknologiavertailu

| Teknologia | Käyttötapaus | Edut | Haitat |
|------------|--------------|------|--------|
| **Chainlit** | Python-kehittäjät, nopea prototyyppaus | Helppo asennus, suoratoistotuki | Vain Python |
| **WebGPU** | Maksimaalinen yksityisyys, offline-tilanteet | Selaimen sisäinen, ei palvelinta | Rajoitettu mallikoko |
| **Open WebUI** | Tuotantokäyttö, tiimit | Ammattimainen käyttöliittymä, käyttäjähallinta | Vaatii Dockerin |

## Esivaatimukset

- **Foundry Local**: Asennettu ja käynnissä ([Lataa](https://aka.ms/foundry-local-installer))
- **Python**: Versio 3.10+ virtuaaliympäristöllä
- **Malli**: Ainakin yksi ladattu (`foundry model run phi-4-mini`)
- **Selain**: Chrome/Edge WebGPU-tuella demoja varten
- **Docker**: Open WebUI:lle (valinnainen)

## Asennus ja käyttöönotto

### 1. Python-ympäristön asennus

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local -asennus

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

## Esimerkkisovellukset

### Chainlit Chat -sovellus

**Ominaisuudet:**
- 🚀 **Reaaliaikainen suoratoisto**: Tokenit näkyvät heti niiden luomisen jälkeen
- 🛡️ **Vahva virheenkäsittely**: Joustava toiminta ja palautuminen
- 🎨 **Moderni käyttöliittymä**: Ammattimainen chat-käyttöliittymä valmiina
- 🔧 **Joustava konfigurointi**: Ympäristömuuttujat ja automaattinen tunnistus
- 📱 **Responsiivinen suunnittelu**: Toimii sekä työpöydällä että mobiililaitteilla

**Pika-aloitus:**
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

### WebGPU-selain-demo

**Ominaisuudet:**
- 🌐 **Selaimen sisäinen tekoäly**: Ei palvelinta, toimii täysin selaimessa
- ⚡ **WebGPU-kiihdytys**: Laitteistokiihdytys, kun saatavilla
- 🔒 **Maksimaalinen yksityisyys**: Tiedot eivät koskaan poistu laitteeltasi
- 🎯 **Ei asennusta**: Toimii missä tahansa yhteensopivassa selaimessa
- 🔄 **Joustava varajärjestelmä**: Siirtyy CPU:lle, jos WebGPU ei ole käytettävissä

**Käynnistys:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI -integraatio

**Ominaisuudet:**
- 🎨 **ChatGPT-tyylinen käyttöliittymä**: Ammattimainen ja tuttu UI
- 👥 **Monikäyttäjätuki**: Käyttäjätilit ja keskusteluhistoria
- 📁 **Tiedostojen käsittely**: Lataa ja analysoi dokumentteja
- 🔄 **Mallien vaihto**: Helppo siirtyminen eri mallien välillä
- 🐳 **Docker-käyttöönotto**: Tuotantovalmis konttipohjainen asennus

**Pika-asennus:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Konfigurointiviite

### Ympäristömuuttujat

| Muuttuja | Kuvaus | Oletus | Esimerkki |
|----------|--------|--------|-----------|
| `MODEL` | Käytettävä mallin alias | `phi-4-mini` | `qwen2.5-7b-instruct` |
| `BASE_URL` | Foundry Local -päätepiste | Automaattisesti tunnistettu | `http://localhost:51211` |
| `API_KEY` | API-avain (valinnainen paikallisessa käytössä) | `""` | `your-api-key` |

## Vianmääritys

### Yleiset ongelmat

**Chainlit-sovellus:**

1. **Palvelu ei ole käytettävissä:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Porttikonfliktit:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python-ympäristöongelmat:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU-demo:**

1. **WebGPU ei tuettu:**
   - Päivitä Chrome/Edge versioon 113+
   - Ota WebGPU käyttöön: `chrome://flags/#enable-unsafe-webgpu`
   - Tarkista GPU-tila: `chrome://gpu`
   - Demo siirtyy automaattisesti CPU:lle

2. **Mallin latausvirheet:**
   - Varmista internet-yhteys mallin latausta varten
   - Tarkista selaimen konsolista CORS-virheet
   - Varmista, että käytät HTTP:tä (ei file://)

**Open WebUI:**

1. **Yhteys evätty:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Mallit eivät näy:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Tarkistuslista

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

## Edistynyt käyttö

### Suorituskyvyn optimointi

**Chainlit:**
- Käytä suoratoistoa paremman käyttäjäkokemuksen saavuttamiseksi
- Ota käyttöön yhteyksien uudelleenkäyttö korkean samanaikaisuuden tilanteissa
- Välimuista mallivastaukset toistuviin kyselyihin
- Seuraa muistinkäyttöä suurissa keskusteluhistorioissa

**WebGPU:**
- Käytä WebGPU:ta maksimaalisen yksityisyyden ja nopeuden saavuttamiseksi
- Toteuta mallien kvantisointi pienempiä malleja varten
- Käytä Web Workerseja taustaprosessointiin
- Välimuista käännetyt mallit selaimen tallennustilassa

**Open WebUI:**
- Käytä pysyviä volyymeja keskusteluhistorian tallentamiseen
- Määritä resurssirajoitukset Docker-kontille
- Toteuta varmuuskopiointistrategiat käyttäjätietoja varten
- Aseta käänteinen välityspalvelin SSL-päätteen asettamiseksi

### Integraatiomallit

**Hybridi paikallinen/pilvi:**
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

**Monimodaalinen putki:**
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

## Tuotantokäyttöönotto

### Tietoturvahuomiot

- **API-avaimet**: Käytä ympäristömuuttujia, älä koskaan kovakoodaa
- **Verkko**: Käytä HTTPS:ää tuotannossa, harkitse VPN:ää tiimikäyttöön
- **Pääsynhallinta**: Toteuta todennus Open WebUI:lle
- **Tietosuoja**: Tarkista, mitkä tiedot pysyvät paikallisina ja mitkä menevät pilveen
- **Päivitykset**: Pidä Foundry Local ja kontit ajan tasalla

### Seuranta ja ylläpito

- **Terveystarkistukset**: Toteuta päätepisteiden seuranta
- **Lokit**: Keskitä kaikkien komponenttien lokit
- **Metrikat**: Seuraa vasteaikoja, virheprosentteja ja resurssien käyttöä
- **Varmuuskopiointi**: Keskustelutietojen ja konfiguraatioiden säännöllinen varmuuskopiointi

## Viitteet ja resurssit

### Dokumentaatio
- [Chainlit-dokumentaatio](https://docs.chainlit.io/) - Kattava kehysopas
- [Foundry Local -dokumentaatio](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Microsoftin viralliset ohjeet
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU-integraatio
- [Open WebUI -dokumentaatio](https://docs.openwebui.com/) - Edistynyt konfigurointi

### Esimerkkitiedostot
- [`app.py`](../../../../../Module08/samples/04/app.py) - Tuotantovalmis Chainlit-sovellus
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Opetuksellinen muistikirja
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Selaimessa toimiva tekoälylaskenta
- [`open-webui-guide.md`](./open-webui-guide.md) - Täydellinen Open WebUI -asennusopas

### Liittyvät esimerkit
- [Session 4 Documentation](../../04.CuttingEdgeModels.md) - Täydellinen istunto-opas
- [Foundry Local -esimerkit](https://github.com/microsoft/foundry-local/tree/main/samples) - Viralliset esimerkit

---

