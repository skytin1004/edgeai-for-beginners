<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c817161ba08864340737d623f761b9ae",
  "translation_date": "2025-09-18T08:54:49+00:00",
  "source_file": "README.md",
  "language_code": "fi"
}
-->
# EdgeAI aloittelijoille

![Kurssin kansikuva](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.fi.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Seuraa näitä ohjeita päästäksesi alkuun näiden resurssien käytössä:

1. **Haarauta repositorio**: Klikkaa [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
2. **Kloonaa repositorio**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**Liity Azure AI Foundry Discordiin ja tapaa asiantuntijoita sekä muita kehittäjiä**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Monikielinen tuki

#### Tuettu GitHub Actionin kautta (automaattinen ja aina ajan tasalla)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Finnish](./README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

**Jos haluat lisätä uusia kieliä, tuetut kielet löytyvät [täältä](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Johdanto

Tervetuloa **EdgeAI aloittelijoille** -kurssille, joka tarjoaa kattavan matkan Edge-tekoälyn mullistavaan maailmaan. Tämä kurssi yhdistää tehokkaat tekoälyominaisuudet ja käytännönläheisen toteutuksen reunalaitteilla, antaen sinulle mahdollisuuden hyödyntää tekoälyn potentiaalia suoraan siellä, missä data syntyy ja päätöksiä tarvitaan.

### Mitä opit hallitsemaan

Kurssi vie sinut peruskäsitteistä tuotantovalmiisiin toteutuksiin, käsitellen:
- **Pienet kielimallit (SLM)**, jotka on optimoitu reunalaitteille
- **Laitteistotietoista optimointia** eri alustoilla
- **Reaaliaikaista päättelyä**, joka säilyttää yksityisyyden
- **Tuotantototeutuksen strategioita** yrityssovelluksiin

### Miksi EdgeAI on tärkeä

EdgeAI edustaa paradigman muutosta, joka vastaa nykyajan kriittisiin haasteisiin:
- **Yksityisyys ja turvallisuus**: Käsittele arkaluontoista dataa paikallisesti ilman pilvipalveluja
- **Reaaliaikainen suorituskyky**: Poista verkkoviive kriittisissä sovelluksissa
- **Kustannustehokkuus**: Vähennä kaistanleveyden ja pilvilaskennan kuluja
- **Toiminnan kestävyys**: Säilytä toiminnallisuus verkkokatkosten aikana
- **Säädösten noudattaminen**: Täytä datan suvereniteettivaatimukset

### EdgeAI

EdgeAI tarkoittaa tekoälyalgoritmien ja kielimallien suorittamista paikallisesti laitteistolla – lähellä datan syntypaikkaa – ilman pilvipalvelujen käyttöä päättelyyn. Tämä vähentää viivettä, parantaa yksityisyyttä ja mahdollistaa reaaliaikaisen päätöksenteon.

### Keskeiset periaatteet:
- **Laitteistopohjainen päättely**: Tekoälymallit toimivat reunalaitteilla (puhelimet, reitittimet, mikro-ohjaimet, teollisuus-PC:t)
- **Offline-kyvykkyys**: Toimii ilman jatkuvaa internet-yhteyttä
- **Matala viive**: Välittömät vastaukset reaaliaikaisiin järjestelmiin
- **Datan suvereniteetti**: Pitää arkaluontoisen datan paikallisena, parantaen turvallisuutta ja säädösten noudattamista

### Pienet kielimallit (SLM)

SLM:t, kuten Phi-4, Mistral-7B ja Gemma, ovat optimoituja versioita suuremmista LLM-malleista – koulutettuja tai tiivistettyjä:
- **Pienempi muistijalanjälki**: Tehokas käyttö reunalaitteiden rajallisessa muistissa
- **Vähemmän laskentatehon tarvetta**: Optimoitu CPU- ja reunalaitteiden GPU-suorituskykyyn
- **Nopeammat käynnistysajat**: Nopeasti reagoivat sovellukset

Ne avaavat tehokkaita NLP-ominaisuuksia samalla täyttäen seuraavat rajoitukset:
- **Sulautetut järjestelmät**: IoT-laitteet ja teollisuusohjaimet
- **Mobiililaitteet**: Älypuhelimet ja tabletit offline-kyvykkyyksillä
- **IoT-laitteet**: Anturit ja älylaitteet, joilla on rajalliset resurssit
- **Reunapalvelimet**: Paikalliset prosessointiyksiköt, joilla on rajalliset GPU-resurssit
- **Henkilökohtaiset tietokoneet**: Työpöytä- ja kannettavat käyttötilanteet

## Kurssin rakenne

### [Moduuli 01: EdgeAI:n perusteet ja muutos](./Module01/README.md)
**Teema**: EdgeAI:n käyttöönoton mullistava muutos

#### Luvun rakenne:
- [**Osio 1: EdgeAI:n perusteet**](./Module01/01.EdgeAIFundamentals.md)
  - Perinteisen pilvitekoälyn ja EdgeAI:n vertailu
  - Reunalaskennan haasteet ja rajoitukset
  - Keskeiset teknologiat: mallien kvantisointi, kompressio-optimointi, pienet kielimallit (SLM)
  - Laitteistokiihdytys: NPU:t, GPU-optimointi, CPU-optimointi
  - Edut: yksityisyys, turvallisuus, matala viive, offline-kyvykkyys, kustannustehokkuus

- [**Osio 2: Käytännön esimerkkitapaukset**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi- ja Mu-malliekosysteemi
  - Japan Airlinesin tekoälyraportointijärjestelmän esimerkkitapaus
  - Markkinavaikutus ja tulevaisuuden suuntaukset
  - Käyttöönoton huomioitavat seikat ja parhaat käytännöt

- [**Osio 3: Käytännön toteutusopas**](./Module01/03.PracticalImplementationGuide.md)
  - Kehitysympäristön asennus (Python 3.10+, .NET 8+)
  - Laitteistovaatimukset ja suositellut kokoonpanot
  - Keskeiset malliperheen resurssit
  - Kvantisointi- ja optimointityökalut (Llama.cpp, Microsoft Olive, Apple MLX)
  - Arviointi- ja tarkistuslista

- [**Osio 4: EdgeAI:n käyttöönoton laitteistoalustat**](./Module01/04.EdgeDeployment.md)
  - EdgeAI:n käyttöönoton huomioitavat seikat ja vaatimukset
  - Intelin EdgeAI-laitteisto ja optimointitekniikat
  - Qualcommin tekoälyratkaisut mobiili- ja sulautettuihin järjestelmiin
  - NVIDIA Jetson ja reunalaskenta-alustat
  - Windowsin tekoäly-PC-alustat NPU-kiihdytyksellä
  - Laitteistokohtaiset optimointistrategiat

---

### [Moduuli 02: Pienten kielimallien perusteet](./Module02/README.md)
**Teema**: SLM:n teoreettiset periaatteet, toteutusstrategiat ja tuotantokäyttö

#### Luvun rakenne:
- [**Osio 1: Microsoft Phi -malliperheen perusteet**](./Module02/01.PhiFamily.md)
  - Suunnittelufilosofian kehitys (Phi-1:stä Phi-4:ään)
  - Tehokkuus ensin -arkkitehtuurisuunnittelu
  - Erikoistuneet ominaisuudet (päättely, multimodaalisuus, reunakäyttöönotto)

- [**Osio 2: Qwen-malliperheen perusteet**](./Module02/02.QwenFamily.md)
  - Avoimen lähdekoodin huippuosaaminen (Qwen 1.0:sta Qwen3:een) – saatavilla Hugging Facen kautta
  - Edistynyt päättelyarkkitehtuuri ajattelutilaominaisuuksilla
  - Skaalautuvat käyttöönotto-optiot (0.5B-235B parametriä)

- [**Osio 3: Gemma-malliperheen perusteet**](./Module02/03.GemmaFamily.md)
  - Tutkimuslähtöinen innovaatio (Gemma 3 & 3n)
  - Multimodaalinen huippuosaaminen
  - Mobiili ensin -arkkitehtuuri

- [**Osio 4: BitNET-malliperheen perusteet**](./Module02/04.BitNETFamily.md)
  - Vallankumouksellinen kvantisointiteknologia (1.58-bittiä)
  - Erikoistunut päättelykehys osoitteessa https://github.com/microsoft/BitNet
  - Kestävä tekoälyjohtajuus äärimmäisen tehokkuuden kautta

- [**Osio 5: Microsoft Mu -mallin perusteet**](./Module02/05.mumodel.md)
  - Laitteisto ensin -arkkitehtuuri, joka on sisäänrakennettu Windows 11:een
  - Järjestelmäintegraatio Windows 11 -asetusten kanssa
  - Yksityisyyttä säilyttävä offline-toiminta

- [**Osio 6: Phi-Silica perusteet**](./Module02/06.phisilica.md)
  - NPU-optimoitu arkkitehtuuri, joka on sisäänrakennettu Windows 11 Copilot+ PC:ihin
  - Poikkeuksellinen tehokkuus (650 tokenia/sekunti 1.5W teholla)
  - Kehittäjäintegraatio Windows App SDK:n kanssa

---

### [Moduuli 03: Pienten kielimallien käyttöönotto](./Module03/README.md)
**Teema**: SLM:n koko elinkaaren käyttöönotto teoriasta tuotantoympäristöön

#### Luvun rakenne:
- [**Osio 1: SLM:n edistynyt oppiminen**](./Module03/01.SLMAdvancedLearning.md)
  - Parametrien luokittelukehys (Micro SLM 100M-1.4B, Medium SLM 14B-30B)
  - Edistyneet optimointitekniikat (kvantisointimenetelmät, BitNET 1-bittinen kvantisointi)
  - Mallien hankintastrategiat (Azure AI Foundry Phi-malleille, Hugging Face valituille malleille)

- [**Osio 2: Paikallisen ympäristön käyttöönotto**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama universaali alustan käyttöönotto
  - Microsoft Foundry paikalliset yritystason ratkaisut
  - Kehysten vertailuanalyysi

- [**Osio 3: Konttipohjainen pilvikäyttöönotto**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM:n suorituskykyinen päättelykäyttöönotto
  - Ollama konttien orkestrointi
  - ONNX Runtime reunalaitteille optimoitu toteutus

---

### [Moduuli 04: Malliformaattien muunnos ja kvantisointi](./Module04/README.md)
**Teema**: Täydellinen mallien optimointityökalupakki reunalaitteille eri alustoilla

#### Luvun rakenne:
- [**Osio 1: Malliformaattien muunnoksen ja kvantisoinnin perusteet**](./Module04/01.Introduce.md)
  - Tarkkuuden luokittelukehys (ultra-matala, matala, keskitarkkuus)
  - GGUF- ja ONNX-formaattien edut ja käyttötapaukset
  - Kvantisoinnin hyödyt operatiivisessa tehokkuudessa
  - Suorituskykyvertailut ja muistijalanjäljen vertailut
- [**Osio 2: Llama.cpp Toteutusopas**](./Module04/02.Llamacpp.md)
  - Monialustainen asennus (Windows, macOS, Linux)
  - GGUF-muodon muuntaminen ja kvantisointitasot (Q2_K - Q8_0)
  - Laitteistokiihdytys (CUDA, Metal, OpenCL, Vulkan)
  - Python-integraatio ja REST API -käyttöönotto

- [**Osio 3: Microsoft Olive Optimointipaketti**](./Module04/03.MicrosoftOlive.md)
  - Laitteistotietoinen mallin optimointi yli 40 sisäänrakennetulla komponentilla
  - Automaattinen optimointi dynaamisella ja staattisella kvantisoinnilla
  - Yritysintegraatio Azure ML -työnkulkujen kanssa
  - Suosittujen mallien tuki (Llama, Phi, valitut Qwen-mallit, Gemma)

- [**Osio 4: OpenVINO Toolkit Optimointipaketti**](./Module04/04.openvino.md)
  - Intelin avoimen lähdekoodin työkalu monialustaiselle AI-käyttöönotolle
  - Neural Network Compression Framework (NNCF) edistyneeseen optimointiin
  - OpenVINO GenAI suurten kielimallien käyttöönottoon
  - Laitteistokiihdytys CPU-, GPU-, VPU- ja AI-kiihdyttimillä

- [**Osio 5: Apple MLX Framework Syväluotaus**](./Module04/05.AppleMLX.md)
  - Yhtenäinen muistirakenne Apple Siliconille
  - Tuki LLaMA-, Mistral-, Phi-3- ja valituille Qwen-malleille
  - LoRA-hienosäätö ja mallin räätälöinti
  - Hugging Face -integraatio 4-bit/8-bit kvantisoinnilla

- [**Osio 6: Edge AI Kehitystyönkulun Synteesi**](./Module04/06.workflow-synthesis.md)
  - Yhtenäinen työnkulkuarkkitehtuuri, joka yhdistää useita optimointikehyksiä
  - Kehyksen valintapuut ja suorituskykyanalyysi
  - Tuotantovalmiuden validointi ja kattavat käyttöönotto-strategiat
  - Tulevaisuuden varmistusstrategiat kehittyville laitteistoille ja mallirakenteille

---

### [Module 05: SLMOps - Pienten Kielimallien Operoinnit](./Module05/README.md)
**Teema**: Täydellinen SLM:n elinkaaren hallinta tislaamisesta tuotantokäyttöön

#### Luvun rakenne:
- [**Osio 1: Johdatus SLMOpsiin**](./Module05/01.IntroduceSLMOps.md)
  - SLMOpsin paradigman muutos AI-operaatioissa
  - Kustannustehokkuus ja yksityisyyttä korostava arkkitehtuuri
  - Strateginen liiketoimintavaikutus ja kilpailuedut
  - Käytännön toteutuksen haasteet ja ratkaisut

- [**Osio 2: Mallin Tislaus - Teoriasta Käytäntöön**](./Module05/02.SLMOps-Distillation.md)
  - Tiedonsiirto opettajamallista oppilasmalleihin
  - Kaksivaiheisen tislausprosessin toteutus
  - Azure ML -tislaustyönkulut käytännön esimerkein
  - 85 % vähemmän inferenssiaikaa säilyttäen 92 % tarkkuuden

- [**Osio 3: Hienosäätö - Mallien Räätälöinti Tiettyihin Tehtäviin**](./Module05/03.SLMOps-Finetuing.md)
  - Parametrien tehokkaat hienosäätötekniikat (PEFT)
  - LoRA- ja QLoRA-edistyneet menetelmät
  - Microsoft Olive -hienosäätö toteutus
  - Moniadapterikoulutus ja hyperparametrien optimointi

- [**Osio 4: Käyttöönotto - Tuotantovalmiin Toteutuksen Käyttöönotto**](./Module05/04.SLMOps.Deployment.md)
  - Mallin muuntaminen ja kvantisointi tuotantokäyttöön
  - Foundry Local -käyttöönottokonfiguraatio
  - Suorituskyvyn vertailu ja laadun validointi
  - 75 % koon pienennys tuotannon seurannalla

---

### [Module 06: SLM Agenttijärjestelmät - AI-agentit ja Funktiokutsut](./Module06/README.md)
**Teema**: SLM-agenttijärjestelmien toteutus perustasta edistyneisiin funktiokutsuihin ja Model Context Protocol -integraatioon

#### Luvun rakenne:
- [**Osio 1: AI-agentit ja Pienten Kielimallien Perusta**](./Module06/01.IntroduceAgent.md)
  - Agenttien luokittelukehys (refleksi-, mallipohjaiset-, tavoitepohjaiset-, oppivat agentit)
  - SLM:n perusteet ja optimointistrategiat (GGUF, kvantisointi, edge-kehykset)
  - SLM vs LLM -analyysi (10-30× kustannussäästö, 70-80 % tehtävän tehokkuus)
  - Käytännön käyttöönotto Ollama-, VLLM- ja Microsoft edge-ratkaisuilla

- [**Osio 2: Funktiokutsut Pienissä Kielimalleissa**](./Module06/02.FunctionCalling.md)
  - Järjestelmällinen työnkulun toteutus (tarkoituksen tunnistus, JSON-tulos, ulkoinen suoritus)
  - Alustakohtaiset toteutukset (Phi-4-mini, valitut Qwen-mallit, Microsoft Foundry Local)
  - Edistyneet esimerkit (moniagenttiyhteistyö, dynaaminen työkalujen valinta)
  - Tuotantokäytön näkökohdat (nopeusrajoitukset, auditointilokit, turvallisuustoimenpiteet)

- [**Osio 3: Model Context Protocol (MCP) Integraatio**](./Module06/03.IntroduceMCP.md)
  - Protokolla-arkkitehtuuri ja kerrostettu järjestelmän suunnittelu
  - Monitaustatuki (Ollama kehitykseen, vLLM tuotantoon)
  - Yhteysprotokollat (STDIO- ja SSE-tilat)
  - Käytännön sovellukset (verkkoprosessointi, datankäsittely, API-integraatio)

---

### [Module 07: EdgeAI Toteutusesimerkit](./Module07/README.md)
**Teema**: Kattavat EdgeAI-toteutukset eri alustoilla ja kehyksillä

#### Luvun rakenne:
- [**AI Toolkit Visual Studio Codelle**](./Module07/aitoolkit.md)
  - Kattava Edge AI -kehitysympäristö VS Codessa
  - Mallikatalogi ja löytö edge-käyttöönottoa varten
  - Paikallinen testaus, optimointi ja agenttikehityksen työnkulut
  - Suorituskyvyn seuranta ja arviointi edge-skenaarioissa

- [**Windows EdgeAI Kehitysohje**](./Module07/windowdeveloper.md)
  - Windows AI Foundry -alustan kattava yleiskatsaus
  - Phi Silica API tehokkaaseen NPU-inferenssiin
  - Tietokonenäkö-API:t kuvankäsittelyyn ja OCR:ään
  - Foundry Local CLI paikalliseen kehitykseen ja testaukseen

- [**EdgeAI NVIDIA Jetson Orin Nanossa**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 67 TOPS AI-suorituskyky luottokortin kokoisessa muodossa
  - Generatiivisten AI-mallien tuki (vision transformers, LLM:t, vision-language-mallit)
  - Sovellukset robotiikassa, droneissa, älykkäissä kameroissa, autonomisissa laitteissa
  - Edullinen $249 alusta demokratisoidulle AI-kehitykselle

- [**EdgeAI Mobiilisovelluksissa .NET MAUI:lla ja ONNX Runtime GenAI:lla**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - Monialustainen mobiili-AI yhdellä C#-koodipohjalla
  - Laitteistokiihdytyksen tuki (CPU, GPU, mobiili-AI-prosessorit)
  - Alustakohtaiset optimoinnit (CoreML iOS:lle, NNAPI Androidille)
  - Täydellinen generatiivisen AI:n silmukan toteutus

- [**EdgeAI Azurella Pienten Kielimallien Moottorilla**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - Pilvi-edge-hybridi käyttöönottoarkkitehtuuri
  - Azure AI -palveluiden integraatio ONNX Runtime -ohjelmistolla
  - Yritystason käyttöönotto ja jatkuva mallinhallinta
  - Hybridi-AI-työnkulut älykkääseen dokumenttien käsittelyyn

- [**EdgeAI Windows ML:llä**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry -perusta tehokkaalle laitepohjaiselle inferenssille
  - Universaali laitteistotuki (AMD, Intel, NVIDIA, Qualcomm-piirit)
  - Automaattinen laitteistoabstraktio ja optimointi
  - Yhtenäinen kehys monipuoliselle Windows-laitteistoympäristölle

- [**EdgeAI Foundry Local -sovelluksilla**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - Yksityisyyttä korostava RAG-toteutus paikallisilla resursseilla
  - Phi-3-kielimallin integraatio semanttiseen hakuun (vain Phi-mallit)
  - Paikallisten vektoridatabassien tuki (SQLite, Qdrant)
  - Tietosuvereniteetti ja offline-toimintamahdollisuudet

## Kurssin Oppimistavoitteet

Tämän kattavan EdgeAI-kurssin suorittamalla kehität asiantuntemusta suunnitella, toteuttaa ja ottaa käyttöön tuotantovalmiita EdgeAI-ratkaisuja. Rakenteellinen lähestymistapamme varmistaa, että hallitset sekä teoreettiset perusteet että käytännön toteutustaidot.

### Tekninen Osaaminen

**Perustiedot**
- Ymmärrä pilvipohjaisten ja edge-pohjaisten AI-arkkitehtuurien keskeiset erot
- Hallitse mallien kvantisoinnin, pakkaamisen ja optimoinnin periaatteet resurssirajoitteisissa ympäristöissä
- Sisäistä laitteistokiihdytysvaihtoehdot (NPU:t, GPU:t, CPU:t) ja niiden käyttöönoton vaikutukset

**Toteutustaidot**
- Ota käyttöön Pieniä Kielimalleja eri edge-alustoilla (mobiili, sulautettu, IoT, edge-palvelimet)
- Sovella optimointikehyksiä, kuten Llama.cpp, Microsoft Olive, ONNX Runtime ja Apple MLX
- Toteuta reaaliaikaisia inferenssijärjestelmiä alle sekunnin vastevaatimuksilla

**Tuotantoasiantuntemus**
- Suunnittele skaalautuvia EdgeAI-arkkitehtuureja yrityssovelluksiin
- Toteuta seurantaa, ylläpitoa ja päivitysstrategioita käyttöön otetuille järjestelmille
- Sovella turvallisuuden parhaita käytäntöjä yksityisyyttä säilyttävissä EdgeAI-toteutuksissa

### Strategiset Kyvykkyydet

**Päätöksentekokehys**
- Arvioi EdgeAI-mahdollisuuksia ja tunnista sopivat käyttötapaukset liiketoimintasovelluksille
- Arvioi kompromisseja mallin tarkkuuden, inferenssinopeuden, virrankulutuksen ja laitekustannusten välillä
- Valitse sopivat SLM-perheet ja konfiguraatiot tiettyjen käyttöönoton rajoitteiden perusteella

**Järjestelmäarkkitehtuuri**
- Suunnittele end-to-end EdgeAI-ratkaisuja, jotka integroituvat olemassa olevaan infrastruktuuriin
- Suunnittele hybridi edge-pilvi-arkkitehtuureja optimaalisen suorituskyvyn ja kustannustehokkuuden saavuttamiseksi
- Toteuta datavirta- ja käsittelyputkia reaaliaikaisiin AI-sovelluksiin

### Teollisuussovellukset

**Käytännön Toteutusskenaariot**
- **Valmistus**: Laadunvalvontajärjestelmät, ennakoiva huolto ja prosessien optimointi
- **Terveysala**: Yksityisyyttä säilyttävät diagnostiikkatyökalut ja potilaan seurantajärjestelmät
- **Liikenne**: Autonomisten ajoneuvojen päätöksenteko ja liikenteen hallinta
- **Älykaupungit**: Älykäs infrastruktuuri ja resurssien hallintajärjestelmät
- **Kulutuselektroniikka**: AI-pohjaiset mobiilisovellukset ja älykotilaitteet

## Oppimistulosten Yhteenveto

### Moduuli 01 Oppimistulokset:
- Ymmärrä pilvi- ja edge-AI-arkkitehtuurien keskeiset erot
- Hallitse keskeiset optimointitekniikat edge-käyttöönottoa varten
- Tunnista käytännön sovellukset ja menestystarinat
- Hanki käytännön taidot EdgeAI-ratkaisujen toteuttamiseen

### Moduuli 02 Oppimistulokset:
- Syvällinen ymmärrys eri SLM-suunnittelufilosofioista ja niiden käyttöönoton vaikutuksista
- Hallitse strategiset päätöksentekokyvyt laskennallisten rajoitteiden ja suorituskykyvaatimusten perusteella
- Ymmärrä käyttöönoton joustavuuden kompromissit
- Omaksu tulevaisuuteen valmiit näkemykset tehokkaista AI-arkkitehtuureista

### Moduuli 03 Oppimistulokset:
- Strategiset mallinvalintakyvyt
- Optimointitekniikoiden hallinta
- Käyttöönoton joustavuuden hallinta
- Tuotantovalmiiden konfiguraatioiden hallinta

### Moduuli 04 Oppimistulokset:
- Syvällinen ymmärrys kvantisointirajoista ja käytännön sovelluksista
- Käytännön kokemus useista optimointikehyksistä (Llama.cpp, Olive, OpenVINO, MLX)
- Hallitse Intel-laitteiston optimointi OpenVINOn ja NNCF:n avulla
- Laitteistotietoisten optimointivalintojen kyvyt eri alustoilla
- Tuotantokäyttöönottotaidot monialustaisissa edge-laskentaympäristöissä
- Strateginen kehysvalinta ja työnkulun synteesi optimaalisiin EdgeAI-ratkaisuihin

### Moduuli 05 Oppimistulokset:
- Hallitse SLMOps-paradigma ja operatiiviset periaatteet
- Toteuta mallin tislaus tiedonsiirtoon ja tehokkuuden optimointiin
- Sovella hienosäätötekniikoita alakohtaisen mallin räätälöintiin
- Ota käyttöön tuotantovalmiita SLM-ratkaisuja seurantaan ja ylläpitoon

### Moduuli 06 Oppimistulokset:
- Ymmärrä AI-agenttien ja Pienten Kielimallien arkkitehtuurin peruskäsitteet
- Hallitse funktiokutsujen toteutus eri alustoilla ja kehyksillä
- Integroi Model Context Protocol (MCP) standardoituun ulkoisten työkalujen vuorovaikutukseen
- Rakenna kehittyneitä agenttijärjestelmiä, jotka vaativat minimaalista ihmisen väliintuloa

### Moduuli 07 Oppimistulokset:
- Hallitse AI Toolkit Visual Studio Codelle kattavien EdgeAI-kehitystyönkulkujen toteuttamiseen
- Hanki asiantuntemusta Windows AI Foundry -alustasta ja NPU-optimointistrategioista
- Saa käytännön kokemusta eri EdgeAI-alustoista ja toteutusstrategioista
- Hallitse laitteistokohtaiset optimointitekniikat NVIDIA-, mobiili-, Azure- ja Windows-alustoilla
- Ymmärrä käyttöönoton kompromissit suorituskyvyn, kustannusten ja yksityisyyden välillä
- Kehitä käytännön taitoja todellisten EdgeAI-sovellusten rakentamiseen eri ekosysteemeissä

## Odotetut Kurssitulokset

Kurssin onnistuneen suorittamisen jälkeen sinulla on tiedot, taidot ja itseluottamus johtaa EdgeAI-aloitteita ammatillisissa ympäristöissä.

### Ammatill
Tämä kurssi asettaa sinut AI-teknologian käyttöönoton eturintamaan, jossa älykkäät ominaisuudet integroituvat saumattomasti laitteisiin ja järjestelmiin, jotka ovat modernin elämän perusta.

## Tiedostorakenteen puukaavio

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

## Kurssin ominaisuudet

- **Progressiivinen oppiminen**: Etene asteittain peruskäsitteistä edistyneeseen käyttöönottoon
- **Teorian ja käytännön yhdistäminen**: Jokainen moduuli sisältää sekä teoreettiset perusteet että käytännön toiminnot
- **Todelliset tapaustutkimukset**: Perustuu Microsoftin, Alibaban, Googlen ja muiden todellisiin tapauksiin
- **Käytännön harjoittelu**: Täydelliset konfiguraatiotiedostot, API-testimenetelmät ja käyttöönoton skriptit
- **Suorituskykyvertailut**: Yksityiskohtaiset vertailut päättelynopeudesta, muistin käytöstä ja resurssivaatimuksista
- **Yritystason näkökulmat**: Turvallisuuskäytännöt, vaatimustenmukaisuuskehykset ja tietosuojastrategiat

## Aloittaminen

Suositeltu oppimispolku:
1. Aloita **Module01**:sta rakentaaksesi perustavanlaatuisen ymmärryksen EdgeAI:sta
2. Jatka **Module02**:een syventääksesi tietämystäsi eri SLM-malliperheistä
3. Opiskele **Module03**:ssa käytännön käyttöönoton taitoja
4. Jatka **Module04**:lla edistyneeseen mallin optimointiin, formaattimuunnoksiin ja kehysintegraatioon
5. Suorita **Module05**: hallitaksesi SLMOps-tuotantovalmiita toteutuksia varten
6. Tutki **Module06**:ta ymmärtääksesi SLM-agenttijärjestelmiä ja toimintokutsujen ominaisuuksia
7. Viimeistele **Module07**:lla saadaksesi käytännön kokemusta AI Toolkitista ja monipuolisista EdgeAI-toteutusesimerkeistä

Jokainen moduuli on suunniteltu itsenäisesti täydelliseksi, mutta peräkkäinen oppiminen tuottaa parhaat tulokset.

## Opas opiskeluun

Kattava [Opas opiskeluun](STUDY_GUIDE.md) on saatavilla auttamaan sinua maksimoimaan oppimiskokemuksesi. Opas sisältää:

- **Rakenteelliset oppimispolut**: Optimoidut aikataulut kurssin suorittamiseen 20 tunnissa
- **Ajan jakamisen ohjeet**: Erityiset suositukset lukemisen, harjoitusten ja projektien tasapainottamiseen
- **Keskeisten käsitteiden painotus**: Priorisoidut oppimistavoitteet jokaiselle moduulille
- **Itsearviointityökalut**: Kysymyksiä ja harjoituksia ymmärryksen testaamiseen
- **Miniprojektien ideat**: Käytännön sovelluksia oppimisen vahvistamiseksi

Opas on suunniteltu sekä intensiiviseen opiskeluun (1 viikko) että osa-aikaiseen opiskeluun (3 viikkoa), ja siinä on selkeät ohjeet siitä, miten voit jakaa aikasi tehokkaasti, vaikka voisit omistaa kurssille vain 10 tuntia.

---

**EdgeAI:n tulevaisuus perustuu jatkuvaan mallirakenteiden, kvantisointitekniikoiden ja käyttöönoton strategioiden parantamiseen, jotka priorisoivat tehokkuuden ja erikoistumisen yleiskäyttöisten ominaisuuksien sijaan. Organisaatiot, jotka omaksuvat tämän paradigman muutoksen, ovat hyvin asemoituneita hyödyntämään AI:n mullistavaa potentiaalia samalla kun ne säilyttävät kontrollin datastaan ja toiminnastaan.**

## Muut kurssit

Tiimimme tuottaa myös muita kursseja! Tutustu:

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

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.