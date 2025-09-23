<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T18:22:33+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "it"
}
-->
# Changelog

Tutte le modifiche rilevanti a EdgeAI for Beginners sono documentate qui. Questo progetto utilizza voci basate su date e lo stile Keep a Changelog (Aggiunto, Modificato, Corretto, Rimosso, Documentazione, Spostato).

## 2025-09-18

### Aggiunto
- Modulo 08: Microsoft Foundry Local – Toolkit completo per sviluppatori
  - Sei sessioni: configurazione, integrazione con Azure AI Foundry, modelli open-source, demo all'avanguardia, agenti e modelli come strumenti
  - Esempi eseguibili sotto `Module08/samples/01`–`06` con istruzioni per cmd su Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart con supporto OpenAI/Foundry Local e Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orchestrazione multi-agente (`python -m samples.05.agents.coordinator`)
    - `06` Router modelli-come-strumenti (`router.py`)
- Supporto Azure OpenAI nell'esempio SDK della Sessione 2 con configurazione tramite variabili di ambiente
- `.vscode/settings.json` per puntare a `Module08/.venv` e migliorare la risoluzione dell'analisi Python
- `.env` con suggerimento `PYTHONPATH` per la consapevolezza di VS Code/Pylance

### Modificato
- Modello predefinito aggiornato a `phi-4-mini` nei documenti e negli esempi del Modulo 08; rimosse le menzioni residue di `phi-3.5` all'interno del Modulo 08
- Miglioramenti al router (`Module08/samples/06/router.py`):
  - Scoperta degli endpoint tramite `foundry service status` con parsing regex
  - Controllo di salute `/v1/models` all'avvio
  - Registro modelli configurabile tramite variabili di ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisiti aggiornati: `Module08/requirements.txt` ora include `openai` (insieme a `requests`, `chainlit`)
- Chiarimenti sulla guida agli esempi Chainlit e aggiunta di risoluzione dei problemi; risoluzione degli import tramite impostazioni del workspace

### Corretto
- Risolti problemi di importazione:
  - Il router non dipende più da un modulo `utils` inesistente; le funzioni sono integrate
  - Il coordinatore utilizza importazioni relative (`from .specialists import ...`) ed è invocato tramite percorso del modulo
  - Configurazione di VS Code/Pylance per risolvere `chainlit` e importazioni di pacchetti
- Corretto un piccolo errore di battitura in `STUDY_GUIDE.md` e aggiunta copertura del Modulo 08

### Rimosso
- Eliminato `Module08/infra/obs.py` non utilizzato e rimosso la directory vuota `infra/`; i pattern di osservabilità sono mantenuti come opzionali nei documenti

### Spostato
- Consolidati i demo del Modulo 08 sotto `Module08/samples` con cartelle numerate per sessione
  - Spostata l'app Chainlit in `samples/04`
  - Spostati gli agenti in `samples/05` e aggiunti file `__init__.py` per la risoluzione dei pacchetti

### Documentazione
- Documenti delle sessioni del Modulo 08 e tutti i README degli esempi arricchiti con riferimenti a Microsoft Learn e fornitori affidabili
- `Module08/README.md` aggiornato con Panoramica degli Esempi, configurazione del router e suggerimenti per la validazione
- Sezione Windows Foundry Local in `Module07/README.md` validata rispetto ai documenti Learn
- `STUDY_GUIDE.md` aggiornato:
  - Aggiunto il Modulo 08 alla panoramica, ai programmi, al tracker di progresso
  - Aggiunta una sezione completa di Riferimenti (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Storico (sommario)
- Architettura del corso e moduli stabiliti (Moduli 01–07)
- Modernizzazione iterativa dei contenuti, standardizzazione della formattazione e aggiunta di casi studio
- Espansione della copertura dei framework di ottimizzazione (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Non rilasciato / Backlog (proposte)
- Test opzionali per ogni esempio per validare la disponibilità di Foundry Local
- Revisione delle traduzioni per allineare i riferimenti ai modelli (es. `phi-4-mini`) dove appropriato
- Aggiunta di una configurazione minima di pyright se i team preferiscono una maggiore rigidità a livello di workspace

---

