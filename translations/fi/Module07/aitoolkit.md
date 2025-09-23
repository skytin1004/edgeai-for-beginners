<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T10:56:10+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "fi"
}
-->
# AI Toolkit for Visual Studio Code - Edge AI -kehityksen opas

## Johdanto

Tervetuloa kattavaan oppaaseen AI Toolkitin käyttöön Visual Studio Codessa Edge AI -kehityksessä. Kun tekoäly siirtyy keskitetystä pilvilaskennasta hajautetuille reunalaitteille, kehittäjät tarvitsevat tehokkaita, integroituja työkaluja, jotka pystyvät vastaamaan reunasovellusten ainutlaatuisiin haasteisiin – kuten resurssirajoituksiin ja offline-toimintavaatimuksiin.

AI Toolkit Visual Studio Codessa täyttää tämän tarpeen tarjoamalla täydellisen kehitysympäristön, joka on suunniteltu erityisesti tekoälysovellusten rakentamiseen, testaamiseen ja optimointiin, jotta ne toimivat tehokkaasti reunalaitteilla. Olitpa kehittämässä IoT-antureille, mobiililaitteille, sulautetuille järjestelmille tai reunapalvelimille, tämä työkalu virtaviivaistaa koko kehitysprosessisi tutussa VS Code -ympäristössä.

Tämä opas johdattaa sinut keskeisiin käsitteisiin, työkaluihin ja parhaisiin käytäntöihin AI Toolkitin hyödyntämiseksi Edge AI -projekteissasi, alkaen mallin valinnasta aina tuotantoon asti.

## Yleiskatsaus

AI Toolkit tarjoaa integroidun kehitysympäristön koko Edge AI -sovelluksen elinkaarelle VS Codessa. Se mahdollistaa saumattoman integraation suosittujen tekoälymallien kanssa, kuten OpenAI, Anthropic, Google ja GitHub, ja tukee paikallista mallien käyttöönottoa ONNX:n ja Ollaman kautta – kriittisiä ominaisuuksia Edge AI -sovelluksille, jotka vaativat laitepohjaista päättelyä.

Mikä erottaa AI Toolkitin muista Edge AI -kehitystyökaluista, on sen keskittyminen koko reunasovellusten käyttöönoton putkistoon. Toisin kuin perinteiset tekoälykehitystyökalut, jotka keskittyvät pääasiassa pilvikäyttöön, AI Toolkit sisältää erikoistuneita ominaisuuksia mallien optimointiin, resurssirajoitteiseen testaukseen ja reunakohtaiseen suorituskyvyn arviointiin. Työkalu ymmärtää, että Edge AI -kehitys vaatii erilaisia huomioita – pienempiä mallikokoja, nopeampia päättelyaikoja, offline-ominaisuuksia ja laitteistokohtaisia optimointeja.

Alusta tukee useita käyttöönoton skenaarioita, yksinkertaisesta laitepohjaisesta päättelystä monimutkaisiin monimallisiin reunarakenteisiin. Se tarjoaa työkaluja mallien muuntamiseen, kvantisointiin ja optimointiin, jotka ovat välttämättömiä onnistuneelle reunasovellusten käyttöönotolle, samalla säilyttäen VS Coden tunnetun kehittäjäystävällisyyden.

## Oppimistavoitteet

Tämän oppaan lopussa osaat:

### Keskeiset taidot
- **Asentaa ja konfiguroida** AI Toolkitin Visual Studio Codeen Edge AI -kehitystyönkulkuja varten
- **Navigoida ja käyttää** AI Toolkitin käyttöliittymää, mukaan lukien Model Catalog, Playground ja Agent Builder
- **Valita ja arvioida** tekoälymalleja, jotka soveltuvat reunasovelluksiin suorituskyvyn ja resurssirajoitusten perusteella
- **Muuntaa ja optimoida** malleja ONNX-muotoon ja kvantisointitekniikoilla reunalaitteita varten

### Edge AI -kehitystaidot
- **Suunnitella ja toteuttaa** Edge AI -sovelluksia integroidussa kehitysympäristössä
- **Testata malleja** reunamaisissa olosuhteissa paikallisen päättelyn ja resurssien seurannan avulla
- **Luoda ja mukauttaa** tekoälyagentteja, jotka on optimoitu reunasovelluksiin
- **Arvioida mallien suorituskykyä** reunalaskentaan liittyvien mittareiden avulla (viive, muistin käyttö, tarkkuus)

### Optimointi ja käyttöönotto
- **Soveltaa kvantisointi- ja karsintatekniikoita** pienentääksesi mallien kokoa säilyttäen hyväksyttävän suorituskyvyn
- **Optimoida malleja** tiettyjä reunalaitteiden laitteistoalustoja varten, mukaan lukien CPU-, GPU- ja NPU-kiihdytys
- **Toteuttaa parhaita käytäntöjä** Edge AI -kehityksessä, mukaan lukien resurssien hallinta ja varajärjestelmät
- **Valmistella mallit ja sovellukset** tuotantokäyttöön reunalaitteilla

### Edistyneet Edge AI -käsitteet
- **Integrointi reunalaskennan kehyksiin**, kuten ONNX Runtime, Windows ML ja TensorFlow Lite
- **Toteuttaa monimallisia arkkitehtuureja** ja hajautetun oppimisen skenaarioita reunaympäristöissä
- **Ratkaista yleisiä Edge AI -ongelmia**, kuten muistin rajoitukset, päättelynopeus ja laitteistoyhteensopivuus
- **Suunnitella seurantaa ja lokitusta** Edge AI -sovelluksille tuotantoympäristössä

### Käytännön soveltaminen
- **Rakentaa kokonaisvaltaisia Edge AI -ratkaisuja** mallin valinnasta käyttöönottoon
- **Osoittaa osaamista** reunakohtaisissa kehitystyönkuluissa ja optimointitekniikoissa
- **Soveltaa opittuja käsitteitä** todellisiin Edge AI -käyttötapauksiin, kuten IoT-, mobiili- ja sulautettuihin sovelluksiin
- **Arvioida ja vertailla** erilaisia Edge AI -käyttöönoton strategioita ja niiden kompromisseja

## Keskeiset ominaisuudet Edge AI -kehitykseen

### 1. Mallikatalogi ja löytäminen
- **Paikallisten mallien tuki**: Löydä ja käytä tekoälymalleja, jotka on erityisesti optimoitu reunasovelluksiin
- **ONNX-integraatio**: Käytä malleja ONNX-muodossa tehokasta reunapäättelyä varten
- **Ollama-tuki**: Hyödynnä paikallisesti toimivia malleja Ollaman kautta yksityisyyden ja offline-toiminnan takaamiseksi
- **Mallien vertailu**: Vertaa malleja rinnakkain löytääksesi optimaalisen tasapainon suorituskyvyn ja resurssien kulutuksen välillä reunalaitteille

### 2. Interaktiivinen Playground
- **Paikallinen testausympäristö**: Testaa malleja paikallisesti ennen reunasovellusten käyttöönottoa
- **Monimodaalinen kokeilu**: Testaa kuvia, tekstiä ja muita reunasovelluksille tyypillisiä syötteitä
- **Parametrien hienosäätö**: Kokeile erilaisia malliparametreja optimoidaksesi reunarajoituksia varten
- **Reaaliaikainen suorituskyvyn seuranta**: Tarkkaile päättelynopeutta ja resurssien käyttöä kehityksen aikana

### 3. Agent Builder reunasovelluksille
- **Prompt Engineering**: Luo optimoituja kehotteita, jotka toimivat tehokkaasti pienempien reunamallien kanssa
- **MCP-työkalujen integrointi**: Integroi Model Context Protocol -työkalut parannettuihin reunasovellusominaisuuksiin
- **Koodin generointi**: Luo tuotantovalmiita koodeja, jotka on optimoitu reunasovelluksia varten
- **Rakenteelliset tulokset**: Suunnittele agentteja, jotka tuottavat johdonmukaisia ja rakenteellisia vastauksia reunasovelluksiin

### 4. Mallien arviointi ja testaus
- **Suorituskykymittarit**: Arvioi malleja reunasovelluksiin liittyvien mittareiden avulla (viive, muistin käyttö, tarkkuus)
- **Erätestaus**: Testaa useita mallikonfiguraatioita samanaikaisesti löytääksesi optimaaliset reunasäädöt
- **Mukautettu arviointi**: Luo mukautettuja arviointikriteerejä reunasovellusten käyttötapauksiin
- **Resurssiprofilointi**: Analysoi muistin ja laskentatehon vaatimuksia reunasovellusten suunnittelua varten

### 5. Mallien muuntaminen ja optimointi
- **ONNX-muunnos**: Muunna mallit eri formaateista ONNX-muotoon reunayhteensopivuutta varten
- **Kvantisointi**: Pienennä mallien kokoa ja paranna päättelynopeutta kvantisointitekniikoilla
- **Laitteisto-optimointi**: Optimoi mallit tiettyjä reunalaitteiden laitteistoja varten (CPU, GPU, NPU)
- **Formaattimuunnos**: Muunna malleja Hugging Facesta ja muista lähteistä reunasovelluksia varten

### 6. Hienosäätö reunaskenaarioihin
- **Toimialakohtainen mukautus**: Mukauta malleja tiettyihin reunasovelluksiin ja ympäristöihin
- **Paikallinen koulutus**: Kouluta malleja paikallisesti GPU-tuen avulla reunakohtaisia vaatimuksia varten
- **Azure-integraatio**: Hyödynnä Azure Container Apps -palvelua pilvipohjaiseen hienosäätöön ennen reunasovellusten käyttöönottoa
- **Siirto-oppiminen**: Mukauta esikoulutettuja malleja reunakohtaisiin tehtäviin ja rajoituksiin

### 7. Suorituskyvyn seuranta ja jäljitys
- **Reunasuorituskyvyn analyysi**: Seuraa mallien suorituskykyä reunamaisissa olosuhteissa
- **Jäljenkeruu**: Kerää yksityiskohtaisia suorituskykytietoja optimointia varten
- **Pullonkaulojen tunnistaminen**: Tunnista suorituskykyongelmat ennen käyttöönottoa reunalaitteilla
- **Resurssien käytön seuranta**: Tarkkaile muistin, suorittimen ja päättelyajan käyttöä reunasovellusten optimointia varten

## Edge AI -kehitystyönkulku

### Vaihe 1: Mallien löytäminen ja valinta
1. **Tutki mallikatalogia**: Etsi malleja, jotka soveltuvat reunasovelluksiin
2. **Vertaa suorituskykyä**: Arvioi malleja koon, tarkkuuden ja päättelynopeuden perusteella
3. **Testaa paikallisesti**: Käytä Ollamaa tai ONNX-malleja paikalliseen testaukseen ennen reunasovellusten käyttöönottoa
4. **Arvioi resurssivaatimukset**: Määritä muistin ja laskentatehon tarpeet kohdelaitteille

### Vaihe 2: Mallien optimointi
1. **Muunna ONNX-muotoon**: Muunna valitut mallit ONNX-muotoon reunayhteensopivuutta varten
2. **Sovella kvantisointia**: Pienennä mallien kokoa INT8- tai INT4-kvantisoinnilla
3. **Laitteisto-optimointi**: Optimoi kohdelaitteiden laitteistoille (ARM, x86, erikoiskiihdyttimet)
4. **Suorituskyvyn validointi**: Varmista, että optimoidut mallit säilyttävät hyväksyttävän tarkkuuden

### Vaihe 3: Sovelluskehitys
1. **Agenttien suunnittelu**: Käytä Agent Builderia luodaksesi reunasovelluksiin optimoituja tekoälyagentteja
2. **Prompt Engineering**: Kehitä kehotteita, jotka toimivat tehokkaasti pienempien mallien kanssa
3. **Integraatiotestaus**: Testaa agentteja simuloiduissa reunaympäristöissä
4. **Koodin generointi**: Luo tuotantokoodi, joka on optimoitu reunasovelluksia varten

### Vaihe 4: Arviointi ja testaus
1. **Eräarviointi**: Testaa useita konfiguraatioita löytääksesi optimaaliset reunasäädöt
2. **Suorituskyvyn profilointi**: Analysoi päättelynopeutta, muistin käyttöä ja tarkkuutta
3. **Reunasimulaatio**: Testaa olosuhteissa, jotka vastaavat kohdelaitteiden ympäristöä
4. **Rasitustestaus**: Arvioi suorituskykyä erilaisissa kuormitustilanteissa

### Vaihe 5: Käyttöönoton valmistelu
1. **Lopullinen optimointi**: Tee lopulliset optimoinnit testitulosten perusteella
2. **Käyttöönottopaketointi**: Pakkaa mallit ja koodi reunasovellusten käyttöönottoa varten
3. **Dokumentointi**: Dokumentoi käyttöönoton vaatimukset ja konfiguraatio
4. **Seurannan asennus**: Valmistele seuranta ja lokitus tuotantokäyttöä varten

## Kohdeyleisö Edge AI -kehityksessä

### Edge AI -kehittäjät
- Sovelluskehittäjät, jotka rakentavat tekoälypohjaisia reunalaitteita ja IoT-ratkaisuja
- Sulautettujen järjestelmien kehittäjät, jotka integroivat tekoälyominaisuuksia resurssirajoitteisiin laitteisiin
- Mobiilikehittäjät, jotka luovat laitepohjaisia tekoälysovelluksia älypuhelimille ja tableteille

### Edge AI -insinöörit
- Tekoälyinsinöörit, jotka optimoivat malleja reunasovelluksiin ja hallitsevat päättelyputkistoja
- DevOps-insinöörit, jotka ottavat käyttöön ja hallitsevat tekoälymalleja hajautetussa reunainfrastruktuurissa
- Suorituskykyinsinöörit, jotka optimoivat tekoälytyökuormia reunalaitteiden laitteistorajoituksia varten

### Tutkijat ja kouluttajat
- Tekoälytutkijat, jotka kehittävät tehokkaita malleja ja algoritmeja reunalaskentaan
- Kouluttajat, jotka opettavat Edge AI -käsitteitä ja esittelevät optimointitekniikoita
- Opiskelijat, jotka oppivat Edge AI -käyttöönoton haasteista ja ratkaisuista

## Edge AI -käyttötapaukset

### Älykkäät IoT-laitteet
- **Reaaliaikainen kuvantunnistus**: Ota käyttöön tietokonenäkömalleja IoT-kameroissa ja -antureissa
- **Puheenkäsittely**: Toteuta puheentunnistus ja luonnollisen kielen käsittely älykaiuttimissa
- **Ennakoiva kunnossapito**: Suorita poikkeavuuksien tunnistusmalleja teollisuuden reunalaitteilla
- **Ympäristön seuranta**: Ota käyttöön anturidatan analyysimalleja ympäristösovelluksiin

### Mobiili- ja sulautetut sovellukset
- **Laitepohjainen käännös**: Toteuta kieltenkäännösmalleja, jotka toimivat offline-tilassa
- **Lisätty todellisuus**: Ota käyttöön reaaliaikainen objektien tunnistus ja seuranta AR-sovelluksissa
- **Terveydenseuranta**: Suorita terveysanalyysimalleja puettavissa laitteissa ja lääketieteellisissä laitteissa
- **Autonomiset järjestelmät**: Toteuta päätöksentekomalleja droneille, roboteille ja ajoneuvoille

### Reunalaskentainfrastruktuuri
- **Reunadatakeskukset**: Ota käyttöön tekoälymalleja reunadatakeskuksissa matalan viiveen sovelluksia varten
- **CDN-integraatio**: Integroi tekoälyn käsittelyominaisuudet sisällönjakeluverkkoihin
- **5G-reuna**: Hyödynnä 5G-reunalaskentaa tekoälypohjaisiin sovelluksiin
- **Sumulaskenta**: Toteuta tekoälyn käsittelyä sumulaskentaympäristöissä

## Asennus ja käyttöönotto

### Nopea asennus
Asenna AI Toolkit -laajennus suoraan Visual Studio Code Marketplacesta:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Esivaatimukset Edge AI -kehitykseen
- **ONNX Runtime**: Asenna ONNX Runtime mallien päättelyä varten
- **Ollama** (valinnainen): Asenna Ollama paikallista mallipalvelua varten
- **Python-ympäristö**: Määritä Python tarvittavilla tekoälykirj
- **Turvallisuus**: Toteuta asianmukaiset turvallisuustoimenpiteet reunalaskennan tekoälysovelluksille

## Integraatio reunalaskennan tekoälykehyksiin

### ONNX Runtime
- **Monialustainen käyttöönotto**: Ota ONNX-mallit käyttöön eri reunalaskenta-alustoilla
- **Laitteistojen optimointi**: Hyödynnä ONNX Runtime -ohjelmiston laitteistokohtaisia optimointeja
- **Mobiilituki**: Käytä ONNX Runtime Mobile -versiota älypuhelin- ja tablettisovelluksissa
- **IoT-integraatio**: Ota käyttöön IoT-laitteilla ONNX Runtime -ohjelmiston kevyitä jakeluversioita

### Windows ML
- **Windows-laitteet**: Optimoi Windows-pohjaisille reunalaitteille ja tietokoneille
- **NPU-kiihdytys**: Hyödynnä Windows-laitteiden neuroprosessointiyksiköitä
- **DirectML**: Käytä DirectML:ää GPU-kiihdytykseen Windows-alustoilla
- **UWP-integraatio**: Integroi Universal Windows Platform -sovelluksiin

### TensorFlow Lite
- **Mobiilioptimointi**: Ota TensorFlow Lite -mallit käyttöön mobiili- ja sulautetuilla laitteilla
- **Laitteistodelegaatit**: Käytä erikoistuneita laitteistodelegaatteja kiihdytykseen
- **Mikrokontrollerit**: Ota käyttöön mikrokontrollereilla TensorFlow Lite Micro -versio
- **Monialustainen tuki**: Ota käyttöön Android-, iOS- ja sulautetuilla Linux-järjestelmillä

### Azure IoT Edge
- **Pilvi-reuna-hybridi**: Yhdistä pilvikoulutus reunalaskennan inferenssiin
- **Moduulien käyttöönotto**: Ota tekoälymallit käyttöön IoT Edge -moduuleina
- **Laitteiden hallinta**: Hallitse reunalaitteita ja mallipäivityksiä etänä
- **Telemetria**: Kerää suorituskykytietoja ja mallimittareita reunalaskennan käyttöönotosta

## Kehittyneet reunalaskennan tekoälytilanteet

### Monimallin käyttöönotto
- **Mallien yhdistelmät**: Ota käyttöön useita malleja tarkkuuden parantamiseksi tai redundanssin lisäämiseksi
- **A/B-testaus**: Testaa eri malleja samanaikaisesti reunalaitteilla
- **Dynaaminen valinta**: Valitse mallit laitteen nykytilan perusteella
- **Resurssien jakaminen**: Optimoi resurssien käyttö useiden mallien välillä

### Federatiivinen oppiminen
- **Hajautettu koulutus**: Kouluta malleja useilla reunalaitteilla
- **Tietosuojan säilyttäminen**: Pidä koulutusdata paikallisena ja jaa vain malliparannuksia
- **Yhteisöllinen oppiminen**: Mahdollista laitteiden oppiminen yhteisistä kokemuksista
- **Reuna-pilvi-yhteistyö**: Koordinoi oppimista reunalaitteiden ja pilvi-infrastruktuurin välillä

### Reaaliaikainen käsittely
- **Virtauskäsittely**: Käsittele jatkuvia datavirtoja reunalaitteilla
- **Matala viive**: Optimoi inferenssi mahdollisimman pienelle viiveelle
- **Eräkäsittely**: Käsittele tehokkaasti datan erämuotoja reunalaitteilla
- **Mukautuva käsittely**: Säädä käsittelyä laitteen nykyisten kyvykkyyksien mukaan

## Reunalaskennan tekoälyn kehityksen vianmääritys

### Yleiset ongelmat
- **Muistirajoitukset**: Malli liian suuri kohdelaitteen muistiin
- **Inferenssin nopeus**: Mallin inferenssi liian hidas reaaliaikaisiin vaatimuksiin
- **Tarkkuuden heikkeneminen**: Optimointi heikentää mallin tarkkuutta liikaa
- **Laitteistoyhteensopivuus**: Malli ei ole yhteensopiva kohdelaitteen kanssa

### Vianmääritysstrategiat
- **Suorituskyvyn profilointi**: Käytä AI Toolkitin jäljitysominaisuuksia pullonkaulojen tunnistamiseen
- **Resurssien seuranta**: Seuraa muistin ja suorittimen käyttöä kehityksen aikana
- **Inkrementaalinen testaus**: Testaa optimointeja vaiheittain ongelmien eristämiseksi
- **Laitteistosimulaatio**: Käytä kehitystyökaluja kohdelaitteiston simulointiin

### Optimointiratkaisut
- **Lisäkvantisointi**: Käytä aggressiivisempia kvantisointitekniikoita
- **Mallin arkkitehtuuri**: Harkitse erilaisia reunalaskentaan optimoituja mallin arkkitehtuureja
- **Esikäsittelyn optimointi**: Optimoi datan esikäsittely reunalaskennan rajoituksiin
- **Inferenssin optimointi**: Käytä laitteistokohtaisia inferenssin optimointeja

## Resurssit ja seuraavat askeleet

### Dokumentaatio
- [AI Toolkit Models Guide](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Documentation](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)

### Yhteisö ja tuki
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Community](https://github.com/onnx/onnx)
- [Edge AI Developer Community](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Oppimisresurssit
- [Reunalaskennan tekoälyn perusteet -kurssi](./Module01/README.md)
- [Pienten kielimallien opas](./Module02/README.md)
- [Reunalaskennan käyttöönoton strategiat](./Module03/README.md)
- [Windows-reunalaskennan tekoälyn kehitys](./windowdeveloper.md)

## Yhteenveto

Visual Studio Code -ohjelmiston AI Toolkit tarjoaa kattavan alustan reunalaskennan tekoälyn kehitykseen, mallien löytämisestä ja optimoinnista käyttöönottoon ja seurantaan. Hyödyntämällä sen integroituja työkaluja ja työnkulkuja kehittäjät voivat tehokkaasti luoda, testata ja ottaa käyttöön tekoälysovelluksia, jotka toimivat hyvin resurssirajoitteisilla reunalaitteilla.

Työkalupakin tuki ONNX:lle, Ollamalle ja eri pilvipalveluntarjoajille, yhdistettynä sen optimointi- ja arviointikykyihin, tekee siitä ihanteellisen valinnan reunalaskennan tekoälyn kehitykseen. Olipa kyseessä IoT-sovellukset, mobiilit tekoälyominaisuudet tai sulautetut älyjärjestelmät, AI Toolkit tarjoaa tarvittavat työkalut ja työnkulut onnistuneeseen reunalaskennan tekoälyn käyttöönottoon.

Kun reunalaskennan tekoäly kehittyy edelleen, Visual Studio Code -ohjelmiston AI Toolkit pysyy eturintamassa, tarjoten kehittäjille huippuluokan työkaluja ja ominaisuuksia seuraavan sukupolven älykkäiden reunasovellusten rakentamiseen.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.