<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T13:23:31+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "fi"
}
-->
# Windows Edge AI Kehitysopas

## Johdanto

Tervetuloa Windows Edge AI -kehityksen pariin – kattavaan oppaaseen, joka auttaa sinua rakentamaan älykkäitä sovelluksia hyödyntäen Microsoftin Windows AI Foundry -alustaa. Tämä opas on suunniteltu erityisesti Windows-kehittäjille, jotka haluavat integroida huippuluokan Edge AI -ominaisuuksia sovelluksiinsa ja hyödyntää Windows-laitteiston kiihdytyksen täyttä potentiaalia.

### Windows AI:n edut

Windows AI Foundry tarjoaa yhtenäisen, luotettavan ja turvallisen alustan, joka tukee koko AI-kehittäjän elinkaarta – mallin valinnasta ja hienosäädöstä optimointiin ja käyttöönottoon CPU-, GPU-, NPU- ja hybridipilviarkkitehtuureissa. Tämä alusta demokratisoi AI-kehityksen tarjoamalla:

- **Laitteistoabstraktio**: Saumaton käyttöönotto AMD-, Intel-, NVIDIA- ja Qualcomm-piirisarjoilla
- **Paikallinen älykkyys**: Tietosuojaa kunnioittava AI, joka toimii täysin paikallisella laitteistolla
- **Optimoitu suorituskyky**: Windows-laitteistolle valmiiksi optimoidut mallit
- **Yrityskäyttöön valmis**: Tuotantotason turvallisuus- ja vaatimustenmukaisuusominaisuudet

### Miksi Windows Edge AI:lle?

**Universaali laitteistotuki**  
Windows ML tarjoaa automaattisen laitteisto-optimoinnin koko Windows-ekosysteemissä, varmistaen, että AI-sovelluksesi toimivat optimaalisesti riippumatta taustalla olevasta piirisarjasta.

**Integroitu AI-ajonaika**  
Sisäänrakennettu Windows ML -tulkintamoottori poistaa monimutkaiset asennusvaatimukset, jolloin kehittäjät voivat keskittyä sovelluslogiikkaan infrastruktuurin sijaan.

**Copilot+ PC -optimointi**  
Tarkoitukseen suunnitellut API:t, jotka on kehitetty erityisesti seuraavan sukupolven Windows-laitteille, joissa on omistettuja Neural Processing Unit (NPU) -yksiköitä, tarjoavat poikkeuksellisen suorituskyvyn per watti.

**Kehittäjäekosysteemi**  
Rikkaat työkalut, kuten Visual Studio -integraatio, kattava dokumentaatio ja esimerkkisovellukset, jotka nopeuttavat kehityssyklejä.

## Oppimistavoitteet

Tämän Windows Edge AI -kehitysoppaan suorittamalla opit olennaiset taidot tuotantovalmiiden AI-sovellusten rakentamiseen Windows-alustalla.

### Keskeiset tekniset osaamisalueet

**Windows AI Foundry -osaaminen**  
- Ymmärrä Windows AI Foundry -alustan arkkitehtuuri ja komponentit  
- Navigoi AI-kehityksen koko elinkaari Windows-ekosysteemissä  
- Toteuta turvallisuusparhaita käytäntöjä paikallisille AI-sovelluksille  
- Optimoi sovellukset eri Windows-laitteistokokoonpanoille  

**API-integraatioasiantuntemus**  
- Hallitse Windows AI API:t tekstin, kuvan ja multimodaalisten sovellusten osalta  
- Toteuta Phi Silica -kielimallin integrointi tekstin generointiin ja päättelyyn  
- Käytä sisäänrakennettuja kuvankäsittely-API:ita tietokonenäköominaisuuksien käyttöönottoon  
- Mukauta valmiiksi koulutettuja malleja LoRA (Low-Rank Adaptation) -tekniikoilla  

**Foundry Local -toteutus**  
- Selaa, arvioi ja ota käyttöön avoimen lähdekoodin kielimalleja Foundry Local CLI:n avulla  
- Ymmärrä mallien optimointi ja kvantisointi paikallista käyttöä varten  
- Toteuta offline-AI-ominaisuuksia, jotka toimivat ilman internet-yhteyttä  
- Hallitse mallien elinkaarta ja päivityksiä tuotantoympäristöissä  

**Windows ML -käyttöönotto**  
- Tuo mukautettuja ONNX-malleja Windows-sovelluksiin Windows ML:n avulla  
- Hyödynnä automaattista laitteistokiihdytystä CPU-, GPU- ja NPU-arkkitehtuureissa  
- Toteuta reaaliaikainen tulkinta optimaalisella resurssien käytöllä  
- Suunnittele skaalautuvia AI-sovelluksia monipuolisille Windows-laiteluokille  

### Sovelluskehitystaidot

**Windowsin monialustakehitys**  
- Rakenna AI-tehostettuja sovelluksia .NET MAUI:lla universaalia Windows-käyttöönottoa varten  
- Integroi AI-ominaisuuksia Win32-, UWP- ja progressiivisiin verkkosovelluksiin  
- Toteuta responsiivisia käyttöliittymiä, jotka mukautuvat AI-prosessointitiloihin  
- Käsittele asynkronisia AI-toimintoja asianmukaisilla käyttäjäkokemusmalleilla  

**Suorituskyvyn optimointi**  
- Profiiloi ja optimoi AI-tulkinnan suorituskyky eri laitteistokokoonpanoissa  
- Toteuta tehokas muistinhallinta suurille kielimalleille  
- Suunnittele sovelluksia, jotka mukautuvat käytettävissä oleviin laitteistoresursseihin  
- Käytä välimuististrategioita usein käytettyjen AI-toimintojen osalta  

**Tuotantovalmius**  
- Toteuta kattava virheenkäsittely ja varajärjestelmät  
- Suunnittele telemetria ja seuranta AI-sovellusten suorituskyvylle  
- Käytä turvallisuusparhaita käytäntöjä paikallisten AI-mallien tallennukseen ja suorittamiseen  
- Suunnittele käyttöönotto- ja jakelustrategiat yritys- ja kuluttajasovelluksille  

### Liiketoiminnallinen ja strateginen ymmärrys

**AI-sovellusarkkitehtuuri**  
- Suunnittele hybridialustat, jotka optimoivat paikallisen ja pilvi-AI-prosessoinnin välillä  
- Arvioi kompromisseja mallin koon, tarkkuuden ja tulkintanopeuden välillä  
- Suunnittele tietovirta-arkkitehtuureja, jotka säilyttävät yksityisyyden ja mahdollistavat älykkyyden  
- Toteuta kustannustehokkaita AI-ratkaisuja, jotka skaalautuvat käyttäjien tarpeiden mukaan  

**Markkinapositiointi**  
- Ymmärrä Windows-natiivien AI-sovellusten kilpailuedut  
- Tunnista käyttötapaukset, joissa paikallinen AI tarjoaa ylivoimaisen käyttäjäkokemuksen  
- Kehitä markkinoillemenostrategioita AI-tehostetuille Windows-sovelluksille  
- Aseta sovellukset hyödyntämään Windows-ekosysteemin etuja  

## Windows App SDK AI -esimerkit

Windows App SDK tarjoaa kattavia esimerkkejä, jotka havainnollistavat AI-integraatiota eri kehys- ja käyttöönottoympäristöissä. Nämä esimerkit ovat olennaisia viitteitä Windows AI -kehitysmallien ymmärtämiseksi.

### Windows AI Foundry -esimerkit

| Esimerkki | Kehys | Painopistealue | Keskeiset ominaisuudet |
|-----------|-------|----------------|-------------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API:t | Täydellinen WinUI-sovellus, joka havainnollistaa Windows AI API:ita, ARM64-optimointia, paketoitua käyttöönottoa |

**Keskeiset teknologiat:**  
- Windows AI API:t  
- WinUI 3 -kehys  
- ARM64-alustan optimointi  
- Copilot+ PC -yhteensopivuus  
- Paketoitu sovelluksen käyttöönotto  

**Edellytykset:**  
- Windows 11, suositeltu Copilot+ PC  
- Visual Studio 2022  
- ARM64-rakennuskonfiguraatio  
- Windows App SDK 1.8.1+  

### Windows ML -esimerkit

#### C++-esimerkit

| Esimerkki | Tyyppi | Painopistealue | Keskeiset ominaisuudet |
|-----------|--------|----------------|-------------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolisovellus | Perus Windows ML | EP-haku, komentorivivaihtoehdot, mallin kääntäminen |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolisovellus | Kehysriippuvainen käyttöönotto | Jaettu ajonaika, pienempi käyttöönottojälki |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolisovellus | Itsenäinen käyttöönotto | Standalone-käyttöönotto, ei ajonaikaisia riippuvuuksia |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Kirjaston käyttö | WindowsML jaettu kirjastossa, muistinhallinta |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet-opetusohjelma | Mallin muuntaminen, EP-kääntäminen, Build 2025 -opetusohjelma |

#### C#-esimerkit

**Konsolisovellukset**

| Esimerkki | Tyyppi | Painopistealue | Keskeiset ominaisuudet |
|-----------|--------|----------------|-------------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsolisovellus | Perus C#-integraatio | Jaettujen apuvälineiden käyttö, komentorivikäyttöliittymä |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet-opetusohjelma | Mallin muuntaminen, EP-kääntäminen, Build 2025 -opetusohjelma |

**GUI-sovellukset**

| Esimerkki | Kehys | Painopistealue | Keskeiset ominaisuudet |
|-----------|-------|----------------|-------------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Työpöytä-GUI | Kuvien luokittelu WPF-käyttöliittymällä |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Perinteinen GUI | Kuvien luokittelu Windows Formsilla |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderni GUI | Kuvien luokittelu WinUI 3 -käyttöliittymällä |

#### Python-esimerkit

| Esimerkki | Kieli | Painopistealue | Keskeiset ominaisuudet |
|-----------|-------|----------------|-------------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Kuvien luokittelu | WinML Python-sidokset, eräkuvankäsittely |

### Esimerkkien edellytykset

**Järjestelmävaatimukset:**  
- Windows 11 PC, versio 24H2 (build 26100) tai uudempi  
- Visual Studio 2022, C++- ja .NET-työkuormat  
- Windows App SDK 1.8.1 tai uudempi  
- Python 3.10–3.13 Python-esimerkeille x64- ja ARM64-laitteilla  

**Windows AI Foundry -erityisvaatimukset:**  
- Suositeltu Copilot+ PC optimaaliseen suorituskykyyn  
- ARM64-rakennuskonfiguraatio Windows AI -esimerkeille  
- Paketti-identiteetti vaaditaan (paketoimattomia sovelluksia ei enää tueta)  

### Yleinen esimerkkityönkulku

Useimmat Windows ML -esimerkit noudattavat tätä vakiomallia:

1. **Ympäristön alustaminen** – Luo ONNX Runtime -ympäristö  
2. **Suoritustarjoajien rekisteröinti** – Etsi ja rekisteröi saatavilla olevat laitteistokiihdyttimet (CPU, GPU, NPU)  
3. **Mallin lataaminen** – Lataa ONNX-malli, tarvittaessa käännä kohdelaitteistolle  
4. **Syötteen esikäsittely** – Muunna kuvat/tiedot mallin syöteformaattiin  
5. **Tulkinnan suorittaminen** – Suorita malli ja hanki ennusteet  
6. **Tulosten käsittely** – Käytä softmaxia ja näytä parhaat ennusteet  

### Käytetyt mallitiedostot

| Malli | Tarkoitus | Sisältyy | Huomautukset |
|-------|----------|----------|--------------|
| SqueezeNet | Kevyt kuvien luokittelu | ✅ Sisältyy | Valmiiksi koulutettu, käyttövalmis |
| ResNet-50 | Korkean tarkkuuden kuvien luokittelu | ❌ Vaatii muuntamisen | Käytä [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) -työkalua muuntamiseen |

### Laitetuki

Kaikki esimerkit havaitsevat ja hyödyntävät automaattisesti saatavilla olevan laitteiston:  
- **CPU** – Universaali tuki kaikilla Windows-laitteilla  
- **GPU** – Automaattinen havaitseminen ja optimointi saatavilla olevalle grafiikkalaitteistolle  
- **NPU** – Hyödyntää Neural Processing Unit -yksiköitä tuetuilla laitteilla (Copilot+ PC:t)  

## Windows AI Foundry -alustan komponentit

### 1. Windows AI API:t

Windows AI API:t tarjoavat käyttövalmiita AI-ominaisuuksia, jotka perustuvat paikallisiin malleihin ja ovat optimoitu tehokkuuden ja suorituskyvyn kannalta Copilot+ PC -laitteilla, vaatimatta monimutkaista asennusta.

#### Keskeiset API-kategoriat

**Phi Silica -kielimalli**  
- Pieni mutta tehokas kielimalli tekstin generointiin ja päättelyyn  
- Optimoitu reaaliaikaiseen tulkintaan vähäisellä virrankulutuksella  
- Tukee mukautettua hienosäätöä LoRA-tekniikoilla  
- Integrointi Windowsin semanttiseen hakuun ja tiedonhakuun  

**Tietokonenäkö-API:t**  
- **Tekstin tunnistus (OCR)**: Tunnista tekstiä kuvista tarkasti  
- **Kuvan superresoluutio**: Paranna kuvien tarkkuutta paikallisilla AI-malleilla  
- **Kuvan segmentointi**: Tunnista ja eristä tiettyjä kohteita kuvista  
- **Kuvan kuvaus**: Luo yksityiskohtaisia tekstikuvauksia visuaaliselle sisällölle  
- **Kohteen poisto**: Poista ei-toivotut kohteet kuvista AI-tehostetulla täydennyksellä  

**Multimodaaliset ominaisuudet**  
- **Näkö- ja kieli-integraatio**: Yhdistä tekstin ja kuvan ymmärrys  
- **Semanttinen haku**: Mahdollista luonnollisen kielen kyselyt multimediasisällössä  
- **Tiedonhaku**: Rakenna älykkäitä hakukokemuksia paikallisilla tiedoilla  

### 2. Foundry Local

Foundry Local tarjoaa kehittäjille nopean pääsyn käyttövalmiisiin avoimen lähdekoodin kielimalleihin Windows-piirisarjoilla, mahdollistaen mallien selaamisen, testaamisen, vuorovaikutuksen ja käyttöönoton paikallisissa sovelluksissa.

#### Foundry Local -esimerkkisovellukset

[Foundry Local -repository](https://github.com/microsoft/Foundry-Local/tree/main/samples) tarjoaa kattavia esimerkkejä eri ohjelmointikielillä ja kehyksillä, jotka havainnollistavat erilaisia integraatiomalleja ja käyttötapauksia.

| Esimerkki | Kieli/Kehys | Painopistealue | Keskeiset ominaisuudet |
|-----------|-------------|----------------|-------------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG-toteutus | Semanttinen Kernel-integraatio, Qdrant-vektorivarasto, JINA-embeddit, dokumenttien syöttö, reaaliaikainen chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Työpöytä-chat-s
- **Ominaisuudet**: Mallin valitsin, suoratoistovastaukset, virheenkäsittely, alustojen välinen käyttöönotto
- **Arkkitehtuuri**: Electron-pääprosessi, IPC-kommunikointi, turvalliset esilatausskriptit

**SDK-integraatioesimerkit**
- **JavaScript (Node.js)**: Perusmallin vuorovaikutus ja suoratoistovastaukset
- **Python**: OpenAI-yhteensopiva API käyttö asynkronisella suoratoistolla
- **Rust**: Matalan tason integraatio reqwestin ja tokion kanssa asynkronisia operaatioita varten

#### Edellytykset Foundry Local -näytteille

**Järjestelmävaatimukset:**
- Windows 11, jossa Foundry Local on asennettuna
- Node.js v16+ JavaScript/Electron-näytteille
- .NET 8.0+ C#-näytteille
- Python 3.10+ Python-näytteille
- Rust 1.70+ Rust-näytteille

**Asennus:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Näytekohtainen asennus

**dotNET RAG -näyte:**
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

**Electron Chat -näyte:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust -näytteet:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Keskeiset ominaisuudet

**Mallikatalogi**
- Laaja kokoelma valmiiksi optimoituja avoimen lähdekoodin malleja
- Mallit optimoitu CPU-, GPU- ja NPU-suorittimille välitöntä käyttöönottoa varten
- Tuki suosituimmille malliperheille, kuten Llama, Mistral, Phi, sekä erikoistuneille alakohtaisille malleille

**CLI-integraatio**
- Komentoriviliittymä mallien hallintaan ja käyttöönottoon
- Automaattiset optimointi- ja kvantisointityönkulut
- Integraatio suosittuihin kehitysympäristöihin ja CI/CD-putkistoihin

**Paikallinen käyttöönotto**
- Täysin offline-toiminta ilman pilviriippuvuuksia
- Tuki mukautetuille malliformaateille ja -konfiguraatioille
- Tehokas mallipalvelu automaattisella laitteisto-optimoinnilla

### 3. Windows ML

Windows ML toimii Windowsin keskeisenä tekoälyalustana ja integroituina inferenssiajona, mahdollistaen mukautettujen mallien tehokkaan käyttöönoton laajassa Windows-laitteistoympäristössä.

#### Arkkitehtuurin edut

**Universaali laitteistotuki**
- Automaattinen optimointi AMD-, Intel-, NVIDIA- ja Qualcomm-piirisarjoille
- Tuki CPU-, GPU- ja NPU-suorituksille läpinäkyvällä vaihtamisella
- Laitteistoabstraktio, joka poistaa alustakohtaisen optimointityön

**Mallien joustavuus**
- Tuki ONNX-malliformaatille automaattisella konversiolla suosituista kehyksistä
- Mukautettujen mallien käyttöönotto tuotantotason suorituskyvyllä
- Integraatio olemassa oleviin Windows-sovellusarkkitehtuureihin

**Yritysintegraatio**
- Yhteensopivuus Windowsin turvallisuus- ja vaatimustenmukaisuuskehysten kanssa
- Tuki yrityskäyttöönotolle ja hallintatyökaluille
- Integraatio Windows-laitteiden hallinta- ja valvontajärjestelmiin

## Kehitystyönkulku

### Vaihe 1: Ympäristön asennus ja työkalujen konfigurointi

**Kehitysympäristön valmistelu**
1. Asenna Visual Studio 2022 C++- ja .NET-työkuormilla
2. Asenna Windows App SDK 1.8.1 tai uudempi
3. Konfiguroi Windows AI Foundry CLI -työkalut
4. Asenna AI Toolkit -laajennus Visual Studio Codeen
5. Ota käyttöön suorituskyvyn profilointi- ja valvontatyökalut
6. Varmista ARM64-rakennuskonfiguraatio Copilot+ PC -optimointia varten

**Näytearkiston asennus**
1. Kloonaa [Windows App SDK Samples -arkisto](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Siirry `Samples/WindowsAIFoundry/cs-winui` -hakemistoon Windows AI API -esimerkkien osalta
3. Siirry `Samples/WindowsML` -hakemistoon kattavien Windows ML -esimerkkien osalta
4. Tarkista [rakennusvaatimukset](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) kohdealustoille

**AI Dev Gallery -tutkimus**
- Tutki näytesovelluksia ja viiteimplementaatioita
- Testaa Windows AI API:ta interaktiivisilla demonstraatioilla
- Tarkista lähdekoodi parhaiden käytäntöjen ja mallien osalta
- Tunnista relevantit näytteet omaa käyttötarkoitustasi varten

### Vaihe 2: Mallin valinta ja integrointi

**Vaatimusanalyysi**
- Määritä tekoälyominaisuuksien toiminnalliset vaatimukset
- Aseta suorituskykyrajoitukset ja optimointitavoitteet
- Arvioi yksityisyys- ja turvallisuusvaatimukset
- Suunnittele käyttöönottoarkkitehtuuri ja skaalausstrategiat

**Mallin arviointi**
- Käytä Foundry Localia avoimen lähdekoodin mallien testaamiseen käyttötarkoitustasi varten
- Suorita Windows AI API -vertailut mukautettujen mallivaatimusten osalta
- Arvioi kompromissit mallin koon, tarkkuuden ja inferenssinopeuden välillä
- Prototyyppaa integraatiolähestymistapoja valittujen mallien kanssa

### Vaihe 3: Sovelluskehitys

**Ydinintegraatio**
- Toteuta Windows AI API -integraatio asianmukaisella virheenkäsittelyllä
- Suunnittele käyttöliittymät, jotka tukevat tekoälyprosessointityönkulkuja
- Toteuta välimuisti- ja optimointistrategiat mallin inferenssille
- Lisää telemetria ja valvonta tekoälytoimintojen suorituskyvyn seuraamiseksi

**Testaus ja validointi**
- Testaa sovelluksia eri Windows-laitteistokonfiguraatioilla
- Vahvista suorituskykymittarit eri kuormitustilanteissa
- Toteuta automatisoitu testaus tekoälytoimintojen luotettavuuden varmistamiseksi
- Suorita käyttäjäkokemustestaus tekoälyparannettujen ominaisuuksien osalta

### Vaihe 4: Optimointi ja käyttöönotto

**Suorituskyvyn optimointi**
- Profiloi sovelluksen suorituskyky kohdelaitteistokonfiguraatioilla
- Optimoi muistin käyttö ja mallin latausstrategiat
- Toteuta mukautuva käyttäytyminen käytettävissä olevien laitteistokapasiteettien perusteella
- Hienosäädä käyttäjäkokemus eri suorituskykyskenaarioille

**Tuotantokäyttöönotto**
- Pakkaa sovellukset asianmukaisilla tekoälymalliriippuvuuksilla
- Toteuta päivitysmekanismit malleille ja sovelluslogiikalle
- Konfiguroi valvonta ja analytiikka tuotantoympäristöille
- Suunnittele käyttöönotto- ja jakelustrategiat yritys- ja kuluttajakäyttöön

## Käytännön toteutusesimerkit

### Esimerkki 1: Älykäs dokumenttien käsittelysovellus

Rakenna Windows-sovellus, joka käsittelee dokumentteja useilla tekoälyominaisuuksilla:

**Käytetyt teknologiat:**
- Phi Silica dokumenttien tiivistämiseen ja kysymys-vastaus -toimintoihin
- OCR-rajapinnat tekstin poimintaan skannatuista dokumenteista
- Kuvan kuvausrajapinnat kaavioiden ja diagrammien analysointiin
- Mukautetut ONNX-mallit dokumenttien luokitteluun

**Toteutustapa:**
- Suunnittele modulaarinen arkkitehtuuri, jossa on liitettävät tekoälykomponentit
- Toteuta asynkroninen käsittely suurille dokumenttierille
- Lisää etenemisen ilmaisimet ja peruutustuki pitkäkestoisille operaatioille
- Sisällytä offline-ominaisuus arkaluontoisten dokumenttien käsittelyyn

### Esimerkki 2: Vähittäiskaupan varastonhallintajärjestelmä

Luo tekoälyllä tehostettu varastonhallintajärjestelmä vähittäiskaupan sovelluksiin:

**Käytetyt teknologiat:**
- Kuvan segmentointi tuotteiden tunnistamiseen
- Mukautetut visiomallit brändi- ja kategoriatunnistukseen
- Foundry Local -käyttöönotto erikoistuneille vähittäiskaupan kielimalleille
- Integraatio olemassa oleviin POS- ja varastojärjestelmiin

**Toteutustapa:**
- Rakenna kameraintegraatio reaaliaikaista tuotteen skannausta varten
- Toteuta viivakoodi- ja visuaalinen tuotetunnistus
- Lisää luonnollisen kielen varastokyselyt paikallisilla kielimalleilla
- Suunnittele skaalautuva arkkitehtuuri monikauppakäyttöönottoa varten

### Esimerkki 3: Terveydenhuollon dokumentointiassistentti

Kehitä yksityisyyttä suojaava terveydenhuollon dokumentointityökalu:

**Käytetyt teknologiat:**
- Phi Silica lääketieteellisten muistiinpanojen luomiseen ja kliiniseen päätöksentukeen
- OCR käsinkirjoitettujen lääketieteellisten asiakirjojen digitalisointiin
- Mukautetut lääketieteelliset kielimallit, jotka on otettu käyttöön Windows ML:n kautta
- Paikallinen vektorivarasto lääketieteellisen tiedon hakua varten

**Toteutustapa:**
- Varmista täydellinen offline-toiminta potilaan yksityisyyden suojaamiseksi
- Toteuta lääketieteellisen terminologian validointi ja ehdotukset
- Lisää auditointiloki sääntelyvaatimusten noudattamiseksi
- Suunnittele integraatio olemassa oleviin sähköisiin potilastietojärjestelmiin

## Suorituskyvyn optimointistrategiat

### Laitteistotietoinen kehitys

**NPU-optimointi**
- Suunnittele sovellukset hyödyntämään NPU-ominaisuuksia Copilot+ PC:llä
- Toteuta sujuva siirtyminen GPU/CPU:lle laitteilla, joilla ei ole NPU:ta
- Optimoi malliformaatit NPU-spesifiseen kiihdytykseen
- Seuraa NPU:n käyttöä ja lämpöominaisuuksia

**Muistin hallinta**
- Toteuta tehokkaat mallin lataus- ja välimuististrategiat
- Käytä muistimappauksia suurille malleille käynnistysajan lyhentämiseksi
- Suunnittele muistia säästävät sovellukset resurssirajoitteisille laitteille
- Toteuta mallin kvantisointi muistin optimointia varten

**Akkutehokkuus**
- Optimoi tekoälytoiminnot mahdollisimman vähäiseen virrankulutukseen
- Toteuta mukautuva käsittely akun tilan perusteella
- Suunnittele tehokas taustakäsittely jatkuville tekoälytoiminnoille
- Käytä virran profilointityökaluja energian käytön optimointiin

### Skaalautuvuuden huomioiminen

**Monisäikeisyys**
- Suunnittele säikeiden turvalliset tekoälytoiminnot rinnakkaista käsittelyä varten
- Toteuta tehokas työnjako käytettävissä olevien ytimien kesken
- Käytä async/await-malleja ei-estävään tekoälykäsittelyyn
- Suunnittele säikeiden optimointi eri laitteistokonfiguraatioille

**Välimuististrategiat**
- Toteuta älykäs välimuisti usein käytetyille tekoälytoiminnoille
- Suunnittele välimuistin mitätöintistrategiat mallipäivityksiä varten
- Käytä pysyvää välimuistia kalliille esikäsittelytoiminnoille
- Toteuta hajautettu välimuisti monikäyttäjätilanteisiin

## Turvallisuus- ja yksityisyyskäytännöt

### Tiedonsuojaus

**Paikallinen käsittely**
- Varmista, että arkaluontoiset tiedot eivät koskaan poistu paikalliselta laitteelta
- Toteuta turvallinen tallennus tekoälymalleille ja väliaikaisille tiedoille
- Käytä Windowsin turvallisuusominaisuuksia sovelluksen hiekkalaatikointiin
- Käytä salausmenetelmiä tallennettujen mallien ja välitulosten suojaamiseen

**Mallien turvallisuus**
- Vahvista mallin eheys ennen latausta ja suorittamista
- Toteuta turvalliset mallipäivitysmekanismit
- Käytä allekirjoitettuja malleja manipuloinnin estämiseksi
- Käytä käyttöoikeusvalvontaa mallitiedostoille ja konfiguraatioille

### Vaatimustenmukaisuuden huomioiminen

**Sääntelyyn mukautuminen**
- Suunnittele sovellukset GDPR-, HIPAA- ja muiden sääntelyvaatimusten mukaisiksi
- Toteuta auditointiloki tekoälypäätöksentekoprosesseille
- Tarjoa läpinäkyvyysominaisuuksia tekoälyn tuottamille tuloksille
- Mahdollista käyttäjän hallinta tekoälydatan käsittelyyn

**Yritysturvallisuus**
- Integroi Windowsin yritysturvallisuuspolitiikkoihin
- Tue hallittua käyttöönottoa yrityksen hallintatyökalujen kautta
- Toteuta roolipohjainen käyttöoikeusvalvonta tekoälyominaisuuksille
- Tarjoa hallinnolliset valvontatyökalut tekoälytoiminnoille

## Vianetsintä ja virheenkorjaus

### Yleiset kehityshaasteet

**Rakennuskonfiguraatio-ongelmat**
- Varmista ARM64-alustakonfiguraatio Windows AI API -näytteille
- Tarkista Windows App SDK -version yhteensopivuus (vaaditaan 1.8.1+)
- Vahvista, että paketti-identiteetti on oikein konfiguroitu (vaaditaan Windows AI API:ille)
- Varmista, että rakennustyökalut tukevat kohdekehysversiota

**Mallin latausongelmat**
- Vahvista ONNX-mallin yhteensopivuus Windows ML:n kanssa
- Tarkista mallin tiedostojen eheys ja formaattivaatimukset
- Vahvista laitteistokapasiteettivaatimukset tiettyjen mallien osalta
- Korjaa muistin allokointiongelmat mallin latauksen aikana
- Varmista suorituspalveluntarjoajan rekisteröinti laitteistokiihdytykselle

**Käyttöönoton tilavaihtoehdot**
- **Itse sisällytetty tila**: Täysin tuettu suuremmalla käyttöönoton koolla
- **Kehysriippuvainen tila**: Pienempi jalanjälki, mutta vaatii jaetun ajonaikaisen ympäristön
- **Pakkaamattomat sovellukset**: Ei enää tuettu Windows AI API:ille
- Käytä `dotnet run -p:Platform=ARM64 -p:SelfContained=true` itse sisällytetyssä ARM64-käyttöönotossa

**Suorituskykyongelmat**
- Profiloi sovelluksen suorituskyky eri laitteistokonfiguraatioilla
- Tunnista pullonkaulat tekoälykäsittelyputkistoissa
- Optimoi datan esikäsittely- ja jälkikäsittelytoiminnot
- Toteuta suorituskyvyn valvonta ja hälytykset

**Integraatiohaasteet**
- Korjaa API-integraatio-ongelmat asianmukaisella virheenkäsittelyllä
- Vahvista syöttödatan formaatit ja esikäsittelyvaatimukset
- Testaa reunatapaukset ja virhetilanteet perusteellisesti
- Toteuta kattava lokitus tuotanto-ongelmien vianetsintään

### Virheenkorjaustyökalut ja -tekniikat

**Visual Studio -integraatio**
- Käytä AI Toolkit -virheenkorjainta mallin suoritusanalyysiin
- Toteuta suorituskyvyn profilointi tekoälytoiminnoille
- Korjaa asynkroniset tekoälytoiminnot asianmukaisella poikkeuskäsittelyllä
- Käytä muistiprofil
- [Windows App SDK Samples Repository](https://github.com/microsoft/WindowsAppSDK-Samples)

### Kehitystyökalut
- [AI Toolkit for Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Samples](https://learn.microsoft.com/windows/ai/samples/)
- [Model Conversion Tools](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tekninen tuki
- [Windows ML Dokumentaatio](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentaatio](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentaatio](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Ilmoita ongelmista - Windows App SDK Samples](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Yhteisö ja tuki
- [Windows Developer Community](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blogi](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Koulutus](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Tämä opas on suunniteltu kehittymään Windows AI -ekosysteemin nopean kehityksen mukana. Säännölliset päivitykset varmistavat, että sisältö pysyy ajan tasalla uusimpien alustakyvykkyyksien ja kehityskäytäntöjen kanssa.*

[08. Käytännön harjoituksia Microsoft Foundry Local - Täydellinen kehittäjätyökalupakki](../Module08/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.