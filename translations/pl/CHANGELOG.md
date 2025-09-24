<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T12:27:15+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "pl"
}
-->
# Dziennik zmian

Wszystkie istotne zmiany w EdgeAI dla Początkujących są tutaj udokumentowane. Ten projekt korzysta z wpisów opartych na datach oraz stylu Keep a Changelog (Dodano, Zmieniono, Naprawiono, Usunięto, Dokumentacja, Przeniesiono).

## 2025-09-23

### Zmieniono - Modernizacja Modułu 08
- **Kompleksowe dostosowanie do wzorców repozytorium Microsoft Foundry-Local**
  - Zaktualizowano wszystkie przykłady kodu, aby korzystały z nowoczesnego `FoundryLocalManager` oraz integracji OpenAI SDK
  - Zastąpiono przestarzałe ręczne wywołania `requests` odpowiednim użyciem SDK
  - Dostosowano wzorce implementacji do oficjalnej dokumentacji i przykładów Microsoftu

- **Modernizacja 05.AIPoweredAgents.md**:
  - Zaktualizowano orkiestrację wieloagentową, aby korzystała z nowoczesnych wzorców SDK
  - Ulepszono implementację koordynatora o zaawansowane funkcje (pętle zwrotne, monitorowanie wydajności)
  - Dodano kompleksowe obsługi błędów i sprawdzanie kondycji usług
  - Zintegrowano odpowiednie odniesienia do lokalnych przykładów (`samples/05/multi_agent_orchestration.ipynb`)
  - Zaktualizowano przykłady wywoływania funkcji, aby korzystały z nowoczesnego parametru `tools` zamiast przestarzałego `functions`
  - Dodano wzorce gotowe do produkcji z monitorowaniem i śledzeniem statystyk

- **Całkowite przepisanie 06.ModelsAsTools.md**:
  - Zastąpiono podstawowy rejestr narzędzi inteligentnym routerem modeli
  - Dodano wybór modeli oparty na słowach kluczowych dla różnych typów zadań (ogólne, rozumowanie, kod, kreatywne)
  - Zintegrowano konfigurację opartą na środowisku z elastycznym przypisaniem modeli
  - Ulepszono kompleksowym monitorowaniem kondycji usług i obsługą błędów
  - Dodano wzorce wdrożeniowe do produkcji z monitorowaniem żądań i śledzeniem wydajności
  - Dostosowano do lokalnej implementacji w `samples/06/router.py` i `samples/06/model_router.ipynb`

- **Ulepszenia struktury dokumentacji**:
  - Dodano sekcje przeglądowe podkreślające modernizację i dostosowanie do SDK
  - Ulepszono za pomocą emoji i lepszego formatowania dla poprawy czytelności
  - Dodano odpowiednie odniesienia do lokalnych plików z przykładami w całej dokumentacji
  - Uwzględniono wskazówki dotyczące implementacji gotowej do produkcji oraz najlepsze praktyki

### Dodano
- Kompleksowe sekcje przeglądowe w plikach Modułu 08 podkreślające integrację nowoczesnego SDK
- Najważniejsze elementy architektury prezentujące zaawansowane funkcje (systemy wieloagentowe, inteligentne routowanie)
- Bezpośrednie odniesienia do lokalnych implementacji przykładów dla praktycznego doświadczenia
- Wskazówki dotyczące wdrożenia produkcyjnego z wzorcami monitorowania i obsługi błędów
- Interaktywne przykłady w notatnikach Jupyter z zaawansowanymi funkcjami i benchmarkami

### Naprawiono
- Rozbieżności w dostosowaniu między dokumentacją a rzeczywistymi implementacjami przykładów
- Przestarzałe wzorce użycia SDK w całym Modułu 08
- Brakujące odniesienia do kompleksowej lokalnej biblioteki przykładów
- Niespójne podejścia do implementacji w różnych sekcjach

---

## 2025-09-18

### Dodano
- Moduł 08: Microsoft Foundry Local – Kompletny zestaw narzędzi dla deweloperów
  - Sześć sesji: konfiguracja, integracja Azure AI Foundry, modele open-source, nowoczesne demonstracje, agenci i modele jako narzędzia
  - Przykłady do uruchomienia w `Module08/samples/01`–`06` z instrukcjami dla Windows cmd
    - `01` REST szybka rozmowa (`chat_quickstart.py`)
    - `02` SDK szybki start z OpenAI/Foundry Local i wsparciem Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista i benchmark (`list_and_bench.cmd`)
    - `04` Demonstracja Chainlit (`app.py`)
    - `05` Orkiestracja wieloagentowa (`python -m samples.05.agents.coordinator`)
    - `06` Router modeli jako narzędzi (`router.py`)
- Wsparcie Azure OpenAI w próbce SDK Sesji 2 z konfiguracją zmiennych środowiskowych
- `.vscode/settings.json` wskazujące na `Module08/.venv` dla poprawy rozpoznawania analizy Python
- `.env` z podpowiedzią `PYTHONPATH` dla świadomości VS Code/Pylance

### Zmieniono
- Domyślny model zaktualizowany do `phi-4-mini` w całej dokumentacji i przykładach Modułu 08; usunięto pozostałe wzmianki o `phi-3.5` w Modułu 08
- Ulepszenia routera (`Module08/samples/06/router.py`):
  - Odkrywanie punktów końcowych za pomocą `foundry service status` z analizą regex
  - Sprawdzanie kondycji `/v1/models` podczas uruchamiania
  - Rejestr modeli konfigurowalny przez środowisko (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Zaktualizowano wymagania: `Module08/requirements.txt` teraz zawiera `openai` (obok `requests`, `chainlit`)
- Wyjaśniono wskazówki dotyczące próbki Chainlit i dodano rozwiązywanie problemów; rozpoznawanie importu przez ustawienia przestrzeni roboczej

### Naprawiono
- Rozwiązano problemy z importem:
  - Router nie zależy już od nieistniejącego modułu `utils`; funkcje są wbudowane
  - Koordynator używa importu względnego (`from .specialists import ...`) i jest wywoływany przez ścieżkę modułu
  - Konfiguracja VS Code/Pylance do rozpoznawania `chainlit` i importów pakietów
- Poprawiono drobną literówkę w `STUDY_GUIDE.md` i dodano pokrycie Modułu 08

### Usunięto
- Usunięto nieużywany `Module08/infra/obs.py` i pusty katalog `infra/`; wzorce obserwowalności zachowane jako opcjonalne w dokumentacji

### Przeniesiono
- Skonsolidowano demonstracje Modułu 08 w `Module08/samples` z folderami numerowanymi sesjami
  - Przeniesiono aplikację Chainlit do `samples/04`
  - Przeniesiono agentów do `samples/05` i dodano pliki `__init__.py` dla rozpoznawania pakietów

### Dokumentacja
- Dokumentacja sesji Modułu 08 i wszystkie README przykładów wzbogacone o odniesienia do Microsoft Learn i zaufanych dostawców
- Zaktualizowano `Module08/README.md` o Przegląd Przykładów, konfigurację routera i wskazówki dotyczące walidacji
- Zweryfikowano sekcję Windows Foundry Local w `Module07/README.md` w odniesieniu do dokumentacji Learn
- Zaktualizowano `STUDY_GUIDE.md`:
  - Dodano Moduł 08 do przeglądu, harmonogramów, śledzenia postępów
  - Dodano kompleksową sekcję Odniesienia (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historyczne (podsumowanie)
- Ustanowiono architekturę kursu i moduły (Moduły 01–07)
- Iteracyjna modernizacja treści, standaryzacja formatowania i dodanie studiów przypadków
- Rozszerzono pokrycie frameworków optymalizacyjnych (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Niewydane / Backlog (propozycje)
- Opcjonalne testy dymne dla każdego przykładu w celu walidacji dostępności Foundry Local
- Przegląd tłumaczeń w celu dostosowania odniesień do modeli (np. `phi-4-mini`) tam, gdzie to właściwe
- Dodanie minimalnej konfiguracji pyright, jeśli zespoły preferują ścisłość w całej przestrzeni roboczej

---

