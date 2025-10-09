<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-09T13:07:32+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "el"
}
-->
# Συνεδρία 6: Foundry Local – Τα Μοντέλα ως Εργαλεία

## Περίληψη

Χρησιμοποιήστε τα μοντέλα ως συνθέσιμα εργαλεία μέσα σε ένα τοπικό λειτουργικό επίπεδο AI. Αυτή η συνεδρία δείχνει πώς να συνδέσετε πολλαπλές εξειδικευμένες κλήσεις SLM/LLM, να δρομολογήσετε επιλεκτικά εργασίες και να εκθέσετε μια ενιαία επιφάνεια SDK στις εφαρμογές. Θα δημιουργήσετε έναν ελαφρύ δρομολογητή μοντέλων + σχεδιαστή εργασιών, θα τον ενσωματώσετε σε ένα σενάριο εφαρμογής και θα περιγράψετε τη διαδρομή κλιμάκωσης προς το Azure AI Foundry για παραγωγικά φορτία.

## Στόχοι Μάθησης

- **Αντιληφθείτε** τα μοντέλα ως ατομικά εργαλεία με δηλωμένες δυνατότητες
- **Δρομολογήστε** αιτήματα βάσει πρόθεσης / βαθμολογίας με ευρετική μέθοδο
- **Συνδέστε** εξόδους σε πολυβήματες εργασίες (αποσύνθεση → επίλυση → βελτίωση)
- **Ενσωματώστε** ένα ενιαίο API πελάτη για εφαρμογές downstream
- **Κλιμακώστε** τον σχεδιασμό στο cloud (ίδιο συμβόλαιο συμβατό με OpenAI)

## Προαπαιτούμενα

- Ολοκληρωμένες συνεδρίες 1–5
- Πολλαπλά τοπικά μοντέλα αποθηκευμένα (π.χ., `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Απόσπασμα Περιβάλλοντος Πολλαπλών Πλατφορμών

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Απομακρυσμένη πρόσβαση/πρόσβαση σε VM από macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Ροή Επίδειξης (30 λεπτά)

### 1. Δήλωση Δυνατοτήτων Εργαλείων (5 λεπτά)

Δημιουργήστε το `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Ανίχνευση Πρόθεσης & Δρομολόγηση (8 λεπτά)

Δημιουργήστε το `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Σύνδεση Πολυβήματων Εργασιών (7 λεπτά)

Δημιουργήστε το `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Έργο Εκκίνησης: Προσαρμογή του `06-models-as-tools` (5 λεπτά)

Βελτιώσεις:
- Προσθέστε υποστήριξη για ροή token (προοδευτική ενημέρωση UI)
- Προσθέστε βαθμολογία εμπιστοσύνης: λεξική επικάλυψη ή κριτήριο προτροπής
- Εξαγωγή JSON ιχνών (πρόθεση → μοντέλο → καθυστέρηση → χρήση token)
- Εφαρμόστε επαναχρησιμοποίηση cache για επαναλαμβανόμενα υποβήματα

### 5. Διαδρομή Κλιμάκωσης προς Azure (5 λεπτά)

| Επίπεδο | Τοπικό (Foundry) | Cloud (Azure AI Foundry) | Στρατηγική Μετάβασης |
|---------|------------------|--------------------------|----------------------|
| Δρομολόγηση | Ευρετική Python | Ανθεκτικό μικρο-υπηρεσία | Κοντεϊνοποίηση & ανάπτυξη API |
| Μοντέλα | Αποθηκευμένα SLMs | Διαχειριζόμενες αναπτύξεις | Χαρτογραφήστε τοπικά ονόματα σε αναγνωριστικά ανάπτυξης |
| Παρατηρησιμότητα | Στατιστικά CLI/χειροκίνητα | Κεντρική καταγραφή & μετρήσεις | Προσθέστε δομημένα συμβάντα ιχνών |
| Ασφάλεια | Μόνο τοπικός host | Πιστοποίηση Azure / δικτύωση | Εισαγάγετε key vault για μυστικά |
| Κόστος | Πόροι συσκευής | Χρέωση κατανάλωσης | Προσθέστε προφυλακτήρες προϋπολογισμού |

## Λίστα Ελέγχου Επικύρωσης

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Αναμένετε επιλογή μοντέλου βάσει πρόθεσης και τελικό βελτιωμένο αποτέλεσμα.

## Αντιμετώπιση Προβλημάτων

| Πρόβλημα | Αιτία | Λύση |
|----------|-------|------|
| Όλες οι εργασίες δρομολογούνται στο ίδιο μοντέλο | Αδύναμοι κανόνες | Εμπλουτίστε το σύνολο regex INTENT_RULES |
| Η αλυσίδα αποτυγχάνει στο μέσο βήμα | Λείπει φορτωμένο μοντέλο | Εκτελέστε `foundry model run <model>` |
| Χαμηλή συνοχή εξόδου | Δεν υπάρχει φάση βελτίωσης | Προσθέστε βήμα περίληψης/επικύρωσης |

## Αναφορές

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Έγγραφα Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Πρότυπα Ποιότητας Προτροπών: Δείτε τη Συνεδρία 2

---

**Διάρκεια Συνεδρίας**: 30 λεπτά  
**Δυσκολία**: Ειδικός

## Δείγμα Σεναρίου & Χαρτογράφηση Εργαστηρίου

| Σενάρια Εργαστηρίου / Σημειωματάρια | Σενάριο | Στόχος | Πηγή Συνόλου Δεδομένων / Καταλόγου |
|------------------------------------|---------|--------|------------------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Βοηθός προγραμματιστή που χειρίζεται μικτές προτροπές πρόθεσης (αναδιάρθρωση, περίληψη, ταξινόμηση) | Ευρετική πρόθεση → δρομολόγηση ψευδωνύμου μοντέλου με χρήση token | Ενσωματωμένο `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Πολυβήματη σχεδίαση & βελτίωση για σύνθετη εργασία βοήθειας κωδικοποίησης | Αποσύνθεση → εξειδικευμένη εκτέλεση → βήμα βελτίωσης περίληψης | Ίδιο `CATALOG`; βήματα που προέρχονται από την έξοδο σχεδίου |

### Αφήγηση Σεναρίου
Ένα εργαλείο παραγωγικότητας μηχανικών λαμβάνει ετερογενείς εργασίες: αναδιάρθρωση κώδικα, περίληψη σημειώσεων αρχιτεκτονικής, ταξινόμηση σχολίων. Για ελαχιστοποίηση καθυστέρησης & χρήσης πόρων, ένα μικρό γενικό μοντέλο σχεδιάζει και συνοψίζει, ένα εξειδικευμένο μοντέλο κώδικα χειρίζεται την αναδιάρθρωση και ένα ελαφρύ μοντέλο ταξινόμησης επισημαίνει τα σχόλια. Το σενάριο αλυσίδας δείχνει σύνδεση + βελτίωση, ενώ το σενάριο δρομολογητή απομονώνει την προσαρμοστική δρομολόγηση μιας προτροπής.

### Στιγμιότυπο Καταλόγου
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Δείγματα Δοκιμαστικών Προτροπών
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Επέκταση Ιχνών (Προαιρετικό)
Προσθέστε γραμμές JSON ιχνών ανά βήμα για το `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Ευρετική Κλιμάκωση (Ιδέα)
Εάν το σχέδιο περιέχει λέξεις-κλειδιά όπως "βελτιστοποίηση", "ασφάλεια" ή το μήκος βήματος > 280 χαρακτήρες → κλιμακώστε σε μεγαλύτερο μοντέλο (π.χ., `gpt-oss-20b`) μόνο για αυτό το βήμα.

### Προαιρετικές Βελτιώσεις

| Περιοχή | Βελτίωση | Αξία | Υπόδειξη |
|---------|----------|------|----------|
| Cache | Επαναχρησιμοποίηση αντικειμένων διαχειριστή + πελάτη | Χαμηλότερη καθυστέρηση, λιγότερη επιβάρυνση | Χρησιμοποιήστε `workshop_utils.get_client` |
| Μετρήσεις Χρήσης | Καταγράψτε tokens & καθυστέρηση ανά βήμα | Προφίλ & βελτιστοποίηση | Χρονομετρήστε κάθε κλήση δρομολόγησης; αποθηκεύστε σε λίστα ιχνών |
| Προσαρμοστική Δρομολόγηση | Εμπιστοσύνη / κόστος | Καλύτερη ισορροπία ποιότητας-κόστους | Προσθέστε βαθμολογία: αν η προτροπή > N χαρακτήρες ή το regex ταιριάζει με το domain → κλιμακώστε σε μεγαλύτερο μοντέλο |
| Δυναμικό Μητρώο Δυνατοτήτων | Hot reload καταλόγου | Χωρίς επανεκκίνηση ανάπτυξης | Φορτώστε το `catalog.json` κατά την εκτέλεση; παρακολουθήστε τη χρονική σήμανση αρχείου |
| Στρατηγική Εφεδρείας | Ανθεκτικότητα σε αποτυχίες | Υψηλότερη διαθεσιμότητα | Δοκιμάστε το κύριο → σε περίπτωση εξαίρεσης fallback ψευδώνυμο |
| Ροή Αλυσίδας | Πρώιμη ανατροφοδότηση | Βελτίωση UX | Ροή κάθε βήματος και buffer τελικής εισόδου βελτίωσης |
| Ενσωματώσεις Πρόθεσης Vector | Πιο λεπτομερής δρομολόγηση | Υψηλότερη ακρίβεια πρόθεσης | Ενσωματώστε την προτροπή, ομαδοποιήστε & χαρτογραφήστε το κέντρο → δυνατότητα |
| Εξαγωγή Ιχνών | Ελεγχόμενη αλυσίδα | Συμμόρφωση/αναφορά | Εκδώστε γραμμές JSON: βήμα, πρόθεση, μοντέλο, καθυστέρηση_ms, tokens |
| Προσομοίωση Κόστους | Εκτίμηση πριν το cloud | Σχεδιασμός προϋπολογισμού | Αναθέστε υποθετικό κόστος/token ανά μοντέλο & συγκεντρώστε ανά εργασία |
| Λειτουργία Ντετερμινισμού | Αναπαραγωγή αναπαραγωγιμότητας | Σταθερή αξιολόγηση | Περιβάλλον: `temperature=0`, σταθερός αριθμός βημάτων |

#### Παράδειγμα Δομής Ιχνών

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Σκίτσο Προσαρμοστικής Κλιμάκωσης

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Hot Reload Καταλόγου Μοντέλων

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```


Προχωρήστε σταδιακά—αποφύγετε την υπερβολική μηχανική σε πρώιμα πρωτότυπα.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.