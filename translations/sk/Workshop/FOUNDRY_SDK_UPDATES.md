<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T15:13:54+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "sk"
}
-->
# Aktualizácie Foundry Local SDK

## Prehľad

Aktualizované poznámkové bloky Workshopu a nástroje na správne používanie **oficiálneho Foundry Local Python SDK** podľa vzorov z:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Upravené súbory

### 1. `Workshop/samples/workshop_utils.py`

**Zmeny:**
- ✅ Pridané spracovanie chýb pri importe balíka `foundry-local-sdk`
- ✅ Vylepšená dokumentácia s oficiálnymi vzormi SDK
- ✅ Zlepšené logovanie pomocou Unicode symbolov (✓, ✗, ⚠)
- ✅ Pridané komplexné docstringy s príkladmi
- ✅ Lepšie chybové hlásenia odkazujúce na príkazy CLI
- ✅ Aktualizované komentáre, aby zodpovedali oficiálnej dokumentácii SDK

**Kľúčové vylepšenia:**

#### Spracovanie chýb pri importe
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Vylepšená funkcia `get_client()`
- Pridaná podrobná dokumentácia o vzore inicializácie SDK
- Vysvetlené, že `FoundryLocalManager` automaticky spúšťa službu
- Vysvetlené rozlíšenie aliasov modelov na hardvérovo optimalizované varianty
- Zlepšené logovanie s informáciami o koncových bodoch
- Lepšie chybové hlásenia s návrhmi na riešenie problémov

#### Vylepšená funkcia `chat_once()`
- Pridaný komplexný docstring s príkladmi použitia
- Vysvetlená kompatibilita s OpenAI SDK
- Zdokumentovaná podpora streamovania (cez kwargs)
- Zlepšené chybové hlásenia s návrhmi príkazov CLI
- Pridané poznámky o kontrole dostupnosti modelov

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Zmeny:**
- ✅ Aktualizované všetky bunky markdown s odkazmi na SDK
- ✅ Vylepšené komentáre kódu s vysvetleniami vzorov SDK
- ✅ Zlepšená dokumentácia buniek a vysvetlenia
- ✅ Pridané pokyny na riešenie problémov
- ✅ Aktualizovaný katalóg modelov (nahradený 'gpt-oss-20b' za 'phi-3.5-mini')
- ✅ Lepšie formátovanie výstupu s vizuálnymi indikátormi
- ✅ Pridané odkazy na SDK a referencie v celom dokumente

**Aktualizácie po bunkách:**

#### Bunky 1 (Názov)
- Pridané odkazy na dokumentáciu SDK
- Odkázané oficiálne GitHub repozitáre

#### Bunky 2 (Scenár)
- Preformátované na očíslované kroky
- Vysvetlený vzor smerovania na základe zámeru
- Zdôraznené výhody lokálneho vykonávania

#### Bunky 3 (Inštalácia závislostí)
- Pridané vysvetlenie, čo poskytuje každý balík
- Zdokumentované schopnosti SDK (rozlíšenie aliasov, hardvérová optimalizácia)

#### Bunky 4 (Nastavenie prostredia)
- Vylepšené docstringy funkcií
- Pridané inline komentáre vysvetľujúce vzory SDK
- Zdokumentovaná štruktúra katalógu modelov
- Vysvetlené priraďovanie priorít/schopností

#### Bunky 5 (Kontrola katalógu)
- Pridané vizuálne zaškrtávacie políčka (✓)
- Lepšie formátovaný výstup

#### Bunky 6 (Test detekcie zámeru)
- Preformátovaný výstup ako tabuľka
- Zobrazuje zámer aj vybraný model

#### Bunky 7 (Funkcia smerovania)
- Komplexné vysvetlenie vzoru SDK
- Zdokumentovaný tok inicializácie
- Uvedené všetky funkcie (retry, sledovanie, chyby)
- Pridaný odkaz na SDK

#### Bunky 8 (Ukážka dávky)
- Vylepšené vysvetlenie očakávaných výsledkov
- Pridaná sekcia riešenia problémov
- Zahrnuté príkazy CLI na ladenie
- Lepšie formátovanie zobrazenia výstupu

### 3. `Workshop/notebooks/session06_README.md` (Nový súbor)

**Vytvorená komplexná dokumentácia pokrývajúca:**

1. **Prehľad**: Diagram architektúry a vysvetlenie komponentov
2. **Integrácia SDK**: Príklady kódu podľa oficiálnych vzorov
3. **Predpoklady**: Krok za krokom pokyny na nastavenie
4. **Použitie**: Ako spustiť a prispôsobiť poznámkový blok
5. **Aliasy modelov**: Vysvetlenie hardvérovo optimalizovaných variantov
6. **Riešenie problémov**: Bežné problémy a ich riešenia
7. **Rozšírenie**: Ako pridať zámery, modely a vlastnú logiku
8. **Tipy na výkon**: Najlepšie postupy pre produkčné použitie
9. **Zdroje**: Odkazy na oficiálnu dokumentáciu a komunitu

## Implementácia vzoru SDK

### Oficiálny vzor (z dokumentácie Foundry Local)

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

### Naša implementácia (v workshop_utils)

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

**Výhody nášho prístupu:**
- ✅ Presne nasleduje oficiálny vzor SDK
- ✅ Pridáva caching na zabránenie opakovanej inicializácie
- ✅ Zahŕňa logiku retry pre robustnosť v produkcii
- ✅ Podporuje sledovanie používania tokenov
- ✅ Poskytuje lepšie chybové hlásenia
- ✅ Zostáva kompatibilný s oficiálnymi príkladmi

## Zmeny katalógu modelov

### Predtým
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Potom
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Dôvod:** Nahradený 'gpt-oss-20b' (neštandardný alias) za 'phi-3.5-mini' (oficiálny alias Foundry Local).

## Závislosti

### Aktualizovaný requirements.txt

Workshop requirements.txt už obsahuje:
```
foundry-local-sdk
openai>=1.30.0
```

Toto sú jediné balíky potrebné na integráciu Foundry Local.

## Testovanie aktualizácií

### 1. Overte, že Foundry Local beží

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Skontrolujte dostupné modely

```bash
foundry model ls
```

Uistite sa, že tieto modely sú dostupné alebo sa automaticky stiahnu:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Spustite poznámkový blok

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Alebo otvorte vo VS Code a spustite všetky bunky.

### 4. Očakávané správanie

**Bunky 1 (Inštalácia):** Úspešne nainštaluje balíky  
**Bunky 2 (Nastavenie):** Žiadne chyby, importy fungujú  
**Bunky 3 (Overenie):** Zobrazuje ✓ so zoznamom modelov  
**Bunky 4 (Test zámeru):** Zobrazuje výsledky detekcie zámeru  
**Bunky 5 (Smerovač):** Zobrazuje ✓ Funkcia smerovania pripravená  
**Bunky 6 (Vykonanie):** Smeruje výzvy na modely, zobrazuje výsledky  

### 5. Riešenie problémov s chybami pripojenia

Ak vidíte `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Premenné prostredia

Podporované sú nasledujúce premenné prostredia:

| Premenná | Predvolená hodnota | Popis |
|----------|--------------------|-------|
| `SHOW_USAGE` | `0` | Nastavte na `1` pre tlač používania tokenov |
| `RETRY_ON_FAIL` | `1` | Povoliť logiku retry |
| `RETRY_BACKOFF` | `1.0` | Počiatočné oneskorenie retry (sekundy) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Prepísať koncový bod služby |

### Príklady použitia

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migrácia zo starého vzoru

Ak máte existujúci kód používajúci priame API volania, tu je postup migrácie:

### Predtým (Priame API)
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

### Potom (SDK)
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

### Výhody migrácie
- ✅ Automatické spravovanie služby
- ✅ Rozlíšenie aliasov modelov
- ✅ Výber hardvérovej optimalizácie
- ✅ Lepšie spracovanie chýb
- ✅ Kompatibilita s OpenAI SDK
- ✅ Podpora streamovania

## Referencie

### Oficiálna dokumentácia
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Zdroj Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Referencie CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Riešenie problémov**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Zdroje Workshopu
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Ukážkový poznámkový blok**: `Workshop/notebooks/session06_models_router.ipynb`

### Komunita
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Ďalšie kroky

1. **Skontrolujte zmeny**: Prečítajte si aktualizované súbory  
2. **Otestujte poznámkový blok**: Spustite session06_models_router.ipynb  
3. **Overte SDK**: Uistite sa, že foundry-local-sdk je nainštalovaný  
4. **Skontrolujte službu**: Overte, že Foundry Local beží  
5. **Preskúmajte dokumentáciu**: Prečítajte si nový session06_README.md  

## Zhrnutie

Tieto aktualizácie zabezpečujú, že materiály Workshopu presne nasledujú **oficiálne vzory Foundry Local SDK**, ako sú zdokumentované v GitHub repozitári. Všetky príklady kódu, dokumentácia a nástroje teraz zodpovedajú odporúčaným najlepším postupom Microsoftu pre lokálne nasadenie AI modelov.

Zmeny zlepšujú:
- ✅ **Správnosť**: Používa oficiálne vzory SDK  
- ✅ **Dokumentáciu**: Komplexné vysvetlenia a príklady  
- ✅ **Spracovanie chýb**: Lepšie hlásenia a pokyny na riešenie problémov  
- ✅ **Údržbu**: Nasleduje oficiálne konvencie  
- ✅ **Používateľskú skúsenosť**: Jasnejšie pokyny a pomoc pri ladení  

---

**Aktualizované:** 8. októbra 2025  
**Verzia SDK:** foundry-local-sdk (najnovšia)  
**Workshop Branch:** Reactor

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, vezmite na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.