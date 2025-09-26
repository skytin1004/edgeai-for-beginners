<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bad055c54c7952c482113fd7fe1d43c1",
  "translation_date": "2025-09-26T18:37:05+00:00",
  "source_file": "Module08/README.md",
  "language_code": "pl"
}
-->
# Moduł 08: Praktyczne Zastosowanie Microsoft Foundry Local - Kompletny Zestaw Narzędzi dla Programistów

## Przegląd

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) to nowa generacja rozwoju AI na urządzeniach brzegowych, oferująca programistom potężne narzędzia do tworzenia, wdrażania i skalowania aplikacji AI lokalnie, przy jednoczesnym zachowaniu płynnej integracji z Azure AI Foundry. Ten moduł obejmuje kompleksowe zagadnienia związane z Foundry Local, od instalacji po zaawansowane tworzenie agentów.

**Kluczowe Technologie:**
- Microsoft Foundry Local CLI i SDK
- Integracja z Azure AI Foundry
- Wnioskowanie modeli na urządzeniu
- Lokalna pamięć podręczna i optymalizacja modeli
- Architektury oparte na agentach

## Cele Nauki

Po ukończeniu tego modułu będziesz w stanie:

- **Opanować Foundry Local**: Zainstalować, skonfigurować i zoptymalizować środowisko dla Windows 11
- **Wdrażać Różnorodne Modele**: Uruchamiać lokalnie modele phi, qwen, deepseek i GPT za pomocą poleceń CLI
- **Tworzyć Rozwiązania Produkcyjne**: Budować aplikacje AI z zaawansowaną inżynierią promptów i integracją danych
- **Wykorzystywać Ekosystem Open-Source**: Integracja modeli Hugging Face i wkład społeczności
- **Tworzyć Agentów AI**: Budować inteligentnych agentów z funkcjami uziemienia i orkiestracji
- **Wdrażać Wzorce Korporacyjne**: Tworzyć modułowe, skalowalne rozwiązania AI do wdrożeń produkcyjnych

## Struktura Sesji

### [1: Pierwsze Kroki z Foundry Local](./01.FoundryLocalSetup.md)
**Temat**: Instalacja, konfiguracja CLI, wdrażanie modeli i optymalizacja sprzętu

**Kluczowe Tematy**: Kompleksowa instalacja • Polecenia CLI • Pamięć podręczna modeli • Przyspieszenie sprzętowe • Wdrażanie wielu modeli

**Przykłady**: [REST Chat Quickstart](./samples/01/README.md) • [Integracja OpenAI SDK](./samples/02/README.md) • [Odkrywanie i Benchmarking Modeli](./samples/03/README.md)

**Czas trwania**: 2-3 godziny | **Poziom**: Początkujący

---

### [2: Tworzenie Rozwiązań AI z Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Temat**: Zaawansowana inżynieria promptów, integracja danych i łączność z chmurą

**Kluczowe Tematy**: Inżynieria promptów • Integracja danych • Przepływy pracy Azure • Optymalizacja wydajności • Monitorowanie

**Przykład**: [Aplikacja Chainlit RAG](./samples/04/README.md)

**Czas trwania**: 2-3 godziny | **Poziom**: Średniozaawansowany

---

### [3: Modele Open-Source w Foundry Local](./03.OpenSourceModels.md)
**Temat**: Integracja Hugging Face, strategie BYOM i modele społecznościowe

**Kluczowe Tematy**: Integracja Hugging Face • Bring-your-own-model • Wgląd w Model Mondays • Wkład społeczności • Wybór modeli

**Przykład**: [Orkiestracja Wieloagentowa](./samples/05/README.md)

**Czas trwania**: 2-3 godziny | **Poziom**: Średniozaawansowany

---

### [4: Eksploracja Najnowocześniejszych Modeli](./04.CuttingEdgeModels.md)
**Temat**: Porównanie LLM vs SLM, implementacja EdgeAI i zaawansowane demonstracje

**Kluczowe Tematy**: Porównanie modeli • Wnioskowanie na urządzeniu vs w chmurze • Phi + ONNX Runtime • Aplikacja Chainlit RAG • Optymalizacja WebGPU

**Przykład**: [Router Models-as-Tools](./samples/06/README.md)

**Czas trwania**: 3-4 godziny | **Poziom**: Zaawansowany

---

### [5: Szybkie Tworzenie Agentów AI](./05.AIPoweredAgents.md)
**Temat**: Architektury agentów, systemowe prompty, uziemienie i orkiestracja

**Kluczowe Tematy**: Wzorce projektowania agentów • Inżynieria systemowych promptów • Techniki uziemienia • Systemy wieloagentowe • Wdrożenie produkcyjne

**Przykłady**: [Orkiestracja Wieloagentowa](./samples/05/README.md) • [Zaawansowany System Wieloagentowy](./samples/09/README.md)

**Czas trwania**: 3-4 godziny | **Poziom**: Zaawansowany

---

### [6: Foundry Local - Modele jako Narzędzia](./06.ModelsAsTools.md)
**Temat**: Modułowe rozwiązania AI, skalowanie korporacyjne i wzorce produkcyjne

**Kluczowe Tematy**: Modele jako narzędzia • Wdrażanie na urządzeniu • Integracja SDK/API • Architektury korporacyjne • Strategie skalowania

**Przykłady**: [Router Models-as-Tools](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Czas trwania**: 3-4 godziny | **Poziom**: Ekspert

---

### [7: Wzorce Integracji API Bezpośredniego](./samples/07/README.md)
**Temat**: Integracja REST API bez zależności od SDK dla maksymalnej kontroli

**Kluczowe Tematy**: Implementacja klienta HTTP • Niestandardowe uwierzytelnianie • Monitorowanie zdrowia modeli • Strumieniowanie odpowiedzi • Obsługa błędów produkcyjnych

**Przykład**: [Bezpośredni Klient API](./samples/07/README.md)

**Czas trwania**: 2-3 godziny | **Poziom**: Średniozaawansowany

---

### [8: Natywna Aplikacja Chatowa dla Windows 11](./samples/08/README.md)
**Temat**: Tworzenie nowoczesnych natywnych aplikacji chatowych z integracją Foundry Local

**Kluczowe Tematy**: Rozwój Electron • Fluent Design System • Natywna integracja z Windows • Strumieniowanie w czasie rzeczywistym • Projektowanie interfejsu chatowego

**Przykład**: [Aplikacja Chatowa dla Windows 11](./samples/08/README.md)

**Czas trwania**: 3-4 godziny | **Poziom**: Zaawansowany

---

### [9: Zaawansowana Orkiestracja Wieloagentowa](./samples/09/README.md)
**Temat**: Zaawansowana koordynacja agentów, delegowanie zadań i współpraca AI

**Kluczowe Tematy**: Inteligentna koordynacja agentów • Wzorce wywoływania funkcji • Komunikacja między agentami • Orkiestracja przepływów pracy • Mechanizmy zapewnienia jakości

**Przykład**: [Zaawansowany System Wieloagentowy](./samples/09/README.md)

**Czas trwania**: 4-5 godzin | **Poziom**: Ekspert

---

### [10: Foundry Local jako Framework Narzędziowy](./samples/10/README.md)
**Temat**: Architektura oparta na narzędziach do integracji Foundry Local z istniejącymi aplikacjami i frameworkami

**Kluczowe Tematy**: Integracja LangChain • Funkcje Semantic Kernel • Frameworki REST API • Narzędzia CLI • Integracja Jupyter • Wzorce wdrożenia produkcyjnego

**Przykład**: [Foundry Tools Framework](./samples/10/README.md)

**Czas trwania**: 4-5 godzin | **Poziom**: Ekspert

## Wymagania Wstępne

### Wymagania Systemowe
- **System Operacyjny**: Windows 11 (22H2 lub nowszy)
- **Pamięć**: 16GB RAM (32GB zalecane dla większych modeli)
- **Przestrzeń Dyskowa**: 50GB wolnego miejsca na pamięć podręczną modeli
- **Sprzęt**: Urządzenie z obsługą NPU (zalecane Copilot+ PC), GPU opcjonalne
- **Sieć**: Szybki internet do początkowego pobierania modeli

### Środowisko Programistyczne
- Visual Studio Code z rozszerzeniem AI Toolkit
- Python 3.10+ i pip
- Git do kontroli wersji
- PowerShell lub Command Prompt
- Azure CLI (opcjonalnie dla integracji z chmurą)

### Wymagana Wiedza
- Podstawowa znajomość koncepcji AI/ML
- Znajomość pracy z wierszem poleceń
- Podstawy programowania w Pythonie
- Koncepcje REST API
- Podstawowa wiedza o promptach i wnioskowaniu modeli

## Harmonogram Modułu

**Całkowity Szacowany Czas**: 30-38 godzin

| Sesja | Obszar Tematyczny | Przykłady | Czas | Złożoność |
|-------|-------------------|-----------|------|-----------|
|  1 | Instalacja i Podstawy | 01, 02, 03 | 2-3 godziny | Początkujący |
|  2 | Rozwiązania AI | 04 | 2-3 godziny | Średniozaawansowany |
|  3 | Open Source | 05 | 2-3 godziny | Średniozaawansowany |
|  4 | Zaawansowane Modele | 06 | 3-4 godziny | Zaawansowany |
|  5 | Agenci AI | 05, 09 | 3-4 godziny | Zaawansowany |
|  6 | Narzędzia Korporacyjne | 06, 10 | 3-4 godziny | Ekspert |
|  7 | Integracja API | 07 | 2-3 godziny | Średniozaawansowany |
|  8 | Aplikacja Chatowa | 08 | 3-4 godziny | Zaawansowany |
|  9 | Wieloagentowa Orkiestracja | 09 | 4-5 godzin | Ekspert |
| 10 | Framework Narzędziowy | 10 | 4-5 godzin | Ekspert |

## Kluczowe Zasoby

**Oficjalna Dokumentacja:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Kod źródłowy i oficjalne przykłady
- [Dokumentacja Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Kompletny przewodnik instalacji i użytkowania
- [Seria Model Mondays](https://aka.ms/model-mondays) - Cotygodniowe prezentacje modeli i samouczki

**Społeczność i Wsparcie:**
- [Dyskusje Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Pytania i odpowiedzi społeczności oraz prośby o funkcje
- [Społeczność Programistów AI Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence) - Najnowsze wiadomości i najlepsze praktyki

## Wyniki Nauki

Po ukończeniu tego modułu będziesz w stanie:

### Techniczne Opanowanie
- **Wdrażać i Zarządzać**: Instalacje Foundry Local w środowiskach rozwojowych i produkcyjnych
- **Integracja Modeli**: Praca z różnorodnymi rodzinami modeli od Microsoft, Hugging Face i społeczności
- **Tworzenie Aplikacji**: Budowanie gotowych do produkcji aplikacji AI z zaawansowanymi funkcjami i optymalizacjami
- **Rozwój Agentów**: Implementacja zaawansowanych agentów AI z uziemieniem, rozumowaniem i integracją narzędzi

### Strategiczne Zrozumienie
- **Decyzje Architektoniczne**: Dokonywanie świadomych wyborów między wdrożeniem lokalnym a chmurowym
- **Optymalizacja Wydajności**: Optymalizacja wydajności wnioskowania na różnych konfiguracjach sprzętowych
- **Skalowanie Korporacyjne**: Projektowanie aplikacji skalowalnych od prototypów lokalnych do wdrożeń korporacyjnych
- **Prywatność i Bezpieczeństwo**: Implementacja rozwiązań AI chroniących prywatność z wnioskowaniem lokalnym

### Zdolności Innowacyjne
- **Szybkie Prototypowanie**: Szybkie tworzenie i testowanie koncepcji aplikacji AI w oparciu o wszystkie 10 wzorców
- **Integracja Społecznościowa**: Wykorzystanie modeli open-source i wkład w ekosystem
- **Zaawansowane Wzorce**: Implementacja najnowocześniejszych wzorców AI, w tym RAG, agentów i integracji narzędzi
- **Opanowanie Frameworków**: Ekspercka integracja z LangChain, Semantic Kernel, Chainlit i Electron
- **Wdrożenie Produkcyjne**: Wdrażanie skalowalnych rozwiązań AI od prototypów lokalnych do systemów korporacyjnych
- **Rozwój Gotowy na Przyszłość**: Tworzenie aplikacji gotowych na nowe technologie i wzorce AI

## Pierwsze Kroki

1. **Konfiguracja Środowiska**: Upewnij się, że masz Windows 11 z zalecanym sprzętem (patrz Wymagania Wstępne)
2. **Instalacja Foundry Local**: Postępuj zgodnie z Sesją 1, aby przeprowadzić pełną instalację i konfigurację
3. **Uruchom Przykład 01**: Rozpocznij od podstawowej integracji REST API, aby zweryfikować konfigurację
4. **Przejdź przez Przykłady**: Ukończ przykłady 01-10, aby zdobyć kompleksową wiedzę

## Metryki Sukcesu

Śledź swoje postępy przez wszystkie 10 kompleksowych przykładów:

### Poziom Podstawowy (Przykłady 01-03)
- [ ] Pomyślnie zainstaluj i skonfiguruj Foundry Local
- [ ] Ukończ integrację REST API (Przykład 01)
- [ ] Implementuj kompatybilność z OpenAI SDK (Przykład 02)
- [ ] Przeprowadź odkrywanie i benchmarking modeli (Przykład 03)

### Poziom Aplikacyjny (Przykłady 04-06)
- [ ] Wdróż i uruchom co najmniej 4 różne rodziny modeli
- [ ] Zbuduj funkcjonalną aplikację RAG chat (Przykład 04)
- [ ] Stwórz system orkiestracji wieloagentowej (Przykład 05)
- [ ] Implementuj inteligentne routowanie modeli (Przykład 06)

### Poziom Zaawansowanej Integracji (Przykłady 07-10)
- [ ] Zbuduj gotowego do produkcji klienta API (Przykład 07)
- [ ] Rozwiń natywną aplikację chatową dla Windows 11 (Przykład 08)
- [ ] Implementuj zaawansowany system wieloagentowy (Przykład 09)
- [ ] Stwórz kompleksowy framework narzędziowy (Przykład 10)

### Wskaźniki Opanowania
- [ ] Pomyślnie uruchom wszystkie 10 przykładów bez błędów
- [ ] Dostosuj co najmniej 3 przykłady do konkretnych przypadków użycia
- [ ] Wdróż 2+ przykłady w środowiskach produkcyjnych
- [ ] Wnieś ulepszenia lub rozszerzenia do kodu przykładowego
- [ ] Zintegruj wzorce Foundry Local w projektach osobistych/profesjonalnych

## Przewodnik Szybkiego Startu - Wszystkie 10 Przykładów

### Konfiguracja Środowiska (Wymagana dla Wszystkich Przykładów)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Podstawowe Przykłady (01-06)

**Przykład 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Przykład 02: Integracja OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Przykład 03: Odkrywanie i Benchmarking Modeli**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Przykład 04: Aplikacja Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Przykład 05: Orkiestracja Wieloagentowa**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Przykład 06: Router Models-as-Tools**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b-instruct

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Zaawansowane Przykłady (07-10)

**Przykład 07: Bezpośredni Klient API**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Przykład 08: Aplikacja Chatowa dla Windows 11**
@@CODE
Ten moduł reprezentuje najnowsze osiągnięcia w rozwoju AI na krawędzi, łącząc narzędzia klasy korporacyjnej Microsoftu z elastycznością i innowacyjnością ekosystemu open-source. Opanowując Foundry Local poprzez wszystkie 10 kompleksowych przykładów, znajdziesz się na czele rozwoju aplikacji AI.

**Kompletny plan nauki:**
- **Podstawy** (Przykłady 01-03): Integracja API i zarządzanie modelami
- **Aplikacje** (Przykłady 04-06): RAG, agenci i inteligentne kierowanie
- **Zaawansowane** (Przykłady 07-10): Ramy produkcyjne i integracja korporacyjna

W celu integracji z Azure OpenAI (Sesja 2), zapoznaj się z indywidualnymi plikami README dla poszczególnych przykładów, aby uzyskać informacje o wymaganych zmiennych środowiskowych i ustawieniach wersji API.

---

