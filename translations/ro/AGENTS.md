<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:44:02+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ro"
}
-->
# AGENTS.md

## Prezentare Generală a Proiectului

EdgeAI pentru Începători este un depozit educațional cuprinzător care predă dezvoltarea Edge AI folosind Modele de Limbaj Mici (SLMs). Cursul acoperă fundamentele EdgeAI, implementarea modelelor, tehnici de optimizare și implementări pregătite pentru producție utilizând Microsoft Foundry Local și diverse cadre AI.

**Tehnologii Cheie:**
- Python 3.8+ (limbaj principal pentru exemple AI/ML)
- .NET C# (exemple AI/ML)
- JavaScript/Node.js cu Electron (pentru aplicații desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Cadre AI: LangChain, Semantic Kernel, Chainlit
- Optimizarea modelelor: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tipul Depozitului:** Depozit de conținut educațional cu 8 module și 10 aplicații exemplu cuprinzătoare

**Arhitectură:** Parcurs de învățare multi-modular cu exemple practice care demonstrează modele de implementare Edge AI

## Structura Depozitului

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

## Comenzi de Configurare

### Configurarea Depozitului

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Configurarea Exemplului Python (Module08 și exemple Python)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Configurarea Exemplului Node.js (Exemplu 08 - Aplicație Chat Windows)

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

### Configurarea Foundry Local

Foundry Local este necesar pentru a rula exemplele din Module08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Flux de Lucru pentru Dezvoltare

### Dezvoltarea Conținutului

Acest depozit conține în principal **conținut educațional în format Markdown**. Când faceți modificări:

1. Editați fișierele `.md` în directoarele modulelor corespunzătoare
2. Urmați modelele de formatare existente
3. Asigurați-vă că exemplele de cod sunt corecte și testate
4. Actualizați conținutul tradus corespunzător, dacă este necesar (sau lăsați automatizarea să se ocupe de asta)

### Dezvoltarea Aplicațiilor Exemplu

Pentru exemplele Python (exemplele 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Pentru exemplul Electron (exemplul 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testarea Aplicațiilor Exemplu

Exemplele Python nu au teste automate, dar pot fi validate prin rularea lor:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Exemplul Electron are infrastructură de testare:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instrucțiuni de Testare

### Validarea Conținutului

Depozitul utilizează fluxuri de lucru automate pentru traduceri. Nu este necesară testarea manuală pentru traduceri.

**Validare manuală pentru modificările de conținut:**
1. Revizuiți redarea Markdown prin previzualizarea fișierelor `.md`
2. Verificați ca toate linkurile să conducă la destinații valide
3. Testați orice fragmente de cod incluse în documentație
4. Asigurați-vă că imaginile se încarcă corect

### Testarea Aplicațiilor Exemplu

**Module08/samples/08 (aplicația Electron) are testare cuprinzătoare:**
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

**Exemplele Python trebuie testate manual:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Ghiduri de Stil pentru Cod

### Conținut Markdown

- Utilizați o ierarhie consistentă a titlurilor (# pentru titlu, ## pentru secțiuni principale, ### pentru subsecțiuni)
- Includeți blocuri de cod cu specificatori de limbaj: ```python, ```bash, ```javascript
- Urmați formatarea existentă pentru tabele, liste și accentuări
- Păstrați liniile ușor de citit (aproximativ 80-100 de caractere, dar nu strict)
- Utilizați linkuri relative pentru referințe interne

### Stilul Codului Python

- Urmați convențiile PEP 8
- Utilizați indicii de tip acolo unde este potrivit
- Includeți docstrings pentru funcții și clase
- Folosiți nume de variabile semnificative
- Păstrați funcțiile concentrate și concise

### Stilul Codului JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Convenții cheie:**
- Configurație ESLint furnizată în exemplul 08
- Prettier pentru formatarea codului
- Utilizați sintaxa modernă ES6+
- Urmați modelele existente în baza de cod

## Ghiduri pentru Cereri de Tragere (Pull Requests)

### Formatul Titlului
```
[ModuleXX] Brief description of change
```
sau
```
[Module08/samples/XX] Description for sample changes
```

### Înainte de Trimitere

**Pentru modificări de conținut:**
- Previzualizați toate fișierele Markdown modificate
- Verificați ca linkurile și imaginile să funcționeze
- Verificați erorile de tipar și gramaticale

**Pentru modificări ale codului exemplu (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Pentru modificări ale exemplului Python:**
- Testați ca exemplul să ruleze cu succes
- Verificați funcționarea gestionării erorilor
- Verificați compatibilitatea cu Foundry Local

### Procesul de Revizuire

- Modificările de conținut educațional sunt revizuite pentru acuratețe și claritate
- Exemplele de cod sunt testate pentru funcționalitate
- Actualizările traducerilor sunt gestionate automat de GitHub Actions

## Sistem de Traducere

**IMPORTANT:** Acest depozit utilizează traduceri automate prin GitHub Actions.

- Traducerile se află în directorul `/translations/` (50+ limbi)
- Automatizate prin fluxul de lucru `co-op-translator.yml`
- **NU editați manual fișierele de traducere** - acestea vor fi suprascrise
- Editați doar fișierele sursă în limba engleză din directoarele rădăcină și module
- Traducerile sunt generate automat la fiecare push către ramura `main`

## Integrarea Foundry Local

Majoritatea exemplelor din Module08 necesită ca Microsoft Foundry Local să fie activ:

### Pornirea Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Verificarea Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Variabile de Mediu pentru Exemple

Majoritatea exemplelor utilizează aceste variabile de mediu:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Construire și Implementare

### Implementarea Conținutului

Acest depozit este în principal documentație - nu este necesar un proces de construire pentru conținut.

### Construirea Aplicațiilor Exemplu

**Aplicația Electron (Module08/samples/08):**
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

**Exemple Python:**
Nu este necesar un proces de construire - exemplele sunt rulate direct cu interpretul Python.

## Probleme Comune și Soluționare

### Foundry Local Nu Rulează
**Problemă:** Exemplele eșuează cu erori de conexiune

**Soluție:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Probleme cu Mediul Virtual Python
**Problemă:** Erori de import module

**Soluție:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Probleme de Construire Electron
**Problemă:** npm install sau eșecuri de construire

**Soluție:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Conflicte în Fluxul de Lucru pentru Traduceri
**Problemă:** PR-ul de traducere intră în conflict cu modificările dvs.

**Soluție:**
- Editați doar fișierele sursă în limba engleză
- Lăsați fluxul de lucru automat să se ocupe de traduceri
- Dacă apar conflicte, îmbinați `main` în ramura dvs. după ce traducerile sunt îmbinate

## Resurse Suplimentare

### Parcursuri de Învățare
- **Parcurs pentru Începători:** Modulele 01-02 (7-9 ore)
- **Parcurs Intermediar:** Modulele 03-04 (9-11 ore)
- **Parcurs Avansat:** Modulele 05-07 (12-15 ore)
- **Parcurs Expert:** Modulul 08 (8-10 ore)

### Conținut Cheie al Modulului
- **Module01:** Fundamentele EdgeAI și studii de caz reale
- **Module02:** Familii și arhitecturi ale Modelelor de Limbaj Mici (SLM)
- **Module03:** Strategii de implementare locală și în cloud
- **Module04:** Optimizarea modelelor cu mai multe cadre
- **Module05:** SLMOps - operațiuni de producție
- **Module06:** Agenți AI și apelarea funcțiilor
- **Module07:** Implementări specifice platformei
- **Module08:** Toolkit Foundry Local cu 10 exemple cuprinzătoare

### Dependențe Externe
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Runtime local pentru modele AI
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Cadru de optimizare
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit de optimizare a modelelor
- [OpenVINO](https://docs.openvino.ai/) - Toolkit de optimizare de la Intel

## Note Specifice Proiectului

### Aplicații Exemplu Modulul 08

Depozitul include 10 aplicații exemplu cuprinzătoare:

1. **01-REST Chat Quickstart** - Integrare de bază OpenAI SDK
2. **02-OpenAI SDK Integration** - Funcții avansate ale SDK
3. **03-Model Discovery & Benchmarking** - Instrumente de comparare a modelelor
4. **04-Chainlit RAG Application** - Generare augmentată prin recuperare
5. **05-Multi-Agent Orchestration** - Coordonare de bază a agenților
6. **06-Models-as-Tools Router** - Rutare inteligentă a modelelor
7. **07-Direct API Client** - Integrare API la nivel scăzut
8. **08-Windows 11 Chat App** - Aplicație desktop nativă Electron
9. **09-Advanced Multi-Agent System** - Orchestrare complexă a agenților
10. **10-Foundry Tools Framework** - Integrare LangChain/Semantic Kernel

Fiecare exemplu demonstrează diferite aspecte ale dezvoltării Edge AI cu Foundry Local.

### Considerații de Performanță

- SLM-urile sunt optimizate pentru implementare la margine (2-16GB RAM)
- Inferența locală oferă timpi de răspuns de 50-500ms
- Tehnicile de cuantizare reduc dimensiunea cu 75% păstrând 85% din performanță
- Capacități de conversație în timp real cu modele locale

### Securitate și Confidențialitate

- Toată procesarea are loc local - niciun fel de date nu sunt trimise în cloud
- Potrivit pentru aplicații sensibile la confidențialitate (sănătate, finanțe)
- Respectă cerințele de suveranitate a datelor
- Foundry Local rulează complet pe hardware local

---

**Acesta este un depozit educațional axat pe predarea dezvoltării Edge AI. Modelul principal de contribuție este îmbunătățirea conținutului educațional și adăugarea/îmbunătățirea aplicațiilor exemplu care demonstrează concepte Edge AI.**

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.