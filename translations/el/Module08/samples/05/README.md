<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T19:22:59+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "el"
}
-->
# Δείγμα Συνεδρίας 5: Ορχήστρωση Πολλαπλών Πρακτόρων

Αυτό το δείγμα παρουσιάζει ένα μοτίβο συντονιστή + ειδικών χρησιμοποιώντας το OpenAI-compatible endpoint του Foundry Local.

## Εκτέλεση (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Επικύρωση
```cmd
curl http://localhost:8000/v1/models
```

## Επίλυση Προβλημάτων
- Εάν το VS Code επισημάνει το `import specialists` ως μη επιλυμένο στο `coordinator.py`, βεβαιωθείτε ότι εκτελείται ως module και ο διερμηνέας δείχνει στο `Module08/.venv`:
	- Εκτέλεση: `python -m samples.05.agents.coordinator`
	- Επιλογή διερμηνέα: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Αναφορές
- Foundry Local (Μάθηση): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Επισκόπηση Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Δείγμα κλήσης λειτουργιών (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

