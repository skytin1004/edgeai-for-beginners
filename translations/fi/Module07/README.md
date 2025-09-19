<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-18T10:47:44+00:00",
  "source_file": "Module07/README.md",
  "language_code": "fi"
}
-->
# Luku 07: EdgeAI-esimerkit

Edge AI edustaa tekoälyn ja reunalaskennan yhdistymistä, mahdollistaen älykkään käsittelyn suoraan laitteilla ilman pilviyhteyttä. Tässä luvussa tarkastellaan viittä erilaista EdgeAI-toteutusta eri alustoilla ja kehyksillä, jotka osoittavat tekoälymallien monipuolisuuden ja tehon reunalaskennassa.

## 1. EdgeAI NVIDIA Jetson Orin Nanolla

NVIDIA Jetson Orin Nano on merkittävä edistysaskel saavutettavassa reunalaskennassa, tarjoten jopa 67 TOPS tekoälytehoa kompaktissa, luottokortin kokoisessa muodossa. Tämä tehokas EdgeAI-alusta demokratisoi generatiivisen tekoälyn kehittämisen harrastajille, opiskelijoille ja ammattilaisille.

### Keskeiset ominaisuudet
- Tarjoaa jopa 67 TOPS tekoälytehoa—1,7-kertainen parannus edeltäjään verrattuna
- 1024 CUDA-ydintä ja jopa 32 Tensor-ydintä tekoälykäsittelyyn
- 6-ytiminen Arm Cortex-A78AE v8.2 64-bittinen CPU, maksimitaajuus 1,5 GHz
- Hinta vain 249 dollaria, tarjoten kehittäjille, opiskelijoille ja harrastajille edullisen ja saavutettavan alustan

### Sovellukset
Jetson Orin Nano loistaa modernien generatiivisten tekoälymallien, kuten visio-transformerien, suurten kielimallien ja visio-kielimallien, suorittamisessa. Se on erityisesti suunniteltu GenAI-käyttötapauksiin, ja nyt voit käyttää useita LLM-malleja kämmenen kokoisella laitteella. Suosittuja käyttötapauksia ovat tekoälyohjatut robotit, älykkäät dronet, älykkäät kamerat ja autonomiset reunalaitteet.

**Lisätietoja**: [NVIDIA:n Jetson Orin Nano SuperComputer: Seuraava suuri askel EdgeAI:ssa](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI mobiilisovelluksissa .NET MAUI:lla ja ONNX Runtime GenAI:lla

Tämä ratkaisu näyttää, kuinka integroida generatiivinen tekoäly ja suuret kielimallit (LLM:t) mobiilisovelluksiin käyttämällä .NET MAUI:ta (Multi-platform App UI) ja ONNX Runtime GenAI:ta. Tämä lähestymistapa mahdollistaa .NET-kehittäjille kehittyneiden tekoälyohjattujen mobiilisovellusten rakentamisen, jotka toimivat natiivisti Android- ja iOS-laitteilla.

### Keskeiset ominaisuudet
- Rakennettu .NET MAUI-kehyksen päälle, tarjoten yhden koodipohjan sekä Android- että iOS-sovelluksille
- ONNX Runtime GenAI -integraatio mahdollistaa generatiivisten tekoälymallien suorittamisen suoraan mobiililaitteilla
- Tukee erilaisia mobiililaitteille räätälöityjä laitteistokiihdyttimiä, kuten CPU, GPU ja erikoistuneet mobiilitekoälyprosessorit
- Alustakohtaiset optimoinnit, kuten CoreML iOS:lle ja NNAPI Androidille ONNX Runtime -kehityksen kautta
- Toteuttaa koko generatiivisen tekoälyprosessin, mukaan lukien esikäsittely, jälkikäsittely, inferenssi, logits-käsittely, haku ja näytteenotto sekä KV-välimuistin hallinta

### Kehityksen hyödyt
.NET MAUI:n avulla kehittäjät voivat hyödyntää olemassa olevia C#- ja .NET-taitojaan rakentaessaan tekoälyohjattuja mobiilisovelluksia. ONNX Runtime GenAI -kehys tukee useita mallirakenteita, kuten Llama, Mistral, Phi, Gemma ja monia muita. Optimoidut ARM64-ytimet nopeuttavat INT4-kvantisointimatriisikertolaskuja, varmistaen tehokkaan suorituskyvyn mobiililaitteilla samalla kun säilytetään tuttu .NET-kehityskokemus.

### Käyttötapaukset
Tämä ratkaisu sopii kehittäjille, jotka haluavat rakentaa tekoälyohjattuja mobiilisovelluksia .NET-teknologioilla, mukaan lukien älykkäät chatbotit, kuvantunnistussovellukset, kieltenkäännöstyökalut ja personoidut suositusjärjestelmät, jotka toimivat täysin laitteessa yksityisyyden ja offline-toiminnallisuuden parantamiseksi.

**Lisätietoja**: [.NET MAUI ONNX Runtime GenAI -esimerkki](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI Azurella ja Small Language Models Engine -ratkaisulla

Microsoftin Azure-pohjainen EdgeAI-ratkaisu keskittyy pienten kielimallien (SLM) tehokkaaseen käyttöönottoon pilvi-reuna-hybridialustoilla. Tämä lähestymistapa yhdistää pilvitasoiset tekoälypalvelut ja reunalaskennan vaatimukset.

### Arkkitehtuurin edut
- Saumaton integraatio Azure AI -palveluiden kanssa
- SLM/LLM- ja multimodaalimallien suorittaminen laitteessa ja pilvessä ONNX Runtime -kehityksen avulla
- Optimoitu yritystason käyttöönottoon
- Tukee jatkuvia mallipäivityksiä ja hallintaa

### Käyttötapaukset
Azure EdgeAI -toteutus loistaa skenaarioissa, jotka vaativat yritystason tekoälyn käyttöönottoa pilvihallintakyvyillä. Näitä ovat älykäs dokumenttien käsittely, reaaliaikainen analytiikka ja hybridit tekoälytyönkulut, jotka hyödyntävät sekä pilvi- että reunalaskentaresursseja.

**Lisätietoja**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI Windows ML:llä

Windows ML edustaa Microsoftin huippuluokan runtimea, joka on optimoitu suorituskykyiseen mallien inferenssiin laitteessa ja yksinkertaiseen käyttöönottoon. Se toimii Windows AI Foundryn perustana, mahdollistaen kehittäjille tekoälyohjattujen Windows-sovellusten luomisen, jotka hyödyntävät PC-laitteiston koko potentiaalia.

### Alustan ominaisuudet
- Toimii kaikilla Windows 11 -tietokoneilla, joissa on versio 24H2 (build 26100) tai uudempi
- Toimii kaikilla x64- ja ARM64-PC-laitteilla, myös tietokoneilla, joissa ei ole NPU:ta tai GPU:ta
- Mahdollistaa kehittäjien omien mallien tuomisen ja tehokkaan käyttöönoton AMD:n, Intelin, NVIDIA:n ja Qualcommin laitteistokumppaniekosysteemissä, mukaan lukien CPU, GPU, NPU
- Infrastruktuuri-API:en avulla kehittäjien ei tarvitse luoda useita sovelluksen versioita eri laitteistoille

### Kehittäjän hyödyt
Windows ML abstrahoi laitteiston ja suorituskykytoimittajat, joten voit keskittyä koodin kirjoittamiseen. Lisäksi Windows ML päivittyy automaattisesti tukemaan uusimpia NPU-, GPU- ja CPU-laitteita niiden julkaisun yhteydessä. Alusta tarjoaa yhtenäisen kehyksen tekoälykehitykselle Windows-laitteiden monipuolisessa ekosysteemissä.

**Lisätietoja**: 
- [Windows ML -yleiskatsaus](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI -kehitysopas](../windowdeveloper.md) - Kattava opas Windows EdgeAI-kehitykseen

## 5. EdgeAI Foundry Local -sovelluksilla

Foundry Local mahdollistaa kehittäjille Retrieval Augmented Generation (RAG) -sovellusten rakentamisen paikallisia resursseja käyttäen .NET:ssä, yhdistäen paikalliset kielimallit semanttisen haun ominaisuuksiin. Tämä lähestymistapa tarjoaa yksityisyyttä korostavia tekoälyratkaisuja, jotka toimivat täysin paikallisessa infrastruktuurissa.

### Tekninen arkkitehtuuri
- Yhdistää Phi-3-kielimallin, paikalliset upotukset ja semanttisen ytimen luodakseen RAG-skenaarion
- Käyttää upotuksia vektoreina (liukulukuarvojen taulukkoina), jotka edustavat sisällön semanttista merkitystä
- Semanttinen ydin toimii pääorkestraattorina, integroimalla Phi-3:n ja älykkäät komponentit saumattoman RAG-putken luomiseksi
- Tukee paikallisia vektoripohjaisia tietokantoja, kuten SQLite ja Qdrant

### Toteutuksen hyödyt
RAG, eli Retrieval Augmented Generation, tarkoittaa yksinkertaisesti "etsi tietoa ja lisää se kehotteeseen". Tämä paikallinen toteutus varmistaa tietosuojan samalla kun tarjoaa älykkäitä vastauksia, jotka perustuvat mukautettuihin tietokantoihin. Lähestymistapa on erityisen arvokas yritysskenaarioissa, jotka vaativat tietosuvereniteettia ja offline-toimintakykyä.

**Lisätietoja**: [Foundry Local RAG -esimerkit](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Windows EdgeAI -kehitysresurssit

Windows-alustaa erityisesti tavoitteleville kehittäjille olemme luoneet kattavan oppaan, joka kattaa koko Windows EdgeAI-ekosysteemin. Tämä resurssi tarjoaa yksityiskohtaista tietoa Windows AI Foundrysta, mukaan lukien API:t, työkalut ja parhaat käytännöt EdgeAI-kehitykseen Windowsissa.

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
Visual Studio Codea käyttävien kehittäjien tarpeisiin AI Toolkit -laajennus tarjoaa kattavan kehitysympäristön, joka on erityisesti suunniteltu EdgeAI-sovellusten rakentamiseen, testaamiseen ja käyttöönottoon. Tämä työkalupakki virtaviivaistaa koko EdgeAI-kehitystyönkulun VS Code -ympäristössä.

**Kehitysopas**: [AI Toolkit EdgeAI-kehitykseen](../aitoolkit.md)

AI Toolkit -opas kattaa:
- Mallien löytämisen ja valinnan reunalaskentaa varten
- Paikalliset testaus- ja optimointityönkulut
- ONNX- ja Ollama-integraation reunamalleille
- Mallien muunnos- ja kvantisointitekniikat
- Agenttien kehitys reunaskenaarioihin
- Suorituskyvyn arviointi ja seuranta
- Käyttöönoton valmistelu ja parhaat käytännöt

## Yhteenveto

Nämä viisi EdgeAI-toteutusta osoittavat reunalaskennan ratkaisujen kypsyyden ja monimuotoisuuden. Laitteistokiihdytetyistä reunalaitteista, kuten Jetson Orin Nano, ohjelmistokehyksiin, kuten ONNX Runtime GenAI ja Windows ML, kehittäjillä on ennennäkemättömiä mahdollisuuksia älykkäiden sovellusten käyttöönottoon reunalaskennassa.

Yhteinen tekijä näissä alustoissa on tekoälyominaisuuksien demokratisointi, joka tekee kehittyneestä koneoppimisesta saavutettavaa kehittäjille eri taitotasoilla ja käyttötapauksissa. Olipa kyseessä mobiilisovellusten, työpöytäsovellusten tai sulautettujen järjestelmien rakentaminen, nämä EdgeAI-ratkaisut tarjoavat perustan seuraavan sukupolven älykkäille sovelluksille, jotka toimivat tehokkaasti ja yksityisesti reunalaskennassa.

Jokainen alusta tarjoaa ainutlaatuisia etuja: Jetson Orin Nano laitteistokiihdytettyyn reunalaskentaan, ONNX Runtime GenAI alustojen väliseen mobiilikehitykseen, Azure EdgeAI yritystason pilvi-reuna-integraatioon, Windows ML Windows-natiivisovelluksiin ja Foundry Local yksityisyyttä korostaviin RAG-toteutuksiin. Yhdessä ne muodostavat kattavan ekosysteemin EdgeAI-kehitykseen.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.