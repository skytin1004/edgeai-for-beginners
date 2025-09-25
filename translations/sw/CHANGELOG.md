<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T00:56:45+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sw"
}
-->
# Changelog

Mabadiliko yote muhimu kwa EdgeAI kwa Kompyuta yanarekodiwa hapa. Mradi huu unatumia maingizo ya tarehe na mtindo wa Keep a Changelog (Imeongezwa, Imebadilishwa, Imetatuliwa, Imeondolewa, Nyaraka, Imehama).

## 2025-09-23

### Imebadilishwa - Uboreshaji Mkubwa wa Moduli 08
- **Ulinganifu wa kina na mifumo ya hifadhi ya Microsoft Foundry-Local**
  - Imesasisha mifano yote ya msimbo kutumia `FoundryLocalManager` ya kisasa na ujumuishaji wa OpenAI SDK
  - Imerejesha miito ya zamani ya `requests` kwa matumizi sahihi ya SDK
  - Imelinganisha mifumo ya utekelezaji na nyaraka rasmi za Microsoft na sampuli

- **05.AIPoweredAgents.md uboreshaji**:
  - Imesasisha uratibu wa mawakala wengi kutumia mifumo ya kisasa ya SDK
  - Imekuza utekelezaji wa uratibu na vipengele vya hali ya juu (mizunguko ya maoni, ufuatiliaji wa utendaji)
  - Imeongeza utunzaji wa makosa wa kina na ukaguzi wa afya ya huduma
  - Imeshirikisha marejeleo sahihi kwa sampuli za ndani (`samples/05/multi_agent_orchestration.ipynb`)
  - Imesasisha mifano ya miito ya kazi kutumia kipengele cha kisasa `tools` badala ya `functions` iliyopitwa na wakati
  - Imeongeza mifumo ya utayarishaji inayofaa na ufuatiliaji na ufuatiliaji wa takwimu

- **06.ModelsAsTools.md imeandikwa upya kabisa**:
  - Imerejesha usajili wa zana wa msingi na utekelezaji wa router ya modeli yenye akili
  - Imeongeza uteuzi wa modeli kulingana na maneno muhimu kwa aina tofauti za kazi (jumla, kufikiri, msimbo, ubunifu)
  - Imeshirikisha usanidi kulingana na mazingira na ugawaji wa modeli unaobadilika
  - Imekuzwa na ufuatiliaji wa afya ya huduma wa kina na utunzaji wa makosa
  - Imeongeza mifumo ya utayarishaji na ufuatiliaji wa maombi na ufuatiliaji wa utendaji
  - Imelinganisha na utekelezaji wa ndani katika `samples/06/router.py` na `samples/06/model_router.ipynb`

- **Uboreshaji wa muundo wa nyaraka**:
  - Imeongeza sehemu za muhtasari zinazosisitiza uboreshaji na ulinganifu wa SDK
  - Imekuzwa na emojis na muundo bora kwa usomaji ulioimarishwa
  - Imeshirikisha marejeleo sahihi kwa faili za sampuli za ndani katika nyaraka
  - Imeshirikisha mwongozo wa utekelezaji wa utayarishaji na mbinu bora

### Imeongezwa
- Sehemu za muhtasari wa kina katika faili za Moduli 08 zinazosisitiza ujumuishaji wa SDK ya kisasa
- Muhtasari wa usanifu unaoonyesha vipengele vya hali ya juu (mifumo ya mawakala wengi, uratibu wenye akili)
- Marejeleo ya moja kwa moja kwa utekelezaji wa sampuli za ndani kwa uzoefu wa vitendo
- Mwongozo wa utayarishaji wa uzalishaji na mifumo ya ufuatiliaji na utunzaji wa makosa
- Mifano ya maingiliano ya Jupyter notebook yenye vipengele vya hali ya juu na viwango vya majaribio

### Imetatuliwa
- Tofauti za ulinganifu kati ya nyaraka na utekelezaji halisi wa sampuli
- Mifumo ya matumizi ya SDK iliyopitwa na wakati katika Moduli 08
- Marejeleo yaliyokosekana kwa maktaba ya sampuli ya ndani ya kina
- Mbinu zisizo thabiti za utekelezaji katika sehemu tofauti

---

## 2025-09-18

### Imeongezwa
- Moduli 08: Microsoft Foundry Local – Kifaa Kamili cha Watengenezaji
  - Vipindi sita: usanidi, ujumuishaji wa Azure AI Foundry, modeli za chanzo huria, maonyesho ya kisasa, mawakala, na modeli-kama-zana
  - Sampuli zinazoweza kuendeshwa chini ya `Module08/samples/01`–`06` na maagizo ya cmd ya Windows
    - `01` REST mazungumzo ya haraka (`chat_quickstart.py`)
    - `02` SDK ya kuanza haraka na OpenAI/Foundry Local na msaada wa Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI orodha-na-majaribio (`list_and_bench.cmd`)
    - `04` Maonyesho ya Chainlit (`app.py`)
    - `05` Uratibu wa mawakala wengi (`python -m samples.05.agents.coordinator`)
    - `06` Router ya Modeli-kama-Zana (`router.py`)
- Msaada wa Azure OpenAI katika sampuli ya SDK ya Kipindi cha 2 na usanidi wa vigezo vya mazingira
- `.vscode/settings.json` kuelekeza kwa `Module08/.venv` na kuboresha azimio la uchambuzi wa Python
- `.env` na kidokezo cha `PYTHONPATH` kwa uelewa wa VS Code/Pylance

### Imebadilishwa
- Modeli ya msingi imesasishwa kuwa `phi-4-mini` katika nyaraka na sampuli za Moduli 08; imerejesha marejeleo ya `phi-3.5` yaliyosalia ndani ya Moduli 08
- Uboreshaji wa Router (`Module08/samples/06/router.py`):
  - Ugunduzi wa endpoint kupitia `foundry service status` na uchambuzi wa regex
  - Ukaguzi wa afya wa `/v1/models` wakati wa kuanza
  - Usajili wa modeli unaoweza kusanidiwa na mazingira (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Mahitaji yamesasishwa: `Module08/requirements.txt` sasa inajumuisha `openai` (pamoja na `requests`, `chainlit`)
- Mwongozo wa sampuli ya Chainlit umefafanuliwa na utatuzi wa matatizo umeongezwa; azimio la uagizaji kupitia mipangilio ya workspace

### Imetatuliwa
- Masuala ya uagizaji yametatuliwa:
  - Router haitegemei tena moduli ya `utils` isiyokuwepo; kazi zimejumuishwa
  - Coordinator hutumia uagizaji wa jamaa (`from .specialists import ...`) na inaitwa kupitia njia ya moduli
  - Usanidi wa VS Code/Pylance kutatua `chainlit` na uagizaji wa kifurushi
- Kosa dogo katika `STUDY_GUIDE.md` limerekebishwa na chanjo ya Moduli 08 imeongezwa

### Imeondolewa
- Imefuta `Module08/infra/obs.py` isiyotumika na kuondoa saraka tupu ya `infra/`; mifumo ya uchunguzi imehifadhiwa kama hiari katika nyaraka

### Imehama
- Maonyesho ya Moduli 08 yameunganishwa chini ya `Module08/samples` na folda zenye namba za vipindi
  - Chainlit app imehamishwa hadi `samples/04`
  - Mawakala wamehamishwa hadi `samples/05` na faili za `__init__.py` zimeongezwa kwa azimio la kifurushi

### Nyaraka
- Nyaraka za vipindi vya Moduli 08 na README zote za sampuli zimeimarishwa na marejeleo ya Microsoft Learn na wauzaji wanaoaminika
- `Module08/README.md` imesasishwa na Muhtasari wa Sampuli, usanidi wa router, na vidokezo vya uthibitishaji
- `Module07/README.md` sehemu ya Windows Foundry Local imethibitishwa dhidi ya nyaraka za Learn
- `STUDY_GUIDE.md` imesasishwa:
  - Moduli 08 imeongezwa kwa muhtasari, ratiba, na ufuatiliaji wa maendeleo
  - Sehemu ya Marejeleo ya kina imeongezwa (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historia (muhtasari)
- Usanifu wa kozi na moduli umeanzishwa (Moduli 01–07)
- Uboreshaji wa maudhui kwa hatua, usanifu wa muundo, na masomo ya kesi yaliyoongezwa
- Upanuzi wa chanjo ya mifumo ya uboreshaji (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Haijachapishwa / Kazi ya nyuma (mapendekezo)
- Vipimo vya moshi vya hiari kwa kila sampuli ili kuthibitisha upatikanaji wa Foundry Local
- Kagua tafsiri ili kulinganisha marejeleo ya modeli (mfano, `phi-4-mini`) inapofaa
- Ongeza usanidi mdogo wa pyright ikiwa timu zinapendelea ukali wa workspace nzima

---

