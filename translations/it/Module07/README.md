<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-18T00:09:33+00:00",
  "source_file": "Module07/README.md",
  "language_code": "it"
}
-->
# Capitolo 07: Esempi di EdgeAI

Edge AI rappresenta la convergenza tra intelligenza artificiale e edge computing, consentendo l'elaborazione intelligente direttamente sui dispositivi senza dipendere dalla connettività cloud. Questo capitolo esplora cinque implementazioni distinte di EdgeAI su diverse piattaforme e framework, mostrando la versatilità e la potenza di eseguire modelli di AI al limite.

## 1. EdgeAI su NVIDIA Jetson Orin Nano

Il NVIDIA Jetson Orin Nano rappresenta un passo avanti nell'accessibilità del computing Edge AI, offrendo fino a 67 TOPS di prestazioni AI in un formato compatto delle dimensioni di una carta di credito. Questa potente piattaforma Edge AI democratizza lo sviluppo di AI generativa per hobbisti, studenti e sviluppatori professionisti.

### Caratteristiche principali
- Offre fino a 67 TOPS di prestazioni AI—un miglioramento di 1,7 volte rispetto al suo predecessore
- 1024 core CUDA e fino a 32 Tensor Core per l'elaborazione AI
- CPU Arm Cortex-A78AE v8.2 a 6 core a 64 bit con frequenza massima di 1,5 GHz
- Prezzo di soli $249, fornendo agli sviluppatori, studenti e maker la piattaforma più accessibile ed economica

### Applicazioni
Il Jetson Orin Nano eccelle nell'esecuzione di moderni modelli di AI generativa, inclusi i vision transformers, i modelli di linguaggio di grandi dimensioni e i modelli visione-linguaggio. È progettato specificamente per casi d'uso di AI generativa e ora è possibile eseguire diversi LLM su un dispositivo palmare. I casi d'uso più comuni includono robotica alimentata da AI, droni intelligenti, telecamere intelligenti e dispositivi autonomi edge.

**Scopri di più**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI nelle applicazioni mobili con .NET MAUI e ONNX Runtime GenAI

Questa soluzione dimostra come integrare AI generativa e modelli di linguaggio di grandi dimensioni (LLM) nelle applicazioni mobili multipiattaforma utilizzando .NET MAUI (Multi-platform App UI) e ONNX Runtime GenAI. Questo approccio consente agli sviluppatori .NET di creare applicazioni mobili sofisticate alimentate da AI che funzionano nativamente su dispositivi Android e iOS.

### Caratteristiche principali
- Basato sul framework .NET MAUI, che fornisce un unico codice per applicazioni Android e iOS
- Integrazione di ONNX Runtime GenAI per eseguire modelli di AI generativa direttamente sui dispositivi mobili
- Supporta vari acceleratori hardware specifici per dispositivi mobili, inclusi CPU, GPU e processori AI specializzati
- Ottimizzazioni specifiche per piattaforma come CoreML per iOS e NNAPI per Android tramite ONNX Runtime
- Implementa l'intero ciclo di AI generativa, inclusi pre e post processing, inferenza, elaborazione dei logits, ricerca e campionamento, e gestione della cache KV

### Vantaggi dello sviluppo
L'approccio .NET MAUI consente agli sviluppatori di sfruttare le loro competenze esistenti in C# e .NET mentre costruiscono applicazioni AI multipiattaforma. Il framework ONNX Runtime GenAI supporta molteplici architetture di modelli, inclusi Llama, Mistral, Phi, Gemma e molti altri. I kernel ARM64 ottimizzati accelerano la moltiplicazione di matrici quantizzate INT4, garantendo prestazioni efficienti sull'hardware mobile mantenendo l'esperienza di sviluppo familiare di .NET.

### Casi d'uso
Questa soluzione è ideale per gli sviluppatori che desiderano creare applicazioni mobili alimentate da AI utilizzando tecnologie .NET, inclusi chatbot intelligenti, app di riconoscimento immagini, strumenti di traduzione linguistica e sistemi di raccomandazione personalizzati che funzionano interamente sul dispositivo per una maggiore privacy e capacità offline.

**Scopri di più**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI su Azure con Small Language Models Engine

La soluzione EdgeAI basata su Azure di Microsoft si concentra sul deployment efficiente di Small Language Models (SLM) in ambienti ibridi cloud-edge. Questo approccio colma il divario tra i servizi AI su scala cloud e i requisiti di deployment edge.

### Vantaggi dell'architettura
- Integrazione senza soluzione di continuità con i servizi AI di Azure
- Esecuzione di SLM/LLM e modelli multimodali su dispositivo e nel cloud con ONNX Runtime
- Ottimizzato per il deployment su scala aziendale
- Supporto per aggiornamenti e gestione continui dei modelli

### Casi d'uso
L'implementazione EdgeAI su Azure eccelle in scenari che richiedono deployment AI di livello aziendale con capacità di gestione cloud. Questo include elaborazione intelligente di documenti, analisi in tempo reale e flussi di lavoro AI ibridi che sfruttano sia il cloud che l'edge computing.

**Scopri di più**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI con Windows ML

Windows ML rappresenta il runtime all'avanguardia di Microsoft ottimizzato per l'inferenza di modelli su dispositivo e il deployment semplificato, fungendo da base per Windows AI Foundry. Questa piattaforma consente agli sviluppatori di creare applicazioni Windows alimentate da AI che sfruttano l'intero spettro dell'hardware PC.

### Capacità della piattaforma
- Funziona su tutti i PC Windows 11 con versione 24H2 (build 26100) o superiore
- Compatibile con hardware PC x64 e ARM64, anche su PC senza NPU o GPU
- Consente agli sviluppatori di portare i propri modelli e distribuirli efficacemente attraverso l'ecosistema dei partner hardware, inclusi AMD, Intel, NVIDIA e Qualcomm, su CPU, GPU, NPU
- Grazie alle API infrastrutturali, gli sviluppatori non devono più creare build multiple della loro app per target diversi hardware

### Vantaggi per gli sviluppatori
Windows ML astrae l'hardware e i provider di esecuzione, permettendoti di concentrarti sulla scrittura del codice. Inoltre, Windows ML si aggiorna automaticamente per supportare le ultime NPU, GPU e CPU man mano che vengono rilasciate. La piattaforma offre un framework unificato per lo sviluppo AI su un ecosistema hardware Windows diversificato.

**Scopri di più**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Guida completa per lo sviluppo Edge AI su Windows

## 5. EdgeAI con Foundry Local Applications

Foundry Local consente agli sviluppatori di creare applicazioni Retrieval Augmented Generation (RAG) utilizzando risorse locali in .NET, combinando modelli linguistici locali con capacità di ricerca semantica. Questo approccio offre soluzioni AI incentrate sulla privacy che operano interamente su infrastrutture locali.

### Architettura tecnica
- Combina il modello linguistico Phi-3, Local Embeddings e Semantic Kernel per creare uno scenario RAG
- Utilizza embeddings come vettori (array) di valori a virgola mobile che rappresentano il contenuto e il suo significato semantico
- Semantic Kernel funge da orchestratore principale, integrando Phi-3 e Smart Components per creare una pipeline RAG senza soluzione di continuità
- Supporto per database vettoriali locali, inclusi SQLite e Qdrant

### Vantaggi dell'implementazione
RAG, o Retrieval Augmented Generation, è semplicemente un modo elegante per dire "cerca alcune informazioni e inseriscile nel prompt". Questa implementazione locale garantisce la privacy dei dati fornendo risposte intelligenti basate su basi di conoscenza personalizzate. L'approccio è particolarmente prezioso per scenari aziendali che richiedono sovranità dei dati e capacità di operazione offline.

**Scopri di più**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Risorse per lo sviluppo EdgeAI su Windows

Per gli sviluppatori che si concentrano specificamente sulla piattaforma Windows, abbiamo creato una guida completa che copre l'intero ecosistema EdgeAI su Windows. Questa risorsa fornisce informazioni dettagliate su Windows AI Foundry, incluse API, strumenti e best practice per lo sviluppo EdgeAI su Windows.

### Piattaforma Windows AI Foundry
La piattaforma Windows AI Foundry offre una suite completa di strumenti e API progettati specificamente per lo sviluppo Edge AI su dispositivi Windows. Questo include supporto specializzato per hardware accelerato da NPU, integrazione Windows ML e tecniche di ottimizzazione specifiche per la piattaforma.

**Guida completa**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Questa guida copre:
- Panoramica e componenti della piattaforma Windows AI Foundry
- API Phi Silica per inferenza efficiente su hardware NPU
- API di Computer Vision per elaborazione immagini e OCR
- Integrazione e ottimizzazione del runtime Windows ML
- CLI Foundry Local per sviluppo e test locali
- Strategie di ottimizzazione hardware per dispositivi Windows
- Esempi pratici di implementazione e best practice

### Toolkit AI per lo sviluppo Edge AI
Per gli sviluppatori che utilizzano Visual Studio Code, l'estensione AI Toolkit offre un ambiente di sviluppo completo progettato specificamente per la creazione, il test e il deployment di applicazioni Edge AI. Questo toolkit semplifica l'intero flusso di lavoro di sviluppo Edge AI all'interno di VS Code.

**Guida allo sviluppo**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

La guida al Toolkit AI copre:
- Scoperta e selezione dei modelli per il deployment edge
- Flussi di lavoro di test e ottimizzazione locali
- Integrazione ONNX e Ollama per modelli edge
- Tecniche di conversione e quantizzazione dei modelli
- Sviluppo di agenti per scenari edge
- Valutazione delle prestazioni e monitoraggio
- Preparazione al deployment e best practice

## Conclusione

Queste cinque implementazioni di EdgeAI dimostrano la maturità e la diversità delle soluzioni AI edge disponibili oggi. Dai dispositivi edge accelerati da hardware come il Jetson Orin Nano ai framework software come ONNX Runtime GenAI e Windows ML, gli sviluppatori hanno opzioni senza precedenti per distribuire applicazioni intelligenti al limite.

Il filo conduttore tra tutte queste piattaforme è la democratizzazione delle capacità AI, rendendo l'apprendimento automatico sofisticato accessibile agli sviluppatori di diversi livelli di competenza e casi d'uso. Che si tratti di creare applicazioni mobili, software desktop o sistemi embedded, queste soluzioni EdgeAI forniscono la base per la prossima generazione di applicazioni intelligenti che operano in modo efficiente e privato al limite.

Ogni piattaforma offre vantaggi unici: Jetson Orin Nano per il computing edge accelerato da hardware, ONNX Runtime GenAI per lo sviluppo mobile multipiattaforma, Azure EdgeAI per l'integrazione cloud-edge aziendale, Windows ML per applicazioni native Windows e Foundry Local per implementazioni RAG incentrate sulla privacy. Insieme, rappresentano un ecosistema completo per lo sviluppo EdgeAI.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.