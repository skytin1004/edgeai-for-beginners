<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ff006cd813df4152f5036e7b2bc5ed32",
  "translation_date": "2025-09-25T02:09:05+00:00",
  "source_file": "README.md",
  "language_code": "sl"
}
-->
# EdgeAI za začetnike

![Slika naslovnice tečaja](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.sl.png)

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

#### Podprto prek GitHub Action (samodejno in vedno posodobljeno)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](./README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

**Če želite dodati dodatne jezike, so podprti jeziki navedeni [tukaj](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Uvod

Dobrodošli v **EdgeAI za začetnike** – vašem celovitem potovanju v preoblikovalni svet Edge umetne inteligence. Ta tečaj povezuje zmogljivosti AI z praktično uporabo na robnih napravah, kar vam omogoča, da izkoristite potencial AI tam, kjer se podatki ustvarjajo in kjer je treba sprejemati odločitve.

### Kaj boste osvojili

Ta tečaj vas vodi od osnovnih konceptov do implementacij, pripravljenih za proizvodnjo, in zajema:
- **Majhni jezikovni modeli (SLM)**, optimizirani za robno uporabo
- **Optimizacija glede na strojno opremo** na različnih platformah
- **Inferenca v realnem času** z ohranjanjem zasebnosti
- **Strategije za proizvodno uporabo** v poslovnih aplikacijah

### Zakaj je EdgeAI pomemben

Edge AI predstavlja premik paradigme, ki rešuje ključne sodobne izzive:
- **Zasebnost in varnost**: Obdelava občutljivih podatkov lokalno, brez izpostavljanja v oblaku
- **Zmogljivost v realnem času**: Odprava omrežne zakasnitve za časovno kritične aplikacije
- **Učinkovitost stroškov**: Zmanjšanje stroškov pasovne širine in računalništva v oblaku
- **Odporne operacije**: Ohranitev funkcionalnosti med izpadi omrežja
- **Skladnost z regulativami**: Izpolnjevanje zahtev glede suverenosti podatkov

### Edge AI

Edge AI se nanaša na izvajanje algoritmov umetne inteligence in jezikovnih modelov lokalno na strojni opremi, blizu mesta, kjer se podatki ustvarjajo, brez zanašanja na oblačne vire za inferenco. To zmanjšuje zakasnitev, izboljšuje zasebnost in omogoča sprejemanje odločitev v realnem času.

### Temeljna načela:
- **Inferenca na napravi**: AI modeli se izvajajo na robnih napravah (telefoni, usmerjevalniki, mikrokrmilniki, industrijski računalniki)
- **Zmožnost delovanja brez povezave**: Deluje brez stalne internetne povezave
- **Nizka zakasnitev**: Takojšnji odzivi, primerni za sisteme v realnem času
- **Suverenost podatkov**: Občutljivi podatki ostanejo lokalni, kar izboljšuje varnost in skladnost

### Majhni jezikovni modeli (SLM)

SLM, kot so Phi-4, Mistral-7B in Gemma, so optimizirane različice večjih LLM – trenirane ali destilirane za:
- **Zmanjšano porabo pomnilnika**: Učinkovita uporaba omejenega pomnilnika robnih naprav
- **Manjše zahteve po računalniški moči**: Optimizirano za zmogljivost CPU in robnih GPU
- **Hitrejši zagonski časi**: Hitro inicializacijo za odzivne aplikacije

Omogočajo zmogljive NLP zmožnosti, hkrati pa izpolnjujejo omejitve:
- **Vgrajeni sistemi**: IoT naprave in industrijski krmilniki
- **Mobilne naprave**: Pametni telefoni in tablice z zmožnostjo delovanja brez povezave
- **IoT naprave**: Senzorji in pametne naprave z omejenimi viri
- **Robni strežniki**: Lokalni procesni enoti z omejenimi GPU viri
- **Osebni računalniki**: Scenariji uporabe na namiznih in prenosnih računalnikih

## Moduli tečaja in navigacija

| Modul | Tema | Osrednje področje | Ključna vsebina | Stopnja | Trajanje |
|-------|------|-------------------|-----------------|---------|----------|
| [📚 01](../../Module01) | [Osnove EdgeAI](./Module01/README.md) | Primerjava med oblakom in Edge AI | Osnove EdgeAI • Študije primerov iz resničnega sveta • Vodnik za implementacijo • Robna uporaba | Začetnik | 3-4 ure |
| [🧠 02](../../Module02) | [Osnove modelov SLM](./Module02/README.md) | Družine modelov in arhitektura | Družina Phi • Družina Qwen • Družina Gemma • BitNET • μModel • Phi-Silica | Začetnik | 4-5 ur |
| [🚀 03](../../Module03) | [Praksa uporabe SLM](./Module03/README.md) | Lokalna in oblačna uporaba | Napredno učenje • Lokalno okolje • Uporaba v oblaku | Srednje | 4-5 ur |
| [⚙️ 04](../../Module04) | [Orodje za optimizacijo modelov](./Module04/README.md) | Optimizacija na različnih platformah | Uvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sinteza delovnih tokov | Srednje | 5-6 ur |
| [🔧 05](../../Module05) | [SLMOps v proizvodnji](./Module05/README.md) | Operacije v proizvodnji | Uvod v SLMOps • Destilacija modelov • Fino prilagajanje • Uporaba v proizvodnji | Napredno | 5-6 ur |
| [🤖 06](../../Module06) | [AI agenti in klicanje funkcij](./Module06/README.md) | Okviri agentov in MCP | Uvod v agente • Klicanje funkcij • Protokol konteksta modela | Napredno | 4-5 ur |
| [💻 07](../../Module07) | [Implementacija platforme](./Module07/README.md) | Primeri uporabe na različnih platformah | AI orodje • Foundry Local • Razvoj za Windows | Napredno | 3-4 ure |
| [🏭 08](../../Module08) | [Orodje Foundry Local](./Module08/README.md) | Primeri, pripravljeni za proizvodnjo | Vzorčne aplikacije (glejte podrobnosti spodaj) | Strokovno | 8-10 ur |

### 🏭 **Modul 08: Vzorčne aplikacije**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK Integration](./Module08/samples/02/README.md)
- [03: Model Discovery & Benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG Application](./Module08/samples/04/README.md)
- [05: Multi-Agent Orchestration](./Module08/samples/05/README.md)
- [06: Models-as-Tools Router](./Module08/samples/06/README.md)
- [07: Direct API Client](./Module08/samples/07/README.md)
- [08: Windows 11 Chat App](./Module08/samples/08/README.md)
- [09: Advanced Multi-Agent System](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 📊 **Povzetek učne poti**
- **Skupno trajanje**: 36-45 ur
- **Pot za začetnike**: Moduli 01-02 (7-9 ur)  
- **Srednja pot**: Moduli 03-04 (9-11 ur)
- **Napredna pot**: Moduli 05-07 (12-15 ur)
- **Strokovna pot**: Modul 08 (8-10 ur)

## Kaj boste ustvarili

### 🎯 Ključne kompetence
- **Arhitektura Edge AI**: Oblikovanje sistemov AI, ki delujejo lokalno, z integracijo v oblak
- **Optimizacija modelov**: Kvantizacija in stiskanje modelov za robno uporabo (85% hitrostna izboljšava, 75% zmanjšanje velikosti)
- **Uporaba na več platformah**: Windows, mobilne naprave, vgrajeni sistemi in hibridni sistemi oblak-rob
- **Operacije v proizvodnji**: Spremljanje, skaliranje in vzdrževanje Edge AI v proizvodnji

### 🏗️ Praktični projekti
- **Foundry Local Chat Apps**: Windows 11 aplikacija z možnostjo preklapljanja modelov
- **Sistemi z več agenti**: Koordinator s specialističnimi agenti za kompleksne delovne tokove  
- **RAG aplikacije**: Lokalna obdelava dokumentov z iskanjem vektorjev
- **Usmerjevalniki modelov**: Inteligentna izbira med modeli glede na analizo nalog
- **Okviri API**: Stranke, pripravljene za proizvodnjo, s pretakanjem in spremljanjem stanja
- **Orodja za več platform**: Vzorci integracije LangChain/Semantic Kernel

### 🏢 Industrijske aplikacije
**Proizvodnja** • **Zdravstvo** • **Avtonomna vozila** • **Pametna mesta** • **Mobilne aplikacije**

## Hitri začetek

**Priporočena učna pot** (skupno 20-30 ur):

1. **📚 Osnove** (Moduli 01-02): Koncepti EdgeAI + družine modelov SLM
2. **⚙️ Optimizacija** (Moduli 03-04): Uporaba + okviri za kvantizacijo  
3. **🚀 Proizvodnja** (Moduli 05-06): SLMOps + AI agenti + klicanje funkcij
4. **💻 Implementacija** (Moduli 07-08): Primeri uporabe na platformah + orodje Foundry Local

Vsak modul vključuje teorijo, praktične vaje in vzorce kode, pripravljene za proizvodnjo.

## Vpliv na kariero
**Tehnične vloge**: EdgeAI Solutions Architect • ML inženir (Edge) • IoT AI razvijalec • Mobilni AI razvijalec

**Industrijski sektorji**: Industrija 4.0 • Zdravstvena tehnologija • Avtonomni sistemi • FinTech • Potrošniška elektronika

**Portfeljski projekti**: Sistemi z več agenti • RAG aplikacije za proizvodnjo • Čezplatformska implementacija • Optimizacija zmogljivosti

## Struktura repozitorija

```
edgeai-for-beginners/
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

✅ **Progresivno učenje**: Teorija → Praksa → Implementacija v produkciji  
✅ **Resnične študije primerov**: Microsoft, Japan Airlines, implementacije v podjetjih  
✅ **Praktični primeri**: 50+ primerov, 10 obsežnih Foundry Local demonstracij  
✅ **Osredotočenost na zmogljivost**: 85% izboljšanje hitrosti, 75% zmanjšanje velikosti  
✅ **Večplatformska podpora**: Windows, mobilne naprave, vgrajeni sistemi, hibridni oblak-edge  
✅ **Pripravljeno za produkcijo**: Spremljanje, skaliranje, varnost, okvirji skladnosti

📖 **[Na voljo učni vodič](STUDY_GUIDE.md)**: Strukturirana 20-urna učna pot z usmeritvami za razporeditev časa in orodji za samoocenjevanje.

---

**EdgeAI predstavlja prihodnost implementacije AI**: lokalno usmerjeno, zasebnost ohranjajoče in učinkovito. Obvladajte te veščine za razvoj naslednje generacije inteligentnih aplikacij.

## Drugi tečaji

Naša ekipa ponuja tudi druge tečaje! Oglejte si:

- [MCP za začetnike](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti za začetnike](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Generativni AI za začetnike z uporabo .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [Generativni AI za začetnike z uporabo JavaScripta](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [Generativni AI za začetnike](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML za začetnike](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Podatkovna znanost za začetnike](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI za začetnike](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Kibernetska varnost za začetnike](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Spletni razvoj za začetnike](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT za začetnike](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR razvoj za začetnike](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Obvladovanje GitHub Copilot za AI programiranje v paru](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [Obvladovanje GitHub Copilot za C#/.NET razvijalce](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Izberite svojo Copilot pustolovščino](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

