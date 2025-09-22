<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c2dacb560380677a2c923171d3e423d",
  "translation_date": "2025-09-22T20:17:46+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "fi"
}
-->
# Windows Edge AI -kehitysopas

## Johdanto

Tervetuloa Windows Edge AI -kehityksen pariin – kattavaan oppaaseen, joka auttaa sinua rakentamaan älykkäitä sovelluksia hyödyntäen Microsoftin Windows AI Foundry -alustaa. Tämä opas on suunniteltu erityisesti Windows-kehittäjille, jotka haluavat integroida huippuluokan Edge AI -ominaisuuksia sovelluksiinsa ja hyödyntää Windows-laitteiston kiihdytyksen täyttä potentiaalia.

### Windows AI:n edut

Windows AI Foundry tarjoaa yhtenäisen, luotettavan ja turvallisen alustan, joka tukee koko AI-kehittäjän elinkaarta – mallin valinnasta ja hienosäädöstä optimointiin ja käyttöönottoon CPU-, GPU-, NPU- ja hybridipilviarkkitehtuureissa. Tämä alusta demokratisoi AI-kehityksen tarjoamalla:

- **Laitteistoabstraktio**: Saumaton käyttöönotto AMD-, Intel-, NVIDIA- ja Qualcomm-piirisarjoilla
- **Paikallinen älykkyys**: Tietosuojaa kunnioittava AI, joka toimii täysin paikallisella laitteistolla
- **Optimoitu suorituskyky**: Windows-laitteistolle valmiiksi optimoidut mallit
- **Yrityskäyttövalmius**: Tuotantotason turvallisuus- ja vaatimustenmukaisuusominaisuudet

### Miksi Windows Edge AI:lle?

**Universaali laitteistotuki**  
Windows ML optimoi automaattisesti laitteistokäytön koko Windows-ekosysteemissä, varmistaen AI-sovellusten optimaalisen suorituskyvyn riippumatta taustalla olevasta piirisarjasta.

**Integroitu AI-ajonaika**  
Sisäänrakennettu Windows ML -tulkintamoottori poistaa monimutkaiset asennusvaatimukset, jolloin kehittäjät voivat keskittyä sovelluslogiikkaan infrastruktuurin sijaan.

**Copilot+ PC -optimointi**  
Tarkoitukseen suunnitellut API:t, jotka on kehitetty erityisesti seuraavan sukupolven Windows-laitteille, joissa on omistettuja Neural Processing Unit (NPU) -yksiköitä, tarjoavat poikkeuksellisen suorituskyvyn per watt.

**Kehittäjäekosysteemi**  
Rikkaat työkalut, kuten Visual Studio -integraatio, kattava dokumentaatio ja esimerkkisovellukset, jotka nopeuttavat kehityssyklejä.

## Oppimistavoitteet

Tämän Windows Edge AI -kehitysoppaan suorittamalla opit olennaiset taidot tuotantovalmiiden AI-sovellusten rakentamiseen Windows-alustalla.

### Keskeiset tekniset osaamisalueet

**Windows AI Foundry -osaaminen**  
- Ymmärrä Windows AI Foundry -alustan arkkitehtuuri ja komponentit  
- Navigoi AI-kehityksen koko elinkaari Windows-ekosysteemissä  
- Toteuta turvallisuusparhaita käytäntöjä paikallisille AI-sovelluksille  
- Optimoi sovellukset eri Windows-laitteistokonfiguraatioille  

**API-integraatioasiantuntemus**  
- Hallitse Windows AI API:t tekstin, kuvan ja multimodaalisten sovellusten osalta  
- Toteuta Phi Silica -kielimallin integrointi tekstin generointiin ja päättelyyn  
- Käytä sisäänrakennettuja kuvankäsittely-API:ita tietokonenäköominaisuuksien käyttöönottoon  
- Mukauta esikoulutettuja malleja LoRA (Low-Rank Adaptation) -tekniikoilla  

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
- Käsittele asynkronisia AI-toimintoja oikeilla käyttäjäkokemusmalleilla  

**Suorituskyvyn optimointi**  
- Profiiloi ja optimoi AI-tulkinnan suorituskyky eri laitteistokonfiguraatioissa  
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

## Windows AI Foundry -alustan komponentit

### 1. Windows AI API:t

Windows AI API:t tarjoavat käyttövalmiita AI-ominaisuuksia, jotka perustuvat paikallisiin malleihin ja ovat optimoitu tehokkuuden ja suorituskyvyn osalta Copilot+ PC -laitteilla, vaatimatta monimutkaista asennusta.

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
- **Kuvauksen generointi**: Luo yksityiskohtaisia tekstikuvauksia visuaalisesta sisällöstä  
- **Kohteen poisto**: Poista ei-toivotut kohteet kuvista AI-pohjaisella täydennyksellä  

**Multimodaaliset ominaisuudet**  
- **Näkö- ja kieliyhdistelmät**: Yhdistä tekstin ja kuvan ymmärrys  
- **Semanttinen haku**: Mahdollista luonnollisen kielen kyselyt multimediasisällössä  
- **Tiedonhaku**: Rakenna älykkäitä hakukokemuksia paikallisella datalla  

### 2. Foundry Local

Foundry Local tarjoaa kehittäjille nopean pääsyn käyttövalmiisiin avoimen lähdekoodin kielimalleihin Windows-piirisarjoilla, mahdollistaen mallien selaamisen, testaamisen, vuorovaikutuksen ja käyttöönoton paikallisissa sovelluksissa.

#### Keskeiset ominaisuudet

**Mallikatalogi**  
- Laaja kokoelma valmiiksi optimoituja avoimen lähdekoodin malleja  
- Mallit optimoitu CPU-, GPU- ja NPU-käyttöön välittömään käyttöönottoon  
- Tuki suosituimmille malliperheille, kuten Llama, Mistral, Phi ja erikoistuneet alakohtaiset mallit  

**CLI-integraatio**  
- Komentoriviliittymä mallien hallintaan ja käyttöönottoon  
- Automatisoidut optimointi- ja kvantisointityönkulut  
- Integrointi suosittuihin kehitysympäristöihin ja CI/CD-putkistoihin  

**Paikallinen käyttöönotto**  
- Täysin offline-toiminta ilman pilviriippuvuuksia  
- Tuki mukautetuille malliformaateille ja konfiguraatioille  
- Tehokas mallipalvelu automaattisella laitteisto-optimoinnilla  

### 3. Windows ML

Windows ML toimii Windowsin keskeisenä AI-alustana ja integroituna tulkintaympäristönä, mahdollistaen mukautettujen mallien tehokkaan käyttöönoton laajassa Windows-laitteistokentässä.

#### Arkkitehtuurin edut

**Universaali laitteistotuki**  
- Automaattinen optimointi AMD-, Intel-, NVIDIA- ja Qualcomm-piirisarjoille  
- Tuki CPU-, GPU- ja NPU-suoritukselle läpinäkyvällä vaihtamisella  
- Laitteistoabstraktio, joka poistaa alustakohtaisen optimointityön  

**Mallin joustavuus**  
- Tuki ONNX-malliformaatille automaattisella konversiolla suosituista kehyksistä  
- Mukautettujen mallien käyttöönotto tuotantotason suorituskyvyllä  
- Integrointi olemassa oleviin Windows-sovellusarkkitehtuureihin  

**Yritysintegraatio**  
- Yhteensopivuus Windowsin turvallisuus- ja vaatimustenmukaisuuskehysten kanssa  
- Tuki yrityskäyttöönotolle ja hallintatyökaluille  
- Integrointi Windows-laitteiden hallinta- ja seurantajärjestelmiin  

## Kehitystyönkulku

### Vaihe 1: Ympäristön asennus ja työkalujen konfigurointi

**Kehitysympäristön valmistelu**  
1. Asenna Visual Studio AI Toolkit -laajennuksella  
2. Konfiguroi Windows AI Foundry CLI -työkalut  
3. Aseta paikallinen mallien testausympäristö  
4. Ota käyttöön suorituskyvyn profilointi- ja seurantatyökalut  

**AI Dev Gallery -tutkimus**  
- Tutki esimerkkisovelluksia ja viiteimplementaatioita  
- Testaa Windows AI API:t interaktiivisilla demonstraatioilla  
- Tarkista lähdekoodi parhaiden käytäntöjen ja mallien osalta  
- Tunnista sovelluksellesi relevantit esimerkit  

### Vaihe 2: Mallin valinta ja integrointi

**Vaatimusten analyysi**  
- Määrittele AI-ominaisuuksien toiminnalliset vaatimukset  
- Aseta suorituskyvyn rajoitukset ja optimointitavoitteet  
- Arvioi yksityisyyden ja turvallisuuden vaatimukset  
- Suunnittele käyttöönottoarkkitehtuuri ja skaalautumisstrategiat  

**Mallin arviointi**  
- Käytä Foundry Localia testataksesi avoimen lähdekoodin malleja käyttötapauksessasi  
- Vertaa Windows AI API:ita mukautettujen mallivaatimusten kanssa  
- Arvioi kompromisseja mallin koon, tarkkuuden ja tulkintanopeuden välillä  
- Prototyyppaa integrointitapoja valituilla malleilla  

### Vaihe 3: Sovelluskehitys

**Ydinintegraatio**  
- Toteuta Windows AI API -integraatio oikealla virheenkäsittelyllä  
- Suunnittele käyttöliittymät, jotka mukautuvat AI-prosessointityönkulkuihin  
- Toteuta välimuisti- ja optimointistrategiat mallin tulkinnalle  
- Lisää telemetria ja seuranta AI-toimintojen suorituskyvylle  

**Testaus ja validointi**  
- Testaa sovelluksia eri Windows-laitteistokonfiguraatioilla  
- Vahvista suorituskykymittarit eri kuormitustilanteissa  
- Toteuta automatisoitu testaus AI-toimintojen luotettavuuden varmistamiseksi  
- Suorita käyttäjäkokemustestaus AI-tehostetuilla ominaisuuksilla  

### Vaihe 4: Optimointi ja käyttöönotto

**Suorituskyvyn optimointi**  
- Profiiloi sovelluksen suorituskyky kohdelaitteistokonfiguraatioissa  
- Optimoi muistinkäyttö ja mallien latausstrategiat  
- Toteuta mukautuva käyttäytyminen käytettävissä olevien laitteistoresurssien perusteella  
- Hienosäädä käyttäjäkokemus eri suorituskykyskenaarioille  

**Tuotantokäyttöönotto**  
- Pakkaa sovellukset oikeilla AI-malliriippuvuuksilla  
- Toteuta päivitysmekanismit malleille ja sovelluslogiikalle  
- Konfiguroi seuranta ja analytiikka tuotantoympäristöille  
- Suunnittele käyttöönotto- ja jakelustrategiat yritys- ja kuluttajakäyttöön  

## Käytännön toteutusesimerkit

### Esimerkki 1: Älykäs asiakirjojen käsittelysovellus

Rakenna Windows-sovellus, joka käsittelee asiakirjoja useilla AI-ominaisuuksilla:

**Käytetyt teknologiat:**  
- Phi Silica asiakirjojen tiivistämiseen ja kysymyksiin vastaamiseen  
- OCR-API:t tekstin poimintaan skannatuista asiakirjoista  
- Kuvauksen generointi-API:t kaavioiden ja diagrammien analysointiin  
- Mukautetut ONNX-mallit asiakirjojen luokitteluun  

**Toteutustapa:**  
- Suunnittele modulaarinen arkkitehtuuri, jossa on liitettävät AI-komponentit  
- Toteuta asynkroninen käsittely suurille asiakirjaerille  
- Lisää etenemisen indikaattorit ja peruutustuki pitkäkestoisille toiminnoille  
- Sisällytä offline-ominaisuus arkaluontoisten asiakirjojen käsittelyyn  

### Esimerkki 2: Vähittäiskaupan varastonhallintajärjestelmä

Luo AI-tehostettu varastonhallintajärjestelmä vähittäiskaupan sovelluksiin:

**Käytetyt teknologiat:**  
- Kuvan segmentointi tuotteiden tunnistamiseen  
- Mukautetut näkömallit brändi- ja kategoriatunnistukseen  
- Foundry Local -käyttöönotto erikoistuneille vähittäiskaupan kielimalleille  
- Integrointi olemassa oleviin POS- ja varastojärjestelmiin  

**Toteutustapa:**  
- Rakenna kameraintegraatio reaaliaikaista tuotetunnistusta varten  
- Toteuta viivakoodin ja visuaalisen tuotetunnistuksen ominaisuudet  
- Lisää luonnollisen kielen varastokyselyt paikallisten kielimallien avulla  
- Suunnittele skaalautuva arkkitehtuuri monikauppakäyttöönottoa varten  

### Esimerkki 3: Terveydenhuollon dokumentointiassistentti

Kehitä tietosuojaa kunnioittava terveydenhuollon dokumentointityökalu:

**Käytetyt teknologiat:**  
- Phi Silica lääketieteellisten muistiinpanojen generointiin ja kliiniseen päätöksentukeen  
- OCR käsinkirjoitettujen lääketieteellisten asiakirjojen digitalisointiin  
- Mukautetut lääketieteelliset kielimallit, jotka otetaan käyttöön Windows ML:n kautta  
- Paikallinen vektorivarasto lääketieteellisen tiedonhakuun  

**Toteutustapa:**  
- Varmista täydellinen offline-toiminta potilastietojen yksityisyyden suojaamiseksi  
- Toteuta lää
- Hyödynnä Foundry Local CLI:tä mallien testaukseen ja validointiin  
- Käytä Windows AI API -testaustyökaluja integraation varmistamiseen  
- Toteuta mukautettu lokitus AI-toimintojen seurantaan  
- Luo automatisoitu testaus AI-toimintojen luotettavuuden varmistamiseksi  

## Sovellusten tulevaisuuden varmistaminen  

### Nousevat teknologiat  

**Seuraavan sukupolven laitteisto**  
- Suunnittele sovelluksia hyödyntämään tulevia NPU-ominaisuuksia  
- Varaudu kasvaviin mallikokoihin ja monimutkaisuuteen  
- Toteuta mukautuvia arkkitehtuureja kehittyvää laitteistoa varten  
- Harkitse kvanttiyhteensopivia algoritmeja tulevaisuuden tarpeisiin  

**Edistyneet AI-ominaisuudet**  
- Valmistaudu multimodaalisen AI:n integrointiin useampien datatyyppien kanssa  
- Suunnittele reaaliaikaista yhteistyötä tekevä AI useiden laitteiden välillä  
- Toteuta ratkaisuja hajautetun oppimisen mahdollistamiseksi  
- Harkitse edge-cloud-hybriditiedustelun arkkitehtuureja  

### Jatkuva oppiminen ja sopeutuminen  

**Mallipäivitykset**  
- Toteuta saumattomat mallipäivitysmekanismit  
- Suunnittele sovelluksia sopeutumaan parannettuihin mallikykyihin  
- Varaudu taaksepäin yhteensopivuuteen olemassa olevien mallien kanssa  
- Toteuta A/B-testaus mallien suorituskyvyn arviointiin  

**Ominaisuuksien kehitys**  
- Suunnittele modulaarisia arkkitehtuureja, jotka tukevat uusia AI-ominaisuuksia  
- Varaudu nousevien Windows AI API:en integrointiin  
- Toteuta ominaisuuslippuja asteittaista ominaisuuksien käyttöönottoa varten  
- Suunnittele käyttöliittymiä, jotka mukautuvat parannettuihin AI-ominaisuuksiin  

## Yhteenveto  

Windows Edge AI -kehitys edustaa tehokkaiden AI-ominaisuuksien yhdistymistä vankkaan, turvalliseen ja skaalautuvaan Windows-alustaan. Hallitsemalla Windows AI Foundry -ekosysteemin kehittäjät voivat luoda älykkäitä sovelluksia, jotka tarjoavat poikkeuksellisia käyttäjäkokemuksia samalla kun ne ylläpitävät korkeimpia yksityisyyden, turvallisuuden ja suorituskyvyn standardeja.  

Windows AI API:t, Foundry Local ja Windows ML tarjoavat vertaansa vailla olevan perustan seuraavan sukupolven älykkäiden Windows-sovellusten rakentamiseen. Kun AI kehittyy edelleen, Windows-alusta varmistaa, että sovelluksesi skaalautuvat nousevien teknologioiden mukana ja säilyttävät yhteensopivuuden ja suorituskyvyn monipuolisessa Windows-laitteistoympäristössä.  

Olitpa rakentamassa kuluttajasovelluksia, yritysratkaisuja tai erikoistuneita teollisuustyökaluja, Windows Edge AI -kehitys antaa sinulle mahdollisuuden luoda älykkäitä, reagoivia ja syvällisesti integroituneita kokemuksia, jotka hyödyntävät modernien Windows-laitteiden täyttä potentiaalia.  

## Lisäresurssit  

Windowsin Foundry Local -käyttöönoton (asennus, CLI, dynaaminen päätepiste, SDK:n käyttö) vaiheittainen opas löytyy täältä: [foundrylocal.md](./foundrylocal.md).  

### Dokumentaatio ja oppiminen  
- [Windows AI Foundry -dokumentaatio](https://learn.microsoft.com/windows/ai/)  
- [Windows AI API -viite](https://learn.microsoft.com/windows/ai/apis/)  
- [Foundry Local -aloitusopas](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)  
- [Windows ML -yleiskatsaus](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)  

### Kehitystyökalut  
- [AI Toolkit for Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)  
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)  
- [Windows AI -esimerkit](https://learn.microsoft.com/windows/ai/samples/)  

### Yhteisö ja tuki  
- [Windows Developer Community](https://developer.microsoft.com/en-us/windows/)  
- [Windows AI Foundry -blogi](https://blogs.windows.com/windowsdeveloper/)  
- [Microsoft Learn AI -koulutus](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)  

---  

*Tämä opas on suunniteltu kehittymään nopeasti etenevän Windows AI -ekosysteemin mukana. Säännölliset päivitykset varmistavat, että sisältö pysyy ajan tasalla uusimpien alustan ominaisuuksien ja kehityskäytäntöjen kanssa.*  

---

