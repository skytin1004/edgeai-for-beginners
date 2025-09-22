<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T13:31:14+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "pl"
}
-->
# Dziennik zmian

Wszystkie istotne zmiany w EdgeAI dla Początkujących są tutaj udokumentowane. Ten projekt korzysta z wpisów opartych na datach oraz stylu Keep a Changelog (Dodano, Zmieniono, Naprawiono, Usunięto, Dokumentacja, Przeniesiono).

## 2025-09-18

### Dodano
- Moduł 08: Microsoft Foundry Local – Kompletny zestaw narzędzi dla programistów
  - Sześć sesji: konfiguracja, integracja z Azure AI Foundry, modele open-source, najnowsze demonstracje, agenci i modele jako narzędzia
  - Przykłady do uruchomienia w `Module08/samples/01`–`06` z instrukcjami dla Windows cmd
    - `01` REST szybka rozmowa (`chat_quickstart.py`)
    - `02` SDK szybki start z OpenAI/Foundry Local i wsparciem Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista i test (`list_and_bench.cmd`)
    - `04` Demonstracja Chainlit (`app.py`)
    - `05` Orkiestracja wieloagentowa (`python -m samples.05.agents.coordinator`)
    - `06` Router modeli jako narzędzi (`router.py`)
- Wsparcie Azure OpenAI w próbce SDK z Sesji 2 z konfiguracją zmiennych środowiskowych
- `.vscode/settings.json` wskazujące na `Module08/.venv` w celu poprawy rozpoznawania analizy Python
- `.env` z podpowiedzią `PYTHONPATH` dla świadomości VS Code/Pylance

### Zmieniono
- Domyślny model zaktualizowany do `phi-4-mini` w dokumentacji i przykładach Modułu 08; usunięto pozostałe odniesienia do `phi-3.5` w obrębie Modułu 08
- Ulepszenia routera (`Module08/samples/06/router.py`):
  - Odkrywanie punktów końcowych za pomocą `foundry service status` z analizą regex
  - Sprawdzanie zdrowia `/v1/models` podczas uruchamiania
  - Rejestr modeli konfigurowalny przez środowisko (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Zaktualizowane wymagania: `Module08/requirements.txt` teraz zawiera `openai` (obok `requests`, `chainlit`)
- Wyjaśnione wskazówki dotyczące próbki Chainlit i dodano rozwiązywanie problemów; rozwiązywanie importów za pomocą ustawień przestrzeni roboczej

### Naprawiono
- Rozwiązano problemy z importem:
  - Router nie zależy już od nieistniejącego modułu `utils`; funkcje zostały wbudowane
  - Koordynator używa importu względnego (`from .specialists import ...`) i jest wywoływany przez ścieżkę modułu
  - Konfiguracja VS Code/Pylance do rozwiązywania importów `chainlit` i pakietów
- Poprawiono drobną literówkę w `STUDY_GUIDE.md` i dodano pokrycie Modułu 08

### Usunięto
- Usunięto nieużywany `Module08/infra/obs.py` i pusty katalog `infra/`; wzorce obserwowalności zachowane jako opcjonalne w dokumentacji

### Przeniesiono
- Skonsolidowano demonstracje Modułu 08 w `Module08/samples` z folderami numerowanymi według sesji
  - Przeniesiono aplikację Chainlit do `samples/04`
  - Przeniesiono agentów do `samples/05` i dodano pliki `__init__.py` dla rozwiązywania pakietów

### Dokumentacja
- Dokumentacja sesji Modułu 08 i wszystkie pliki README dla próbek wzbogacone o odniesienia do Microsoft Learn i zaufanych dostawców
- Zaktualizowano `Module08/README.md` o Przegląd Próbek, konfigurację routera i wskazówki dotyczące walidacji
- Zaktualizowano sekcję Windows Foundry Local w `Module07/README.md` zgodnie z dokumentacją Learn
- Zaktualizowano `STUDY_GUIDE.md`:
  - Dodano Moduł 08 do przeglądu, harmonogramów, śledzenia postępów
  - Dodano kompleksową sekcję Odniesienia (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historyczne (podsumowanie)
- Ustanowiono architekturę kursu i moduły (Moduły 01–07)
- Iteracyjna modernizacja treści, standaryzacja formatowania i dodanie studiów przypadków
- Rozszerzone pokrycie frameworków optymalizacyjnych (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nieopublikowane / Backlog (propozycje)
- Opcjonalne testy dymne dla każdej próbki w celu walidacji dostępności Foundry Local
- Przegląd tłumaczeń w celu dopasowania odniesień do modeli (np. `phi-4-mini`) tam, gdzie to właściwe
- Dodanie minimalnej konfiguracji pyright, jeśli zespoły preferują ścisłość w całej przestrzeni roboczej

---

