<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb6eadc312d5658a0cd71c0085b43742",
  "translation_date": "2025-09-22T20:16:20+00:00",
  "source_file": "Module07/README.md",
  "language_code": "fi"
}
-->
# Luku 07: EdgeAI-esimerkit

Edge AI yhdistää tekoälyn ja reunalaskennan, mahdollistaen älykkään datankäsittelyn suoraan laitteilla ilman pilviyhteyttä. Tässä luvussa tarkastellaan viittä erilaista EdgeAI-toteutusta eri alustoilla ja kehyksillä, jotka osoittavat tekoälymallien monipuolisuuden ja tehokkuuden reunalaskennassa.

## 1. EdgeAI NVIDIA Jetson Orin Nanolla

NVIDIA Jetson Orin Nano on merkittävä edistysaskel saavutettavassa reunalaskennassa, tarjoten jopa 67 TOPS:n tekoälytehoa kompaktissa, luottokortin kokoisessa muodossa. Tämä tehokas EdgeAI-alusta tuo generatiivisen tekoälyn kehittämisen harrastajien, opiskelijoiden ja ammattilaisten ulottuville.

### Keskeiset ominaisuudet
- Tarjoaa jopa 67 TOPS:n tekoälytehoa—1,7-kertainen parannus edeltäjään verrattuna
- 1024 CUDA-ydintä ja jopa 32 Tensor-ydintä tekoälykäsittelyyn
- 6-ytiminen Arm Cortex-A78AE v8.2 64-bittinen CPU, maksimitaajuus 1,5 GHz
- Hinta vain $249, mikä tekee siitä edullisen ja saavutettavan alustan kehittäjille, opiskelijoille ja harrastajille

### Sovellukset
Jetson Orin Nano loistaa modernien generatiivisten tekoälymallien, kuten visio-transformerien, suurten kielimallien ja visio-kielimallien, suorittamisessa. Se on erityisesti suunniteltu GenAI-käyttötapauksiin, ja nyt voit ajaa useita LLM-malleja kämmenen kokoisella laitteella. Suosittuja käyttötapauksia ovat tekoälyohjatut robotit, älykkäät dronet, älykkäät kamerat ja autonomiset reunalaitteet.

**Lisätietoja**: [NVIDIA:n Jetson Orin Nano SuperComputer: Seuraava suuri askel EdgeAI:ssa](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI mobiilisovelluksissa .NET MAUI:lla ja ONNX Runtime GenAI:lla

Tämä ratkaisu näyttää, kuinka Generatiivinen tekoäly ja Suuret kielimallit (LLM:t) voidaan integroida alustojen välisiin mobiilisovelluksiin käyttämällä .NET MAUI:ta (Multi-platform App UI) ja ONNX Runtime GenAI:ta. Tämä lähestymistapa mahdollistaa .NET-kehittäjille kehittyneiden tekoälyohjattujen mobiilisovellusten rakentamisen, jotka toimivat natiivisti Android- ja iOS-laitteilla.

### Keskeiset ominaisuudet
- Rakennettu .NET MAUI-kehykselle, joka tarjoaa yhden koodipohjan sekä Android- että iOS-sovelluksille
- ONNX Runtime GenAI -integraatio mahdollistaa generatiivisten tekoälymallien suorittamisen suoraan mobiililaitteilla
- Tukee erilaisia mobiililaitteille räätälöityjä laitteistokiihdyttimiä, kuten CPU, GPU ja erikoistuneet mobiilitekoälyprosessorit
- Alustakohtaiset optimoinnit, kuten CoreML iOS:lle ja NNAPI Androidille ONNX Runtime -kehityksen kautta
- Toteuttaa koko generatiivisen tekoälyprosessin, mukaan lukien esikäsittely, jälkikäsittely, inferenssi, logits-käsittely, haku ja näytteenotto sekä KV-välimuistin hallinta

### Kehityksen hyödyt
.NET MAUI:n avulla kehittäjät voivat hyödyntää olemassa olevia C#- ja .NET-taitojaan rakentaessaan alustojen välisiä tekoälysovelluksia. ONNX Runtime GenAI -kehys tukee useita mallirakenteita, kuten Llama, Mistral, Phi, Gemma ja monia muita. Optimoidut ARM64-ytimet nopeuttavat INT4-kvantisointimatriisikertolaskuja, varmistaen tehokkaan suorituskyvyn mobiililaitteilla samalla kun säilytetään tuttu .NET-kehityskokemus.

### Käyttötapaukset
Tämä ratkaisu sopii kehittäjille, jotka haluavat rakentaa tekoälyohjattuja mobiilisovelluksia .NET-teknologioilla, mukaan lukien älykkäät chatbotit, kuvantunnistussovellukset, kieltenkäännöstyökalut ja henkilökohtaiset suositusjärjestelmät, jotka toimivat täysin laitteella yksityisyyden ja offline-toiminnallisuuden parantamiseksi.

**Lisätietoja**: [.NET MAUI ONNX Runtime GenAI -esimerkki](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI Azurella ja Small Language Models Engine -ratkaisulla

Microsoftin Azure-pohjainen EdgeAI-ratkaisu keskittyy Pienten kielimallien (SLM) tehokkaaseen käyttöönottoon pilvi-reuna-hybridialustoilla. Tämä lähestymistapa yhdistää pilvipalvelujen laajamittaiset tekoälyominaisuudet ja reunalaskennan vaatimukset.

### Arkkitehtuurin edut
- Saumaton integrointi Azure AI -palveluihin
- SLM/LLM- ja multimodaalimallien suorittaminen laitteella ja pilvessä ONNX Runtime -kehityksen avulla
- Optimoitu yritystason käyttöönottoon
- Tuki jatkuville mallipäivityksille ja hallinnalle

### Käyttötapaukset
Azure EdgeAI -toteutus loistaa tilanteissa, joissa tarvitaan yritystason tekoälyn käyttöönottoa pilvihallintakyvyillä. Näitä ovat esimerkiksi älykäs asiakirjojen käsittely, reaaliaikainen analytiikka ja hybridit tekoälytyönkulut, jotka hyödyntävät sekä pilvi- että reunalaskentaresursseja.

**Lisätietoja**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI Windows ML:llä

Windows ML on Microsoftin huippuluokan runtime, joka on optimoitu tehokkaaseen mallien suorittamiseen laitteella ja yksinkertaiseen käyttöönottoon. Se toimii Windows AI Foundryn perustana ja mahdollistaa kehittäjille tekoälyohjattujen Windows-sovellusten luomisen, jotka hyödyntävät PC-laitteiston koko potentiaalia.

### Alustan ominaisuudet
- Toimii kaikilla Windows 11 -tietokoneilla, joissa on versio 24H2 (build 26100) tai uudempi
- Toimii kaikilla x64- ja ARM64-PC-laitteilla, myös tietokoneilla, joissa ei ole NPU:ta tai GPU:ta
- Mahdollistaa kehittäjille omien mallien tuomisen ja tehokkaan käyttöönoton AMD:n, Intelin, NVIDIA:n ja Qualcommin CPU-, GPU- ja NPU-ekosysteemissä
- Infrastruktuuri-API:en avulla kehittäjien ei tarvitse luoda useita sovelluksen versioita eri laitteistoille

### Kehittäjän hyödyt
Windows ML abstrahoi laitteiston ja suorituspalvelut, joten voit keskittyä koodin kirjoittamiseen. Lisäksi Windows ML päivittyy automaattisesti tukemaan uusimpia NPU-, GPU- ja CPU-laitteita niiden julkaisun yhteydessä. Alusta tarjoaa yhtenäisen kehyksen tekoälykehitykselle Windows-laitteiden monipuolisessa ekosysteemissä.

**Lisätietoja**: 
- [Windows ML -yleiskatsaus](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI -kehitysopas](../windowdeveloper.md) - Kattava opas Windows EdgeAI-kehitykseen

## 5. EdgeAI Foundry Local -sovelluksilla

Foundry Local mahdollistaa kehittäjille Retrieval Augmented Generation (RAG) -sovellusten rakentamisen paikallisia resursseja käyttäen .NET:ssä, yhdistäen paikalliset kielimallit semanttisen haun ominaisuuksiin. Tämä lähestymistapa tarjoaa yksityisyyttä korostavia tekoälyratkaisuja, jotka toimivat täysin paikallisessa infrastruktuurissa.

### Tekninen arkkitehtuuri
- Yhdistää Phi-kielimallin, paikalliset upotukset ja semanttisen ytimen RAG-skenaarion luomiseksi
- Käyttää upotuksia vektoreina (liukulukuarvojen taulukkoina), jotka edustavat sisällön semanttista merkitystä
- Semanttinen ydin toimii pääorkestraattorina, integroimalla Phi:n ja älykkäät komponentit saumattoman RAG-putken luomiseksi
- Tuki paikallisille vektorikannoille, kuten SQLite ja Qdrant

### Toteutuksen hyödyt
RAG, eli Retrieval Augmented Generation, tarkoittaa yksinkertaisesti "etsitään tietoa ja lisätään se kehotteeseen". Tämä paikallinen toteutus varmistaa datan yksityisyyden samalla kun tarjoaa älykkäitä vastauksia, jotka perustuvat mukautettuihin tietokantoihin. Lähestymistapa on erityisen arvokas yritysskenaarioissa, joissa vaaditaan datan suvereniteettia ja offline-toimintakykyä.

**Lisätietoja**: [Foundry Local RAG -esimerkit](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local tarjoaa OpenAI-yhteensopivan REST-palvelimen, joka käyttää ONNX Runtimea mallien suorittamiseen paikallisesti Windowsilla. Alla on nopea, validoitu yhteenveto; katso viralliset dokumentit täydellisiä tietoja varten.

- Aloita: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkkitehtuuri: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-viite: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Täydellinen Windows-opas tässä repossa: [foundrylocal.md](./foundrylocal.md)

Asenna tai päivitä Windowsilla (cmd.exe):
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

Windows-alustaa erityisesti tavoitteleville kehittäjille olemme luoneet kattavan oppaan, joka kattaa koko Windows EdgeAI-ekosysteemin. Tämä resurssi tarjoaa yksityiskohtaista tietoa Windows AI Foundrysta, mukaan lukien API:t, työkalut ja parhaat käytännöt EdgeAI-kehitykseen Windowsilla.

### Windows AI Foundry -alusta
Windows AI Foundry -alusta tarjoaa kattavan työkalujen ja API:en valikoiman, joka on erityisesti suunniteltu EdgeAI-kehitykseen Windows-laitteilla. Tämä sisältää erikoistuen NPU-kiihdytetyille laitteille, Windows ML -integraation ja alustakohtaiset optimointitekniikat.

**Kattava opas**: [Windows EdgeAI -kehitysopas](../windowdeveloper.md)

Tämä opas kattaa:
- Windows AI Foundry -alustan yleiskatsauksen ja komponentit
- Phi Silica API tehokkaaseen inferenssiin NPU-laitteistolla
- Tietokonenäkö-API:t kuvankäsittelyyn ja OCR:ään
- Windows ML -runtime-integraation ja optimoinnin
- Foundry Local CLI paikalliseen kehitykseen ja testaukseen
- Laitteisto-optimointistrategiat Windows-laitteille
- Käytännön toteutusesimerkit ja parhaat käytännöt

### Tekoälytyökalupakki EdgeAI-kehitykseen
Visual Studio Codea käyttävien kehittäjien tarpeisiin AI Toolkit -laajennus tarjoaa kattavan kehitysympäristön, joka on erityisesti suunniteltu EdgeAI-sovellusten rakentamiseen, testaamiseen ja käyttöönottoon. Tämä työkalupakki virtaviivaistaa koko EdgeAI-kehitysprosessin VS Code -ympäristössä.

**Kehitysopas**: [AI Toolkit EdgeAI-kehitykseen](../aitoolkit.md)

AI Toolkit -opas kattaa:
- Mallien löytäminen ja valinta reunalaskentaan
- Paikalliset testaus- ja optimointityönkulut
- ONNX- ja Ollama-integraatio reunamalleille
- Mallien muunnos- ja kvantisointitekniikat
- Agenttien kehitys reunaskenaarioihin
- Suorituskyvyn arviointi ja seuranta
- Käyttöönoton valmistelu ja parhaat käytännöt

## Yhteenveto

Nämä viisi EdgeAI-toteutusta osoittavat reunalaskennan tekoälyratkaisujen kypsyyden ja monimuotoisuuden. Laitteistokiihdytetyistä reunalaitteista, kuten Jetson Orin Nano, ohjelmistokehyksiin, kuten ONNX Runtime GenAI ja Windows ML, kehittäjillä on ennennäkemättömiä mahdollisuuksia älykkäiden sovellusten käyttöönottoon reunalla.

Kaikkien näiden alustojen yhteinen piirre on tekoälyominaisuuksien demokratisointi, mikä tekee kehittyneestä koneoppimisesta saavutettavaa kehittäjille eri taitotasoilla ja käyttötapauksissa. Olipa kyseessä mobiilisovellusten, työpöytäsovellusten tai sulautettujen järjestelmien rakentaminen, nämä EdgeAI-ratkaisut tarjoavat perustan seuraavan sukupolven älykkäille sovelluksille, jotka toimivat tehokkaasti ja yksityisesti reunalla.

Jokainen alusta tarjoaa ainutlaatuisia etuja: Jetson Orin Nano laitteistokiihdytettyyn reunalaskentaan, ONNX Runtime GenAI alustojen väliseen mobiilikehitykseen, Azure EdgeAI yritystason pilvi-reuna-integraatioon, Windows ML Windows-natiivisovelluksiin ja Foundry Local yksityisyyttä korostaviin RAG-toteutuksiin. Yhdessä ne muodostavat kattavan ekosysteemin EdgeAI-kehitykseen.

---

