<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T10:25:01+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "it"
}
-->
# Changelog

Tutte le modifiche rilevanti a EdgeAI for Beginners sono documentate qui. Questo progetto utilizza voci basate su date e lo stile Keep a Changelog (Aggiunto, Modificato, Corretto, Rimosso, Documentazione, Spostato).

## 2025-10-08

### Aggiunto - Aggiornamento completo del Workshop
- **Riscrittura completa di Workshop README.md**:
  - Aggiunta un'introduzione completa che spiega il valore dell'Edge AI (privacy, prestazioni, costi)
  - Creati 6 obiettivi di apprendimento principali con competenze dettagliate
  - Aggiunta una tabella degli obiettivi di apprendimento con deliverable e matrice delle competenze
  - Inclusa una sezione sulle competenze pronte per il mercato del lavoro per la rilevanza industriale
  - Aggiunta una guida rapida con prerequisiti e configurazione in 3 passaggi
  - Create tabelle delle risorse per esempi Python (8 file con tempi di esecuzione)
  - Aggiunta una tabella dei notebook Jupyter (8 notebook con valutazioni di difficoltà)
  - Creata una tabella della documentazione (7 documenti chiave con indicazioni "Quando usare")
  - Aggiunte raccomandazioni sui percorsi di apprendimento per diversi livelli di competenza

- **Infrastruttura di validazione e test del Workshop**:
  - Creato `scripts/validate_samples.py` - Strumento di validazione completo per sintassi, importazioni e best practice
  - Creato `scripts/test_samples.py` - Esecutore di test preliminari per tutti gli esempi Python
  - Aggiunta documentazione di validazione a `scripts/README.md`

- **Documentazione completa**:
  - Creato `SAMPLES_UPDATE_SUMMARY.md` - Guida dettagliata di oltre 400 righe che copre tutti i miglioramenti
  - Creato `UPDATE_COMPLETE.md` - Sintesi esecutiva del completamento dell'aggiornamento
  - Creato `QUICK_REFERENCE.md` - Scheda di riferimento rapido per il Workshop

### Modificato - Modernizzazione degli esempi Python del Workshop
- **Aggiornati tutti gli 8 esempi Python con best practice**:
  - Migliorata la gestione degli errori con blocchi try-except per tutte le operazioni di I/O
  - Aggiunti suggerimenti sui tipi e docstring completi
  - Implementato un modello di logging coerente [INFO]/[ERROR]/[RESULT]
  - Protette le importazioni opzionali con suggerimenti per l'installazione
  - Migliorato il feedback all'utente in tutti gli esempi

- **session01/chat_bootstrap.py**:
  - Migliorata l'inizializzazione del client con messaggi di errore completi
  - Migliorata la gestione degli errori di streaming con la validazione dei chunk
  - Aggiunta una gestione migliore delle eccezioni per l'indisponibilità del servizio

- **session02/rag_pipeline.py**:
  - Aggiunte protezioni per le importazioni di sentence-transformers con suggerimenti per l'installazione
  - Migliorata la gestione degli errori per operazioni di embedding e generazione
  - Migliorato il formato dell'output con risultati strutturati

- **session02/rag_eval_ragas.py**:
  - Protette le importazioni opzionali (ragas, datasets) con messaggi di errore user-friendly
  - Aggiunta gestione degli errori per le metriche di valutazione
  - Migliorato il formato dell'output per i risultati della valutazione

- **session03/benchmark_oss_models.py**:
  - Implementata una degradazione graduale (continua in caso di errori sui modelli)
  - Aggiunta una reportistica dettagliata sui progressi e gestione degli errori per modello
  - Migliorato il calcolo delle statistiche con un recupero completo dagli errori

- **session04/model_compare.py**:
  - Aggiunti suggerimenti sui tipi (tipi Tuple nei ritorni)
  - Migliorato il formato dell'output con risultati JSON strutturati
  - Implementata gestione degli errori per modello con recupero

- **session05/agents_orchestrator.py**:
  - Migliorata Agent.act() con docstring complete
  - Aggiunta gestione degli errori della pipeline con logging per ogni fase
  - Migliorata la gestione della memoria e il tracciamento dello stato

- **session06/models_router.py**:
  - Migliorata la documentazione delle funzioni per tutti i componenti di routing
  - Aggiunto logging dettagliato nella funzione route()
  - Migliorato l'output dei test con risultati strutturati

- **session06/models_pipeline.py**:
  - Aggiunta gestione degli errori alla funzione helper chat()
  - Migliorata pipeline() con logging delle fasi e reportistica sui progressi
  - Migliorata main() con un recupero completo dagli errori

### Documentazione - Miglioramento della documentazione del Workshop
- Aggiornato il README.md principale con una sezione sul Workshop che evidenzia il percorso di apprendimento pratico
- Migliorata STUDY_GUIDE.md con una sezione completa sul Workshop che include:
  - Obiettivi di apprendimento e aree di studio
  - Domande di autovalutazione
  - Esercizi pratici con stime di tempo
  - Allocazione del tempo per studio concentrato e part-time
  - Aggiunto il Workshop al modello di tracciamento dei progressi
- Aggiornata la guida all'allocazione del tempo da 20 ore a 30 ore (incluso il Workshop)
- Aggiunte descrizioni degli esempi del Workshop e obiettivi di apprendimento al README

### Corretto
- Risolti schemi incoerenti di gestione degli errori negli esempi del Workshop
- Corrette importazioni opzionali con protezioni adeguate
- Corrette mancanze di suggerimenti sui tipi in funzioni critiche
- Risolto feedback insufficiente all'utente in scenari di errore
- Corrette problematiche di validazione con un'infrastruttura di test completa

---

## 2025-09-23

### Modificato - Modernizzazione del Modulo 08
- **Allineamento completo con i modelli del repository Microsoft Foundry-Local**:
  - Aggiornati tutti gli esempi di codice per utilizzare il moderno `FoundryLocalManager` e l'integrazione con OpenAI SDK
  - Sostituite chiamate manuali deprecate di `requests` con un uso corretto dell'SDK
  - Allineati i modelli di implementazione con la documentazione ufficiale Microsoft e gli esempi

- **Modernizzazione di 05.AIPoweredAgents.md**:
  - Aggiornata l'orchestrazione multi-agente per utilizzare modelli SDK moderni
  - Migliorata l'implementazione del coordinatore con funzionalità avanzate (cicli di feedback, monitoraggio delle prestazioni)
  - Aggiunta gestione completa degli errori e controllo della salute del servizio
  - Integrati riferimenti adeguati agli esempi locali (`samples/05/multi_agent_orchestration.ipynb`)
  - Aggiornati esempi di chiamata di funzioni per utilizzare il moderno parametro `tools` invece del deprecato `functions`
  - Aggiunti modelli pronti per la produzione con monitoraggio e tracciamento delle statistiche

- **Riscrittura completa di 06.ModelsAsTools.md**:
  - Sostituito il registro degli strumenti di base con un'implementazione intelligente del router dei modelli
  - Aggiunta selezione dei modelli basata su parole chiave per diversi tipi di attività (generale, ragionamento, codice, creativo)
  - Integrata configurazione basata sull'ambiente con assegnazione flessibile dei modelli
  - Migliorata con monitoraggio completo della salute del servizio e gestione degli errori
  - Aggiunti modelli di distribuzione in produzione con monitoraggio delle richieste e tracciamento delle prestazioni
  - Allineato con l'implementazione locale in `samples/06/router.py` e `samples/06/model_router.ipynb`

- **Miglioramenti alla struttura della documentazione**:
  - Aggiunte sezioni panoramiche che evidenziano la modernizzazione e l'allineamento con l'SDK
  - Migliorata con emoji e formattazione per una leggibilità superiore
  - Aggiunti riferimenti adeguati ai file di esempio locali in tutta la documentazione
  - Inclusa guida all'implementazione pronta per la produzione e best practice

### Aggiunto
- Sezioni panoramiche complete nei file del Modulo 08 che evidenziano l'integrazione moderna con l'SDK
- Evidenziazioni architetturali che mostrano funzionalità avanzate (sistemi multi-agente, routing intelligente)
- Riferimenti diretti alle implementazioni di esempio locali per un'esperienza pratica
- Guida alla distribuzione in produzione con modelli di monitoraggio e gestione degli errori
- Esempi interattivi di notebook Jupyter con funzionalità avanzate e benchmark

### Corretto
- Discrepanze di allineamento tra documentazione e implementazioni di esempio effettive
- Modelli di utilizzo dell'SDK obsoleti in tutto il Modulo 08
- Mancanza di riferimenti alla libreria di esempi locali completa
- Approcci di implementazione incoerenti tra le diverse sezioni

---

## 2025-09-18

### Aggiunto
- Modulo 08: Microsoft Foundry Local – Toolkit completo per sviluppatori
  - Sei sessioni: configurazione, integrazione Azure AI Foundry, modelli open-source, demo all'avanguardia, agenti e modelli-come-strumenti
  - Esempi eseguibili sotto `Module08/samples/01`–`06` con istruzioni per cmd Windows
    - `01` Chat REST rapida (`chat_quickstart.py`)
    - `02` Quickstart SDK con supporto OpenAI/Foundry Local e Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI elenco e benchmark (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orchestrazione multi-agente (`python -m samples.05.agents.coordinator`)
    - `06` Router Modelli-come-Strumenti (`router.py`)
- Supporto Azure OpenAI nell'esempio SDK della Sessione 2 con configurazione tramite variabili d'ambiente
- `.vscode/settings.json` per puntare a `Module08/.venv` e migliorare la risoluzione dell'analisi Python
- `.env` con suggerimento `PYTHONPATH` per la consapevolezza di VS Code/Pylance

### Modificato
- Modello predefinito aggiornato a `phi-4-mini` in tutta la documentazione e gli esempi del Modulo 08; rimosse le menzioni residue di `phi-3.5` nel Modulo 08
- Miglioramenti al router (`Module08/samples/06/router.py`):
  - Scoperta degli endpoint tramite `foundry service status` con parsing regex
  - Controllo della salute `/v1/models` all'avvio
  - Registro dei modelli configurabile tramite ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisiti aggiornati: `Module08/requirements.txt` ora include `openai` (insieme a `requests`, `chainlit`)
- Chiarita la guida agli esempi Chainlit e aggiunta risoluzione dei problemi; risoluzione delle importazioni tramite impostazioni del workspace

### Corretto
- Risolti problemi di importazione:
  - Il router non dipende più da un modulo inesistente `utils`; le funzioni sono state integrate
  - Il coordinatore utilizza un'importazione relativa (`from .specialists import ...`) ed è invocato tramite percorso del modulo
  - Configurazione di VS Code/Pylance per risolvere `chainlit` e importazioni di pacchetti
- Corretto un piccolo errore di battitura in `STUDY_GUIDE.md` e aggiunta copertura del Modulo 08

### Rimosso
- Eliminato `Module08/infra/obs.py` non utilizzato e rimossa la directory vuota `infra/`; i modelli di osservabilità sono stati mantenuti come opzionali nella documentazione

### Spostato
- Consolidate le demo del Modulo 08 sotto `Module08/samples` con cartelle numerate per sessione
  - Spostata l'app Chainlit in `samples/04`
  - Spostati gli agenti in `samples/05` e aggiunti file `__init__.py` per la risoluzione dei pacchetti

### Documentazione
- Documentazione delle sessioni del Modulo 08 e tutti i README degli esempi arricchiti con riferimenti a Microsoft Learn e fornitori affidabili
- `Module08/README.md` aggiornato con Panoramica degli Esempi, configurazione del router e suggerimenti per la validazione
- `Module07/README.md` sezione Windows Foundry Local validata rispetto alla documentazione Learn
- `STUDY_GUIDE.md` aggiornato:
  - Aggiunto il Modulo 08 a panoramica, programmi, tracciatore di progressi
  - Aggiunta una sezione di Riferimenti completa (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Storico (sintesi)
- Architettura del corso e moduli stabiliti (Moduli 01–07)
- Modernizzazione iterativa dei contenuti, standardizzazione della formattazione e aggiunta di casi studio
- Espansione della copertura dei framework di ottimizzazione (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Non rilasciato / Backlog (proposte)
- Test opzionali per esempio per validare la disponibilità di Foundry Local
- Revisione delle traduzioni per allineare i riferimenti ai modelli (es. `phi-4-mini`) dove appropriato
- Aggiunta di una configurazione minima di pyright se i team preferiscono una maggiore rigidità a livello di workspace

---

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.