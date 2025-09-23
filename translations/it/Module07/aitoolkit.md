<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T00:20:29+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "it"
}
-->
# AI Toolkit per Visual Studio Code - Guida allo sviluppo Edge AI

## Introduzione

Benvenuto nella guida completa per utilizzare AI Toolkit per Visual Studio Code nello sviluppo Edge AI. Con l'intelligenza artificiale che si sposta dal cloud centralizzato ai dispositivi edge distribuiti, gli sviluppatori necessitano di strumenti potenti e integrati per affrontare le sfide uniche del deployment edge, come vincoli di risorse e requisiti di funzionamento offline.

AI Toolkit per Visual Studio Code colma questa lacuna fornendo un ambiente di sviluppo completo, progettato specificamente per costruire, testare e ottimizzare applicazioni AI che funzionano in modo efficiente sui dispositivi edge. Che tu stia sviluppando per sensori IoT, dispositivi mobili, sistemi embedded o server edge, questo toolkit semplifica l'intero flusso di lavoro di sviluppo all'interno dell'ambiente familiare di VS Code.

Questa guida ti accompagnerà attraverso i concetti essenziali, gli strumenti e le migliori pratiche per sfruttare AI Toolkit nei tuoi progetti Edge AI, dalla selezione iniziale del modello al deployment in produzione.

## Panoramica

AI Toolkit offre un ambiente di sviluppo integrato per l'intero ciclo di vita delle applicazioni Edge AI all'interno di VS Code. Fornisce un'integrazione fluida con modelli AI popolari di fornitori come OpenAI, Anthropic, Google e GitHub, supportando al contempo il deployment locale dei modelli tramite ONNX e Ollama - capacità cruciali per le applicazioni Edge AI che richiedono inferenza on-device.

Ciò che distingue AI Toolkit per lo sviluppo Edge AI è il suo focus sull'intera pipeline di deployment edge. A differenza degli strumenti tradizionali di sviluppo AI che si concentrano principalmente sul deployment cloud, AI Toolkit include funzionalità specializzate per l'ottimizzazione dei modelli, test in condizioni di risorse limitate e valutazione delle prestazioni specifiche per l'edge. Il toolkit comprende che lo sviluppo Edge AI richiede considerazioni diverse: dimensioni dei modelli più ridotte, tempi di inferenza più rapidi, capacità offline e ottimizzazioni hardware-specifiche.

La piattaforma supporta diversi scenari di deployment, dall'inferenza semplice on-device a complesse architetture edge multi-modello. Fornisce strumenti per la conversione, la quantizzazione e l'ottimizzazione dei modelli, essenziali per un deployment edge di successo, mantenendo al contempo la produttività degli sviluppatori che VS Code è noto per offrire.

## Obiettivi di apprendimento

Alla fine di questa guida, sarai in grado di:

### Competenze principali
- **Installare e configurare** AI Toolkit per Visual Studio Code per flussi di lavoro di sviluppo Edge AI
- **Navigare e utilizzare** l'interfaccia di AI Toolkit, inclusi Catalogo Modelli, Playground e Agent Builder
- **Selezionare e valutare** modelli AI adatti al deployment edge in base a prestazioni e vincoli di risorse
- **Convertire e ottimizzare** modelli utilizzando il formato ONNX e tecniche di quantizzazione per dispositivi edge

### Competenze di sviluppo Edge AI
- **Progettare e implementare** applicazioni Edge AI utilizzando l'ambiente di sviluppo integrato
- **Eseguire test sui modelli** in condizioni simili all'edge utilizzando inferenza locale e monitoraggio delle risorse
- **Creare e personalizzare** agenti AI ottimizzati per scenari di deployment edge
- **Valutare le prestazioni dei modelli** utilizzando metriche rilevanti per il computing edge (latenza, utilizzo della memoria, accuratezza)

### Ottimizzazione e deployment
- **Applicare tecniche di quantizzazione e pruning** per ridurre le dimensioni dei modelli mantenendo prestazioni accettabili
- **Ottimizzare i modelli** per piattaforme hardware edge specifiche, inclusa l'accelerazione tramite CPU, GPU e NPU
- **Implementare le migliori pratiche** per lo sviluppo Edge AI, inclusa la gestione delle risorse e strategie di fallback
- **Preparare modelli e applicazioni** per il deployment in produzione su dispositivi edge

### Concetti avanzati di Edge AI
- **Integrare con framework Edge AI** come ONNX Runtime, Windows ML e TensorFlow Lite
- **Implementare architetture multi-modello** e scenari di apprendimento federato per ambienti edge
- **Risolvere problemi comuni di Edge AI** come vincoli di memoria, velocità di inferenza e compatibilità hardware
- **Progettare strategie di monitoraggio e logging** per applicazioni Edge AI in produzione

### Applicazione pratica
- **Costruire soluzioni Edge AI end-to-end** dalla selezione del modello al deployment
- **Dimostrare competenza** nei flussi di lavoro di sviluppo e tecniche di ottimizzazione specifiche per l'edge
- **Applicare i concetti appresi** a casi d'uso Edge AI reali, inclusi IoT, mobile e applicazioni embedded
- **Valutare e confrontare** diverse strategie di deployment Edge AI e i loro compromessi

## Caratteristiche principali per lo sviluppo Edge AI

### 1. Catalogo Modelli e Scoperta
- **Supporto Modelli Locali**: Scopri e accedi a modelli AI ottimizzati specificamente per il deployment edge
- **Integrazione ONNX**: Accedi a modelli in formato ONNX per inferenza edge efficiente
- **Supporto Ollama**: Sfrutta modelli che funzionano localmente tramite Ollama per privacy e operazioni offline
- **Confronto Modelli**: Confronta i modelli fianco a fianco per trovare il miglior equilibrio tra prestazioni e consumo di risorse per dispositivi edge

### 2. Playground Interattivo
- **Ambiente di Test Locale**: Testa i modelli localmente prima del deployment edge
- **Esperimenti Multi-modali**: Testa con immagini, testo e altri input tipici degli scenari edge
- **Regolazione dei Parametri**: Sperimenta con diversi parametri del modello per ottimizzare i vincoli edge
- **Monitoraggio delle Prestazioni in Tempo Reale**: Osserva la velocità di inferenza e l'uso delle risorse durante lo sviluppo

### 3. Agent Builder per Applicazioni Edge
- **Prompt Engineering**: Crea prompt ottimizzati che funzionano efficientemente con modelli edge più piccoli
- **Integrazione MCP Tool**: Integra strumenti Model Context Protocol per capacità avanzate degli agenti edge
- **Generazione di Codice**: Genera codice pronto per la produzione ottimizzato per scenari di deployment edge
- **Output Strutturati**: Progetta agenti che forniscono risposte coerenti e strutturate adatte alle applicazioni edge

### 4. Valutazione e Test dei Modelli
- **Metriche di Prestazione**: Valuta i modelli utilizzando metriche rilevanti per il deployment edge (latenza, utilizzo della memoria, accuratezza)
- **Test Batch**: Testa simultaneamente più configurazioni di modelli per trovare impostazioni edge ottimali
- **Valutazione Personalizzata**: Crea criteri di valutazione personalizzati specifici per i casi d'uso Edge AI
- **Profilazione delle Risorse**: Analizza i requisiti di memoria e calcolo per la pianificazione del deployment edge

### 5. Conversione e Ottimizzazione dei Modelli
- **Conversione ONNX**: Converti modelli da vari formati a ONNX per compatibilità edge
- **Quantizzazione**: Riduci le dimensioni dei modelli e migliora la velocità di inferenza tramite tecniche di quantizzazione
- **Ottimizzazione Hardware**: Ottimizza i modelli per hardware edge specifico (CPU, GPU, NPU)
- **Trasformazione del Formato**: Trasforma modelli da Hugging Face e altre fonti per il deployment edge

### 6. Fine-tuning per Scenari Edge
- **Adattamento al Dominio**: Personalizza i modelli per casi d'uso e ambienti edge specifici
- **Training Locale**: Allena i modelli localmente con supporto GPU per requisiti specifici dell'edge
- **Integrazione Azure**: Sfrutta Azure Container Apps per il fine-tuning basato su cloud prima del deployment edge
- **Transfer Learning**: Adatta modelli pre-addestrati per compiti e vincoli specifici dell'edge

### 7. Monitoraggio delle Prestazioni e Tracing
- **Analisi delle Prestazioni Edge**: Monitora le prestazioni dei modelli in condizioni simili all'edge
- **Raccolta Tracing**: Raccogli dati dettagliati sulle prestazioni per l'ottimizzazione
- **Identificazione dei Collo di Bottiglia**: Identifica problemi di prestazioni prima del deployment sui dispositivi edge
- **Monitoraggio dell'Uso delle Risorse**: Monitora memoria, CPU e tempi di inferenza per l'ottimizzazione edge

## Flusso di lavoro per lo sviluppo Edge AI

### Fase 1: Scoperta e Selezione del Modello
1. **Esplora il Catalogo Modelli**: Usa il catalogo modelli per trovare modelli adatti al deployment edge
2. **Confronta le Prestazioni**: Valuta i modelli in base a dimensioni, accuratezza e velocità di inferenza
3. **Testa Localmente**: Usa modelli Ollama o ONNX per test locali prima del deployment edge
4. **Valuta i Requisiti di Risorse**: Determina le esigenze di memoria e calcolo per i dispositivi edge target

### Fase 2: Ottimizzazione del Modello
1. **Converti in ONNX**: Converti i modelli selezionati in formato ONNX per compatibilità edge
2. **Applica Quantizzazione**: Riduci le dimensioni dei modelli tramite quantizzazione INT8 o INT4
3. **Ottimizzazione Hardware**: Ottimizza per hardware edge target (ARM, x86, acceleratori specializzati)
4. **Validazione delle Prestazioni**: Valida che i modelli ottimizzati mantengano un'accuratezza accettabile

### Fase 3: Sviluppo dell'Applicazione
1. **Progettazione degli Agenti**: Usa Agent Builder per creare agenti AI ottimizzati per l'edge
2. **Prompt Engineering**: Sviluppa prompt che funzionano efficacemente con modelli più piccoli
3. **Test di Integrazione**: Testa gli agenti in condizioni simulate edge
4. **Generazione di Codice**: Genera codice di produzione ottimizzato per il deployment edge

### Fase 4: Valutazione e Test
1. **Valutazione Batch**: Testa più configurazioni per trovare impostazioni edge ottimali
2. **Profilazione delle Prestazioni**: Analizza velocità di inferenza, utilizzo della memoria e accuratezza
3. **Simulazione Edge**: Testa in condizioni simili all'ambiente di deployment edge target
4. **Stress Testing**: Valuta le prestazioni sotto varie condizioni di carico

### Fase 5: Preparazione al Deployment
1. **Ottimizzazione Finale**: Applica ottimizzazioni finali basate sui risultati dei test
2. **Packaging per il Deployment**: Prepara modelli e codice per il deployment edge
3. **Documentazione**: Documenta i requisiti di deployment e configurazione
4. **Setup del Monitoraggio**: Prepara il monitoraggio e il logging per il deployment in produzione

## Pubblico target per lo sviluppo Edge AI

### Sviluppatori Edge AI
- Sviluppatori di applicazioni che costruiscono dispositivi edge e soluzioni IoT alimentate da AI
- Sviluppatori di sistemi embedded che integrano capacità AI in dispositivi con risorse limitate
- Sviluppatori mobili che creano applicazioni AI on-device per smartphone e tablet

### Ingegneri Edge AI
- Ingegneri AI che ottimizzano modelli per il deployment edge e gestiscono pipeline di inferenza
- Ingegneri DevOps che distribuiscono e gestiscono modelli AI su infrastrutture edge distribuite
- Ingegneri delle prestazioni che ottimizzano carichi di lavoro AI per vincoli hardware edge

### Ricercatori ed Educatori
- Ricercatori AI che sviluppano modelli e algoritmi efficienti per il computing edge
- Educatori che insegnano concetti Edge AI e dimostrano tecniche di ottimizzazione
- Studenti che apprendono le sfide e le soluzioni nel deployment Edge AI

## Casi d'uso Edge AI

### Dispositivi IoT intelligenti
- **Riconoscimento immagini in tempo reale**: Deployment di modelli di visione artificiale su telecamere e sensori IoT
- **Elaborazione vocale**: Implementazione di riconoscimento vocale e elaborazione del linguaggio naturale su altoparlanti intelligenti
- **Manutenzione predittiva**: Esecuzione di modelli di rilevamento anomalie su dispositivi edge industriali
- **Monitoraggio ambientale**: Deployment di modelli di analisi dei dati dei sensori per applicazioni ambientali

### Applicazioni mobili e embedded
- **Traduzione on-device**: Implementazione di modelli di traduzione linguistica che funzionano offline
- **Realtà aumentata**: Deployment di riconoscimento e tracciamento oggetti in tempo reale per applicazioni AR
- **Monitoraggio della salute**: Esecuzione di modelli di analisi della salute su dispositivi indossabili e attrezzature mediche
- **Sistemi autonomi**: Implementazione di modelli decisionali per droni, robot e veicoli

### Infrastruttura Edge Computing
- **Data center edge**: Deployment di modelli AI nei data center edge per applicazioni a bassa latenza
- **Integrazione CDN**: Integrazione di capacità di elaborazione AI nelle reti di distribuzione dei contenuti
- **Edge 5G**: Sfruttamento del computing edge 5G per applicazioni alimentate da AI
- **Fog Computing**: Implementazione di elaborazione AI in ambienti di fog computing

## Installazione e configurazione

### Installazione rapida
Installa l'estensione AI Toolkit direttamente dal Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Prerequisiti per lo sviluppo Edge AI
- **ONNX Runtime**: Installa ONNX Runtime per l'inferenza dei modelli
- **Ollama** (Opzionale): Installa Ollama per il servizio locale dei modelli
- **Ambiente Python**: Configura Python con le librerie AI richieste
- **Strumenti hardware edge**: Installa strumenti di sviluppo specifici per hardware (CUDA, OpenVINO, ecc.)

### Configurazione iniziale
1. Apri VS Code e installa l'estensione AI Toolkit
2. Configura le fonti dei modelli (ONNX, Ollama, fornitori cloud)
3. Configura l'ambiente di sviluppo locale per i test edge
4. Configura le opzioni di accelerazione hardware per la tua macchina di sviluppo

## Iniziare con lo sviluppo Edge AI

### Passo 1: Selezione del Modello
1. Apri la vista AI Toolkit nella barra delle attività
2. Sfoglia il Catalogo Modelli per modelli compatibili con l'edge
3. Filtra per dimensioni del modello, formato (ONNX) e caratteristiche di prestazione
4. Confronta i modelli utilizzando gli strumenti di confronto integrati

### Passo 2: Test Locale
1. Usa il Playground per testare i modelli selezionati localmente
2. Sperimenta con diversi prompt e parametri
3. Monitora le metriche di prestazione durante i test
4. Valuta le risposte dei modelli per i requisiti dei casi d'uso edge

### Passo 3: Ottimizzazione del Modello
1. Usa gli strumenti di conversione dei modelli per ottimizzare il deployment edge
2. Applica la quantizzazione per ridurre le dimensioni del modello
3. Testa i modelli ottimizzati per garantire prestazioni accettabili
4. Documenta le impostazioni di ottimizzazione e i compromessi di prestazione

### Passo 4: Sviluppo degli Agenti
1. Usa Agent Builder per creare agenti AI ottimizzati per l'edge
2. Sviluppa prompt che funzionano efficacemente con modelli più piccoli
3. Integra strumenti e API necessari per scenari edge
4. Testa gli agenti in condizioni simulate edge

### Passo 5: Valutazione e Deployment
1. Usa la valutazione bulk per testare più configurazioni
2. Profila le prestazioni in varie condizioni
3. Prepara pacchetti di deployment per dispositivi edge target
4. Configura il monitoraggio e il logging per il deployment in produzione

## Migliori pratiche per lo sviluppo Edge AI

### Selezione del Modello
- **Vincoli di dimensioni**: Scegli modelli che si adattino ai limiti di memoria dei dispositivi target
- **Velocità di inferenza**: Dai priorità a modelli con tempi di inferenza rapidi per applicazioni in tempo reale
- **Compromessi di accuratezza**: Bilancia l'accuratezza del modello con i vincoli di risorse
- **Compatibilità del formato**: Preferisci formati ONNX o ottimizzati per hardware per il deployment edge

### Tecniche di Ottimizzazione
- **Quantizzazione**: Usa la quantizzazione INT8 o INT4 per ridurre le dimensioni del modello e migliorare la velocità
- **Pruning**: Rimuovi parametri del modello non necessari per ridurre i requisiti computazionali
- **Distillazione della conoscenza**: Crea modelli più piccoli che mantengano le prestazioni di quelli più grandi
- **Accelerazione hardware**: Sfrutta NPUs, GPUs o acceleratori specializzati quando disponibili

### Flusso di lavoro di sviluppo
- **Test iterativi**: Testa frequentemente in condizioni simili all'edge durante lo sviluppo
- **Monitoraggio delle prestazioni**: Monitora continuamente l'uso delle risorse e la velocità di inferenza
- **Controllo delle versioni**: Tieni traccia delle versioni dei modelli e delle impostazioni di ottimizzazione
- **Documentazione**: Documenta tutte le
- **Sicurezza**: Implementare misure di sicurezza adeguate per le applicazioni AI edge

## Integrazione con Framework Edge AI

### ONNX Runtime
- **Distribuzione Cross-platform**: Distribuire modelli ONNX su diverse piattaforme edge
- **Ottimizzazione Hardware**: Sfruttare le ottimizzazioni specifiche per hardware di ONNX Runtime
- **Supporto Mobile**: Utilizzare ONNX Runtime Mobile per applicazioni su smartphone e tablet
- **Integrazione IoT**: Distribuire su dispositivi IoT utilizzando le distribuzioni leggere di ONNX Runtime

### Windows ML
- **Dispositivi Windows**: Ottimizzare per dispositivi edge e PC basati su Windows
- **Accelerazione NPU**: Sfruttare le Neural Processing Units sui dispositivi Windows
- **DirectML**: Utilizzare DirectML per l'accelerazione GPU su piattaforme Windows
- **Integrazione UWP**: Integrare con applicazioni della Universal Windows Platform

### TensorFlow Lite
- **Ottimizzazione Mobile**: Distribuire modelli TensorFlow Lite su dispositivi mobili e embedded
- **Delegati Hardware**: Utilizzare delegati hardware specializzati per l'accelerazione
- **Microcontrollori**: Distribuire su microcontrollori utilizzando TensorFlow Lite Micro
- **Supporto Cross-platform**: Distribuire su Android, iOS e sistemi Linux embedded

### Azure IoT Edge
- **Ibrido Cloud-Edge**: Combinare l'addestramento in cloud con l'inferenza edge
- **Distribuzione Moduli**: Distribuire modelli AI come moduli IoT Edge
- **Gestione Dispositivi**: Gestire dispositivi edge e aggiornamenti dei modelli da remoto
- **Telemetria**: Raccogliere dati sulle prestazioni e metriche dei modelli dalle distribuzioni edge

## Scenari Avanzati di Edge AI

### Distribuzione Multi-Modello
- **Ensemble di Modelli**: Distribuire più modelli per migliorare l'accuratezza o la ridondanza
- **Test A/B**: Testare diversi modelli simultaneamente sui dispositivi edge
- **Selezione Dinamica**: Scegliere i modelli in base alle condizioni attuali del dispositivo
- **Condivisione Risorse**: Ottimizzare l'uso delle risorse tra più modelli distribuiti

### Federated Learning
- **Addestramento Distribuito**: Addestrare modelli su più dispositivi edge
- **Preservazione della Privacy**: Mantenere i dati di addestramento locali condividendo solo i miglioramenti del modello
- **Apprendimento Collaborativo**: Consentire ai dispositivi di apprendere dalle esperienze collettive
- **Coordinazione Edge-Cloud**: Coordinare l'apprendimento tra dispositivi edge e infrastruttura cloud

### Elaborazione in Tempo Reale
- **Elaborazione di Flussi**: Elaborare flussi di dati continui sui dispositivi edge
- **Inferenza a Bassa Latenza**: Ottimizzare per una latenza minima nell'inferenza
- **Elaborazione Batch**: Elaborare efficientemente batch di dati sui dispositivi edge
- **Elaborazione Adattiva**: Adattare l'elaborazione in base alle capacità attuali del dispositivo

## Risoluzione dei Problemi nello Sviluppo Edge AI

### Problemi Comuni
- **Vincoli di Memoria**: Modello troppo grande per la memoria del dispositivo target
- **Velocità di Inferenza**: Inferenza del modello troppo lenta per i requisiti in tempo reale
- **Degradazione dell'Accuratezza**: L'ottimizzazione riduce l'accuratezza del modello in modo inaccettabile
- **Compatibilità Hardware**: Modello non compatibile con l'hardware target

### Strategie di Debugging
- **Profilazione delle Prestazioni**: Utilizzare le funzionalità di tracciamento dell'AI Toolkit per identificare i colli di bottiglia
- **Monitoraggio delle Risorse**: Monitorare l'uso di memoria e CPU durante lo sviluppo
- **Test Incrementale**: Testare le ottimizzazioni in modo incrementale per isolare i problemi
- **Simulazione Hardware**: Utilizzare strumenti di sviluppo per simulare l'hardware target

### Soluzioni di Ottimizzazione
- **Quantizzazione Ulteriore**: Applicare tecniche di quantizzazione più aggressive
- **Architettura del Modello**: Considerare diverse architetture di modelli ottimizzate per l'edge
- **Ottimizzazione della Pre-elaborazione**: Ottimizzare la pre-elaborazione dei dati per i vincoli edge
- **Ottimizzazione dell'Inferenza**: Utilizzare ottimizzazioni specifiche per l'hardware nell'inferenza

## Risorse e Prossimi Passi

### Documentazione
- [Guida ai Modelli AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/models)
- [Documentazione Model Playground](https://code.visualstudio.com/docs/intelligentapps/playground)
- [Documentazione ONNX Runtime](https://onnxruntime.ai/)
- [Documentazione Windows ML](https://docs.microsoft.com/en-us/windows/ai/)

### Comunità e Supporto
- [GitHub AI Toolkit per VS Code](https://github.com/microsoft/vscode-ai-toolkit)
- [Comunità ONNX](https://github.com/onnx/onnx)
- [Comunità Sviluppatori Edge AI](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [Marketplace Estensioni VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Risorse di Apprendimento
- [Corso Fondamenti di Edge AI](./Module01/README.md)
- [Guida ai Modelli Linguistici Piccoli](./Module02/README.md)
- [Strategie di Distribuzione Edge](./Module03/README.md)
- [Sviluppo Edge AI su Windows](./windowdeveloper.md)

## Conclusione

AI Toolkit per Visual Studio Code offre una piattaforma completa per lo sviluppo di Edge AI, dalla scoperta e ottimizzazione dei modelli alla distribuzione e monitoraggio. Sfruttando i suoi strumenti e flussi di lavoro integrati, gli sviluppatori possono creare, testare e distribuire applicazioni AI che funzionano efficacemente su dispositivi edge con risorse limitate.

Il supporto del toolkit per ONNX, Ollama e vari provider cloud, combinato con le sue capacità di ottimizzazione e valutazione, lo rende una scelta ideale per lo sviluppo di Edge AI. Che si tratti di costruire applicazioni IoT, funzionalità AI mobili o sistemi di intelligenza embedded, AI Toolkit fornisce gli strumenti e i flussi di lavoro necessari per una distribuzione Edge AI di successo.

Con l'evoluzione continua dell'Edge AI, AI Toolkit per VS Code rimane all'avanguardia, offrendo agli sviluppatori strumenti e capacità all'avanguardia per costruire la prossima generazione di applicazioni intelligenti edge.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.