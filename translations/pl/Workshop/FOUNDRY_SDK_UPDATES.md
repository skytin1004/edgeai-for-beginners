<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T21:36:59+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "pl"
}
-->
# Aktualizacje Foundry Local SDK

## Przegląd

Zaktualizowano notatniki warsztatowe i narzędzia, aby poprawnie korzystały z **oficjalnego Foundry Local Python SDK**, zgodnie z wzorcami z:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Zmodyfikowane pliki

### 1. `Workshop/samples/workshop_utils.py`

**Zmiany:**
- ✅ Dodano obsługę błędów importu dla pakietu `foundry-local-sdk`
- ✅ Ulepszono dokumentację zgodnie z oficjalnymi wzorcami SDK
- ✅ Poprawiono logowanie za pomocą symboli Unicode (✓, ✗, ⚠)
- ✅ Dodano szczegółowe docstringi z przykładami
- ✅ Lepsze komunikaty o błędach z odniesieniami do poleceń CLI
- ✅ Zaktualizowano komentarze, aby pasowały do dokumentacji SDK

**Kluczowe ulepszenia:**

#### Obsługa błędów importu
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Ulepszona funkcja `get_client()`
- Dodano szczegółową dokumentację dotyczącą wzorca inicjalizacji SDK
- Wyjaśniono, że `FoundryLocalManager` automatycznie uruchamia usługę
- Wyjaśniono rozwiązywanie aliasów modeli na warianty zoptymalizowane sprzętowo
- Poprawiono logowanie z informacjami o endpointach
- Lepsze komunikaty o błędach z sugestiami dotyczącymi rozwiązywania problemów

#### Ulepszona funkcja `chat_once()`
- Dodano szczegółowy docstring z przykładami użycia
- Wyjaśniono kompatybilność z OpenAI SDK
- Udokumentowano obsługę strumieniowania (przez kwargs)
- Poprawiono komunikaty o błędach z sugestiami poleceń CLI
- Dodano uwagi dotyczące sprawdzania dostępności modeli

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Zmiany:**
- ✅ Zaktualizowano wszystkie komórki markdown z odniesieniami do SDK
- ✅ Ulepszono komentarze w kodzie, wyjaśniając wzorce SDK
- ✅ Poprawiono dokumentację i wyjaśnienia w komórkach
- ✅ Dodano wskazówki dotyczące rozwiązywania problemów
- ✅ Zaktualizowano katalog modeli (zastąpiono 'gpt-oss-20b' na 'phi-3.5-mini')
- ✅ Lepsze formatowanie wyników z wizualnymi wskaźnikami
- ✅ Dodano linki i odniesienia do SDK

**Aktualizacje komórka po komórce:**

#### Komórka 1 (Tytuł)
- Dodano linki do dokumentacji SDK
- Odniesiono się do oficjalnych repozytoriów GitHub

#### Komórka 2 (Scenariusz)
- Sformatowano w kroki numerowane
- Wyjaśniono wzorzec routingu oparty na intencjach
- Podkreślono korzyści z lokalnego wykonywania

#### Komórka 3 (Instalacja zależności)
- Dodano wyjaśnienie, co zapewnia każdy pakiet
- Udokumentowano możliwości SDK (rozwiązywanie aliasów, optymalizacja sprzętowa)

#### Komórka 4 (Konfiguracja środowiska)
- Ulepszono docstringi funkcji
- Dodano komentarze w kodzie wyjaśniające wzorce SDK
- Udokumentowano strukturę katalogu modeli
- Wyjaśniono dopasowanie priorytetów/możliwości

#### Komórka 5 (Sprawdzanie katalogu)
- Dodano wizualne znaczniki (✓)
- Lepsze formatowanie wyników

#### Komórka 6 (Test wykrywania intencji)
- Wyniki sformatowane w stylu tabeli
- Pokazuje zarówno intencję, jak i wybrany model

#### Komórka 7 (Funkcja routingu)
- Szczegółowe wyjaśnienie wzorca SDK
- Udokumentowano przepływ inicjalizacji
- Wymieniono wszystkie funkcje (ponawianie prób, śledzenie, błędy)
- Dodano link do dokumentacji SDK

#### Komórka 8 (Demo wsadowe)
- Ulepszono wyjaśnienie, czego się spodziewać
- Dodano sekcję rozwiązywania problemów
- Uwzględniono polecenia CLI do debugowania
- Lepsze formatowanie wyświetlania wyników

### 3. `Workshop/notebooks/session06_README.md` (Nowy plik)

**Stworzono kompleksową dokumentację obejmującą:**

1. **Przegląd**: Diagram architektury i wyjaśnienie komponentów
2. **Integracja SDK**: Przykłady kodu zgodne z oficjalnymi wzorcami
3. **Wymagania wstępne**: Instrukcje konfiguracji krok po kroku
4. **Użycie**: Jak uruchomić i dostosować notatnik
5. **Aliasy modeli**: Wyjaśnienie wariantów zoptymalizowanych sprzętowo
6. **Rozwiązywanie problemów**: Typowe problemy i rozwiązania
7. **Rozszerzanie**: Jak dodawać intencje, modele i logikę niestandardową
8. **Wskazówki dotyczące wydajności**: Najlepsze praktyki do użytku produkcyjnego
9. **Zasoby**: Linki do oficjalnej dokumentacji i społeczności

## Implementacja wzorca SDK

### Oficjalny wzorzec (z dokumentacji Foundry Local)

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

### Nasza implementacja (w workshop_utils)

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

**Korzyści z naszego podejścia:**
- ✅ Dokładnie zgodne z oficjalnym wzorcem SDK
- ✅ Dodano buforowanie, aby uniknąć wielokrotnej inicjalizacji
- ✅ Zawiera logikę ponawiania prób dla większej niezawodności
- ✅ Obsługuje śledzenie użycia tokenów
- ✅ Zapewnia lepsze komunikaty o błędach
- ✅ Pozostaje kompatybilne z oficjalnymi przykładami

## Zmiany w katalogu modeli

### Przed
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Po
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Powód:** Zastąpiono 'gpt-oss-20b' (niestandardowy alias) na 'phi-3.5-mini' (oficjalny alias Foundry Local).

## Zależności

### Zaktualizowany plik requirements.txt

Plik requirements.txt warsztatu już zawiera:
```
foundry-local-sdk
openai>=1.30.0
```

To jedyne pakiety potrzebne do integracji z Foundry Local.

## Testowanie aktualizacji

### 1. Sprawdź, czy Foundry Local działa

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Sprawdź dostępne modele

```bash
foundry model ls
```

Upewnij się, że te modele są dostępne lub zostaną automatycznie pobrane:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Uruchom notatnik

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Lub otwórz w VS Code i uruchom wszystkie komórki.

### 4. Oczekiwane zachowanie

**Komórka 1 (Instalacja):** Pakiety instalują się pomyślnie  
**Komórka 2 (Konfiguracja):** Brak błędów, importy działają  
**Komórka 3 (Weryfikacja):** Wyświetla ✓ z listą modeli  
**Komórka 4 (Test intencji):** Wyświetla wyniki wykrywania intencji  
**Komórka 5 (Router):** Wyświetla ✓ Funkcja routingu gotowa  
**Komórka 6 (Wykonanie):** Kieruje zapytania do modeli, wyświetla wyniki  

### 5. Rozwiązywanie problemów z błędami połączenia

Jeśli zobaczysz `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Zmienne środowiskowe

Obsługiwane są następujące zmienne środowiskowe:

| Zmienna | Domyślna | Opis |
|---------|----------|------|
| `SHOW_USAGE` | `0` | Ustaw na `1`, aby wyświetlić użycie tokenów |
| `RETRY_ON_FAIL` | `1` | Włącz logikę ponawiania prób |
| `RETRY_BACKOFF` | `1.0` | Początkowe opóźnienie ponawiania (sekundy) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Nadpisz endpoint usługi |

### Przykłady użycia

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migracja ze starego wzorca

Jeśli masz istniejący kod korzystający z bezpośrednich wywołań API, oto jak go zmigrować:

### Przed (bezpośrednie API)
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

### Po (SDK)
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

### Korzyści z migracji
- ✅ Automatyczne zarządzanie usługą
- ✅ Rozwiązywanie aliasów modeli
- ✅ Wybór optymalizacji sprzętowej
- ✅ Lepsza obsługa błędów
- ✅ Kompatybilność z OpenAI SDK
- ✅ Obsługa strumieniowania

## Odniesienia

### Oficjalna dokumentacja
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local  
- **Źródło Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **Referencja CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **Rozwiązywanie problemów**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### Zasoby warsztatowe
- **README sesji 06**: `Workshop/notebooks/session06_README.md`  
- **Narzędzia warsztatowe**: `Workshop/samples/workshop_utils.py`  
- **Przykładowy notatnik**: `Workshop/notebooks/session06_models_router.ipynb`  

### Społeczność
- **Discord**: https://aka.ms/foundry-local-discord  
- **Problemy GitHub**: https://github.com/microsoft/Foundry-Local/issues  

## Kolejne kroki

1. **Przejrzyj zmiany**: Przeczytaj zaktualizowane pliki  
2. **Przetestuj notatnik**: Uruchom session06_models_router.ipynb  
3. **Zweryfikuj SDK**: Upewnij się, że foundry-local-sdk jest zainstalowane  
4. **Sprawdź usługę**: Potwierdź, że Foundry Local działa  
5. **Przeglądaj dokumentację**: Przeczytaj nowy plik session06_README.md  

## Podsumowanie

Te aktualizacje zapewniają, że materiały warsztatowe dokładnie podążają za **oficjalnymi wzorcami Foundry Local SDK**, zgodnie z dokumentacją w repozytorium GitHub. Wszystkie przykłady kodu, dokumentacja i narzędzia są teraz zgodne z zalecanymi najlepszymi praktykami Microsoftu dotyczącymi lokalnego wdrażania modeli AI.

Zmiany poprawiają:
- ✅ **Poprawność**: Korzysta z oficjalnych wzorców SDK  
- ✅ **Dokumentację**: Kompleksowe wyjaśnienia i przykłady  
- ✅ **Obsługę błędów**: Lepsze komunikaty i wskazówki dotyczące rozwiązywania problemów  
- ✅ **Utrzymanie**: Zgodność z oficjalnymi konwencjami  
- ✅ **Doświadczenie użytkownika**: Jaśniejsze instrukcje i pomoc w debugowaniu  

---

**Zaktualizowano:** 8 października 2025  
**Wersja SDK:** foundry-local-sdk (najnowsza)  
**Gałąź warsztatu:** Reactor  

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.