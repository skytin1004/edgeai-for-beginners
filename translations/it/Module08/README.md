<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T18:24:51+00:00",
  "source_file": "Module08/README.md",
  "language_code": "it"
}
-->
# Modulo 08: Pratica con Microsoft Foundry Local - Toolkit Completo per Sviluppatori

## Panoramica

Microsoft Foundry Local rappresenta la nuova generazione dello sviluppo AI edge, offrendo agli sviluppatori strumenti potenti per creare, distribuire e scalare applicazioni AI localmente, mantenendo un'integrazione fluida con Azure AI Foundry. Questo modulo fornisce una copertura completa di Foundry Local, dall'installazione allo sviluppo avanzato di agenti.

**Tecnologie Chiave:**
- Microsoft Foundry Local CLI e SDK
- Integrazione con Azure AI Foundry
- Inferenza di modelli su dispositivo
- Caching e ottimizzazione dei modelli locali
- Architetture basate su agenti

## Obiettivi di Apprendimento del Modulo

Completando questo modulo, sarai in grado di:

- **Padroneggiare la Configurazione di Foundry Local**: Installare, configurare e ottimizzare Foundry Local per lo sviluppo su Windows 11
- **Distribuire Modelli Diversi**: Eseguire i modelli phi, qwen, deepseek e GPT-OSS-20B localmente tramite comandi CLI
- **Creare Soluzioni di Produzione**: Sviluppare applicazioni AI con tecniche avanzate di prompt engineering e integrazione dei dati
- **Sfruttare l'Ecosistema Open-Source**: Integrare modelli Hugging Face e contributi della comunità
- **Confrontare Architetture AI**: Comprendere i compromessi tra LLM e SLM e le strategie di distribuzione
- **Sviluppare Agenti AI**: Creare agenti intelligenti utilizzando l'architettura e le capacità di grounding di Foundry Local
- **Implementare Modelli come Strumenti**: Creare soluzioni AI modulari e personalizzabili per applicazioni aziendali

## Struttura della Sessione

### [1: Introduzione a Foundry Local](./01.FoundryLocalSetup.md)
**Focus**: Installazione, configurazione CLI, caching dei modelli e accelerazione hardware

**Cosa Imparerai:**
- Installazione completa di Foundry Local su Windows 11
- Configurazione CLI e struttura dei comandi
- Strategie di caching dei modelli per prestazioni ottimali
- Configurazione e ottimizzazione dell'accelerazione hardware
- Distribuzione pratica dei modelli phi, qwen, deepseek e GPT-OSS-20B

**Durata**: 2-3 ore  
**Prerequisiti**: Windows 11, conoscenze di base della riga di comando

---

### [2: Creare Soluzioni AI con Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus**: Tecniche avanzate di prompt engineering, integrazione dei dati e attività pratiche

**Cosa Imparerai:**
- Tecniche avanzate di prompt engineering
- Modelli di integrazione dei dati e migliori pratiche
- Creazione di attività AI pratiche con Foundry Local
- Workflow di integrazione fluida con Azure AI Foundry
- Ottimizzazione delle prestazioni e monitoraggio

**Durata**: 2-3 ore  
**Prerequisiti**: Completamento della Sessione 1, account Azure (opzionale)

---

### [3: Modelli Open-Source con Foundry Local](./03.OpenSourceModels.md)
**Focus**: Integrazione Hugging Face, strategie di selezione dei modelli e contributi della comunità

**Cosa Imparerai:**
- Integrazione dei modelli Hugging Face con Foundry Local
- Strategie e implementazione BYOM (Bring-your-own-model)
- Approfondimenti della serie Model Mondays e contributi della comunità
- Distribuzione e ottimizzazione di modelli personalizzati
- Criteri di valutazione e selezione dei modelli della comunità

**Durata**: 2-3 ore  
**Prerequisiti**: Completamento delle Sessioni 1-2, account Hugging Face

---

### [4: Esplora Modelli Avanzati - LLM, SLM e Inferenza su Dispositivo](./04.CuttingEdgeModels.md)
**Focus**: Confronto tra modelli, EdgeAI con Phi e ONNX Runtime, demo avanzati

**Cosa Imparerai:**
- Confronto completo tra LLM e SLM e casi d'uso
- Compromessi tra inferenza locale e cloud e framework decisionali
- Implementazione EdgeAI con Phi e ONNX Runtime
- Sviluppo e distribuzione dell'app Chainlit RAG Chat
- Tecniche di ottimizzazione dell'inferenza WebGPU
- Integrazione e capacità dell'SDK AI PC

**Durata**: 3-4 ore  
**Prerequisiti**: Completamento delle Sessioni 1-3, comprensione dei concetti di inferenza

---

### [5: Creare Agenti AI Rapidamente con Foundry Local](./05.AIPoweredAgents.md)
**Focus**: Sviluppo rapido di app GenAI, prompt di sistema, grounding e architetture di agenti

**Cosa Imparerai:**
- Architettura e modelli di progettazione degli agenti di Foundry Local
- Tecniche di prompt di sistema per il comportamento degli agenti
- Tecniche di grounding per risposte affidabili degli agenti
- Workflow di sviluppo rapido di applicazioni GenAI
- Orchestrazione di agenti e sistemi multi-agente
- Strategie di distribuzione in produzione per agenti AI

**Durata**: 3-4 ore  
**Prerequisiti**: Completamento delle Sessioni 1-4, comprensione di base degli agenti AI

---

### [6: Foundry Local - Modelli come Strumenti](./06.ModelsAsTools.md)
**Focus**: Soluzioni AI modulari, distribuzione su dispositivo e scalabilità aziendale

**Cosa Imparerai:**
- Trattare i modelli AI come strumenti modulari e personalizzabili
- Distribuzione su dispositivo senza dipendenza dal cloud
- Inferenza a bassa latenza, economica e rispettosa della privacy
- Modelli di integrazione SDK, API e CLI
- Personalizzazione dei modelli per casi d'uso specifici
- Strategie di scalabilità da locale ad Azure AI Foundry
- Architetture di applicazioni AI pronte per l'azienda

**Durata**: 3-4 ore  
**Prerequisiti**: Tutte le sessioni precedenti, esperienza nello sviluppo aziendale utile

## Prerequisiti

### Requisiti di Sistema
- **Sistema Operativo**: Windows 11 (22H2 o successivo)
- **Memoria**: 16GB RAM (32GB consigliati per modelli più grandi)
- **Spazio di Archiviazione**: 50GB di spazio libero per il caching dei modelli
- **Hardware**: Dispositivo con NPU consigliato (Copilot+ PC), GPU opzionale
- **Rete**: Connessione internet ad alta velocità per il download iniziale dei modelli

### Ambiente di Sviluppo
- Visual Studio Code con estensione AI Toolkit
- Python 3.10+ e pip
- Git per il controllo di versione
- PowerShell o Prompt dei Comandi
- Azure CLI (opzionale per l'integrazione cloud)

### Conoscenze Prerequisite
- Comprensione di base dei concetti AI/ML
- Familiarità con la riga di comando
- Nozioni di base di programmazione Python
- Concetti di REST API
- Conoscenza di base del prompting e dell'inferenza dei modelli

## Cronologia del Modulo

**Tempo Totale Stimato**: 15-20 ore

| Sessione | Area di Focus | Tempo | Complessità |
|----------|---------------|-------|-------------|
|  1 | Configurazione e Basi | 2-3 ore | Principiante |
|  2 | Soluzioni AI | 2-3 ore | Intermedio |
|  3 | Open Source | 2-3 ore | Intermedio |
|  4 | Modelli Avanzati | 3-4 ore | Avanzato |
|  5 | Agenti AI | 3-4 ore | Avanzato |
|  6 | Strumenti Aziendali | 3-4 ore | Esperto |

## Risorse Chiave

### Documentazione Principale
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Documentazione Azure AI Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Serie Model Mondays](https://aka.ms/model-mondays)

### Risorse della Comunità
- [Discussioni della Comunità Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Esempi Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Comunità Sviluppatori AI Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence)

## Risultati di Apprendimento

Completando questo modulo, sarai in grado di:

### Padronanza Tecnica
- **Distribuire e Gestire**: Installazioni di Foundry Local in ambienti di sviluppo e produzione
- **Integrare Modelli**: Lavorare senza problemi con famiglie di modelli diverse da Microsoft, Hugging Face e fonti della comunità
- **Creare Applicazioni**: Sviluppare applicazioni AI pronte per la produzione con funzionalità avanzate e ottimizzazioni
- **Sviluppare Agenti**: Implementare agenti AI sofisticati con grounding, ragionamento e integrazione di strumenti

### Comprensione Strategica
- **Decisioni Architetturali**: Fare scelte informate tra distribuzione locale e cloud
- **Ottimizzazione delle Prestazioni**: Ottimizzare le prestazioni di inferenza su diverse configurazioni hardware
- **Scalabilità Aziendale**: Progettare applicazioni che scalano da prototipi locali a distribuzioni aziendali
- **Privacy e Sicurezza**: Implementare soluzioni AI rispettose della privacy con inferenza locale

### Capacità di Innovazione
- **Prototipazione Rapida**: Creare e testare rapidamente concetti di applicazioni AI
- **Integrazione Comunitaria**: Sfruttare modelli open-source e contribuire all'ecosistema
- **Modelli Avanzati**: Implementare modelli AI all'avanguardia, inclusi RAG, agenti e integrazione di strumenti
- **Sviluppo Pronto per il Futuro**: Creare applicazioni pronte per tecnologie e modelli AI emergenti

## Come Iniziare

1. **Prepara il Tuo Ambiente**: Assicurati di avere Windows 11 con le specifiche hardware consigliate
2. **Installa i Prerequisiti**: Configura strumenti di sviluppo e dipendenze
3. **Inizia con la Sessione 1**: Parti dall'installazione e configurazione di Foundry Local
4. **Prosegui in Ordine**: Completa le sessioni in sequenza per una progressione ottimale dell'apprendimento
5. **Pratica Continuamente**: Applica i concetti attraverso esercizi pratici e progetti

## Metriche di Successo

Monitora i tuoi progressi attraverso il modulo:

- [ ] Installare e configurare con successo Foundry Local
- [ ] Distribuire ed eseguire almeno 4 famiglie di modelli diverse
- [ ] Creare una soluzione AI completa con integrazione dei dati
- [ ] Integrare almeno 2 modelli open-source
- [ ] Creare un'applicazione chat RAG funzionale
- [ ] Sviluppare e distribuire un agente AI
- [ ] Implementare un'architettura di modelli-come-strumenti

## Avvio Rapido per Esempi

### 1) Configurazione dell'ambiente (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Avvia un modello locale (nuovo terminale)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Esegui la demo Chainlit (Sessione 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Esegui il coordinatore multi-agente (Sessione 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Se vedi errori di connessione, valida Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Configurazione del router (Sessione 6)
Il router esegue un controllo rapido dello stato e supporta la configurazione basata su ambiente:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Questo modulo rappresenta l'avanguardia dello sviluppo AI edge, combinando gli strumenti di livello aziendale di Microsoft con la flessibilità e l'innovazione dell'ecosistema open-source. Padroneggiando Foundry Local, sarai posizionato all'avanguardia dello sviluppo di applicazioni AI.

Per Azure OpenAI (Sessione 2), consulta il README di esempio per le variabili di ambiente richieste e le impostazioni della versione API.

## Panoramica degli Esempi

- `samples/01`: Chat REST rapida con Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integrazione SDK OpenAI (`sdk_quickstart.py`).
- `samples/03`: Scoperta dei modelli + benchmark rapido (`list_and_bench.cmd`).
- `samples/04`: Demo Chainlit RAG (`app.py`).
- `samples/05`: Orchestrazione multi-agente (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router Modelli-come-Strumenti (`python samples\06\router.py`).

---

