<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c8a73e11384e3462674273498d0f9a6",
  "translation_date": "2025-10-09T21:17:15+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "lt"
}
-->
# Sesija 1: Pradžia su Foundry Local

## Santrauka

Pradėkite savo kelionę su Foundry Local įdiegdami ir konfigūruodami jį Windows 11 sistemoje. Sužinokite, kaip nustatyti CLI, įjungti aparatūros pagreitį ir talpinti modelius greitam vietiniam inferencijai. Ši praktinė sesija parodys, kaip paleisti modelius, tokius kaip Phi, Qwen, DeepSeek ir GPT-OSS-20B, naudojant atkuriamus CLI komandas.

## Mokymosi tikslai

Po šios sesijos jūs:

- **Įdiegsite ir konfigūruosite**: Nustatysite Foundry Local Windows 11 sistemoje su optimaliomis našumo nuostatomis
- **Įvaldysite CLI operacijas**: Naudosite Foundry Local CLI modelių valdymui ir diegimui
- **Įjungsite aparatūros pagreitį**: Konfigūruosite GPU pagreitį su ONNXRuntime arba WebGPU
- **Diegsite kelis modelius**: Vietoje paleisite phi-4, GPT-OSS-20B, Qwen ir DeepSeek modelius
- **Sukursite pirmąją programą**: Pritaikysite esamus pavyzdžius naudodami Foundry Local Python SDK

# Testuokite modelį (neinteraktyvus vieno klausimo atsakymas)
foundry model run phi-4-mini --prompt "Sveiki, prisistatykite"

- Windows 11 (22H2 ar naujesnė versija)
# Peržiūrėkite galimus katalogo modelius (įkelti modeliai pasirodys po paleidimo)
foundry model list
## PASTABA: Šiuo metu nėra dedikuoto `--running` parametro; norėdami pamatyti, kurie modeliai įkelti, pradėkite pokalbį arba peržiūrėkite paslaugos žurnalus.
- Įdiegta Python 3.10+
- Visual Studio Code su Python plėtiniu
- Administratoriaus teisės diegimui

### (Pasirinktinai) Aplinkos kintamieji

Sukurkite `.env` (arba nustatykite apvalkale), kad skriptai būtų perkeliamieji:
# Palyginkite atsakymus (neinteraktyvus)
foundry model run gpt-oss-20b --prompt "Paaiškinkite, kas yra edge AI paprastais žodžiais"
| Kintamasis | Paskirtis | Pavyzdys |
|------------|-----------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Pageidaujamas modelio aliasas (katalogas automatiškai parenka geriausią variantą) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Pakeisti galinį tašką (kitaip automatiškai iš valdytojo) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Įjungti srautinį demonstravimą | `true` |

> Jei `FOUNDRY_LOCAL_ENDPOINT=auto` (arba nenustatytas), jis bus gautas iš SDK valdytojo.

## Demonstracijos eiga (30 minučių)

### 1. Įdiekite Foundry Local ir patikrinkite CLI nustatymą (10 minučių)

# Peržiūrėkite talpintus modelius
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Peržiūra / Jei palaikoma)**

Jei pateikiamas vietinis macOS paketas (patikrinkite oficialią dokumentaciją dėl naujausios informacijos):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Jei macOS vietiniai dvejetainiai failai dar nepateikti, vis tiek galite: 
1. Naudoti Windows 11 ARM/Intel VM (Parallels / UTM) ir sekti Windows žingsnius. 
2. Paleisti modelius per konteinerį (jei paskelbtas konteinerio vaizdas) ir nustatyti `FOUNDRY_LOCAL_ENDPOINT` į atidarytą prievadą. 

**Sukurkite Python virtualią aplinką (kryžminė platforma)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Atnaujinkite pip ir įdiekite pagrindines priklausomybes:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### 1.2 žingsnis: Patikrinkite diegimą

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### 1.3 žingsnis: Konfigūruokite aplinką

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK paleidimas (rekomenduojama)

Užuot rankiniu būdu paleidus paslaugą ir modelius, **Foundry Local Python SDK** gali paleisti viską automatiškai:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Jei norite aiškios kontrolės, vis tiek galite naudoti CLI + OpenAI klientą, kaip parodyta vėliau.

### 2. Įjunkite GPU pagreitį (5 minutės)

#### 2.1 žingsnis: Patikrinkite aparatūros galimybes

```powershell
# Check available compute providers
foundry system info

# List GPU capabilities
foundry system gpu-info
```

#### 2.2 žingsnis: Konfigūruokite aparatūros pagreitį

```powershell
# Enable ONNX Runtime GPU (if NVIDIA GPU available)
foundry config set compute.onnx.enable_gpu true

# Enable WebGPU for broader hardware support
foundry config set compute.webgpu.enabled true

# Verify configuration
foundry config list
```

### 3. Paleiskite modelius vietoje per CLI (10 minučių)

#### 3.1 žingsnis: Diegkite Phi-4 modelį

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### 3.2 žingsnis: Diegkite GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### 3.3 žingsnis: Įkelkite papildomus modelius

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Pradinis projektas: Pritaikykite 01-run-phi Foundry Local (5 minutės)

#### 4.1 žingsnis: Sukurkite pagrindinę pokalbių programą

Sukurkite `samples/01-foundry-quickstart/chat_quickstart.py` (atnaujinta naudoti valdytoją, jei yra):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### 4.2 žingsnis: Testuokite programą

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Pagrindinės aptartos sąvokos

### 1. Foundry Local architektūra

- **Vietinis inferencijos variklis**: Modeliai veikia visiškai jūsų įrenginyje
- **OpenAI SDK suderinamumas**: Sklandus integravimas su esamu OpenAI kodu
- **Modelių valdymas**: Efektyvus modelių atsisiuntimas, talpinimas ir paleidimas
- **Aparatūros optimizavimas**: Naudojamas GPU, NPU ir CPU pagreitis

### 2. CLI komandų nuoroda

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK integracija

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Dažniausiai pasitaikančių problemų sprendimas

### Problema 1: "Foundry komanda nerasta"

**Sprendimas:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problema 2: "Modelio įkėlimas nepavyko"

**Sprendimas:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problema 3: "Ryšys atmestas localhost:5273"

**Sprendimas:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Našumo optimizavimo patarimai

### 1. Modelio pasirinkimo strategija

- **Phi-4-mini**: Geriausias bendroms užduotims, mažesnis atminties naudojimas
- **Qwen2.5-0.5b**: Greičiausias inferencijos laikas, minimalūs resursai
- **GPT-OSS-20B**: Aukščiausia kokybė, reikalauja daugiau resursų
- **DeepSeek-Coder**: Optimizuotas programavimo užduotims

### 2. Aparatūros optimizavimas

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Našumo stebėjimas

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Pasirinktiniai patobulinimai

| Patobulinimas | Kas | Kaip |
|---------------|-----|------|
| Bendri įrankiai | Pašalinkite pasikartojančią klientų/paleidimo logiką | Naudokite `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Žetonų naudojimo matomumas | Mokykite apie kaštus/efektyvumą anksti | Nustatykite `SHOW_USAGE=1`, kad spausdintumėte klausimo/atsakymo/bendrą žetonų skaičių |
| Deterministiniai palyginimai | Stabilus testavimas ir regresijos patikrinimai | Naudokite `temperature=0`, `top_p=1`, nuoseklų klausimo tekstą |
| Pirmojo žetono vėlinimas | Matomas atsako greičio rodiklis | Pritaikykite testavimo skriptą su srautiniu režimu (`BENCH_STREAM=1`) |
| Pakartotinis bandymas dėl laikino klaidų | Atsparūs demonstravimai šalto paleidimo metu | `RETRY_ON_FAIL=1` (numatytasis) ir koreguokite `RETRY_BACKOFF` |
| Greitas testavimas | Greita pagrindinių funkcijų patikra | Paleiskite `python Workshop/tests/smoke.py` prieš dirbtuves |
| Modelio alias profiliai | Greitai keiskite modelių rinkinį tarp įrenginių | Laikykite `.env` su `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Talpinimo efektyvumas | Venkite pakartotinių paleidimų kelių pavyzdžių metu | Naudokite talpinimo valdytojus; pakartotinai naudokite skriptuose/notebook'uose |
| Pirmojo paleidimo apšilimas | Sumažinkite p95 vėlinimo šuolius | Paleiskite trumpą klausimą po `FoundryLocalManager` sukūrimo |

Pavyzdys deterministinio apšilimo (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Turėtumėte matyti panašų išvestį ir identišką žetonų skaičių antrame paleidime, patvirtinant deterministiškumą.

## Kiti žingsniai

Po šios sesijos:

1. **Išbandykite 2 sesiją**: Kurkite AI sprendimus su Azure AI Foundry RAG
2. **Išbandykite skirtingus modelius**: Eksperimentuokite su Qwen, DeepSeek ir kitomis modelių šeimomis
3. **Optimizuokite našumą**: Koreguokite nustatymus pagal savo specifinę aparatūrą
4. **Kurkite pritaikytas programas**: Naudokite Foundry Local SDK savo projektuose

## Papildomi ištekliai

### Dokumentacija
- [Foundry Local Python SDK nuoroda](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local diegimo vadovas](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modelių katalogas](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Pavyzdinis kodas
- [Module08 Pavyzdys 01](./samples/01/README.md) - REST pokalbių greitas startas
- [Module08 Pavyzdys 02](./samples/02/README.md) - OpenAI SDK integracija
- [Module08 Pavyzdys 03](./samples/03/README.md) - Modelių atradimas ir testavimas

### Bendruomenė
- [Foundry Local GitHub diskusijos](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI bendruomenė](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sesijos trukmė**: 30 minučių praktika + 15 minučių klausimai ir atsakymai  
**Sudėtingumo lygis**: Pradedantysis  
**Būtinos sąlygos**: Windows 11, Python 3.10+, administratoriaus teisės

## Pavyzdinė situacija ir dirbtuvių susiejimas

| Dirbtuvių skriptas / užrašų knygelė | Situacija | Tikslas | Pavyzdiniai įvesties duomenys | Reikalingas duomenų rinkinys |
|------------------------------------|-----------|--------|-----------------------------|-----------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Vidinė IT komanda vertina vietinį inferenciją privatumo vertinimo portale | Įrodyti, kad vietinis SLM atsako per mažiau nei sekundę standartiniams klausimams | "Išvardinkite dvi vietinio inferencijos naudas." | Nėra (vieno klausimo atsakymas) |
| Greito starto adaptacijos kodas | Kūrėjas, migruojantis esamą OpenAI skriptą į Foundry Local | Parodyti suderinamumą | "Išvardinkite dvi vietinio inferencijos naudas." | Tik įterptas klausimas |

### Situacijos pasakojimas
Saugumo ir atitikties komanda turi patikrinti, ar jautrūs prototipiniai duomenys gali būti apdorojami vietoje. Jie paleidžia paleidimo skriptą su keliais klausimais (privatumas, vėlinimas, kaštai), naudodami deterministinį režimą `temperature=0`, kad užfiksuotų bazinius rezultatus vėlesniam palyginimui (3 sesijos testavimas ir 4 sesijos SLM vs LLM kontrastas).

### Minimalus klausimų rinkinys JSON (pasirinktinai)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Naudokite šį sąrašą, kad sukurtumėte atkuriamą vertinimo ciklą arba inicijuotumėte būsimą regresijos testavimo sistemą.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.