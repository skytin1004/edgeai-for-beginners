<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T19:23:24+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "el"
}
-->
# Δείγμα Συνεδρίας 4: Επίδειξη Chainlit RAG

Εκτελέστε την ελάχιστη εφαρμογή Chainlit με το Foundry Local.

## Προαπαιτούμενα
- Windows 11, Python 3.10+
- Εγκατεστημένο το Foundry Local και διαθέσιμο ένα μοντέλο (π.χ., `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Εκτέλεση (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Επικύρωση
```cmd
curl http://localhost:8000/v1/models
```

## Επίλυση Προβλημάτων
- Εάν το VS Code εμφανίζει "chainlit could not be resolved":
	- Επιλέξτε τον διερμηνέα `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Βεβαιωθείτε ότι έχουν εγκατασταθεί οι εξαρτήσεις: `pip install -r Module08\requirements.txt`

## Αναφορές
- Οδηγός για το Open WebUI (εφαρμογή συνομιλίας με Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Μάθηση): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

