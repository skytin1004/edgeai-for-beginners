<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T21:23:08+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "pl"
}
-->
# Dziennik zmian

Wszystkie istotne zmiany w EdgeAI for Beginners są tutaj dokumentowane. Projekt korzysta z wpisów opartych na datach oraz stylu Keep a Changelog (Dodano, Zmieniono, Naprawiono, Usunięto, Dokumentacja, Przeniesiono).

## 2025-10-08

### Dodano - Kompleksowa aktualizacja warsztatów
- **Całkowite przepisanie pliku README.md warsztatów**:
  - Dodano szczegółowe wprowadzenie wyjaśniające wartość Edge AI (prywatność, wydajność, koszty)
  - Stworzono 6 głównych celów edukacyjnych z opisanymi kompetencjami
  - Dodano tabelę wyników nauki z dostarczonymi materiałami i matrycą kompetencji
  - Uwzględniono sekcję umiejętności zawodowych dla zwiększenia znaczenia w przemyśle
  - Dodano przewodnik szybkiego startu z wymaganiami wstępnymi i 3-etapową konfiguracją
  - Stworzono tabele zasobów dla przykładów w Pythonie (8 plików z czasami uruchomienia)
  - Dodano tabelę notatników Jupyter (8 notatników z oceną trudności)
  - Stworzono tabelę dokumentacji (7 kluczowych dokumentów z poradami „Kiedy używać”)
  - Dodano rekomendacje ścieżek nauki dla różnych poziomów zaawansowania

- **Infrastruktura walidacji i testowania warsztatów**:
  - Stworzono `scripts/validate_samples.py` - kompleksowe narzędzie do walidacji składni, importów i dobrych praktyk
  - Stworzono `scripts/test_samples.py` - narzędzie do testów wstępnych dla wszystkich przykładów w Pythonie
  - Dodano dokumentację walidacji do `scripts/README.md`

- **Kompleksowa dokumentacja**:
  - Stworzono `SAMPLES_UPDATE_SUMMARY.md` - szczegółowy przewodnik (ponad 400 linii) opisujący wszystkie ulepszenia
  - Stworzono `UPDATE_COMPLETE.md` - podsumowanie wykonania aktualizacji
  - Stworzono `QUICK_REFERENCE.md` - karta szybkiego odniesienia dla warsztatów

### Zmieniono - Modernizacja przykładów w Pythonie w warsztatach
- **Zaktualizowano wszystkie 8 przykładów w Pythonie zgodnie z najlepszymi praktykami**:
  - Ulepszono obsługę błędów za pomocą bloków try-except wokół wszystkich operacji I/O
  - Dodano wskazówki typów i szczegółowe docstringi
  - Wprowadzono spójny wzorzec logowania [INFO]/[ERROR]/[RESULT]
  - Zabezpieczono opcjonalne importy z podpowiedziami dotyczącymi instalacji
  - Poprawiono komunikację z użytkownikiem we wszystkich przykładach

- **session01/chat_bootstrap.py**:
  - Ulepszono inicjalizację klienta z bardziej szczegółowymi komunikatami o błędach
  - Poprawiono obsługę błędów strumieniowych poprzez walidację fragmentów
  - Dodano lepszą obsługę wyjątków w przypadku niedostępności usługi

- **session02/rag_pipeline.py**:
  - Dodano zabezpieczenia importów dla sentence-transformers z podpowiedziami dotyczącymi instalacji
  - Ulepszono obsługę błędów dla operacji osadzania i generowania
  - Poprawiono formatowanie wyników za pomocą strukturalnych rezultatów

- **session02/rag_eval_ragas.py**:
  - Zabezpieczono opcjonalne importy (ragas, datasets) z przyjaznymi komunikatami o błędach
  - Dodano obsługę błędów dla metryk ewaluacyjnych
  - Ulepszono formatowanie wyników ewaluacji

- **session03/benchmark_oss_models.py**:
  - Wprowadzono łagodne degradacje (kontynuacja w przypadku awarii modelu)
  - Dodano szczegółowe raportowanie postępu i obsługę błędów dla każdego modelu
  - Ulepszono obliczenia statystyk z kompleksowym odzyskiwaniem błędów

- **session04/model_compare.py**:
  - Dodano wskazówki typów (zwracane typy Tuple)
  - Ulepszono formatowanie wyników za pomocą strukturalnych wyników JSON
  - Wprowadzono obsługę błędów dla każdego modelu z odzyskiwaniem

- **session05/agents_orchestrator.py**:
  - Ulepszono Agent.act() za pomocą szczegółowych docstringów
  - Dodano obsługę błędów w potokach z logowaniem etapowym
  - Poprawiono zarządzanie pamięcią i śledzenie stanu

- **session06/models_router.py**:
  - Ulepszono dokumentację funkcji dla wszystkich komponentów routingu
  - Dodano szczegółowe logowanie w funkcji route()
  - Poprawiono wyniki testów za pomocą strukturalnych rezultatów

- **session06/models_pipeline.py**:
  - Dodano obsługę błędów do funkcji pomocniczej chat()
  - Ulepszono pipeline() za pomocą logowania etapowego i raportowania postępu
  - Poprawiono main() za pomocą kompleksowego odzyskiwania błędów

### Dokumentacja - Ulepszenie dokumentacji warsztatów
- Zaktualizowano główny README.md, dodając sekcję warsztatów podkreślającą ścieżkę nauki praktycznej
- Ulepszono STUDY_GUIDE.md, dodając szczegółową sekcję warsztatów, w tym:
  - Cele nauki i obszary koncentracji
  - Pytania do samooceny
  - Ćwiczenia praktyczne z szacunkowym czasem wykonania
  - Przydział czasu dla nauki intensywnej i w niepełnym wymiarze godzin
  - Dodano warsztaty do szablonu śledzenia postępów
- Zaktualizowano przewodnik przydziału czasu z 20 godzin do 30 godzin (w tym warsztaty)
- Dodano opisy przykładów warsztatowych i wyniki nauki do README

### Naprawiono
- Rozwiązano niespójności w obsłudze błędów w przykładach warsztatowych
- Naprawiono błędy importu opcjonalnych zależności za pomocą odpowiednich zabezpieczeń
- Skorygowano brakujące wskazówki typów w kluczowych funkcjach
- Rozwiązano problem z niewystarczającą komunikacją z użytkownikiem w scenariuszach błędów
- Naprawiono problemy z walidacją za pomocą kompleksowej infrastruktury testowej

---

## 2025-09-23

### Zmieniono - Modernizacja głównego modułu 08
- **Kompleksowe dostosowanie do wzorców repozytorium Microsoft Foundry-Local**:
  - Zaktualizowano wszystkie przykłady kodu, aby korzystały z nowoczesnego `FoundryLocalManager` i integracji z OpenAI SDK
  - Zastąpiono przestarzałe ręczne wywołania `requests` odpowiednim użyciem SDK
  - Dostosowano wzorce implementacji do oficjalnej dokumentacji i przykładów Microsoftu

- **Modernizacja 05.AIPoweredAgents.md**:
  - Zaktualizowano orkiestrację wieloagentową, aby korzystała z nowoczesnych wzorców SDK
  - Ulepszono implementację koordynatora o zaawansowane funkcje (pętle zwrotne, monitorowanie wydajności)
  - Dodano kompleksową obsługę błędów i sprawdzanie kondycji usług
  - Zintegrowano odpowiednie odniesienia do lokalnych przykładów (`samples/05/multi_agent_orchestration.ipynb`)
  - Zaktualizowano przykłady wywołań funkcji, aby korzystały z nowoczesnego parametru `tools` zamiast przestarzałego `functions`
  - Dodano wzorce gotowe do produkcji z monitorowaniem i śledzeniem statystyk

- **Całkowite przepisanie 06.ModelsAsTools.md**:
  - Zastąpiono podstawowy rejestr narzędzi inteligentnym routerem modeli
  - Dodano wybór modelu oparty na słowach kluczowych dla różnych typów zadań (ogólne, rozumowanie, kod, kreatywność)
  - Zintegrowano konfigurację opartą na środowisku z elastycznym przypisaniem modeli
  - Ulepszono o kompleksowe monitorowanie kondycji usług i obsługę błędów
  - Dodano wzorce wdrożenia produkcyjnego z monitorowaniem żądań i śledzeniem wydajności
  - Dostosowano do lokalnej implementacji w `samples/06/router.py` i `samples/06/model_router.ipynb`

- **Ulepszenia struktury dokumentacji**:
  - Dodano sekcje przeglądowe podkreślające modernizację i integrację SDK
  - Ulepszono za pomocą emotikonów i lepszego formatowania dla poprawy czytelności
  - Dodano odpowiednie odniesienia do lokalnych plików z przykładami w całej dokumentacji
  - Uwzględniono wskazówki dotyczące implementacji gotowej do produkcji i najlepsze praktyki

### Dodano
- Kompleksowe sekcje przeglądowe w plikach modułu 08 podkreślające nowoczesną integrację SDK
- Najważniejsze elementy architektury prezentujące zaawansowane funkcje (systemy wieloagentowe, inteligentne routowanie)
- Bezpośrednie odniesienia do lokalnych implementacji przykładów dla praktycznego doświadczenia
- Wskazówki dotyczące wdrożenia produkcyjnego z monitorowaniem i wzorcami obsługi błędów
- Interaktywne przykłady w notatnikach Jupyter z zaawansowanymi funkcjami i benchmarkami

### Naprawiono
- Rozbieżności między dokumentacją a rzeczywistymi implementacjami przykładów
- Przestarzałe wzorce użycia SDK w całym module 08
- Brakujące odniesienia do kompleksowej lokalnej biblioteki przykładów
- Niespójne podejścia do implementacji w różnych sekcjach

---

## 2025-09-18

### Dodano
- Moduł 08: Microsoft Foundry Local – Kompletny zestaw narzędzi dla deweloperów
  - Sześć sesji: konfiguracja, integracja Azure AI Foundry, modele open-source, nowoczesne dema, agenci i modele jako narzędzia
  - Przykłady do uruchomienia w `Module08/samples/01`–`06` z instrukcjami dla Windows cmd
    - `01` REST szybki czat (`chat_quickstart.py`)
    - `02` SDK szybki start z OpenAI/Foundry Local i wsparciem Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista i benchmark (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkiestracja wieloagentowa (`python -m samples.05.agents.coordinator`)
    - `06` Router modeli jako narzędzi (`router.py`)
- Wsparcie Azure OpenAI w przykładzie SDK sesji 2 z konfiguracją zmiennych środowiskowych
- `.vscode/settings.json` wskazujące na `Module08/.venv` dla poprawy rozpoznawania analizy Pythona
- `.env` z podpowiedzią `PYTHONPATH` dla świadomości VS Code/Pylance

### Zmieniono
- Domyślny model zaktualizowany do `phi-4-mini` w całej dokumentacji i przykładach modułu 08; usunięto pozostałe wzmianki o `phi-3.5` w module 08
- Ulepszenia routera (`Module08/samples/06/router.py`):
  - Odkrywanie punktów końcowych za pomocą `foundry service status` z analizą regex
  - Sprawdzanie kondycji `/v1/models` przy uruchomieniu
  - Rejestr modeli konfigurowalny środowiskowo (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Zaktualizowano wymagania: `Module08/requirements.txt` teraz zawiera `openai` (obok `requests`, `chainlit`)
- Wyjaśniono wskazówki dotyczące przykładu Chainlit i dodano rozwiązywanie problemów; rozwiązywanie importów za pomocą ustawień obszaru roboczego

### Naprawiono
- Rozwiązano problemy z importem:
  - Router nie zależy już od nieistniejącego modułu `utils`; funkcje zostały wbudowane
  - Koordynator używa importu względnego (`from .specialists import ...`) i jest wywoływany za pomocą ścieżki modułu
  - Konfiguracja VS Code/Pylance do rozwiązywania importów `chainlit` i pakietów
- Skorygowano drobny błąd w `STUDY_GUIDE.md` i dodano pokrycie modułu 08

### Usunięto
- Usunięto nieużywany `Module08/infra/obs.py` i pusty katalog `infra/`; wzorce obserwowalności zachowane jako opcjonalne w dokumentacji

### Przeniesiono
- Skonsolidowano dema modułu 08 w `Module08/samples` z folderami ponumerowanymi według sesji
  - Przeniesiono aplikację Chainlit do `samples/04`
  - Przeniesiono agentów do `samples/05` i dodano pliki `__init__.py` dla rozwiązywania pakietów

### Dokumentacja
- Dokumenty sesji modułu 08 i wszystkie README przykładów wzbogacone o odniesienia do Microsoft Learn i zaufanych dostawców
- `Module08/README.md` zaktualizowano o przegląd przykładów, konfigurację routera i wskazówki dotyczące walidacji
- `Module07/README.md` sekcja Windows Foundry Local zweryfikowana względem dokumentacji Learn
- `STUDY_GUIDE.md` zaktualizowano:
  - Dodano moduł 08 do przeglądu, harmonogramów, śledzenia postępów
  - Dodano kompleksową sekcję Referencje (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historyczne (podsumowanie)
- Ustanowiono architekturę kursu i moduły (Moduły 01–07)
- Iteracyjna modernizacja treści, standaryzacja formatowania i dodanie studiów przypadków
- Rozszerzono zakres optymalizacji frameworków (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nieopublikowane / Backlog (propozycje)
- Opcjonalne testy wstępne dla każdego przykładu w celu walidacji dostępności Foundry Local
- Przegląd tłumaczeń w celu dostosowania odniesień do modeli (np. `phi-4-mini`) tam, gdzie to właściwe
- Dodanie minimalnej konfiguracji pyright, jeśli zespoły preferują ścisłość w całym obszarze roboczym

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.