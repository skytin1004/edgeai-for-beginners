<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-18T10:15:06+00:00",
  "source_file": "Module04/README.md",
  "language_code": "fi"
}
-->
# Luku 04: Mallimuotojen Muuntaminen ja Kvantisointi - Luvun Yleiskatsaus

EdgeAI:n nousu on tehnyt mallimuotojen muuntamisesta ja kvantisoinnista olennaisia teknologioita, kun kehittyneitä koneoppimiskykyjä otetaan käyttöön resurssirajoitteisilla laitteilla. Tämä kattava luku tarjoaa täydellisen oppaan mallien ymmärtämiseen, toteuttamiseen ja optimointiin reunalaskennan käyttöskenaarioita varten.

## 📚 Luvun Rakenne ja Oppimispolku

Tämä luku on jaettu kuuteen vaiheittaiseen osioon, jotka rakentuvat toistensa päälle tarjoten kokonaisvaltaisen ymmärryksen mallien optimoinnista reunalaskentaa varten:

---

## [Osio 1: Mallimuotojen Muuntamisen ja Kvantisoinnin Perusteet](./01.Introduce.md)

### 🎯 Yleiskatsaus
Tämä perusosio luo teoreettisen pohjan mallien optimoinnille reunalaskentaympäristöissä, kattaen kvantisoinnin tarkkuustasot 1-bitistä 8-bittiin sekä keskeiset muuntostrategiat.

**Keskeiset Aiheet:**
- Tarkkuusluokittelun viitekehys (erittäin matala, matala, keskitarkkuus)
- GGUF- ja ONNX-muotojen edut ja käyttötapaukset
- Kvantisoinnin hyödyt toiminnallisessa tehokkuudessa ja käyttöönoton joustavuudessa
- Suorituskykyvertailut ja muistijalanjäljen analyysit

**Oppimistavoitteet:**
- Ymmärtää kvantisoinnin rajat ja luokittelut
- Tunnistaa sopivat muuntotekniikat
- Oppia edistyneitä optimointistrategioita reunakäyttöön

---

## [Osio 2: Llama.cpp:n Toteutusopas](./02.Llamacpp.md)

### 🎯 Yleiskatsaus
Kattava opas Llama.cpp:n toteuttamiseen, tehokas C++-kehys, joka mahdollistaa suurten kielimallien suorittamisen vähäisellä asennuksella eri laitteistoalustoilla.

**Keskeiset Aiheet:**
- Asennus Windows-, macOS- ja Linux-alustoille
- GGUF-muodon muuntaminen ja eri kvantisointitasot (Q2_K–Q8_0)
- Laitteistokiihdytys CUDA:n, Metalin, OpenCL:n ja Vulkanin avulla
- Python-integraatio ja tuotantokäyttöstrategiat

**Oppimistavoitteet:**
- Hallita monialustainen asennus ja lähdekoodista rakentaminen
- Toteuttaa mallien kvantisointi ja optimointitekniikat
- Ottaa mallit käyttöön palvelintilassa REST API -integraatiolla

---

## [Osio 3: Microsoft Olive -optimointityökalu](./03.MicrosoftOlive.md)

### 🎯 Yleiskatsaus
Tutustuminen Microsoft Oliveen, laitteistotietoiseen mallien optimointityökaluun, jossa on yli 40 sisäänrakennettua optimointikomponenttia, suunniteltu yritystason mallien käyttöönottoon eri laitteistoalustoilla.

**Keskeiset Aiheet:**
- Automaattiset optimointiominaisuudet dynaamisella ja staattisella kvantisoinnilla
- Laitteistotietoinen älykkyys CPU-, GPU- ja NPU-käyttöönottoa varten
- Suosittujen mallien (Llama, Phi, Qwen, Gemma) tuki suoraan
- Yritysintegraatio Azure ML:n ja tuotantotyönkulkujen kanssa

**Oppimistavoitteet:**
- Hyödyntää automaattista optimointia eri mallirakenteille
- Toteuttaa monialustaisia käyttöönotto-strategioita
- Rakentaa yritysvalmiita optimointiputkia

---

## [Osio 4: OpenVINO Toolkit -optimointityökalu](./04.openvino.md)

### 🎯 Yleiskatsaus
Kattava katsaus Intelin OpenVINO-työkaluun, avoimen lähdekoodin alusta, joka mahdollistaa suorituskykyisten tekoälyratkaisujen käyttöönoton pilvessä, paikallisympäristöissä ja reunalaskennassa edistyneillä Neural Network Compression Framework (NNCF) -ominaisuuksilla.

**Keskeiset Aiheet:**
- Monialustainen käyttöönotto laitteistokiihdytyksellä (CPU, GPU, VPU, AI-kiihdyttimet)
- Neural Network Compression Framework (NNCF) edistyneeseen kvantisointiin ja karsintaan
- OpenVINO GenAI suurten kielimallien optimointiin ja käyttöönottoon
- Yritystason mallipalvelimen ominaisuudet ja skaalautuvat käyttöönotto-strategiat

**Oppimistavoitteet:**
- Hallita OpenVINO-mallien muunto- ja optimointityönkulut
- Toteuttaa edistyneitä kvantisointitekniikoita NNCF:n avulla
- Ottaa käyttöön optimoituja malleja eri laitteistoalustoilla Model Serverin avulla

---

## [Osio 5: Apple MLX Framework -syväluotaus](./05.AppleMLX.md)

### 🎯 Yleiskatsaus
Kattava katsaus Apple MLX:ään, vallankumoukselliseen kehykseen, joka on erityisesti suunniteltu tehokkaaseen koneoppimiseen Apple Siliconilla, painottaen suurten kielimallien kyvykkyyksiä ja paikallista käyttöönottoa.

**Keskeiset Aiheet:**
- Yhdistetyn muistirakenteen edut ja Metal Performance Shaders
- Tuki LLaMA-, Mistral-, Phi-3-, Qwen- ja Code Llama -malleille
- LoRA-hienosäätö tehokkaaseen mallien räätälöintiin
- Hugging Face -integraatio ja kvantisointituki (4-bittinen ja 8-bittinen)

**Oppimistavoitteet:**
- Hallita Apple Silicon -optimointi suurten kielimallien käyttöönottoa varten
- Toteuttaa hienosäätö- ja mallien räätälöintitekniikoita
- Rakentaa yritystason tekoälysovelluksia parannetuilla yksityisyysominaisuuksilla

---

## [Osio 6: Edge AI -kehitystyönkulun Synteesi](./06.workflow-synthesis.md)

### 🎯 Yleiskatsaus
Kaikkien optimointikehysten kattava synteesi yhtenäisiksi työnkuluiksi, päätösmatriiseiksi ja parhaiksi käytännöiksi tuotantovalmiiseen Edge AI -käyttöönottoon eri alustoilla ja käyttötapauksissa.

**Keskeiset Aiheet:**
- Yhtenäinen työnkulkuarkkitehtuuri, joka integroi useita optimointikehyksiä
- Kehyksen valintapuut ja suorituskykyyn liittyvien kompromissien analyysi
- Tuotantovalmiuden validointi ja kattavat käyttöönotto-strategiat
- Tulevaisuuden varmistaminen uusille laitteistoille ja mallirakenteille

**Oppimistavoitteet:**
- Hallita systemaattinen kehyksen valinta vaatimusten ja rajoitteiden perusteella
- Toteuttaa tuotantotason Edge AI -putkia kattavalla seurannalla
- Suunnitella mukautuvia työnkulkuja, jotka kehittyvät uusien teknologioiden ja vaatimusten mukana

---

## 🎯 Luvun Oppimistavoitteet

Tämän kattavan luvun suorittamisen jälkeen lukijat saavuttavat:

### **Tekninen Hallinta**
- Syvällinen ymmärrys kvantisoinnin rajoista ja käytännön sovelluksista
- Käytännön kokemus useista optimointikehyksistä
- Tuotantokäyttöön liittyvät taidot reunalaskentaympäristöissä

### **Strateginen Ymmärrys**
- Laitteistotietoisen optimoinnin valintakyvyt
- Tietoinen päätöksenteko suorituskykyyn liittyvistä kompromisseista
- Yritystason käyttöönotto- ja seurantastrategiat

### **Suorituskykyvertailut**

| Kehys      | Kvantisointi | Muistin Käyttö | Nopeuden Parannus | Käyttötapa             |
|------------|--------------|----------------|--------------------|------------------------|
| Llama.cpp  | Q4_K_M       | ~4GB           | 2-3x              | Monialustainen käyttö |
| Olive      | INT4         | 60-75% vähemmän| 2-6x              | Yritystyönkulut       |
| OpenVINO   | INT8/INT4    | 50-75% vähemmän| 2-5x              | Intel-laitteiston optimointi |
| MLX        | 4-bittinen   | ~4GB           | 2-4x              | Apple Silicon -optimointi |

## 🚀 Seuraavat Askeleet ja Edistyneet Sovellukset

Tämä luku tarjoaa vankan perustan:
- Räätälöityjen mallien kehittämiseen tiettyjä aloja varten
- Reunalaskennan optimointitutkimukseen
- Kaupallisten tekoälysovellusten kehittämiseen
- Suurten yritystason Edge AI -käyttöönottojen toteuttamiseen

Näiden kuuden osion tiedot tarjoavat kattavan työkalupakin nopeasti kehittyvän Edge AI -mallien optimoinnin ja käyttöönoton kentän hallintaan.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.