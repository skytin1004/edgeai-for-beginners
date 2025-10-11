<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c8a73e11384e3462674273498d0f9a6",
  "translation_date": "2025-10-11T11:51:59+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "et"
}
-->
# Sessioon 1: Foundry Locali kasutamise alustamine

## Kokkuvõte

Alusta oma teekonda Foundry Localiga, paigaldades ja seadistades selle Windows 11 operatsioonisüsteemis. Õpi CLI seadistamist, riistvarakiirenduse lubamist ja mudelite vahemällu salvestamist kiireks lokaalseks järeldamiseks. See praktiline sessioon juhendab mudelite nagu Phi, Qwen, DeepSeek ja GPT-OSS-20B käivitamist korduvate CLI käskudega.

## Õpieesmärgid

Sessiooni lõpuks oskad:

- **Paigaldada ja seadistada**: Optimeeritud jõudlusseadistustega Foundry Locali paigaldamine Windows 11-le
- **Valdada CLI toiminguid**: Foundry Local CLI kasutamine mudelite haldamiseks ja juurutamiseks
- **Lubada riistvarakiirendus**: GPU kiirenduse seadistamine ONNXRuntime'i või WebGPU abil
- **Juurutada mitmeid mudeleid**: Käivitada lokaalselt phi-4, GPT-OSS-20B, Qwen ja DeepSeek mudeleid
- **Luua oma esimene rakendus**: Kohandada olemasolevaid näiteid Foundry Local Python SDK kasutamiseks

# Testi mudelit (mitte-interaktiivne üksik küsimus)
foundry model run phi-4-mini --prompt "Tere, tutvusta ennast"

- Windows 11 (22H2 või uuem)
# Loetle saadaval olevad kataloogimudelid (laaditud mudelid ilmuvad pärast käivitamist)
foundry model list
## NOTE: Praegu puudub spetsiaalne `--running` lipp; et näha, millised mudelid on laaditud, alusta vestlust või vaata teenuse logisid.
- Python 3.10+ paigaldatud
- Visual Studio Code koos Python laiendusega
- Administraatori õigused paigaldamiseks

### (Valikuline) Keskkonnamuutujad

Loo `.env` (või määra shellis), et skriptid oleksid kaasaskantavad:
# Võrdle vastuseid (mitte-interaktiivne)
foundry model run gpt-oss-20b --prompt "Selgita lihtsate sõnadega, mis on edge AI"
| Muutuja | Eesmärk | Näide |
|---------|---------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Eelistatud mudeli alias (kataloog valib automaatselt parima variandi) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Ülekirjutatud lõpp-punkt (muidu automaatne haldurist) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Luba voogesituse demo | `true` |

> Kui `FOUNDRY_LOCAL_ENDPOINT=auto` (või määramata), tuletame selle SDK haldurist.

## Demo voog (30 minutit)

### 1. Paigalda Foundry Local ja kontrolli CLI seadistust (10 minutit)

# Loetle vahemällu salvestatud mudelid
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Eelvaade / Kui toetatud)**

Kui on saadaval macOS-i natiivne pakett (kontrolli ametlikke dokumente uusima versiooni jaoks):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Kui macOS-i natiivsed binaarid pole veel saadaval, saad siiski:
1. Kasutada Windows 11 ARM/Intel VM-i (Parallels / UTM) ja järgida Windowsi samme.
2. Käivitada mudeleid konteineri kaudu (kui konteineripilt on avaldatud) ja määrata `FOUNDRY_LOCAL_ENDPOINT` avatud pordile.

**Loo Python virtuaalne keskkond (platvormidevaheline)**

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

Uuenda pip ja paigalda põhikomponendid:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Samm 1.2: Kontrolli paigaldust

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Samm 1.3: Seadista keskkond

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Soovitatav)

Teenuse käsitsi käivitamise ja mudelite käitamise asemel saab **Foundry Local Python SDK** kõike automaatselt käivitada:

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

Kui eelistad selget kontrolli, saad siiski kasutada CLI-d + OpenAI klienti, nagu hiljem näidatud.

### 2. Luba GPU kiirendus (5 minutit)

#### Samm 2.1: Kontrolli riistvara võimekust

```powershell
# Check available compute providers
foundry system info

# List GPU capabilities
foundry system gpu-info
```

#### Samm 2.2: Seadista riistvarakiirendus

```powershell
# Enable ONNX Runtime GPU (if NVIDIA GPU available)
foundry config set compute.onnx.enable_gpu true

# Enable WebGPU for broader hardware support
foundry config set compute.webgpu.enabled true

# Verify configuration
foundry config list
```

### 3. Käivita mudeleid lokaalselt CLI kaudu (10 minutit)

#### Samm 3.1: Juuruta Phi-4 mudel

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Samm 3.2: Juuruta GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Samm 3.3: Laadi täiendavad mudelid

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Algprojekt: Kohanda 01-run-phi Foundry Locali jaoks (5 minutit)

#### Samm 4.1: Loo lihtne vestlusrakendus

Loo `samples/01-foundry-quickstart/chat_quickstart.py` (uuendatud halduri kasutamiseks, kui saadaval):

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

#### Samm 4.2: Testi rakendust

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Olulised käsitletud mõisted

### 1. Foundry Local arhitektuur

- **Lokaalne järeldusmootor**: Käitab mudeleid täielikult sinu seadmes
- **OpenAI SDK ühilduvus**: Sujuv integreerimine olemasoleva OpenAI koodiga
- **Mudelite haldamine**: Tõhus mudelite allalaadimine, vahemällu salvestamine ja käitamine
- **Riistvara optimeerimine**: Kasuta GPU, NPU ja CPU kiirendust

### 2. CLI käskude viide

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK integreerimine

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

## Tavaliste probleemide lahendamine

### Probleem 1: "Foundry käsku ei leitud"

**Lahendus:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Probleem 2: "Mudeli laadimine ebaõnnestus"

**Lahendus:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Probleem 3: "Ühendus localhost:5273 keeldus"

**Lahendus:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Jõudluse optimeerimise näpunäited

### 1. Mudeli valimise strateegia

- **Phi-4-mini**: Parim üldisteks ülesanneteks, madalam mälukasutus
- **Qwen2.5-0.5b**: Kiireim järeldus, minimaalsed ressursid
- **GPT-OSS-20B**: Kõrgeim kvaliteet, vajab rohkem ressursse
- **DeepSeek-Coder**: Optimeeritud programmeerimisülesannete jaoks

### 2. Riistvara optimeerimine

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Jõudluse jälgimine

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

### Valikulised täiustused

| Täiustus | Mis | Kuidas |
|----------|-----|-------|
| Jagatud utiliidid | Eemalda korduv klient/bootstrapi loogika | Kasuta `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Tokenite kasutuse nähtavus | Õpeta varakult kulude/efektiivsuse mõtlemist | Määra `SHOW_USAGE=1`, et printida küsimuse/vastuse/kokku tokenid |
| Deterministlikud võrdlused | Stabiilne võrdlusalus ja regressioonikontroll | Kasuta `temperature=0`, `top_p=1`, järjepidevat küsimuse teksti |
| Esimese tokeni latentsus | Tajutava reageerimisvõime mõõdik | Kohanda võrdlusaluse skripti voogesitusega (`BENCH_STREAM=1`) |
| Ajutiste vigade korral uuesti proovimine | Vastupidavad demod külmkäivitusel | `RETRY_ON_FAIL=1` (vaikimisi) ja kohanda `RETRY_BACKOFF` |
| Suitsu testimine | Kiire kontroll peamiste voogude üle | Käivita `python Workshop/tests/smoke.py` enne töötuba |
| Mudeli alias profiilid | Kiire mudelikomplekti vahetus masinate vahel | Hoia `.env` koos `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Vahemälu tõhusus | Väldi korduvaid soojendusi mitme näite käitamisel | Utiliidid vahemälu halduritele; taaskasuta skriptides/märkmikes |
| Esimese käivituse soojendus | Vähenda p95 latentsuse piike | Käivita väike küsimus pärast `FoundryLocalManager` loomist |

Näide deterministlikust soojast algtasemest (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Te peaksite nägema sarnast väljundit ja identseid tokenite arve teisel käivitamisel, kinnitades determinismi.

## Järgmised sammud

Pärast sessiooni lõpetamist:

1. **Uuri sessiooni 2**: Ehita AI lahendusi Azure AI Foundry RAG abil
2. **Proovi erinevaid mudeleid**: Katseta Qwen, DeepSeek ja teisi mudeliperekondi
3. **Optimeeri jõudlust**: Peenhäälesta seadeid vastavalt oma riistvarale
4. **Ehita kohandatud rakendusi**: Kasuta Foundry Local SDK-d oma projektides

## Täiendavad ressursid

### Dokumentatsioon
- [Foundry Local Python SDK viide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local paigaldusjuhend](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Mudelikataloog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Näidiskood
- [Moodul08 Näide 01](./samples/01/README.md) - REST vestluse kiirstart
- [Moodul08 Näide 02](./samples/02/README.md) - OpenAI SDK integreerimine
- [Moodul08 Näide 03](./samples/03/README.md) - Mudelite avastamine ja võrdlusalus

### Kogukond
- [Foundry Local GitHub arutelud](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI kogukond](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sessiooni kestus**: 30 minutit praktilist + 15 minutit küsimusi ja vastuseid  
**Raskusaste**: Algaja  
**Eeldused**: Windows 11, Python 3.10+, Administraatori juurdepääs

## Näidistsenaarium ja töötoa kaardistamine

| Töötoa skript / märkmik | Stsenaarium | Eesmärk | Näide sisend(id) | Vajalik andmestik |
|--------------------------|------------|--------|------------------|------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Sisemine IT meeskond hindab lokaalse järelduse kasutamist privaatsuse hindamise portaalis | Tõesta, et lokaalne SLM vastab standardsetele küsimustele alla sekundi latentsusega | "Loetle kaks lokaalse järelduse eelist." | Puudub (üksik küsimus) |
| Kiirstarti kohandamise koodiplokk | Arendaja, kes migreerib olemasolevat OpenAI skripti Foundry Localile | Näita ühilduvust | "Anna kaks lokaalse järelduse eelist." | Ainult sisemine küsimus |

### Stsenaariumi narratiiv
Turvalisuse ja vastavuse meeskond peab kinnitama, kas tundlikku prototüübi andmeid saab töödelda lokaalselt. Nad käivitavad bootstrap-skripti mitme küsimusega (privaatsus, latentsus, kulud), kasutades deterministlikku temperatuuri=0 režiimi, et jäädvustada algtaseme väljundid hilisemaks võrdluseks (Sessioon 3 võrdlusalus ja Sessioon 4 SLM vs LLM kontrast).

### Minimaalne küsimuste komplekt JSON (valikuline)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Kasuta seda loendit korduva hindamistsükli loomiseks või tulevase regressioonitesti raamistikuks.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.