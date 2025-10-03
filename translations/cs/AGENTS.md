<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:42:53+00:00",
  "source_file": "AGENTS.md",
  "language_code": "cs"
}
-->
# AGENTS.md

## Přehled projektu

EdgeAI for Beginners je komplexní vzdělávací úložiště zaměřené na výuku vývoje Edge AI s malými jazykovými modely (SLM). Kurz pokrývá základy EdgeAI, nasazení modelů, optimalizační techniky a implementace připravené pro produkci pomocí Microsoft Foundry Local a různých AI frameworků.

**Klíčové technologie:**
- Python 3.8+ (hlavní jazyk pro AI/ML ukázky)
- .NET C# (AI/ML ukázky)
- JavaScript/Node.js s Electronem (pro desktopové aplikace)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI frameworky: LangChain, Semantic Kernel, Chainlit
- Optimalizace modelů: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Typ úložiště:** Vzdělávací obsahové úložiště s 8 moduly a 10 komplexními ukázkovými aplikacemi

**Architektura:** Více modulová vzdělávací cesta s praktickými ukázkami nasazení Edge AI

## Struktura úložiště

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

## Příkazy pro nastavení

### Nastavení úložiště

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Nastavení Python ukázek (Modul08 a Python ukázky)

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

### Nastavení Node.js ukázek (Ukázka 08 - Windows Chat App)

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

### Nastavení Foundry Local

Foundry Local je nutné pro spuštění ukázek z Modulu08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Vývojový pracovní postup

### Vývoj obsahu

Toto úložiště obsahuje primárně **Markdown vzdělávací obsah**. Při provádění změn:

1. Upravte soubory `.md` ve vhodných adresářích modulů
2. Dodržujte existující formátovací vzory
3. Zajistěte, že ukázky kódu jsou přesné a otestované
4. Aktualizujte odpovídající překlady, pokud je to nutné (nebo to nechte na automatizaci)

### Vývoj ukázkových aplikací

Pro Python ukázky (ukázky 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Pro Electron ukázku (ukázka 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testování ukázkových aplikací

Python ukázky nemají automatizované testy, ale lze je ověřit jejich spuštěním:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron ukázka má testovací infrastrukturu:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Pokyny k testování

### Ověření obsahu

Úložiště používá automatizované překladové pracovní postupy. Manuální testování překladů není nutné.

**Manuální ověření změn obsahu:**
1. Zkontrolujte vykreslení Markdownu náhledem souborů `.md`
2. Ověřte, že všechny odkazy směřují na platné cíle
3. Otestujte jakékoli ukázky kódu zahrnuté v dokumentaci
4. Zkontrolujte, zda se obrázky načítají správně

### Testování ukázkových aplikací

**Modul08/samples/08 (Electron aplikace) má komplexní testování:**
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

**Python ukázky by měly být testovány manuálně:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Pokyny ke stylu kódu

### Markdown obsah

- Používejte konzistentní hierarchii nadpisů (# pro titul, ## pro hlavní sekce, ### pro podsekce)
- Zahrnujte bloky kódu s určením jazyka: ```python, ```bash, ```javascript
- Dodržujte existující formátování pro tabulky, seznamy a zvýraznění
- Udržujte čitelnost řádků (cílem je ~80-100 znaků, ale není to striktní)
- Používejte relativní odkazy pro interní reference

### Styl kódu Python

- Dodržujte konvence PEP 8
- Používejte typové anotace, kde je to vhodné
- Zahrnujte docstringy pro funkce a třídy
- Používejte smysluplné názvy proměnných
- Udržujte funkce zaměřené a stručné

### Styl kódu JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Klíčové konvence:**
- ESLint konfigurace poskytována v ukázce 08
- Prettier pro formátování kódu
- Používejte moderní syntaxi ES6+
- Dodržujte existující vzory v kódu

## Pokyny pro Pull Requesty

### Formát názvu
```
[ModuleXX] Brief description of change
```
nebo
```
[Module08/samples/XX] Description for sample changes
```

### Před odesláním

**Pro změny obsahu:**
- Náhled všech upravených Markdown souborů
- Ověřte funkčnost odkazů a obrázků
- Zkontrolujte překlepy a gramatické chyby

**Pro změny ukázkového kódu (Modul08/samples/08):**
```bash
npm run lint
npm test
```

**Pro změny Python ukázek:**
- Otestujte, že ukázka běží úspěšně
- Ověřte funkčnost zpracování chyb
- Zkontrolujte kompatibilitu s Foundry Local

### Proces revize

- Změny vzdělávacího obsahu jsou kontrolovány z hlediska přesnosti a srozumitelnosti
- Ukázky kódu jsou testovány z hlediska funkčnosti
- Aktualizace překladů jsou zpracovávány automaticky pomocí GitHub Actions

## Překladový systém

**DŮLEŽITÉ:** Toto úložiště používá automatizovaný překlad prostřednictvím GitHub Actions.

- Překlady jsou v adresáři `/translations/` (50+ jazyků)
- Automatizováno pomocí workflow `co-op-translator.yml`
- **NEUPRAVUJTE manuálně překladové soubory** - budou přepsány
- Upravujte pouze anglické zdrojové soubory v kořenovém adresáři a adresářích modulů
- Překlady jsou automaticky generovány při pushi do větve `main`

## Integrace Foundry Local

Většina ukázek z Modulu08 vyžaduje spuštění Microsoft Foundry Local:

### Spuštění Foundry Local
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

### Ověření Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Proměnné prostředí pro ukázky

Většina ukázek používá tyto proměnné prostředí:
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

## Sestavení a nasazení

### Nasazení obsahu

Toto úložiště je primárně dokumentace - není vyžadován žádný proces sestavení pro obsah.

### Sestavení ukázkových aplikací

**Electron aplikace (Modul08/samples/08):**
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

**Python ukázky:**
Žádný proces sestavení - ukázky se spouštějí přímo pomocí Python interpreteru.

## Běžné problémy a jejich řešení

### Foundry Local není spuštěn
**Problém:** Ukázky selhávají s chybami připojení

**Řešení:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problémy s Python virtuálním prostředím
**Problém:** Chyby při importu modulů

**Řešení:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Problémy se sestavením Electronu
**Problém:** Chyby při instalaci npm nebo sestavení

**Řešení:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflikty v překladovém workflow
**Problém:** Překladový PR je v konfliktu s vašimi změnami

**Řešení:**
- Upravujte pouze anglické zdrojové soubory
- Nechte automatizovaný překladový workflow zpracovat překlady
- Pokud dojde ke konfliktům, sloučte `main` do své větve po sloučení překladů

## Další zdroje

### Vzdělávací cesty
- **Cesta pro začátečníky:** Moduly 01-02 (7-9 hodin)
- **Cesta pro pokročilé:** Moduly 03-04 (9-11 hodin)
- **Cesta pro zkušené:** Moduly 05-07 (12-15 hodin)
- **Cesta pro experty:** Modul 08 (8-10 hodin)

### Klíčový obsah modulů
- **Modul01:** Základy EdgeAI a případové studie z reálného světa
- **Modul02:** Rodiny a architektury malých jazykových modelů (SLM)
- **Modul03:** Strategie nasazení na lokální a cloudové úrovni
- **Modul04:** Optimalizace modelů pomocí různých frameworků
- **Modul05:** SLMOps - provozní operace v produkci
- **Modul06:** AI agenti a volání funkcí
- **Modul07:** Implementace specifické pro platformy
- **Modul08:** Nástrojová sada Foundry Local s 10 komplexními ukázkami

### Externí závislosti
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokální runtime pro AI modely
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimalizační framework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Nástroj pro optimalizaci modelů
- [OpenVINO](https://docs.openvino.ai/) - Optimalizační nástroj od Intelu

## Poznámky specifické pro projekt

### Ukázkové aplikace Modulu08

Úložiště obsahuje 10 komplexních ukázkových aplikací:

1. **01-REST Chat Quickstart** - Základní integrace OpenAI SDK
2. **02-OpenAI SDK Integration** - Pokročilé funkce SDK
3. **03-Model Discovery & Benchmarking** - Nástroje pro porovnání modelů
4. **04-Chainlit RAG Application** - Generace s podporou vyhledávání
5. **05-Multi-Agent Orchestration** - Základní koordinace agentů
6. **06-Models-as-Tools Router** - Inteligentní směrování modelů
7. **07-Direct API Client** - Nízkoúrovňová integrace API
8. **08-Windows 11 Chat App** - Nativní desktopová aplikace Electron
9. **09-Advanced Multi-Agent System** - Komplexní orchestrace agentů
10. **10-Foundry Tools Framework** - Integrace LangChain/Semantic Kernel

Každá ukázka demonstruje různé aspekty vývoje Edge AI s Foundry Local.

### Výkonnostní úvahy

- SLM jsou optimalizovány pro nasazení na okraji (2-16GB RAM)
- Lokální inference poskytuje odezvy 50-500ms
- Kvantizační techniky dosahují 75% redukce velikosti při zachování 85% výkonu
- Schopnosti pro konverzaci v reálném čase s lokálními modely

### Bezpečnost a soukromí

- Veškeré zpracování probíhá lokálně - žádná data nejsou odesílána do cloudu
- Vhodné pro aplikace citlivé na soukromí (zdravotnictví, finance)
- Splňuje požadavky na suverenitu dat
- Foundry Local běží zcela na lokálním hardwaru

---

**Toto je vzdělávací úložiště zaměřené na výuku vývoje Edge AI. Hlavním příspěvkovým vzorem je zlepšování vzdělávacího obsahu a přidávání/zdokonalování ukázkových aplikací, které demonstrují koncepty Edge AI.**

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.