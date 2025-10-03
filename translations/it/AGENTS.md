<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:32:45+00:00",
  "source_file": "AGENTS.md",
  "language_code": "it"
}
-->
# AGENTS.md

## Panoramica del Progetto

EdgeAI for Beginners è un repository educativo completo che insegna lo sviluppo di Edge AI con Small Language Models (SLMs). Il corso copre i fondamenti di EdgeAI, il deployment dei modelli, le tecniche di ottimizzazione e implementazioni pronte per la produzione utilizzando Microsoft Foundry Local e vari framework AI.

**Tecnologie Chiave:**
- Python 3.8+ (linguaggio principale per esempi AI/ML)
- .NET C# (esempi AI/ML)
- JavaScript/Node.js con Electron (per applicazioni desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Framework AI: LangChain, Semantic Kernel, Chainlit
- Ottimizzazione dei modelli: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tipo di Repository:** Repository di contenuti educativi con 8 moduli e 10 applicazioni di esempio complete

**Architettura:** Percorso di apprendimento multi-modulo con esempi pratici che dimostrano i modelli di deployment di Edge AI

## Struttura del Repository

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Comandi di Configurazione

### Configurazione del Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Configurazione degli Esempi Python (Modulo08 e esempi Python)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Configurazione degli Esempi Node.js (Esempio 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Configurazione di Foundry Local

Foundry Local è necessario per eseguire gli esempi del Modulo08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Workflow di Sviluppo

### Sviluppo dei Contenuti

Questo repository contiene principalmente **contenuti educativi in Markdown**. Quando si apportano modifiche:

1. Modificare i file `.md` nelle directory dei moduli appropriati
2. Seguire i modelli di formattazione esistenti
3. Assicurarsi che gli esempi di codice siano accurati e testati
4. Aggiornare i contenuti tradotti corrispondenti, se necessario (o lasciare che l'automazione se ne occupi)

### Sviluppo delle Applicazioni di Esempio

Per gli esempi Python (esempi 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Per l'esempio Electron (esempio 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Test delle Applicazioni di Esempio

Gli esempi Python non hanno test automatizzati ma possono essere validati eseguendoli:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

L'esempio Electron ha un'infrastruttura di test:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Istruzioni per i Test

### Validazione dei Contenuti

Il repository utilizza workflow di traduzione automatizzati. Non è richiesto alcun test manuale per le traduzioni.

**Validazione manuale per modifiche ai contenuti:**
1. Controllare il rendering Markdown visualizzando i file `.md`
2. Verificare che tutti i link puntino a destinazioni valide
3. Testare eventuali frammenti di codice inclusi nella documentazione
4. Controllare che le immagini vengano caricate correttamente

### Test delle Applicazioni di Esempio

**Modulo08/samples/08 (app Electron) ha test completi:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Gli esempi Python devono essere testati manualmente:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Linee Guida per lo Stile del Codice

### Contenuti Markdown

- Utilizzare una gerarchia coerente per i titoli (# per il titolo, ## per le sezioni principali, ### per le sottosezioni)
- Includere blocchi di codice con specificatori di linguaggio: ```python, ```bash, ```javascript
- Seguire la formattazione esistente per tabelle, elenchi e enfasi
- Mantenere le righe leggibili (circa 80-100 caratteri, ma non in modo rigido)
- Utilizzare link relativi per riferimenti interni

### Stile del Codice Python

- Seguire le convenzioni PEP 8
- Utilizzare suggerimenti di tipo quando appropriato
- Includere docstring per funzioni e classi
- Usare nomi di variabili significativi
- Mantenere le funzioni focalizzate e concise

### Stile del Codice JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Convenzioni chiave:**
- Configurazione ESLint fornita nell'esempio 08
- Prettier per la formattazione del codice
- Utilizzare la sintassi moderna ES6+
- Seguire i modelli esistenti nel codice

## Linee Guida per le Pull Request

### Formato del Titolo
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### Prima di Inviare

**Per modifiche ai contenuti:**
- Visualizzare in anteprima tutti i file Markdown modificati
- Verificare che i link e le immagini funzionino
- Controllare errori di battitura e grammaticali

**Per modifiche al codice di esempio (Modulo08/samples/08):**
```bash
npm run lint
npm test
```

**Per modifiche agli esempi Python:**
- Testare che l'esempio venga eseguito correttamente
- Verificare che la gestione degli errori funzioni
- Controllare la compatibilità con Foundry Local

### Processo di Revisione

- Le modifiche ai contenuti educativi vengono revisionate per accuratezza e chiarezza
- Gli esempi di codice vengono testati per funzionalità
- Gli aggiornamenti delle traduzioni sono gestiti automaticamente da GitHub Actions

## Sistema di Traduzione

**IMPORTANTE:** Questo repository utilizza traduzioni automatizzate tramite GitHub Actions.

- Le traduzioni si trovano nella directory `/translations/` (50+ lingue)
- Automatizzate tramite il workflow `co-op-translator.yml`
- **NON modificare manualmente i file di traduzione** - verranno sovrascritti
- Modificare solo i file sorgente in inglese nella directory principale e nei moduli
- Le traduzioni vengono generate automaticamente al push sul branch `main`

## Integrazione con Foundry Local

La maggior parte degli esempi del Modulo08 richiede che Microsoft Foundry Local sia in esecuzione:

### Avvio di Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Verifica di Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Variabili d'Ambiente per gli Esempi

La maggior parte degli esempi utilizza queste variabili d'ambiente:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Build e Deployment

### Deployment dei Contenuti

Questo repository è principalmente documentazione - non è richiesto alcun processo di build per i contenuti.

### Build delle Applicazioni di Esempio

**Applicazione Electron (Modulo08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Esempi Python:**
Nessun processo di build - gli esempi vengono eseguiti direttamente con l'interprete Python.

## Problemi Comuni e Risoluzione

### Foundry Local Non in Esecuzione
**Problema:** Gli esempi falliscono con errori di connessione

**Soluzione:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problemi con l'Ambiente Virtuale Python
**Problema:** Errori di importazione dei moduli

**Soluzione:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Problemi di Build Electron
**Problema:** Errori durante npm install o build

**Soluzione:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Conflitti nel Workflow di Traduzione
**Problema:** La PR di traduzione confligge con le tue modifiche

**Soluzione:**
- Modificare solo i file sorgente in inglese
- Lasciare che il workflow di traduzione automatizzato gestisca le traduzioni
- Se si verificano conflitti, unire `main` nel tuo branch dopo che le traduzioni sono state unite

## Risorse Aggiuntive

### Percorsi di Apprendimento
- **Percorso Principiante:** Moduli 01-02 (7-9 ore)
- **Percorso Intermedio:** Moduli 03-04 (9-11 ore)
- **Percorso Avanzato:** Moduli 05-07 (12-15 ore)
- **Percorso Esperto:** Modulo 08 (8-10 ore)

### Contenuti Chiave dei Moduli
- **Modulo01:** Fondamenti di EdgeAI e casi di studio reali
- **Modulo02:** Famiglie e architetture di Small Language Model (SLM)
- **Modulo03:** Strategie di deployment locale e cloud
- **Modulo04:** Ottimizzazione dei modelli con diversi framework
- **Modulo05:** SLMOps - operazioni di produzione
- **Modulo06:** Agenti AI e chiamata di funzioni
- **Modulo07:** Implementazioni specifiche per piattaforma
- **Modulo08:** Toolkit Foundry Local con 10 esempi completi

### Dipendenze Esterne
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Runtime locale per modelli AI
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework di ottimizzazione
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit di ottimizzazione dei modelli
- [OpenVINO](https://docs.openvino.ai/) - Toolkit di ottimizzazione di Intel

## Note Specifiche del Progetto

### Applicazioni di Esempio del Modulo08

Il repository include 10 applicazioni di esempio complete:

1. **01-REST Chat Quickstart** - Integrazione base con OpenAI SDK
2. **02-OpenAI SDK Integration** - Funzionalità avanzate dell'SDK
3. **03-Model Discovery & Benchmarking** - Strumenti di confronto tra modelli
4. **04-Chainlit RAG Application** - Generazione aumentata da recupero
5. **05-Multi-Agent Orchestration** - Coordinamento base tra agenti
6. **06-Models-as-Tools Router** - Routing intelligente dei modelli
7. **07-Direct API Client** - Integrazione API a basso livello
8. **08-Windows 11 Chat App** - Applicazione desktop nativa Electron
9. **09-Advanced Multi-Agent System** - Orchestrazione complessa tra agenti
10. **10-Foundry Tools Framework** - Integrazione LangChain/Semantic Kernel

Ogni esempio dimostra diversi aspetti dello sviluppo di Edge AI con Foundry Local.

### Considerazioni sulle Prestazioni

- Gli SLM sono ottimizzati per il deployment edge (2-16GB RAM)
- L'inferenza locale offre tempi di risposta di 50-500ms
- Le tecniche di quantizzazione riducono le dimensioni del 75% mantenendo l'85% delle prestazioni
- Capacità di conversazione in tempo reale con modelli locali

### Sicurezza e Privacy

- Tutto il processamento avviene localmente - nessun dato inviato al cloud
- Adatto per applicazioni sensibili alla privacy (sanità, finanza)
- Soddisfa i requisiti di sovranità dei dati
- Foundry Local funziona interamente su hardware locale

---

**Questo è un repository educativo focalizzato sull'insegnamento dello sviluppo di Edge AI. Il modello principale di contributo consiste nel migliorare i contenuti educativi e aggiungere/migliorare le applicazioni di esempio che dimostrano i concetti di Edge AI.**

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.