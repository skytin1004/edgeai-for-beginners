<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T14:54:46+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "sl"
}
-->
# Vodnik za razvoj Windows Edge AI

## Uvod

Dobrodošli v svetu razvoja Windows Edge AI – vašem celovitem vodniku za gradnjo inteligentnih aplikacij, ki izkoriščajo moč umetne inteligence na napravi z uporabo platforme Windows AI Foundry podjetja Microsoft. Ta vodnik je posebej zasnovan za razvijalce Windows, ki želijo v svoje aplikacije vključiti najnovejše zmogljivosti Edge AI in hkrati izkoristiti celoten spekter strojne pospešitve Windows.

### Prednosti Windows AI

Windows AI Foundry predstavlja enotno, zanesljivo in varno platformo, ki podpira celoten življenjski cikel razvoja umetne inteligence – od izbire in prilagajanja modelov do optimizacije in uvajanja na CPU, GPU, NPU ter hibridne oblačne arhitekture. Ta platforma demokratizira razvoj umetne inteligence z zagotavljanjem:

- **Abstrakcije strojne opreme**: Brezhibno uvajanje na AMD, Intel, NVIDIA in Qualcomm čipe
- **Inteligence na napravi**: AI, ki ohranja zasebnost in deluje izključno na lokalni strojni opremi
- **Optimizirane zmogljivosti**: Modeli, predhodno optimizirani za konfiguracije strojne opreme Windows
- **Pripravljenost za podjetja**: Varnostne in skladnostne funkcije na ravni produkcije

### Zakaj Windows za Edge AI?

**Univerzalna podpora strojne opreme**  
Windows ML zagotavlja samodejno optimizacijo strojne opreme po celotnem ekosistemu Windows, kar omogoča, da vaše AI aplikacije delujejo optimalno ne glede na osnovno arhitekturo čipov.

**Integrirano AI okolje**  
Vgrajeni Windows ML inferenčni motor odpravlja zapletene zahteve za nastavitev, kar razvijalcem omogoča, da se osredotočijo na logiko aplikacije namesto na infrastrukturne skrbi.

**Optimizacija za Copilot+ PC**  
Posebej zasnovani API-ji za naprave Windows nove generacije z namensko nevronsko procesno enoto (NPU), ki zagotavljajo izjemno zmogljivost na vat.

**Razvijalski ekosistem**  
Bogata orodja, vključno z integracijo Visual Studio, obsežno dokumentacijo in vzorčnimi aplikacijami, ki pospešujejo razvojne cikle.

## Cilji učenja

Z zaključkom tega vodnika za razvoj Windows Edge AI boste obvladali ključne veščine za gradnjo produkcijsko pripravljenih AI aplikacij na platformi Windows.

### Osnovne tehnične kompetence

**Obvladovanje Windows AI Foundry**  
- Razumevanje arhitekture in komponent platforme Windows AI Foundry  
- Navigacija po celotnem življenjskem ciklu razvoja AI znotraj ekosistema Windows  
- Uvajanje najboljših varnostnih praks za aplikacije AI na napravi  
- Optimizacija aplikacij za različne konfiguracije strojne opreme Windows  

**Ekspertiza pri integraciji API-jev**  
- Obvladovanje Windows AI API-jev za besedilo, vizijo in multimodalne aplikacije  
- Uvajanje jezikovnega modela Phi Silica za generiranje besedila in sklepanje  
- Uporaba zmogljivosti računalniškega vida z vgrajenimi API-ji za obdelavo slik  
- Prilagajanje predhodno usposobljenih modelov z uporabo tehnik LoRA (Low-Rank Adaptation)  

**Lokalna implementacija Foundry**  
- Brskanje, ocenjevanje in uvajanje odprtokodnih jezikovnih modelov z uporabo Foundry Local CLI  
- Razumevanje optimizacije modelov in kvantizacije za lokalno uvajanje  
- Uvajanje AI zmogljivosti brez povezave, ki delujejo brez internetne povezave  
- Upravljanje življenjskega cikla modelov in posodobitev v produkcijskih okoljih  

**Uvajanje Windows ML**  
- Uvajanje prilagojenih ONNX modelov v aplikacije Windows z uporabo Windows ML  
- Izkoristek samodejne strojne pospešitve na CPU, GPU in NPU arhitekturah  
- Uvajanje inferenc v realnem času z optimalno uporabo virov  
- Oblikovanje skalabilnih AI aplikacij za različne kategorije naprav Windows  

### Veščine razvoja aplikacij

**Razvoj aplikacij za več platform Windows**  
- Gradnja aplikacij, ki jih poganja AI, z uporabo .NET MAUI za univerzalno uvajanje na Windows  
- Integracija AI zmogljivosti v Win32, UWP in progresivne spletne aplikacije  
- Uvajanje odzivnih UI dizajnov, ki se prilagajajo stanjem AI obdelave  
- Upravljanje asinhronih AI operacij z ustreznimi vzorci uporabniške izkušnje  

**Optimizacija zmogljivosti**  
- Profiliranje in optimizacija zmogljivosti AI inferenc na različnih konfiguracijah strojne opreme  
- Uvajanje učinkovitega upravljanja pomnilnika za velike jezikovne modele  
- Oblikovanje aplikacij, ki se prilagodljivo odzivajo glede na razpoložljive zmogljivosti strojne opreme  
- Uporaba strategij predpomnjenja za pogosto uporabljene AI operacije  

**Pripravljenost za produkcijo**  
- Uvajanje celovitega upravljanja napak in mehanizmov za povratne ukrepe  
- Oblikovanje telemetrije in spremljanja zmogljivosti AI aplikacij  
- Uvajanje najboljših varnostnih praks za lokalno shranjevanje in izvajanje AI modelov  
- Načrtovanje strategij uvajanja za podjetniške in potrošniške aplikacije  

### Poslovno in strateško razumevanje

**Arhitektura AI aplikacij**  
- Oblikovanje hibridnih arhitektur, ki optimizirajo med lokalno in oblačno obdelavo AI  
- Ocenjevanje kompromisov med velikostjo modela, natančnostjo in hitrostjo inferenc  
- Načrtovanje arhitektur podatkovnih tokov, ki ohranjajo zasebnost in omogočajo inteligenco  
- Uvajanje stroškovno učinkovitih AI rešitev, ki se prilagajajo zahtevam uporabnikov  

**Pozicioniranje na trgu**  
- Razumevanje konkurenčnih prednosti Windows-native AI aplikacij  
- Identifikacija primerov uporabe, kjer AI na napravi zagotavlja boljšo uporabniško izkušnjo  
- Razvoj strategij za vstop na trg za AI izboljšane Windows aplikacije  
- Pozicioniranje aplikacij za izkoriščanje prednosti ekosistema Windows  

## Vzorci AI v Windows App SDK

Windows App SDK ponuja obsežne vzorce, ki prikazujejo integracijo AI v različnih okvirih in scenarijih uvajanja. Ti vzorci so ključne reference za razumevanje vzorcev razvoja Windows AI.

### Vzorci Windows AI Foundry

| Vzorec | Okvir | Področje | Ključne značilnosti |
|--------|-------|----------|---------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integracija Windows AI API-jev | Celovita WinUI aplikacija, ki prikazuje Windows AI API-je, optimizacijo ARM64, paketno uvajanje |

**Ključne tehnologije:**  
- Windows AI API-ji  
- Okvir WinUI 3  
- Optimizacija platforme ARM64  
- Združljivost s Copilot+ PC  
- Paketno uvajanje aplikacij  

**Predpogoji:**  
- Windows 11, priporočljivo z Copilot+ PC  
- Visual Studio 2022  
- Konfiguracija gradnje ARM64  
- Windows App SDK 1.8.1+  

### Vzorci Windows ML

#### Vzorci v C++

| Vzorec | Tip | Področje | Ključne značilnosti |
|--------|-----|----------|---------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Osnovni Windows ML | Odkritje EP, možnosti ukazne vrstice, kompilacija modela |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Uvajanje okvira | Skupna izvedba, manjši odtis uvajanja |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Samostojno uvajanje | Samostojno uvajanje, brez odvisnosti od okvira |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Uporaba knjižnice | WindowsML v skupni knjižnici, upravljanje pomnilnika |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Vadnica ResNet | Pretvorba modela, kompilacija EP, vadnica Build 2025 |

#### Vzorci v C#

**Konzolne aplikacije**

| Vzorec | Tip | Področje | Ključne značilnosti |
|--------|-----|----------|---------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolna aplikacija | Osnovna integracija C# | Uporaba skupnih pripomočkov, vmesnik ukazne vrstice |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Vadnica ResNet | Pretvorba modela, kompilacija EP, vadnica Build 2025 |

**GUI aplikacije**

| Vzorec | Okvir | Področje | Ključne značilnosti |
|--------|-------|----------|---------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Namizni GUI | Razvrščanje slik z vmesnikom WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradicionalni GUI | Razvrščanje slik z Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderni GUI | Razvrščanje slik z vmesnikom WinUI 3 |

#### Vzorci v Pythonu

| Vzorec | Jezik | Področje | Ključne značilnosti |
|--------|-------|----------|---------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Razvrščanje slik | Python povezave za WinML, obdelava slik v serijah |

### Predpogoji za vzorce

**Sistemske zahteve:**  
- Windows 11 PC z različico 24H2 (gradnja 26100) ali novejšo  
- Visual Studio 2022 z delovnimi obremenitvami za C++ in .NET  
- Windows App SDK 1.8.1 ali novejši  
- Python 3.10-3.13 za Python vzorce na napravah x64 in ARM64  

**Specifično za Windows AI Foundry:**  
- Priporočljiv Copilot+ PC za optimalno zmogljivost  
- Konfiguracija gradnje ARM64 za vzorce Windows AI  
- Zahtevana identiteta paketa (nepakirane aplikacije niso več podprte)  

### Pogost potek dela pri vzorcih

Večina vzorcev Windows ML sledi temu standardnemu vzorcu:

1. **Inicializacija okolja** – Ustvarite okolje ONNX Runtime  
2. **Registracija izvajalnih ponudnikov** – Odkrijte in registrirajte razpoložljive strojne pospeševalnike (CPU, GPU, NPU)  
3. **Nalaganje modela** – Naložite ONNX model, po potrebi ga kompilirajte za ciljno strojno opremo  
4. **Predobdelava vhodnih podatkov** – Pretvorite slike/podatke v format vhodnih podatkov modela  
5. **Izvajanje inferenc** – Izvedite model in pridobite napovedi  
6. **Obdelava rezultatov** – Uporabite softmax in prikažite najboljše napovedi  

### Uporabljene datoteke modelov

| Model | Namen | Vključen | Opombe |
|-------|-------|----------|--------|
| SqueezeNet | Lahka razvrščanje slik | ✅ Vključen | Predhodno usposobljen, pripravljen za uporabo |
| ResNet-50 | Razvrščanje slik z visoko natančnostjo | ❌ Zahteva pretvorbo | Uporabite [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) za pretvorbo |

### Podpora strojne opreme

Vsi vzorci samodejno zaznajo in uporabljajo razpoložljivo strojno opremo:  
- **CPU** – Univerzalna podpora na vseh napravah Windows  
- **GPU** – Samodejno zaznavanje in optimizacija za razpoložljivo grafično strojno opremo  
- **NPU** – Izkoristek nevronskih procesnih enot na podprtih napravah (Copilot+ PC)  

## Komponente platforme Windows AI Foundry

### 1. Windows AI API-ji

Windows AI API-ji zagotavljajo pripravljene AI zmogljivosti, ki jih poganjajo modeli na napravi, optimizirani za učinkovitost in zmogljivost na napravah Copilot+ PC z minimalno potrebno nastavitvijo.

#### Osnovne kategorije API-jev

**Jezikovni model Phi Silica**  
- Majhen, a zmogljiv jezikovni model za generiranje besedila in sklepanje  
- Optimiziran za inferenco v realnem času z minimalno porabo energije  
- Podpora za prilagajanje z uporabo tehnik LoRA  
- Integracija z iskanjem po semantiki Windows in pridobivanjem znanja  

**API-ji za računalniški vid**  
- **Prepoznavanje besedila (OCR)**: Izvleček besedila iz slik z visoko natančnostjo  
- **Super resolucija slik**: Povečanje slik z uporabo lokalnih AI modelov  
- **Segmentacija slik**: Identifikacija in izolacija specifičnih objektov na slikah  
- **Opis slik**: Generiranje podrobnih besedilnih opisov za vizualne vsebine  
- **Brisanje objektov**: Odstranjevanje neželenih objektov s slik z AI-podprtim retuširanjem  

**Multimodalne zmogljivosti**  
- **Integracija vizije in jezika**: Združevanje razumevanja besedila in slik  
- **Semantično iskanje**: Omogočanje naravnih jezikovnih poizvedb po večpredstavnostnih vsebinah  
- **Pridobivanje znanja**: Gradnja inteligentnih iskalnih izkušenj z lokalnimi podatki  

### 2. Foundry Local

Foundry Local razvijalcem omogoča hiter dostop do pripravljenih odprtokodnih jezikovnih modelov na Windows Silicon, kar omogoča brskanje, testiranje, interakcijo in uvajanje modelov v lokalne aplikacije.

#### Vzorčne aplikacije Foundry Local

[Foundry Local repozitorij](https://github.com/microsoft/Foundry-Local/tree/main/samples) ponuja obsežne vzorce v različnih programskih jezikih in okvirih, ki prikazujejo različne vzorce integracije in primere uporabe.

| Vzorec | Jezik/Okvir | Področje | Ključne značilnosti |
|--------|-------------|----------|---------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementacija RAG | Integracija Semantic Kernel, Qdrant vektorska shramba, JINA vektorske predstavitve, zajem dokumentov, pretočni klepet |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Namizna klepetalna aplikacija | Klepet na več platformah, preklapljanje med lokalnimi/oblaki modeli, integracija OpenAI SDK, pretočno sporočanje |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Osnovna integracija | Preprosta uporaba SDK, inicializacija modela, osnovna funkcionalnost klepeta |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Osnovna integracija | Uporaba Python SDK, pretočni odgovori, OpenAI-kompatibilni API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Sistemska integracija | N
- **Funkcije**: Izbira modela, pretočni odgovori, obravnava napak, večplatformska namestitev
- **Arhitektura**: Glavni proces Electron, komunikacija IPC, varni skripti za prednalaganje

**Primeri integracije SDK**
- **JavaScript (Node.js)**: Osnovna interakcija z modeli in pretočni odgovori
- **Python**: Uporaba API-ja, združljivega z OpenAI, z asinhronim pretokom
- **Rust**: Nizkoročnostna integracija z reqwest in tokio za asinhrone operacije

#### Predpogoji za lokalne vzorce Foundry

**Sistemske zahteve:**
- Windows 11 z nameščenim Foundry Local
- Node.js v16+ za vzorce JavaScript/Electron
- .NET 8.0+ za vzorce C#
- Python 3.10+ za vzorce Python
- Rust 1.70+ za vzorce Rust

**Namestitev:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Nastavitev specifična za vzorce

**dotNET RAG vzorec:**
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

**Electron Chat vzorec:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust vzorci:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Ključne funkcije

**Katalog modelov**
- Obsežna zbirka predhodno optimiziranih odprtokodnih modelov
- Optimizacija modelov za CPU, GPU in NPU za takojšnjo uporabo
- Podpora za priljubljene družine modelov, vključno z Llama, Mistral, Phi in specializiranimi modeli za določene domene

**Integracija CLI**
- Vmesnik ukazne vrstice za upravljanje in namestitev modelov
- Avtomatizirani postopki optimizacije in kvantizacije
- Integracija z priljubljenimi razvojnimi okolji in CI/CD procesi

**Lokalna namestitev**
- Popolno delovanje brez povezave, brez odvisnosti od oblaka
- Podpora za prilagojene formate in konfiguracije modelov
- Učinkovito serviranje modelov z avtomatsko optimizacijo strojne opreme

### 3. Windows ML

Windows ML je osrednja AI platforma in integrirano okolje za izvajanje modelov na Windows, ki omogoča razvijalcem učinkovito namestitev prilagojenih modelov na širok spekter strojne opreme Windows.

#### Prednosti arhitekture

**Univerzalna podpora strojne opreme**
- Avtomatska optimizacija za AMD, Intel, NVIDIA in Qualcomm čipe
- Podpora za izvajanje na CPU, GPU in NPU z avtomatskim preklapljanjem
- Abstrakcija strojne opreme, ki odpravlja potrebo po specifični optimizaciji za platformo

**Prilagodljivost modelov**
- Podpora za format modelov ONNX z avtomatsko pretvorbo iz priljubljenih ogrodij
- Namestitev prilagojenih modelov z zmogljivostjo na ravni produkcije
- Integracija z obstoječimi arhitekturami aplikacij Windows

**Integracija v podjetjih**
- Združljivost z varnostnimi in skladnostnimi okviri Windows
- Podpora za orodja za namestitev in upravljanje v podjetjih
- Integracija z orodji za upravljanje in spremljanje naprav Windows

## Potek razvoja

### Faza 1: Priprava okolja in konfiguracija orodij

**Priprava razvojnega okolja**
1. Namestite Visual Studio 2022 z delovnimi obremenitvami za C++ in .NET
2. Namestite Windows App SDK 1.8.1 ali novejši
3. Konfigurirajte CLI orodja Windows AI Foundry
4. Nastavite razširitev AI Toolkit za Visual Studio Code
5. Vzpostavite orodja za profiliranje zmogljivosti in spremljanje
6. Zagotovite konfiguracijo ARM64 za optimizacijo Copilot+ PC

**Nastavitev repozitorija vzorcev**
1. Klonirajte [repozitorij vzorcev Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Pomaknite se do `Samples/WindowsAIFoundry/cs-winui` za primere API-jev Windows AI
3. Pomaknite se do `Samples/WindowsML` za obsežne primere Windows ML
4. Preglejte [zahteve za gradnjo](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) za ciljne platforme

**Raziskovanje galerije AI Dev**
- Raziskujte vzorčne aplikacije in referenčne implementacije
- Preizkusite API-je Windows AI z interaktivnimi demonstracijami
- Preglejte izvorno kodo za najboljše prakse in vzorce
- Identificirajte ustrezne vzorce za vaš specifični primer uporabe

### Faza 2: Izbira in integracija modela

**Analiza zahtev**
- Določite funkcionalne zahteve za AI zmogljivosti
- Vzpostavite omejitve zmogljivosti in cilje optimizacije
- Ocenite zahteve glede zasebnosti in varnosti
- Načrtujte arhitekturo namestitve in strategije skaliranja

**Ocenjevanje modelov**
- Uporabite Foundry Local za testiranje odprtokodnih modelov za vaš primer uporabe
- Primerjajte API-je Windows AI glede na zahteve prilagojenih modelov
- Ocenite kompromise med velikostjo modela, natančnostjo in hitrostjo sklepanja
- Prototipirajte pristope integracije z izbranimi modeli

### Faza 3: Razvoj aplikacije

**Osnovna integracija**
- Implementirajte integracijo API-jev Windows AI z ustreznim obravnavanjem napak
- Oblikujte uporabniške vmesnike, ki upoštevajo delovne tokove AI obdelave
- Implementirajte strategije predpomnjenja in optimizacije za sklepanja modelov
- Dodajte telemetrijo in spremljanje za zmogljivost AI operacij

**Testiranje in validacija**
- Testirajte aplikacije na različnih konfiguracijah strojne opreme Windows
- Validirajte zmogljivostne metrike pod različnimi pogoji obremenitve
- Implementirajte avtomatizirano testiranje za zanesljivost funkcionalnosti AI
- Izvedite testiranje uporabniške izkušnje z AI izboljšanimi funkcijami

### Faza 4: Optimizacija in namestitev

**Optimizacija zmogljivosti**
- Profilirajte zmogljivost aplikacije na ciljni strojni opremi
- Optimizirajte uporabo pomnilnika in strategije nalaganja modelov
- Implementirajte prilagodljivo vedenje glede na razpoložljive zmogljivosti strojne opreme
- Izboljšajte uporabniško izkušnjo za različne scenarije zmogljivosti

**Namestitev v produkcijo**
- Pakirajte aplikacije z ustreznimi odvisnostmi modelov AI
- Implementirajte mehanizme za posodobitev modelov in logike aplikacij
- Konfigurirajte spremljanje in analitiko za produkcijska okolja
- Načrtujte strategije uvajanja za podjetja in potrošnike

## Praktični primeri implementacije

### Primer 1: Aplikacija za inteligentno obdelavo dokumentov

Razvijte Windows aplikacijo, ki obdeluje dokumente z več AI zmogljivostmi:

**Uporabljene tehnologije:**
- Phi Silica za povzemanje dokumentov in odgovarjanje na vprašanja
- OCR API-ji za ekstrakcijo besedila iz skeniranih dokumentov
- API-ji za opis slik za analizo grafikonov in diagramov
- Prilagojeni ONNX modeli za klasifikacijo dokumentov

**Pristop k implementaciji:**
- Oblikujte modularno arhitekturo s priključljivimi AI komponentami
- Implementirajte asinhrono obdelavo za velike serije dokumentov
- Dodajte indikatorje napredka in podporo za preklic dolgotrajnih operacij
- Vključite funkcionalnost brez povezave za obdelavo občutljivih dokumentov

### Primer 2: Sistem za upravljanje zalog v trgovini

Ustvarite AI-podprt sistem za upravljanje zalog za trgovinske aplikacije:

**Uporabljene tehnologije:**
- Segmentacija slik za identifikacijo izdelkov
- Prilagojeni vizualni modeli za klasifikacijo blagovnih znamk in kategorij
- Lokalna namestitev specializiranih jezikovnih modelov za trgovino prek Foundry Local
- Integracija z obstoječimi POS in sistemi za upravljanje zalog

**Pristop k implementaciji:**
- Zgradite integracijo kamer za skeniranje izdelkov v realnem času
- Implementirajte prepoznavanje črtnih kod in vizualno prepoznavanje izdelkov
- Dodajte naravne jezikovne poizvedbe zalog z lokalnimi jezikovnimi modeli
- Oblikujte skalabilno arhitekturo za več trgovin

### Primer 3: Pomočnik za dokumentacijo v zdravstvu

Razvijte orodje za dokumentacijo v zdravstvu, ki ohranja zasebnost:

**Uporabljene tehnologije:**
- Phi Silica za generiranje medicinskih zapisov in podporo pri kliničnih odločitvah
- OCR za digitalizacijo ročno pisanih medicinskih zapisov
- Prilagojeni medicinski jezikovni modeli, nameščeni prek Windows ML
- Lokalno shranjevanje vektorjev za iskanje medicinskega znanja

**Pristop k implementaciji:**
- Zagotovite popolno delovanje brez povezave za zasebnost pacientov
- Implementirajte validacijo medicinske terminologije in predloge
- Dodajte beleženje revizij za skladnost z regulativami
- Oblikujte integracijo z obstoječimi sistemi elektronskih zdravstvenih zapisov

## Strategije optimizacije zmogljivosti

### Razvoj, ki upošteva strojno opremo

**Optimizacija za NPU**
- Oblikujte aplikacije, ki izkoriščajo zmogljivosti NPU na napravah Copilot+
- Implementirajte elegantno preklapljanje na GPU/CPU na napravah brez NPU
- Optimizirajte formate modelov za pospeševanje specifično za NPU
- Spremljajte uporabo NPU in termične značilnosti

**Upravljanje pomnilnika**
- Implementirajte učinkovite strategije nalaganja in predpomnjenja modelov
- Uporabite preslikavo pomnilnika za velike modele za zmanjšanje časa zagona
- Oblikujte aplikacije, ki so zavedne porabe pomnilnika za naprave z omejenimi viri
- Implementirajte kvantizacijo modelov za optimizacijo pomnilnika

**Učinkovitost baterije**
- Optimizirajte AI operacije za minimalno porabo energije
- Implementirajte prilagodljivo obdelavo glede na stanje baterije
- Oblikujte učinkovito obdelavo v ozadju za neprekinjene AI operacije
- Uporabite orodja za profiliranje porabe energije za optimizacijo

### Premisleki o skalabilnosti

**Večnitnost**
- Oblikujte varne AI operacije za sočasno obdelavo
- Implementirajte učinkovito porazdelitev dela med razpoložljiva jedra
- Uporabite vzorce async/await za neblokirajoče AI operacije
- Načrtujte optimizacijo bazenov niti za različne konfiguracije strojne opreme

**Strategije predpomnjenja**
- Implementirajte inteligentno predpomnjenje za pogosto uporabljene AI operacije
- Oblikujte strategije za invalidacijo predpomnilnika pri posodobitvah modelov
- Uporabite trajno predpomnjenje za drage operacije predobdelave
- Implementirajte porazdeljeno predpomnjenje za scenarije z več uporabniki

## Najboljše prakse za varnost in zasebnost

### Zaščita podatkov

**Lokalna obdelava**
- Zagotovite, da občutljivi podatki nikoli ne zapustijo lokalne naprave
- Implementirajte varno shranjevanje za AI modele in začasne podatke
- Uporabite varnostne funkcije Windows za peskovnik aplikacij
- Uporabite šifriranje za shranjene modele in vmesne rezultate obdelave

**Varnost modelov**
- Validirajte celovitost modelov pred nalaganjem in izvajanjem
- Implementirajte varne mehanizme za posodobitev modelov
- Uporabite podpisane modele za preprečevanje manipulacij
- Uporabite nadzorne ukrepe za datoteke modelov in konfiguracijo

### Premisleki o skladnosti

**Regulativna skladnost**
- Oblikujte aplikacije, ki ustrezajo GDPR, HIPAA in drugim regulativnim zahtevam
- Implementirajte beleženje revizij za procese odločanja AI
- Zagotovite funkcije transparentnosti za rezultate, ki jih generira AI
- Omogočite uporabniški nadzor nad obdelavo podatkov AI

**Varnost v podjetjih**
- Integrirajte z varnostnimi politikami podjetja Windows
- Podprite upravljano namestitev prek orodij za upravljanje v podjetjih
- Implementirajte nadzor dostopa na podlagi vlog za funkcije AI
- Zagotovite administrativne kontrole za funkcionalnost AI

## Odpravljanje težav in razhroščevanje

### Pogosti izzivi pri razvoju

**Težave s konfiguracijo gradnje**
- Zagotovite konfiguracijo platforme ARM64 za vzorce API-jev Windows AI
- Preverite združljivost različice Windows App SDK (zahtevana različica 1.8.1+)
- Preverite, ali je identiteta paketa pravilno konfigurirana (zahtevano za API-je Windows AI)
- Validirajte, ali orodja za gradnjo podpirajo ciljno različico ogrodja

**Težave z nalaganjem modelov**
- Validirajte združljivost modelov ONNX z Windows ML
- Preverite celovitost datotek modelov in zahteve glede formata
- Preverite zahteve glede zmogljivosti strojne opreme za specifične modele
- Razhroščite težave z dodeljevanjem pomnilnika med nalaganjem modelov
- Zagotovite registracijo ponudnika izvajanja za pospeševanje strojne opreme

**Premisleki o načinu namestitve**
- **Samostojni način**: Popolnoma podprt z večjo velikostjo namestitve
- **Način odvisen od ogrodja**: Manjši odtis, vendar zahteva skupni runtime
- **Nepakirane aplikacije**: Ni več podprto za API-je Windows AI
- Uporabite `dotnet run -p:Platform=ARM64 -p:SelfContained=true` za samostojno namestitev ARM64

**Težave z zmogljivostjo**
- Profilirajte zmogljivost aplikacije na različnih konfiguracijah strojne opreme
- Identificirajte ozka grla v procesnih tokovih AI
- Optimizirajte operacije predobdelave in postobdelave podatkov
- Implementirajte spremljanje zmogljivosti in opozarjanje

**Težave z integracijo**
- Razhroščite težave z integracijo API-jev z ustreznim obravnavanjem napak
- Validirajte formate vhodnih podatkov in zahteve predobdelave
- Temeljito testirajte robne primere in pogoje napak
- Implementirajte obsežno beleženje za razhroščevanje težav v produkciji

### Orodja in tehnike za razhroščevanje

**Integracija z Visual Studio**
- Uporabite razhroščevalnik AI Toolkit za analizo izvajanja modelov
- Implementirajte profiliranje zmogljivosti za operacije AI
- Razhroščite asinhrone operacije AI z ustreznim obravnavanjem izjem
- Uporabite orodja za profiliranje pomnilnika za optimizacijo

**Orodja Windows AI Foundry**
- Izkoristite CLI Foundry Local za testiranje in validacijo modelov
- Uporabite orodja za testiranje API-jev Windows AI za preverjanje integracije
- Implementirajte prilagojeno beleženje za spremljanje operacij AI
- Ustvarite avtomatizirano testiranje za zanesljivost funkcionalnosti AI

## Priprava aplikacij na prihodnost

### Nastajajoče tehnologije

**Strojna oprema naslednje generacije**
- Oblikujte aplikacije, ki izkoriščajo prihodnje zmogljivosti NPU
- Načrtujte za povečanje velikosti in kompleksnosti modelov
- Implementirajte prilagodljive arhitekture za razvijajočo se strojno opremo
- Razmislite o algoritmih, pripravljenih na kvantno računalništvo, za prihodnjo združljivost

**Napredne AI zmogljivosti**
- Pripravite se na multimodalno integracijo AI za več vrst podatkov
- Načrtujte za sodelovalno AI v realnem času med več napravami
- Oblikujte za zmogljivosti federativnega učenja
- Razmislite o hibridnih arhitekturah inteligence med robom
- [Windows App SDK Samples Repository](https://github.com/microsoft/WindowsAppSDK-Samples)

### Orodja za razvoj
- [AI Toolkit za Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Vzorci](https://learn.microsoft.com/windows/ai/samples/)
- [Orodja za pretvorbo modelov](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tehnična podpora
- [Dokumentacija za Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentacija za ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentacija za Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Poročanje težav - Windows App SDK Samples](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Skupnost in podpora
- [Skupnost razvijalcev za Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Usposabljanje](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ta vodnik je zasnovan tako, da se razvija skupaj s hitro napredujočim ekosistemom Windows AI. Redne posodobitve zagotavljajo usklajenost z najnovejšimi zmogljivostmi platforme in najboljšimi praksami razvoja.*

[08. Praktično z Microsoft Foundry Local - Celoten komplet za razvijalce](../Module08/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.