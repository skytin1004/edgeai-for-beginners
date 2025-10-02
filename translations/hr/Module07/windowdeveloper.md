<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T14:46:18+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "hr"
}
-->
# Vodič za razvoj Windows Edge AI

## Uvod

Dobrodošli u razvoj Windows Edge AI - vaš sveobuhvatan vodič za izradu inteligentnih aplikacija koje koriste snagu AI-a na uređaju putem Microsoftove platforme Windows AI Foundry. Ovaj vodič je posebno osmišljen za Windows programere koji žele integrirati najnovije mogućnosti Edge AI-a u svoje aplikacije, koristeći puni potencijal hardverske akceleracije na Windows uređajima.

### Prednosti Windows AI-a

Windows AI Foundry predstavlja jedinstvenu, pouzdanu i sigurnu platformu koja podržava cijeli životni ciklus razvoja AI-a - od odabira i prilagodbe modela do optimizacije i implementacije na CPU, GPU, NPU i hibridne cloud arhitekture. Ova platforma demokratizira razvoj AI-a pružajući:

- **Hardversku apstrakciju**: Jednostavna implementacija na AMD, Intel, NVIDIA i Qualcomm čipovima
- **Inteligenciju na uređaju**: AI koji čuva privatnost i radi isključivo na lokalnom hardveru
- **Optimizirane performanse**: Modeli unaprijed optimizirani za Windows hardverske konfiguracije
- **Spremnost za poduzeća**: Sigurnosne značajke i usklađenost na razini proizvodnje

### Zašto odabrati Windows za Edge AI?

**Univerzalna podrška za hardver**  
Windows ML automatski optimizira hardver u cijelom Windows ekosustavu, osiguravajući da vaše AI aplikacije rade optimalno bez obzira na arhitekturu čipova.

**Integrirani AI Runtime**  
Ugrađeni Windows ML inference engine eliminira složene zahtjeve za postavljanje, omogućujući programerima da se usredotoče na logiku aplikacije umjesto na infrastrukturne probleme.

**Optimizacija za Copilot+ PC**  
API-ji dizajnirani za sljedeću generaciju Windows uređaja s posvećenim Neural Processing Units (NPU) pružaju izvanredne performanse po potrošenom vatu.

**Razvojni ekosustav**  
Bogati alati uključujući integraciju s Visual Studiom, opsežnu dokumentaciju i uzorke aplikacija koji ubrzavaju razvojne cikluse.

## Ciljevi učenja

Završetkom ovog vodiča za razvoj Windows Edge AI-a, savladat ćete ključne vještine potrebne za izradu AI aplikacija spremnih za proizvodnju na Windows platformi.

### Osnovne tehničke kompetencije

**Majstorstvo Windows AI Foundry-a**  
- Razumijevanje arhitekture i komponenti platforme Windows AI Foundry  
- Navigacija kroz cijeli životni ciklus razvoja AI-a unutar Windows ekosustava  
- Implementacija sigurnosnih najboljih praksi za AI aplikacije na uređaju  
- Optimizacija aplikacija za različite Windows hardverske konfiguracije  

**Ekspertiza u integraciji API-ja**  
- Savladavanje Windows AI API-ja za tekst, viziju i multimodalne aplikacije  
- Implementacija Phi Silica jezičnog modela za generiranje teksta i zaključivanje  
- Primjena računalne vizije koristeći ugrađene API-je za obradu slika  
- Prilagodba unaprijed treniranih modela pomoću LoRA (Low-Rank Adaptation) tehnika  

**Lokalna implementacija Foundry-a**  
- Pregled, evaluacija i implementacija otvorenih jezičnih modela pomoću Foundry Local CLI  
- Razumijevanje optimizacije i kvantizacije modela za lokalnu implementaciju  
- Implementacija offline AI mogućnosti koje funkcioniraju bez internetske povezanosti  
- Upravljanje životnim ciklusima modela i ažuriranjima u proizvodnim okruženjima  

**Implementacija Windows ML-a**  
- Integracija prilagođenih ONNX modela u Windows aplikacije koristeći Windows ML  
- Iskorištavanje automatske hardverske akceleracije na CPU, GPU i NPU arhitekturama  
- Implementacija real-time inferencije uz optimalno korištenje resursa  
- Dizajn skalabilnih AI aplikacija za različite kategorije Windows uređaja  

### Vještine razvoja aplikacija

**Razvoj za više platformi na Windowsu**  
- Izrada AI aplikacija koristeći .NET MAUI za univerzalnu implementaciju na Windowsu  
- Integracija AI mogućnosti u Win32, UWP i progresivne web aplikacije  
- Implementacija responzivnih UI dizajna koji se prilagođavaju AI procesima  
- Upravljanje asinkronim AI operacijama uz pravilne obrasce korisničkog iskustva  

**Optimizacija performansi**  
- Profiliranje i optimizacija performansi AI inferencije na različitim hardverskim konfiguracijama  
- Implementacija učinkovitog upravljanja memorijom za velike jezične modele  
- Dizajn aplikacija koje se prilagođavaju dostupnim hardverskim mogućnostima  
- Primjena strategija predmemoriranja za često korištene AI operacije  

**Spremnost za proizvodnju**  
- Implementacija sveobuhvatnog rukovanja greškama i mehanizama za povratne opcije  
- Dizajn telemetrije i praćenja performansi AI aplikacija  
- Primjena sigurnosnih najboljih praksi za lokalno pohranjivanje i izvršavanje AI modela  
- Planiranje strategija implementacije za poduzeća i potrošačke aplikacije  

### Poslovno i strateško razumijevanje

**Arhitektura AI aplikacija**  
- Dizajn hibridnih arhitektura koje optimiziraju između lokalne i cloud AI obrade  
- Procjena kompromisa između veličine modela, točnosti i brzine inferencije  
- Planiranje arhitektura protoka podataka koje čuvaju privatnost uz omogućavanje inteligencije  
- Implementacija isplativih AI rješenja koja se skaliraju prema zahtjevima korisnika  

**Pozicioniranje na tržištu**  
- Razumijevanje konkurentskih prednosti Windows-native AI aplikacija  
- Identifikacija slučajeva upotrebe gdje AI na uređaju pruža superiorno korisničko iskustvo  
- Razvoj strategija za plasiranje AI-poboljšanih Windows aplikacija na tržište  
- Pozicioniranje aplikacija za iskorištavanje prednosti Windows ekosustava  

## Uzorci AI aplikacija za Windows App SDK

Windows App SDK pruža opsežne uzorke koji demonstriraju integraciju AI-a kroz različite okvire i scenarije implementacije. Ovi uzorci su ključni za razumijevanje obrazaca razvoja Windows AI-a.

### Uzorci Windows AI Foundry-a

| Uzorak | Okvir | Područje fokusa | Ključne značajke |
|--------|-------|-----------------|------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integracija Windows AI API-ja | Kompletna WinUI aplikacija koja demonstrira Windows AI API-je, optimizaciju za ARM64, paketnu implementaciju |

**Ključne tehnologije:**  
- Windows AI API-je  
- WinUI 3 okvir  
- Optimizacija za ARM64 platformu  
- Kompatibilnost s Copilot+ PC-jem  
- Paketna implementacija aplikacije  

**Preduvjeti:**  
- Windows 11 s preporučenim Copilot+ PC-jem  
- Visual Studio 2022  
- Konfiguracija za ARM64 build  
- Windows App SDK 1.8.1+  

### Uzorci Windows ML-a

#### C++ Uzorci

| Uzorak | Tip | Područje fokusa | Ključne značajke |
|--------|-----|-----------------|------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Osnovni Windows ML | Otkrivanje EP-a, opcije naredbenog retka, kompilacija modela |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Implementacija okvira | Dijeljeni runtime, manji otisak implementacije |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Samostalna implementacija | Samostalna implementacija, bez runtime ovisnosti |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Korištenje biblioteke | WindowsML u dijeljenoj biblioteci, upravljanje memorijom |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet vodič | Konverzija modela, kompilacija EP-a, Build 2025 vodič |

#### C# Uzorci

**Konzolne aplikacije**

| Uzorak | Tip | Područje fokusa | Ključne značajke |
|--------|-----|-----------------|------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolna aplikacija | Osnovna C# integracija | Korištenje zajedničkih pomoćnih alata, sučelje naredbenog retka |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet vodič | Konverzija modela, kompilacija EP-a, Build 2025 vodič |

**GUI aplikacije**

| Uzorak | Okvir | Područje fokusa | Ključne značajke |
|--------|-------|-----------------|------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Klasifikacija slika s WPF sučeljem |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradicionalni GUI | Klasifikacija slika s Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderni GUI | Klasifikacija slika s WinUI 3 sučeljem |

#### Python Uzorci

| Uzorak | Jezik | Područje fokusa | Ključne značajke |
|--------|-------|-----------------|------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasifikacija slika | WinML Python binding, obrada slika u batchu |

### Preduvjeti za uzorke

**Sistemski zahtjevi:**  
- Windows 11 PC s verzijom 24H2 (build 26100) ili novijom  
- Visual Studio 2022 s C++ i .NET radnim opterećenjima  
- Windows App SDK 1.8.1 ili noviji  
- Python 3.10-3.13 za Python uzorke na x64 i ARM64 uređajima  

**Specifično za Windows AI Foundry:**  
- Preporučen Copilot+ PC za optimalne performanse  
- Konfiguracija za ARM64 build za Windows AI uzorke  
- Potrebna identifikacija paketa (nepodržane aplikacije bez paketa)  

### Uobičajeni tijek rada uzoraka

Većina Windows ML uzoraka slijedi ovaj standardni obrazac:

1. **Inicijalizacija okruženja** - Kreiranje ONNX Runtime okruženja  
2. **Registracija izvršnih pružatelja usluga** - Otkrivanje i registracija dostupnih hardverskih akceleratora (CPU, GPU, NPU)  
3. **Učitavanje modela** - Učitavanje ONNX modela, opcionalno kompajliranje za ciljani hardver  
4. **Predobrada ulaza** - Pretvaranje slika/podataka u format ulaza modela  
5. **Izvršavanje inferencije** - Pokretanje modela i dobivanje predikcija  
6. **Obrada rezultata** - Primjena softmaxa i prikaz najboljih predikcija  

### Korišteni modeli

| Model | Namjena | Uključen | Napomene |
|-------|---------|----------|----------|
| SqueezeNet | Laka klasifikacija slika | ✅ Uključen | Unaprijed treniran, spreman za korištenje |
| ResNet-50 | Klasifikacija slika visoke točnosti | ❌ Potrebna konverzija | Koristite [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) za konverziju |

### Podrška za hardver

Svi uzorci automatski otkrivaju i koriste dostupni hardver:  
- **CPU** - Univerzalna podrška na svim Windows uređajima  
- **GPU** - Automatsko otkrivanje i optimizacija za dostupni grafički hardver  
- **NPU** - Iskorištavanje Neural Processing Units na podržanim uređajima (Copilot+ PC-ji)  

## Komponente platforme Windows AI Foundry

### 1. Windows AI API-je

Windows AI API-je pružaju gotove AI mogućnosti koje pokreću modeli na uređaju, optimizirani za učinkovitost i performanse na Copilot+ PC uređajima uz minimalne zahtjeve za postavljanje.

#### Osnovne kategorije API-ja

**Phi Silica jezični model**  
- Mali, ali moćan jezični model za generiranje teksta i zaključivanje  
- Optimiziran za real-time inferenciju uz minimalnu potrošnju energije  
- Podrška za prilagodbu pomoću LoRA tehnika  
- Integracija s Windows semantičkom pretragom i dohvatom znanja  

**API-je za računalnu viziju**  
- **Prepoznavanje teksta (OCR)**: Ekstrakcija teksta iz slika s visokom točnošću  
- **Super rezolucija slike**: Povećanje kvalitete slika pomoću lokalnih AI modela  
- **Segmentacija slike**: Identifikacija i izolacija specifičnih objekata na slikama  
- **Opis slike**: Generiranje detaljnih tekstualnih opisa za vizualni sadržaj  
- **Brisanje objekata**: Uklanjanje neželjenih objekata sa slika pomoću AI-a  

**Multimodalne mogućnosti**  
- **Integracija vizije i jezika**: Kombinacija razumijevanja teksta i slika  
- **Semantička pretraga**: Omogućavanje prirodnih jezičnih upita za multimedijski sadržaj  
- **Dohvat znanja**: Izgradnja inteligentnih iskustava pretrage s lokalnim podacima  

### 2. Foundry Local

Foundry Local omogućuje programerima brz pristup gotovim otvorenim jezičnim modelima na Windows Siliconu, nudeći mogućnost pregleda, testiranja, interakcije i implementacije modela u lokalnim aplikacijama.

#### Uzorci aplikacija Foundry Local-a

[Foundry Local repozitorij](https://github.com/microsoft/Foundry-Local/tree/main/samples) pruža opsežne uzorke kroz različite programske jezike i okvire, demonstrirajući različite obrasce integracije i slučajeve upotrebe.

| Uzorak | Jezik/Okvir | Područje fokusa | Ključne značajke |
|--------|-------------|-----------------|------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementacija RAG-a | Integracija Semantic Kernel-a, Qdrant vektorske pohrane, JINA embeddings, unos dokumenata, streaming chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktop chat aplikacija | Cross-platform chat, lokalno/cloud prebacivanje modela, integracija OpenAI SDK-a, real-time streaming |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Osnovna integracija | Jednostavno korištenje SDK-a, inicijalizacija modela, osnovna funkcionalnost chata |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Osnovna integracija | Korištenje Python SDK-a, streaming odgovora, OpenAI-kompatibilni API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integracija sustava | Niskorazinsko korištenje SDK-a, asinkrone operacije, reqwest HTTP klijent |

#### Kategorije uzoraka prema slučaju upotrebe

**RAG (Retrieval-Augmented Generation)**  
- **dotNET/rag**: Kompletna implementacija RAG-a koristeći Semantic Kernel, Qdrant vektorsku bazu podataka i JINA embeddings  
- **Arhitektura**: Unos dokumenata → Razbijanje teksta → Vektorski embeddings → Pretraga sličnosti → Odgovori svjesni konteksta  
- **Tehnologije**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, streaming chat completion  

**Desktop aplikacije**  
- **electron/foundry-chat**: Chat aplikacija spremna za proizvodnju s lokalnim/cloud prebacivan
- **Značajke**: Odabir modela, streaming odgovora, rukovanje pogreškama, višestruka platforma za implementaciju  
- **Arhitektura**: Glavni proces Electron, IPC komunikacija, sigurni preload skripti  

**Primjeri integracije SDK-a**  
- **JavaScript (Node.js)**: Osnovna interakcija s modelom i streaming odgovori  
- **Python**: Korištenje OpenAI-kompatibilnog API-ja s asinhronim streamingom  
- **Rust**: Niskorazinska integracija s reqwest i tokio za asinhrone operacije  

#### Preduvjeti za lokalne uzorke Foundry  

**Sistemski zahtjevi:**  
- Windows 11 s instaliranim Foundry Local  
- Node.js v16+ za JavaScript/Electron uzorke  
- .NET 8.0+ za C# uzorke  
- Python 3.10+ za Python uzorke  
- Rust 1.70+ za Rust uzorke  

**Instalacija:**  
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```
  

#### Postavljanje specifično za uzorke  

**dotNET RAG uzorak:**  
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```
  
**Electron Chat uzorak:**  
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```
  
**JavaScript/Python/Rust uzorci:**  
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```
  

#### Ključne značajke  

**Katalog modela**  
- Sveobuhvatan skup unaprijed optimiziranih open-source modela  
- Optimizacija modela za CPU, GPU i NPU za trenutnu implementaciju  
- Podrška za popularne obitelji modela, uključujući Llama, Mistral, Phi i specijalizirane modele za određene domene  

**CLI integracija**  
- Sučelje naredbenog retka za upravljanje modelima i implementaciju  
- Automatizirani tijekovi rada za optimizaciju i kvantizaciju  
- Integracija s popularnim razvojnim okruženjima i CI/CD pipeline-ima  

**Lokalna implementacija**  
- Potpuno offline rad bez ovisnosti o oblaku  
- Podrška za prilagođene formate i konfiguracije modela  
- Učinkovito posluživanje modela s automatskom optimizacijom hardvera  

### 3. Windows ML  

Windows ML služi kao osnovna AI platforma i integrirani runtime za inferenciju na Windowsu, omogućujući programerima učinkovitu implementaciju prilagođenih modela na širokom Windows hardverskom ekosustavu.  

#### Prednosti arhitekture  

**Univerzalna podrška za hardver**  
- Automatska optimizacija za AMD, Intel, NVIDIA i Qualcomm čipove  
- Podrška za CPU, GPU i NPU izvršavanje s transparentnim prebacivanjem  
- Apstrakcija hardvera koja eliminira potrebu za optimizacijom specifičnom za platformu  

**Fleksibilnost modela**  
- Podrška za ONNX format modela s automatskom konverzijom iz popularnih okvira  
- Implementacija prilagođenih modela s performansama spremnim za produkciju  
- Integracija s postojećim arhitekturama Windows aplikacija  

**Integracija za poduzeća**  
- Kompatibilnost s Windows sigurnosnim i usklađenim okvirima  
- Podrška za alate za implementaciju i upravljanje u poduzećima  
- Integracija s alatima za upravljanje i praćenje Windows uređaja  

## Tijek razvoja  

### Faza 1: Postavljanje okruženja i konfiguracija alata  

**Priprema razvojnog okruženja**  
1. Instalirajte Visual Studio 2022 s C++ i .NET radnim opterećenjima  
2. Instalirajte Windows App SDK 1.8.1 ili noviji  
3. Konfigurirajte Windows AI Foundry CLI alate  
4. Postavite AI Toolkit ekstenziju za Visual Studio Code  
5. Uspostavite alate za profiliranje performansi i praćenje  
6. Osigurajte ARM64 konfiguraciju za optimizaciju Copilot+ PC-a  

**Postavljanje repozitorija uzoraka**  
1. Klonirajte [Windows App SDK Samples repozitorij](https://github.com/microsoft/WindowsAppSDK-Samples)  
2. Navigirajte do `Samples/WindowsAIFoundry/cs-winui` za primjere Windows AI API-ja  
3. Navigirajte do `Samples/WindowsML` za sveobuhvatne primjere Windows ML-a  
4. Pregledajte [zahtjeve za izgradnju](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) za ciljne platforme  

**Istraživanje AI Dev galerije**  
- Istražite uzorke aplikacija i referentne implementacije  
- Testirajte Windows AI API-je s interaktivnim demonstracijama  
- Pregledajte izvorni kod za najbolje prakse i obrasce  
- Identificirajte relevantne uzorke za vaš specifični slučaj upotrebe  

### Faza 2: Odabir i integracija modela  

**Analiza zahtjeva**  
- Definirajte funkcionalne zahtjeve za AI mogućnosti  
- Uspostavite ograničenja performansi i ciljeve optimizacije  
- Procijenite zahtjeve za privatnost i sigurnost  
- Planirajte arhitekturu implementacije i strategije skaliranja  

**Evaluacija modela**  
- Koristite Foundry Local za testiranje open-source modela za vaš slučaj upotrebe  
- Benchmarkirajte Windows AI API-je prema zahtjevima prilagođenih modela  
- Procijenite kompromise između veličine modela, točnosti i brzine inferencije  
- Prototipirajte pristupe integraciji s odabranim modelima  

### Faza 3: Razvoj aplikacije  

**Osnovna integracija**  
- Implementirajte integraciju Windows AI API-ja s pravilnim rukovanjem pogreškama  
- Dizajnirajte korisnička sučelja koja podržavaju AI tijekove obrade  
- Implementirajte strategije predmemoriranja i optimizacije za inferenciju modela  
- Dodajte telemetriju i praćenje performansi AI operacija  

**Testiranje i validacija**  
- Testirajte aplikacije na različitim Windows hardverskim konfiguracijama  
- Validirajte metrike performansi pod različitim uvjetima opterećenja  
- Implementirajte automatizirano testiranje za pouzdanost AI funkcionalnosti  
- Provedite testiranje korisničkog iskustva s AI-poboljšanim značajkama  

### Faza 4: Optimizacija i implementacija  

**Optimizacija performansi**  
- Profilirajte performanse aplikacije na ciljnim hardverskim konfiguracijama  
- Optimizirajte korištenje memorije i strategije učitavanja modela  
- Implementirajte adaptivno ponašanje na temelju dostupnih hardverskih mogućnosti  
- Fino podesite korisničko iskustvo za različite scenarije performansi  

**Implementacija u produkciji**  
- Pakirajte aplikacije s odgovarajućim AI modelima i ovisnostima  
- Implementirajte mehanizme ažuriranja za modele i logiku aplikacije  
- Konfigurirajte praćenje i analitiku za produkcijska okruženja  
- Planirajte strategije uvođenja za poduzeća i potrošače  

## Primjeri praktične implementacije  

### Primjer 1: Inteligentna aplikacija za obradu dokumenata  

Izradite Windows aplikaciju koja obrađuje dokumente koristeći više AI mogućnosti:  

**Korištene tehnologije:**  
- Phi Silica za sažimanje dokumenata i odgovaranje na pitanja  
- OCR API-ji za ekstrakciju teksta iz skeniranih dokumenata  
- API-ji za opis slika za analizu grafikona i dijagrama  
- Prilagođeni ONNX modeli za klasifikaciju dokumenata  

**Pristup implementaciji:**  
- Dizajnirajte modularnu arhitekturu s priključivim AI komponentama  
- Implementirajte asinhronu obradu za velike serije dokumenata  
- Dodajte indikatore napretka i podršku za otkazivanje dugotrajnih operacija  
- Uključite offline mogućnosti za obradu osjetljivih dokumenata  

### Primjer 2: Sustav za upravljanje inventarom u maloprodaji  

Izradite AI-pokretan sustav inventara za maloprodajne aplikacije:  

**Korištene tehnologije:**  
- Segmentacija slika za identifikaciju proizvoda  
- Prilagođeni vizualni modeli za klasifikaciju brendova i kategorija  
- Foundry Local implementacija specijaliziranih jezičnih modela za maloprodaju  
- Integracija s postojećim POS i inventarnim sustavima  

**Pristup implementaciji:**  
- Izgradite integraciju kamera za skeniranje proizvoda u stvarnom vremenu  
- Implementirajte prepoznavanje bar kodova i vizualnih proizvoda  
- Dodajte prirodne jezične upite inventara koristeći lokalne jezične modele  
- Dizajnirajte skalabilnu arhitekturu za implementaciju u više trgovina  

### Primjer 3: Asistent za dokumentaciju u zdravstvu  

Razvijte alat za dokumentaciju u zdravstvu koji čuva privatnost:  

**Korištene tehnologije:**  
- Phi Silica za generiranje medicinskih bilješki i podršku kliničkim odlukama  
- OCR za digitalizaciju rukom pisanih medicinskih zapisa  
- Prilagođeni medicinski jezični modeli implementirani putem Windows ML-a  
- Lokalno pohranjivanje vektora za dohvaćanje medicinskog znanja  

**Pristup implementaciji:**  
- Osigurajte potpuno offline rad za privatnost pacijenata  
- Implementirajte validaciju i sugestije medicinske terminologije  
- Dodajte zapisivanje revizije za usklađenost s regulativama  
- Dizajnirajte integraciju s postojećim sustavima elektroničkih medicinskih zapisa  

## Strategije optimizacije performansi  

### Razvoj svjestan hardvera  

**Optimizacija za NPU**  
- Dizajnirajte aplikacije koje koriste NPU mogućnosti na Copilot+ PC-ima  
- Implementirajte elegantan povratak na GPU/CPU na uređajima bez NPU-a  
- Optimizirajte formate modela za ubrzanje specifično za NPU  
- Pratite korištenje NPU-a i termalne karakteristike  

**Upravljanje memorijom**  
- Implementirajte učinkovite strategije učitavanja i predmemoriranja modela  
- Koristite mapiranje memorije za velike modele kako biste smanjili vrijeme pokretanja  
- Dizajnirajte aplikacije svjesne memorije za uređaje s ograničenim resursima  
- Implementirajte kvantizaciju modela za optimizaciju memorije  

**Učinkovitost baterije**  
- Optimizirajte AI operacije za minimalnu potrošnju energije  
- Implementirajte adaptivnu obradu na temelju statusa baterije  
- Dizajnirajte učinkovitu obradu u pozadini za kontinuirane AI operacije  
- Koristite alate za profiliranje energije za optimizaciju potrošnje  

### Razmatranja skalabilnosti  

**Višestruko niti**  
- Dizajnirajte AI operacije sigurne za niti za istovremenu obradu  
- Implementirajte učinkovitu distribuciju rada na dostupnim jezgrama  
- Koristite asinhrone obrasce za neblokirajuće AI operacije  
- Planirajte optimizaciju bazena niti za različite hardverske konfiguracije  

**Strategije predmemoriranja**  
- Implementirajte inteligentno predmemoriranje za često korištene AI operacije  
- Dizajnirajte strategije poništavanja predmemorije za ažuriranja modela  
- Koristite trajno predmemoriranje za skupe operacije predobrade  
- Implementirajte distribuirano predmemoriranje za scenarije s više korisnika  

## Najbolje prakse za sigurnost i privatnost  

### Zaštita podataka  

**Lokalna obrada**  
- Osigurajte da osjetljivi podaci nikada ne napuštaju lokalni uređaj  
- Implementirajte sigurno pohranjivanje za AI modele i privremene podatke  
- Koristite sigurnosne značajke Windowsa za sandboxing aplikacija  
- Primijenite enkripciju za pohranjene modele i rezultate međuprocesiranja  

**Sigurnost modela**  
- Validirajte integritet modela prije učitavanja i izvršavanja  
- Implementirajte sigurne mehanizme ažuriranja modela  
- Koristite potpisane modele kako biste spriječili neovlaštene izmjene  
- Primijenite kontrole pristupa za datoteke modela i konfiguraciju  

### Razmatranja usklađenosti  

**Usklađenost s regulativama**  
- Dizajnirajte aplikacije koje zadovoljavaju GDPR, HIPAA i druge regulativne zahtjeve  
- Implementirajte zapisivanje revizije za procese donošenja odluka AI-ja  
- Pružite značajke transparentnosti za rezultate generirane AI-jem  
- Omogućite korisnicima kontrolu nad obradom podataka AI-ja  

**Sigurnost u poduzeću**  
- Integrirajte s sigurnosnim politikama poduzeća na Windowsu  
- Podržite upravljanu implementaciju putem alata za upravljanje poduzećem  
- Implementirajte kontrole pristupa temeljene na ulogama za AI značajke  
- Pružite administrativne kontrole za funkcionalnost AI-ja  

## Rješavanje problema i ispravljanje pogrešaka  

### Uobičajeni izazovi u razvoju  

**Problemi s konfiguracijom izgradnje**  
- Osigurajte konfiguraciju platforme ARM64 za uzorke Windows AI API-ja  
- Provjerite kompatibilnost verzije Windows App SDK-a (potrebna verzija 1.8.1+)  
- Provjerite je li identitet paketa pravilno konfiguriran (potrebno za Windows AI API-je)  
- Validirajte podršku alata za izgradnju za ciljne verzije okvira  

**Problemi s učitavanjem modela**  
- Validirajte kompatibilnost ONNX modela s Windows ML-om  
- Provjerite integritet datoteke modela i zahtjeve formata  
- Provjerite zahtjeve hardverskih mogućnosti za specifične modele  
- Ispravite probleme s dodjelom memorije tijekom učitavanja modela  
- Osigurajte registraciju pružatelja usluga izvršavanja za hardversko ubrzanje  

**Razmatranja načina implementacije**  
- **Samostalni način rada**: Potpuno podržan s većom veličinom implementacije  
- **Način rada ovisan o okviru**: Manji otisak, ali zahtijeva zajednički runtime  
- **Aplikacije bez paketa**: Više nisu podržane za Windows AI API-je  
- Koristite `dotnet run -p:Platform=ARM64 -p:SelfContained=true` za samostalnu ARM64 implementaciju  

**Problemi s performansama**  
- Profilirajte performanse aplikacije na različitim hardverskim konfiguracijama  
- Identificirajte uska grla u AI procesnim cjevovodima  
- Optimizirajte operacije predobrade i postobrade podataka  
- Implementirajte praćenje performansi i upozorenja  

**Poteškoće s integracijom**  
- Ispravite probleme s integracijom API-ja uz pravilno rukovanje pogreškama  
- Validirajte formate ulaznih podataka i zahtjeve predobrade  
- Temeljito testirajte rubne slučajeve i uvjete pogreške  
- Implementirajte sveobuhvatno zapisivanje za ispravljanje problema u produkciji  

### Alati i tehnike za ispravljanje pogrešaka  

**Integracija s Visual Studiom**  
- Koristite AI Toolkit debugger za analizu izvršavanja modela  
- Implementirajte profiliranje performansi za AI operacije  
- Ispravite asinhrone AI operacije uz pravilno rukovanje iznimkama  
- Koristite alate za profiliranje memorije za optimizaciju  

**Alati Windows AI Foundry**  
- Iskoristite Foundry Local CLI za testiranje i validaciju modela  
- Koristite alate za testiranje Windows AI API-ja za provjeru integracije  
- Implementirajte prilagođeno zapisivanje za praćenje AI operacija  
- Kreirajte automatizirano testiranje za pouzdanost AI funkcionalnosti  

## Budućnost vaših aplikacija  

### Tehnologije u nastajanju  

**Hardver nove generacije**  
- Dizajnirajte aplikacije koje koriste buduće NPU mogućnosti  
- Planirajte za povećane veličine i složenost modela  
- Implementirajte adaptivne arhitekture za evoluciju hardvera  
- Razmotrite algoritme spremne za kvantnu tehnologiju za buduću kompatibilnost  

**Napredne AI mogućnosti**  
- Pripremite se za multimodalnu AI integraciju preko više vrsta podataka  
- Planirajte za real-time suradnički AI između više uređaja  
- Dizajnirajte za mogućnosti federativnog učenja  
- Razmotrite hibridne arhitekture inteligencije na rubu i oblaku  

### Kontinuirano učenje i prilagodba  

**Ažuriranja modela**  
- Implementirajte neprimjetne mehanizme ažuriranja modela  
- Dizajnirajte aplikacije koje se prilagođavaju poboljšanim mogućnostima modela  
- Planirajte za kompatibilnost unatrag s postojećim modelima  
- Implementirajte A/B testiranje za evaluaciju performansi modela  

**Evolucija značajki**  

- [Windows App SDK Samples Repository](https://github.com/microsoft/WindowsAppSDK-Samples)

### Alati za razvoj
- [AI Toolkit za Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Primjeri](https://learn.microsoft.com/windows/ai/samples/)
- [Alati za konverziju modela](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tehnička podrška
- [Windows ML Dokumentacija](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentacija](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentacija](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Prijava problema - Windows App SDK Primjeri](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Zajednica i podrška
- [Windows Zajednica za razvojne programere](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Obuka](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ovaj vodič osmišljen je da se razvija zajedno s brzo napredujućim ekosustavom Windows AI. Redovita ažuriranja osiguravaju usklađenost s najnovijim mogućnostima platforme i najboljim praksama razvoja.*

[08. Praktično s Microsoft Foundry Local - Kompletan alat za razvojne programere](../Module08/README.md)

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.