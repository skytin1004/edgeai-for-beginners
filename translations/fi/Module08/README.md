<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T20:20:16+00:00",
  "source_file": "Module08/README.md",
  "language_code": "fi"
}
-->
# Moduuli 08: Käytännön harjoituksia Microsoft Foundry Localilla - Täydellinen kehittäjätyökalupakki

## Yleiskatsaus

Microsoft Foundry Local edustaa seuraavan sukupolven reunalaskennan tekoälykehitystä, tarjoten kehittäjille tehokkaita työkaluja tekoälysovellusten rakentamiseen, käyttöönottoon ja skaalaamiseen paikallisesti samalla säilyttäen saumattoman integraation Azure AI Foundryn kanssa. Tämä moduuli kattaa Foundry Localin perusteellisesti asennuksesta edistyneeseen agenttikehitykseen.

**Keskeiset teknologiat:**
- Microsoft Foundry Local CLI ja SDK
- Azure AI Foundry -integraatio
- Mallien paikallinen päättely
- Mallien paikallinen välimuisti ja optimointi
- Agenttipohjaiset arkkitehtuurit

## Moduulin oppimistavoitteet

Tämän moduulin suorittamalla opit:

- **Foundry Localin hallinta**: Asenna, konfiguroi ja optimoi Foundry Local Windows 11 -kehitystä varten
- **Erilaisten mallien käyttöönotto**: Suorita phi-, qwen-, deepseek- ja GPT-OSS-20B-malleja paikallisesti CLI-komentojen avulla
- **Tuotantoratkaisujen rakentaminen**: Luo tekoälysovelluksia edistyneellä kehotussuunnittelulla ja dataintegraatiolla
- **Avoimen lähdekoodin ekosysteemin hyödyntäminen**: Integroi Hugging Face -malleja ja yhteisön lisäyksiä
- **Tekoälyarkkitehtuurien vertailu**: Ymmärrä LLM- ja SLM-mallien kompromissit ja käyttöönoton strategiat
- **Tekoälyagenttien kehittäminen**: Rakenna älykkäitä agentteja Foundry Localin arkkitehtuurin ja pohjustustekniikoiden avulla
- **Mallien työkalukäyttö**: Luo modulaarisia, räätälöitäviä tekoälyratkaisuja yrityssovelluksiin

## Istunnon rakenne

### [1: Foundry Localin käyttöönotto](./01.FoundryLocalSetup.md)
**Painopiste**: Asennus, CLI-asetukset, mallien välimuisti ja laitteistokiihdytys

**Mitä opit:**
- Foundry Localin täydellinen asennus Windows 11:lle
- CLI-konfiguraatio ja komentorakenne
- Mallien välimuististrategiat optimaalisen suorituskyvyn saavuttamiseksi
- Laitteistokiihdytyksen asennus ja optimointi
- Käytännön harjoituksia phi-, qwen-, deepseek- ja GPT-OSS-20B-mallien käyttöönotossa

**Kesto**: 2-3 tuntia  
**Edellytykset**: Windows 11, perustiedot komentorivistä

---

### [2: Tekoälyratkaisujen rakentaminen Azure AI Foundrylla](./02.AzureAIFoundryIntegration.md)
**Painopiste**: Edistynyt kehotussuunnittelu, dataintegraatio ja käytännön tehtävät

**Mitä opit:**
- Kehotussuunnittelun edistyneet tekniikat
- Dataintegraatiomallit ja parhaat käytännöt
- Käytännön tekoälytehtävien rakentaminen Foundry Localilla
- Saumattomat Azure AI Foundry -integraatiotyönkulut
- Suorituskyvyn optimointi ja seuranta

**Kesto**: 2-3 tuntia  
**Edellytykset**: Istunto 1 suoritettu, Azure-tili (valinnainen)

---

### [3: Avoimen lähdekoodin mallit Foundry Localilla](./03.OpenSourceModels.md)
**Painopiste**: Hugging Face -integraatio, mallivalintastrategiat ja yhteisön lisäykset

**Mitä opit:**
- Hugging Face -mallien integrointi Foundry Localiin
- Omat mallit (BYOM) -strategiat ja toteutus
- Model Mondays -sarjan oivallukset ja yhteisön panokset
- Räätälöityjen mallien käyttöönotto ja optimointi
- Yhteisön mallien arviointi ja valintakriteerit

**Kesto**: 2-3 tuntia  
**Edellytykset**: Istuntojen 1-2 suorittaminen, Hugging Face -tili

---

### [4: Huippumallien tutkiminen - LLM:t, SLM:t ja paikallinen päättely](./04.CuttingEdgeModels.md)
**Painopiste**: Mallien vertailu, EdgeAI Phi- ja ONNX Runtime -ratkaisuilla, edistyneet demot

**Mitä opit:**
- LLM- ja SLM-mallien kattava vertailu ja käyttötapaukset
- Paikallisen ja pilvipäättelyn kompromissit ja päätöksentekokehykset
- EdgeAI-toteutus Phi- ja ONNX Runtime -ratkaisuilla
- Chainlit RAG Chat -sovelluksen kehitys ja käyttöönotto
- WebGPU-päättelyn optimointitekniikat
- AI PC SDK -integraatio ja ominaisuudet

**Kesto**: 3-4 tuntia  
**Edellytykset**: Istuntojen 1-3 suorittaminen, päättelykonseptien ymmärtäminen

---

### [5: Tekoälyagenttien nopea rakentaminen Foundry Localilla](./05.AIPoweredAgents.md)
**Painopiste**: Nopean GenAI-sovelluskehityksen, järjestelmäkehotusten, pohjustuksen ja agenttiarkkitehtuurien suunnittelu

**Mitä opit:**
- Foundry Localin agenttiarkkitehtuuri ja suunnittelumallit
- Järjestelmäkehotusten suunnittelu agenttien käyttäytymiseen
- Pohjustustekniikat luotettavien agenttivastausten saavuttamiseksi
- Nopean GenAI-sovelluskehityksen työnkulut
- Agenttien orkestrointi ja monen agentin järjestelmät
- Tuotantokäyttöönottostrategiat tekoälyagenteille

**Kesto**: 3-4 tuntia  
**Edellytykset**: Istuntojen 1-4 suorittaminen, perustiedot tekoälyagenteista

---

### [6: Foundry Local - Mallit työkaluina](./06.ModelsAsTools.md)
**Painopiste**: Modulaariset tekoälyratkaisut, paikallinen käyttöönotto ja yritysskaalaus

**Mitä opit:**
- Tekoälymallien käsittely modulaarisina, räätälöitävinä työkaluina
- Paikallinen käyttöönotto ilman pilviriippuvuutta
- Matala viive, kustannustehokas ja yksityisyyttä säilyttävä päättely
- SDK-, API- ja CLI-integraatiomallit
- Mallien räätälöinti tiettyihin käyttötapauksiin
- Skaalausstrategiat paikallisesta Azure AI Foundryyn
- Yritysvalmiit tekoälysovellusarkkitehtuurit

**Kesto**: 3-4 tuntia  
**Edellytykset**: Kaikki aiemmat istunnot, yrityskehityskokemus hyödyllinen

## Edellytykset

### Järjestelmävaatimukset
- **Käyttöjärjestelmä**: Windows 11 (22H2 tai uudempi)
- **Muisti**: 16GB RAM (32GB suositeltu suuremmille malleille)
- **Tallennustila**: 50GB vapaata tilaa mallien välimuistille
- **Laitteisto**: NPU-tuettu laite suositeltu (Copilot+ PC), GPU valinnainen
- **Verkko**: Nopea internetyhteys mallien alkuperäistä latausta varten

### Kehitysympäristö
- Visual Studio Code AI Toolkit -laajennuksella
- Python 3.10+ ja pip
- Git versionhallintaan
- PowerShell tai komentokehote
- Azure CLI (valinnainen pilvi-integraatiota varten)

### Tietovaatimukset
- Perustiedot tekoäly-/koneoppimiskonsepteista
- Komentorivin peruskäyttö
- Python-ohjelmoinnin perusteet
- REST API -konseptit
- Perustiedot kehotuksista ja mallien päättelystä

## Moduulin aikataulu

**Arvioitu kokonaisaika**: 15-20 tuntia

| Istunto | Painopistealue | Aika | Vaikeustaso |
|---------|----------------|------|-------------|
|  1 | Asennus ja perusteet | 2-3 tuntia | Aloittelija |
|  2 | Tekoälyratkaisut | 2-3 tuntia | Keskitaso |
|  3 | Avoin lähdekoodi | 2-3 tuntia | Keskitaso |
|  4 | Edistyneet mallit | 3-4 tuntia | Edistynyt |
|  5 | Tekoälyagentit | 3-4 tuntia | Edistynyt |
|  6 | Yritystyökalut | 3-4 tuntia | Asiantuntija |

## Keskeiset resurssit

### Päädokumentaatio
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentaatio](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays -sarja](https://aka.ms/model-mondays)

### Yhteisöresurssit
- [Foundry Local -yhteisökeskustelut](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry -esimerkit](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Oppimistulokset

Moduulin suorittamisen jälkeen sinulla on valmiudet:

### Tekninen osaaminen
- **Käyttöönotto ja hallinta**: Foundry Local -asennukset kehitys- ja tuotantoympäristöissä
- **Mallien integrointi**: Työskentely monipuolisten malliperheiden kanssa Microsoftilta, Hugging Facelta ja yhteisöltä
- **Sovellusten rakentaminen**: Tuotantovalmiiden tekoälysovellusten luominen edistyneillä ominaisuuksilla ja optimoinneilla
- **Agenttien kehittäminen**: Kehittyneiden tekoälyagenttien toteutus pohjustuksella, päättelyllä ja työkalujen integroinnilla

### Strateginen ymmärrys
- **Arkkitehtuuripäätökset**: Tietoiset valinnat paikallisen ja pilvikäyttöönoton välillä
- **Suorituskyvyn optimointi**: Päättelyn optimointi eri laitteistokonfiguraatioissa
- **Yritysskaalaus**: Sovellusten suunnittelu, jotka skaalautuvat paikallisista prototyypeistä yrityskäyttöön
- **Yksityisyys ja turvallisuus**: Yksityisyyttä säilyttävien tekoälyratkaisujen toteutus paikallisella päättelyllä

### Innovointikyvyt
- **Nopea prototyyppaus**: Tekoälysovelluskonseptien nopea rakentaminen ja testaus
- **Yhteisöintegraatio**: Avoimen lähdekoodin mallien hyödyntäminen ja ekosysteemiin osallistuminen
- **Edistyneet mallit**: Huippuluokan tekoälymallien, kuten RAG, agenttien ja työkalujen integroinnin toteutus
- **Tulevaisuuteen valmis kehitys**: Sovellusten rakentaminen, jotka ovat valmiita kehittyville tekoälyteknologioille ja -malleille

## Aloittaminen

1. **Valmista ympäristösi**: Varmista Windows 11 ja suositellut laitteistovaatimukset
2. **Asenna edellytykset**: Asenna kehitystyökalut ja riippuvuudet
3. **Aloita istunnosta 1**: Aloita Foundry Localin asennuksella ja perusasetuksilla
4. **Etene järjestyksessä**: Suorita istunnot järjestyksessä optimaalisen oppimisen varmistamiseksi
5. **Harjoittele jatkuvasti**: Sovella käsitteitä käytännön harjoituksissa ja projekteissa

## Menestysmittarit

Seuraa edistymistäsi moduulin aikana:

- [ ] Foundry Localin onnistunut asennus ja konfigurointi
- [ ] Vähintään 4 eri malliperheen käyttöönotto ja suoritus
- [ ] Täydellisen tekoälyratkaisun rakentaminen dataintegraatiolla
- [ ] Vähintään 2 avoimen lähdekoodin mallin integrointi
- [ ] Toimivan RAG-chat-sovelluksen luominen
- [ ] Tekoälyagentin kehittäminen ja käyttöönotto
- [ ] Mallit työkaluina -arkkitehtuurin toteutus

## Nopea aloitus esimerkeille

### 1) Ympäristön asennus (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Paikallisen mallin käynnistäminen (uusi terminaali)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Chainlit-demon suorittaminen (Istunto 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Monen agentin koordinaattorin suorittaminen (Istunto 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Jos näet yhteysvirheitä, validoi Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Reitittimen konfigurointi (Istunto 6)
Reititin suorittaa nopean kuntotarkistuksen ja tukee ympäristöön perustuvaa konfiguraatiota:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Tämä moduuli edustaa reunalaskennan tekoälykehityksen huippua, yhdistäen Microsoftin yritystason työkalut avoimen lähdekoodin ekosysteemin joustavuuteen ja innovaatioon. Hallitsemalla Foundry Localin, olet tekoälysovelluskehityksen eturintamassa.

Azure OpenAI (Istunto 2) -osiossa katso esimerkin README tarvittavia ympäristömuuttujia ja API-versioasetuksia varten.

## Esimerkkien yleiskatsaus

- `samples/01`: Nopea REST-chat Foundry Localille (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK -integraatio (`sdk_quickstart.py`).
- `samples/03`: Mallien etsintä + nopea vertailu (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG -demo (`app.py`).
- `samples/05`: Monen agentin orkestrointi (`python -m samples.05.agents.coordinator`).
- `samples/06`: Mallit työkaluina -reititin (`python samples\06\router.py`).

---

