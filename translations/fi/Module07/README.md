<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:37:31+00:00",
  "source_file": "Module07/README.md",
  "language_code": "fi"
}
-->
# Luku 07: EdgeAI-esimerkit

Edge AI yhdistää tekoälyn ja reunalaskennan, mahdollistaen älykkään käsittelyn suoraan laitteilla ilman pilviyhteyttä. Tässä luvussa tarkastellaan viittä erilaista EdgeAI-toteutusta eri alustoilla ja kehyksillä, jotka osoittavat tekoälymallien monipuolisuuden ja tehon reunalaitteilla.

## 1. EdgeAI NVIDIA Jetson Orin Nano -laitteessa

NVIDIA Jetson Orin Nano edustaa merkittävää edistysaskelta saavutettavassa reunalaskennassa, tarjoten jopa 67 TOPS:n tekoälytehon kompaktissa, luottokortin kokoisessa muodossa. Tämä tehokas EdgeAI-alusta demokratisoi generatiivisen tekoälyn kehittämisen harrastajille, opiskelijoille ja ammattilaisille.

### Keskeiset ominaisuudet
- Tarjoaa jopa 67 TOPS:n tekoälytehon—1,7-kertainen parannus edeltäjään verrattuna
- 1024 CUDA-ydintä ja jopa 32 Tensor-ydintä tekoälykäsittelyyn
- 6-ytiminen Arm Cortex-A78AE v8.2 64-bittinen CPU, maksimitaajuus 1,5 GHz
- Hinta vain 249 dollaria, tarjoten kehittäjille, opiskelijoille ja harrastajille edullisen ja saavutettavan alustan

### Sovellukset
Jetson Orin Nano loistaa modernien generatiivisten tekoälymallien, kuten visio-transformerien, suurten kielimallien ja visio-kielimallien, suorittamisessa. Se on erityisesti suunniteltu GenAI-käyttötarkoituksiin, ja nyt voit käyttää useita LLM-malleja kämmenen kokoisella laitteella. Suosittuja käyttötarkoituksia ovat tekoälyohjatut robotit, älykkäät dronet, älykkäät kamerat ja autonomiset reunalaitteet.

**Lisätietoja**: [NVIDIA:n Jetson Orin Nano SuperComputer: Seuraava suuri askel EdgeAI:ssa](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI mobiilisovelluksissa .NET MAUI:n ja ONNX Runtime GenAI:n avulla

Tämä ratkaisu näyttää, kuinka Generatiivinen tekoäly ja Suuret kielimallit (LLM:t) voidaan integroida alustojen välisiin mobiilisovelluksiin käyttämällä .NET MAUI:ta (Multi-platform App UI) ja ONNX Runtime GenAI:ta. Tämä lähestymistapa mahdollistaa .NET-kehittäjille kehittyneiden tekoälyohjattujen mobiilisovellusten rakentamisen, jotka toimivat natiivisti Android- ja iOS-laitteilla.

### Keskeiset ominaisuudet
- Rakennettu .NET MAUI-kehyksen päälle, tarjoten yhden koodipohjan sekä Android- että iOS-sovelluksille
- ONNX Runtime GenAI -integraatio mahdollistaa generatiivisten tekoälymallien suorittamisen suoraan mobiililaitteilla
- Tukee erilaisia mobiililaitteille räätälöityjä laitteistokiihdyttimiä, kuten CPU, GPU ja erikoistuneet mobiilitekoälyprosessorit
- Alustakohtaiset optimoinnit, kuten CoreML iOS:lle ja NNAPI Androidille ONNX Runtime -kehityksen kautta
- Toteuttaa täydellisen generatiivisen tekoälyprosessin, mukaan lukien esikäsittely, jälkikäsittely, inferenssi, logits-käsittely, haku ja näytteenotto sekä KV-välimuistin hallinta

### Kehityksen hyödyt
.NET MAUI:n avulla kehittäjät voivat hyödyntää olemassa olevia C#- ja .NET-taitojaan rakentaessaan alustojen välisiä tekoälysovelluksia. ONNX Runtime GenAI -kehys tukee useita mallirakenteita, kuten Llama, Mistral, Phi, Gemma ja monia muita. Optimoidut ARM64-ytimet nopeuttavat INT4-kvantisointimatriisikertolaskuja, varmistaen tehokkaan suorituskyvyn mobiililaitteilla samalla kun säilytetään tuttu .NET-kehityskokemus.

### Käyttötarkoitukset
Tämä ratkaisu sopii kehittäjille, jotka haluavat rakentaa tekoälyohjattuja mobiilisovelluksia .NET-teknologioilla, mukaan lukien älykkäät chatbotit, kuvantunnistussovellukset, kieltenkäännöstyökalut ja henkilökohtaiset suositusjärjestelmät, jotka toimivat täysin laitteessa yksityisyyden ja offline-toiminnallisuuden parantamiseksi.

**Lisätietoja**: [.NET MAUI ONNX Runtime GenAI -esimerkki](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI Azure-alustalla Small Language Models Engine -ratkaisun avulla

Microsoftin Azure-pohjainen EdgeAI-ratkaisu keskittyy Pienten kielimallien (SLM) tehokkaaseen käyttöönottoon pilvi-reuna-hybridialustoilla. Tämä lähestymistapa yhdistää pilvipalvelujen tekoälyominaisuudet ja reunalaitteiden vaatimukset.

### Arkkitehtuurin edut
- Saumaton integrointi Azure AI -palveluihin
- SLM/LLM- ja multimodaalimallien suorittaminen laitteessa ja pilvessä ONNX Runtime -kehityksen avulla
- Optimoitu yritystason käyttöönottoon
- Tukee jatkuvia mallipäivityksiä ja hallintaa

### Käyttötarkoitukset
Azure EdgeAI -toteutus loistaa tilanteissa, joissa tarvitaan yritystason tekoälyn käyttöönottoa pilvihallintakyvyillä. Tämä sisältää älykkään dokumenttien käsittelyn, reaaliaikaisen analytiikan ja hybriditekoälytyönkulut, jotka hyödyntävät sekä pilvi- että reunalaskentaresursseja.

**Lisätietoja**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI Windows ML:n avulla](./windowdeveloper.md)

Windows ML edustaa Microsoftin huippuluokan suoritusympäristöä, joka on optimoitu tehokkaaseen mallien suorittamiseen laitteessa ja yksinkertaiseen käyttöönottoon. Se toimii Windows AI Foundryn perustana, mahdollistaen tekoälyohjattujen Windows-sovellusten kehittämisen, jotka hyödyntävät PC-laitteiston koko potentiaalia.

### Alustan ominaisuudet
- Toimii kaikilla Windows 11 -tietokoneilla, joissa on versio 24H2 (build 26100) tai uudempi
- Toimii kaikilla x64- ja ARM64-PC-laitteilla, myös tietokoneilla, joissa ei ole NPU:ta tai GPU:ta
- Mahdollistaa kehittäjien omien mallien tuomisen ja tehokkaan käyttöönoton AMD:n, Intelin, NVIDIA:n ja Qualcommin laitteistokumppaniekosysteemissä, mukaan lukien CPU, GPU, NPU
- Infrastruktuuri-API:en avulla kehittäjien ei enää tarvitse luoda useita sovellusrakenteita eri laitteistoille

### Kehittäjän hyödyt
Windows ML abstrahoi laitteiston ja suoritusympäristöt, joten voit keskittyä koodin kirjoittamiseen. Lisäksi Windows ML päivittyy automaattisesti tukemaan uusimpia NPU-, GPU- ja CPU-laitteita niiden julkaisun yhteydessä. Alusta tarjoaa yhtenäisen kehyksen tekoälyn kehittämiseen Windows-laitteiden monipuolisessa ekosysteemissä.

**Lisätietoja**: 
- [Windows ML -yleiskatsaus](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI -kehitysopas](./windowdeveloper.md) - Kattava opas Windows EdgeAI-kehitykseen

## [5. EdgeAI Foundry Local -sovellusten avulla](./foundrylocal.md)

Foundry Local mahdollistaa Windows- ja Mac-kehittäjille Retrieval Augmented Generation (RAG) -sovellusten rakentamisen paikallisia resursseja käyttäen .NET:ssä, yhdistäen paikalliset kielimallit semanttisen haun ominaisuuksiin. Tämä lähestymistapa tarjoaa yksityisyyttä korostavia tekoälyratkaisuja, jotka toimivat täysin paikallisessa infrastruktuurissa.

### Tekninen arkkitehtuuri
- Yhdistää Phi-kielimallin, paikalliset upotukset ja semanttisen ytimen RAG-skenaarion luomiseksi
- Käyttää upotuksia vektoreina (liukulukuarvojen taulukkoina), jotka edustavat sisältöä ja sen semanttista merkitystä
- Semanttinen ydin toimii pääorkestraattorina, integroimalla Phi:n ja älykkäät komponentit saumattoman RAG-putken luomiseksi
- Tukee paikallisia vektorikantoja, kuten SQLite ja Qdrant

### Toteutuksen hyödyt
RAG, eli Retrieval Augmented Generation, tarkoittaa yksinkertaisesti "etsi tietoa ja lisää se kehotteeseen". Tämä paikallinen toteutus varmistaa tietosuojan samalla kun tarjoaa älykkäitä vastauksia, jotka perustuvat mukautettuihin tietokantoihin. Lähestymistapa on erityisen arvokas yritystapauksissa, joissa vaaditaan tietosuvereniteettia ja offline-toimintakykyä.

**Lisätietoja**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG -esimerkit](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local tarjoaa OpenAI-yhteensopivan REST-palvelimen, jota ONNX Runtime käyttää mallien suorittamiseen paikallisesti Windowsissa. Alla on nopea, validoitu yhteenveto; katso viralliset dokumentit saadaksesi täydelliset tiedot.

- Aloita: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkkitehtuuri: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-viite: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Täydellinen Windows-opas tässä repossa: [foundrylocal.md](./foundrylocal.md)

Asenna tai päivitä Windowsissa (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Tutki CLI-kategorioita:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Suorita malli ja löydä dynaaminen päätepiste:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Nopea REST-tarkistus mallien listaamiseksi (korvaa PORT tilasta):
```cmd
curl -s http://localhost:PORT/v1/models
```

Vinkkejä:
- SDK-integraatio: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Tuo oma malli (käännä): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI-kehitysresurssit

Windows-alustaa erityisesti tavoitteleville kehittäjille olemme luoneet kattavan oppaan, joka kattaa koko Windows EdgeAI-ekosysteemin. Tämä resurssi tarjoaa yksityiskohtaista tietoa Windows AI Foundrysta, mukaan lukien API:t, työkalut ja parhaat käytännöt EdgeAI-kehitykseen Windowsissa.

### Windows AI Foundry -alusta
Windows AI Foundry -alusta tarjoaa kattavan työkalujen ja API:en valikoiman, joka on erityisesti suunniteltu EdgeAI-kehitykseen Windows-laitteilla. Tämä sisältää erikoistuen NPU-kiihdytetylle laitteistolle, Windows ML -integraation ja alustakohtaiset optimointitekniikat.

**Kattava opas**: [Windows EdgeAI -kehitysopas](../windowdeveloper.md)

Tämä opas kattaa:
- Windows AI Foundry -alustan yleiskatsauksen ja komponentit
- Phi Silica API tehokkaaseen inferenssiin NPU-laitteistolla
- Tietokonenäkö-API:t kuvankäsittelyyn ja OCR:ään
- Windows ML -suoritusympäristön integrointi ja optimointi
- Foundry Local CLI paikalliseen kehitykseen ja testaukseen
- Laitteisto-optimointistrategiat Windows-laitteille
- Käytännön toteutusesimerkit ja parhaat käytännöt

### [AI Toolkit EdgeAI-kehitykseen](./aitoolkit.md)
Visual Studio Codea käyttäville kehittäjille AI Toolkit -laajennus tarjoaa kattavan kehitysympäristön, joka on erityisesti suunniteltu EdgeAI-sovellusten rakentamiseen, testaamiseen ja käyttöönottoon. Tämä työkalu virtaviivaistaa koko EdgeAI-kehitystyönkulun VS Code -ympäristössä.

**Kehitysopas**: [AI Toolkit EdgeAI-kehitykseen](./aitoolkit.md)

AI Toolkit -opas kattaa:
- Mallien löytäminen ja valinta reunakäyttöön
- Paikalliset testaus- ja optimointityönkulut
- ONNX- ja Ollama-integraatio reunamalleille
- Mallien muunnos- ja kvantisointitekniikat
- Agenttien kehitys reunaskenaarioihin
- Suorituskyvyn arviointi ja seuranta
- Käyttöönoton valmistelu ja parhaat käytännöt

## Yhteenveto

Nämä viisi EdgeAI-toteutusta osoittavat reunalaskennan ratkaisujen kypsyyden ja monimuotoisuuden nykyään. Laitteistokiihdytetyistä reunalaitteista, kuten Jetson Orin Nano, ohjelmistokehyksiin, kuten ONNX Runtime GenAI ja Windows ML, kehittäjillä on ennennäkemättömiä vaihtoehtoja älykkäiden sovellusten käyttöönottoon reunalla.

Kaikkien näiden alustojen yhteinen piirre on tekoälyominaisuuksien demokratisointi, joka tekee kehittyneestä koneoppimisesta saavutettavaa kehittäjille eri taitotasoilla ja käyttötarkoituksissa. Olipa kyseessä mobiilisovellusten, työpöytäohjelmistojen tai sulautettujen järjestelmien rakentaminen, nämä EdgeAI-ratkaisut tarjoavat perustan seuraavan sukupolven älykkäille sovelluksille, jotka toimivat tehokkaasti ja yksityisesti reunalla.

Jokainen alusta tarjoaa ainutlaatuisia etuja: Jetson Orin Nano laitteistokiihdytettyyn reunalaskentaan, ONNX Runtime GenAI alustojen väliseen mobiilikehitykseen, Azure EdgeAI yritystason pilvi-reuna-integraatioon, Windows ML Windows-natiivisovelluksiin ja Foundry Local yksityisyyttä korostaviin RAG-toteutuksiin. Yhdessä ne muodostavat kattavan ekosysteemin EdgeAI-kehitykseen.

---

