<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c817161ba08864340737d623f761b9ae",
  "translation_date": "2025-09-18T21:13:32+00:00",
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

Dobrodošli v **EdgeAI za začetnike** – vašem celovitem potovanju v preoblikovalni svet umetne inteligence na robu. Ta tečaj povezuje zmogljivosti umetne inteligence z praktično uporabo na napravah na robu, kar vam omogoča, da izkoristite potencial AI neposredno tam, kjer se podatki ustvarjajo in kjer je treba sprejemati odločitve.

### Kaj boste osvojili

Ta tečaj vas vodi od osnovnih konceptov do implementacij, pripravljenih za proizvodnjo, in zajema:
- **Majhni jezikovni modeli (SLM)**, optimizirani za uporabo na robu
- **Optimizacija glede na strojno opremo** na različnih platformah
- **Inferenca v realnem času** z ohranjanjem zasebnosti
- **Strategije za proizvodno uporabo** v poslovnih aplikacijah

### Zakaj je EdgeAI pomemben

Edge AI predstavlja spremembo paradigme, ki obravnava ključne sodobne izzive:
- **Zasebnost in varnost**: Obdelava občutljivih podatkov lokalno, brez izpostavljanja oblaku
- **Zmogljivost v realnem času**: Odprava zakasnitve omrežja za aplikacije, kjer je čas ključnega pomena
- **Učinkovitost stroškov**: Zmanjšanje stroškov pasovne širine in računalništva v oblaku
- **Odporne operacije**: Ohranitev funkcionalnosti med izpadi omrežja
- **Skladnost z regulativami**: Izpolnjevanje zahtev glede suverenosti podatkov

### Edge AI

Edge AI se nanaša na izvajanje algoritmov umetne inteligence in jezikovnih modelov lokalno na strojni opremi – blizu mesta, kjer se podatki ustvarjajo – brez zanašanja na oblačne vire za inferenco. Zmanjšuje zakasnitev, izboljšuje zasebnost in omogoča sprejemanje odločitev v realnem času.

### Temeljna načela:
- **Inferenca na napravi**: AI modeli se izvajajo na napravah na robu (telefoni, usmerjevalniki, mikrokrmilniki, industrijski računalniki)
- **Zmožnost delovanja brez povezave**: Deluje brez stalne internetne povezave
- **Nizka zakasnitev**: Takojšnji odzivi, primerni za sisteme v realnem času
- **Suverenost podatkov**: Občutljivi podatki ostanejo lokalni, kar izboljšuje varnost in skladnost

### Majhni jezikovni modeli (SLM)

SLM, kot so Phi-4, Mistral-7B in Gemma, so optimizirane različice večjih LLM – trenirane ali destilirane za:
- **Zmanjšano porabo pomnilnika**: Učinkovita uporaba omejenega pomnilnika naprav na robu
- **Manjše zahteve po računalniški moči**: Optimizirano za delovanje na CPU in GPU naprav na robu
- **Hitrejši zagonski časi**: Hitro inicializacijo za odzivne aplikacije

Omogočajo zmogljive NLP zmožnosti, hkrati pa izpolnjujejo omejitve:
- **Vgrajeni sistemi**: IoT naprave in industrijski krmilniki
- **Mobilne naprave**: Pametni telefoni in tablice z zmožnostjo delovanja brez povezave
- **IoT naprave**: Senzorji in pametne naprave z omejenimi viri
- **Strežniki na robu**: Lokalni procesni enoti z omejenimi GPU viri
- **Osebni računalniki**: Scenariji uporabe na namiznih in prenosnih računalnikih

## Arhitektura tečaja

### [Modul 01: Osnove EdgeAI in preoblikovanje](./Module01/README.md)
**Tema**: Preoblikovalni premik pri uporabi Edge AI

#### Struktura poglavja:
- [**Razdelek 1: Osnove EdgeAI**](./Module01/01.EdgeAIFundamentals.md)
  - Primerjava tradicionalne oblačne AI in Edge AI
  - Izzivi in omejitve pri robnem računalništvu
  - Ključne tehnologije: kvantizacija modelov, optimizacija stiskanja, majhni jezikovni modeli (SLM)
  - Pospeševanje strojne opreme: NPUs, optimizacija GPU, optimizacija CPU
  - Prednosti: varnost zasebnosti, nizka zakasnitev, zmožnost delovanja brez povezave, stroškovna učinkovitost

- [**Razdelek 2: Študije primerov iz resničnega sveta**](./Module01/02.RealWorldCaseStudies.md)
  - Ekosistem modelov Microsoft Phi & Mu
  - Študija primera AI poročanja pri Japan Airlines
  - Vpliv na trg in prihodnje smernice
  - Premisleki in najboljše prakse pri uporabi

- [**Razdelek 3: Praktični vodnik za implementacijo**](./Module01/03.PracticalImplementationGuide.md)
  - Nastavitev razvojnega okolja (Python 3.10+, .NET 8+)
  - Zahteve glede strojne opreme in priporočene konfiguracije
  - Viri družine osnovnih modelov
  - Orodja za kvantizacijo in optimizacijo (Llama.cpp, Microsoft Olive, Apple MLX)
  - Kontrolni seznam za ocenjevanje in preverjanje

- [**Razdelek 4: Strojne platforme za uporabo Edge AI**](./Module01/04.EdgeDeployment.md)
  - Premisleki in zahteve za uporabo Edge AI
  - Intelova strojna oprema za Edge AI in tehnike optimizacije
  - Qualcommove AI rešitve za mobilne in vgrajene sisteme
  - NVIDIA Jetson in platforme za robno računalništvo
  - Windows AI PC platforme z NPU pospeševanjem
  - Strategije optimizacije, specifične za strojno opremo

---

### [Modul 02: Osnove majhnih jezikovnih modelov](./Module02/README.md)
**Tema**: Teoretična načela SLM, strategije implementacije in uporaba v proizvodnji

#### Struktura poglavja:
- [**Razdelek 1: Osnove družine modelov Microsoft Phi**](./Module02/01.PhiFamily.md)
  - Evolucija filozofije oblikovanja (Phi-1 do Phi-4)
  - Oblikovanje arhitekture z učinkovitostjo na prvem mestu
  - Specializirane zmožnosti (razmišljanje, multimodalnost, uporaba na robu)

- [**Razdelek 2: Osnove družine Qwen**](./Module02/02.QwenFamily.md)
  - Odličnost odprte kode (Qwen 1.0 do Qwen3) – na voljo prek Hugging Face
  - Napredna arhitektura razmišljanja z zmožnostmi načina razmišljanja
  - Možnosti skalabilne uporabe (0.5B-235B parametrov)

- [**Razdelek 3: Osnove družine Gemma**](./Module02/03.GemmaFamily.md)
  - Inovacije, ki jih vodi raziskovanje (Gemma 3 & 3n)
  - Multimodalna odličnost
  - Arhitektura, osredotočena na mobilne naprave

- [**Razdelek 4: Osnove družine BitNET**](./Module02/04.BitNETFamily.md)
  - Revolucionarna tehnologija kvantizacije (1.58-bit)
  - Specializiran okvir za inferenco s https://github.com/microsoft/BitNet
  - Trajnostno vodstvo AI prek ekstremne učinkovitosti

- [**Razdelek 5: Osnove modela Microsoft Mu**](./Module02/05.mumodel.md)
  - Arhitektura, osredotočena na naprave, vgrajena v Windows 11
  - Integracija sistema z nastavitvami Windows 11
  - Zasebnost, ki omogoča delovanje brez povezave

- [**Razdelek 6: Osnove Phi-Silica**](./Module02/06.phisilica.md)
  - Arhitektura, optimizirana za NPU, vgrajena v Windows 11 Copilot+ PC-je
  - Izjemna učinkovitost (650 tokenov/sekundo pri 1.5W)
  - Integracija za razvijalce z Windows App SDK

---

### [Modul 03: Uporaba majhnih jezikovnih modelov](./Module03/README.md)
**Tema**: Celoten življenjski cikel uporabe SLM, od teorije do proizvodnega okolja

#### Struktura poglavja:
- [**Razdelek 1: Napredno učenje SLM**](./Module03/01.SLMAdvancedLearning.md)
  - Okvir za razvrščanje parametrov (Micro SLM 100M-1.4B, Medium SLM 14B-30B)
  - Napredne tehnike optimizacije (metode kvantizacije, BitNET 1-bit kvantizacija)
  - Strategije pridobivanja modelov (Azure AI Foundry za modele Phi, Hugging Face za izbrane modele)

- [**Razdelek 2: Uporaba v lokalnem okolju**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama univerzalna platforma za uporabo
  - Lokalne rešitve Microsoft Foundry za podjetja
  - Primerjalna analiza okvirov

- [**Razdelek 3: Uporaba v oblaku s kontejnerji**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM uporaba za inferenco z visoko zmogljivostjo
  - Orkestracija kontejnerjev Ollama
  - Edge-optimizirana implementacija ONNX Runtime

---

### [Modul 04: Pretvorba formatov modelov in kvantizacija](./Module04/README.md)
**Tema**: Celoten komplet orodij za optimizacijo modelov za uporabo na robu na različnih platformah

#### Struktura poglavja:
- [**Razdelek 1: Osnove pretvorbe formatov modelov in kvantizacije**](./Module04/01.Introduce.md)
  - Okvir za razvrščanje natančnosti (ultra-nizka, nizka, srednja natančnost)
  - Prednosti formatov GGUF in ONNX ter primeri uporabe
  - Prednosti kvantizacije za operativno učinkovitost
  - Primerjalne analize zmogljivosti in porabe pomnilnika
- [**Oddelek 2: Llama.cpp Vodnik za implementacijo**](./Module04/02.Llamacpp.md)
  - Namestitev na več platformah (Windows, macOS, Linux)
  - Pretvorba v format GGUF in ravni kvantizacije (Q2_K do Q8_0)
  - Pospeševanje strojne opreme (CUDA, Metal, OpenCL, Vulkan)
  - Integracija s Pythonom in uvedba REST API-ja

- [**Oddelek 3: Microsoft Olive Optimizacijski paket**](./Module04/03.MicrosoftOlive.md)
  - Optimizacija modelov, prilagojena strojni opremi, z več kot 40 vgrajenimi komponentami
  - Samodejna optimizacija z dinamično in statično kvantizacijo
  - Integracija v podjetniške delovne tokove Azure ML
  - Podpora za priljubljene modele (Llama, Phi, izbrane modele Qwen, Gemma)

- [**Oddelek 4: OpenVINO Toolkit Optimizacijski paket**](./Module04/04.openvino.md)
  - Intelov odprtokodni paket za uvajanje AI na več platformah
  - Okvir za stiskanje nevronskih mrež (NNCF) za napredno optimizacijo
  - OpenVINO GenAI za uvajanje velikih jezikovnih modelov
  - Pospeševanje strojne opreme na CPU, GPU, VPU in AI pospeševalnikih

- [**Oddelek 5: Apple MLX Framework - poglobljen pregled**](./Module04/05.AppleMLX.md)
  - Enotna arhitektura pomnilnika za Apple Silicon
  - Podpora za LLaMA, Mistral, Phi-3, izbrane modele Qwen
  - LoRA prilagoditev in prilagajanje modelov
  - Integracija s Hugging Face z 4-bitno/8-bitno kvantizacijo

- [**Oddelek 6: Sinteza delovnega toka za razvoj Edge AI**](./Module04/06.workflow-synthesis.md)
  - Enotna arhitektura delovnega toka, ki združuje več optimizacijskih paketov
  - Odločitvena drevesa za izbiro okvirjev in analiza kompromisov zmogljivosti
  - Validacija pripravljenosti za produkcijo in celovite strategije uvajanja
  - Strategije za prihodnost za nove strojne opreme in arhitekture modelov

---

### [Modul 05: SLMOps - Operacije za majhne jezikovne modele](./Module05/README.md)
**Tema**: Celoten življenjski cikel SLM od destilacije do uvajanja v produkcijo

#### Struktura poglavij:
- [**Oddelek 1: Uvod v SLMOps**](./Module05/01.IntroduceSLMOps.md)
  - Paradigmatski premik SLMOps v AI operacijah
  - Stroškovna učinkovitost in arhitektura, osredotočena na zasebnost
  - Strateški poslovni vpliv in konkurenčne prednosti
  - Izzivi in rešitve pri implementaciji v resničnem svetu

- [**Oddelek 2: Destilacija modelov - od teorije do prakse**](./Module05/02.SLMOps-Distillation.md)
  - Prenos znanja iz učiteljskih v študentske modele
  - Implementacija dvostopenjskega procesa destilacije
  - Delovni tokovi destilacije Azure ML s praktičnimi primeri
  - 85% zmanjšanje časa sklepanja z ohranitvijo 92% natančnosti

- [**Oddelek 3: Fino prilagajanje - prilagoditev modelov za specifične naloge**](./Module05/03.SLMOps-Finetuing.md)
  - Tehnike učinkovitega fine-tuninga (PEFT)
  - Napredne metode LoRA in QLoRA
  - Implementacija fine-tuninga z Microsoft Olive
  - Večadapterno usposabljanje in optimizacija hiperparametrov

- [**Oddelek 4: Uvajanje - implementacija pripravljena na produkcijo**](./Module05/04.SLMOps.Deployment.md)
  - Pretvorba modelov in kvantizacija za produkcijo
  - Konfiguracija lokalnega uvajanja Foundry
  - Primerjalno testiranje zmogljivosti in validacija kakovosti
  - 75% zmanjšanje velikosti z nadzorom produkcije

---

### [Modul 06: SLM Agentni sistemi - AI agenti in klic funkcij](./Module06/README.md)
**Tema**: Implementacija SLM agentnih sistemov od osnov do naprednega klica funkcij in integracije Model Context Protocol

#### Struktura poglavij:
- [**Oddelek 1: AI agenti in osnove majhnih jezikovnih modelov**](./Module06/01.IntroduceAgent.md)
  - Okvir za klasifikacijo agentov (refleksni, na modelu temelječi, ciljno usmerjeni, učni agenti)
  - Osnove SLM in strategije optimizacije (GGUF, kvantizacija, robni okvirji)
  - Analiza kompromisov med SLM in LLM (10-30× zmanjšanje stroškov, 70-80% učinkovitost nalog)
  - Praktično uvajanje z Ollama, VLLM in Microsoft edge rešitvami

- [**Oddelek 2: Klic funkcij v majhnih jezikovnih modelih**](./Module06/02.FunctionCalling.md)
  - Sistematična implementacija delovnega toka (zaznavanje namena, JSON izhod, zunanja izvedba)
  - Implementacije, specifične za platformo (Phi-4-mini, izbrani modeli Qwen, Microsoft Foundry Local)
  - Napredni primeri (sodelovanje več agentov, dinamična izbira orodij)
  - Premisleki za produkcijo (omejevanje hitrosti, beleženje revizij, varnostni ukrepi)

- [**Oddelek 3: Integracija Model Context Protocol (MCP)**](./Module06/03.IntroduceMCP.md)
  - Arhitektura protokola in zasnova slojevitih sistemov
  - Podpora za več zaledij (Ollama za razvoj, vLLM za produkcijo)
  - Povezovalni protokoli (STDIO in SSE načini)
  - Resnične aplikacije (spletna avtomatizacija, obdelava podatkov, integracija API-jev)

---

### [Modul 07: Primeri implementacije EdgeAI](./Module07/README.md)
**Tema**: Celovite implementacije EdgeAI na različnih platformah in okvirjih

#### Struktura poglavij:
- [**AI orodjarna za Visual Studio Code**](./Module07/aitoolkit.md)
  - Celovito razvojno okolje Edge AI znotraj VS Code
  - Katalog modelov in odkrivanje za robno uvajanje
  - Lokalno testiranje, optimizacija in delovni tokovi razvoja agentov
  - Spremljanje zmogljivosti in ocenjevanje za robne scenarije

- [**Vodnik za razvoj EdgeAI na Windows**](./Module07/windowdeveloper.md)
  - Celovit pregled platforme Windows AI Foundry
  - Phi Silica API za učinkovito sklepanje na NPU
  - API-ji za računalniški vid za obdelavo slik in OCR
  - Foundry Local CLI za lokalni razvoj in testiranje

- [**EdgeAI na NVIDIA Jetson Orin Nano**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 67 TOPS AI zmogljivosti v velikosti kreditne kartice
  - Podpora za generativne AI modele (transformatorji za vid, LLM, modeli za vid-jezik)
  - Aplikacije v robotiki, dronih, inteligentnih kamerah, avtonomnih napravah
  - Dostopna platforma za $249 za demokratiziran AI razvoj

- [**EdgeAI v mobilnih aplikacijah z .NET MAUI in ONNX Runtime GenAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - Mobilni AI na več platformah z enotno C# kodo
  - Podpora za pospeševanje strojne opreme (CPU, GPU, mobilni AI procesorji)
  - Optimizacije, specifične za platformo (CoreML za iOS, NNAPI za Android)
  - Celovita implementacija generativnega AI cikla

- [**EdgeAI v Azure z motorjem za majhne jezikovne modele**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - Hibridna arhitektura uvajanja med oblakom in robom
  - Integracija Azure AI storitev z ONNX Runtime
  - Uvajanje na ravni podjetja in stalno upravljanje modelov
  - Hibridni AI delovni tokovi za inteligentno obdelavo dokumentov

- [**EdgeAI z Windows ML**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Temelj platforme Windows AI Foundry za zmogljivo sklepanje na napravi
  - Univerzalna podpora za strojno opremo (AMD, Intel, NVIDIA, Qualcomm silicij)
  - Samodejna abstrakcija strojne opreme in optimizacija
  - Enoten okvir za raznolik ekosistem strojne opreme Windows

- [**EdgeAI z lokalnimi aplikacijami Foundry**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - Implementacija RAG, osredotočena na zasebnost, z lokalnimi viri
  - Integracija jezikovnega modela Phi-3 s semantičnim iskanjem (samo modeli Phi)
  - Podpora za lokalne vektorske baze podatkov (SQLite, Qdrant)
  - Zmožnosti suverenosti podatkov in delovanja brez povezave

## Cilji učenja tečaja

Z zaključkom tega celovitega tečaja EdgeAI boste pridobili strokovno znanje za načrtovanje, implementacijo in uvajanje rešitev EdgeAI, pripravljenih na produkcijo. Naš strukturiran pristop zagotavlja, da obvladate tako teoretične osnove kot praktične veščine implementacije.
Ta tečaj vas postavi v ospredje uvajanja AI tehnologij, kjer se inteligentne zmogljivosti brezhibno integrirajo v naprave in sisteme, ki poganjajo sodobno življenje.

## Diagram strukture datotek

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

## Značilnosti tečaja

- **Postopno učenje**: Postopno napredovanje od osnovnih konceptov do napredne implementacije
- **Integracija teorije in prakse**: Vsak modul vključuje tako teoretične osnove kot praktične operacije
- **Resnične študije primerov**: Na podlagi dejanskih primerov iz Microsofta, Alibabe, Googla in drugih
- **Praktične vaje**: Izpolnjevanje konfiguracijskih datotek, postopki testiranja API-jev in skripte za implementacijo
- **Merila zmogljivosti**: Podrobne primerjave hitrosti sklepanja, porabe pomnilnika in zahtev po virih
- **Razmisleki na ravni podjetja**: Prakse varnosti, okvirji skladnosti in strategije zaščite podatkov

## Začetek

Priporočena učna pot:
1. Začnite z **Module01**, da pridobite osnovno razumevanje EdgeAI
2. Nadaljujte z **Module02**, da podrobno spoznate različne družine modelov SLM
3. Naučite se **Module03**, da obvladate praktične veščine implementacije
4. Nadaljujte z **Module04** za napredno optimizacijo modelov, pretvorbo formatov in sintezo okvirjev
5. Zaključite z **Module05**, da obvladate SLMOps za implementacije, pripravljene za proizvodnjo
6. Raziskujte **Module06**, da razumete agentne sisteme SLM in zmogljivosti klicanja funkcij
7. Zaključite z **Module07**, da pridobite praktične izkušnje z AI Toolkit in raznolikimi primeri implementacije EdgeAI

Vsak modul je zasnovan kot samostojna celota, vendar bo zaporedno učenje prineslo najboljše rezultate.

## Vodnik za študij

Na voljo je celovit [Vodnik za študij](STUDY_GUIDE.md), ki vam bo pomagal kar najbolje izkoristiti vaše učenje. Vodnik za študij vključuje:

- **Strukturirane učne poti**: Optimizirani urniki za dokončanje tečaja v 20 urah
- **Smernice za razporeditev časa**: Specifična priporočila za uravnoteženje branja, vaj in projektov
- **Osredotočenost na ključne koncepte**: Prednostne učne cilje za vsak modul
- **Orodja za samoocenjevanje**: Vprašanja in vaje za preverjanje vašega razumevanja
- **Ideje za mini projekte**: Praktične aplikacije za utrditev vašega znanja

Vodnik za študij je zasnovan tako, da ustreza intenzivnemu učenju (1 teden) in študiju s krajšim delovnim časom (3 tedne), s jasnimi smernicami, kako učinkovito razporediti čas, tudi če lahko tečaju namenite le 10 ur.

---

**Prihodnost EdgeAI temelji na nenehnem izboljševanju arhitektur modelov, tehnik kvantizacije in strategij implementacije, ki dajejo prednost učinkovitosti in specializaciji pred splošnimi zmogljivostmi. Organizacije, ki sprejmejo to spremembo paradigme, bodo dobro pripravljene na izkoriščanje transformativnega potenciala AI, hkrati pa ohranjale nadzor nad svojimi podatki in operacijami.**

## Drugi tečaji

Naša ekipa pripravlja tudi druge tečaje! Oglejte si:

- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents For Beginners](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners using JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML for Beginners](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Data Science for Beginners](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI for Beginners](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT for Beginners](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for AI Paired Programming](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.