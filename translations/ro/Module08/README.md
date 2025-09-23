<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-23T00:49:22+00:00",
  "source_file": "Module08/README.md",
  "language_code": "ro"
}
-->
# Modulul 08: Practică cu Microsoft Foundry Local - Kit complet pentru dezvoltatori

## Prezentare generală

Microsoft Foundry Local reprezintă generația următoare în dezvoltarea AI la margine, oferind dezvoltatorilor instrumente puternice pentru a construi, implementa și scala aplicații AI local, menținând în același timp integrarea fluidă cu Azure AI Foundry. Acest modul acoperă în detaliu Foundry Local, de la instalare până la dezvoltarea avansată a agenților.

**Tehnologii cheie:**
- Microsoft Foundry Local CLI și SDK
- Integrare cu Azure AI Foundry
- Inferență de modele pe dispozitiv
- Cache local de modele și optimizare
- Arhitecturi bazate pe agenți

## Obiectivele de învățare ale modulului

După finalizarea acestui modul, vei putea:

- **Stăpâni configurarea Foundry Local**: Instala, configura și optimiza Foundry Local pentru dezvoltarea pe Windows 11
- **Implementa modele diverse**: Rula modele phi, qwen, deepseek și GPT-OSS-20B local folosind comenzi CLI
- **Construi soluții de producție**: Crea aplicații AI cu inginerie avansată a prompturilor și integrare de date
- **Valorifica ecosistemul open-source**: Integra modele Hugging Face și contribuții comunitare
- **Compara arhitecturi AI**: Înțelege compromisurile între LLM-uri și SLM-uri și strategiile de implementare
- **Dezvolta agenți AI**: Construi agenți inteligenți folosind arhitectura și capacitățile de ancorare ale Foundry Local
- **Implementa modele ca instrumente**: Crea soluții AI modulare și personalizabile pentru aplicații enterprise

## Structura sesiunii

### [1: Începutul cu Foundry Local](./01.FoundryLocalSetup.md)
**Focus**: Instalare, configurare CLI, cache de modele și accelerare hardware

**Ce vei învăța:**
- Instalarea completă a Foundry Local pe Windows 11
- Configurarea CLI și structura comenzilor
- Strategii de cache pentru performanță optimă
- Configurarea și optimizarea accelerării hardware
- Implementarea practică a modelelor phi, qwen, deepseek și GPT-OSS-20B

**Durată**: 2-3 ore  
**Cerințe preliminare**: Windows 11, cunoștințe de bază despre linia de comandă

---

### [2: Construirea soluțiilor AI cu Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus**: Inginerie avansată a prompturilor, integrare de date și sarcini acționabile

**Ce vei învăța:**
- Tehnici avansate de inginerie a prompturilor
- Modele de integrare a datelor și bune practici
- Construirea sarcinilor AI acționabile cu Foundry Local
- Fluxuri de lucru pentru integrarea fluidă cu Azure AI Foundry
- Optimizarea performanței și monitorizare

**Durată**: 2-3 ore  
**Cerințe preliminare**: Finalizarea sesiunii 1, cont Azure (opțional)

---

### [3: Modele open-source în Foundry Local](./03.OpenSourceModels.md)
**Focus**: Integrarea Hugging Face, strategii de selecție a modelelor și contribuții comunitare

**Ce vei învăța:**
- Integrarea modelelor Hugging Face cu Foundry Local
- Strategii și implementare BYOM (adu-ți propriul model)
- Perspective din seria Model Mondays și contribuții comunitare
- Implementarea și optimizarea modelelor personalizate
- Criterii de evaluare și selecție a modelelor comunitare

**Durată**: 2-3 ore  
**Cerințe preliminare**: Finalizarea sesiunilor 1-2, cont Hugging Face

---

### [4: Explorarea modelelor de ultimă generație - LLM-uri, SLM-uri și inferență pe dispozitiv](./04.CuttingEdgeModels.md)
**Focus**: Compararea modelelor, EdgeAI cu Phi și ONNX Runtime, demonstrații avansate

**Ce vei învăța:**
- Compararea completă între LLM-uri și SLM-uri și cazuri de utilizare
- Compromisuri între inferența locală și cea în cloud și cadre de decizie
- Implementarea EdgeAI cu Phi și ONNX Runtime
- Dezvoltarea și implementarea aplicației Chainlit RAG Chat
- Tehnici de optimizare a inferenței WebGPU
- Integrarea și capacitățile SDK AI PC

**Durată**: 3-4 ore  
**Cerințe preliminare**: Finalizarea sesiunilor 1-3, înțelegerea conceptelor de inferență

---

### [5: Construirea rapidă a agenților AI cu Foundry Local](./05.AIPoweredAgents.md)
**Focus**: Dezvoltarea rapidă a aplicațiilor GenAI, prompturi de sistem, ancorare și arhitecturi de agenți

**Ce vei învăța:**
- Arhitectura și modelele de design ale agenților Foundry Local
- Ingineria prompturilor de sistem pentru comportamentul agenților
- Tehnici de ancorare pentru răspunsuri fiabile ale agenților
- Fluxuri de lucru pentru dezvoltarea rapidă a aplicațiilor GenAI
- Orchestrarea agenților și sisteme multi-agent
- Strategii de implementare în producție pentru agenți AI

**Durată**: 3-4 ore  
**Cerințe preliminare**: Finalizarea sesiunilor 1-4, înțelegerea de bază a agenților AI

---

### [6: Foundry Local - Modele ca instrumente](./06.ModelsAsTools.md)
**Focus**: Soluții AI modulare, implementare pe dispozitiv și scalare enterprise

**Ce vei învăța:**
- Tratarea modelelor AI ca instrumente modulare și personalizabile
- Implementare pe dispozitiv fără dependență de cloud
- Inferență cu latență redusă, eficientă din punct de vedere al costurilor și care protejează confidențialitatea
- Modele de integrare SDK, API și CLI
- Personalizarea modelelor pentru cazuri de utilizare specifice
- Strategii de scalare de la local la Azure AI Foundry
- Arhitecturi de aplicații AI pregătite pentru enterprise

**Durată**: 3-4 ore  
**Cerințe preliminare**: Toate sesiunile anterioare, experiența în dezvoltare enterprise este utilă

## Cerințe preliminare

### Cerințe de sistem
- **Sistem de operare**: Windows 11 (22H2 sau mai recent)
- **Memorie**: 16GB RAM (32GB recomandat pentru modele mai mari)
- **Spațiu de stocare**: 50GB spațiu liber pentru cache-ul modelelor
- **Hardware**: Dispozitiv cu NPU recomandat (Copilot+ PC), GPU opțional
- **Rețea**: Internet de mare viteză pentru descărcarea inițială a modelelor

### Mediu de dezvoltare
- Visual Studio Code cu extensia AI Toolkit
- Python 3.10+ și pip
- Git pentru controlul versiunilor
- PowerShell sau Command Prompt
- Azure CLI (opțional pentru integrarea în cloud)

### Cunoștințe preliminare
- Înțelegere de bază a conceptelor AI/ML
- Familiaritate cu linia de comandă
- Noțiuni de bază de programare în Python
- Concepte REST API
- Cunoștințe de bază despre prompturi și inferența modelelor

## Cronologia modulului

**Timp estimat total**: 15-20 ore

| Sesiune | Domeniu de focus | Timp | Complexitate |
|---------|------------------|------|--------------|
|  1 | Configurare & Baze | 2-3 ore | Începător |
|  2 | Soluții AI | 2-3 ore | Intermediar |
|  3 | Open Source | 2-3 ore | Intermediar |
|  4 | Modele avansate | 3-4 ore | Avansat |
|  5 | Agenți AI | 3-4 ore | Avansat |
|  6 | Instrumente enterprise | 3-4 ore | Expert |

## Resurse cheie

### Documentație principală
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Documentația Azure AI Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Seria Model Mondays](https://aka.ms/model-mondays)

### Resurse comunitare
- [Discuții comunitare Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Exemple Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Comunitatea Microsoft AI Developer](https://techcommunity.microsoft.com/category/artificialintelligence)

## Rezultate ale învățării

După finalizarea acestui modul, vei fi pregătit să:

### Stăpânire tehnică
- **Implementa și gestiona**: Instalări Foundry Local în medii de dezvoltare și producție
- **Integra modele**: Lucrezi fără probleme cu diverse familii de modele de la Microsoft, Hugging Face și surse comunitare
- **Construiești aplicații**: Creezi aplicații AI pregătite pentru producție cu funcționalități avansate și optimizări
- **Dezvolți agenți**: Implementa agenți AI sofisticați cu ancorare, raționament și integrare de instrumente

### Înțelegere strategică
- **Decizii de arhitectură**: Alegi între implementarea locală și cea în cloud
- **Optimizare performanță**: Optimizezi performanța inferenței pe diferite configurații hardware
- **Scalare enterprise**: Proiectezi aplicații care se extind de la prototipuri locale la implementări enterprise
- **Confidențialitate și securitate**: Implementa soluții AI care protejează confidențialitatea prin inferență locală

### Capacități de inovare
- **Prototipare rapidă**: Construiești și testezi rapid concepte de aplicații AI
- **Integrare comunitară**: Valorifici modele open-source și contribui la ecosistem
- **Modele avansate**: Implementa modele AI de ultimă generație, inclusiv RAG, agenți și integrare de instrumente
- **Dezvoltare pregătită pentru viitor**: Construiești aplicații pregătite pentru tehnologii și modele AI emergente

## Începe acum

1. **Pregătește mediul**: Asigură-te că ai Windows 11 cu specificațiile hardware recomandate
2. **Instalează cerințele preliminare**: Configurează instrumentele de dezvoltare și dependențele
3. **Începe cu Sesiunea 1**: Începe cu instalarea și configurarea de bază a Foundry Local
4. **Progresează secvențial**: Completează sesiunile în ordine pentru o progresie optimă a învățării
5. **Exersează continuu**: Aplică conceptele prin exerciții practice și proiecte

## Metrice de succes

Urmărește progresul tău prin modul:

- [ ] Instalează și configurează cu succes Foundry Local
- [ ] Implementează și rulează cel puțin 4 familii de modele diferite
- [ ] Construiește o soluție AI completă cu integrare de date
- [ ] Integrează cel puțin 2 modele open-source
- [ ] Creează o aplicație funcțională RAG chat
- [ ] Dezvoltă și implementează un agent AI
- [ ] Implementa o arhitectură de tip modele-ca-instrumente

## Start rapid pentru exemple

### 1) Configurarea mediului (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Pornește un model local (terminal nou)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Rulează demonstrația Chainlit (Sesiunea 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Rulează coordonatorul multi-agent (Sesiunea 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Dacă vezi erori de conexiune, validează Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Configurarea routerului (Sesiunea 6)
Routerul efectuează un control rapid al stării și suportă configurarea bazată pe mediu:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Acest modul reprezintă vârful dezvoltării AI la margine, combinând instrumentele de nivel enterprise ale Microsoft cu flexibilitatea și inovația ecosistemului open-source. Prin stăpânirea Foundry Local, vei fi poziționat în fruntea dezvoltării aplicațiilor AI.

Pentru Azure OpenAI (Sesiunea 2), vezi README-ul exemplului pentru variabilele de mediu necesare și setările versiunii API.

## Prezentare generală a exemplelor

- `samples/01`: Chat REST rapid cu Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integrare SDK OpenAI (`sdk_quickstart.py`).
- `samples/03`: Descoperirea modelelor + test rapid (`list_and_bench.cmd`).
- `samples/04`: Demonstrație Chainlit RAG (`app.py`).
- `samples/05`: Orchestrare multi-agent (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router pentru modele-ca-instrumente (`python samples\06\router.py`).

---

