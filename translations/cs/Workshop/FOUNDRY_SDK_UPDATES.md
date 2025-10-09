<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T21:05:35+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "cs"
}
-->
# Aktualizace Foundry Local SDK

## Přehled

Aktualizovali jsme pracovní sešity Workshopu a nástroje tak, aby správně využívaly **oficiální Foundry Local Python SDK** podle vzorů z:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Upravené soubory

### 1. `Workshop/samples/workshop_utils.py`

**Změny:**
- ✅ Přidána obsluha chyb při importu balíčku `foundry-local-sdk`
- ✅ Vylepšena dokumentace podle oficiálních vzorů SDK
- ✅ Zlepšeno logování pomocí Unicode symbolů (✓, ✗, ⚠)
- ✅ Přidány podrobné docstringy s příklady
- ✅ Lepší chybové zprávy odkazující na příkazy CLI
- ✅ Aktualizovány komentáře tak, aby odpovídaly dokumentaci oficiálního SDK

**Klíčová vylepšení:**

#### Obsluha chyb při importu
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Vylepšená funkce `get_client()`
- Přidána podrobná dokumentace o vzoru inicializace SDK
- Vysvětleno, že `FoundryLocalManager` automaticky spouští službu
- Popsáno řešení aliasů modelů na hardwarově optimalizované varianty
- Zlepšeno logování s informacemi o endpointu
- Lepší chybové zprávy s návrhy kroků pro řešení problémů

#### Vylepšená funkce `chat_once()`
- Přidán podrobný docstring s příklady použití
- Ujasněna kompatibilita s OpenAI SDK
- Zdokumentována podpora streamování (přes kwargs)
- Zlepšeny chybové zprávy s návrhy příkazů CLI
- Přidány poznámky o kontrole dostupnosti modelů

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Změny:**
- ✅ Aktualizovány všechny buňky s markdownem s odkazy na SDK
- ✅ Vylepšeny komentáře kódu s vysvětlením vzorů SDK
- ✅ Zlepšena dokumentace a vysvětlení buněk
- ✅ Přidány pokyny pro řešení problémů
- ✅ Aktualizován katalog modelů (nahrazen 'gpt-oss-20b' za 'phi-3.5-mini')
- ✅ Lepší formátování výstupů s vizuálními indikátory
- ✅ Přidány odkazy na SDK a reference napříč dokumentem

**Aktualizace po buňkách:**

#### Buňka 1 (Název)
- Přidány odkazy na dokumentaci SDK
- Odkázány oficiální repozitáře GitHub

#### Buňka 2 (Scénář)
- Přeformátováno do očíslovaných kroků
- Ujasněn vzor směrování na základě záměru
- Zdůrazněny výhody lokálního provádění

#### Buňka 3 (Instalace závislostí)
- Přidáno vysvětlení, co každý balíček poskytuje
- Zdokumentovány schopnosti SDK (řešení aliasů, hardwarová optimalizace)

#### Buňka 4 (Nastavení prostředí)
- Vylepšeny docstringy funkcí
- Přidány inline komentáře vysvětlující vzory SDK
- Zdokumentována struktura katalogu modelů
- Ujasněno párování priorit/schopností

#### Buňka 5 (Kontrola katalogu)
- Přidány vizuální zaškrtávací značky (✓)
- Lepší formátování výstupu

#### Buňka 6 (Test detekce záměru)
- Přeformátováno jako tabulkový výstup
- Zobrazuje jak záměr, tak vybraný model

#### Buňka 7 (Směrovací funkce)
- Komplexní vysvětlení vzoru SDK
- Zdokumentován průběh inicializace
- Vypsány všechny funkce (opakování, sledování, chyby)
- Přidán odkaz na SDK

#### Buňka 8 (Ukázka dávkového zpracování)
- Vylepšeno vysvětlení očekávaného výstupu
- Přidána sekce pro řešení problémů
- Zahrnuty příkazy CLI pro ladění
- Lepší formátování zobrazení výstupu

### 3. `Workshop/notebooks/session06_README.md` (Nový soubor)

**Vytvořena komplexní dokumentace zahrnující:**

1. **Přehled**: Diagram architektury a vysvětlení komponent
2. **Integrace SDK**: Příklady kódu podle oficiálních vzorů
3. **Předpoklady**: Krok za krokem nastavení
4. **Použití**: Jak spustit a přizpůsobit pracovní sešit
5. **Alias modelů**: Vysvětlení hardwarově optimalizovaných variant
6. **Řešení problémů**: Běžné problémy a jejich řešení
7. **Rozšíření**: Jak přidat záměry, modely a vlastní logiku
8. **Tipy pro výkon**: Nejlepší postupy pro produkční použití
9. **Zdroje**: Odkazy na oficiální dokumentaci a komunitu

## Implementace vzoru SDK

### Oficiální vzor (z dokumentace Foundry Local)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Naše implementace (v workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Výhody našeho přístupu:**
- ✅ Přesně následuje oficiální vzor SDK
- ✅ Přidává caching, aby se zabránilo opakované inicializaci
- ✅ Zahrnuje logiku opakování pro robustnost v produkci
- ✅ Podporuje sledování použití tokenů
- ✅ Poskytuje lepší chybové zprávy
- ✅ Zůstává kompatibilní s oficiálními příklady

## Změny katalogu modelů

### Předtím
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Poté
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Důvod:** Nahrazen 'gpt-oss-20b' (nestandardní alias) za 'phi-3.5-mini' (oficiální alias Foundry Local).

## Závislosti

### Aktualizovaný requirements.txt

Workshop requirements.txt již obsahuje:
```
foundry-local-sdk
openai>=1.30.0
```

To jsou jediné balíčky potřebné pro integraci Foundry Local.

## Testování aktualizací

### 1. Ověřte, že Foundry Local běží

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Zkontrolujte dostupné modely

```bash
foundry model ls
```

Ujistěte se, že tyto modely jsou dostupné nebo se automaticky stáhnou:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Spusťte pracovní sešit

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Nebo otevřete ve VS Code a spusťte všechny buňky.

### 4. Očekávané chování

**Buňka 1 (Instalace):** Úspěšně nainstaluje balíčky  
**Buňka 2 (Nastavení):** Žádné chyby, importy fungují  
**Buňka 3 (Ověření):** Zobrazuje ✓ s seznamem modelů  
**Buňka 4 (Test záměru):** Zobrazuje výsledky detekce záměru  
**Buňka 5 (Směrovač):** Zobrazuje ✓ Funkce směrování připravena  
**Buňka 6 (Provádění):** Směruje výzvy na modely, zobrazuje výsledky  

### 5. Řešení problémů s připojením

Pokud se zobrazí `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Proměnné prostředí

Podporovány jsou následující proměnné prostředí:

| Proměnná | Výchozí | Popis |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Nastavte na `1` pro zobrazení použití tokenů |
| `RETRY_ON_FAIL` | `1` | Povolit logiku opakování |
| `RETRY_BACKOFF` | `1.0` | Počáteční zpoždění opakování (v sekundách) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Přepsání endpointu služby |

### Příklady použití

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migrace ze starého vzoru

Pokud máte existující kód používající přímé API volání, zde je postup migrace:

### Předtím (Přímé API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Poté (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Výhody migrace
- ✅ Automatické řízení služby
- ✅ Řešení aliasů modelů
- ✅ Výběr hardwarové optimalizace
- ✅ Lepší obsluha chyb
- ✅ Kompatibilita s OpenAI SDK
- ✅ Podpora streamování

## Reference

### Oficiální dokumentace
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Zdroj Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Referenční CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Řešení problémů**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Zdroje Workshopu
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Ukázkový pracovní sešit**: `Workshop/notebooks/session06_models_router.ipynb`

### Komunita
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Další kroky

1. **Projděte změny**: Přečtěte si aktualizované soubory  
2. **Otestujte pracovní sešit**: Spusťte session06_models_router.ipynb  
3. **Ověřte SDK**: Ujistěte se, že foundry-local-sdk je nainstalováno  
4. **Zkontrolujte službu**: Ověřte, že Foundry Local běží  
5. **Prozkoumejte dokumentaci**: Přečtěte si nový session06_README.md  

## Shrnutí

Tyto aktualizace zajišťují, že materiály Workshopu přesně následují **oficiální vzory Foundry Local SDK**, jak jsou dokumentovány v repozitáři GitHub. Všechny příklady kódu, dokumentace a nástroje nyní odpovídají doporučeným postupům Microsoftu pro lokální nasazení AI modelů.

Změny zlepšují:
- ✅ **Správnost**: Používá oficiální vzory SDK  
- ✅ **Dokumentaci**: Komplexní vysvětlení a příklady  
- ✅ **Obsluhu chyb**: Lepší zprávy a pokyny pro řešení problémů  
- ✅ **Udržovatelnost**: Následuje oficiální konvence  
- ✅ **Uživatelskou zkušenost**: Jasnější instrukce a pomoc při ladění  

---

**Aktualizováno:** 8. října 2025  
**Verze SDK:** foundry-local-sdk (nejnovější)  
**Větev Workshopu:** Reactor

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.