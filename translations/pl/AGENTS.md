<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:33:20+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pl"
}
-->
# AGENTS.md

## Przegląd projektu

EdgeAI for Beginners to kompleksowe repozytorium edukacyjne uczące rozwoju Edge AI z wykorzystaniem Małych Modeli Językowych (SLM). Kurs obejmuje podstawy EdgeAI, wdrażanie modeli, techniki optymalizacji oraz implementacje gotowe do produkcji z użyciem Microsoft Foundry Local i różnych frameworków AI.

**Kluczowe technologie:**
- Python 3.8+ (główny język dla przykładów AI/ML)
- .NET C# (przykłady AI/ML)
- JavaScript/Node.js z Electron (dla aplikacji desktopowych)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Frameworki AI: LangChain, Semantic Kernel, Chainlit
- Optymalizacja modeli: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Typ repozytorium:** Repozytorium edukacyjne z 8 modułami i 10 kompleksowymi aplikacjami przykładowymi

**Architektura:** Wielomodułowa ścieżka nauki z praktycznymi przykładami pokazującymi wzorce wdrażania Edge AI

## Struktura repozytorium

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

## Komendy konfiguracji

### Konfiguracja repozytorium

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Konfiguracja przykładów w Pythonie (Moduł08 i przykłady w Pythonie)

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

### Konfiguracja przykładów w Node.js (Przykład 08 - Windows Chat App)

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

### Konfiguracja Foundry Local

Foundry Local jest wymagane do uruchomienia przykładów z Modułu08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Przebieg pracy deweloperskiej

### Tworzenie treści

To repozytorium zawiera głównie **edukacyjne treści w formacie Markdown**. Podczas wprowadzania zmian:

1. Edytuj pliki `.md` w odpowiednich katalogach modułów
2. Przestrzegaj istniejących wzorców formatowania
3. Upewnij się, że przykłady kodu są poprawne i przetestowane
4. Zaktualizuj odpowiednie treści tłumaczone, jeśli to konieczne (lub pozwól automatyzacji się tym zająć)

### Tworzenie aplikacji przykładowych

Dla przykładów w Pythonie (przykłady 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Dla przykładu w Electron (przykład 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testowanie aplikacji przykładowych

Przykłady w Pythonie nie mają testów automatycznych, ale można je zweryfikować, uruchamiając je:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Przykład w Electron posiada infrastrukturę testową:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instrukcje testowania

### Walidacja treści

Repozytorium korzysta z automatycznych przepływów pracy tłumaczeniowej. Nie jest wymagane ręczne testowanie tłumaczeń.

**Ręczna walidacja zmian treści:**
1. Przejrzyj renderowanie Markdown, podglądając pliki `.md`
2. Upewnij się, że wszystkie linki prowadzą do poprawnych celów
3. Przetestuj fragmenty kodu zawarte w dokumentacji
4. Sprawdź, czy obrazy ładują się poprawnie

### Testowanie aplikacji przykładowych

**Moduł08/przykłady/08 (aplikacja Electron) posiada kompleksowe testy:**
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

**Przykłady w Pythonie powinny być testowane ręcznie:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Wytyczne dotyczące stylu kodu

### Treści w Markdown

- Używaj spójnej hierarchii nagłówków (# dla tytułu, ## dla głównych sekcji, ### dla podsekcji)
- Dodawaj bloki kodu ze specyfikatorami języka: ```python, ```bash, ```javascript
- Przestrzegaj istniejącego formatowania dla tabel, list i wyróżnień
- Zachowaj czytelność linii (celuj w ~80-100 znaków, ale nie rygorystycznie)
- Używaj linków względnych dla odwołań wewnętrznych

### Styl kodu w Pythonie

- Przestrzegaj konwencji PEP 8
- Używaj wskazówek typów, gdzie to możliwe
- Dodawaj docstringi do funkcji i klas
- Używaj znaczących nazw zmiennych
- Twórz funkcje skoncentrowane i zwięzłe

### Styl kodu w JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Kluczowe konwencje:**
- Konfiguracja ESLint dostarczona w przykładzie 08
- Prettier do formatowania kodu
- Używaj nowoczesnej składni ES6+
- Przestrzegaj istniejących wzorców w kodzie

## Wytyczne dotyczące pull requestów

### Format tytułu
```
[ModuleXX] Brief description of change
```
lub
```
[Module08/samples/XX] Description for sample changes
```

### Przed przesłaniem

**Dla zmian treści:**
- Przejrzyj wszystkie zmodyfikowane pliki Markdown
- Upewnij się, że linki i obrazy działają
- Sprawdź błędy ortograficzne i gramatyczne

**Dla zmian kodu przykładowego (Moduł08/przykłady/08):**
```bash
npm run lint
npm test
```

**Dla zmian w przykładach w Pythonie:**
- Przetestuj, czy przykład działa poprawnie
- Zweryfikuj obsługę błędów
- Sprawdź kompatybilność z Foundry Local

### Proces przeglądu

- Zmiany w treściach edukacyjnych są oceniane pod kątem dokładności i jasności
- Przykłady kodu są testowane pod kątem funkcjonalności
- Aktualizacje tłumaczeń są obsługiwane automatycznie przez GitHub Actions

## System tłumaczeń

**WAŻNE:** To repozytorium korzysta z automatycznego tłumaczenia za pomocą GitHub Actions.

- Tłumaczenia znajdują się w katalogu `/translations/` (ponad 50 języków)
- Automatyzowane za pomocą przepływu pracy `co-op-translator.yml`
- **NIE edytuj ręcznie plików tłumaczeń** - zostaną nadpisane
- Edytuj tylko angielskie pliki źródłowe w katalogu głównym i modułach
- Tłumaczenia są generowane automatycznie po przesłaniu zmian do gałęzi `main`

## Integracja Foundry Local

Większość przykładów z Modułu08 wymaga uruchomienia Microsoft Foundry Local:

### Uruchamianie Foundry Local
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

### Weryfikacja Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Zmienne środowiskowe dla przykładów

Większość przykładów korzysta z tych zmiennych środowiskowych:
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

## Budowa i wdrażanie

### Wdrażanie treści

To repozytorium zawiera głównie dokumentację - proces budowy nie jest wymagany dla treści.

### Budowa aplikacji przykładowych

**Aplikacja Electron (Moduł08/przykłady/08):**
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

**Przykłady w Pythonie:**
Brak procesu budowy - przykłady są uruchamiane bezpośrednio za pomocą interpretera Pythona.

## Typowe problemy i rozwiązywanie

### Foundry Local nie działa
**Problem:** Przykłady kończą się błędami połączenia

**Rozwiązanie:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problemy z wirtualnym środowiskiem Pythona
**Problem:** Błędy importu modułów

**Rozwiązanie:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Problemy z budową Electron
**Problem:** Błędy przy npm install lub budowie

**Rozwiązanie:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflikty w przepływie pracy tłumaczeniowej
**Problem:** Konflikty PR tłumaczeń z Twoimi zmianami

**Rozwiązanie:**
- Edytuj tylko angielskie pliki źródłowe
- Pozwól automatycznemu przepływowi tłumaczeń obsłużyć tłumaczenia
- Jeśli wystąpią konflikty, scal `main` z Twoją gałęzią po scaleniu tłumaczeń

## Dodatkowe zasoby

### Ścieżki nauki
- **Ścieżka dla początkujących:** Moduły 01-02 (7-9 godzin)
- **Ścieżka średniozaawansowana:** Moduły 03-04 (9-11 godzin)
- **Ścieżka zaawansowana:** Moduły 05-07 (12-15 godzin)
- **Ścieżka ekspercka:** Moduł 08 (8-10 godzin)

### Kluczowe treści modułów
- **Moduł01:** Podstawy EdgeAI i studia przypadków
- **Moduł02:** Rodziny i architektury Małych Modeli Językowych (SLM)
- **Moduł03:** Strategie wdrażania lokalnego i w chmurze
- **Moduł04:** Optymalizacja modeli z użyciem różnych frameworków
- **Moduł05:** SLMOps - operacje produkcyjne
- **Moduł06:** Agenci AI i wywoływanie funkcji
- **Moduł07:** Implementacje specyficzne dla platform
- **Moduł08:** Narzędzia Foundry Local z 10 kompleksowymi przykładami

### Zewnętrzne zależności
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokalny runtime modeli AI
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework optymalizacyjny
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Narzędzie do optymalizacji modeli
- [OpenVINO](https://docs.openvino.ai/) - Narzędzie optymalizacyjne Intela

## Uwagi specyficzne dla projektu

### Przykłady aplikacji z Modułu08

Repozytorium zawiera 10 kompleksowych aplikacji przykładowych:

1. **01-REST Chat Quickstart** - Podstawowa integracja OpenAI SDK
2. **02-OpenAI SDK Integration** - Zaawansowane funkcje SDK
3. **03-Model Discovery & Benchmarking** - Narzędzia do porównywania modeli
4. **04-Chainlit RAG Application** - Generacja wspomagana wyszukiwaniem
5. **05-Multi-Agent Orchestration** - Podstawowa koordynacja agentów
6. **06-Models-as-Tools Router** - Inteligentne trasowanie modeli
7. **07-Direct API Client** - Niskopoziomowa integracja API
8. **08-Windows 11 Chat App** - Natywna aplikacja desktopowa Electron
9. **09-Advanced Multi-Agent System** - Złożona orkiestracja agentów
10. **10-Foundry Tools Framework** - Integracja LangChain/Semantic Kernel

Każdy przykład pokazuje różne aspekty rozwoju Edge AI z Foundry Local.

### Uwagi dotyczące wydajności

- SLM są zoptymalizowane do wdrożeń na urządzeniach brzegowych (2-16GB RAM)
- Lokalna inferencja zapewnia czasy odpowiedzi 50-500ms
- Techniki kwantyzacji osiągają redukcję rozmiaru o 75% przy zachowaniu 85% wydajności
- Możliwości rozmów w czasie rzeczywistym z lokalnymi modelami

### Bezpieczeństwo i prywatność

- Wszystkie procesy odbywają się lokalnie - dane nie są wysyłane do chmury
- Odpowiednie dla aplikacji wrażliwych na prywatność (opieka zdrowotna, finanse)
- Spełnia wymagania dotyczące suwerenności danych
- Foundry Local działa całkowicie na lokalnym sprzęcie

---

**To jest repozytorium edukacyjne skoncentrowane na nauczaniu rozwoju Edge AI. Głównym wzorcem wkładu jest ulepszanie treści edukacyjnych oraz dodawanie/rozbudowa aplikacji przykładowych demonstrujących koncepcje Edge AI.**

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.