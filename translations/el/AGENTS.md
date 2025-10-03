<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:34:49+00:00",
  "source_file": "AGENTS.md",
  "language_code": "el"
}
-->
# AGENTS.md

## Επισκόπηση Έργου

Το EdgeAI for Beginners είναι ένα ολοκληρωμένο εκπαιδευτικό αποθετήριο που διδάσκει την ανάπτυξη Edge AI με Μικρά Μοντέλα Γλώσσας (SLMs). Το μάθημα καλύπτει τις βασικές αρχές του EdgeAI, την ανάπτυξη μοντέλων, τεχνικές βελτιστοποίησης και υλοποιήσεις έτοιμες για παραγωγή χρησιμοποιώντας το Microsoft Foundry Local και διάφορα πλαίσια AI.

**Κύριες Τεχνολογίες:**
- Python 3.8+ (κύρια γλώσσα για παραδείγματα AI/ML)
- .NET C# (παραδείγματα AI/ML)
- JavaScript/Node.js με Electron (για εφαρμογές desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Πλαίσια AI: LangChain, Semantic Kernel, Chainlit
- Βελτιστοποίηση Μοντέλων: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Τύπος Αποθετηρίου:** Εκπαιδευτικό αποθετήριο περιεχομένου με 8 ενότητες και 10 ολοκληρωμένες παραδειγματικές εφαρμογές

**Αρχιτεκτονική:** Πολυεπίπεδο μονοπάτι μάθησης με πρακτικά παραδείγματα που δείχνουν μοτίβα ανάπτυξης Edge AI

## Δομή Αποθετηρίου

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Εντολές Ρύθμισης

### Ρύθμιση Αποθετηρίου

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Ρύθμιση Παραδειγμάτων Python (Ενότητα08 και παραδείγματα Python)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Ρύθμιση Παραδειγμάτων Node.js (Παράδειγμα 08 - Εφαρμογή Συνομιλίας Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Ρύθμιση Foundry Local

Το Foundry Local απαιτείται για την εκτέλεση των παραδειγμάτων της Ενότητας08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Ροή Εργασίας Ανάπτυξης

### Ανάπτυξη Περιεχομένου

Αυτό το αποθετήριο περιέχει κυρίως **εκπαιδευτικό περιεχόμενο σε Markdown**. Κατά την πραγματοποίηση αλλαγών:

1. Επεξεργαστείτε αρχεία `.md` στους αντίστοιχους φακέλους ενοτήτων
2. Ακολουθήστε τα υπάρχοντα μοτίβα μορφοποίησης
3. Βεβαιωθείτε ότι τα παραδείγματα κώδικα είναι ακριβή και δοκιμασμένα
4. Ενημερώστε το αντίστοιχο μεταφρασμένο περιεχόμενο αν χρειάζεται (ή αφήστε την αυτοματοποίηση να το χειριστεί)

### Ανάπτυξη Παραδειγματικών Εφαρμογών

Για παραδείγματα Python (παραδείγματα 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Για το παράδειγμα Electron (παράδειγμα 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Δοκιμή Παραδειγματικών Εφαρμογών

Τα παραδείγματα Python δεν έχουν αυτοματοποιημένες δοκιμές αλλά μπορούν να επικυρωθούν με την εκτέλεσή τους:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Το παράδειγμα Electron διαθέτει υποδομή δοκιμών:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Οδηγίες Δοκιμών

### Επικύρωση Περιεχομένου

Το αποθετήριο χρησιμοποιεί αυτοματοποιημένες ροές εργασίας μετάφρασης. Δεν απαιτείται χειροκίνητη δοκιμή για μεταφράσεις.

**Χειροκίνητη επικύρωση για αλλαγές περιεχομένου:**
1. Ελέγξτε την απόδοση Markdown προβάλλοντας αρχεία `.md`
2. Βεβαιωθείτε ότι όλοι οι σύνδεσμοι οδηγούν σε έγκυρους προορισμούς
3. Δοκιμάστε οποιαδήποτε αποσπάσματα κώδικα περιλαμβάνονται στην τεκμηρίωση
4. Ελέγξτε ότι οι εικόνες φορτώνονται σωστά

### Δοκιμή Παραδειγματικών Εφαρμογών

**Η Ενότητα08/παραδείγματα/08 (εφαρμογή Electron) διαθέτει ολοκληρωμένες δοκιμές:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Τα παραδείγματα Python πρέπει να δοκιμαστούν χειροκίνητα:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Οδηγίες Στυλ Κώδικα

### Περιεχόμενο Markdown

- Χρησιμοποιήστε συνεπή ιεραρχία επικεφαλίδων (# για τίτλο, ## για κύριες ενότητες, ### για υποενότητες)
- Συμπεριλάβετε μπλοκ κώδικα με καθορισμό γλώσσας: ```python, ```bash, ```javascript
- Ακολουθήστε την υπάρχουσα μορφοποίηση για πίνακες, λίστες και έμφαση
- Κρατήστε τις γραμμές ευανάγνωστες (στόχος ~80-100 χαρακτήρες, αλλά όχι αυστηρά)
- Χρησιμοποιήστε σχετικούς συνδέσμους για εσωτερικές αναφορές

### Στυλ Κώδικα Python

- Ακολουθήστε τις συμβάσεις PEP 8
- Χρησιμοποιήστε υποδείξεις τύπου όπου είναι κατάλληλο
- Συμπεριλάβετε docstrings για συναρτήσεις και κλάσεις
- Χρησιμοποιήστε ουσιαστικά ονόματα μεταβλητών
- Κρατήστε τις συναρτήσεις εστιασμένες και συνοπτικές

### Στυλ Κώδικα JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Βασικές συμβάσεις:**
- Παρέχεται διαμόρφωση ESLint στο παράδειγμα 08
- Prettier για μορφοποίηση κώδικα
- Χρησιμοποιήστε σύγχρονη σύνταξη ES6+
- Ακολουθήστε τα υπάρχοντα μοτίβα στον κώδικα

## Οδηγίες Αιτημάτων Ενσωμάτωσης

### Μορφή Τίτλου
```
[ModuleXX] Brief description of change
```
ή
```
[Module08/samples/XX] Description for sample changes
```

### Πριν την Υποβολή

**Για αλλαγές περιεχομένου:**
- Προβάλετε όλα τα τροποποιημένα αρχεία Markdown
- Βεβαιωθείτε ότι οι σύνδεσμοι και οι εικόνες λειτουργούν
- Ελέγξτε για τυπογραφικά λάθη και γραμματικά σφάλματα

**Για αλλαγές κώδικα παραδειγμάτων (Ενότητα08/παραδείγματα/08):**
```bash
npm run lint
npm test
```

**Για αλλαγές παραδειγμάτων Python:**
- Δοκιμάστε ότι το παράδειγμα εκτελείται επιτυχώς
- Βεβαιωθείτε ότι η διαχείριση σφαλμάτων λειτουργεί
- Ελέγξτε τη συμβατότητα με το Foundry Local

### Διαδικασία Αναθεώρησης

- Οι αλλαγές εκπαιδευτικού περιεχομένου αναθεωρούνται για ακρίβεια και σαφήνεια
- Τα παραδείγματα κώδικα δοκιμάζονται για λειτουργικότητα
- Οι ενημερώσεις μετάφρασης χειρίζονται αυτόματα από το GitHub Actions

## Σύστημα Μετάφρασης

**ΣΗΜΑΝΤΙΚΟ:** Αυτό το αποθετήριο χρησιμοποιεί αυτοματοποιημένη μετάφραση μέσω GitHub Actions.

- Οι μεταφράσεις βρίσκονται στον φάκελο `/translations/` (50+ γλώσσες)
- Αυτοματοποιημένο μέσω της ροής εργασίας `co-op-translator.yml`
- **ΜΗΝ επεξεργάζεστε χειροκίνητα αρχεία μετάφρασης** - θα αντικατασταθούν
- Επεξεργαστείτε μόνο τα αρχεία πηγής στα Αγγλικά στον ριζικό φάκελο και στους φακέλους ενοτήτων
- Οι μεταφράσεις δημιουργούνται αυτόματα κατά την προώθηση στον κλάδο `main`

## Ενσωμάτωση Foundry Local

Τα περισσότερα παραδείγματα της Ενότητας08 απαιτούν την εκτέλεση του Microsoft Foundry Local:

### Εκκίνηση Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Επαλήθευση Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Μεταβλητές Περιβάλλοντος για Παραδείγματα

Τα περισσότερα παραδείγματα χρησιμοποιούν αυτές τις μεταβλητές περιβάλλοντος:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Δημιουργία και Ανάπτυξη

### Ανάπτυξη Περιεχομένου

Αυτό το αποθετήριο είναι κυρίως τεκμηρίωση - δεν απαιτείται διαδικασία δημιουργίας για το περιεχόμενο.

### Δημιουργία Παραδειγματικών Εφαρμογών

**Εφαρμογή Electron (Ενότητα08/παραδείγματα/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Παραδείγματα Python:**
Δεν απαιτείται διαδικασία δημιουργίας - τα παραδείγματα εκτελούνται απευθείας με τον διερμηνέα Python.

## Συνηθισμένα Προβλήματα και Αντιμετώπιση

### Το Foundry Local Δεν Εκτελείται
**Πρόβλημα:** Τα παραδείγματα αποτυγχάνουν με σφάλματα σύνδεσης

**Λύση:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Προβλήματα Εικονικού Περιβάλλοντος Python
**Πρόβλημα:** Σφάλματα εισαγωγής μονάδων

**Λύση:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Προβλήματα Δημιουργίας Electron
**Πρόβλημα:** Αποτυχίες npm install ή build

**Λύση:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Συγκρούσεις Ροής Εργασίας Μετάφρασης
**Πρόβλημα:** Το PR μετάφρασης συγκρούεται με τις αλλαγές σας

**Λύση:**
- Επεξεργαστείτε μόνο αρχεία πηγής στα Αγγλικά
- Αφήστε την αυτοματοποιημένη ροή εργασίας μετάφρασης να χειριστεί τις μεταφράσεις
- Εάν προκύψουν συγκρούσεις, συγχωνεύστε τον `main` στον κλάδο σας μετά τη συγχώνευση των μεταφράσεων

## Πρόσθετοι Πόροι

### Μονοπάτια Μάθησης
- **Μονοπάτι Αρχαρίων:** Ενότητες 01-02 (7-9 ώρες)
- **Μονοπάτι Μεσαίου Επιπέδου:** Ενότητες 03-04 (9-11 ώρες)
- **Μονοπάτι Προχωρημένων:** Ενότητες 05-07 (12-15 ώρες)
- **Μονοπάτι Ειδικών:** Ενότητα 08 (8-10 ώρες)

### Κύριο Περιεχόμενο Ενοτήτων
- **Ενότητα01:** Βασικές αρχές EdgeAI και πραγματικές περιπτώσεις χρήσης
- **Ενότητα02:** Οικογένειες και αρχιτεκτονικές Μικρών Μοντέλων Γλώσσας (SLM)
- **Ενότητα03:** Στρατηγικές ανάπτυξης τοπικά και στο cloud
- **Ενότητα04:** Βελτιστοποίηση μοντέλων με πολλαπλά πλαίσια
- **Ενότητα05:** SLMOps - λειτουργίες παραγωγής
- **Ενότητα06:** Πράκτορες AI και κλήση λειτουργιών
- **Ενότητα07:** Υλοποιήσεις ειδικές για πλατφόρμες
- **Ενότητα08:** Εργαλειοθήκη Foundry Local με 10 ολοκληρωμένα παραδείγματα

### Εξωτερικές Εξαρτήσεις
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Τοπικός χρόνος εκτέλεσης μοντέλων AI
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Πλαίσιο βελτιστοποίησης
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Εργαλειοθήκη βελτιστοποίησης μοντέλων
- [OpenVINO](https://docs.openvino.ai/) - Εργαλειοθήκη βελτιστοποίησης της Intel

## Σημειώσεις Ειδικές για το Έργο

### Παραδειγματικές Εφαρμογές Ενότητας08

Το αποθετήριο περιλαμβάνει 10 ολοκληρωμένες παραδειγματικές εφαρμογές:

1. **01-REST Chat Quickstart** - Βασική ενσωμάτωση OpenAI SDK
2. **02-OpenAI SDK Integration** - Προηγμένες δυνατότητες SDK
3. **03-Model Discovery & Benchmarking** - Εργαλεία σύγκρισης μοντέλων
4. **04-Chainlit RAG Application** - Δημιουργία με ενισχυμένη ανάκτηση
5. **05-Multi-Agent Orchestration** - Βασικός συντονισμός πρακτόρων
6. **06-Models-as-Tools Router** - Έξυπνη δρομολόγηση μοντέλων
7. **07-Direct API Client** - Χαμηλού επιπέδου ενσωμάτωση API
8. **08-Windows 11 Chat App** - Εγγενής εφαρμογή desktop Electron
9. **09-Advanced Multi-Agent System** - Σύνθετος συντονισμός πρακτόρων
10. **10-Foundry Tools Framework** - Ενσωμάτωση LangChain/Semantic Kernel

Κάθε παράδειγμα δείχνει διαφορετικές πτυχές της ανάπτυξης Edge AI με το Foundry Local.

### Σκέψεις Απόδοσης

- Τα SLMs είναι βελτιστοποιημένα για ανάπτυξη σε edge (2-16GB RAM)
- Η τοπική πρόβλεψη παρέχει χρόνους απόκρισης 50-500ms
- Οι τεχνικές ποσοτικοποίησης επιτυγχάνουν μείωση μεγέθους κατά 75% με διατήρηση απόδοσης 85%
- Δυνατότητες συνομιλίας σε πραγματικό χρόνο με τοπικά μοντέλα

### Ασφάλεια και Ιδιωτικότητα

- Όλη η επεξεργασία γίνεται τοπικά - δεν αποστέλλονται δεδομένα στο cloud
- Κατάλληλο για εφαρμογές ευαίσθητες στην ιδιωτικότητα (υγειονομική περίθαλψη, χρηματοοικονομικά)
- Πληροί τις απαιτήσεις κυριαρχίας δεδομένων
- Το Foundry Local λειτουργεί εξ ολοκλήρου σε τοπικό υλικό

---

**Αυτό είναι ένα εκπαιδευτικό αποθετήριο που επικεντρώνεται στη διδασκαλία της ανάπτυξης Edge AI. Το κύριο μοτίβο συνεισφοράς είναι η βελτίωση του εκπαιδευτικού περιεχομένου και η προσθήκη/ενίσχυση παραδειγματικών εφαρμογών που δείχνουν έννοιες Edge AI.**

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.