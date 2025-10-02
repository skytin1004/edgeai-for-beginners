<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T12:46:32+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "pl"
}
-->
# Przewodnik po Rozwoju Windows Edge AI

## Wprowadzenie

Witamy w Windows Edge AI Development - kompleksowym przewodniku po tworzeniu inteligentnych aplikacji wykorzystujących moc AI na urządzeniach dzięki platformie Windows AI Foundry firmy Microsoft. Ten przewodnik jest przeznaczony dla programistów Windows, którzy chcą zintegrować najnowocześniejsze funkcje Edge AI w swoich aplikacjach, korzystając z pełnego zakresu akceleracji sprzętowej Windows.

### Zalety Windows AI

Windows AI Foundry to jednolita, niezawodna i bezpieczna platforma wspierająca pełny cykl życia programisty AI - od wyboru i dostosowania modelu, przez optymalizację, aż po wdrożenie na CPU, GPU, NPU i hybrydowych architekturach chmurowych. Platforma ta demokratyzuje rozwój AI, oferując:

- **Abstrakcję Sprzętową**: Bezproblemowe wdrożenie na układach AMD, Intel, NVIDIA i Qualcomm
- **Inteligencję na Urządzeniu**: AI chroniące prywatność, działające całkowicie na lokalnym sprzęcie
- **Optymalizowaną Wydajność**: Modele zoptymalizowane dla konfiguracji sprzętowych Windows
- **Gotowość dla Przedsiębiorstw**: Funkcje bezpieczeństwa i zgodności na poziomie produkcyjnym

### Dlaczego Windows dla Edge AI?

**Uniwersalne Wsparcie Sprzętowe**  
Windows ML automatycznie optymalizuje sprzęt w całym ekosystemie Windows, zapewniając, że aplikacje AI działają optymalnie niezależnie od architektury układu.

**Zintegrowany Runtime AI**  
Wbudowany silnik inferencji Windows ML eliminuje skomplikowane wymagania konfiguracji, pozwalając programistom skupić się na logice aplikacji zamiast na kwestiach infrastrukturalnych.

**Optymalizacja Copilot+ PC**  
Dedykowane API zaprojektowane specjalnie dla urządzeń Windows nowej generacji z dedykowanymi jednostkami przetwarzania neuronowego (NPU), zapewniające wyjątkową wydajność na wat.

**Ekosystem Programistyczny**  
Bogate narzędzia, w tym integracja z Visual Studio, kompleksowa dokumentacja i przykładowe aplikacje, które przyspieszają cykle rozwoju.

## Cele Nauki

Po ukończeniu tego przewodnika rozwoju Windows Edge AI, opanujesz kluczowe umiejętności potrzebne do tworzenia aplikacji AI gotowych do produkcji na platformie Windows.

### Kluczowe Kompetencje Techniczne

**Opanowanie Windows AI Foundry**  
- Zrozumienie architektury i komponentów platformy Windows AI Foundry  
- Nawigacja po pełnym cyklu rozwoju AI w ekosystemie Windows  
- Wdrażanie najlepszych praktyk bezpieczeństwa dla aplikacji AI na urządzeniach  
- Optymalizacja aplikacji dla różnych konfiguracji sprzętowych Windows  

**Ekspertyza w Integracji API**  
- Opanowanie API Windows AI dla aplikacji tekstowych, wizualnych i multimodalnych  
- Wdrażanie integracji modelu językowego Phi Silica dla generowania tekstu i rozumowania  
- Wykorzystanie możliwości widzenia komputerowego za pomocą wbudowanych API przetwarzania obrazów  
- Dostosowywanie modeli wstępnie wytrenowanych za pomocą technik LoRA (Low-Rank Adaptation)  

**Implementacja Foundry Local**  
- Przeglądanie, ocena i wdrażanie otwartych modeli językowych za pomocą Foundry Local CLI  
- Zrozumienie optymalizacji i kwantyzacji modeli dla lokalnego wdrożenia  
- Wdrażanie funkcji AI offline działających bez połączenia z internetem  
- Zarządzanie cyklami życia modeli i ich aktualizacjami w środowiskach produkcyjnych  

**Wdrożenie Windows ML**  
- Wprowadzanie niestandardowych modeli ONNX do aplikacji Windows za pomocą Windows ML  
- Wykorzystanie automatycznej akceleracji sprzętowej na architekturach CPU, GPU i NPU  
- Implementacja inferencji w czasie rzeczywistym z optymalnym wykorzystaniem zasobów  
- Projektowanie skalowalnych aplikacji AI dla różnych kategorii urządzeń Windows  

### Umiejętności Tworzenia Aplikacji

**Rozwój Windows Cross-Platform**  
- Tworzenie aplikacji zasilanych AI za pomocą .NET MAUI dla uniwersalnego wdrożenia na Windows  
- Integracja funkcji AI w aplikacjach Win32, UWP i Progressive Web Applications  
- Implementacja responsywnych projektów UI dostosowujących się do stanów przetwarzania AI  
- Obsługa asynchronicznych operacji AI z odpowiednimi wzorcami doświadczenia użytkownika  

**Optymalizacja Wydajności**  
- Profilowanie i optymalizacja wydajności inferencji AI na różnych konfiguracjach sprzętowych  
- Implementacja efektywnego zarządzania pamięcią dla dużych modeli językowych  
- Projektowanie aplikacji, które łagodnie degradują się w zależności od dostępnych możliwości sprzętowych  
- Stosowanie strategii buforowania dla często używanych operacji AI  

**Gotowość Produkcyjna**  
- Implementacja kompleksowego obsługi błędów i mechanizmów awaryjnych  
- Projektowanie telemetrii i monitorowania wydajności aplikacji AI  
- Stosowanie najlepszych praktyk bezpieczeństwa dla lokalnego przechowywania i wykonywania modeli AI  
- Planowanie strategii wdrożeniowych dla aplikacji przedsiębiorstw i konsumentów  

### Zrozumienie Biznesowe i Strategiczne

**Architektura Aplikacji AI**  
- Projektowanie hybrydowych architektur optymalizujących między lokalnym a chmurowym przetwarzaniem AI  
- Ocena kompromisów między rozmiarem modelu, dokładnością a szybkością inferencji  
- Planowanie architektur przepływu danych, które zachowują prywatność przy jednoczesnym umożliwieniu inteligencji  
- Implementacja opłacalnych rozwiązań AI, które skalują się wraz z wymaganiami użytkowników  

**Pozycjonowanie na Rynku**  
- Zrozumienie przewag konkurencyjnych aplikacji AI natywnych dla Windows  
- Identyfikacja przypadków użycia, w których AI na urządzeniu zapewnia lepsze doświadczenia użytkownika  
- Opracowanie strategii wejścia na rynek dla aplikacji Windows wzbogaconych o AI  
- Pozycjonowanie aplikacji w celu wykorzystania korzyści ekosystemu Windows  

## Przykłady AI w Windows App SDK

Windows App SDK oferuje kompleksowe przykłady demonstrujące integrację AI w różnych frameworkach i scenariuszach wdrożeniowych. Te przykłady są kluczowymi odniesieniami dla zrozumienia wzorców rozwoju AI w Windows.

### Przykłady Windows AI Foundry

| Przykład | Framework | Obszar Zastosowania | Kluczowe Funkcje |
|----------|-----------|---------------------|------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integracja API Windows AI | Kompletny przykład aplikacji WinUI demonstrujący API Windows AI, optymalizację ARM64, wdrożenie pakietowe |

**Kluczowe Technologie:**  
- API Windows AI  
- Framework WinUI 3  
- Optymalizacja platformy ARM64  
- Kompatybilność z Copilot+ PC  
- Wdrożenie aplikacji w pakiecie  

**Wymagania Wstępne:**  
- Windows 11 z zalecanym Copilot+ PC  
- Visual Studio 2022  
- Konfiguracja kompilacji ARM64  
- Windows App SDK 1.8.1+  

### Przykłady Windows ML

#### Przykłady w C++

| Przykład | Typ | Obszar Zastosowania | Kluczowe Funkcje |
|----------|-----|---------------------|------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikacja Konsolowa | Podstawy Windows ML | Odkrywanie EP, opcje wiersza poleceń, kompilacja modelu |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikacja Konsolowa | Wdrożenie Framework | Współdzielony runtime, mniejszy ślad wdrożeniowy |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikacja Konsolowa | Wdrożenie Samodzielne | Wdrożenie autonomiczne, brak zależności runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Użycie Biblioteki | WindowsML w bibliotece współdzielonej, zarządzanie pamięcią |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Tutorial ResNet | Konwersja modelu, kompilacja EP, tutorial Build 2025 |

#### Przykłady w C#

**Aplikacje Konsolowe**

| Przykład | Typ | Obszar Zastosowania | Kluczowe Funkcje |
|----------|-----|---------------------|------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Aplikacja Konsolowa | Podstawowa Integracja C# | Współdzielone użycie helperów, interfejs wiersza poleceń |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Tutorial ResNet | Konwersja modelu, kompilacja EP, tutorial Build 2025 |

**Aplikacje GUI**

| Przykład | Framework | Obszar Zastosowania | Kluczowe Funkcje |
|----------|-----------|---------------------|------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI Desktopowe | Klasyfikacja obrazów z interfejsem WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradycyjne GUI | Klasyfikacja obrazów z Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Nowoczesne GUI | Klasyfikacja obrazów z interfejsem WinUI 3 |

#### Przykłady w Pythonie

| Przykład | Język | Obszar Zastosowania | Kluczowe Funkcje |
|----------|-------|---------------------|------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasyfikacja Obrazów | Powiązania WinML dla Pythona, przetwarzanie obrazów w partiach |

### Wymagania Wstępne dla Przykładów

**Wymagania Systemowe:**  
- Komputer z Windows 11 w wersji 24H2 (build 26100) lub wyższej  
- Visual Studio 2022 z obciążeniami C++ i .NET  
- Windows App SDK 1.8.1 lub nowszy  
- Python 3.10-3.13 dla przykładów w Pythonie na urządzeniach x64 i ARM64  

**Specyficzne dla Windows AI Foundry:**  
- Zalecany Copilot+ PC dla optymalnej wydajności  
- Konfiguracja kompilacji ARM64 dla przykładów Windows AI  
- Wymagana tożsamość pakietu (aplikacje niepakietowe nie są już wspierane)  

### Typowy Przebieg Pracy z Przykładami

Większość przykładów Windows ML podąża za tym standardowym schematem:

1. **Inicjalizacja Środowiska** - Utworzenie środowiska ONNX Runtime  
2. **Rejestracja Dostawców Wykonania** - Odkrywanie i rejestracja dostępnych akceleratorów sprzętowych (CPU, GPU, NPU)  
3. **Ładowanie Modelu** - Ładowanie modelu ONNX, opcjonalnie kompilacja dla docelowego sprzętu  
4. **Przetwarzanie Wstępne Wejścia** - Konwersja obrazów/danych do formatu wejściowego modelu  
5. **Wykonanie Inferencji** - Wykonanie modelu i uzyskanie przewidywań  
6. **Przetwarzanie Wyników** - Zastosowanie softmax i wyświetlenie najlepszych przewidywań  

### Używane Pliki Modeli

| Model | Cel | Dołączony | Uwagi |
|-------|-----|----------|-------|
| SqueezeNet | Lekka klasyfikacja obrazów | ✅ Dołączony | Wstępnie wytrenowany, gotowy do użycia |
| ResNet-50 | Klasyfikacja obrazów o wysokiej dokładności | ❌ Wymaga konwersji | Użyj [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) do konwersji |

### Wsparcie Sprzętowe

Wszystkie przykłady automatycznie wykrywają i wykorzystują dostępny sprzęt:  
- **CPU** - Uniwersalne wsparcie na wszystkich urządzeniach Windows  
- **GPU** - Automatyczne wykrywanie i optymalizacja dla dostępnego sprzętu graficznego  
- **NPU** - Wykorzystanie jednostek przetwarzania neuronowego na wspieranych urządzeniach (Copilot+ PC)  

## Komponenty Platformy Windows AI Foundry

### 1. API Windows AI

API Windows AI oferują gotowe do użycia funkcje AI zasilane modelami na urządzeniach, zoptymalizowane pod kątem efektywności i wydajności na urządzeniach Copilot+ PC, z minimalnymi wymaganiami konfiguracji.

#### Główne Kategorie API

**Model Językowy Phi Silica**  
- Mały, ale potężny model językowy do generowania tekstu i rozumowania  
- Zoptymalizowany pod kątem inferencji w czasie rzeczywistym przy minimalnym zużyciu energii  
- Wsparcie dla dostosowywania za pomocą technik LoRA  
- Integracja z wyszukiwaniem semantycznym Windows i pozyskiwaniem wiedzy  

**API Widzenia Komputerowego**  
- **Rozpoznawanie Tekstu (OCR)**: Wyodrębnianie tekstu z obrazów z wysoką dokładnością  
- **Super Rozdzielczość Obrazów**: Skalowanie obrazów za pomocą lokalnych modeli AI  
- **Segmentacja Obrazów**: Identyfikacja i izolacja konkretnych obiektów na obrazach  
- **Opis Obrazów**: Generowanie szczegółowych opisów tekstowych dla treści wizualnych  
- **Usuwanie Obiektów**: Usuwanie niechcianych obiektów z obrazów za pomocą AI  

**Funkcje Multimodalne**  
- **Integracja Wizji i Języka**: Łączenie rozumienia tekstu i obrazu  
- **Wyszukiwanie Semantyczne**: Umożliwienie zapytań w języku naturalnym w treściach multimedialnych  
- **Pozyskiwanie Wiedzy**: Budowanie inteligentnych doświadczeń wyszukiwania z lokalnymi danymi  

### 2. Foundry Local

Foundry Local zapewnia programistom szybki dostęp do gotowych do użycia otwartych modeli językowych na Windows Silicon, oferując możliwość przeglądania, testowania, interakcji i wdrażania modeli w lokalnych aplikacjach.

#### Przykładowe Aplikacje Foundry Local

Repozytorium [Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) oferuje kompleksowe przykłady w różnych językach programowania i frameworkach, demonstrujące różne wzorce integracji i przypadki użycia.

| Przykład | Język/Framework | Obszar Zastosowania | Kluczowe Funkcje |
|----------|-----------------|---------------------|------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementacja RAG | Integracja Semantic Kernel, magazyn wektorów Qdrant, osadzenia JINA, wprowadzanie dokumentów, streaming czatu |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Aplikacja Czatu na Desktop | Czatu cross-platformowy, przełączanie modeli lokalnych/chmurowych, integracja OpenAI SDK, streaming w czasie rzeczywistym |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Podstawowa Integracja | Proste użycie SDK, inicjalizacja modelu, podstawowa funkcjonalność czatu |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Podstawowa Integracja | Użycie SDK dla Pythona, odpowiedzi streamingowe, kompatybilne API OpenAI |
| [rust/hello-foundry-local](https
- **Funkcje**: Wybór modelu, strumieniowe odpowiedzi, obsługa błędów, wdrożenie międzyplatformowe  
- **Architektura**: Główny proces Electron, komunikacja IPC, bezpieczne skrypty preload  

**Przykłady integracji SDK**  
- **JavaScript (Node.js)**: Podstawowa interakcja z modelem i strumieniowe odpowiedzi  
- **Python**: Wykorzystanie API kompatybilnego z OpenAI z asynchronicznym strumieniowaniem  
- **Rust**: Niskopoziomowa integracja z reqwest i tokio dla operacji asynchronicznych  

#### Wymagania wstępne dla lokalnych próbek Foundry  

**Wymagania systemowe:**  
- Windows 11 z zainstalowanym Foundry Local  
- Node.js v16+ dla próbek JavaScript/Electron  
- .NET 8.0+ dla próbek C#  
- Python 3.10+ dla próbek Python  
- Rust 1.70+ dla próbek Rust  

**Instalacja:**  
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```
  

#### Konfiguracja specyficzna dla próbek  

**Próbka dotNET RAG:**  
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```
  
**Próbka Electron Chat:**  
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```
  
**Próbki JavaScript/Python/Rust:**  
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```
  

#### Kluczowe funkcje  

**Katalog modeli**  
- Kompleksowa kolekcja zoptymalizowanych modeli open-source  
- Modele zoptymalizowane dla CPU, GPU i NPU, gotowe do natychmiastowego wdrożenia  
- Obsługa popularnych rodzin modeli, takich jak Llama, Mistral, Phi oraz modeli specjalistycznych  

**Integracja CLI**  
- Interfejs wiersza poleceń do zarządzania modelami i ich wdrażania  
- Zautomatyzowane procesy optymalizacji i kwantyzacji  
- Integracja z popularnymi środowiskami programistycznymi i pipeline'ami CI/CD  

**Lokalne wdrożenie**  
- Pełna praca offline bez zależności od chmury  
- Obsługa niestandardowych formatów i konfiguracji modeli  
- Wydajne serwowanie modeli z automatyczną optymalizacją sprzętową  

### 3. Windows ML  

Windows ML to podstawowa platforma AI i zintegrowany runtime inferencji na Windows, umożliwiająca deweloperom efektywne wdrażanie niestandardowych modeli w szerokim ekosystemie sprzętowym Windows.  

#### Korzyści architektoniczne  

**Uniwersalne wsparcie sprzętowe**  
- Automatyczna optymalizacja dla układów AMD, Intel, NVIDIA i Qualcomm  
- Obsługa CPU, GPU i NPU z przełączaniem w tle  
- Abstrakcja sprzętowa eliminująca konieczność optymalizacji specyficznej dla platformy  

**Elastyczność modeli**  
- Obsługa formatu modelu ONNX z automatyczną konwersją z popularnych frameworków  
- Wdrożenie niestandardowych modeli z wydajnością na poziomie produkcyjnym  
- Integracja z istniejącymi architekturami aplikacji Windows  

**Integracja dla przedsiębiorstw**  
- Zgodność z ramami bezpieczeństwa i zgodności Windows  
- Obsługa narzędzi wdrożeniowych i zarządzania dla przedsiębiorstw  
- Integracja z systemami zarządzania i monitorowania urządzeń Windows  

## Przebieg pracy deweloperskiej  

### Faza 1: Przygotowanie środowiska i konfiguracja narzędzi  

**Przygotowanie środowiska deweloperskiego**  
1. Zainstaluj Visual Studio 2022 z obciążeniami C++ i .NET  
2. Zainstaluj Windows App SDK 1.8.1 lub nowszy  
3. Skonfiguruj narzędzia CLI Windows AI Foundry  
4. Ustaw rozszerzenie AI Toolkit dla Visual Studio Code  
5. Skonfiguruj narzędzia do profilowania wydajności i monitorowania  
6. Upewnij się, że konfiguracja ARM64 jest ustawiona dla optymalizacji Copilot+ PC  

**Konfiguracja repozytorium próbek**  
1. Sklonuj [repozytorium próbek Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)  
2. Przejdź do `Samples/WindowsAIFoundry/cs-winui` dla przykładów API Windows AI  
3. Przejdź do `Samples/WindowsML` dla kompleksowych przykładów Windows ML  
4. Przejrzyj [wymagania dotyczące budowy](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) dla docelowych platform  

**Eksploracja galerii AI Dev**  
- Przeglądaj aplikacje przykładowe i implementacje referencyjne  
- Testuj API Windows AI za pomocą interaktywnych demonstracji  
- Przeglądaj kod źródłowy dla najlepszych praktyk i wzorców  
- Identyfikuj odpowiednie próbki dla swojego konkretnego przypadku użycia  

### Faza 2: Wybór modelu i integracja  

**Analiza wymagań**  
- Zdefiniuj wymagania funkcjonalne dla możliwości AI  
- Ustal ograniczenia wydajności i cele optymalizacyjne  
- Oceń wymagania dotyczące prywatności i bezpieczeństwa  
- Zaplanuj architekturę wdrożenia i strategie skalowania  

**Ocena modeli**  
- Użyj Foundry Local do testowania modeli open-source dla swojego przypadku użycia  
- Przeprowadź benchmark API Windows AI względem wymagań niestandardowych modeli  
- Oceń kompromisy między rozmiarem modelu, dokładnością a szybkością inferencji  
- Prototypuj podejścia integracyjne z wybranymi modelami  

### Faza 3: Rozwój aplikacji  

**Integracja podstawowa**  
- Zaimplementuj integrację API Windows AI z odpowiednią obsługą błędów  
- Zaprojektuj interfejsy użytkownika uwzględniające przepływy pracy związane z przetwarzaniem AI  
- Zaimplementuj strategie buforowania i optymalizacji dla inferencji modeli  
- Dodaj telemetrię i monitorowanie wydajności operacji AI  

**Testowanie i walidacja**  
- Testuj aplikacje na różnych konfiguracjach sprzętowych Windows  
- Waliduj metryki wydajności pod różnymi warunkami obciążenia  
- Zaimplementuj testy automatyczne dla niezawodności funkcjonalności AI  
- Przeprowadź testy doświadczenia użytkownika z funkcjami wspomaganymi AI  

### Faza 4: Optymalizacja i wdrożenie  

**Optymalizacja wydajności**  
- Profiluj wydajność aplikacji na docelowych konfiguracjach sprzętowych  
- Optymalizuj wykorzystanie pamięci i strategie ładowania modeli  
- Zaimplementuj adaptacyjne zachowanie w zależności od dostępnych możliwości sprzętowych  
- Dopracuj doświadczenie użytkownika dla różnych scenariuszy wydajności  

**Wdrożenie produkcyjne**  
- Pakuj aplikacje z odpowiednimi zależnościami modeli AI  
- Zaimplementuj mechanizmy aktualizacji dla modeli i logiki aplikacji  
- Skonfiguruj monitorowanie i analitykę dla środowisk produkcyjnych  
- Zaplanuj strategie wdrożenia dla przedsiębiorstw i konsumentów  

## Praktyczne przykłady implementacji  

### Przykład 1: Inteligentna aplikacja do przetwarzania dokumentów  

Zbuduj aplikację Windows, która przetwarza dokumenty za pomocą wielu możliwości AI:  

**Wykorzystane technologie:**  
- Phi Silica do podsumowywania dokumentów i odpowiadania na pytania  
- API OCR do ekstrakcji tekstu ze skanowanych dokumentów  
- API opisu obrazów do analizy wykresów i diagramów  
- Niestandardowe modele ONNX do klasyfikacji dokumentów  

**Podejście do implementacji:**  
- Zaprojektuj modularną architekturę z wtyczkowymi komponentami AI  
- Zaimplementuj asynchroniczne przetwarzanie dla dużych partii dokumentów  
- Dodaj wskaźniki postępu i wsparcie anulowania dla operacji długotrwałych  
- Uwzględnij możliwość pracy offline dla przetwarzania wrażliwych dokumentów  

### Przykład 2: System zarządzania zapasami w handlu detalicznym  

Stwórz system zarządzania zapasami wspomagany AI dla aplikacji detalicznych:  

**Wykorzystane technologie:**  
- Segmentacja obrazów do identyfikacji produktów  
- Niestandardowe modele wizji do klasyfikacji marek i kategorii  
- Lokalna implementacja Foundry specjalistycznych modeli językowych dla handlu detalicznego  
- Integracja z istniejącymi systemami POS i zarządzania zapasami  

**Podejście do implementacji:**  
- Zbuduj integrację z kamerami do skanowania produktów w czasie rzeczywistym  
- Zaimplementuj rozpoznawanie kodów kreskowych i wizualne rozpoznawanie produktów  
- Dodaj naturalne zapytania dotyczące zapasów za pomocą lokalnych modeli językowych  
- Zaprojektuj skalowalną architekturę dla wdrożenia w wielu sklepach  

### Przykład 3: Asystent dokumentacji medycznej  

Opracuj narzędzie do dokumentacji medycznej z zachowaniem prywatności:  

**Wykorzystane technologie:**  
- Phi Silica do generowania notatek medycznych i wsparcia decyzji klinicznych  
- OCR do cyfryzacji ręcznie pisanych dokumentów medycznych  
- Niestandardowe modele językowe medyczne wdrożone za pomocą Windows ML  
- Lokalna pamięć wektorowa do wyszukiwania wiedzy medycznej  

**Podejście do implementacji:**  
- Zapewnij pełną pracę offline dla ochrony prywatności pacjentów  
- Zaimplementuj walidację i sugestie terminologii medycznej  
- Dodaj rejestrowanie audytowe dla zgodności regulacyjnej  
- Zaprojektuj integrację z istniejącymi systemami elektronicznej dokumentacji medycznej  

## Strategie optymalizacji wydajności  

### Rozwój uwzględniający sprzęt  

**Optymalizacja NPU**  
- Projektuj aplikacje wykorzystujące możliwości NPU na komputerach Copilot+  
- Zaimplementuj łagodne przejście na GPU/CPU na urządzeniach bez NPU  
- Optymalizuj formaty modeli dla przyspieszenia specyficznego dla NPU  
- Monitoruj wykorzystanie NPU i charakterystyki termiczne  

**Zarządzanie pamięcią**  
- Zaimplementuj efektywne strategie ładowania i buforowania modeli  
- Używaj mapowania pamięci dla dużych modeli, aby skrócić czas uruchamiania  
- Projektuj aplikacje świadome pamięci dla urządzeń o ograniczonych zasobach  
- Zaimplementuj kwantyzację modeli dla optymalizacji pamięci  

**Efektywność baterii**  
- Optymalizuj operacje AI dla minimalnego zużycia energii  
- Zaimplementuj adaptacyjne przetwarzanie w zależności od stanu baterii  
- Projektuj efektywne przetwarzanie w tle dla ciągłych operacji AI  
- Używaj narzędzi do profilowania energii, aby zoptymalizować zużycie energii  

### Rozważania dotyczące skalowalności  

**Wielowątkowość**  
- Projektuj operacje AI bezpieczne dla wątków do przetwarzania równoległego  
- Zaimplementuj efektywny podział pracy na dostępne rdzenie  
- Używaj wzorców async/await dla operacji AI bez blokowania  
- Planuj optymalizację puli wątków dla różnych konfiguracji sprzętowych  

**Strategie buforowania**  
- Zaimplementuj inteligentne buforowanie dla często używanych operacji AI  
- Projektuj strategie unieważniania bufora dla aktualizacji modeli  
- Używaj trwałego buforowania dla kosztownych operacji wstępnego przetwarzania  
- Zaimplementuj rozproszone buforowanie dla scenariuszy wieloużytkownikowych  

## Najlepsze praktyki dotyczące bezpieczeństwa i prywatności  

### Ochrona danych  

**Przetwarzanie lokalne**  
- Upewnij się, że wrażliwe dane nigdy nie opuszczają lokalnego urządzenia  
- Zaimplementuj bezpieczne przechowywanie modeli AI i danych tymczasowych  
- Używaj funkcji bezpieczeństwa Windows do izolacji aplikacji  
- Zastosuj szyfrowanie dla przechowywanych modeli i wyników pośrednich  

**Bezpieczeństwo modeli**  
- Waliduj integralność modeli przed ich załadowaniem i wykonaniem  
- Zaimplementuj bezpieczne mechanizmy aktualizacji modeli  
- Używaj podpisanych modeli, aby zapobiec manipulacjom  
- Zastosuj kontrolę dostępu do plików modeli i konfiguracji  

### Rozważania dotyczące zgodności  

**Dostosowanie do regulacji**  
- Projektuj aplikacje zgodne z GDPR, HIPAA i innymi wymaganiami regulacyjnymi  
- Zaimplementuj rejestrowanie audytowe dla procesów decyzyjnych AI  
- Zapewnij funkcje przejrzystości dla wyników generowanych przez AI  
- Umożliwiaj użytkownikom kontrolę nad przetwarzaniem danych przez AI  

**Bezpieczeństwo przedsiębiorstwa**  
- Integracja z politykami bezpieczeństwa przedsiębiorstwa Windows  
- Obsługa zarządzanego wdrożenia za pomocą narzędzi zarządzania przedsiębiorstwem  
- Zaimplementuj kontrolę dostępu opartą na rolach dla funkcji AI  
- Zapewnij kontrolę administracyjną dla funkcjonalności AI  

## Rozwiązywanie problemów i debugowanie  

### Typowe wyzwania deweloperskie  

**Problemy z konfiguracją budowy**  
- Upewnij się, że konfiguracja platformy ARM64 jest ustawiona dla próbek API Windows AI  
- Zweryfikuj kompatybilność wersji Windows App SDK (wymagana 1.8.1+)  
- Sprawdź, czy tożsamość pakietu jest poprawnie skonfigurowana (wymagana dla API Windows AI)  
- Zweryfikuj, czy narzędzia budowy obsługują docelową wersję frameworka  

**Problemy z ładowaniem modeli**  
- Zweryfikuj kompatybilność modeli ONNX z Windows ML  
- Sprawdź integralność plików modeli i wymagania dotyczące formatu  
- Zweryfikuj wymagania sprzętowe dla konkretnych modeli  
- Debuguj problemy z alokacją pamięci podczas ładowania modeli  
- Upewnij się, że rejestracja dostawcy wykonania dla przyspieszenia sprzętowego jest poprawna  

**Rozważania dotyczące trybu wdrożenia**  
- **Tryb samodzielny**: W pełni obsługiwany, większy rozmiar wdrożenia  
- **Tryb zależny od frameworka**: Mniejszy rozmiar, wymaga współdzielonego runtime  
- **Aplikacje niepakowane**: Nie są już obsługiwane dla API Windows AI  
- Użyj `dotnet run -p:Platform=ARM64 -p:SelfContained=true` dla samodzielnego wdrożenia ARM64  

**Problemy z wydajnością**  
- Profiluj wydajność aplikacji na różnych konfiguracjach sprzętowych  
- Identyfikuj wąskie gardła w pipeline'ach przetwarzania AI  
- Optymalizuj operacje wstępnego i końcowego przetwarzania danych  
- Zaimplementuj monitorowanie wydajności i alerty  

**Trudności z integracją**  
- Debuguj problemy z integracją API z odpowiednią obsługą błędów  
- Waliduj formaty danych wejściowych i wymagania dotyczące wstępnego przetwarzania  
- Testuj przypadki brzegowe i warunki błędów dokładnie  
- Zaimplementuj kompleksowe logowanie dla debugowania problemów produkcyjnych  

### Narzędzia i techniki debugowania  

**Integracja z Visual Studio**  
- Używaj debugera AI Toolkit do analizy wykonania modeli  
- Zaimplementuj profilowanie wydajności dla operacji AI  
- Debuguj asynchroniczne operacje AI z odpowiednią obsługą wyjątków  
- Używaj narzędzi do profilowania pamięci dla optymalizacji  

**Narzędzia Windows AI Foundry**  
- Wykorzystaj CLI Foundry Local do testowania i walidacji modeli  
- Używaj narzędzi testowych API Windows AI do weryfikacji integracji  
- Zaimplementuj niestandardowe logowanie dla monitorowania operacji AI  
- Twórz testy automatyczne dla niezawodności funkcjonalności AI  

## Przyszłościowe podejście do aplikacji  

### Nowe technologie  

**Sprzęt nowej generacji**  
- Projektuj aplikacje wykorzystujące przyszłe możliwości NPU  
- Planuj dla większych rozmiarów modeli i ich złożoności  
- Zaimplementuj adaptacyjne architektury dla rozwijającego się sprzętu  
- Rozważ algorytmy gotowe na kwantową kompatybilność  

**Zaawansowane możliwości AI**  
- Przygotuj się na integrację multimodalną AI dla większej liczby typów danych  
- Planuj dla współpracy w czasie rzeczywistym AI między wieloma urządzeniami  
- Projektuj dla możliwości uczenia federacyjnego  
- Rozważ hybrydowe architektury inteligencji edge-cloud  

### Ciągłe uczenie się i adaptacja  

**Aktualizacje modeli**  
- Za
- [Repozytorium przykładów Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Narzędzia programistyczne
- [AI Toolkit dla Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galeria dla deweloperów AI](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Przykłady Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Narzędzia do konwersji modeli](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Pomoc techniczna
- [Dokumentacja Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentacja ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentacja Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Zgłaszanie problemów - Przykłady Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Społeczność i wsparcie
- [Społeczność deweloperów Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Szkolenia AI na Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ten przewodnik został zaprojektowany tak, aby ewoluować wraz z szybko rozwijającym się ekosystemem Windows AI. Regularne aktualizacje zapewniają zgodność z najnowszymi możliwościami platformy i najlepszymi praktykami programistycznymi.*

[08. Praktyczne ćwiczenia z Microsoft Foundry Local - Kompletny zestaw narzędzi dla deweloperów](../Module08/README.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.