<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:33:08+00:00",
  "source_file": "Module07/README.md",
  "language_code": "it"
}
-->
# Capitolo 07: Esempi di EdgeAI

Edge AI rappresenta la convergenza tra intelligenza artificiale e edge computing, consentendo l'elaborazione intelligente direttamente sui dispositivi senza dipendere dalla connettività cloud. Questo capitolo esplora cinque implementazioni distinte di EdgeAI su diverse piattaforme e framework, mostrando la versatilità e la potenza di eseguire modelli di AI al margine.

## 1. EdgeAI su NVIDIA Jetson Orin Nano

Il NVIDIA Jetson Orin Nano rappresenta un passo avanti nell'ambito del computing AI al margine, offrendo fino a 67 TOPS di prestazioni AI in un formato compatto delle dimensioni di una carta di credito. Questa potente piattaforma Edge AI democratizza lo sviluppo di AI generativa per hobbisti, studenti e sviluppatori professionisti.

### Caratteristiche principali
- Offre fino a 67 TOPS di prestazioni AI—un miglioramento del 1,7X rispetto al suo predecessore
- 1024 core CUDA e fino a 32 Tensor Core per l'elaborazione AI
- CPU Arm Cortex-A78AE v8.2 a 6 core a 64 bit con frequenza massima di 1,5 GHz
- Prezzo di soli $249, rendendo la piattaforma accessibile e conveniente per sviluppatori, studenti e creatori

### Applicazioni
Il Jetson Orin Nano eccelle nell'esecuzione di modelli AI generativi moderni, inclusi i vision transformer, i modelli di linguaggio di grandi dimensioni e i modelli visione-linguaggio. È progettato specificamente per casi d'uso GenAI e consente di eseguire diversi LLM su un dispositivo palmare. Casi d'uso popolari includono robotica alimentata da AI, droni intelligenti, telecamere intelligenti e dispositivi autonomi al margine.

**Scopri di più**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI nelle applicazioni mobili con .NET MAUI e ONNX Runtime GenAI

Questa soluzione dimostra come integrare AI generativa e modelli di linguaggio di grandi dimensioni (LLM) nelle applicazioni mobili multipiattaforma utilizzando .NET MAUI (Multi-platform App UI) e ONNX Runtime GenAI. Questo approccio consente agli sviluppatori .NET di creare applicazioni mobili sofisticate alimentate da AI che funzionano nativamente su dispositivi Android e iOS.

### Caratteristiche principali
- Basato sul framework .NET MAUI, che offre un unico codice sorgente per applicazioni Android e iOS
- Integrazione di ONNX Runtime GenAI per eseguire modelli AI generativi direttamente sui dispositivi mobili
- Supporta vari acceleratori hardware specifici per dispositivi mobili, inclusi CPU, GPU e processori AI mobili specializzati
- Ottimizzazioni specifiche per piattaforma come CoreML per iOS e NNAPI per Android tramite ONNX Runtime
- Implementa l'intero ciclo di AI generativa, inclusi pre e post processing, inferenza, elaborazione dei logits, ricerca e campionamento, e gestione della cache KV

### Vantaggi per gli sviluppatori
L'approccio .NET MAUI consente agli sviluppatori di sfruttare le loro competenze esistenti in C# e .NET mentre costruiscono applicazioni AI multipiattaforma. Il framework ONNX Runtime GenAI supporta molteplici architetture di modelli, tra cui Llama, Mistral, Phi, Gemma e altri. I kernel ARM64 ottimizzati accelerano la moltiplicazione di matrici quantizzate INT4, garantendo prestazioni efficienti sull'hardware mobile mantenendo l'esperienza di sviluppo familiare di .NET.

### Casi d'uso
Questa soluzione è ideale per gli sviluppatori che desiderano creare applicazioni mobili alimentate da AI utilizzando tecnologie .NET, inclusi chatbot intelligenti, app di riconoscimento immagini, strumenti di traduzione linguistica e sistemi di raccomandazione personalizzati che funzionano interamente sul dispositivo per una maggiore privacy e capacità offline.

**Scopri di più**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI su Azure con Small Language Models Engine

La soluzione EdgeAI basata su Azure di Microsoft si concentra sulla distribuzione efficiente di Small Language Models (SLM) in ambienti ibridi cloud-edge. Questo approccio colma il divario tra i servizi AI su scala cloud e i requisiti di distribuzione al margine.

### Vantaggi dell'architettura
- Integrazione senza soluzione di continuità con i servizi AI di Azure
- Esecuzione di SLM/LLM e modelli multimodali su dispositivo e nel cloud con ONNX Runtime
- Ottimizzato per distribuzioni su scala aziendale
- Supporto per aggiornamenti e gestione continui dei modelli

### Casi d'uso
L'implementazione EdgeAI di Azure eccelle in scenari che richiedono distribuzioni AI di livello aziendale con capacità di gestione cloud. Questo include elaborazione intelligente di documenti, analisi in tempo reale e flussi di lavoro AI ibridi che sfruttano sia le risorse cloud che quelle al margine.

**Scopri di più**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI con Windows ML](./windowdeveloper.md)

Windows ML rappresenta il runtime all'avanguardia di Microsoft ottimizzato per l'inferenza di modelli su dispositivo e la distribuzione semplificata, fungendo da base per Windows AI Foundry. Questa piattaforma consente agli sviluppatori di creare applicazioni Windows alimentate da AI che sfruttano l'intero spettro dell'hardware PC.

### Capacità della piattaforma
- Funziona su tutti i PC Windows 11 con versione 24H2 (build 26100) o superiore
- Compatibile con hardware PC x64 e ARM64, anche su PC senza NPU o GPU
- Consente agli sviluppatori di portare i propri modelli e distribuirli efficacemente attraverso l'ecosistema di partner hardware, inclusi AMD, Intel, NVIDIA e Qualcomm, su CPU, GPU, NPU
- Grazie alle API infrastrutturali, gli sviluppatori non devono più creare build multiple della loro app per target diversi

### Vantaggi per gli sviluppatori
Windows ML astrae l'hardware e i provider di esecuzione, permettendoti di concentrarti sulla scrittura del codice. Inoltre, Windows ML si aggiorna automaticamente per supportare le ultime NPU, GPU e CPU man mano che vengono rilasciate. La piattaforma offre un framework unificato per lo sviluppo AI attraverso il variegato ecosistema hardware di Windows.

**Scopri di più**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md) - Guida completa per lo sviluppo di Edge AI su Windows

## [5. EdgeAI con Foundry Local Applications](./foundrylocal.md)

Foundry Local consente agli sviluppatori Windows e Mac di creare applicazioni RAG (Retrieval Augmented Generation) utilizzando risorse locali in .NET, combinando modelli linguistici locali con capacità di ricerca semantica. Questo approccio offre soluzioni AI incentrate sulla privacy che operano interamente su infrastrutture locali.

### Architettura tecnica
- Combina il modello linguistico Phi, gli embeddings locali e il Semantic Kernel per creare uno scenario RAG
- Utilizza embeddings come vettori (array) di valori a virgola mobile che rappresentano contenuti e il loro significato semantico
- Semantic Kernel funge da orchestratore principale, integrando Phi e Smart Components per creare una pipeline RAG fluida
- Supporto per database vettoriali locali, inclusi SQLite e Qdrant

### Vantaggi dell'implementazione
RAG, o Retrieval Augmented Generation, è semplicemente un modo per dire "cerca alcune informazioni e inseriscile nel prompt". Questa implementazione locale garantisce la privacy dei dati fornendo risposte intelligenti basate su basi di conoscenza personalizzate. L'approccio è particolarmente utile per scenari aziendali che richiedono sovranità dei dati e capacità di operazione offline.

**Scopri di più**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local offre un server REST compatibile con OpenAI alimentato da ONNX Runtime per eseguire modelli localmente su Windows. Di seguito un riepilogo rapido e validato; consulta la documentazione ufficiale per i dettagli completi.

- Per iniziare: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architettura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Riferimento CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Guida completa per Windows in questo repository: [foundrylocal.md](./foundrylocal.md)

Installa o aggiorna su Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Esplora categorie CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Esegui un modello e scopri l'endpoint dinamico:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Controllo REST rapido per elencare i modelli (sostituisci PORT da status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Suggerimenti:
- Integrazione SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Porta il tuo modello (compilazione): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Risorse per lo sviluppo di EdgeAI su Windows

Per gli sviluppatori che si concentrano specificamente sulla piattaforma Windows, abbiamo creato una guida completa che copre l'intero ecosistema Windows EdgeAI. Questa risorsa fornisce informazioni dettagliate su Windows AI Foundry, incluse API, strumenti e best practice per lo sviluppo di EdgeAI su Windows.

### Piattaforma Windows AI Foundry
La piattaforma Windows AI Foundry offre una suite completa di strumenti e API progettati specificamente per lo sviluppo AI al margine su dispositivi Windows. Questo include supporto specializzato per hardware accelerato da NPU, integrazione Windows ML e tecniche di ottimizzazione specifiche per piattaforma.

**Guida completa**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Questa guida copre:
- Panoramica e componenti della piattaforma Windows AI Foundry
- API Phi Silica per inferenza efficiente su hardware NPU
- API di Computer Vision per elaborazione immagini e OCR
- Integrazione e ottimizzazione del runtime Windows ML
- CLI Foundry Local per sviluppo e test locali
- Strategie di ottimizzazione hardware per dispositivi Windows
- Esempi pratici di implementazione e best practice

### [AI Toolkit per lo sviluppo di Edge AI](./aitoolkit.md)
Per gli sviluppatori che utilizzano Visual Studio Code, l'estensione AI Toolkit offre un ambiente di sviluppo completo progettato specificamente per la creazione, il test e la distribuzione di applicazioni Edge AI. Questo toolkit semplifica l'intero flusso di lavoro di sviluppo Edge AI all'interno di VS Code.

**Guida allo sviluppo**: [AI Toolkit per lo sviluppo di Edge AI](./aitoolkit.md)

La guida AI Toolkit copre:
- Scoperta e selezione dei modelli per la distribuzione al margine
- Flussi di lavoro di test e ottimizzazione locali
- Integrazione ONNX e Ollama per modelli al margine
- Tecniche di conversione e quantizzazione dei modelli
- Sviluppo di agenti per scenari al margine
- Valutazione delle prestazioni e monitoraggio
- Preparazione alla distribuzione e best practice

## Conclusione

Queste cinque implementazioni di EdgeAI dimostrano la maturità e la diversità delle soluzioni AI al margine disponibili oggi. Dai dispositivi edge accelerati da hardware come il Jetson Orin Nano ai framework software come ONNX Runtime GenAI e Windows ML, gli sviluppatori hanno opzioni senza precedenti per distribuire applicazioni intelligenti al margine.

Il filo conduttore tra tutte queste piattaforme è la democratizzazione delle capacità AI, rendendo accessibile lo sviluppo di machine learning sofisticato agli sviluppatori di diversi livelli di competenza e casi d'uso. Che si tratti di creare applicazioni mobili, software desktop o sistemi embedded, queste soluzioni EdgeAI forniscono la base per la prossima generazione di applicazioni intelligenti che operano in modo efficiente e privato al margine.

Ogni piattaforma offre vantaggi unici: Jetson Orin Nano per il computing edge accelerato da hardware, ONNX Runtime GenAI per lo sviluppo mobile multipiattaforma, Azure EdgeAI per l'integrazione cloud-edge aziendale, Windows ML per applicazioni native Windows e Foundry Local per implementazioni RAG incentrate sulla privacy. Insieme, rappresentano un ecosistema completo per lo sviluppo di EdgeAI.

---

