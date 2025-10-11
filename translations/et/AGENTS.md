<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-11T10:59:04+00:00",
  "source_file": "AGENTS.md",
  "language_code": "et"
}
-->
# AGENTS.md

> **Arendajate juhend EdgeAI algajatele**
> 
> See dokument pakub põhjalikku teavet arendajatele, tehisintellekti agentidele ja kaastöötajatele, kes töötavad selle repositooriumiga. See hõlmab seadistamist, arendustöövooge, testimist ja parimaid tavasid.
> 
> **Viimati uuendatud**: oktoober 2025 | **Dokumendi versioon**: 2.0

## Sisukord

- [Projekti ülevaade](../..)
- [Repositooriumi struktuur](../..)
- [Eeltingimused](../..)
- [Seadistuskäsud](../..)
- [Arendustöövoog](../..)
- [Testimisjuhised](../..)
- [Koodistiili juhised](../..)
- [Pull Request'i juhised](../..)
- [Tõlkesüsteem](../..)
- [Foundry Local integratsioon](../..)
- [Ehitamine ja juurutamine](../..)
- [Levinud probleemid ja tõrkeotsing](../..)
- [Täiendavad ressursid](../..)
- [Projektispetsiifilised märkused](../..)
- [Abi saamine](../..)

## Projekti ülevaade

EdgeAI for Beginners on põhjalik hariduslik repositoorium, mis õpetab Edge AI arendamist väikeste keelemudelite (SLM) abil. Kursus hõlmab EdgeAI aluseid, mudelite juurutamist, optimeerimistehnikaid ja tootmiskõlblikke rakendusi, kasutades Microsoft Foundry Local'i ja erinevaid tehisintellekti raamistikke.

**Peamised tehnoloogiad:**
- Python 3.8+ (peamine keel AI/ML näidete jaoks)
- .NET C# (AI/ML näited)
- JavaScript/Node.js koos Electroniga (töölauarakenduste jaoks)
- Microsoft Foundry Local SDK
- Microsoft Windows ML
- VSCode AI Toolkit
- OpenAI SDK
- AI raamistikud: LangChain, Semantic Kernel, Chainlit
- Mudelite optimeerimine: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repositooriumi tüüp:** Haridusliku sisuga repositoorium, mis sisaldab 8 moodulit ja 10 põhjalikku näidisrakendust

**Arhitektuur:** Mitme mooduliga õpitee praktiliste näidetega, mis demonstreerivad Edge AI juurutusmustreid

## Repositooriumi struktuur

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Eeltingimused

### Vajalikud tööriistad

- **Python 3.8+** - AI/ML näidete ja märkmike jaoks
- **Node.js 16+** - Electroni näidisrakenduse jaoks
- **Git** - Versioonihalduseks
- **Microsoft Foundry Local** - AI mudelite kohalikuks käitamiseks

### Soovitatavad tööriistad

- **Visual Studio Code** - Python, Jupyter ja Pylance laiendustega
- **Windows Terminal** - Parema käsureakogemuse jaoks (Windowsi kasutajatele)
- **Docker** - Konteineripõhiseks arendamiseks (valikuline)

### Süsteeminõuded

- **RAM**: minimaalselt 8GB, soovitatavalt 16GB+ mitme mudeli stsenaariumide jaoks
- **Salvestusruum**: vähemalt 10GB vaba ruumi mudelite ja sõltuvuste jaoks
- **Operatsioonisüsteem**: Windows 10/11, macOS 11+ või Linux (Ubuntu 20.04+)
- **Riistvara**: AVX2 toega protsessor; GPU (CUDA, Qualcomm NPU) on valikuline, kuid soovitatav

### Teadmiste eeltingimused

- Pythoni programmeerimise põhialuste tundmine
- Käsurealiideste tundmine
- AI/ML kontseptsioonide mõistmine (näidiste arendamiseks)
- Git töövoogude ja pull request'i protsesside tundmine

## Seadistuskäsud

### Repositooriumi seadistamine

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Pythoni näidiste seadistamine (Moodul08 ja Pythoni näidised)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js näidise seadistamine (Näidis 08 - Windowsi vestlusrakendus)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local seadistamine

Foundry Local on vajalik näidiste käitamiseks. Laadi alla ja installi ametlikust repositooriumist:

**Paigaldamine:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Käsitsi**: Laadi alla [väljalaske lehelt](https://github.com/microsoft/Foundry-Local/releases)

**Kiirstart:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Märkus**: Foundry Local valib automaatselt teie riistvarale parima mudelivariandi (CUDA GPU, Qualcomm NPU või CPU).

## Arendustöövoog

### Sisu arendamine

See repositoorium sisaldab peamiselt **Markdowni haridussisu**. Muudatuste tegemisel:

1. Redigeeri `.md` faile vastavates moodulite kaustades
2. Järgi olemasolevaid vormindusmustreid
3. Veendu, et koodinäited on täpsed ja testitud
4. Uuenda vastavalt vajadusele ka tõlgitud sisu (või lase automatiseerimisel seda teha)

### Näidisrakenduste arendamine

Pythoni näidiste jaoks (näidised 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electroni näidise jaoks (näidis 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Näidisrakenduste testimine

Pythoni näidistel puuduvad automaatsed testid, kuid neid saab valideerida käivitamise teel:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electroni näidisel on testimistaristu:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testimisjuhised

### Sisu valideerimine

Repositoorium kasutab automaatseid tõlkevooge. Tõlgete käsitsi testimine pole vajalik.

**Käsitsi valideerimine sisu muudatuste korral:**
1. Vaata üle Markdowni renderdamine, eelvaadates `.md` faile
2. Veendu, et kõik lingid viivad kehtivatele sihtkohtadele
3. Testi dokumentatsioonis sisalduvaid koodinäiteid
4. Kontrolli, et pildid laaditakse õigesti

### Näidisrakenduste testimine

**Moodul08/näidised/08 (Electroni rakendus) sisaldab põhjalikku testimist:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Pythoni näidiseid tuleks testida käsitsi:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Koodistiili juhised

### Markdowni sisu

- Kasuta järjepidevat pealkirjade hierarhiat (# pealkirja jaoks, ## põhiosade jaoks, ### alajaotuste jaoks)
- Lisa koodiplokid keele määrangutega: ```python, ```bash, ```javascript
- Järgi olemasolevat vormindust tabelite, loendite ja rõhuasetuste jaoks
- Hoia read loetavad (~80-100 tähemärki, kuid mitte range reegel)
- Kasuta sisemiste viidete jaoks suhtelisi linke

### Pythoni koodistiil

- Järgi PEP 8 konventsioone
- Kasuta tüübi vihjeid, kui võimalik
- Lisa funktsioonidele ja klassidele dokumentatsioon
- Kasuta tähenduslikke muutujanimesid
- Hoia funktsioonid keskendunud ja lühikesed

### JavaScript/Node.js koodistiil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Peamised konventsioonid:**
- ESLint konfiguratsioon on saadaval näidises 08
- Prettier koodi vormindamiseks
- Kasuta kaasaegset ES6+ süntaksit
- Järgi olemasolevaid mustreid koodibaasis

## Pull Request'i juhised

### Kaastöövoog

1. **Fork'i repositoorium** ja loo uus haru `main` harust
2. **Tee oma muudatused**, järgides koodistiili juhiseid
3. **Testi põhjalikult**, kasutades ülaltoodud testimisjuhiseid
4. **Kommenteeri selgelt**, järgides konventsionaalsete commit'ide formaati
5. **Lükka oma fork'i** ja loo pull request
6. **Vasta tagasisidele**, mida hooldajad ülevaatuse käigus annavad

### Haru nimetamise konventsioon

- `feature/<moodul>-<kirjeldus>` - Uute funktsioonide või sisu jaoks
- `fix/<moodul>-<kirjeldus>` - Vigade parandamiseks
- `docs/<kirjeldus>` - Dokumentatsiooni täiustamiseks
- `refactor/<kirjeldus>` - Koodi refaktoreerimiseks

### Commit'i sõnumi formaat

Järgi [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Näited:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Pealkirja formaat
```
[ModuleXX] Brief description of change
```
või
```
[Module08/samples/XX] Description for sample changes
```

### Käitumisjuhend

Kõik kaastöötajad peavad järgima [Microsofti avatud lähtekoodiga käitumisjuhendit](https://opensource.microsoft.com/codeofconduct/). Palun tutvu [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) failiga enne kaastöö tegemist.

### Enne esitamist

**Sisu muudatuste korral:**
- Vaata üle kõik muudetud Markdowni failid
- Veendu, et lingid ja pildid töötavad
- Kontrolli õigekirja ja grammatikavigu

**Näidiskoodi muudatuste korral (Moodul08/näidised/08):**
```bash
npm run lint
npm test
```

**Pythoni näidiste muudatuste korral:**
- Testi, et näidis töötab edukalt
- Veendu, et veakäsitlus toimib
- Kontrolli ühilduvust Foundry Local'iga

### Ülevaatuse protsess

- Haridussisu muudatusi vaadatakse üle täpsuse ja selguse osas
- Koodinäidiseid testitakse funktsionaalsuse osas
- Tõlkeuuendusi haldab automaatselt GitHub Actions

## Tõlkesüsteem

**OLULINE:** See repositoorium kasutab automaatset tõlget GitHub Actions'i kaudu.

- Tõlked asuvad kaustas `/translations/` (üle 50 keele)
- Automatiseeritud `co-op-translator.yml` töövoo kaudu
- **ÄRGE muutke tõlkefailide sisu käsitsi** - need kirjutatakse üle
- Muutke ainult ingliskeelseid algfaile juur- ja moodulite kaustades
- Tõlked luuakse automaatselt, kui muudatused lükatakse `main` harusse

## Foundry Local integratsioon

Enamik Moodul08 näidiseid nõuab Microsoft Foundry Local'i töötamist.

### Paigaldamine ja seadistamine

**Paigalda Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Paigalda Pythoni SDK:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local'i käivitamine
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK kasutamine (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-3.5-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local'i kontrollimine
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Keskkonnamuutujad näidiste jaoks

Enamik näidiseid kasutab järgmisi keskkonnamuutujaid:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-3.5-mini  # or phi-4-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Märkus**: Kui kasutate `FoundryLocalManager`'i, haldab SDK automaatselt teenuste avastamist ja mudelite laadimist. Mudelite aliasid (nt `phi-3.5-mini`) kasutatakse parima variandi valimiseks teie riistvara jaoks.

## Ehitamine ja juurutamine

### Sisu juurutamine

See repositoorium on peamiselt dokumentatsioon - sisu jaoks pole ehitusprotsessi vaja.

### Näidisrakenduste ehitamine

**Electroni rakendus (Moodul08/näidised/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Pythoni näidised:**
Ehitamisprotsessi pole - näidised käivitatakse otse Pythoni tõlgiga.

## Levinud probleemid ja tõrkeotsing

> **Vihje**: Kontrolli [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) teadaolevate probleemide ja lahenduste kohta.

### Kriitilised probleemid (tõkestavad)

#### Foundry Local ei tööta
**Probleem:** Näidised ebaõnnestuvad ühendusvigade tõttu

**Lahendus:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-3.5-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Levinud probleemid (mõõdukad)

#### Pythoni virtuaalse keskkonna probleemid
**Probleem:** Mooduli importimise vead

**Lahendus:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electroni ehitamise probleemid
**Probleem:** npm installi või ehitamise vead

**Lahendus:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Töövoo probleemid (väiksemad)

#### Tõlkevoo konfliktid
**Probleem:** Tõlke PR on vastuolus teie muudatustega

**Lahendus:**
- Muutke ainult ingliskeelseid algfaile
- Laske automaatsel tõlkevoogul tõlked hallata
- Kui konfliktid tekivad, ühendage `main` oma haruga pärast tõlgete ühendamist

#### Mudeli allalaadimise vead
**Probleem:** Foundry Local ei suuda mudeleid alla laadida

**Lahendus:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Täiendavad ressursid

### Õppeteed
- **Algajate tee:** Moodulid 01-02 (7-9 tundi)
- **Kesktase:** Moodulid 03-04 (9-11 tundi)
- **Edasijõudnud:** Moodulid 05-07 (12-15 tundi)
- **Ekspertide tee:** Moodul 08 (8-10 tundi)

### Olulised mooduli sisud
- **Moodul01:** EdgeAI alused ja reaalsed juhtumiuuringud
- **Moodul02:** Väikeste keelemudelite (SLM) perekonnad ja arhitektuurid
- **Moodul03:** Kohalikud ja pilvepõhised juurutusstrateegiad
- **Moodul04:** Mudelite optimeerimine mitme raamistiku abil
- **Moodul05:** SLMOps - tootmistoimingud
- **Moodul06:** AI agendid ja funktsioonide kutsumine
- **Moodul07:** Platvormispetsiifilised rakendused
- **Moodul08:** Foundry Local tööriistakomplekt 10 põhjaliku näidisega

### Välised sõltuvused
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Kohalik AI mudelite käituskeskkond OpenAI-ühilduva API-ga
  - [Dokumentatsioon](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Pythoni SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScripti SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimeerimisraamistik
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Mudelite optimeerimise tööriistakomplekt
- [OpenVINO](https://docs.openvino.ai/) - Inteli optimeerimise tööriistakomplekt

## Projektispetsiifilised märkused

### Moodul08 näidisrakendused

Repositoorium sisaldab 10 põhjalikku näidisrakendust:

1. **01-REST Chat Quickstart** - Põhiline OpenAI SDK integreerimine
2. **02-OpenAI SDK integreerimine** - Täiustatud SDK funktsioonid
3. **03-Mudelite avastamine ja võrdlemine** - Mudelite võrdlustööriistad
4. **04-Chainlit RAG rakendus** - Otsingupõhine generatsioon
5. **05-Multi-Agent Orchestration** - Põhiline agentide koordineerimine
6. **06-Models-as-Tools Router** - Nutikas mudelite suunamine
7. **07-Otsene API klient** - Madala taseme API integreerimine
8. **08-Windows 11 vestlusrakendus** - Kohalik Electroni töölauarakendus
9. **09-Täiustatud multi-agent süsteem** - Keeruline agentide koordineerimine
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel integratsioon

Iga näidis demonstreerib erinevaid Edge AI ar
- Kohalik järeldamine pakub 50-500ms vastuseaegu  
- Kvantiseerimistehnikad saavutavad 75% suuruse vähendamise, säilitades 85% jõudlusest  
- Reaalajas vestlusvõimalused kohalike mudelitega  

### Turvalisus ja privaatsus  

- Kogu töötlemine toimub kohapeal - andmeid pilve ei saadeta  
- Sobib privaatsustundlikele rakendustele (tervishoid, rahandus)  
- Vastab andmesuveräänsuse nõuetele  
- Foundry Local töötab täielikult kohalikul riistvaral  

## Abi saamine  

### Dokumentatsioon  

- **Peamine README**: [README.md](README.md) - Repositooriumi ülevaade ja õppejuhised  
- **Õppejuhend**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Õpperessursid ja ajakava  
- **Tugi**: [SUPPORT.md](SUPPORT.md) - Kuidas abi saada  
- **Turvalisus**: [SECURITY.md](SECURITY.md) - Turvaküsimuste raporteerimine  

### Kogukonna tugi  

- **GitHubi probleemid**: [Teata vigadest või taotle funktsioone](https://github.com/microsoft/edgeai-for-beginners/issues)  
- **GitHubi arutelud**: [Esita küsimusi ja jaga ideid](https://github.com/microsoft/edgeai-for-beginners/discussions)  
- **Foundry Local probleemid**: [Tehnilised probleemid Foundry Localiga](https://github.com/microsoft/Foundry-Local/issues)  

### Kontakt  

- **Hooldajad**: Vaata [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)  
- **Turvaküsimused**: Järgi vastutustundlikku avalikustamist [SECURITY.md](SECURITY.md)  
- **Microsofti tugi**: Ettevõtte toe jaoks võta ühendust Microsofti klienditeenindusega  

### Lisamaterjalid  

- **Microsoft Learn**: [AI ja masinõppe õpperajad](https://learn.microsoft.com/training/browse/?products=ai-services)  
- **Foundry Local dokumentatsioon**: [Ametlikud dokumendid](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)  
- **Kogukonna näidised**: Vaata [GitHubi arutelud](https://github.com/microsoft/edgeai-for-beginners/discussions) kogukonna panuste jaoks  

---

**See on hariduslik repositoorium, mis keskendub Edge AI arenduse õpetamisele. Peamine panustamise viis on haridusliku sisu täiustamine ja näidisrakenduste lisamine/parendamine, mis demonstreerivad Edge AI kontseptsioone.**  

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.