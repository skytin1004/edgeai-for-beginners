<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8bcf70fe61c9007c880f9753cc9c3e01",
  "translation_date": "2025-10-08T13:57:01+00:00",
  "source_file": "README.md",
  "language_code": "hr"
}
-->
# EdgeAI za početnike

![Naslovna slika tečaja](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.hr.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)  

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Slijedite ove korake kako biste započeli s korištenjem ovih resursa:

1. **Forkajte repozitorij**: Kliknite [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
2. **Klonirajte repozitorij**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**Pridružite se Azure AI Foundry Discordu i upoznajte stručnjake i kolege developere**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Podrška za više jezika

#### Podržano putem GitHub Action (Automatizirano i uvijek ažurirano)

[Arapski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bugarski](../bg/README.md) | [Burmanski (Mjanmar)](../my/README.md) | [Kineski (pojednostavljeni)](../zh/README.md) | [Kineski (tradicionalni, Hong Kong)](../hk/README.md) | [Kineski (tradicionalni, Macau)](../mo/README.md) | [Kineski (tradicionalni, Tajvan)](../tw/README.md) | [Hrvatski](./README.md) | [Češki](../cs/README.md) | [Danski](../da/README.md) | [Nizozemski](../nl/README.md) | [Finski](../fi/README.md) | [Francuski](../fr/README.md) | [Njemački](../de/README.md) | [Grčki](../el/README.md) | [Hebrejski](../he/README.md) | [Hindski](../hi/README.md) | [Mađarski](../hu/README.md) | [Indonezijski](../id/README.md) | [Talijanski](../it/README.md) | [Japanski](../ja/README.md) | [Korejski](../ko/README.md) | [Malajski](../ms/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Norveški](../no/README.md) | [Perzijski (Farsi)](../fa/README.md) | [Poljski](../pl/README.md) | [Portugalski (Brazil)](../br/README.md) | [Portugalski (Portugal)](../pt/README.md) | [Pandžapski (Gurmukhi)](../pa/README.md) | [Rumunjski](../ro/README.md) | [Ruski](../ru/README.md) | [Srpski (ćirilica)](../sr/README.md) | [Slovački](../sk/README.md) | [Slovenski](../sl/README.md) | [Španjolski](../es/README.md) | [Svahili](../sw/README.md) | [Švedski](../sv/README.md) | [Tagalog (Filipinski)](../tl/README.md) | [Tajlandski](../th/README.md) | [Turski](../tr/README.md) | [Ukrajinski](../uk/README.md) | [Urdu](../ur/README.md) | [Vijetnamski](../vi/README.md)

**Ako želite dodati podršku za dodatne jezike, popis podržanih jezika nalazi se [ovdje](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Uvod

Dobrodošli u **EdgeAI za početnike** – vaš sveobuhvatan vodič u transformativni svijet Edge umjetne inteligencije. Ovaj tečaj povezuje moćne AI mogućnosti s praktičnom primjenom na edge uređajima, omogućujući vam da iskoristite potencijal AI-a tamo gdje se podaci generiraju i gdje se odluke trebaju donositi.

### Što ćete savladati

Ovaj tečaj vas vodi od osnovnih koncepata do implementacija spremnih za proizvodnju, pokrivajući:
- **Mali jezični modeli (SLM)** optimizirani za edge primjenu
- **Optimizacija prilagođena hardveru** za različite platforme
- **Inference u stvarnom vremenu** uz očuvanje privatnosti
- **Strategije za proizvodnu primjenu** u poslovnim aplikacijama

### Zašto je EdgeAI važan

Edge AI predstavlja promjenu paradigme koja rješava ključne moderne izazove:
- **Privatnost i sigurnost**: Obrada osjetljivih podataka lokalno, bez izlaganja oblaku
- **Performanse u stvarnom vremenu**: Eliminacija mrežne latencije za aplikacije koje zahtijevaju brzinu
- **Učinkovitost troškova**: Smanjenje troškova za bandwidth i računalne resurse u oblaku
- **Otpornost sustava**: Funkcionalnost tijekom prekida mreže
- **Regulatorna usklađenost**: Zadovoljavanje zahtjeva za suverenitetom podataka

### Edge AI

Edge AI odnosi se na pokretanje AI algoritama i jezičnih modela lokalno na hardveru, blizu mjesta gdje se podaci generiraju, bez oslanjanja na resurse oblaka za inference. Smanjuje latenciju, poboljšava privatnost i omogućuje donošenje odluka u stvarnom vremenu.

### Osnovni principi:
- **Inference na uređaju**: AI modeli se pokreću na edge uređajima (telefonima, routerima, mikrokontrolerima, industrijskim PC-ima)
- **Offline sposobnost**: Funkcionira bez stalne internetske povezanosti
- **Niska latencija**: Trenutni odgovori prilagođeni sustavima u stvarnom vremenu
- **Suverenitet podataka**: Zadržava osjetljive podatke lokalno, poboljšavajući sigurnost i usklađenost

### Mali jezični modeli (SLM)

SLM-ovi poput Phi-4, Mistral-7B i Gemma su optimizirane verzije većih LLM-ova – trenirani ili destilirani za:
- **Smanjeni memorijski otisak**: Učinkovito korištenje ograničene memorije edge uređaja
- **Niži zahtjevi za računalnu snagu**: Optimizirani za performanse CPU-a i edge GPU-a
- **Brže vrijeme pokretanja**: Brza inicijalizacija za responzivne aplikacije

Oni omogućuju moćne NLP mogućnosti uz zadovoljenje ograničenja:
- **Ugrađeni sustavi**: IoT uređaji i industrijski kontroleri
- **Mobilni uređaji**: Pametni telefoni i tableti s offline sposobnostima
- **IoT uređaji**: Senzori i pametni uređaji s ograničenim resursima
- **Edge serveri**: Lokalni procesni uređaji s ograničenim GPU resursima
- **Osobna računala**: Scenariji primjene na desktop i laptop uređajima

## Moduli tečaja i navigacija

| Modul | Tema | Fokus područje | Ključni sadržaj | Razina | Trajanje |
|-------|------|----------------|-----------------|--------|----------|
| [📖 00 ](./introduction.md) | [Uvod u EdgeAI](./introduction.md) | Osnove i kontekst | Pregled EdgeAI-a • Industrijske primjene • Uvod u SLM • Ciljevi učenja | Početnik | 1-2 sata |
| [📚 01](../../Module01) | [Osnove EdgeAI-a](./Module01/README.md) | Usporedba oblaka i Edge AI-a | Osnove EdgeAI-a • Studije slučaja • Vodič za implementaciju • Edge primjena | Početnik | 3-4 sata |
| [🧠 02](../../Module02) | [Osnove SLM modela](./Module02/README.md) | Obitelji modela i arhitektura | Phi obitelj • Qwen obitelj • Gemma obitelj • BitNET • μModel • Phi-Silica | Početnik | 4-5 sati |
| [🚀 03](../../Module03) | [Praksa primjene SLM-a](./Module03/README.md) | Lokalna i oblačna primjena | Napredno učenje • Lokalno okruženje • Primjena u oblaku | Srednji | 4-5 sati |
| [⚙️ 04](../../Module04) | [Alati za optimizaciju modela](./Module04/README.md) | Optimizacija za različite platforme | Uvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sinteza radnog tijeka | Srednji | 5-6 sati |
| [🔧 05](../../Module05) | [SLMOps u proizvodnji](./Module05/README.md) | Operacije u proizvodnji | Uvod u SLMOps • Destilacija modela • Fino podešavanje • Primjena u proizvodnji | Napredni | 5-6 sati |
| [🤖 06](../../Module06) | [AI agenti i pozivanje funkcija](./Module06/README.md) | Okviri za agente i MCP | Uvod u agente • Pozivanje funkcija • Protokol konteksta modela | Napredni | 4-5 sati |
| [💻 07](../../Module07) | [Implementacija na platformama](./Module07/README.md) | Primjeri za različite platforme | AI alatni set • Foundry Local • Razvoj za Windows | Napredni | 3-4 sata |
| [🏭 08](../../Module08) | [Foundry Local alatni set](./Module08/README.md) | Primjeri spremni za proizvodnju | Primjeri aplikacija (vidi detalje dolje) | Ekspert | 8-10 sati |

### 🏭 **Modul 08: Primjeri aplikacija**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)  
- [02: Integracija OpenAI SDK-a](./Module08/samples/02/README.md)  
- [03: Otkrivanje modela i benchmarking](./Module08/samples/03/README.md)  
- [04: Chainlit RAG aplikacija](./Module08/samples/04/README.md)  
- [05: Orkestracija više agenata](./Module08/samples/05/README.md)  
- [06: Router za modele kao alate](./Module08/samples/06/README.md)  
- [07: Direktni API klijent](./Module08/samples/07/README.md)  
- [08: Windows 11 Chat aplikacija](./Module08/samples/08/README.md)  
- [09: Napredni sustav više agenata](./Module08/samples/09/README.md)  
- [10: Okvir za Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Radionica: Praktični put učenja**

Sveobuhvatni materijali za radionicu s implementacijama spremnim za proizvodnju:

- **[Vodič za radionicu](./Workshop/Readme.md)** - Ciljevi učenja, ishodi i navigacija resursima  
- **Python primjeri** (6 sesija) - Ažurirano s najboljim praksama, rukovanjem greškama i detaljnom dokumentacijom  
- **Jupyter bilježnice** (8 interaktivnih) - Korak-po-korak vodiči s benchmarkovima i praćenjem performansi  
- **Vodiči za sesije** - Detaljni vodiči u markdown formatu za svaku sesiju radionice  
- **Alati za validaciju** - Skripte za provjeru kvalitete koda i testiranje

**Što ćete izgraditi:**
- Lokalna AI chat aplikacija s podrškom za streaming  
- RAG pipeline s evaluacijom kvalitete (RAGAS)  
- Alati za benchmarking i usporedbu više modela  
- Sustavi za orkestraciju više agenata  
- Inteligentno usmjeravanje modela prema zadacima  

### 📊 **Sažetak puta učenja**
- **Ukupno trajanje**: 36-45 sati  
- **Put za početnike**: Moduli 01-02 (7-9 sati)  
- **Put za srednje napredne**: Moduli 03-04 (9-11 sati)  
- **Put za napredne**: Moduli 05-07 (12-15 sati)  
- **Put za eksperte**: Modul 08 (8-10 sati)

## Što ćete izgraditi

### 🎯 Ključne kompetencije
- **Arhitektura Edge AI-a**: Dizajnirajte AI sustave s lokalnim fokusom i integracijom oblaka  
- **Optimizacija modela**: Kvantizirajte i komprimirajte modele za edge primjenu (85% ubrzanje, 75% smanjenje veličine)  
- **Primjena na više platformi**: Windows, mobilni uređaji, ugrađeni sustavi i hibridni sustavi oblaka i edge-a  
- **Operacije u proizvodnji**: Praćenje, skaliranje i održavanje Edge AI-a u proizvodnji  

### 🏗️ Praktični projekti
- **Foundry Local chat aplikacije**: Windows 11 aplikacija s mogućnošću prebacivanja modela  
- **Sustavi više agenata**: Koordinator sa specijaliziranim agentima za složene radne tijekove  
- **RAG aplikacije**: Lokalna obrada dokumenata s pretraživanjem vektora  
- **Modelni usmjerivači**: Inteligentni odabir između modela na temelju analize zadatka  
- **API okviri**: Klijenti spremni za produkciju s podrškom za streaming i praćenje stanja  
- **Alati za više platformi**: Integracijski obrasci za LangChain/Semantic Kernel  

### 🏢 Industrijske primjene  
**Proizvodnja** • **Zdravstvo** • **Autonomna vozila** • **Pametni gradovi** • **Mobilne aplikacije**  

## Brzi početak  

**Preporučeni put učenja** (ukupno 20-30 sati):  

0. **📖 Uvod** ([Introduction.md](./introduction.md)): Osnove EdgeAI + industrijski kontekst + okvir za učenje  
1. **📚 Osnove** (Moduli 01-02): Koncepti EdgeAI + obitelji SLM modela  
2. **⚙️ Optimizacija** (Moduli 03-04): Implementacija + okviri za kvantizaciju  
3. **🚀 Produkcija** (Moduli 05-06): SLMOps + AI agenti + pozivanje funkcija  
4. **💻 Implementacija** (Moduli 07-08): Primjeri platformi + Foundry Local alatni set  

Svaki modul uključuje teoriju, praktične vježbe i uzorke koda spremne za produkciju.  

## Utjecaj na karijeru  

**Tehničke uloge**: Arhitekt EdgeAI rješenja • ML inženjer (Edge) • IoT AI programer • Programer mobilne AI tehnologije  

**Industrijski sektori**: Proizvodnja 4.0 • Zdravstvena tehnologija • Autonomni sustavi • FinTech • Potrošačka elektronika  

**Projekti za portfelj**: Sustavi s više agenata • Produkcijske RAG aplikacije • Implementacija na više platformi • Optimizacija performansi  

## Struktura repozitorija  

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```
  
## Istaknuti dijelovi tečaja  

✅ **Progresivno učenje**: Teorija → Praksa → Implementacija u produkciji  
✅ **Stvarne studije slučaja**: Microsoft, Japan Airlines, implementacije u poduzećima  
✅ **Praktični primjeri**: 50+ primjera, 10 sveobuhvatnih Foundry Local demonstracija  
✅ **Fokus na performanse**: Poboljšanja brzine od 85%, smanjenje veličine od 75%  
✅ **Više platformi**: Windows, mobilni uređaji, ugrađeni sustavi, hibridni cloud-edge  
✅ **Spremno za produkciju**: Okviri za praćenje, skaliranje, sigurnost i usklađenost  

📖 **[Dostupan vodič za učenje](STUDY_GUIDE.md)**: Strukturirani 20-satni put učenja s preporukama za raspodjelu vremena i alatima za samoprocjenu.  

---  

**EdgeAI predstavlja budućnost implementacije AI-a**: lokalno orijentiran, s očuvanjem privatnosti i učinkovitošću. Savladajte ove vještine kako biste izgradili sljedeću generaciju inteligentnih aplikacija.  

## Ostali tečajevi  

Naš tim nudi i druge tečajeve! Pogledajte:  

- [MCP za početnike](https://github.com/microsoft/mcp-for-beginners)  
- [AI agenti za početnike](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Generativni AI za početnike koristeći .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
- [Generativni AI za početnike koristeći JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
- [Generativni AI za početnike](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [ML za početnike](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
- [Data Science za početnike](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
- [AI za početnike](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
- [Kibernetička sigurnost za početnike](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)  
- [Web razvoj za početnike](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
- [IoT za početnike](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [XR razvoj za početnike](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Savladavanje GitHub Copilota za AI programiranje u paru](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [Savladavanje GitHub Copilota za C#/.NET programere](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [Odaberite vlastitu Copilot avanturu](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

## Dobivanje pomoći  

Ako zapnete ili imate pitanja o izradi AI aplikacija, pridružite se:  

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)  

Ako imate povratne informacije o proizvodu ili naiđete na pogreške tijekom izrade, posjetite:  

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)  

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.