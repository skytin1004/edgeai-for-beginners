<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8bcf70fe61c9007c880f9753cc9c3e01",
  "translation_date": "2025-10-08T11:44:44+00:00",
  "source_file": "README.md",
  "language_code": "sl"
}
-->
# EdgeAI za začetnike

![Naslovna slika tečaja](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.sl.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Sledite tem korakom, da začnete uporabljati te vire:

1. **Forkajte repozitorij**: Kliknite [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klonirajte repozitorij**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pridružite se Azure AI Foundry Discordu in spoznajte strokovnjake ter druge razvijalce**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Podpora za več jezikov

#### Podprto prek GitHub Action (avtomatizirano in vedno posodobljeno)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](./README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

**Če želite dodati dodatne prevode, so podprti jeziki navedeni [tukaj](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Uvod

Dobrodošli v **EdgeAI za začetnike** – na vaši celoviti poti v preoblikovalni svet umetne inteligence na robu (Edge AI). Ta tečaj premošča vrzel med zmogljivostmi umetne inteligence in praktično uporabo v resničnem svetu na robnih napravah, kar vam omogoča, da izkoristite potencial umetne inteligence neposredno tam, kjer se podatki ustvarjajo in kjer je treba sprejemati odločitve.

### Kaj boste osvojili

Ta tečaj vas bo popeljal od osnovnih konceptov do implementacij, pripravljenih za produkcijo, in zajema:
- **Majhne jezikovne modele (SLM)**, optimizirane za uporabo na robu
- **Optimizacijo, prilagojeno strojni opremi**, na različnih platformah
- **Inferenco v realnem času** z možnostmi ohranjanja zasebnosti
- **Strategije za produkcijsko implementacijo** za poslovne aplikacije

### Zakaj je EdgeAI pomemben

Edge AI predstavlja premik paradigme, ki naslavlja ključne sodobne izzive:
- **Zasebnost in varnost**: Obdelava občutljivih podatkov lokalno, brez izpostavljanja oblaku
- **Izvedba v realnem času**: Odprava omrežne zakasnitve za časovno občutljive aplikacije
- **Učinkovitost stroškov**: Zmanjšanje stroškov pasovne širine in oblačnega računalništva
- **Odpornost delovanja**: Zagotavljanje funkcionalnosti tudi ob izpadih omrežja
- **Skladnost z zakonodajo**: Izpolnjevanje zahtev glede suverenosti podatkov

### Edge AI

Edge AI se nanaša na izvajanje algoritmov umetne inteligence in jezikovnih modelov lokalno na strojni opremi, blizu mesta, kjer se podatki ustvarjajo, brez zanašanja na oblačne vire za inferenco. To zmanjšuje zakasnitev, izboljšuje zasebnost in omogoča sprejemanje odločitev v realnem času.

### Temeljna načela:
- **Inferenca na napravi**: AI modeli se izvajajo na robnih napravah (telefoni, usmerjevalniki, mikrokrmilniki, industrijski računalniki)
- **Sposobnost delovanja brez povezave**: Delovanje brez stalne internetne povezave
- **Nizka zakasnitev**: Takojšnji odzivi, primerni za sisteme v realnem času
- **Suverenost podatkov**: Občutljivi podatki ostanejo lokalni, kar izboljša varnost in skladnost

### Majhni jezikovni modeli (SLM)

SLM, kot so Phi-4, Mistral-7B in Gemma, so optimizirane različice večjih LLM, ki so usposobljene ali destilirane za:
- **Zmanjšano porabo pomnilnika**: Učinkovita uporaba omejenega pomnilnika robnih naprav
- **Manjšo potrebo po računski moči**: Optimizirani za delovanje na CPU in robnih GPU
- **Hitrejši zagonski čas**: Hitro inicializacijo za odzivne aplikacije

Omogočajo zmogljive zmožnosti NLP, hkrati pa ustrezajo omejitvam:
- **Vgrajeni sistemi**: IoT naprave in industrijski krmilniki
- **Mobilne naprave**: Pametni telefoni in tablice z možnostjo delovanja brez povezave
- **IoT naprave**: Senzorji in pametne naprave z omejenimi viri
- **Robni strežniki**: Lokalni procesni enoti z omejenimi GPU viri
- **Osebni računalniki**: Namizne in prenosne naprave za implementacijo

## Moduli tečaja in navigacija

| Modul | Tema | Osrednje področje | Ključne vsebine | Nivo | Trajanje |
|-------|------|-------------------|-----------------|------|----------|
| [📖 00 ](./introduction.md) | [Uvod v EdgeAI](./introduction.md) | Osnove in kontekst | Pregled EdgeAI • Industrijske aplikacije • Uvod v SLM • Cilji učenja | Začetnik | 1-2 uri |
| [📚 01](../../Module01) | [Osnove EdgeAI](./Module01/README.md) | Primerjava med oblakom in Edge AI | Osnove EdgeAI • Primeri iz resničnega sveta • Vodnik za implementacijo • Uporaba na robu | Začetnik | 3-4 ure |
| [🧠 02](../../Module02) | [Osnove modelov SLM](./Module02/README.md) | Družine in arhitektura modelov | Družina Phi • Družina Qwen • Družina Gemma • BitNET • μModel • Phi-Silica | Začetnik | 4-5 ur |
| [🚀 03](../../Module03) | [Praksa implementacije SLM](./Module03/README.md) | Lokalna in oblačna implementacija | Napredno učenje • Lokalno okolje • Implementacija v oblaku | Srednje | 4-5 ur |
| [⚙️ 04](../../Module04) | [Orodja za optimizacijo modelov](./Module04/README.md) | Optimizacija za različne platforme | Uvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sinteza delovnih tokov | Srednje | 5-6 ur |
| [🔧 05](../../Module05) | [SLMOps v produkciji](./Module05/README.md) | Operacije v produkciji | Uvod v SLMOps • Destilacija modelov • Fino prilagajanje • Implementacija v produkciji | Napredno | 5-6 ur |
| [🤖 06](../../Module06) | [AI agenti in klicanje funkcij](./Module06/README.md) | Okviri za agente in MCP | Uvod v agente • Klicanje funkcij • Protokol konteksta modela | Napredno | 4-5 ur |
| [💻 07](../../Module07) | [Implementacija platforme](./Module07/README.md) | Primeri za različne platforme | AI orodja • Foundry Local • Razvoj za Windows | Napredno | 3-4 ure |
| [🏭 08](../../Module08) | [Orodja Foundry Local](./Module08/README.md) | Primeri, pripravljeni za produkcijo | Vzorčne aplikacije (glejte podrobnosti spodaj) | Strokovno | 8-10 ur |

### 🏭 **Modul 08: Vzorčne aplikacije**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK integracija](./Module08/samples/02/README.md)
- [03: Odkritje in ocenjevanje modelov](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikacija](./Module08/samples/04/README.md)
- [05: Orkestracija več agentov](./Module08/samples/05/README.md)
- [06: Usmerjevalnik Models-as-Tools](./Module08/samples/06/README.md)
- [07: Neposredni API odjemalec](./Module08/samples/07/README.md)
- [08: Windows 11 aplikacija za klepet](./Module08/samples/08/README.md)
- [09: Napreden sistem z več agenti](./Module08/samples/09/README.md)
- [10: Okvir orodij Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Delavnica: Praktična učna pot**

Celoviti materiali za praktično delavnico z implementacijami, pripravljenimi za produkcijo:

- **[Vodnik za delavnico](./Workshop/Readme.md)** - Celoviti učni cilji, rezultati in navigacija po virih
- **Python primeri** (6 sej) - Posodobljeni z najboljšimi praksami, obravnavo napak in celovito dokumentacijo
- **Jupyter zvezki** (8 interaktivnih) - Korak za korakom vadnice z meritvami in spremljanjem zmogljivosti
- **Vodniki za seje** - Podrobni markdown vodniki za vsako delavnico
- **Orodja za validacijo** - Skripte za preverjanje kakovosti kode in izvajanje testov

**Kaj boste zgradili:**
- Lokalno AI aplikacijo za klepet s podporo za pretakanje
- RAG cevovode z ocenjevanjem kakovosti (RAGAS)
- Orodja za primerjavo in ocenjevanje več modelov
- Sisteme za orkestracijo več agentov
- Inteligentno usmerjanje modelov z izbiro na podlagi nalog

### 📊 **Povzetek učne poti**
- **Skupno trajanje**: 36-45 ur
- **Pot za začetnike**: Moduli 01-02 (7-9 ur)  
- **Pot za srednje napredne**: Moduli 03-04 (9-11 ur)
- **Pot za napredne**: Moduli 05-07 (12-15 ur)
- **Pot za strokovnjake**: Modul 08 (8-10 ur)

## Kaj boste zgradili

### 🎯 Ključne kompetence
- **Arhitektura Edge AI**: Oblikovanje lokalno usmerjenih AI sistemov z integracijo v oblak
- **Optimizacija modelov**: Kvantizacija in stiskanje modelov za uporabo na robu (85 % hitrejša obdelava, 75 % manjša velikost)
- **Implementacija na več platformah**: Windows, mobilne naprave, vgrajeni sistemi in hibridni sistemi oblak-rob
- **Operacije v produkciji**: Spremljanje, skaliranje in vzdrževanje Edge AI v produkciji

### 🏗️ Praktični projekti
- **Aplikacije za klepet Foundry Local**: Izvorna aplikacija za Windows 11 s preklapljanjem modelov
- **Sistemi z več agenti**: Koordinator s specializiranimi agenti za kompleksne delovne tokove  
- **RAG aplikacije**: Lokalna obdelava dokumentov z iskanjem vektorjev
- **Usmerjevalniki modelov**: Pametna izbira med modeli na podlagi analize nalog  
- **API ogrodja**: Pripravljeni odjemalci za produkcijo s pretakanjem in spremljanjem stanja  
- **Orodja za več platform**: Vzorci integracije LangChain/Semantic Kernel  

### 🏢 Industrijske aplikacije  
**Proizvodnja** • **Zdravstvo** • **Avtonomna vozila** • **Pametna mesta** • **Mobilne aplikacije**  

## Hiter začetek  

**Priporočena učna pot** (skupno 20–30 ur):  

0. **📖 Uvod** ([Introduction.md](./introduction.md)): Osnove EdgeAI + industrijski kontekst + učni okvir  
1. **📚 Osnove** (Moduli 01–02): Koncepti EdgeAI + družine modelov SLM  
2. **⚙️ Optimizacija** (Moduli 03–04): Implementacija + ogrodja za kvantizacijo  
3. **🚀 Produkcija** (Moduli 05–06): SLMOps + AI agenti + klicanje funkcij  
4. **💻 Implementacija** (Moduli 07–08): Primeri platform + orodje Foundry Local  

Vsak modul vključuje teorijo, praktične vaje in produkcijsko pripravljene vzorce kode.  

## Vpliv na kariero  

**Tehnične vloge**: Arhitekt rešitev EdgeAI • ML inženir (Edge) • Razvijalec IoT AI • Razvijalec mobilnih AI aplikacij  

**Industrijski sektorji**: Proizvodnja 4.0 • Zdravstvena tehnologija • Avtonomni sistemi • FinTech • Potrošniška elektronika  

**Projekti za portfelj**: Sistemi z več agenti • Produkcijske RAG aplikacije • Implementacija na več platformah • Optimizacija zmogljivosti  

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
  

## Poudarki tečaja  

✅ **Postopno učenje**: Teorija → Praksa → Implementacija v produkciji  
✅ **Resnične študije primerov**: Microsoft, Japan Airlines, implementacije v podjetjih  
✅ **Praktični primeri**: Več kot 50 primerov, 10 obsežnih demo posnetkov Foundry Local  
✅ **Osredotočenost na zmogljivost**: 85 % izboljšanje hitrosti, 75 % zmanjšanje velikosti  
✅ **Več platform**: Windows, mobilne naprave, vgrajeni sistemi, hibridni oblak-edge  
✅ **Pripravljeno za produkcijo**: Spremljanje, skaliranje, varnost, ogrodja za skladnost  

📖 **[Na voljo učni vodič](STUDY_GUIDE.md)**: Strukturirana 20-urna učna pot z usmeritvami za razporeditev časa in orodji za samoocenjevanje.  

---  

**EdgeAI predstavlja prihodnost implementacije AI**: lokalno usmerjeno, zasebnost ohranjajoče in učinkovito. Obvladajte te veščine za razvoj naslednje generacije inteligentnih aplikacij.  

## Drugi tečaji  

Naša ekipa ponuja tudi druge tečaje! Oglejte si:  

- [MCP za začetnike](https://github.com/microsoft/mcp-for-beginners)  
- [AI agenti za začetnike](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Generativni AI za začetnike z uporabo .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
- [Generativni AI za začetnike z uporabo JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
- [Generativni AI za začetnike](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [ML za začetnike](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
- [Podatkovna znanost za začetnike](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
- [AI za začetnike](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
- [Kibernetska varnost za začetnike](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)  
- [Razvoj spletnih aplikacij za začetnike](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
- [IoT za začetnike](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [Razvoj XR za začetnike](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Obvladovanje GitHub Copilot za AI programiranje v paru](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [Obvladovanje GitHub Copilot za razvijalce C#/.NET](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [Izberite svojo Copilot pustolovščino](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

## Pomoč  

Če se zataknete ali imate vprašanja o razvoju AI aplikacij, se pridružite:  

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)  

Če imate povratne informacije o izdelku ali naletite na napake med razvojem, obiščite:  

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)  

---

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.