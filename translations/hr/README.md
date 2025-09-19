<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c817161ba08864340737d623f761b9ae",
  "translation_date": "2025-09-18T21:10:12+00:00",
  "source_file": "README.md",
  "language_code": "hr"
}
-->
# EdgeAI za početnike

![Slika naslovnice tečaja](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.hr.png)

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
3. [**Pridružite se Azure AI Foundry Discordu i upoznajte stručnjake i kolege programere**](https://discord.com/invite/ByRwuEEgH4)  

### 🌐 Podrška za više jezika

#### Podržano putem GitHub Action (Automatizirano i uvijek ažurirano)

[Arapski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bugarski](../bg/README.md) | [Burmanski (Mjanmar)](../my/README.md) | [Kineski (pojednostavljeni)](../zh/README.md) | [Kineski (tradicionalni, Hong Kong)](../hk/README.md) | [Kineski (tradicionalni, Makao)](../mo/README.md) | [Kineski (tradicionalni, Tajvan)](../tw/README.md) | [Hrvatski](./README.md) | [Češki](../cs/README.md) | [Danski](../da/README.md) | [Nizozemski](../nl/README.md) | [Finski](../fi/README.md) | [Francuski](../fr/README.md) | [Njemački](../de/README.md) | [Grčki](../el/README.md) | [Hebrejski](../he/README.md) | [Hindski](../hi/README.md) | [Mađarski](../hu/README.md) | [Indonezijski](../id/README.md) | [Talijanski](../it/README.md) | [Japanski](../ja/README.md) | [Korejski](../ko/README.md) | [Malajski](../ms/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Norveški](../no/README.md) | [Perzijski (Farsi)](../fa/README.md) | [Poljski](../pl/README.md) | [Portugalski (Brazil)](../br/README.md) | [Portugalski (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumunjski](../ro/README.md) | [Ruski](../ru/README.md) | [Srpski (ćirilica)](../sr/README.md) | [Slovački](../sk/README.md) | [Slovenski](../sl/README.md) | [Španjolski](../es/README.md) | [Svahili](../sw/README.md) | [Švedski](../sv/README.md) | [Tagalog (Filipinski)](../tl/README.md) | [Tajlandski](../th/README.md) | [Turski](../tr/README.md) | [Ukrajinski](../uk/README.md) | [Urdu](../ur/README.md) | [Vijetnamski](../vi/README.md)

**Ako želite da se podrže dodatni jezici, popis podržanih jezika nalazi se [ovdje](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Uvod

Dobrodošli u **EdgeAI za početnike** – vaš sveobuhvatan put u transformativni svijet rubne umjetne inteligencije. Ovaj tečaj povezuje moćne AI mogućnosti s praktičnom primjenom u stvarnom svijetu na rubnim uređajima, omogućujući vam da iskoristite potencijal AI-a tamo gdje se podaci generiraju i odluke trebaju donositi.

### Što ćete savladati

Ovaj tečaj vas vodi od osnovnih pojmova do implementacija spremnih za proizvodnju, pokrivajući:
- **Mali jezični modeli (SLM)** optimizirani za rubnu primjenu
- **Optimizacija prilagođena hardveru** na raznim platformama
- **Inference u stvarnom vremenu** uz očuvanje privatnosti
- **Strategije implementacije** za poslovne aplikacije

### Zašto je EdgeAI važan

Edge AI predstavlja promjenu paradigme koja rješava ključne moderne izazove:
- **Privatnost i sigurnost**: Obrada osjetljivih podataka lokalno, bez izlaganja oblaku
- **Performanse u stvarnom vremenu**: Eliminacija mrežne latencije za aplikacije osjetljive na vrijeme
- **Učinkovitost troškova**: Smanjenje troškova propusnosti i računalnih resursa u oblaku
- **Otpornost operacija**: Održavanje funkcionalnosti tijekom prekida mreže
- **Regulatorna usklađenost**: Zadovoljavanje zahtjeva za suverenitetom podataka

### Edge AI

Edge AI odnosi se na pokretanje AI algoritama i jezičnih modela lokalno na hardveru – blizu mjesta gdje se podaci generiraju – bez oslanjanja na resurse oblaka za inference. Smanjuje latenciju, poboljšava privatnost i omogućuje donošenje odluka u stvarnom vremenu.

### Osnovni principi:
- **Inference na uređaju**: AI modeli se pokreću na rubnim uređajima (telefonima, ruterima, mikrokontrolerima, industrijskim PC-ima)
- **Offline sposobnost**: Funkcionira bez stalne internetske povezanosti
- **Niska latencija**: Trenutni odgovori prilagođeni sustavima u stvarnom vremenu
- **Suverenitet podataka**: Zadržava osjetljive podatke lokalno, poboljšavajući sigurnost i usklađenost

### Mali jezični modeli (SLM)

SLM-ovi poput Phi-4, Mistral-7B i Gemma su optimizirane verzije većih LLM-ova – trenirani ili destilirani za:
- **Smanjeni memorijski otisak**: Učinkovito korištenje ograničene memorije rubnih uređaja
- **Niži zahtjevi za računalnu snagu**: Optimizirani za performanse CPU-a i rubnih GPU-a
- **Brže vrijeme pokretanja**: Brza inicijalizacija za responzivne aplikacije

Oni omogućuju moćne NLP mogućnosti dok zadovoljavaju ograničenja:
- **Ugrađeni sustavi**: IoT uređaji i industrijski kontroleri
- **Mobilni uređaji**: Pametni telefoni i tableti s offline sposobnostima
- **IoT uređaji**: Senzori i pametni uređaji s ograničenim resursima
- **Rubni serveri**: Lokalni procesni uređaji s ograničenim GPU resursima
- **Osobna računala**: Scenariji implementacije na stolnim i prijenosnim računalima

## Struktura tečaja

### [Modul 01: Osnove EdgeAI i transformacija](./Module01/README.md)  
**Tema**: Transformativna promjena u implementaciji Edge AI-a  

#### Struktura poglavlja:
- [**Sekcija 1: Osnove EdgeAI**](./Module01/01.EdgeAIFundamentals.md)  
  - Usporedba tradicionalnog AI-a u oblaku i Edge AI-a  
  - Izazovi i ograničenja rubnog računalstva  
  - Ključne tehnologije: kvantizacija modela, optimizacija kompresije, mali jezični modeli (SLM)  
  - Hardverska akceleracija: NPU-ovi, optimizacija GPU-a, optimizacija CPU-a  
  - Prednosti: privatnost, sigurnost, niska latencija, offline sposobnosti, troškovna učinkovitost  

- [**Sekcija 2: Studije slučaja iz stvarnog svijeta**](./Module01/02.RealWorldCaseStudies.md)  
  - Ekosustav modela Microsoft Phi & Mu  
  - Studija slučaja AI sustava izvještavanja Japan Airlinesa  
  - Utjecaj na tržište i budući smjerovi  
  - Razmatranja i najbolje prakse za implementaciju  

- [**Sekcija 3: Praktični vodič za implementaciju**](./Module01/03.PracticalImplementationGuide.md)  
  - Postavljanje razvojnog okruženja (Python 3.10+, .NET 8+)  
  - Hardverski zahtjevi i preporučene konfiguracije  
  - Resursi obitelji osnovnih modela  
  - Alati za kvantizaciju i optimizaciju (Llama.cpp, Microsoft Olive, Apple MLX)  
  - Popis za procjenu i provjeru  

- [**Sekcija 4: Hardverske platforme za implementaciju Edge AI-a**](./Module01/04.EdgeDeployment.md)  
  - Razmatranja i zahtjevi za implementaciju Edge AI-a  
  - Intel hardver za Edge AI i tehnike optimizacije  
  - Qualcomm AI rješenja za mobilne i ugrađene sustave  
  - NVIDIA Jetson i platforme za rubno računalstvo  
  - Windows AI PC platforme s NPU akceleracijom  
  - Strategije optimizacije specifične za hardver  

---

### [Modul 02: Osnove malih jezičnih modela](./Module02/README.md)  
**Tema**: Teorijski principi SLM-a, strategije implementacije i primjena u proizvodnji  

#### Struktura poglavlja:
- [**Sekcija 1: Osnove obitelji modela Microsoft Phi**](./Module02/01.PhiFamily.md)  
  - Evolucija filozofije dizajna (Phi-1 do Phi-4)  
  - Dizajn arhitekture s naglaskom na učinkovitost  
  - Specijalizirane sposobnosti (rezoniranje, multimodalnost, rubna primjena)  

- [**Sekcija 2: Osnove obitelji modela Qwen**](./Module02/02.QwenFamily.md)  
  - Izvrsnost otvorenog koda (Qwen 1.0 do Qwen3) – dostupno putem Hugging Face  
  - Napredna arhitektura rezoniranja s mogućnostima "thinking mode"  
  - Skalabilne opcije implementacije (0.5B-235B parametara)  

- [**Sekcija 3: Osnove obitelji modela Gemma**](./Module02/03.GemmaFamily.md)  
  - Inovacija vođena istraživanjem (Gemma 3 & 3n)  
  - Multimodalna izvrsnost  
  - Arhitektura prilagođena mobilnim uređajima  

- [**Sekcija 4: Osnove obitelji modela BitNET**](./Module02/04.BitNETFamily.md)  
  - Revolucionarna tehnologija kvantizacije (1.58-bit)  
  - Specijalizirani okvir za inference s https://github.com/microsoft/BitNet  
  - Održivo AI vodstvo kroz ekstremnu učinkovitost  

- [**Sekcija 5: Osnove modela Microsoft Mu**](./Module02/05.mumodel.md)  
  - Arhitektura prilagođena uređajima ugrađena u Windows 11  
  - Integracija sustava s postavkama Windows 11  
  - Offline operacija uz očuvanje privatnosti  

- [**Sekcija 6: Osnove Phi-Silica modela**](./Module02/06.phisilica.md)  
  - Arhitektura optimizirana za NPU ugrađena u Windows 11 Copilot+ PC-e  
  - Izvanredna učinkovitost (650 tokena/sekundi pri 1.5W)  
  - Integracija za programere s Windows App SDK-om  

---

### [Modul 03: Implementacija malih jezičnih modela](./Module03/README.md)  
**Tema**: Cjelokupni životni ciklus implementacije SLM-a, od teorije do proizvodnog okruženja  

#### Struktura poglavlja:
- [**Sekcija 1: Napredno učenje SLM-a**](./Module03/01.SLMAdvancedLearning.md)  
  - Okvir za klasifikaciju parametara (Mikro SLM 100M-1.4B, Srednji SLM 14B-30B)  
  - Napredne tehnike optimizacije (metode kvantizacije, BitNET 1-bit kvantizacija)  
  - Strategije nabave modela (Azure AI Foundry za Phi modele, Hugging Face za odabrane modele)  

- [**Sekcija 2: Implementacija u lokalnom okruženju**](./Module03/02.DeployingSLMinLocalEnv.md)  
  - Ollama univerzalna platforma za implementaciju  
  - Microsoft Foundry lokalna rješenja za poslovnu primjenu  
  - Komparativna analiza okvira  

- [**Sekcija 3: Implementacija u oblaku s kontejnerima**](./Module03/03.DeployingSLMinCloud.md)  
  - vLLM implementacija za inference visokih performansi  
  - Orkestracija kontejnera Ollama  
  - ONNX Runtime optimizirana implementacija za rub  

---

### [Modul 04: Konverzija formata modela i kvantizacija](./Module04/README.md)  
**Tema**: Kompletan alat za optimizaciju modela za rubnu primjenu na različitim platformama  

#### Struktura poglavlja:
- [**Sekcija 1: Osnove konverzije formata modela i kvantizacije**](./Module04/01.Introduce.md)  
  - Okvir za klasifikaciju preciznosti (ultra-niska, niska, srednja preciznost)  
  - Prednosti i primjene GGUF i ONNX formata  
  - Prednosti kvantizacije za operativnu učinkovitost  
  - Usporedbe performansi i memorijskog otiska  
- [**Odjeljak 2: Vodič za implementaciju Llama.cpp**](./Module04/02.Llamacpp.md)
  - Instalacija na više platformi (Windows, macOS, Linux)
  - Konverzija u GGUF format i razine kvantizacije (Q2_K do Q8_0)
  - Hardverska akceleracija (CUDA, Metal, OpenCL, Vulkan)
  - Integracija s Pythonom i implementacija REST API-ja

- [**Odjeljak 3: Microsoft Olive Optimization Suite**](./Module04/03.MicrosoftOlive.md)
  - Optimizacija modela prilagođena hardveru s više od 40 ugrađenih komponenti
  - Automatska optimizacija s dinamičkom i statičkom kvantizacijom
  - Integracija u poslovne procese putem Azure ML radnih tijekova
  - Podrška za popularne modele (Llama, Phi, odabrani Qwen modeli, Gemma)

- [**Odjeljak 4: OpenVINO Toolkit Optimization Suite**](./Module04/04.openvino.md)
  - Intelov otvoreni alat za implementaciju AI-a na više platformi
  - Okvir za kompresiju neuronskih mreža (NNCF) za naprednu optimizaciju
  - OpenVINO GenAI za implementaciju velikih jezičnih modela
  - Hardverska akceleracija na CPU, GPU, VPU i AI akceleratorima

- [**Odjeljak 5: Apple MLX Framework - Detaljna analiza**](./Module04/05.AppleMLX.md)
  - Arhitektura unificirane memorije za Apple Silicon
  - Podrška za LLaMA, Mistral, Phi-3, odabrane Qwen modele
  - LoRA fino podešavanje i prilagodba modela
  - Integracija s Hugging Face uz kvantizaciju od 4-bit/8-bit

- [**Odjeljak 6: Sinteza radnog tijeka za razvoj Edge AI-a**](./Module04/06.workflow-synthesis.md)
  - Unificirana arhitektura radnog tijeka koja integrira više okvira za optimizaciju
  - Stabla odluka za odabir okvira i analiza kompromisa u performansama
  - Validacija spremnosti za proizvodnju i strategije za implementaciju
  - Strategije za buduću prilagodbu novim hardverskim i modelskim arhitekturama

---

### [Modul 05: SLMOps - Operacije malih jezičnih modela](./Module05/README.md)
**Tema**: Cjelokupni životni ciklus SLM-a od destilacije do implementacije u proizvodnji

#### Struktura poglavlja:
- [**Odjeljak 1: Uvod u SLMOps**](./Module05/01.IntroduceSLMOps.md)
  - Paradigmatska promjena u AI operacijama kroz SLMOps
  - Učinkovitost troškova i arhitektura usmjerena na privatnost
  - Strateški poslovni utjecaj i konkurentske prednosti
  - Izazovi i rješenja u stvarnoj implementaciji

- [**Odjeljak 2: Destilacija modela - Od teorije do prakse**](./Module05/02.SLMOps-Distillation.md)
  - Prijenos znanja s učiteljskih na učeničke modele
  - Implementacija dvostupanjskog procesa destilacije
  - Azure ML radni tijekovi destilacije s praktičnim primjerima
  - Smanjenje vremena inferencije za 85% uz zadržavanje 92% točnosti

- [**Odjeljak 3: Fino podešavanje - Prilagodba modela za specifične zadatke**](./Module05/03.SLMOps-Finetuing.md)
  - Tehnike učinkovitog finog podešavanja parametara (PEFT)
  - Napredne metode LoRA i QLoRA
  - Implementacija finog podešavanja putem Microsoft Olive
  - Trening s više adaptera i optimizacija hiperparametara

- [**Odjeljak 4: Implementacija - Spremnost za proizvodnju**](./Module05/04.SLMOps.Deployment.md)
  - Konverzija i kvantizacija modela za proizvodnju
  - Konfiguracija za lokalnu implementaciju putem Foundry Local
  - Benchmarking performansi i validacija kvalitete
  - Smanjenje veličine za 75% uz praćenje u proizvodnji

---

### [Modul 06: SLM agentni sustavi - AI agenti i pozivanje funkcija](./Module06/README.md)
**Tema**: Implementacija SLM agentnih sustava od temelja do naprednog pozivanja funkcija i integracije Model Context Protocol-a

#### Struktura poglavlja:
- [**Odjeljak 1: AI agenti i temelji malih jezičnih modela**](./Module06/01.IntroduceAgent.md)
  - Okvir za klasifikaciju agenata (refleksni, temeljeni na modelu, temeljeni na cilju, učeni agenti)
  - Temelji SLM-a i strategije optimizacije (GGUF, kvantizacija, edge okviri)
  - Analiza kompromisa između SLM-a i LLM-a (10-30× smanjenje troškova, 70-80% učinkovitosti zadatka)
  - Praktična implementacija s Ollama, VLLM i Microsoft edge rješenjima

- [**Odjeljak 2: Pozivanje funkcija u malim jezičnim modelima**](./Module06/02.FunctionCalling.md)
  - Sustavna implementacija radnog tijeka (detekcija namjere, JSON izlaz, vanjsko izvršenje)
  - Implementacije specifične za platformu (Phi-4-mini, odabrani Qwen modeli, Microsoft Foundry Local)
  - Napredni primjeri (suradnja više agenata, dinamički odabir alata)
  - Razmatranja za proizvodnju (ograničavanje brzine, zapisivanje revizija, sigurnosne mjere)

- [**Odjeljak 3: Integracija Model Context Protocol-a (MCP)**](./Module06/03.IntroduceMCP.md)
  - Arhitektura protokola i dizajn slojevitog sustava
  - Podrška za više backend sustava (Ollama za razvoj, vLLM za proizvodnju)
  - Protokoli povezivanja (STDIO i SSE modovi)
  - Primjene u stvarnom svijetu (automatizacija weba, obrada podataka, integracija API-ja)

---

### [Modul 07: Primjeri implementacije EdgeAI-a](./Module07/README.md)
**Tema**: Sveobuhvatne implementacije EdgeAI-a na različitim platformama i okvirima

#### Struktura poglavlja:
- [**AI alat za Visual Studio Code**](./Module07/aitoolkit.md)
  - Sveobuhvatno razvojno okruženje za Edge AI unutar VS Code-a
  - Katalog modela i otkrivanje za implementaciju na rubu
  - Lokalno testiranje, optimizacija i radni tijekovi razvoja agenata
  - Praćenje performansi i evaluacija za rubne scenarije

- [**Vodič za razvoj EdgeAI-a na Windowsu**](./Module07/windowdeveloper.md)
  - Sveobuhvatan pregled Windows AI Foundry platforme
  - Phi Silica API za učinkovitu inferenciju na NPU-u
  - API-ji za računalni vid za obradu slika i OCR
  - Foundry Local CLI za lokalni razvoj i testiranje

- [**EdgeAI na NVIDIA Jetson Orin Nano**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 67 TOPS AI performansi u formatu veličine kreditne kartice
  - Podrška za generativne AI modele (transformeri za vid, LLM-ovi, modeli za vid-jezik)
  - Primjene u robotici, dronovima, inteligentnim kamerama, autonomnim uređajima
  - Pristupačna platforma od $249 za demokratizirani AI razvoj

- [**EdgeAI u mobilnim aplikacijama s .NET MAUI i ONNX Runtime GenAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - AI na mobilnim uređajima s jedinstvenom C# bazom koda
  - Podrška za hardversku akceleraciju (CPU, GPU, mobilni AI procesori)
  - Optimizacije specifične za platformu (CoreML za iOS, NNAPI za Android)
  - Kompletna implementacija generativnog AI ciklusa

- [**EdgeAI u Azureu s motorom malih jezičnih modela**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - Hibridna arhitektura implementacije između oblaka i ruba
  - Integracija Azure AI usluga s ONNX Runtime-om
  - Implementacija na razini poduzeća i kontinuirano upravljanje modelima
  - Hibridni AI radni tijekovi za inteligentnu obradu dokumenata

- [**EdgeAI s Windows ML-om**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Temelj Windows AI Foundry-a za učinkovitu inferenciju na uređaju
  - Univerzalna podrška za hardver (AMD, Intel, NVIDIA, Qualcomm čipovi)
  - Automatska apstrakcija i optimizacija hardvera
  - Unificirani okvir za raznoliki Windows hardverski ekosustav

- [**EdgeAI s lokalnim aplikacijama Foundry-a**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - Implementacija usmjerena na privatnost s lokalnim resursima
  - Integracija Phi-3 jezičnog modela sa semantičkom pretragom (samo Phi modeli)
  - Podrška za lokalne vektorske baze podataka (SQLite, Qdrant)
  - Suverenitet podataka i mogućnosti rada izvan mreže

## Ciljevi učenja tečaja

Završetkom ovog sveobuhvatnog tečaja EdgeAI-a, razvijat ćete stručnost u dizajnu, implementaciji i implementaciji proizvodno spremnih EdgeAI rješenja. Naš strukturirani pristup osigurava da savladate i teorijske temelje i praktične vještine implementacije.

### Tehničke kompetencije

**Temeljno znanje**
- Razumijevanje temeljnih razlika između AI arhitektura temeljenih na oblaku i rubu
- Ovladavanje principima kvantizacije modela, kompresije i optimizacije za okruženja s ograničenim resursima
- Razumijevanje opcija hardverske akceleracije (NPU, GPU, CPU) i njihovih implikacija na implementaciju

**Vještine implementacije**
- Implementacija malih jezičnih modela na raznim rubnim platformama (mobilne, ugrađene, IoT, rubni serveri)
- Primjena okvira za optimizaciju uključujući Llama.cpp, Microsoft Olive, ONNX Runtime i Apple MLX
- Implementacija sustava za inferenciju u stvarnom vremenu s zahtjevima za odziv ispod sekunde

**Ekspertiza u proizvodnji**
- Dizajn skalabilnih EdgeAI arhitektura za poslovne aplikacije
- Implementacija strategija za praćenje, održavanje i ažuriranje sustava
- Primjena najboljih sigurnosnih praksi za implementacije EdgeAI-a koje čuvaju privatnost

### Strateške sposobnosti

**Okvir za donošenje odluka**
- Procjena EdgeAI prilika i identifikacija prikladnih slučajeva upotrebe za poslovne aplikacije
- Procjena kompromisa između točnosti modela, brzine inferencije, potrošnje energije i troškova hardvera
- Odabir odgovarajućih obitelji SLM-a i konfiguracija na temelju specifičnih ograničenja implementacije

**Arhitektura sustava**
- Dizajn end-to-end EdgeAI rješenja koja se integriraju s postojećom infrastrukturom
- Planiranje hibridnih arhitektura oblaka i ruba za optimalne performanse i troškovnu učinkovitost
- Implementacija tijekova podataka i obrada za AI aplikacije u stvarnom vremenu

### Industrijske primjene

**Praktični scenariji implementacije**
- **Proizvodnja**: Sustavi za kontrolu kvalitete, prediktivno održavanje i optimizaciju procesa
- **Zdravstvo**: Dijagnostički alati koji čuvaju privatnost i sustavi za praćenje pacijenata
- **Transport**: Donošenje odluka za autonomna vozila i upravljanje prometom
- **Pametni gradovi**: Inteligentna infrastruktura i sustavi za upravljanje resursima
- **Potrošačka elektronika**: Mobilne aplikacije s AI-om i pametni kućni uređaji

## Pregled ishoda učenja

### Ishodi učenja Modula 01:
- Razumijevanje temeljnih razlika između AI arhitektura temeljenih na oblaku i rubu
- Ovladavanje osnovnim tehnikama optimizacije za implementaciju na rubu
- Prepoznavanje stvarnih primjena i uspješnih priča
- Stjecanje praktičnih vještina za implementaciju EdgeAI rješenja

### Ishodi učenja Modula 02:
- Duboko razumijevanje različitih filozofija dizajna SLM-a i njihovih implikacija na implementaciju
- Ovladavanje strateškim sposobnostima donošenja odluka na temelju računalnih ograničenja i zahtjeva za performansama
- Razumijevanje kompromisa u fleksibilnosti implementacije
- Posjedovanje uvida u budućnost učinkovitih AI arhitektura

### Ishodi učenja Modula 03:
- Strateške sposobnosti odabira modela
- Ovladavanje tehnikama optimizacije
- Ovladavanje fleksibilnošću implementacije
- Sposobnosti konfiguracije spremne za proizvodnju

### Ishodi učenja Modula 04:
- Duboko razumijevanje granica kvantizacije i praktičnih primjena
- Praktično iskustvo s više okvira za optimizaciju (Llama.cpp, Olive, OpenVINO, MLX)
- Ovladavanje Intelovom hardverskom optimizacijom putem OpenVINO-a i NNCF-a
- Sposobnosti odabira optimizacije prilagođene hardveru na raznim platformama
- Vještine implementacije za proizvodnju u okruženjima za računalstvo na rubu
- Strateški odabir okvira i sinteza radnog tijeka za optimalna Edge AI rješenja

### Ishodi učenja Modula 05:
- Ovladavanje paradigmom SLMOps-a i operativnim principima
- Implementacija destilacije modela za prijenos znanja i optimizaciju učinkovitosti
- Primjena tehnika finog podešavanja za prilagodbu modela specifičnim domenama
- Implementacija proizvodno spremnih SLM rješenja s strategijama za praćenje i održavanje

### Ishodi učenja Modula 06:
- Razumijevanje temeljnih koncepata AI agenata i arhitekture malih jezičnih modela
- Ovladavanje implementacijom pozivanja funkcija na više platformi i okvira
- Integracija Model Context Protocol-a (MCP) za standardiziranu interakciju s vanjskim alatima
- Izgradnja sofisticiranih agentnih sustava s minimalnim zahtjevima za ljudsku intervenciju

### Ishodi učenja Modula 07:
- Ovladavanje AI alatom za Visual Studio Code za sveobuhvatne radne tijekove razvoja Edge AI-a
- Stjecanje stručnosti u Windows AI Foundry platformi i strategijama optimizacije NPU-a
- Praktično iskustvo s raznim EdgeAI platformama i strategijama implementacije
- Ovladavanje tehnikama optimizacije specifičnim za hardver na NVIDIA, mobilnim, Azure i Windows platformama
- Razumijevanje kompromisa u implementaciji između performansi, troškova i zahtjeva za privatnost
- Razvoj praktičnih vještina za izgradnju stvarnih EdgeAI aplikacija u različitim ekosustavima

## Očekivani ishodi tečaja

Nakon uspješnog završetka ovog tečaja, bit ćete opremljeni znanjem, vještinama i samopouzdanjem za vođenje EdgeAI inicijativa u profesionalnim okruženjima.

### Spremnost za profesionalni rad

**Tehničko vodstvo**
- **Arhitektura rješenja**: Dizajn sveobuhvatnih EdgeAI sustava koji zadovoljavaju poslovne zahtjeve
- **Optimizacija performansi**: Postizanje optimalne ravnoteže između točnosti, brzine i potrošnje resursa
- **Implementacija na više platformi**: Implementacija rješenja na Windows, Linux, mobilnim i ugrađenim platformama
- **Operacije u proizvodnji**: Održavanje i skaliranje EdgeAI sustava s pouzdanošću na razini poduzeća

**Industrijska stručnost**
- **Procjena tehnologije**: Procjena i preporuka EdgeAI rješenja za specifične poslovne izazove
- **Planiranje implementacije**: Razvoj realističnih vremenskih okvira i zahtjeva za resursima za EdgeAI projekte
- **Upravljanje rizicima**: Identifikacija i ublažavanje tehničkih i operativnih rizika u EdgeAI implementacijama
- **Optimizacija ROI-a**: Demonstracija mjerljive poslovne vrijednosti od EdgeAI implementacija

### Mogućnosti za napredovanje u kar
Ovaj tečaj postavlja vas na čelo primjene AI tehnologije, gdje se inteligentne sposobnosti besprijekorno integriraju u uređaje i sustave koji pokreću suvremeni život.

## Dijagram strukture datoteka

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

## Značajke tečaja

- **Progresivno učenje**: Postupno napredovanje od osnovnih pojmova do napredne primjene
- **Integracija teorije i prakse**: Svaki modul sadrži teorijske temelje i praktične operacije
- **Stvarne studije slučaja**: Temeljene na stvarnim slučajevima iz Microsofta, Alibabe, Googlea i drugih
- **Praktična vježba**: Kompletne konfiguracijske datoteke, postupci testiranja API-ja i skripte za primjenu
- **Referentne performanse**: Detaljne usporedbe brzine zaključivanja, korištenja memorije i zahtjeva za resursima
- **Razmatranja na razini poduzeća**: Prakse sigurnosti, okviri usklađenosti i strategije zaštite podataka

## Početak

Preporučeni put učenja:
1. Započnite s **Module01** kako biste izgradili temeljno razumijevanje EdgeAI-a
2. Nastavite s **Module02** za dubinsko razumijevanje različitih obitelji SLM modela
3. Naučite **Module03** kako biste savladali praktične vještine primjene
4. Nastavite s **Module04** za naprednu optimizaciju modela, konverziju formata i sintezu okvira
5. Završite **Module05** kako biste savladali SLMOps za implementacije spremne za proizvodnju
6. Istražite **Module06** kako biste razumjeli SLM agentne sustave i mogućnosti pozivanja funkcija
7. Završite s **Module07** kako biste stekli praktično iskustvo s AI Toolkitom i raznovrsnim primjerima primjene EdgeAI-a

Svaki modul je dizajniran da bude samostalno cjelovit, ali sekvencijalno učenje pružit će najbolje rezultate.

## Vodič za učenje

Sveobuhvatan [Vodič za učenje](STUDY_GUIDE.md) dostupan je kako bi vam pomogao da maksimalno iskoristite svoje iskustvo učenja. Vodič za učenje pruža:

- **Strukturirane putove učenja**: Optimizirani rasporedi za završetak tečaja u 20 sati
- **Smjernice za raspodjelu vremena**: Specifične preporuke za balansiranje čitanja, vježbi i projekata
- **Fokus na ključne pojmove**: Prioritetni ciljevi učenja za svaki modul
- **Alati za samoprocjenu**: Pitanja i vježbe za testiranje vašeg razumijevanja
- **Ideje za mini-projekte**: Praktične primjene za učvršćivanje vašeg znanja

Vodič za učenje prilagođen je intenzivnom učenju (1 tjedan) i učenju u slobodno vrijeme (3 tjedna), s jasnim smjernicama o tome kako učinkovito raspodijeliti vrijeme čak i ako možete posvetiti samo 10 sati tečaju.

---

**Budućnost EdgeAI-a leži u kontinuiranom poboljšanju arhitektura modela, tehnika kvantizacije i strategija primjene koje daju prednost učinkovitosti i specijalizaciji nad općim sposobnostima. Organizacije koje prihvate ovu promjenu paradigme bit će u dobroj poziciji da iskoriste transformativni potencijal AI-a, dok istovremeno zadržavaju kontrolu nad svojim podacima i operacijama.**

## Ostali tečajevi

Naš tim proizvodi i druge tečajeve! Pogledajte:

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

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.