<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T12:37:08+00:00",
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

AI Toolkit per Visual Studio Code è un'estensione potente che semplifica lo sviluppo di agenti e la creazione di applicazioni AI. Il toolkit offre capacità complete per esplorare, valutare e distribuire modelli AI da una vasta gamma di fornitori—tra cui Anthropic, OpenAI, GitHub, Google—supportando al contempo l'esecuzione locale dei modelli utilizzando ONNX e Ollama.

Ciò che distingue AI Toolkit è il suo approccio completo all'intero ciclo di vita dello sviluppo AI. A differenza degli strumenti tradizionali che si concentrano su singoli aspetti, AI Toolkit fornisce un ambiente integrato che copre la scoperta dei modelli, la sperimentazione, lo sviluppo di agenti, la valutazione e il deployment—tutto all'interno dell'ambiente familiare di VS Code.

La piattaforma è progettata specificamente per il prototipaggio rapido e il deployment in produzione, con funzionalità come generazione di prompt, avviatori rapidi, integrazioni fluide con MCP (Model Context Protocol) e ampie capacità di valutazione. Per lo sviluppo Edge AI, questo significa che puoi sviluppare, testare e ottimizzare applicazioni AI per scenari di deployment edge in modo efficiente, mantenendo l'intero flusso di lavoro di sviluppo all'interno di VS Code.

## Obiettivi di apprendimento

Alla fine di questa guida, sarai in grado di:

### Competenze principali
- **Installare e configurare** AI Toolkit per Visual Studio Code per flussi di lavoro di sviluppo Edge AI
- **Navigare e utilizzare** l'interfaccia di AI Toolkit, inclusi Catalogo Modelli, Playground e Costruttore di Agenti
- **Selezionare e valutare** modelli AI adatti al deployment edge in base a prestazioni e vincoli di risorse
- **Convertire e ottimizzare** modelli utilizzando il formato ONNX e tecniche di quantizzazione per dispositivi edge

### Competenze di sviluppo Edge AI
- **Progettare e implementare** applicazioni Edge AI utilizzando l'ambiente di sviluppo integrato
- **Eseguire test sui modelli** in condizioni simili a quelle edge utilizzando inferenza locale e monitoraggio delle risorse
- **Creare e personalizzare** agenti AI ottimizzati per scenari di deployment edge
- **Valutare le prestazioni dei modelli** utilizzando metriche rilevanti per il calcolo edge (latenza, utilizzo della memoria, accuratezza)

### Ottimizzazione e deployment
- **Applicare tecniche di quantizzazione e pruning** per ridurre la dimensione dei modelli mantenendo prestazioni accettabili
- **Ottimizzare i modelli** per piattaforme hardware edge specifiche, inclusa l'accelerazione CPU, GPU e NPU
- **Implementare le migliori pratiche** per lo sviluppo Edge AI, inclusa la gestione delle risorse e strategie di fallback
- **Preparare modelli e applicazioni** per il deployment in produzione su dispositivi edge

### Concetti avanzati di Edge AI
- **Integrare con framework Edge AI** come ONNX Runtime, Windows ML e TensorFlow Lite
- **Implementare architetture multi-modello** e scenari di apprendimento federato per ambienti edge
- **Risolvere problemi comuni di Edge AI** come vincoli di memoria, velocità di inferenza e compatibilità hardware
- **Progettare strategie di monitoraggio e logging** per applicazioni Edge AI in produzione

### Applicazione pratica
- **Costruire soluzioni Edge AI end-to-end** dalla selezione del modello al deployment
- **Dimostrare competenza** nei flussi di lavoro di sviluppo specifici per l'edge e nelle tecniche di ottimizzazione
- **Applicare i concetti appresi** a casi d'uso reali di Edge AI, inclusi IoT, mobile e applicazioni embedded
- **Valutare e confrontare** diverse strategie di deployment Edge AI e i loro compromessi

## Funzionalità chiave per lo sviluppo Edge AI

### 1. Catalogo Modelli e Scoperta
- **Supporto multi-fornitore**: Sfoglia e accedi a modelli AI da Anthropic, OpenAI, GitHub, Google e altri fornitori
- **Integrazione modelli locali**: Scoperta semplificata di modelli ONNX e Ollama per il deployment edge
- **Modelli GitHub**: Integrazione diretta con l'hosting di modelli su GitHub per un accesso semplificato
- **Confronto modelli**: Confronta i modelli fianco a fianco per trovare il miglior equilibrio per i vincoli dei dispositivi edge

### 2. Playground Interattivo
- **Ambiente di test interattivo**: Sperimentazione rapida con le capacità dei modelli in un ambiente controllato
- **Supporto multi-modale**: Testa con immagini, testo e altri input tipici degli scenari edge
- **Sperimentazione in tempo reale**: Feedback immediato sulle risposte e prestazioni dei modelli
- **Ottimizzazione dei parametri**: Affina i parametri dei modelli per i requisiti di deployment edge

### 3. Costruttore di Prompt (Agenti)
- **Generazione di linguaggio naturale**: Genera prompt iniziali utilizzando descrizioni in linguaggio naturale
- **Raffinamento iterativo**: Migliora i prompt in base alle risposte e alle prestazioni dei modelli
- **Decomposizione dei compiti**: Suddividi compiti complessi con concatenazione di prompt e output strutturati
- **Supporto variabili**: Usa variabili nei prompt per comportamenti dinamici degli agenti
- **Generazione di codice di produzione**: Genera codice pronto per la produzione per uno sviluppo rapido delle app

### 4. Esecuzione e Valutazione in Massa
- **Test multi-modello**: Esegui più prompt su modelli selezionati simultaneamente
- **Test efficiente su larga scala**: Testa vari input e configurazioni in modo efficiente
- **Casi di test personalizzati**: Esegui agenti con casi di test per validare la funzionalità
- **Confronto delle prestazioni**: Confronta i risultati tra diversi modelli e configurazioni

### 5. Valutazione dei Modelli con Dataset
- **Metriche standard**: Testa i modelli AI utilizzando valutatori integrati (F1 score, rilevanza, somiglianza, coerenza)
- **Valutatori personalizzati**: Crea metriche di valutazione personalizzate per casi d'uso specifici
- **Integrazione dataset**: Testa i modelli contro dataset completi
- **Misurazione delle prestazioni**: Quantifica le prestazioni dei modelli per decisioni di deployment edge

### 6. Capacità di Fine-tuning
- **Personalizzazione dei modelli**: Personalizza i modelli per casi d'uso e domini specifici
- **Adattamento specializzato**: Adatta i modelli a domini e requisiti specializzati
- **Ottimizzazione per l'edge**: Affina i modelli specificamente per i vincoli di deployment edge
- **Training specifico per il dominio**: Crea modelli su misura per casi d'uso edge specifici

### 7. Integrazione con MCP Tool
- **Connettività con strumenti esterni**: Collega agenti a strumenti esterni tramite server Model Context Protocol
- **Azioni reali**: Consenti agli agenti di interrogare database, accedere a API o eseguire logiche personalizzate
- **Server MCP esistenti**: Usa strumenti da protocolli command (stdio) o HTTP (server-sent event)
- **Sviluppo MCP personalizzato**: Costruisci e configura nuovi server MCP con test nel Costruttore di Agenti

### 8. Sviluppo e Test degli Agenti
- **Supporto chiamata funzioni**: Consenti agli agenti di invocare funzioni esterne dinamicamente
- **Test di integrazione in tempo reale**: Testa integrazioni con esecuzioni in tempo reale e utilizzo degli strumenti
- **Versionamento degli agenti**: Controllo delle versioni per gli agenti con capacità di confronto dei risultati di valutazione
- **Debugging e tracciamento**: Capacità di tracciamento e debugging locale per lo sviluppo degli agenti

## Flusso di lavoro per lo sviluppo Edge AI

### Fase 1: Scoperta e Selezione dei Modelli
1. **Esplora il Catalogo Modelli**: Usa il catalogo modelli per trovare modelli adatti al deployment edge
2. **Confronta le prestazioni**: Valuta i modelli in base a dimensioni, accuratezza e velocità di inferenza
3. **Testa localmente**: Usa modelli Ollama o ONNX per testare localmente prima del deployment edge
4. **Valuta i requisiti di risorse**: Determina le esigenze di memoria e calcolo per i dispositivi edge target

### Fase 2: Ottimizzazione dei Modelli
1. **Converti in ONNX**: Converti i modelli selezionati nel formato ONNX per la compatibilità edge
2. **Applica la quantizzazione**: Riduci la dimensione dei modelli tramite quantizzazione INT8 o INT4
3. **Ottimizzazione hardware**: Ottimizza per hardware edge target (ARM, x86, acceleratori specializzati)
4. **Validazione delle prestazioni**: Valida che i modelli ottimizzati mantengano un'accuratezza accettabile

### Fase 3: Sviluppo dell'Applicazione
1. **Progettazione degli agenti**: Usa il Costruttore di Agenti per creare agenti AI ottimizzati per l'edge
2. **Ingegneria dei prompt**: Sviluppa prompt che funzionano efficacemente con modelli edge più piccoli
3. **Test di integrazione**: Testa gli agenti in condizioni simulate simili a quelle edge
4. **Generazione di codice**: Genera codice di produzione ottimizzato per il deployment edge

### Fase 4: Valutazione e Test
1. **Valutazione in batch**: Testa più configurazioni per trovare impostazioni edge ottimali
2. **Profilazione delle prestazioni**: Analizza velocità di inferenza, utilizzo della memoria e accuratezza
3. **Simulazione edge**: Testa in condizioni simili all'ambiente di deployment edge target
4. **Stress test**: Valuta le prestazioni sotto varie condizioni di carico

### Fase 5: Preparazione al Deployment
1. **Ottimizzazione finale**: Applica ottimizzazioni finali basate sui risultati dei test
2. **Packaging per il deployment**: Prepara modelli e codice per il deployment edge
3. **Documentazione**: Documenta i requisiti e la configurazione del deployment
4. **Setup di monitoraggio**: Prepara il monitoraggio e il logging per il deployment edge

## Pubblico target per lo sviluppo Edge AI

### Sviluppatori Edge AI
- Sviluppatori di applicazioni che costruiscono dispositivi edge e soluzioni IoT alimentate da AI
- Sviluppatori di sistemi embedded che integrano capacità AI in dispositivi con vincoli di risorse
- Sviluppatori mobili che creano applicazioni AI on-device per smartphone e tablet

### Ingegneri Edge AI
- Ingegneri AI che ottimizzano modelli per il deployment edge e gestiscono pipeline di inferenza
- Ingegneri DevOps che distribuiscono e gestiscono modelli AI su infrastrutture edge distribuite
- Ingegneri delle prestazioni che ottimizzano carichi di lavoro AI per vincoli hardware edge

### Ricercatori ed Educatori
- Ricercatori AI che sviluppano modelli e algoritmi efficienti per il calcolo edge
- Educatori che insegnano concetti Edge AI e dimostrano tecniche di ottimizzazione
- Studenti che apprendono le sfide e le soluzioni nel deployment Edge AI

## Casi d'uso Edge AI

### Dispositivi IoT intelligenti
- **Riconoscimento immagini in tempo reale**: Distribuisci modelli di visione artificiale su telecamere e sensori IoT
- **Elaborazione vocale**: Implementa riconoscimento vocale e elaborazione del linguaggio naturale su altoparlanti intelligenti
- **Manutenzione predittiva**: Esegui modelli di rilevamento anomalie su dispositivi edge industriali
- **Monitoraggio ambientale**: Distribuisci modelli di analisi dei dati dei sensori per applicazioni ambientali

### Applicazioni mobili e embedded
- **Traduzione on-device**: Implementa modelli di traduzione linguistica che funzionano offline
- **Realtà aumentata**: Distribuisci riconoscimento e tracciamento oggetti in tempo reale per applicazioni AR
- **Monitoraggio della salute**: Esegui modelli di analisi della salute su dispositivi indossabili e attrezzature mediche
- **Sistemi autonomi**: Implementa modelli decisionali per droni, robot e veicoli

### Infrastruttura Edge Computing
- **Data center edge**: Distribuisci modelli AI nei data center edge per applicazioni a bassa latenza
- **Integrazione CDN**: Integra capacità di elaborazione AI nelle reti di distribuzione dei contenuti
- **Edge 5G**: Sfrutta il calcolo edge 5G per applicazioni alimentate da AI
- **Fog Computing**: Implementa elaborazione AI in ambienti di fog computing

## Installazione e Configurazione

### Installazione dell'estensione
Installa l'estensione AI Toolkit direttamente dal Visual Studio Code Marketplace:

**ID Estensione**: `ms-windows-ai-studio.windows-ai-studio`

**Metodi di installazione**:
1. **Marketplace di VS Code**: Cerca "AI Toolkit" nella vista Estensioni
2. **Linea di comando**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Installazione diretta**: Scarica da [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Prerequisiti per lo sviluppo Edge AI
- **Visual Studio Code**: Versione più recente consigliata
- **Ambiente Python**: Python 3.8+ con librerie AI richieste
- **ONNX Runtime** (Opzionale): Per inferenza di modelli ONNX
- **Ollama** (Opzionale): Per il servizio locale dei modelli
- **Strumenti di accelerazione hardware**: CUDA, OpenVINO o acceleratori specifici per piattaforma

### Configurazione iniziale
1. **Attivazione dell'estensione**: Apri VS Code e verifica che AI Toolkit appaia nella Barra delle Attività
2. **Configurazione fornitori di modelli**: Configura l'accesso a GitHub, OpenAI, Anthropic o altri fornitori di modelli
3. **Ambiente locale**: Configura l'ambiente Python e installa i pacchetti richiesti
4. **Accelerazione hardware**: Configura l'accelerazione GPU/NPU se disponibile
5. **Integrazione MCP**: Configura server Model Context Protocol se necessario

### Checklist per la configurazione iniziale
- [ ] Estensione AI Toolkit installata e attivata
- [ ] Catalogo modelli accessibile e modelli individuabili
- [ ] Playground funzionante per test sui modelli
- [ ] Costruttore di Agenti accessibile per lo sviluppo di prompt
- [ ] Ambiente di sviluppo locale configurato
- [ ] Accelerazione hardware (se disponibile) configurata correttamente

## Iniziare con AI Toolkit

### Guida rapida

Consigliamo di iniziare con i modelli ospitati da GitHub per un'esperienza più semplificata:

1. **Installazione**: Segui la [guida all'installazione](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) per configurare AI Toolkit sul tuo dispositivo
2. **Scoperta dei modelli**: Dalla vista dell'estensione, seleziona **CATALOG > Models** per esplorare i modelli disponibili
3. **Modelli GitHub**: Inizia con i modelli ospitati da GitHub per un'integrazione ottimale
4. **Test nel Playground**: Da qualsiasi scheda modello, seleziona **Try in Playground** per iniziare a sperimentare le capacità del modello

### Sviluppo Edge AI passo dopo passo

#### Passo 1: Esplorazione e selezione dei modelli
1. Apri la vista AI Toolkit nella Barra delle Attività di VS Code
2. Sfoglia il Catalogo Modelli per modelli adatti al deployment edge
3. Filtra per fornitore (GitHub, ONNX, Ollama) in base ai tuoi requisiti edge
4. Usa **Try in Playground** per testare immediatamente le capacità del modello

#### Passo 2: Sviluppo degli agenti
1. Usa il **Costruttore di Prompt (Agenti)** per creare agenti AI ottimizzati per l'edge
2. Genera prompt iniziali utilizzando descrizioni in linguaggio naturale  
3. Itera e perfeziona i prompt basandoti sulle risposte del modello  
4. Integra strumenti MCP per migliorare le capacità degli agenti  

#### Passo 3: Test e Valutazione  
1. Utilizza **Bulk Run** per testare più prompt su modelli selezionati  
2. Esegui agenti con casi di test per validare la funzionalità  
3. Valuta accuratezza e prestazioni utilizzando metriche integrate o personalizzate  
4. Confronta diversi modelli e configurazioni  

#### Passo 4: Ottimizzazione e Fine-tuning  
1. Personalizza i modelli per casi d'uso specifici  
2. Applica il fine-tuning per domini specifici  
3. Ottimizza per vincoli di distribuzione edge  
4. Versiona e confronta diverse configurazioni di agenti  

#### Passo 5: Preparazione alla Distribuzione  
1. Genera codice pronto per la produzione utilizzando l'Agent Builder  
2. Configura connessioni al server MCP per l'uso in produzione  
3. Prepara pacchetti di distribuzione per dispositivi edge  
4. Configura metriche di monitoraggio e valutazione  

## Best Practices per lo Sviluppo di AI Edge  

### Selezione del Modello  
- **Vincoli di Dimensione**: Scegli modelli che rientrano nei limiti di memoria dei dispositivi target  
- **Velocità di Inferenza**: Dai priorità a modelli con tempi di inferenza rapidi per applicazioni in tempo reale  
- **Compromessi di Accuratezza**: Bilancia l'accuratezza del modello con i vincoli di risorse  
- **Compatibilità del Formato**: Preferisci formati ONNX o ottimizzati per hardware per distribuzioni edge  

### Tecniche di Ottimizzazione  
- **Quantizzazione**: Utilizza quantizzazione INT8 o INT4 per ridurre la dimensione del modello e migliorare la velocità  
- **Pruning**: Rimuovi parametri inutili del modello per ridurre i requisiti computazionali  
- **Knowledge Distillation**: Crea modelli più piccoli che mantengano le prestazioni di quelli più grandi  
- **Accelerazione Hardware**: Sfrutta NPUs, GPUs o acceleratori specializzati quando disponibili  

### Workflow di Sviluppo  
- **Test Iterativi**: Testa frequentemente in condizioni simili a quelle edge durante lo sviluppo  
- **Monitoraggio delle Prestazioni**: Monitora continuamente l'uso delle risorse e la velocità di inferenza  
- **Controllo delle Versioni**: Tieni traccia delle versioni dei modelli e delle impostazioni di ottimizzazione  
- **Documentazione**: Documenta tutte le decisioni di ottimizzazione e i compromessi di prestazioni  

### Considerazioni per la Distribuzione  
- **Monitoraggio delle Risorse**: Monitora memoria, CPU e consumo energetico in produzione  
- **Strategie di Fallback**: Implementa meccanismi di fallback per guasti del modello  
- **Meccanismi di Aggiornamento**: Pianifica aggiornamenti del modello e gestione delle versioni  
- **Sicurezza**: Implementa misure di sicurezza adeguate per applicazioni AI edge  

## Integrazione con Framework AI Edge  

### ONNX Runtime  
- **Distribuzione Cross-platform**: Distribuisci modelli ONNX su diverse piattaforme edge  
- **Ottimizzazione Hardware**: Sfrutta le ottimizzazioni specifiche per hardware di ONNX Runtime  
- **Supporto Mobile**: Utilizza ONNX Runtime Mobile per applicazioni su smartphone e tablet  
- **Integrazione IoT**: Distribuisci su dispositivi IoT utilizzando distribuzioni leggere di ONNX Runtime  

### Windows ML  
- **Dispositivi Windows**: Ottimizza per dispositivi edge basati su Windows e PC  
- **Accelerazione NPU**: Sfrutta le Neural Processing Units sui dispositivi Windows  
- **DirectML**: Utilizza DirectML per l'accelerazione GPU su piattaforme Windows  
- **Integrazione UWP**: Integra con applicazioni Universal Windows Platform  

### TensorFlow Lite  
- **Ottimizzazione Mobile**: Distribuisci modelli TensorFlow Lite su dispositivi mobili e embedded  
- **Delegati Hardware**: Utilizza delegati hardware specializzati per l'accelerazione  
- **Microcontrollori**: Distribuisci su microcontrollori utilizzando TensorFlow Lite Micro  
- **Supporto Cross-platform**: Distribuisci su Android, iOS e sistemi Linux embedded  

### Azure IoT Edge  
- **Ibrido Cloud-Edge**: Combina training in cloud con inferenza edge  
- **Distribuzione Moduli**: Distribuisci modelli AI come moduli IoT Edge  
- **Gestione Dispositivi**: Gestisci dispositivi edge e aggiornamenti dei modelli da remoto  
- **Telemetria**: Raccogli dati sulle prestazioni e metriche dei modelli dalle distribuzioni edge  

## Scenari Avanzati di AI Edge  

### Distribuzione Multi-Modello  
- **Ensemble di Modelli**: Distribuisci più modelli per migliorare l'accuratezza o la ridondanza  
- **Test A/B**: Testa diversi modelli simultaneamente su dispositivi edge  
- **Selezione Dinamica**: Scegli modelli basandoti sulle condizioni attuali del dispositivo  
- **Condivisione delle Risorse**: Ottimizza l'uso delle risorse tra modelli distribuiti  

### Federated Learning  
- **Training Distribuito**: Allena modelli su più dispositivi edge  
- **Preservazione della Privacy**: Mantieni i dati di training locali condividendo solo miglioramenti del modello  
- **Apprendimento Collaborativo**: Permetti ai dispositivi di apprendere dalle esperienze collettive  
- **Coordinazione Edge-Cloud**: Coordina l'apprendimento tra dispositivi edge e infrastruttura cloud  

### Elaborazione in Tempo Reale  
- **Elaborazione di Flussi**: Elabora flussi di dati continui su dispositivi edge  
- **Inferenza a Bassa Latenza**: Ottimizza per una latenza di inferenza minima  
- **Elaborazione Batch**: Elabora efficientemente batch di dati su dispositivi edge  
- **Elaborazione Adattiva**: Adatta l'elaborazione basandoti sulle capacità attuali del dispositivo  

## Risoluzione dei Problemi nello Sviluppo di AI Edge  

### Problemi Comuni  
- **Vincoli di Memoria**: Modello troppo grande per la memoria del dispositivo target  
- **Velocità di Inferenza**: Inferenza del modello troppo lenta per requisiti in tempo reale  
- **Degradazione dell'Accuratezza**: L'ottimizzazione riduce l'accuratezza del modello in modo inaccettabile  
- **Compatibilità Hardware**: Modello non compatibile con l'hardware target  

### Strategie di Debug  
- **Profilazione delle Prestazioni**: Utilizza le funzionalità di tracciamento di AI Toolkit per identificare i colli di bottiglia  
- **Monitoraggio delle Risorse**: Monitora memoria e utilizzo della CPU durante lo sviluppo  
- **Test Incrementali**: Testa le ottimizzazioni in modo incrementale per isolare i problemi  
- **Simulazione Hardware**: Utilizza strumenti di sviluppo per simulare l'hardware target  

### Soluzioni di Ottimizzazione  
- **Quantizzazione Ulteriore**: Applica tecniche di quantizzazione più aggressive  
- **Architettura del Modello**: Considera diverse architetture di modelli ottimizzate per edge  
- **Ottimizzazione Preprocessing**: Ottimizza il preprocessing dei dati per vincoli edge  
- **Ottimizzazione Inferenza**: Utilizza ottimizzazioni di inferenza specifiche per hardware  

## Risorse e Prossimi Passi  

### Documentazione Ufficiale  
- [Documentazione per Sviluppatori AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Guida all'Installazione e Configurazione](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Documentazione VS Code Intelligent Apps](https://code.visualstudio.com/docs/intelligentapps)  
- [Documentazione Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Community e Supporto  
- [Repository GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problemi e Richieste di Funzionalità su GitHub](https://aka.ms/AIToolkit/feedback)  
- [Community Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace Estensioni VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Risorse Tecniche  
- [Documentazione ONNX Runtime](https://onnxruntime.ai/)  
- [Documentazione Ollama](https://ollama.ai/)  
- [Documentazione Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Documentazione Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Percorsi di Apprendimento  
- [Corso Fondamenti di AI Edge](../Module01/README.md)  
- [Guida ai Modelli Linguistici Piccoli](../Module02/README.md)  
- [Strategie di Distribuzione Edge](../Module03/README.md)  
- [Sviluppo AI Edge su Windows](./windowdeveloper.md)  

### Risorse Aggiuntive  
- **Statistiche Repository**: 1.8k+ stelle, 150+ fork, 18+ contributori  
- **Licenza**: Licenza MIT  
- **Sicurezza**: Si applicano le politiche di sicurezza Microsoft  
- **Telemetria**: Rispetta le impostazioni di telemetria di VS Code  

## Conclusione  

AI Toolkit per Visual Studio Code rappresenta una piattaforma completa per lo sviluppo moderno di AI, fornendo capacità di sviluppo di agenti semplificate particolarmente utili per applicazioni AI edge. Con il suo ampio catalogo di modelli che supporta fornitori come Anthropic, OpenAI, GitHub e Google, combinato con l'esecuzione locale tramite ONNX e Ollama, il toolkit offre la flessibilità necessaria per scenari di distribuzione edge diversificati.  

La forza del toolkit risiede nel suo approccio integrato—dalla scoperta e sperimentazione dei modelli nel Playground allo sviluppo sofisticato di agenti con il Prompt Builder, capacità di valutazione complete e integrazione fluida degli strumenti MCP. Per gli sviluppatori AI edge, questo significa prototipazione rapida e test di agenti AI prima della distribuzione edge, con la possibilità di iterare rapidamente e ottimizzare per ambienti con risorse limitate.  

Vantaggi chiave per lo sviluppo di AI edge includono:  
- **Sperimentazione Rapida**: Testa modelli e agenti rapidamente prima di impegnarti nella distribuzione edge  
- **Flessibilità Multi-Fornitore**: Accedi a modelli da varie fonti per trovare soluzioni edge ottimali  
- **Sviluppo Locale**: Testa con ONNX e Ollama per sviluppo offline e rispettoso della privacy  
- **Prontezza per la Produzione**: Genera codice pronto per la produzione e integra con strumenti esterni tramite MCP  
- **Valutazione Completa**: Utilizza metriche integrate e personalizzate per validare le prestazioni AI edge  

Man mano che l'AI si sposta verso scenari di distribuzione edge, AI Toolkit per VS Code fornisce l'ambiente di sviluppo e il workflow necessari per costruire, testare e ottimizzare applicazioni intelligenti per ambienti con risorse limitate. Che tu stia sviluppando soluzioni IoT, applicazioni AI mobili o sistemi di intelligenza embedded, il set completo di funzionalità del toolkit e il workflow integrato supportano l'intero ciclo di vita dello sviluppo AI edge.  

Con uno sviluppo continuo e una community attiva (1.8k+ stelle su GitHub), AI Toolkit rimane all'avanguardia tra gli strumenti di sviluppo AI, evolvendosi costantemente per soddisfare le esigenze degli sviluppatori AI moderni che costruiscono per scenari di distribuzione edge.  

[Next Foundry Local](./foundrylocal.md)  

---

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.