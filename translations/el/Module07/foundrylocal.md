<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T19:23:50+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "el"
}
-->
# Foundry Local στα Windows (Επικυρωμένο)

Αυτός ο οδηγός σας βοηθά να εγκαταστήσετε, να εκτελέσετε και να ενσωματώσετε το Microsoft Foundry Local στα Windows. Όλα τα βήματα και οι εντολές έχουν επικυρωθεί σύμφωνα με τα έγγραφα του Microsoft Learn.

- Ξεκινήστε: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Αρχιτεκτονική: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Αναφορά CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Ενσωμάτωση SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Συμπίεση μοντέλων HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Τοπικό vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Εγκατάσταση / Αναβάθμιση στα Windows

- Εγκατάσταση:
```cmd
winget install Microsoft.FoundryLocal
```
- Αναβάθμιση:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Έλεγχος έκδοσης:
```cmd
foundry --version
```

## 2) Βασικά CLI (Τρεις Κατηγορίες)

- Μοντέλο:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Υπηρεσία:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Σημειώσεις:
- Η υπηρεσία παρέχει ένα REST API συμβατό με OpenAI. Η θύρα του endpoint εκχωρείται δυναμικά· χρησιμοποιήστε `foundry service status` για να την εντοπίσετε.
- Χρησιμοποιήστε τα SDKs για ευκολία· αυτά διαχειρίζονται αυτόματα την ανακάλυψη του endpoint όπου υποστηρίζεται.

## 3) Εντοπισμός Τοπικού Endpoint (Δυναμική Θύρα)

Το Foundry Local εκχωρεί μια δυναμική θύρα κάθε φορά που ξεκινά η υπηρεσία:
```cmd
foundry service status
```
Χρησιμοποιήστε το αναφερόμενο `http://localhost:<PORT>` ως `base_url` με μονοπάτια συμβατά με OpenAI (για παράδειγμα, `/v1/chat/completions`).

## 4) Γρήγορη Δοκιμή μέσω OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Αναφορές:
- Ενσωμάτωση SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Φέρτε το Δικό σας Μοντέλο (Συμπίεση με Olive)

Αν χρειάζεστε ένα μοντέλο που δεν υπάρχει στον κατάλογο, συμπιέστε το σε ONNX για το Foundry Local χρησιμοποιώντας το Olive.

Γενική ροή (δείτε τα έγγραφα για βήματα):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Έγγραφα:
- Συμπίεση BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Αντιμετώπιση Προβλημάτων

- Έλεγχος κατάστασης υπηρεσίας και αρχείων καταγραφής:
```cmd
foundry service status
foundry service diag
```
- Εκκαθάριση ή μετακίνηση cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Ενημέρωση στην τελευταία προεπισκόπηση:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Σχετική Εμπειρία Ανάπτυξης στα Windows

- Επιλογές τοπικής vs cloud AI στα Windows, συμπεριλαμβανομένων των Foundry Local και Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit με Foundry Local (χρησιμοποιήστε `foundry service status` για να λάβετε το URL του chat endpoint):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

