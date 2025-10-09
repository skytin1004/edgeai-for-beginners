<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T20:33:20+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sw"
}
-->
# Changelog

Mabadiliko yote muhimu kwa EdgeAI kwa Kompyuta yameandikwa hapa. Mradi huu hutumia maingizo ya tarehe na mtindo wa Keep a Changelog (Imeongezwa, Imebadilishwa, Imetatuliwa, Imeondolewa, Nyaraka, Imehama).

## 2025-10-08

### Imeongezwa - Sasisho Kamili la Warsha
- **Kuandikwa upya kwa README.md ya Warsha**:
  - Imeongezwa utangulizi wa kina unaoelezea thamani ya Edge AI (faragha, utendaji, gharama)
  - Malengo 6 ya msingi ya kujifunza yaliyo na ujuzi wa kina
  - Jedwali la matokeo ya kujifunza likiwa na matokeo na matriki ya ujuzi
  - Imejumuisha sehemu ya ujuzi wa kazi kwa umuhimu wa viwanda
  - Mwongozo wa kuanza haraka ukiwa na mahitaji na hatua 3 za usanidi
  - Imeunda meza za rasilimali kwa sampuli za Python (faili 8 na muda wa utekelezaji)
  - Imeongeza jedwali la daftari za Jupyter (daftari 8 na viwango vya ugumu)
  - Imeunda jedwali la nyaraka (nyaraka 7 muhimu na mwongozo wa "Tumia Wakati")
  - Imeongeza mapendekezo ya njia za kujifunza kwa viwango tofauti vya ujuzi

- **Miundombinu ya uthibitishaji na upimaji wa Warsha**:
  - Imeunda `scripts/validate_samples.py` - Zana ya uthibitishaji wa kina kwa sintaksia, uagizaji, na mbinu bora
  - Imeunda `scripts/test_samples.py` - Kipimaji cha haraka kwa sampuli zote za Python
  - Imeongeza nyaraka za uthibitishaji kwenye `scripts/README.md`

- **Nyaraka za kina**:
  - Imeunda `SAMPLES_UPDATE_SUMMARY.md` - Mwongozo wa kina wa mistari 400+ unaoelezea maboresho yote
  - Imeunda `UPDATE_COMPLETE.md` - Muhtasari wa utekelezaji wa sasisho
  - Imeunda `QUICK_REFERENCE.md` - Kadi ya rejeleo la haraka kwa Warsha

### Imebadilishwa - Kisasa cha Sampuli za Python za Warsha
- **Sampuli zote 8 za Python zimesasishwa kwa mbinu bora**:
  - Imeimarisha usimamizi wa makosa kwa vizuizi vya try-except kwenye shughuli zote za I/O
  - Imeongeza vidokezo vya aina na maelezo ya kina ya docstring
  - Imetekeleza muundo wa kuandika logi wa [INFO]/[ERROR]/[RESULT] kwa uthabiti
  - Uagizaji wa hiari umelindwa kwa vidokezo vya usakinishaji
  - Imeboresha maoni ya mtumiaji katika sampuli zote

- **session01/chat_bootstrap.py**:
  - Imeimarisha usanidi wa mteja kwa ujumbe wa makosa wa kina
  - Imeboresha usimamizi wa makosa ya utiririshaji kwa uthibitishaji wa vipande
  - Imeongeza usimamizi bora wa makosa kwa kutopatikana kwa huduma

- **session02/rag_pipeline.py**:
  - Imeongeza ulinzi wa uagizaji kwa sentence-transformers na vidokezo vya usakinishaji
  - Imeimarisha usimamizi wa makosa kwa shughuli za embedding na kizazi
  - Imeboresha muundo wa matokeo kwa matokeo yaliyojengwa

- **session02/rag_eval_ragas.py**:
  - Uagizaji wa hiari umelindwa (ragas, datasets) kwa ujumbe wa makosa wa kirafiki
  - Imeongeza usimamizi wa makosa kwa vipimo vya tathmini
  - Imeimarisha muundo wa matokeo kwa matokeo ya tathmini

- **session03/benchmark_oss_models.py**:
  - Imetekeleza kushuka kwa neema (inaendelea kwenye kushindwa kwa modeli)
  - Imeongeza ripoti ya maendeleo ya kina na usimamizi wa makosa kwa kila modeli
  - Imeimarisha hesabu za takwimu kwa urejeshaji wa makosa wa kina

- **session04/model_compare.py**:
  - Imeongeza vidokezo vya aina (Aina za Tuple za kurudi)
  - Imeimarisha muundo wa matokeo kwa matokeo ya JSON yaliyojengwa
  - Imetekeleza usimamizi wa makosa kwa kila modeli na urejeshaji

- **session05/agents_orchestrator.py**:
  - Imeimarisha Agent.act() kwa maelezo ya kina ya docstring
  - Imeongeza usimamizi wa makosa ya bomba kwa kuandika logi hatua kwa hatua
  - Imeboresha usimamizi wa kumbukumbu na ufuatiliaji wa hali

- **session06/models_router.py**:
  - Imeimarisha nyaraka za kazi kwa vipengele vyote vya uelekezaji
  - Imeongeza kuandika logi kwa kina katika kazi ya route()
  - Imeboresha matokeo ya majaribio kwa matokeo yaliyojengwa

- **session06/models_pipeline.py**:
  - Imeongeza usimamizi wa makosa kwa kazi ya msaidizi ya chat()
  - Imeimarisha pipeline() kwa kuandika logi ya hatua na ripoti ya maendeleo
  - Imeboresha main() kwa urejeshaji wa makosa wa kina

### Nyaraka - Uboreshaji wa Nyaraka za Warsha
- README.md kuu imesasishwa kwa sehemu ya Warsha inayoangazia njia ya kujifunza kwa vitendo
- STUDY_GUIDE.md imeimarishwa kwa sehemu ya Warsha ikijumuisha:
  - Malengo ya kujifunza na maeneo ya kuzingatia
  - Maswali ya kujitathmini
  - Mazoezi ya vitendo na makadirio ya muda
  - Ugawaji wa muda kwa kujifunza kwa umakini na kwa muda wa ziada
  - Imeongeza Warsha kwenye kiolezo cha ufuatiliaji wa maendeleo
- Mwongozo wa ugawaji wa muda umesasishwa kutoka saa 20 hadi saa 30 (ikiwemo Warsha)
- Maelezo ya sampuli za Warsha na matokeo ya kujifunza yameongezwa kwenye README

### Imetatuliwa
- Mifumo isiyo thabiti ya usimamizi wa makosa katika sampuli za Warsha imetatuliwa
- Makosa ya uagizaji wa utegemezi wa hiari yamesahihishwa kwa ulinzi sahihi
- Vidokezo vya aina vilivyokosekana katika kazi muhimu vimesahihishwa
- Ukosefu wa maoni ya mtumiaji katika hali za makosa umeshughulikiwa
- Masuala ya uthibitishaji yamesahihishwa kwa miundombinu ya majaribio ya kina

---

## 2025-09-23

### Imebadilishwa - Kisasa cha Moduli 08 Kubwa
- **Ulinganifu wa kina na mifumo ya hifadhi ya Microsoft Foundry-Local**:
  - Mifano yote ya msimbo imesasishwa kutumia `FoundryLocalManager` ya kisasa na ujumuishaji wa OpenAI SDK
  - Simu za `requests` zilizopitwa na wakati zimebadilishwa na matumizi sahihi ya SDK
  - Mifumo ya utekelezaji imepatanishwa na nyaraka rasmi za Microsoft na sampuli

- **05.AIPoweredAgents.md kisasa**:
  - Uratibu wa mawakala wengi umesasishwa kutumia mifumo ya kisasa ya SDK
  - Utekelezaji wa mratibu umeimarishwa kwa vipengele vya hali ya juu (mizunguko ya maoni, ufuatiliaji wa utendaji)
  - Usimamizi wa makosa wa kina na ukaguzi wa afya ya huduma umeongezwa
  - Marejeleo sahihi ya sampuli za ndani yamejumuishwa (`samples/05/multi_agent_orchestration.ipynb`)
  - Mifano ya kupiga kazi imesasishwa kutumia kipengele cha kisasa cha `tools` badala ya `functions` zilizopitwa na wakati
  - Mifumo ya utayarishaji wa uzalishaji yenye ufuatiliaji na ufuatiliaji wa takwimu imeongezwa

- **06.ModelsAsTools.md kuandikwa upya kabisa**:
  - Usajili wa zana za msingi umebadilishwa na utekelezaji wa router ya modeli yenye akili
  - Uchaguzi wa modeli kwa msingi wa maneno muhimu umeongezwa kwa aina tofauti za kazi (jumla, hoja, msimbo, ubunifu)
  - Ujumuishaji wa usanidi wa mazingira wenye ugawaji wa modeli unaobadilika umeongezwa
  - Ufuatiliaji wa afya ya huduma na usimamizi wa makosa wa kina umeimarishwa
  - Mifumo ya utayarishaji wa uzalishaji yenye ufuatiliaji wa maombi na ufuatiliaji wa utendaji imeongezwa
  - Imeunganishwa na utekelezaji wa ndani katika `samples/06/router.py` na `samples/06/model_router.ipynb`

- **Maboresho ya muundo wa nyaraka**:
  - Sehemu za muhtasari zimeongezwa zikionyesha kisasa na ulinganifu wa SDK
  - Imeimarishwa na emojis na muundo bora kwa usomaji rahisi
  - Marejeleo sahihi ya faili za sampuli za ndani yameongezwa katika nyaraka
  - Mwongozo wa utekelezaji wa uzalishaji na mbinu bora umejumuishwa

### Imeongezwa
- Sehemu za muhtasari wa kina katika faili za Moduli 08 zikionyesha ujumuishaji wa SDK ya kisasa
- Vipengele vya usanifu vinavyoonyesha vipengele vya hali ya juu (mifumo ya mawakala wengi, uelekezaji wenye akili)
- Marejeleo ya moja kwa moja kwa utekelezaji wa sampuli za ndani kwa uzoefu wa vitendo
- Mwongozo wa utayarishaji wa uzalishaji wenye mifumo ya ufuatiliaji na usimamizi wa makosa
- Mifano ya daftari za Jupyter za mwingiliano zenye vipengele vya hali ya juu na alama za utendaji

### Imetatuliwa
- Tofauti za ulinganifu kati ya nyaraka na utekelezaji halisi wa sampuli
- Mifumo ya matumizi ya SDK iliyopitwa na wakati katika Moduli 08
- Marejeleo yaliyokosekana kwa maktaba ya sampuli za ndani
- Mbinu zisizo thabiti za utekelezaji katika sehemu tofauti

---

## 2025-09-18

### Imeongezwa
- Moduli 08: Microsoft Foundry Local – Zana Kamili ya Msanidi Programu
  - Vipindi sita: usanidi, ujumuishaji wa Azure AI Foundry, mifano ya chanzo huria, maonyesho ya hali ya juu, mawakala, na modeli-kama-zana
  - Sampuli zinazoweza kuendeshwa chini ya `Module08/samples/01`–`06` na maagizo ya cmd ya Windows
    - `01` REST mazungumzo ya haraka (`chat_quickstart.py`)
    - `02` SDK kuanza haraka na OpenAI/Foundry Local na msaada wa Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI orodha-na-alama (`list_and_bench.cmd`)
    - `04` Maonyesho ya Chainlit (`app.py`)
    - `05` Uratibu wa mawakala wengi (`python -m samples.05.agents.coordinator`)
    - `06` Router ya Modeli-kama-Zana (`router.py`)
- Msaada wa Azure OpenAI katika sampuli ya SDK ya Kipindi cha 2 na usanidi wa mabadiliko ya mazingira
- `.vscode/settings.json` kuelekeza kwenye `Module08/.venv` na kuboresha azimio la uchambuzi wa Python
- `.env` na kidokezo cha `PYTHONPATH` kwa uelewa wa VS Code/Pylance

### Imebadilishwa
- Modeli chaguo-msingi imesasishwa kuwa `phi-4-mini` katika nyaraka na sampuli za Moduli 08; marejeleo yaliyobaki ya `phi-3.5` yameondolewa ndani ya Moduli 08
- Maboresho ya Router (`Module08/samples/06/router.py`):
  - Ugunduzi wa mwisho kupitia `foundry service status` na uchambuzi wa regex
  - Ukaguzi wa afya wa `/v1/models` wakati wa kuanza
  - Usajili wa modeli unaoweza kusanidiwa na mazingira (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Mahitaji yamesasishwa: `Module08/requirements.txt` sasa inajumuisha `openai` (pamoja na `requests`, `chainlit`)
- Mwongozo wa sampuli za Chainlit umefafanuliwa na utatuzi wa matatizo umeongezwa; azimio la uagizaji kupitia mipangilio ya eneo la kazi

### Imetatuliwa
- Masuala ya uagizaji yamesuluhishwa:
  - Router haitegemei tena moduli isiyokuwepo ya `utils`; kazi zimejumuishwa
  - Mratibu hutumia uagizaji wa jamaa (`from .specialists import ...`) na inaitwa kupitia njia ya moduli
  - Usanidi wa VS Code/Pylance kutatua `chainlit` na uagizaji wa kifurushi
- Typo ndogo katika `STUDY_GUIDE.md` imesahihishwa na chanjo ya Moduli 08 imeongezwa

### Imeondolewa
- `Module08/infra/obs.py` isiyotumika imefutwa na saraka tupu ya `infra/` imeondolewa; mifumo ya ufuatiliaji imehifadhiwa kama hiari katika nyaraka

### Imehama
- Maonyesho ya Moduli 08 yameunganishwa chini ya `Module08/samples` na folda zenye namba za vipindi
  - Chainlit app imehamishwa hadi `samples/04`
  - Mawakala wamehamishwa hadi `samples/05` na faili za `__init__.py` zimeongezwa kwa azimio la kifurushi

### Nyaraka
- Nyaraka za vipindi vya Moduli 08 na README zote za sampuli zimeimarishwa na marejeleo ya Microsoft Learn na wauzaji wanaoaminika
- `Module08/README.md` imesasishwa na Muhtasari wa Sampuli, usanidi wa router, na vidokezo vya uthibitishaji
- Sehemu ya Windows Foundry Local ya `Module07/README.md` imethibitishwa dhidi ya nyaraka za Learn
- `STUDY_GUIDE.md` imesasishwa:
  - Moduli 08 imeongezwa kwenye muhtasari, ratiba, kiolezo cha ufuatiliaji wa maendeleo
  - Sehemu ya Marejeleo ya kina imeongezwa (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historia (muhtasari)
- Usanifu wa kozi na moduli umeanzishwa (Moduli 01–07)
- Kisasa cha maudhui kwa hatua, usanifishaji wa muundo, na masomo ya kesi yaliyoongezwa
- Chanjo ya mifumo ya uboreshaji imepanuliwa (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Haijachapishwa / Hifadhi (mapendekezo)
- Vipimo vya moshi vya hiari kwa kila sampuli kuthibitisha upatikanaji wa Foundry Local
- Kagua tafsiri ili kupatanisha marejeleo ya modeli (mfano, `phi-4-mini`) inapofaa
- Ongeza usanidi wa chini wa pyright ikiwa timu zinapendelea ukali wa kiwango cha eneo la kazi

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.