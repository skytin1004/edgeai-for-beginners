<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T12:46:14+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "el"
}
-->
# Ενημερώσεις για το Foundry Local SDK

## Επισκόπηση

Ενημερώθηκαν τα σημειωματάρια Workshop και τα βοηθητικά εργαλεία ώστε να χρησιμοποιούν σωστά το **επίσημο Foundry Local Python SDK**, ακολουθώντας τα πρότυπα από:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Αρχεία που τροποποιήθηκαν

### 1. `Workshop/samples/workshop_utils.py`

**Αλλαγές:**
- ✅ Προστέθηκε χειρισμός σφαλμάτων εισαγωγής για το πακέτο `foundry-local-sdk`
- ✅ Βελτιώθηκε η τεκμηρίωση με πρότυπα του επίσημου SDK
- ✅ Ενισχύθηκε η καταγραφή με Unicode σύμβολα (✓, ✗, ⚠)
- ✅ Προστέθηκαν αναλυτικά docstrings με παραδείγματα
- ✅ Καλύτερα μηνύματα σφαλμάτων που αναφέρονται σε CLI εντολές
- ✅ Ενημερώθηκαν τα σχόλια ώστε να ταιριάζουν με την τεκμηρίωση του επίσημου SDK

**Κύριες Βελτιώσεις:**

#### Χειρισμός Σφαλμάτων Εισαγωγής
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Βελτιωμένη Συνάρτηση `get_client()`
- Προστέθηκε λεπτομερής τεκμηρίωση για το πρότυπο αρχικοποίησης του SDK
- Διευκρινίστηκε ότι το `FoundryLocalManager` ξεκινά την υπηρεσία αυτόματα
- Επεξηγήθηκε η επίλυση ψευδωνύμων μοντέλων σε παραλλαγές βελτιστοποιημένες για υλικό
- Βελτιώθηκε η καταγραφή με πληροφορίες για το endpoint
- Καλύτερα μηνύματα σφαλμάτων που προτείνουν βήματα αντιμετώπισης προβλημάτων

#### Βελτιωμένη Συνάρτηση `chat_once()`
- Προστέθηκε αναλυτικό docstring με παραδείγματα χρήσης
- Διευκρινίστηκε η συμβατότητα με το OpenAI SDK
- Τεκμηριώθηκε η υποστήριξη streaming (μέσω kwargs)
- Βελτιώθηκαν τα μηνύματα σφαλμάτων με προτάσεις CLI εντολών
- Προστέθηκαν σημειώσεις για τον έλεγχο διαθεσιμότητας μοντέλων

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Αλλαγές:**
- ✅ Ενημερώθηκαν όλα τα markdown κελιά με αναφορές στο SDK
- ✅ Βελτιώθηκαν τα σχόλια κώδικα με εξηγήσεις για τα πρότυπα του SDK
- ✅ Ενισχύθηκε η τεκμηρίωση και οι εξηγήσεις των κελιών
- ✅ Προστέθηκαν οδηγίες αντιμετώπισης προβλημάτων
- ✅ Ενημερώθηκε ο κατάλογος μοντέλων (αντικαταστάθηκε το 'gpt-oss-20b' με το 'phi-3.5-mini')
- ✅ Καλύτερη μορφοποίηση εξόδου με οπτικούς δείκτες
- ✅ Προστέθηκαν συνδέσεις και αναφορές στο SDK σε όλο το σημειωματάριο

**Ενημερώσεις ανά κελί:**

#### Κελί 1 (Τίτλος)
- Προστέθηκαν συνδέσεις τεκμηρίωσης SDK
- Αναφέρθηκαν τα επίσημα αποθετήρια GitHub

#### Κελί 2 (Σενάριο)
- Αναμορφώθηκε με αριθμημένα βήματα
- Διευκρινίστηκε το πρότυπο δρομολόγησης βάσει προθέσεων
- Τονίστηκαν τα οφέλη της τοπικής εκτέλεσης

#### Κελί 3 (Εγκατάσταση Εξαρτήσεων)
- Προστέθηκε εξήγηση για το τι παρέχει κάθε πακέτο
- Τεκμηριώθηκαν οι δυνατότητες του SDK (επίλυση ψευδωνύμων, βελτιστοποίηση υλικού)

#### Κελί 4 (Ρύθμιση Περιβάλλοντος)
- Ενισχύθηκαν τα docstrings των συναρτήσεων
- Προστέθηκαν σχόλια εντός κώδικα που εξηγούν τα πρότυπα του SDK
- Τεκμηριώθηκε η δομή του καταλόγου μοντέλων
- Διευκρινίστηκε η αντιστοίχιση προτεραιοτήτων/δυνατοτήτων

#### Κελί 5 (Έλεγχος Καταλόγου)
- Προστέθηκαν οπτικά σημάδια ελέγχου (✓)
- Καλύτερη μορφοποίηση εξόδου

#### Κελί 6 (Δοκιμή Ανίχνευσης Πρόθεσης)
- Αναμορφώθηκε η έξοδος σε μορφή πίνακα
- Εμφανίζει τόσο την πρόθεση όσο και το επιλεγμένο μοντέλο

#### Κελί 7 (Συνάρτηση Δρομολόγησης)
- Αναλυτική εξήγηση προτύπου SDK
- Τεκμηριώθηκε η ροή αρχικοποίησης
- Καταγράφηκαν όλες οι δυνατότητες (επανάληψη, παρακολούθηση, σφάλματα)
- Προστέθηκε σύνδεση αναφοράς SDK

#### Κελί 8 (Παραδειγματική Παρτίδα)
- Ενισχύθηκε η εξήγηση του τι να περιμένετε
- Προστέθηκε ενότητα αντιμετώπισης προβλημάτων
- Συμπεριλήφθηκαν CLI εντολές για αποσφαλμάτωση
- Καλύτερη μορφοποίηση εμφάνισης εξόδου

### 3. `Workshop/notebooks/session06_README.md` (Νέο Αρχείο)

**Δημιουργήθηκε αναλυτική τεκμηρίωση που καλύπτει:**

1. **Επισκόπηση**: Διάγραμμα αρχιτεκτονικής και εξήγηση συστατικών
2. **Ενσωμάτωση SDK**: Παραδείγματα κώδικα που ακολουθούν τα επίσημα πρότυπα
3. **Προαπαιτούμενα**: Οδηγίες ρύθμισης βήμα προς βήμα
4. **Χρήση**: Πώς να εκτελέσετε και να προσαρμόσετε το σημειωματάριο
5. **Ψευδώνυμα Μοντέλων**: Εξήγηση παραλλαγών βελτιστοποιημένων για υλικό
6. **Αντιμετώπιση Προβλημάτων**: Συνηθισμένα ζητήματα και λύσεις
7. **Επέκταση**: Πώς να προσθέσετε προθέσεις, μοντέλα και προσαρμοσμένη λογική
8. **Συμβουλές Απόδοσης**: Βέλτιστες πρακτικές για χρήση σε παραγωγή
9. **Πόροι**: Συνδέσεις σε επίσημη τεκμηρίωση και κοινότητα

## Υλοποίηση Προτύπου SDK

### Επίσημο Πρότυπο (από την τεκμηρίωση του Foundry Local)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Η Υλοποίησή μας (στο workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Οφέλη της Προσέγγισής μας:**
- ✅ Ακολουθεί ακριβώς το επίσημο πρότυπο SDK
- ✅ Προσθέτει caching για αποφυγή επαναλαμβανόμενης αρχικοποίησης
- ✅ Περιλαμβάνει λογική επανάληψης για ανθεκτικότητα σε παραγωγή
- ✅ Υποστηρίζει παρακολούθηση χρήσης token
- ✅ Παρέχει καλύτερα μηνύματα σφαλμάτων
- ✅ Παραμένει συμβατό με τα επίσημα παραδείγματα

## Αλλαγές στον Κατάλογο Μοντέλων

### Πριν
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Μετά
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Λόγος:** Αντικαταστάθηκε το 'gpt-oss-20b' (μη τυπικό ψευδώνυμο) με το 'phi-3.5-mini' (επίσημο ψευδώνυμο του Foundry Local).

## Εξαρτήσεις

### Ενημερωμένο requirements.txt

Το Workshop requirements.txt περιλαμβάνει ήδη:
```
foundry-local-sdk
openai>=1.30.0
```

Αυτά είναι τα μόνα πακέτα που χρειάζονται για την ενσωμάτωση του Foundry Local.

## Δοκιμή των Ενημερώσεων

### 1. Επαλήθευση ότι το Foundry Local Εκτελείται

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Έλεγχος Διαθέσιμων Μοντέλων

```bash
foundry model ls
```

Βεβαιωθείτε ότι αυτά τα μοντέλα είναι διαθέσιμα ή θα κατέβουν αυτόματα:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Εκτέλεση του Σημειωματάριου

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Ή ανοίξτε το στο VS Code και εκτελέστε όλα τα κελιά.

### 4. Αναμενόμενη Συμπεριφορά

**Κελί 1 (Εγκατάσταση):** Εγκαθιστά επιτυχώς τα πακέτα  
**Κελί 2 (Ρύθμιση):** Χωρίς σφάλματα, οι εισαγωγές λειτουργούν  
**Κελί 3 (Επαλήθευση):** Εμφανίζει ✓ με τη λίστα μοντέλων  
**Κελί 4 (Δοκιμή Πρόθεσης):** Εμφανίζει αποτελέσματα ανίχνευσης πρόθεσης  
**Κελί 5 (Δρομολογητής):** Εμφανίζει ✓ Συνάρτηση δρομολόγησης έτοιμη  
**Κελί 6 (Εκτέλεση):** Δρομολογεί προτροπές σε μοντέλα, εμφανίζει αποτελέσματα  

### 5. Αντιμετώπιση Σφαλμάτων Σύνδεσης

Αν δείτε `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Μεταβλητές Περιβάλλοντος

Οι παρακάτω μεταβλητές περιβάλλοντος υποστηρίζονται:

| Μεταβλητή | Προεπιλογή | Περιγραφή |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Ορίστε σε `1` για εκτύπωση χρήσης token |
| `RETRY_ON_FAIL` | `1` | Ενεργοποίηση λογικής επανάληψης |
| `RETRY_BACKOFF` | `1.0` | Αρχική καθυστέρηση επανάληψης (δευτερόλεπτα) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Υπέρβαση του endpoint της υπηρεσίας |

### Παραδείγματα Χρήσης

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Μετάβαση από το Παλιό Πρότυπο

Αν έχετε υπάρχοντα κώδικα που χρησιμοποιεί άμεσες κλήσεις API, δείτε πώς να μεταβείτε:

### Πριν (Άμεσο API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Μετά (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Οφέλη της Μετάβασης
- ✅ Αυτόματη διαχείριση υπηρεσιών
- ✅ Επίλυση ψευδωνύμων μοντέλων
- ✅ Επιλογή βελτιστοποίησης υλικού
- ✅ Καλύτερος χειρισμός σφαλμάτων
- ✅ Συμβατότητα με το OpenAI SDK
- ✅ Υποστήριξη streaming

## Αναφορές

### Επίσημη Τεκμηρίωση
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Πηγή Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Αναφορά CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Αντιμετώπιση Προβλημάτων**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Πόροι Workshop
- **README Συνεδρίας 06**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Παραδειγματικό Σημειωματάριο**: `Workshop/notebooks/session06_models_router.ipynb`

### Κοινότητα
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Επόμενα Βήματα

1. **Ανασκόπηση Αλλαγών**: Διαβάστε τα ενημερωμένα αρχεία
2. **Δοκιμή Σημειωματάριου**: Εκτελέστε το session06_models_router.ipynb
3. **Επαλήθευση SDK**: Βεβαιωθείτε ότι το foundry-local-sdk είναι εγκατεστημένο
4. **Έλεγχος Υπηρεσίας**: Επιβεβαιώστε ότι το Foundry Local εκτελείται
5. **Εξερεύνηση Τεκμηρίωσης**: Διαβάστε το νέο session06_README.md

## Περίληψη

Αυτές οι ενημερώσεις διασφαλίζουν ότι τα υλικά του Workshop ακολουθούν τα **επίσημα πρότυπα του Foundry Local SDK** ακριβώς όπως τεκμηριώνονται στο αποθετήριο GitHub. Όλα τα παραδείγματα κώδικα, η τεκμηρίωση και τα βοηθητικά εργαλεία ευθυγραμμίζονται πλέον με τις συνιστώμενες βέλτιστες πρακτικές της Microsoft για τοπική ανάπτυξη μοντέλων AI.

Οι αλλαγές βελτιώνουν:
- ✅ **Ορθότητα**: Χρήση επίσημων προτύπων SDK
- ✅ **Τεκμηρίωση**: Αναλυτικές εξηγήσεις και παραδείγματα
- ✅ **Χειρισμός Σφαλμάτων**: Καλύτερα μηνύματα και οδηγίες αντιμετώπισης προβλημάτων
- ✅ **Συντηρησιμότητα**: Ακολουθεί επίσημες συμβάσεις
- ✅ **Εμπειρία Χρήστη**: Πιο σαφείς οδηγίες και βοήθεια αποσφαλμάτωσης

---

**Ενημερώθηκε:** 8 Οκτωβρίου 2025  
**Έκδοση SDK:** foundry-local-sdk (τελευταία)  
**Κλάδος Workshop:** Reactor

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.