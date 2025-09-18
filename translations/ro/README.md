<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c817161ba08864340737d623f761b9ae",
  "translation_date": "2025-09-18T18:01:11+00:00",
  "source_file": "README.md",
  "language_code": "ro"
}
-->
# EdgeAI pentru Începători

![Imagine de copertă a cursului](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ro.png)

[![Contribuitori GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![Probleme GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![Pull-requests GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![Observatori GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![Fork-uri GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![Stele GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)  

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Urmați acești pași pentru a începe să utilizați aceste resurse:

1. **Forkați Repozitoriul**: Click [![Fork-uri GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
2. **Clonați Repozitoriul**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**Alăturați-vă Discordului Azure AI Foundry și întâlniți experți și alți dezvoltatori**](https://discord.com/invite/ByRwuEEgH4)  

### 🌐 Suport Multi-Limbă

#### Suportat prin GitHub Action (Automatizat & Mereu Actualizat)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](./README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

**Dacă doriți să aveți suport pentru alte limbi, acestea sunt listate [aici](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Introducere

Bine ați venit la **EdgeAI pentru Începători** – călătoria voastră completă în lumea transformatoare a Inteligenței Artificiale la margine. Acest curs face legătura între capacitățile puternice ale AI și implementarea practică în lumea reală pe dispozitive edge, oferindu-vă posibilitatea de a valorifica potențialul AI direct acolo unde se generează datele și unde trebuie luate deciziile.

### Ce Veți Învăța

Acest curs vă duce de la concepte fundamentale la implementări gata de producție, acoperind:
- **Modele de Limbaj Mici (SLMs)** optimizate pentru implementarea la margine
- **Optimizare conștientă de hardware** pe diverse platforme
- **Inferență în timp real** cu capacități de protejare a confidențialității
- **Strategii de implementare în producție** pentru aplicații de întreprindere

### De ce Este Important EdgeAI

Edge AI reprezintă o schimbare de paradigmă care abordează provocările moderne critice:
- **Confidențialitate & Securitate**: Procesați datele sensibile local, fără expunere la cloud
- **Performanță în Timp Real**: Eliminați latența rețelei pentru aplicații critice
- **Eficiență Costuri**: Reduceți cheltuielile de lățime de bandă și calcul în cloud
- **Operațiuni Reziliente**: Mențineți funcționalitatea în timpul întreruperilor de rețea
- **Conformitate Regulatorie**: Respectați cerințele de suveranitate a datelor

### Edge AI

Edge AI se referă la rularea algoritmilor AI și a modelelor de limbaj local pe hardware – aproape de locul unde se generează datele – fără a se baza pe resurse cloud pentru inferență. Reduce latența, îmbunătățește confidențialitatea și permite luarea deciziilor în timp real.

### Principii de Bază:
- **Inferență pe dispozitiv**: Modelele AI rulează pe dispozitive edge (telefoane, routere, microcontrolere, PC-uri industriale)
- **Capacitate offline**: Funcționează fără conectivitate persistentă la internet
- **Latență redusă**: Răspunsuri imediate potrivite pentru sisteme în timp real
- **Suveranitatea datelor**: Păstrează datele sensibile local, îmbunătățind securitatea și conformitatea

### Modele de Limbaj Mici (SLMs)

SLMs precum Phi-4, Mistral-7B și Gemma sunt versiuni optimizate ale LLM-urilor mai mari – antrenate sau distilate pentru:
- **Amprentă de memorie redusă**: Utilizare eficientă a memoriei limitate a dispozitivelor edge
- **Cerere de calcul mai mică**: Optimizate pentru performanța CPU și GPU edge
- **Timpuri de pornire mai rapide**: Inițializare rapidă pentru aplicații receptive

Acestea deblochează capacități NLP puternice respectând constrângerile:
- **Sisteme încorporate**: Dispozitive IoT și controlere industriale
- **Dispozitive mobile**: Smartphone-uri și tablete cu capacități offline
- **Dispozitive IoT**: Senzori și dispozitive inteligente cu resurse limitate
- **Servere edge**: Unități de procesare locală cu resurse GPU limitate
- **Computere personale**: Scenarii de implementare pe desktop și laptop

## Arhitectura Cursului

### [Modulul 01: Fundamentele și Transformarea EdgeAI](./Module01/README.md)
**Temă**: Schimbarea transformatoare a implementării AI la margine

#### Structura Capitolului:
- [**Secțiunea 1: Fundamentele EdgeAI**](./Module01/01.EdgeAIFundamentals.md)
  - Comparație între AI tradițional în cloud și AI la margine
  - Provocări și constrângeri ale calculului la margine
  - Tehnologii cheie: cuantificarea modelelor, optimizarea compresiei, Modele de Limbaj Mici (SLMs)
  - Accelerare hardware: NPUs, optimizare GPU, optimizare CPU
  - Avantaje: securitate confidențialitate, latență redusă, capacități offline, eficiență costuri

- [**Secțiunea 2: Studii de Caz din Lumea Reală**](./Module01/02.RealWorldCaseStudies.md)
  - Ecosistemul de modele Microsoft Phi & Mu
  - Studiu de caz al sistemului de raportare AI al Japan Airlines
  - Impactul pieței și direcțiile viitoare
  - Considerații și bune practici de implementare

- [**Secțiunea 3: Ghid Practic de Implementare**](./Module01/03.PracticalImplementationGuide.md)
  - Configurarea mediului de dezvoltare (Python 3.10+, .NET 8+)
  - Cerințe hardware și configurații recomandate
  - Resursele familiei de modele de bază
  - Instrumente de cuantificare și optimizare (Llama.cpp, Microsoft Olive, Apple MLX)
  - Lista de verificare pentru evaluare și verificare

- [**Secțiunea 4: Platforme Hardware pentru Implementarea Edge AI**](./Module01/04.EdgeDeployment.md)
  - Considerații și cerințe pentru implementarea Edge AI
  - Hardware Intel pentru AI la margine și tehnici de optimizare
  - Soluții AI Qualcomm pentru sisteme mobile și încorporate
  - Platforme de calcul la margine NVIDIA Jetson
  - Platforme PC Windows AI cu accelerare NPU
  - Strategii de optimizare specifice hardware-ului

---

### [Modulul 02: Fundamentele Modelelor de Limbaj Mici](./Module02/README.md)
**Temă**: Principii teoretice ale SLM, strategii de implementare și implementare în producție

#### Structura Capitolului:
- [**Secțiunea 1: Fundamentele Familiei de Modele Microsoft Phi**](./Module02/01.PhiFamily.md)
  - Evoluția filozofiei de design (Phi-1 la Phi-4)
  - Designul arhitecturii orientat spre eficiență
  - Capacități specializate (raționament, multimodal, implementare la margine)

- [**Secțiunea 2: Fundamentele Familiei Qwen**](./Module02/02.QwenFamily.md)
  - Excelență open source (Qwen 1.0 la Qwen3) - disponibilă prin Hugging Face
  - Arhitectură avansată de raționament cu capacități de mod gândire
  - Opțiuni scalabile de implementare (0.5B-235B parametri)

- [**Secțiunea 3: Fundamentele Familiei Gemma**](./Module02/03.GemmaFamily.md)
  - Inovație bazată pe cercetare (Gemma 3 & 3n)
  - Excelență multimodală
  - Arhitectură orientată spre mobil

- [**Secțiunea 4: Fundamentele Familiei BitNET**](./Module02/04.BitNETFamily.md)
  - Tehnologie revoluționară de cuantificare (1.58-bit)
  - Cadru de inferență specializat de la https://github.com/microsoft/BitNet
  - Leadership AI sustenabil prin eficiență extremă

- [**Secțiunea 5: Fundamentele Modelului Microsoft Mu**](./Module02/05.mumodel.md)
  - Arhitectură orientată spre dispozitive integrată în Windows 11
  - Integrare sistemică cu Setările Windows 11
  - Operare offline care protejează confidențialitatea

- [**Secțiunea 6: Fundamentele Phi-Silica**](./Module02/06.phisilica.md)
  - Arhitectură optimizată pentru NPU integrată în PC-urile Windows 11 Copilot+
  - Eficiență excepțională (650 tokeni/secundă la 1.5W)
  - Integrare pentru dezvoltatori cu Windows App SDK

---

### [Modulul 03: Implementarea Modelelor de Limbaj Mici](./Module03/README.md)
**Temă**: Implementarea completă a ciclului de viață al SLM, de la teorie la mediu de producție

#### Structura Capitolului:
- [**Secțiunea 1: Învățare Avansată SLM**](./Module03/01.SLMAdvancedLearning.md)
  - Cadru de clasificare a parametrilor (Micro SLM 100M-1.4B, Medium SLM 14B-30B)
  - Tehnici avansate de optimizare (metode de cuantificare, cuantificare BitNET 1-bit)
  - Strategii de achiziție a modelelor (Azure AI Foundry pentru modelele Phi, Hugging Face pentru modelele selectate)

- [**Secțiunea 2: Implementare în Mediu Local**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Implementare universală pe platforma Ollama
  - Soluții locale de nivel enterprise Microsoft Foundry
  - Analiză comparativă a cadrelor

- [**Secțiunea 3: Implementare Containerizată în Cloud**](./Module03/03.DeployingSLMinCloud.md)
  - Implementare de inferență performantă vLLM
  - Orchestrare de containere Ollama
  - Implementare optimizată pentru margine ONNX Runtime

---

### [Modulul 04: Conversia Formatului Modelului și Cuantificare](./Module04/README.md)
**Temă**: Set complet de instrumente de optimizare a modelului pentru implementarea la margine pe diverse platforme

#### Structura Capitolului:
- [**Secțiunea 1: Fundamentele Conversiei Formatului Modelului și Cuantificării**](./Module04/01.Introduce.md)
  - Cadru de clasificare a preciziei (ultra-scăzută, scăzută, medie)
  - Avantajele și cazurile de utilizare ale formatelor GGUF și ONNX
  - Beneficiile cuantificării pentru eficiența operațională
  - Benchmark-uri de performanță și comparații ale amprentei de memorie
- [**Secțiunea 2: Ghid de Implementare Llama.cpp**](./Module04/02.Llamacpp.md)
  - Instalare multiplatformă (Windows, macOS, Linux)
  - Conversie în format GGUF și niveluri de cuantizare (Q2_K până la Q8_0)
  - Accelerare hardware (CUDA, Metal, OpenCL, Vulkan)
  - Integrare Python și implementare API REST

- [**Secțiunea 3: Microsoft Olive Optimization Suite**](./Module04/03.MicrosoftOlive.md)
  - Optimizare de modele adaptată hardware-ului cu peste 40 de componente integrate
  - Auto-optimizare cu cuantizare dinamică și statică
  - Integrare enterprise cu fluxuri de lucru Azure ML
  - Suport pentru modele populare (Llama, Phi, modele Qwen selectate, Gemma)

- [**Secțiunea 4: OpenVINO Toolkit Optimization Suite**](./Module04/04.openvino.md)
  - Toolkit open-source de la Intel pentru implementarea AI multiplatformă
  - Neural Network Compression Framework (NNCF) pentru optimizare avansată
  - OpenVINO GenAI pentru implementarea modelelor de limbaj extins
  - Accelerare hardware pe CPU, GPU, VPU și acceleratoare AI

- [**Secțiunea 5: Apple MLX Framework - Analiză Detaliată**](./Module04/05.AppleMLX.md)
  - Arhitectură de memorie unificată pentru Apple Silicon
  - Suport pentru LLaMA, Mistral, Phi-3, modele Qwen selectate
  - Fine-tuning LoRA și personalizare de modele
  - Integrare Hugging Face cu cuantizare 4-bit/8-bit

- [**Secțiunea 6: Sinteza Fluxului de Dezvoltare Edge AI**](./Module04/06.workflow-synthesis.md)
  - Arhitectură unificată a fluxului de lucru care integrează mai multe cadre de optimizare
  - Arbori decizionali pentru selecția cadrelor și analiza compromisurilor de performanță
  - Validarea pregătirii pentru producție și strategii de implementare cuprinzătoare
  - Strategii de adaptare pentru hardware emergent și arhitecturi de modele

---

### [Module 05: SLMOps - Operațiuni pentru Modele de Limbaj Mic](./Module05/README.md)
**Temă**: Operațiuni complete pentru ciclul de viață SLM, de la distilare la implementare în producție

#### Structura Capitolelor:
- [**Secțiunea 1: Introducere în SLMOps**](./Module05/01.IntroduceSLMOps.md)
  - Schimbarea paradigmei SLMOps în operațiunile AI
  - Eficiență costurilor și arhitectură orientată spre confidențialitate
  - Impact strategic asupra afacerilor și avantaje competitive
  - Provocări și soluții în implementarea reală

- [**Secțiunea 2: Distilarea Modelului - De la Teorie la Practică**](./Module05/02.SLMOps-Distillation.md)
  - Transfer de cunoștințe de la modele profesor la modele elev
  - Implementarea procesului de distilare în două etape
  - Fluxuri de lucru Azure ML pentru distilare cu exemple practice
  - Reducere de 85% a timpului de inferență cu păstrarea a 92% din acuratețe

- [**Secțiunea 3: Fine-Tuning - Personalizarea Modelului pentru Sarcini Specifice**](./Module05/03.SLMOps-Finetuing.md)
  - Tehnici de fine-tuning eficiente din punct de vedere al parametrilor (PEFT)
  - Metode avansate LoRA și QLoRA
  - Implementarea fine-tuning-ului cu Microsoft Olive
  - Antrenament multi-adaptor și optimizarea hiperparametrilor

- [**Secțiunea 4: Implementare - Pregătirea pentru Producție**](./Module05/04.SLMOps.Deployment.md)
  - Conversia și cuantizarea modelului pentru producție
  - Configurarea implementării locale Foundry
  - Benchmarking de performanță și validarea calității
  - Reducere de 75% a dimensiunii cu monitorizare în producție

---

### [Module 06: Sisteme Agentice SLM - Agenți AI și Apelarea Funcțiilor](./Module06/README.md)
**Temă**: Implementarea sistemelor agentice SLM de la bază la apelarea avansată a funcțiilor și integrarea Model Context Protocol

#### Structura Capitolelor:
- [**Secțiunea 1: Agenți AI și Fundamentele Modelelor de Limbaj Mic**](./Module06/01.IntroduceAgent.md)
  - Cadru de clasificare a agenților (reflex, bazat pe model, bazat pe scop, agenți de învățare)
  - Fundamentele SLM și strategii de optimizare (GGUF, cuantizare, cadre edge)
  - Analiza compromisurilor SLM vs LLM (reducere de costuri 10-30×, eficiență 70-80% pentru sarcini)
  - Implementare practică cu Ollama, VLLM și soluții edge Microsoft

- [**Secțiunea 2: Apelarea Funcțiilor în Modele de Limbaj Mic**](./Module06/02.FunctionCalling.md)
  - Implementarea sistematică a fluxului de lucru (detectarea intenției, output JSON, execuție externă)
  - Implementări specifice platformei (Phi-4-mini, modele Qwen selectate, Microsoft Foundry Local)
  - Exemple avansate (colaborare multi-agent, selecție dinamică de instrumente)
  - Considerații pentru producție (limitarea ratei, jurnalizare audit, măsuri de securitate)

- [**Secțiunea 3: Integrarea Model Context Protocol (MCP)**](./Module06/03.IntroduceMCP.md)
  - Arhitectura protocolului și designul sistemului stratificat
  - Suport multi-backend (Ollama pentru dezvoltare, vLLM pentru producție)
  - Protocoale de conexiune (moduri STDIO și SSE)
  - Aplicații reale (automatizare web, procesare de date, integrare API)

---

### [Module 07: Exemple de Implementare EdgeAI](./Module07/README.md)
**Temă**: Implementări complete EdgeAI pe diverse platforme și cadre

#### Structura Capitolelor:
- [**Toolkit AI pentru Visual Studio Code**](./Module07/aitoolkit.md)
  - Mediu de dezvoltare Edge AI complet în VS Code
  - Catalog de modele și descoperire pentru implementare edge
  - Fluxuri de lucru pentru testare locală, optimizare și dezvoltare de agenți
  - Monitorizarea performanței și evaluarea pentru scenarii edge

- [**Ghid de Dezvoltare EdgeAI pentru Windows**](./Module07/windowdeveloper.md)
  - Prezentare cuprinzătoare a platformei Windows AI Foundry
  - API Phi Silica pentru inferență eficientă pe NPU
  - API-uri de Computer Vision pentru procesarea imaginilor și OCR
  - CLI Foundry Local pentru dezvoltare și testare locală

- [**EdgeAI în NVIDIA Jetson Orin Nano**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - Performanță AI de 67 TOPS într-un format de dimensiunea unui card de credit
  - Suport pentru modele generative AI (transformatoare de viziune, LLM-uri, modele de viziune-limbaj)
  - Aplicații în robotică, drone, camere inteligente, dispozitive autonome
  - Platformă accesibilă de $249 pentru democratizarea dezvoltării AI

- [**EdgeAI în Aplicații Mobile cu .NET MAUI și ONNX Runtime GenAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - AI mobil multiplatformă cu un singur cod C#
  - Suport pentru accelerare hardware (CPU, GPU, procesoare AI mobile)
  - Optimizări specifice platformei (CoreML pentru iOS, NNAPI pentru Android)
  - Implementarea completă a buclei generative AI

- [**EdgeAI în Azure cu Motorul pentru Modele de Limbaj Mic**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - Arhitectură hibridă cloud-edge pentru implementare
  - Integrare cu servicii Azure AI și ONNX Runtime
  - Implementare la scară enterprise și gestionarea continuă a modelelor
  - Fluxuri de lucru hibride AI pentru procesarea inteligentă a documentelor

- [**EdgeAI cu Windows ML**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Fundația Windows AI Foundry pentru inferență performantă pe dispozitiv
  - Suport hardware universal (AMD, Intel, NVIDIA, Qualcomm silicon)
  - Abstracție automată a hardware-ului și optimizare
  - Cadru unificat pentru ecosistemul divers de hardware Windows

- [**EdgeAI cu Aplicații Foundry Local**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - Implementare RAG orientată spre confidențialitate cu resurse locale
  - Integrare model de limbaj Phi-3 cu căutare semantică (doar modele Phi)
  - Suport pentru baze de date vectoriale locale (SQLite, Qdrant)
  - Capacități de suveranitate a datelor și operare offline

## Obiectivele Cursului

Prin completarea acestui curs cuprinzător EdgeAI, veți dezvolta expertiza necesară pentru a proiecta, implementa și implementa soluții EdgeAI pregătite pentru producție. Abordarea noastră structurată asigură că veți stăpâni atât fundamentele teoretice, cât și abilitățile practice de implementare.

### Competențe Tehnice

**Cunoștințe Fundamentale**
- Înțelegeți diferențele fundamentale între arhitecturile AI bazate pe cloud și cele bazate pe edge
- Stăpâniți principiile cuantizării, compresiei și optimizării modelelor pentru medii cu resurse limitate
- Înțelegeți opțiunile de accelerare hardware (NPUs, GPUs, CPUs) și implicațiile lor de implementare

**Abilități de Implementare**
- Implementați Modele de Limbaj Mic pe diverse platforme edge (mobile, embedded, IoT, servere edge)
- Aplicați cadre de optimizare, inclusiv Llama.cpp, Microsoft Olive, ONNX Runtime și Apple MLX
- Implementați sisteme de inferență în timp real cu cerințe de răspuns sub o secundă

**Expertiză în Producție**
- Proiectați arhitecturi EdgeAI scalabile pentru aplicații enterprise
- Implementați strategii de monitorizare, întreținere și actualizare pentru sistemele implementate
- Aplicați cele mai bune practici de securitate pentru implementări EdgeAI care protejează confidențialitatea

### Capacități Strategice

**Cadru de Luare a Deciziilor**
- Evaluați oportunitățile EdgeAI și identificați cazuri de utilizare potrivite pentru aplicații de afaceri
- Analizați compromisurile între acuratețea modelului, viteza de inferență, consumul de energie și costurile hardware
- Selectați familii și configurații SLM adecvate pe baza constrângerilor specifice de implementare

**Arhitectura Sistemului**
- Proiectați soluții EdgeAI de la cap la coadă care se integrează cu infrastructura existentă
- Planificați arhitecturi hibride edge-cloud pentru performanță optimă și eficiență costurilor
- Implementați fluxuri de date și conducte de procesare pentru aplicații AI în timp real

### Aplicații Industriale

**Scenarii de Implementare Practică**
- **Producție**: Sisteme de control al calității, întreținere predictivă și optimizarea proceselor
- **Sănătate**: Instrumente de diagnostic care protejează confidențialitatea și sisteme de monitorizare a pacienților
- **Transport**: Luarea deciziilor pentru vehicule autonome și gestionarea traficului
- **Orașe Inteligente**: Infrastructură inteligentă și sisteme de gestionare a resurselor
- **Electronice de Consum**: Aplicații mobile alimentate de AI și dispozitive inteligente pentru acasă

## Prezentare Generală a Rezultatelor Învățării

### Rezultatele Învățării Modul 01:
- Înțelegeți diferențele fundamentale între arhitecturile AI bazate pe cloud și cele bazate pe edge
- Stăpâniți tehnicile de optimizare de bază pentru implementarea edge
- Recunoașteți aplicațiile reale și poveștile de succes
- Dobândiți abilități practice pentru implementarea soluțiilor EdgeAI

### Rezultatele Învățării Modul 02:
- Înțelegere profundă a diferitelor filozofii de design SLM și implicațiile lor de implementare
- Stăpâniți capacitățile strategice de luare a deciziilor bazate pe constrângerile computaționale și cerințele de performanță
- Înțelegeți compromisurile de flexibilitate în implementare
- Dobândiți perspective pregătite pentru viitor în arhitectura AI eficientă

### Rezultatele Învățării Modul 03:
- Capacități strategice de selecție a modelelor
- Stăpânirea tehnicilor de optimizare
- Stăpânirea flexibilității în implementare
- Capacități de configurare pregătite pentru producție

### Rezultatele Învățării Modul 04:
- Înțelegere profundă a limitelor de cuantizare și aplicațiilor practice
- Experiență practică cu mai multe cadre de optimizare (Llama.cpp, Olive, OpenVINO, MLX)
- Stăpânirea optimizării hardware Intel cu OpenVINO și NNCF
- Capacități de selecție a optimizării adaptate hardware-ului pe diverse platforme
- Abilități de implementare în producție pentru medii de calcul edge multiplatformă
- Selecție strategică a cadrelor și sinteza fluxului de lucru pentru soluții Edge AI optime

### Rezultatele Învățării Modul 05:
- Stăpânirea paradigmei SLMOps și principiilor operaționale
- Implementarea distilării modelului pentru transfer de cunoștințe și optimizarea eficienței
- Aplicarea tehnicilor de fine-tuning pentru personalizarea modelului specific domeniului
- Implementarea soluțiilor SLM pregătite pentru producție cu strategii de monitorizare și întreținere

### Rezultatele Învățării Modul 06:
- Înțelegerea conceptelor fundamentale ale agenților AI și arhitecturii Modelelor de Limbaj Mic
- Stăpânirea implementării apelării funcțiilor pe diverse platforme și cadre
- Integrarea Model Context Protocol (MCP) pentru interacțiunea standardizată cu instrumente externe
- Construirea sistemelor agentice sofisticate cu cerințe minime de intervenție umană

### Rezultatele Învățării Modul 07:
- Stăpânirea Toolkit-ului AI pentru Visual Studio Code pentru fluxuri de lucru complete de dezvoltare Edge AI
- Dobândirea expertizei în platforma Windows AI Foundry și strategiile de optimizare NPU
- Experiență practică cu diverse platforme EdgeAI și strategii de implementare
- Stăpânirea tehnicilor de optimizare specifice hardware-ului pe platforme NVIDIA, mobile, Azure și Windows
- Înțelegerea compromisurilor de implementare între performanță, cost și cerințe de confidențialitate
- Dezvoltarea abilităților practice pentru construirea aplicațiilor EdgeAI reale pe diferite ecosisteme

## Rezultatele Așteptate ale Cursului

La finalizarea cu succes a acestui curs, veți fi echipat cu cunoștințele, abilitățile și încrederea necesare pentru a conduce inițiative EdgeAI în medii profesionale.

### Pregătire Profesională

**Leadership Tehnic**
- **Arhitectura Soluțiilor**: Proiectați sisteme EdgeAI complete care îndeplinesc cerințele enterprise
- **Optimizarea Performanței**: Obțineți echilibrul optim între acuratețe, viteză și consum de resurse
- **Implementare Multiplatformă**: Implementați soluții pe Windows, Linux, mobile și platforme embedded
- **Operațiuni de Producție**: Mențineți și scalați sistemele EdgeAI cu fiabilitate de nivel enterprise

**Expertiză Industrială**
- **Evaluarea Tehnologiei**: Evaluați și recomandați soluții EdgeAI pentru provocări specifice de afaceri
- **Planificarea Implementării**: Dezvoltați termene realiste și cerințe de resurse pentru proiectele EdgeAI
- **Managementul Riscurilor**: Identificați și atenuați riscurile tehnice și operaționale în implementările EdgeAI
- **Optimizarea ROI**: Demonstrați valoarea de afaceri măsurabilă din implementările EdgeAI

### Oportunități de Avansare în Carieră

**Roluri Profesionale**
- Arhitect de Soluții EdgeAI
- Inginer Machine Learning (Specializare Edge)
- Dezvoltator IoT AI
- Dezvoltator Aplicații Mobile AI
- Consultant AI Enterprise

**Sectore Industriale**
- Producție Inteligentă și Industria 4.0

Acest curs te poziționează în avangarda implementării tehnologiei AI, unde capabilitățile inteligente sunt integrate perfect în dispozitivele și sistemele care susțin viața modernă.

## Diagrama structurii fișierelor

```
edgeai-for-beginners/
├── imgs/
│   └── cover.png
├── Module01/ (EdgeAI Fundamentals and Transformation)
│   ├── 01.EdgeAIFundamentals.md
│   ├── 02.RealWorldCaseStudies.md
│   ├── 03.PracticalImplementationGuide.md
│   ├── 04.EdgeDeployment.md
│   └── README.md
├── Module02/ (Small Language Model Foundations)
│   ├── 01.PhiFamily.md
│   ├── 02.QwenFamily.md
│   ├── 03.GemmaFamily.md
│   ├── 04.BitNETFamily.md
│   ├── 05.mumodel.md
│   ├── 06.phisilica.md
│   └── README.md
├── Module03/ (SLM Deployment Practice)
│   ├── 01.SLMAdvancedLearning.md
│   ├── 02.DeployingSLMinLocalEnv.md
│   ├── 03.DeployingSLMinCloud.md
│   └── README.md
├── Module04/ (Model Format Conversion and Quantization)
│   ├── 01.Introduce.md
│   ├── 02.Llamacpp.md
│   ├── 03.MicrosoftOlive.md
│   ├── 04.openvino.md
│   ├── 05.AppleMLX.md
│   ├── 06.workflow-synthesis.md
│   └── README.md
├── Module05/ (SLMOps - Small Language Model Operations)
│   ├── 01.IntroduceSLMOps.md
│   ├── 02.SLMOps-Distillation.md
│   ├── 03.SLMOps-Finetuing.md
│   ├── 04.SLMOps.Deployment.md
│   └── README.md
├── Module06/ (SLM Agentic Systems)
│   ├── 01.IntroduceAgent.md
│   ├── 02.FunctionCalling.md
│   ├── 03.IntroduceMCP.md
│   └── README.md
├── Module07/ (EdgeAI Implementation Samples)
│   ├── aitoolkit.md
│   ├── windowdeveloper.md
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## Caracteristici ale cursului

- **Învățare progresivă**: Avansează treptat de la concepte de bază la implementări avansate
- **Integrarea teoriei cu practica**: Fiecare modul conține atât fundamente teoretice, cât și operațiuni practice
- **Studii de caz reale**: Bazate pe cazuri reale de la Microsoft, Alibaba, Google și alții
- **Exerciții practice**: Fișiere de configurare complete, proceduri de testare API și scripturi de implementare
- **Repere de performanță**: Comparații detaliate ale vitezei de inferență, utilizării memoriei și cerințelor de resurse
- **Considerații de nivel enterprise**: Practici de securitate, cadre de conformitate și strategii de protecție a datelor

## Începe

Calea de învățare recomandată:
1. Începe cu **Module01** pentru a construi o înțelegere fundamentală a EdgeAI
2. Continuă cu **Module02** pentru a înțelege în profunzime diverse familii de modele SLM
3. Învață **Module03** pentru a stăpâni abilități practice de implementare
4. Continuă cu **Module04** pentru optimizarea avansată a modelelor, conversia formatelor și sinteza cadrelor
5. Finalizează **Module05** pentru a stăpâni SLMOps pentru implementări pregătite pentru producție
6. Explorează **Module06** pentru a înțelege sistemele agentice SLM și capabilitățile de apelare a funcțiilor
7. Termină cu **Module07** pentru a dobândi experiență practică cu AI Toolkit și diverse exemple de implementare EdgeAI

Fiecare modul este conceput să fie complet independent, dar învățarea secvențială va oferi cele mai bune rezultate.

## Ghid de studiu

Un [Ghid de studiu](STUDY_GUIDE.md) cuprinzător este disponibil pentru a te ajuta să maximizezi experiența de învățare. Ghidul de studiu oferă:

- **Căi de învățare structurate**: Programe optimizate pentru finalizarea cursului în 20 de ore
- **Orientări pentru alocarea timpului**: Recomandări specifice pentru echilibrarea lecturii, exercițiilor și proiectelor
- **Concentrare pe concepte cheie**: Obiective de învățare prioritizate pentru fiecare modul
- **Instrumente de autoevaluare**: Întrebări și exerciții pentru a testa înțelegerea
- **Idei de mini-proiecte**: Aplicații practice pentru a consolida învățarea

Ghidul de studiu este conceput pentru a se adapta atât învățării intensive (1 săptămână), cât și studiului part-time (3 săptămâni), cu indicații clare despre cum să îți aloci timpul eficient chiar dacă poți dedica doar 10 ore cursului.

---

**Viitorul EdgeAI constă în îmbunătățirea continuă a arhitecturilor de modele, tehnicilor de cuantizare și strategiilor de implementare care prioritizează eficiența și specializarea în detrimentul capabilităților generaliste. Organizațiile care adoptă această schimbare de paradigmă vor fi bine poziționate să valorifice potențialul transformator al AI, menținând în același timp controlul asupra datelor și operațiunilor lor.**

## Alte cursuri

Echipa noastră produce și alte cursuri! Descoperă:

- [MCP pentru Începători](https://github.com/microsoft/mcp-for-beginners)
- [Agenți AI pentru Începători](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [AI Generativ pentru Începători folosind .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [AI Generativ pentru Începători folosind JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [AI Generativ pentru Începători](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML pentru Începători](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Știința Datelor pentru Începători](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI pentru Începători](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Securitate Cibernetică pentru Începători](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Dezvoltare Web pentru Începători](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT pentru Începători](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [Dezvoltare XR pentru Începători](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Stăpânirea GitHub Copilot pentru Programare AI în Perechi](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [Stăpânirea GitHub Copilot pentru Dezvoltatori C#/.NET](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Alege-ți propria aventură Copilot](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.