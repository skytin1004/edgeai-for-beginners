<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-09T13:04:36+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "el"
}
-->
# Συνεδρία 3: Μοντέλα Ανοιχτού Κώδικα στο Foundry Local

## Περίληψη

Ανακαλύψτε πώς να ενσωματώσετε μοντέλα του Hugging Face και άλλα μοντέλα ανοιχτού κώδικα στο Foundry Local. Μάθετε στρατηγικές επιλογής, διαδικασίες συνεισφοράς στην κοινότητα, μεθοδολογία σύγκρισης απόδοσης και πώς να επεκτείνετε το Foundry με προσαρμοσμένες εγγραφές μοντέλων. Αυτή η συνεδρία συνδέεται με τα εβδομαδιαία θέματα εξερεύνησης "Model Mondays" και σας εξοπλίζει για να αξιολογήσετε και να λειτουργήσετε μοντέλα ανοιχτού κώδικα τοπικά πριν από την κλιμάκωση στο Azure.

## Στόχοι Μάθησης

Μέχρι το τέλος θα μπορείτε:

- **Ανακάλυψη & Αξιολόγηση**: Να εντοπίζετε υποψήφια μοντέλα (mistral, gemma, qwen, deepseek) χρησιμοποιώντας την ισορροπία ποιότητας και πόρων.
- **Φόρτωση & Εκτέλεση**: Να χρησιμοποιείτε το Foundry Local CLI για λήψη, προσωρινή αποθήκευση και εκκίνηση μοντέλων της κοινότητας.
- **Αξιολόγηση Απόδοσης**: Να εφαρμόζετε συνεπείς μετρήσεις καθυστέρησης, ρυθμού παραγωγής tokens και ποιότητας.
- **Επέκταση**: Να εγγράφετε ή να προσαρμόζετε ένα προσαρμοσμένο περιτύλιγμα μοντέλου σύμφωνα με τα πρότυπα συμβατά με το SDK.
- **Σύγκριση**: Να παράγετε δομημένες συγκρίσεις για αποφάσεις επιλογής SLM έναντι μεσαίου μεγέθους LLM.

## Προαπαιτούμενα

- Ολοκληρωμένες οι Συνεδρίες 1 & 2
- Περιβάλλον Python με εγκατεστημένο το `foundry-local-sdk`
- Τουλάχιστον 15GB ελεύθερου χώρου στο δίσκο για πολλαπλές προσωρινές αποθηκεύσεις μοντέλων
- Προαιρετικά: Ενεργοποιημένη επιτάχυνση GPU/WebGPU (`foundry config list`)

### Γρήγορη Εκκίνηση Περιβάλλοντος Πολλαπλών Πλατφορμών

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
  
Όταν εκτελείτε αξιολόγηση από macOS σε υπηρεσία υποδοχής Windows, ορίστε:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## Ροή Επίδειξης (30 λεπτά)

### 1. Φόρτωση Μοντέλων Hugging Face μέσω CLI (8 λεπτά)

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
  

### 2. Εκτέλεση & Γρήγορη Δοκιμή (5 λεπτά)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  

### 3. Σενάριο Αξιολόγησης Απόδοσης (8 λεπτά)

Δημιουργήστε το `samples/03-oss-models/benchmark_models.py`:  
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
  
Εκτελέστε:  
```powershell
python samples/03-oss-models/benchmark_models.py
```
  

### 4. Σύγκριση Απόδοσης (5 λεπτά)

Συζητήστε τις ισορροπίες: χρόνος φόρτωσης, αποτύπωμα μνήμης (παρατηρήστε το Task Manager / `nvidia-smi` / παρακολούθηση πόρων OS), ποιότητα εξόδου έναντι ταχύτητας. Χρησιμοποιήστε το σενάριο αξιολόγησης Python (Συνεδρία 3) για καθυστέρηση και ρυθμό παραγωγής; επαναλάβετε μετά την ενεργοποίηση της επιτάχυνσης GPU.

### 5. Έργο Εκκίνησης (4 λεπτά)

Δημιουργήστε έναν δημιουργό αναφορών σύγκρισης μοντέλων (επεκτείνετε το σενάριο αξιολόγησης με εξαγωγή σε markdown).

## Έργο Εκκίνησης: Επέκταση `03-huggingface-models`

Βελτιώστε το υπάρχον δείγμα με:

1. Προσθήκη συγκέντρωσης αξιολόγησης + εξαγωγή σε CSV/Markdown.
2. Εφαρμογή απλής ποιοτικής βαθμολόγησης (σετ ζευγών προτροπών + αρχείο χειροκίνητης σχολιασμού).
3. Εισαγωγή ενός JSON config (`models.json`) για λίστα μοντέλων και σετ προτροπών που μπορούν να προσαρμοστούν.

## Λίστα Ελέγχου Επικύρωσης

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
Όλα τα μοντέλα στόχοι πρέπει να εμφανίζονται και να ανταποκρίνονται σε ένα αίτημα συνομιλίας.

## Σενάριο Δείγματος & Χαρτογράφηση Εργαστηρίου

| Σενάριο Εργαστηρίου | Σενάριο | Στόχος | Πηγή Προτροπών / Δεδομένων |
|---------------------|---------|--------|---------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Ομάδα πλατφόρμας edge που επιλέγει το προεπιλεγμένο SLM για ενσωματωμένο εργαλείο περίληψης | Παραγωγή σύγκρισης καθυστέρησης + p95 + tokens/sec μεταξύ υποψήφιων μοντέλων | Ενσωματωμένη μεταβλητή `PROMPT` + λίστα περιβάλλοντος `BENCH_MODELS` |

### Αφήγηση Σεναρίου

Η ομάδα μηχανικών προϊόντων πρέπει να επιλέξει ένα προεπιλεγμένο ελαφρύ μοντέλο περίληψης για μια λειτουργία σημειώσεων συναντήσεων εκτός σύνδεσης. Εκτελούν ελεγχόμενες ντετερμινιστικές αξιολογήσεις (temperature=0) σε ένα σταθερό σετ προτροπών (δείτε το παράδειγμα παρακάτω) και συλλέγουν μετρήσεις καθυστέρησης και ρυθμού παραγωγής με και χωρίς επιτάχυνση GPU.

### Παράδειγμα JSON Σετ Προτροπών (επεκτάσιμο)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
Επαναλάβετε κάθε προτροπή ανά μοντέλο, καταγράψτε την καθυστέρηση ανά προτροπή για να εξάγετε μετρήσεις κατανομής και να εντοπίσετε ακραίες τιμές.

## Πλαίσιο Επιλογής Μοντέλου

| Διάσταση | Μετρική | Γιατί Είναι Σημαντική |
|----------|---------|-----------------------|
| Καθυστέρηση | μέσος όρος / p95 | Συνοχή εμπειρίας χρήστη |
| Ρυθμός Παραγωγής | tokens/sec | Κλιμακωσιμότητα παρτίδας & ροής |
| Μνήμη | μέγεθος κατοικίας | Συμβατότητα συσκευής & ταυτόχρονη χρήση |
| Ποιότητα | προτροπές αξιολόγησης | Καταλληλότητα για την εργασία |
| Αποτύπωμα | προσωρινή αποθήκευση δίσκου | Διανομή & ενημερώσεις |
| Άδεια | επιτρεπόμενη χρήση | Συμμόρφωση με εμπορική χρήση |

## Επέκταση Με Προσαρμοσμένο Μοντέλο

Υψηλού επιπέδου μοτίβο (ψευδοκώδικας):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```
  
Συμβουλευτείτε το επίσημο αποθετήριο για εξελισσόμενες διεπαφές προσαρμογέα:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  

## Αντιμετώπιση Προβλημάτων

| Πρόβλημα | Αιτία | Λύση |
|----------|-------|------|
| OOM στο mistral-7b | Ανεπαρκής RAM/GPU | Σταματήστε άλλα μοντέλα; δοκιμάστε μικρότερη παραλλαγή |
| Αργή πρώτη απόκριση | Ψυχρή φόρτωση | Διατηρήστε ζεστό με περιοδική ελαφριά προτροπή |
| Καθυστέρηση λήψης | Αστάθεια δικτύου | Επαναλάβετε; προφορτώστε κατά τις ώρες μη αιχμής |

## Αναφορές

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Model Mondays: https://aka.ms/model-mondays  
- Ανακάλυψη Μοντέλων Hugging Face: https://huggingface.co/models  

---

**Διάρκεια Συνεδρίας**: 30 λεπτά (+ προαιρετική εμβάθυνση)  
**Δυσκολία**: Μεσαία  

### Προαιρετικές Βελτιώσεις

| Βελτίωση | Όφελος | Πώς |
|----------|--------|-----|
| Καθυστέρηση Πρώτου Token Ροής | Μετρά αντιληπτή ανταπόκριση | Εκτελέστε αξιολόγηση με `BENCH_STREAM=1` (βελτιωμένο σενάριο στο `Workshop/samples/session03`) |
| Ντετερμινιστική Λειτουργία | Σταθερές συγκρίσεις παλινδρόμησης | `temperature=0`, σταθερό σετ προτροπών, καταγράψτε εξόδους JSON υπό έλεγχο έκδοσης |
| Βαθμολόγηση Ποιότητας | Προσθέτει ποιοτική διάσταση | Διατηρήστε το `prompts.json` με αναμενόμενες πτυχές; σχολιάστε βαθμολογίες (1–5) χειροκίνητα ή μέσω δευτερεύοντος μοντέλου |
| Εξαγωγή σε CSV / Markdown | Κοινόχρηστη αναφορά | Επεκτείνετε το σενάριο για να γράψετε το `benchmark_report.md` με πίνακα & επισημάνσεις |
| Ετικέτες Δυνατοτήτων Μοντέλου | Βοηθά στην αυτοματοποιημένη δρομολόγηση αργότερα | Διατηρήστε το `models.json` με `{alias: {capabilities:[], size_mb:..}}` |
| Φάση Προθέρμανσης Cache | Μείωση προκατάληψης ψυχρής εκκίνησης | Εκτελέστε έναν γύρο προθέρμανσης πριν από τον βρόχο χρονισμού (ήδη υλοποιημένο) |
| Ακρίβεια Ποσοστών | Ανθεκτική καθυστέρηση ουράς | Χρησιμοποιήστε το numpy percentile (ήδη στο αναδιαμορφωμένο σενάριο) |
| Προσέγγιση Κόστους Token | Οικονομική σύγκριση | Προσέγγιση κόστους = (tokens/sec * μέσος όρος tokens ανά αίτημα) * ενεργειακή εκτίμηση |
| Αυτόματη Παράκαμψη Αποτυχημένων Μοντέλων | Ανθεκτικότητα σε παρτίδες | Τυλίξτε κάθε αξιολόγηση σε try/except και σημειώστε πεδίο κατάστασης |

#### Ελάχιστο Απόσπασμα Εξαγωγής Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  
#### Παράδειγμα Σταθερού Σετ Προτροπών

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
Επαναλάβετε τη στατική λίστα αντί για τυχαίες προτροπές για συγκρίσιμες μετρήσεις μεταξύ commits.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.