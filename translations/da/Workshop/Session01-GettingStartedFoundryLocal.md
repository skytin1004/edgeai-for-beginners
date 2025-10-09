<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c8a73e11384e3462674273498d0f9a6",
  "translation_date": "2025-10-09T14:28:51+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "da"
}
-->
# Session 1: Kom godt i gang med Foundry Local

## Resumé

Start din rejse med Foundry Local ved at installere og konfigurere det på Windows 11. Lær, hvordan du opsætter CLI, aktiverer hardwareacceleration og cacher modeller for hurtig lokal inferens. Denne praktiske session guider dig gennem kørsel af modeller som Phi, Qwen, DeepSeek og GPT-OSS-20B ved hjælp af reproducerbare CLI-kommandoer.

## Læringsmål

Ved slutningen af denne session vil du:

- **Installere og konfigurere**: Opsætte Foundry Local på Windows 11 med optimale ydelsesindstillinger
- **Beherske CLI-operationer**: Bruge Foundry Local CLI til modelhåndtering og implementering
- **Aktivere hardwareacceleration**: Konfigurere GPU-acceleration med ONNXRuntime eller WebGPU
- **Implementere flere modeller**: Køre phi-4, GPT-OSS-20B, Qwen og DeepSeek-modeller lokalt
- **Bygge din første app**: Tilpasse eksisterende eksempler til at bruge Foundry Local Python SDK

# Test modellen (ikke-interaktiv enkelt prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 eller nyere)
# Liste over tilgængelige katalogmodeller (indlæste modeller vises efter kørsel)
foundry model list
## NOTE: Der er i øjeblikket ikke et dedikeret `--running` flag; for at se hvilke der er indlæst, start en chat eller inspicer servicelogfiler.
- Python 3.10+ installeret
- Visual Studio Code med Python-udvidelse
- Administratorrettigheder til installation

### (Valgfrit) Miljøvariabler

Opret en `.env` (eller sæt i shell) for at gøre scripts bærbare:
# Sammenlign svar (ikke-interaktiv)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| Variabel | Formål | Eksempel |
|----------|--------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Foretrukken modelalias (katalog vælger automatisk den bedste variant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Overstyr endpoint (ellers automatisk fra manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Aktivér streaming-demo | `true` |

> Hvis `FOUNDRY_LOCAL_ENDPOINT=auto` (eller ikke sat), afledes det fra SDK-manageren.

## Demo-forløb (30 minutter)

### 1. Installer Foundry Local og verificer CLI-opsætning (10 minutter)

# Liste over cachede modeller
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Preview / Hvis understøttet)**

Hvis en native macOS-pakke er tilgængelig (tjek officielle dokumenter for seneste version):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Hvis macOS-native binære filer endnu ikke er tilgængelige, kan du stadig: 
1. Bruge en Windows 11 ARM/Intel VM (Parallels / UTM) og følge Windows-trinnene. 
2. Køre modeller via container (hvis containerbillede er udgivet) og sætte `FOUNDRY_LOCAL_ENDPOINT` til den eksponerede port. 

**Opret Python-virtuelt miljø (platformuafhængigt)**

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

Opgrader pip og installer kerneafhængigheder:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Trin 1.2: Verificer installation

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Trin 1.3: Konfigurer miljø

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (anbefalet)

I stedet for manuelt at starte tjenesten og køre modeller, kan **Foundry Local Python SDK** bootstrappe alt:

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

Hvis du foretrækker eksplicit kontrol, kan du stadig bruge CLI + OpenAI-klienten som vist senere.

### 2. Aktivér GPU-acceleration (5 minutter)

#### Trin 2.1: Tjek hardwarekapaciteter

```powershell
# Check available compute providers
foundry system info

# List GPU capabilities
foundry system gpu-info
```

#### Trin 2.2: Konfigurer hardwareacceleration

```powershell
# Enable ONNX Runtime GPU (if NVIDIA GPU available)
foundry config set compute.onnx.enable_gpu true

# Enable WebGPU for broader hardware support
foundry config set compute.webgpu.enabled true

# Verify configuration
foundry config list
```

### 3. Kør modeller lokalt via CLI (10 minutter)

#### Trin 3.1: Implementer Phi-4-modellen

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Trin 3.2: Implementer GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Trin 3.3: Indlæs yderligere modeller

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Startprojekt: Tilpas 01-run-phi til Foundry Local (5 minutter)

#### Trin 4.1: Opret en grundlæggende chatapplikation

Opret `samples/01-foundry-quickstart/chat_quickstart.py` (opdateret til at bruge manageren, hvis tilgængelig):

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

#### Trin 4.2: Test applikationen

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Centrale begreber dækket

### 1. Foundry Local-arkitektur

- **Lokal inferensmotor**: Kører modeller udelukkende på din enhed
- **OpenAI SDK-kompatibilitet**: Problemfri integration med eksisterende OpenAI-kode
- **Modelhåndtering**: Download, cache og kør flere modeller effektivt
- **Hardwareoptimering**: Udnyt GPU-, NPU- og CPU-acceleration

### 2. CLI-kommandooversigt

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK-integration

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

## Fejlfinding af almindelige problemer

### Problem 1: "Foundry command not found"

**Løsning:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problem 2: "Model failed to load"

**Løsning:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problem 3: "Connection refused on localhost:5273"

**Løsning:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Tips til optimering af ydeevne

### 1. Strategi for modelvalg

- **Phi-4-mini**: Bedst til generelle opgaver, lavt hukommelsesforbrug
- **Qwen2.5-0.5b**: Hurtigste inferens, minimale ressourcer
- **GPT-OSS-20B**: Højeste kvalitet, kræver flere ressourcer
- **DeepSeek-Coder**: Optimeret til programmeringsopgaver

### 2. Hardwareoptimering

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Overvågning af ydeevne

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

### Valgfrie forbedringer

| Forbedring | Hvad | Hvordan |
|------------|------|---------|
| Delte værktøjer | Fjern duplikeret klient/bootstrap-logik | Brug `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Synlighed af tokenforbrug | Lær om omkostninger/effektivitet tidligt | Sæt `SHOW_USAGE=1` for at udskrive prompt/completion/total tokens |
| Deterministiske sammenligninger | Stabil benchmarking og regressionstests | Brug `temperature=0`, `top_p=1`, konsekvent prompttekst |
| Første-token-latens | Opfattet responsivitet | Tilpas benchmark-script med streaming (`BENCH_STREAM=1`) |
| Genforsøg ved midlertidige fejl | Robust demo ved koldstart | `RETRY_ON_FAIL=1` (standard) & juster `RETRY_BACKOFF` |
| Røgtest | Hurtig kontrol af nøglefunktioner | Kør `python Workshop/tests/smoke.py` før en workshop |
| Modelalias-profiler | Hurtig skift mellem maskiner | Vedligehold `.env` med `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Cache-effektivitet | Undgå gentagne opvarmninger i flere prøvekørsler | Genbrug cache-managere på tværs af scripts/notebooks |
| Første kørsel opvarmning | Reducer p95-latensspidser | Send en lille prompt efter `FoundryLocalManager`-oprettelse |

Eksempel på deterministisk varm baseline (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Du bør se lignende output og identiske tokenantal ved anden kørsel, hvilket bekræfter determinisme.

## Næste skridt

Efter at have gennemført denne session:

1. **Udforsk Session 2**: Byg AI-løsninger med Azure AI Foundry RAG
2. **Prøv forskellige modeller**: Eksperimentér med Qwen, DeepSeek og andre modelfamilier
3. **Optimer ydeevne**: Finjuster indstillinger til din specifikke hardware
4. **Byg brugerdefinerede applikationer**: Brug Foundry Local SDK i dine egne projekter

## Yderligere ressourcer

### Dokumentation
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installationsvejledning](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modelkatalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Eksempelkode
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Modelopdagelse og benchmarking

### Fællesskab
- [Foundry Local GitHub Diskussioner](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Sessionsvarighed**: 30 minutters praktisk arbejde + 15 minutters Q&A  
**Sværhedsgrad**: Begynder  
**Forudsætninger**: Windows 11, Python 3.10+, Administratoradgang  

## Eksempelscenarie og workshopkortlægning

| Workshop Script / Notebook | Scenarie | Mål | Eksempelinput | Nødvendigt datasæt |
|----------------------------|----------|-----|---------------|--------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Internt IT-team evaluerer on-device inferens til en portal for privatlivsvurdering | Bevise, at lokal SLM reagerer inden for sub-sekund latens på standardprompter | "List two benefits of local inference." | Ingen (enkelt prompt) |
| Quickstart-tilpasningskodeblok | Udvikler migrerer et eksisterende OpenAI-script til Foundry Local | Vise drop-in-kompatibilitet | "Give two benefits of local inference." | Kun inline-prompt |

### Scenariefortælling
Sikkerheds- og compliance-teamet skal validere, om følsomme prototype-data kan behandles lokalt. De kører bootstrap-scriptet med flere prompter (privatliv, latens, omkostninger) ved hjælp af en deterministisk temperatur=0-tilstand for at fange baseline-output til senere sammenligning (Session 3 benchmarking og Session 4 SLM vs LLM-kontrast).

### Minimal Prompt Set JSON (valgfrit)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Brug denne liste til at skabe en reproducerbar evalueringssløjfe eller til at forberede en fremtidig regressionstest-harness.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.