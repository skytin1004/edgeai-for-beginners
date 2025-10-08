<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-08T21:51:49+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "pl"
}
-->
# Sesja 3: Modele Open-Source w Foundry Local

## Streszczenie

Dowiedz się, jak wprowadzać modele Hugging Face i inne modele open-source do Foundry Local. Poznaj strategie wyboru, procesy współpracy z społecznością, metodologię porównywania wydajności oraz sposoby rozszerzania Foundry o rejestrację niestandardowych modeli. Ta sesja nawiązuje do cotygodniowych tematów eksploracyjnych "Modelowe Poniedziałki" i wyposaża Cię w umiejętności oceny i wdrażania modeli open-source lokalnie przed ich skalowaniem na platformie Azure.

## Cele nauki

Po zakończeniu sesji będziesz w stanie:

- **Odkrywać i oceniać**: Identyfikować potencjalne modele (mistral, gemma, qwen, deepseek) z uwzględnieniem kompromisów między jakością a zasobami.
- **Ładować i uruchamiać**: Korzystać z Foundry Local CLI do pobierania, buforowania i uruchamiania modeli społecznościowych.
- **Przeprowadzać benchmarki**: Stosować spójne heurystyki dla opóźnień, przepustowości tokenów i jakości.
- **Rozszerzać**: Rejestrować lub dostosowywać niestandardowe opakowania modeli zgodnie z wzorcami kompatybilnymi z SDK.
- **Porównywać**: Tworzyć uporządkowane porównania dla decyzji dotyczących wyboru SLM w porównaniu z modelami LLM średniej wielkości.

## Wymagania wstępne

- Ukończone sesje 1 i 2
- Środowisko Python z zainstalowanym `foundry-local-sdk`
- Co najmniej 15 GB wolnego miejsca na dysku na potrzeby buforowania modeli
- Opcjonalnie: Włączona akceleracja GPU/WebGPU (`foundry config list`)

### Szybki start w środowisku wieloplatformowym

Windows PowerShell:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
macOS / Linux:  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
Podczas przeprowadzania benchmarków z macOS na usłudze hostowanej na Windows, ustaw:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## Przebieg demonstracji (30 minut)

### 1. Ładowanie modeli Hugging Face za pomocą CLI (8 minut)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```
  

### 2. Uruchomienie i szybka analiza (5 minut)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  

### 3. Skrypt benchmarkowy (8 minut)

Utwórz plik `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```
  
Uruchom:

```powershell
python samples/03-oss-models/benchmark_models.py
```
  

### 4. Porównanie wydajności (5 minut)

Omów kompromisy: czas ładowania, zużycie pamięci (obserwuj Menedżera zadań / `nvidia-smi` / monitor zasobów systemu operacyjnego), jakość wyników w porównaniu z szybkością. Użyj skryptu benchmarkowego w Pythonie (Sesja 3) do pomiaru opóźnień i przepustowości; powtórz testy po włączeniu akceleracji GPU.

### 5. Projekt startowy (4 minuty)

Utwórz generator raportów porównawczych modeli (rozszerz skrypt benchmarkowy o eksport do formatu markdown).

## Projekt startowy: Rozszerz `03-huggingface-models`

Ulepsz istniejący przykład poprzez:

1. Dodanie agregacji wyników benchmarków + eksportu do CSV/Markdown.
2. Wdrożenie prostego systemu oceny jakościowej (zestaw par promptów + plik szkieletowy do ręcznego oznaczania).
3. Wprowadzenie konfiguracji JSON (`models.json`) dla listy modeli i zestawu promptów.

## Lista kontrolna walidacji

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
Wszystkie docelowe modele powinny się pojawić i odpowiedzieć na zapytanie testowe.

## Przykładowy scenariusz i mapowanie warsztatowe

| Skrypt warsztatowy | Scenariusz | Cel | Źródło promptów / danych |
|---------------------|------------|-----|--------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Zespół platformy brzegowej wybierający domyślny SLM dla wbudowanego narzędzia do podsumowywania | Opracowanie porównania opóźnień + p95 + tokenów/sekundę dla wybranych modeli | Wbudowana zmienna `PROMPT` + lista środowiskowa `BENCH_MODELS` |

### Narracja scenariusza

Zespół inżynierii produktu musi wybrać domyślny lekki model do podsumowywania dla funkcji offline do notatek ze spotkań. Przeprowadzają kontrolowane, deterministyczne testy porównawcze (temperature=0) na stałym zestawie promptów (patrz przykład poniżej) i zbierają metryki opóźnień i przepustowości z włączoną i wyłączoną akceleracją GPU.

### Przykładowy zestaw promptów w formacie JSON (rozszerzalny)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
Pętla dla każdego promptu na model, rejestracja opóźnienia dla każdego promptu w celu wyprowadzenia metryk rozkładu i wykrycia wartości odstających.

## Ramy wyboru modelu

| Wymiar | Metryka | Dlaczego to ważne |
|--------|---------|-------------------|
| Opóźnienie | średnia / p95 | Spójność doświadczenia użytkownika |
| Przepustowość | tokeny/sekundę | Skalowalność wsadowa i strumieniowa |
| Pamięć | rozmiar rezydentny | Dopasowanie do urządzenia i współbieżność |
| Jakość | prompty oceny | Przydatność do zadania |
| Ślad | buforowanie na dysku | Dystrybucja i aktualizacje |
| Licencja | zgodność użytkowania | Zgodność komercyjna |

## Rozszerzanie o niestandardowy model

Wzorzec na wysokim poziomie (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```
  
Zapoznaj się z oficjalnym repozytorium, aby uzyskać aktualne interfejsy adapterów:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  

## Rozwiązywanie problemów

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| OOM na mistral-7b | Niewystarczająca ilość RAM/GPU | Zatrzymaj inne modele; spróbuj mniejszy wariant |
| Wolna pierwsza odpowiedź | Zimne ładowanie | Utrzymuj w gotowości za pomocą okresowego lekkiego promptu |
| Zawieszenie pobierania | Niestabilność sieci | Spróbuj ponownie; pobierz w czasie poza szczytem |

## Źródła

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Modelowe Poniedziałki: https://aka.ms/model-mondays  
- Odkrywanie modeli Hugging Face: https://huggingface.co/models  

---

**Czas trwania sesji**: 30 minut (+ opcjonalne pogłębienie)  
**Poziom trudności**: Średniozaawansowany  

### Opcjonalne ulepszenia

| Ulepszenie | Korzyść | Jak |
|------------|---------|-----|
| Opóźnienie pierwszego tokena w strumieniu | Pomiar postrzeganej responsywności | Uruchom benchmark z `BENCH_STREAM=1` (ulepszony skrypt w `Workshop/samples/session03`) |
| Tryb deterministyczny | Stabilne porównania regresji | `temperature=0`, stały zestaw promptów, rejestracja wyników JSON pod kontrolą wersji |
| Ocena jakościowa | Dodaje wymiar jakościowy | Utrzymuj `prompts.json` z oczekiwanymi aspektami; oznaczaj wyniki (1–5) ręcznie lub za pomocą modelu pomocniczego |
| Eksport do CSV / Markdown | Udostępnianie raportów | Rozszerz skrypt, aby zapisywał `benchmark_report.md` z tabelą i podsumowaniem |
| Tagi zdolności modelu | Pomaga w automatycznym routingu | Utrzymuj `models.json` z `{alias: {capabilities:[], size_mb:..}}` |
| Faza rozgrzewki bufora | Redukcja wpływu zimnego startu | Wykonaj jedną rundę rozgrzewki przed pętlą czasową (już zaimplementowane) |
| Dokładność percentylowa | Solidne opóźnienia końcowe | Użyj percentyla numpy (już w zrefaktoryzowanym skrypcie) |
| Przybliżenie kosztu tokena | Porównanie ekonomiczne | Przybliżony koszt = (tokeny/sek * średnia liczba tokenów na żądanie) * heurystyka energii |
| Automatyczne pomijanie nieudanych modeli | Odporność w partiach | Owiń każdy benchmark w try/except i oznacz pole statusu |

#### Minimalny fragment eksportu do Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  

#### Przykład deterministycznego zestawu promptów

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
Pętla na statycznej liście zamiast losowych promptów dla porównywalnych metryk w różnych commitach.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.