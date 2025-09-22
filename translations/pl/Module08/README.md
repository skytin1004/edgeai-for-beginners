<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T13:32:19+00:00",
  "source_file": "Module08/README.md",
  "language_code": "pl"
}
-->
# Moduł 08: Praktyczne Zastosowanie Microsoft Foundry Local - Kompletny Zestaw Narzędzi dla Programistów

## Przegląd

Microsoft Foundry Local to nowa generacja rozwoju AI na urządzeniach brzegowych, oferująca programistom potężne narzędzia do tworzenia, wdrażania i skalowania aplikacji AI lokalnie, przy jednoczesnym zachowaniu płynnej integracji z Azure AI Foundry. Ten moduł obejmuje Foundry Local od instalacji po zaawansowane tworzenie agentów.

**Kluczowe technologie:**
- Microsoft Foundry Local CLI i SDK
- Integracja z Azure AI Foundry
- Wnioskowanie modeli na urządzeniu
- Lokalna pamięć podręczna modeli i ich optymalizacja
- Architektury oparte na agentach

## Cele nauki modułu

Po ukończeniu tego modułu będziesz w stanie:

- **Opanować konfigurację Foundry Local**: Zainstalować, skonfigurować i zoptymalizować Foundry Local dla rozwoju na Windows 11
- **Wdrażać różnorodne modele**: Uruchamiać lokalnie modele phi, qwen, deepseek i GPT-OSS-20B za pomocą poleceń CLI
- **Tworzyć rozwiązania produkcyjne**: Budować aplikacje AI z zaawansowaną inżynierią promptów i integracją danych
- **Wykorzystywać ekosystem open-source**: Integracja modeli Hugging Face i dodatków społecznościowych
- **Porównywać architektury AI**: Zrozumieć kompromisy między LLM a SLM oraz strategie wdrażania
- **Tworzyć agentów AI**: Budować inteligentnych agentów korzystając z architektury Foundry Local i technik ugruntowania
- **Implementować modele jako narzędzia**: Tworzyć modułowe, dostosowywalne rozwiązania AI dla aplikacji korporacyjnych

## Struktura sesji

### [1: Pierwsze kroki z Foundry Local](./01.FoundryLocalSetup.md)
**Temat**: Instalacja, konfiguracja CLI, pamięć podręczna modeli i akceleracja sprzętowa

**Czego się nauczysz:**
- Kompletną instalację Foundry Local na Windows 11
- Konfigurację CLI i strukturę poleceń
- Strategie pamięci podręcznej modeli dla optymalnej wydajności
- Konfigurację i optymalizację akceleracji sprzętowej
- Praktyczne wdrażanie modeli phi, qwen, deepseek i GPT-OSS-20B

**Czas trwania**: 2-3 godziny  
**Wymagania wstępne**: Windows 11, podstawowa znajomość wiersza poleceń

---

### [2: Tworzenie rozwiązań AI z Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Temat**: Zaawansowana inżynieria promptów, integracja danych i zadania do wykonania

**Czego się nauczysz:**
- Zaawansowane techniki inżynierii promptów
- Wzorce integracji danych i najlepsze praktyki
- Tworzenie zadań AI z Foundry Local
- Płynne przepływy pracy integracji z Azure AI Foundry
- Optymalizacja wydajności i monitorowanie

**Czas trwania**: 2-3 godziny  
**Wymagania wstępne**: Ukończenie sesji 1, konto Azure (opcjonalne)

---

### [3: Modele open-source w Foundry Local](./03.OpenSourceModels.md)
**Temat**: Integracja Hugging Face, strategie wyboru modeli i dodatki społecznościowe

**Czego się nauczysz:**
- Integracja modeli Hugging Face z Foundry Local
- Strategie i implementacja BYOM (Bring-Your-Own-Model)
- Wgląd w serię Model Mondays i wkład społeczności
- Wdrażanie i optymalizacja modeli niestandardowych
- Kryteria oceny i wyboru modeli społecznościowych

**Czas trwania**: 2-3 godziny  
**Wymagania wstępne**: Ukończenie sesji 1-2, konto Hugging Face

---

### [4: Eksploracja najnowocześniejszych modeli - LLM, SLM i wnioskowanie na urządzeniu](./04.CuttingEdgeModels.md)
**Temat**: Porównanie modeli, EdgeAI z Phi i ONNX Runtime, zaawansowane demonstracje

**Czego się nauczysz:**
- Kompleksowe porównanie LLM i SLM oraz ich zastosowania
- Kompromisy między wnioskowaniem lokalnym a w chmurze oraz ramy decyzyjne
- Implementacja EdgeAI z Phi i ONNX Runtime
- Tworzenie i wdrażanie aplikacji Chainlit RAG Chat
- Techniki optymalizacji wnioskowania WebGPU
- Integracja i możliwości SDK AI PC

**Czas trwania**: 3-4 godziny  
**Wymagania wstępne**: Ukończenie sesji 1-3, zrozumienie koncepcji wnioskowania

---

### [5: Szybkie tworzenie agentów AI z Foundry Local](./05.AIPoweredAgents.md)
**Temat**: Szybki rozwój aplikacji GenAI, systemowe prompty, ugruntowanie i architektury agentów

**Czego się nauczysz:**
- Architektura agentów Foundry Local i wzorce projektowe
- Inżynieria promptów systemowych dla zachowań agentów
- Techniki ugruntowania dla wiarygodnych odpowiedzi agentów
- Przepływy pracy szybkiego rozwoju aplikacji GenAI
- Orkiestracja agentów i systemy wieloagentowe
- Strategie wdrażania produkcyjnego dla agentów AI

**Czas trwania**: 3-4 godziny  
**Wymagania wstępne**: Ukończenie sesji 1-4, podstawowa znajomość agentów AI

---

### [6: Foundry Local - Modele jako narzędzia](./06.ModelsAsTools.md)
**Temat**: Modułowe rozwiązania AI, wdrażanie na urządzeniu i skalowanie w przedsiębiorstwie

**Czego się nauczysz:**
- Traktowanie modeli AI jako modułowych, dostosowywalnych narzędzi
- Wdrażanie na urządzeniu bez zależności od chmury
- Wnioskowanie o niskim opóźnieniu, efektywne kosztowo i chroniące prywatność
- Wzorce integracji SDK, API i CLI
- Dostosowywanie modeli do konkretnych przypadków użycia
- Strategie skalowania od lokalnych prototypów do Azure AI Foundry
- Architektury aplikacji AI gotowe dla przedsiębiorstw

**Czas trwania**: 3-4 godziny  
**Wymagania wstępne**: Wszystkie poprzednie sesje, pomocne doświadczenie w rozwoju dla przedsiębiorstw

## Wymagania wstępne

### Wymagania systemowe
- **System operacyjny**: Windows 11 (22H2 lub nowszy)
- **Pamięć**: 16GB RAM (32GB zalecane dla większych modeli)
- **Miejsce na dysku**: 50GB wolnego miejsca na pamięć podręczną modeli
- **Sprzęt**: Zalecane urządzenie z NPU (Copilot+ PC), GPU opcjonalne
- **Sieć**: Szybki internet do początkowego pobierania modeli

### Środowisko programistyczne
- Visual Studio Code z rozszerzeniem AI Toolkit
- Python 3.10+ i pip
- Git do kontroli wersji
- PowerShell lub Wiersz poleceń
- Azure CLI (opcjonalne dla integracji z chmurą)

### Wymagana wiedza
- Podstawowe zrozumienie koncepcji AI/ML
- Znajomość wiersza poleceń
- Podstawy programowania w Pythonie
- Koncepcje REST API
- Podstawowa wiedza o promptach i wnioskowaniu modeli

## Harmonogram modułu

**Całkowity szacowany czas**: 15-20 godzin

| Sesja | Obszar tematyczny | Czas | Poziom trudności |
|-------|-------------------|------|------------------|
|  1 | Konfiguracja i podstawy | 2-3 godziny | Początkujący |
|  2 | Rozwiązania AI | 2-3 godziny | Średniozaawansowany |
|  3 | Open Source | 2-3 godziny | Średniozaawansowany |
|  4 | Zaawansowane modele | 3-4 godziny | Zaawansowany |
|  5 | Agenci AI | 3-4 godziny | Zaawansowany |
|  6 | Narzędzia dla przedsiębiorstw | 3-4 godziny | Ekspert |

## Kluczowe zasoby

### Dokumentacja podstawowa
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Dokumentacja Azure AI Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Seria Model Mondays](https://aka.ms/model-mondays)

### Zasoby społecznościowe
- [Dyskusje społeczności Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Przykłady Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Społeczność programistów Microsoft AI](https://techcommunity.microsoft.com/category/artificialintelligence)

## Wyniki nauki

Po ukończeniu tego modułu będziesz w stanie:

### Opanowanie techniczne
- **Wdrażać i zarządzać**: Instalacje Foundry Local w środowiskach rozwojowych i produkcyjnych
- **Integracja modeli**: Praca z różnorodnymi rodzinami modeli od Microsoft, Hugging Face i społeczności
- **Tworzenie aplikacji**: Budowanie gotowych do produkcji aplikacji AI z zaawansowanymi funkcjami i optymalizacjami
- **Rozwój agentów**: Implementacja zaawansowanych agentów AI z ugruntowaniem, rozumowaniem i integracją narzędzi

### Zrozumienie strategiczne
- **Decyzje architektoniczne**: Dokonywanie świadomych wyborów między wdrożeniem lokalnym a w chmurze
- **Optymalizacja wydajności**: Optymalizacja wydajności wnioskowania na różnych konfiguracjach sprzętowych
- **Skalowanie w przedsiębiorstwie**: Projektowanie aplikacji skalowalnych od lokalnych prototypów do wdrożeń korporacyjnych
- **Prywatność i bezpieczeństwo**: Implementacja rozwiązań AI chroniących prywatność z wnioskowaniem lokalnym

### Zdolności innowacyjne
- **Szybkie prototypowanie**: Szybkie tworzenie i testowanie koncepcji aplikacji AI
- **Integracja społecznościowa**: Wykorzystanie modeli open-source i wkład w ekosystem
- **Zaawansowane wzorce**: Implementacja najnowocześniejszych wzorców AI, w tym RAG, agentów i integracji narzędzi
- **Rozwój gotowy na przyszłość**: Tworzenie aplikacji gotowych na nowe technologie i wzorce AI

## Pierwsze kroki

1. **Przygotuj środowisko**: Upewnij się, że masz Windows 11 z zalecanymi specyfikacjami sprzętowymi
2. **Zainstaluj wymagania wstępne**: Skonfiguruj narzędzia programistyczne i zależności
3. **Rozpocznij od sesji 1**: Zacznij od instalacji Foundry Local i podstawowej konfiguracji
4. **Postępuj sekwencyjnie**: Ukończ sesje w kolejności dla optymalnego postępu nauki
5. **Ćwicz regularnie**: Zastosuj koncepcje w praktycznych ćwiczeniach i projektach

## Metryki sukcesu

Śledź swoje postępy w module:

- [ ] Pomyślnie zainstaluj i skonfiguruj Foundry Local
- [ ] Wdróż i uruchom co najmniej 4 różne rodziny modeli
- [ ] Zbuduj kompletne rozwiązanie AI z integracją danych
- [ ] Zintegruj co najmniej 2 modele open-source
- [ ] Stwórz funkcjonalną aplikację RAG chat
- [ ] Rozwiń i wdroż agenta AI
- [ ] Zaimplementuj architekturę modeli jako narzędzi

## Szybki start dla przykładów

### 1) Konfiguracja środowiska (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Uruchom lokalny model (nowe okno terminala)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Uruchom demo Chainlit (Sesja 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Uruchom koordynatora wieloagentowego (Sesja 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Jeśli pojawią się błędy połączenia, zweryfikuj Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Konfiguracja routera (Sesja 6)
Router wykonuje szybki test zdrowia i obsługuje konfigurację opartą na środowisku:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Ten moduł reprezentuje najnowocześniejsze podejście do rozwoju AI na urządzeniach brzegowych, łącząc narzędzia klasy korporacyjnej Microsoft z elastycznością i innowacyjnością ekosystemu open-source. Opanowując Foundry Local, znajdziesz się na czele rozwoju aplikacji AI.

Dla Azure OpenAI (Sesja 2), zobacz README przykładu, aby uzyskać wymagane zmienne środowiskowe i ustawienia wersji API.

## Przegląd przykładów

- `samples/01`: Szybki REST chat z Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integracja SDK OpenAI (`sdk_quickstart.py`).
- `samples/03`: Odkrywanie modeli + szybki test (`list_and_bench.cmd`).
- `samples/04`: Demo Chainlit RAG (`app.py`).
- `samples/05`: Orkiestracja wieloagentowa (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router modeli jako narzędzi (`python samples\06\router.py`).

---

