<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T21:22:59+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "it"
}
-->
# Changelog

Tutte le modifiche rilevanti a EdgeAI for Beginners sono documentate qui. Questo progetto utilizza voci basate su date e lo stile Keep a Changelog (Aggiunto, Modificato, Corretto, Rimosso, Documentazione, Spostato).

## 2025-09-23

### Modificato - Modernizzazione principale del Modulo 08
- **Allineamento completo con i modelli di repository Microsoft Foundry-Local**
  - Aggiornati tutti gli esempi di codice per utilizzare `FoundryLocalManager` moderno e l'integrazione con OpenAI SDK
  - Sostituiti le chiamate manuali `requests` deprecate con l'uso corretto dell'SDK
  - Allineati i modelli di implementazione con la documentazione ufficiale Microsoft e i campioni

- **Modernizzazione di 05.AIPoweredAgents.md**:
  - Aggiornata l'orchestrazione multi-agente per utilizzare modelli SDK moderni
  - Migliorata l'implementazione del coordinatore con funzionalità avanzate (cicli di feedback, monitoraggio delle prestazioni)
  - Aggiunta gestione completa degli errori e controllo dello stato del servizio
  - Integrati riferimenti appropriati ai campioni locali (`samples/05/multi_agent_orchestration.ipynb`)
  - Aggiornati gli esempi di chiamata delle funzioni per utilizzare il parametro moderno `tools` invece di `functions` deprecato
  - Aggiunti modelli pronti per la produzione con monitoraggio e tracciamento delle statistiche

- **Riscrittura completa di 06.ModelsAsTools.md**:
  - Sostituito il registro degli strumenti di base con un'implementazione intelligente del router di modelli
  - Aggiunta selezione dei modelli basata su parole chiave per diversi tipi di attività (generale, ragionamento, codice, creativo)
  - Integrata configurazione basata sull'ambiente con assegnazione flessibile dei modelli
  - Migliorata con monitoraggio completo dello stato del servizio e gestione degli errori
  - Aggiunti modelli di distribuzione in produzione con monitoraggio delle richieste e tracciamento delle prestazioni
  - Allineati con l'implementazione locale in `samples/06/router.py` e `samples/06/model_router.ipynb`

- **Miglioramenti alla struttura della documentazione**:
  - Aggiunte sezioni panoramiche che evidenziano la modernizzazione e l'allineamento con l'SDK
  - Migliorata con emoji e una formattazione migliore per una maggiore leggibilità
  - Aggiunti riferimenti appropriati ai file di campioni locali in tutta la documentazione
  - Inclusa guida all'implementazione pronta per la produzione e migliori pratiche

### Aggiunto
- Sezioni panoramiche complete nei file del Modulo 08 che evidenziano l'integrazione moderna con l'SDK
- Punti salienti dell'architettura che mostrano funzionalità avanzate (sistemi multi-agente, routing intelligente)
- Riferimenti diretti alle implementazioni di campioni locali per un'esperienza pratica
- Guida alla distribuzione in produzione con modelli di monitoraggio e gestione degli errori
- Esempi interattivi di notebook Jupyter con funzionalità avanzate e benchmark

### Corretto
- Discrepanze di allineamento tra documentazione e implementazioni di campioni effettivi
- Modelli di utilizzo dell'SDK obsoleti in tutto il Modulo 08
- Riferimenti mancanti alla libreria completa di campioni locali
- Approcci di implementazione incoerenti tra diverse sezioni

---

## 2025-09-18

### Aggiunto
- Modulo 08: Microsoft Foundry Local – Toolkit completo per sviluppatori
  - Sei sessioni: configurazione, integrazione Azure AI Foundry, modelli open-source, demo all'avanguardia, agenti e modelli-come-strumenti
  - Campioni eseguibili sotto `Module08/samples/01`–`06` con istruzioni cmd per Windows
    - `01` Chat REST rapida (`chat_quickstart.py`)
    - `02` Avvio rapido SDK con OpenAI/Foundry Local e supporto Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI elenco e benchmark (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orchestrazione multi-agente (`python -m samples.05.agents.coordinator`)
    - `06` Router modelli-come-strumenti (`router.py`)
- Supporto Azure OpenAI nel campione SDK della Sessione 2 con configurazione delle variabili d'ambiente
- `.vscode/settings.json` per puntare a `Module08/.venv` e migliorare la risoluzione dell'analisi Python
- `.env` con suggerimento `PYTHONPATH` per la consapevolezza di VS Code/Pylance

### Modificato
- Modello predefinito aggiornato a `phi-4-mini` in tutta la documentazione e i campioni del Modulo 08; rimosse le menzioni rimanenti di `phi-3.5` nel Modulo 08
- Miglioramenti al router (`Module08/samples/06/router.py`):
  - Scoperta degli endpoint tramite `foundry service status` con parsing regex
  - Controllo dello stato `/v1/models` all'avvio
  - Registro dei modelli configurabile tramite ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisiti aggiornati: `Module08/requirements.txt` ora include `openai` (insieme a `requests`, `chainlit`)
- Guida al campione Chainlit chiarita e aggiunta risoluzione dei problemi; risoluzione delle importazioni tramite impostazioni del workspace

### Corretto
- Risolti problemi di importazione:
  - Il router non dipende più da un modulo `utils` inesistente; le funzioni sono integrate
  - Il coordinatore utilizza importazioni relative (`from .specialists import ...`) ed è invocato tramite percorso del modulo
  - Configurazione VS Code/Pylance per risolvere `chainlit` e importazioni di pacchetti
- Corretto un piccolo errore di battitura in `STUDY_GUIDE.md` e aggiunta copertura del Modulo 08

### Rimosso
- Eliminato `Module08/infra/obs.py` inutilizzato e rimossa la directory `infra/` vuota; i modelli di osservabilità sono mantenuti come opzionali nella documentazione

### Spostato
- Consolidati i demo del Modulo 08 sotto `Module08/samples` con cartelle numerate per sessione
  - Spostata l'app Chainlit in `samples/04`
  - Spostati gli agenti in `samples/05` e aggiunti file `__init__.py` per la risoluzione dei pacchetti

### Documentazione
- Documentazione delle sessioni del Modulo 08 e tutti i README dei campioni arricchiti con riferimenti Microsoft Learn e fornitori affidabili
- `Module08/README.md` aggiornato con Panoramica dei campioni, configurazione del router e suggerimenti per la validazione
- Sezione Windows Foundry Local di `Module07/README.md` validata rispetto alla documentazione Learn
- `STUDY_GUIDE.md` aggiornato:
  - Aggiunto il Modulo 08 alla panoramica, ai programmi, al tracker di progresso
  - Aggiunta una sezione di Riferimenti completa (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Storico (sommario)
- Architettura del corso e moduli stabiliti (Moduli 01–07)
- Modernizzazione iterativa dei contenuti, standardizzazione della formattazione e aggiunta di casi studio
- Espansione della copertura dei framework di ottimizzazione (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Non rilasciato / Backlog (proposte)
- Test opzionali per campione per convalidare la disponibilità di Foundry Local
- Revisione delle traduzioni per allineare i riferimenti ai modelli (es. `phi-4-mini`) dove appropriato
- Aggiunta configurazione minima di pyright se i team preferiscono una maggiore rigidità a livello di workspace

---

