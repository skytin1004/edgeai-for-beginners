<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T13:10:13+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "el"
}
-->
# Δείγματα Εργαστηρίου - Περίληψη Ενημέρωσης Foundry Local SDK

## Επισκόπηση

Όλα τα δείγματα Python στον κατάλογο `Workshop/samples` έχουν ενημερωθεί ώστε να ακολουθούν τις βέλτιστες πρακτικές του Foundry Local SDK και να διασφαλίζουν τη συνοχή σε όλο το εργαστήριο.

**Ημερομηνία**: 8 Οκτωβρίου 2025  
**Πεδίο Εφαρμογής**: 9 αρχεία Python σε 6 συνεδρίες εργαστηρίου  
**Κύρια Εστίαση**: Διαχείριση σφαλμάτων, τεκμηρίωση, πρότυπα SDK, εμπειρία χρήστη

---

## Ενημερωμένα Αρχεία

### Συνεδρία 01: Ξεκινώντας
- ✅ `chat_bootstrap.py` - Βασικά παραδείγματα συνομιλίας και ροής

### Συνεδρία 02: Λύσεις RAG
- ✅ `rag_pipeline.py` - Υλοποίηση RAG με embeddings
- ✅ `rag_eval_ragas.py` - Αξιολόγηση RAG με μετρικές RAGAS

### Συνεδρία 03: Μοντέλα Ανοιχτού Κώδικα
- ✅ `benchmark_oss_models.py` - Συγκριτική αξιολόγηση πολλαπλών μοντέλων

### Συνεδρία 04: Μοντέλα Αιχμής
- ✅ `model_compare.py` - Σύγκριση SLM και LLM

### Συνεδρία 05: Πράκτορες με Τεχνητή Νοημοσύνη
- ✅ `agents_orchestrator.py` - Συντονισμός πολλαπλών πρακτόρων

### Συνεδρία 06: Μοντέλα ως Εργαλεία
- ✅ `models_router.py` - Δρομολόγηση μοντέλων βάσει πρόθεσης
- ✅ `models_pipeline.py` - Πολυβηματική δρομολογημένη διαδικασία

### Υποστηρικτική Υποδομή
- ✅ `workshop_utils.py` - Ήδη ακολουθεί τις βέλτιστες πρακτικές (δεν απαιτούνται αλλαγές)

---

## Κύριες Βελτιώσεις

### 1. Ενισχυμένη Διαχείριση Σφαλμάτων

**Πριν:**
```python
manager, client, model_id = get_client(alias)
```

**Μετά:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Οφέλη:**
- Ομαλή διαχείριση σφαλμάτων με σαφή μηνύματα
- Χρήσιμες υποδείξεις για αντιμετώπιση προβλημάτων
- Κατάλληλοι κωδικοί εξόδου για scripting

### 2. Καλύτερη Διαχείριση Εισαγωγών

**Πριν:**
```python
from sentence_transformers import SentenceTransformer
```

**Μετά:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Οφέλη:**
- Σαφείς οδηγίες όταν λείπουν εξαρτήσεις
- Αποφυγή ασαφών σφαλμάτων εισαγωγής
- Φιλικές προς τον χρήστη οδηγίες εγκατάστασης

### 3. Αναλυτική Τεκμηρίωση

**Προστέθηκε σε όλα τα δείγματα:**
- Τεκμηρίωση μεταβλητών περιβάλλοντος στις docstrings
- Σύνδεσμοι αναφοράς SDK
- Παραδείγματα χρήσης
- Αναλυτική τεκμηρίωση συναρτήσεων/παραμέτρων
- Υποδείξεις τύπων για καλύτερη υποστήριξη IDE

**Παράδειγμα:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Βελτιωμένη Ανατροφοδότηση Χρήστη

**Προστέθηκε ενημερωτική καταγραφή:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Δείκτες προόδου:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Δομημένη έξοδος:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Αξιόπιστη Συγκριτική Αξιολόγηση

**Βελτιώσεις Συνεδρίας 03:**
- Διαχείριση σφαλμάτων ανά μοντέλο (συνεχίζει σε περίπτωση αποτυχίας)
- Αναλυτική αναφορά προόδου
- Σωστή εκτέλεση γύρων προθέρμανσης
- Υποστήριξη μέτρησης καθυστέρησης πρώτου token
- Σαφής διαχωρισμός σταδίων

### 6. Συνεπείς Υποδείξεις Τύπων

**Προστέθηκαν παντού:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Οφέλη:**
- Καλύτερη αυτόματη συμπλήρωση στο IDE
- Έγκαιρη ανίχνευση σφαλμάτων
- Αυτοτεκμηριούμενος κώδικας

### 7. Ενισχυμένος Δρομολογητής Μοντέλων

**Βελτιώσεις Συνεδρίας 06:**
- Αναλυτική τεκμηρίωση ανίχνευσης πρόθεσης
- Επεξήγηση αλγορίθμου επιλογής μοντέλου
- Αναλυτικά αρχεία καταγραφής δρομολόγησης
- Μορφοποίηση εξόδου δοκιμών
- Ανάκτηση σφαλμάτων σε δοκιμές παρτίδας

### 8. Ορχήστρα Πολλαπλών Πρακτόρων

**Βελτιώσεις Συνεδρίας 05:**
- Αναφορά προόδου ανά στάδιο
- Διαχείριση σφαλμάτων ανά πράκτορα
- Σαφής δομή διαδικασίας
- Καλύτερη τεκμηρίωση διαχείρισης μνήμης

---

## Λίστα Ελέγχου Δοκιμών

### Προαπαιτούμενα
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Δοκιμή Κάθε Δείγματος

#### Συνεδρία 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Συνεδρία 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Συνεδρία 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Συνεδρία 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Συνεδρία 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Συνεδρία 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Αναφορά Μεταβλητών Περιβάλλοντος

### Γενικές (Όλα τα Δείγματα)
| Μεταβλητή | Περιγραφή | Προεπιλογή |
|-----------|-----------|------------|
| `FOUNDRY_LOCAL_ALIAS` | Ψευδώνυμο μοντέλου προς χρήση | Διαφέρει ανά δείγμα |
| `FOUNDRY_LOCAL_ENDPOINT` | Υπέρβαση τελικού σημείου υπηρεσίας | Αυτόματη ανίχνευση |
| `SHOW_USAGE` | Εμφάνιση χρήσης token | `0` |
| `RETRY_ON_FAIL` | Ενεργοποίηση λογικής επανάληψης | `1` |
| `RETRY_BACKOFF` | Αρχική καθυστέρηση επανάληψης | `1.0` |

### Ειδικές για Δείγματα
| Μεταβλητή | Χρησιμοποιείται Από | Περιγραφή |
|-----------|---------------------|-----------|
| `EMBED_MODEL` | Συνεδρία 02 | Όνομα μοντέλου embeddings |
| `RAG_QUESTION` | Συνεδρία 02 | Ερώτηση δοκιμής για RAG |
| `BENCH_MODELS` | Συνεδρία 03 | Μοντέλα για συγκριτική αξιολόγηση (διαχωρισμένα με κόμμα) |
| `BENCH_ROUNDS` | Συνεδρία 03 | Αριθμός γύρων συγκριτικής αξιολόγησης |
| `BENCH_PROMPT` | Συνεδρία 03 | Ερώτημα δοκιμής για συγκριτική αξιολόγηση |
| `BENCH_STREAM` | Συνεδρία 03 | Μέτρηση καθυστέρησης πρώτου token |
| `SLM_ALIAS` | Συνεδρία 04 | Μικρό μοντέλο γλώσσας |
| `LLM_ALIAS` | Συνεδρία 04 | Μεγάλο μοντέλο γλώσσας |
| `COMPARE_PROMPT` | Συνεδρία 04 | Ερώτημα δοκιμής σύγκρισης |
| `AGENT_MODEL_PRIMARY` | Συνεδρία 05 | Κύριο μοντέλο πράκτορα |
| `AGENT_MODEL_EDITOR` | Συνεδρία 05 | Μοντέλο πράκτορα επεξεργαστή |
| `AGENT_QUESTION` | Συνεδρία 05 | Ερώτηση δοκιμής για πράκτορες |
| `PIPELINE_TASK` | Συνεδρία 06 | Εργασία για τη διαδικασία |

---

## Σημαντικές Αλλαγές

**Καμία** - Όλες οι αλλαγές είναι συμβατές προς τα πίσω.

Τα υπάρχοντα scripts θα συνεχίσουν να λειτουργούν. Τα νέα χαρακτηριστικά είναι:
- Προαιρετικές μεταβλητές περιβάλλοντος
- Ενισχυμένα μηνύματα σφαλμάτων (δεν διακόπτουν τη λειτουργικότητα)
- Πρόσθετη καταγραφή (μπορεί να κατασταλεί)
- Καλύτερες υποδείξεις τύπων (χωρίς επίδραση κατά την εκτέλεση)

---

## Εφαρμοσμένες Βέλτιστες Πρακτικές

### 1. Χρήση του Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Κατάλληλο Πρότυπο Διαχείρισης Σφαλμάτων
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Ενημερωτική Καταγραφή
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Υποδείξεις Τύπων
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Αναλυτικές Docstrings
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Υποστήριξη Μεταβλητών Περιβάλλοντος
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Ομαλή Υποβάθμιση
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Συνήθη Προβλήματα & Λύσεις

### Πρόβλημα: Σφάλματα Εισαγωγής
**Λύση:** Εγκαταστήστε τις ελλείπουσες εξαρτήσεις
```bash
pip install sentence-transformers ragas datasets numpy
```

### Πρόβλημα: Σφάλματα Σύνδεσης
**Λύση:** Βεβαιωθείτε ότι το Foundry Local εκτελείται
```bash
foundry service status
foundry model run phi-4-mini
```

### Πρόβλημα: Μοντέλο Δεν Βρέθηκε
**Λύση:** Ελέγξτε τα διαθέσιμα μοντέλα
```bash
foundry model ls
foundry model download <alias>
```

### Πρόβλημα: Αργή Απόδοση
**Λύση:** Χρησιμοποιήστε μικρότερα μοντέλα ή προσαρμόστε τις παραμέτρους
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Επόμενα Βήματα

### 1. Δοκιμή Όλων των Δειγμάτων
Εκτελέστε τη λίστα ελέγχου δοκιμών παραπάνω για να επαληθεύσετε ότι όλα τα δείγματα λειτουργούν σωστά.

### 2. Ενημέρωση Τεκμηρίωσης
- Ενημερώστε τα αρχεία markdown των συνεδριών με νέα παραδείγματα
- Προσθέστε ενότητα αντιμετώπισης προβλημάτων στο κύριο README
- Δημιουργήστε έναν οδηγό γρήγορης αναφοράς

### 3. Δημιουργία Δοκιμών Ενσωμάτωσης
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Προσθήκη Συγκριτικών Αξιολογήσεων Απόδοσης
Παρακολουθήστε τις βελτιώσεις απόδοσης από τις βελτιώσεις διαχείρισης σφαλμάτων.

### 5. Ανατροφοδότηση Χρηστών
Συλλέξτε ανατροφοδότηση από τους συμμετέχοντες του εργαστηρίου σχετικά με:
- Την σαφήνεια των μηνυμάτων σφαλμάτων
- Την πληρότητα της τεκμηρίωσης
- Την ευκολία χρήσης

---

## Πόροι

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Γρήγορη Αναφορά**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Σημειώσεις Μετάβασης**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Κύριο Αποθετήριο**: https://github.com/microsoft/Foundry-Local

---

## Συντήρηση

### Προσθήκη Νέων Δειγμάτων
Ακολουθήστε αυτά τα πρότυπα κατά τη δημιουργία νέων δειγμάτων:

1. Χρησιμοποιήστε το `workshop_utils` για διαχείριση πελατών
2. Προσθέστε αναλυτική διαχείριση σφαλμάτων
3. Συμπεριλάβετε υποστήριξη μεταβλητών περιβάλλοντος
4. Προσθέστε υποδείξεις τύπων και docstrings
5. Παρέχετε ενημερωτική καταγραφή
6. Συμπεριλάβετε παραδείγματα χρήσης στη docstring
7. Συνδέστε με την τεκμηρίωση SDK

### Ανασκόπηση Ενημερώσεων
Κατά την ανασκόπηση ενημερώσεων δειγμάτων, ελέγξτε για:
- [ ] Διαχείριση σφαλμάτων σε όλες τις λειτουργίες I/O
- [ ] Υποδείξεις τύπων σε δημόσιες συναρτήσεις
- [ ] Αναλυτικές docstrings
- [ ] Τεκμηρίωση μεταβλητών περιβάλλοντος
- [ ] Ενημερωτική ανατροφοδότηση χρήστη
- [ ] Σύνδεσμοι αναφοράς SDK
- [ ] Συνεπή στυλ κώδικα

---

**Περίληψη**: Όλα τα δείγματα Python του Εργαστηρίου ακολουθούν πλέον τις βέλτιστες πρακτικές του Foundry Local SDK με ενισχυμένη διαχείριση σφαλμάτων, αναλυτική τεκμηρίωση και βελτιωμένη εμπειρία χρήστη. Δεν υπάρχουν αλλαγές που να διακόπτουν τη λειτουργικότητα - όλη η υπάρχουσα λειτουργικότητα διατηρείται και ενισχύεται.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.