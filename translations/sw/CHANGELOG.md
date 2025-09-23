<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:44:13+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sw"
}
-->
# Changelog

Mabadiliko yote muhimu kwa EdgeAI for Beginners yameandikwa hapa. Mradi huu unatumia maingizo ya tarehe na mtindo wa Keep a Changelog (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-18

### Added
- Moduli 08: Microsoft Foundry Local – Zana Kamili ya Waendelezaji
  - Vipindi sita: usanidi, ujumuishaji wa Azure AI Foundry, mifano ya chanzo huria, maonyesho ya kisasa, mawakala, na mifano kama zana
  - Sampuli zinazoweza kuendeshwa chini ya `Module08/samples/01`–`06` na maelekezo ya cmd ya Windows
    - `01` REST mazungumzo ya haraka (`chat_quickstart.py`)
    - `02` SDK kuanza haraka na OpenAI/Foundry Local na msaada wa Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI orodha-na-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Uratibu wa mawakala wengi (`python -m samples.05.agents.coordinator`)
    - `06` Router wa Models-as-Tools (`router.py`)
- Msaada wa Azure OpenAI katika sampuli ya SDK ya Kipindi cha 2 na usanidi wa mazingira
- `.vscode/settings.json` kuelekeza kwa `Module08/.venv` na kuboresha azimio la uchambuzi wa Python
- `.env` na kidokezo cha `PYTHONPATH` kwa uelewa wa VS Code/Pylance

### Changed
- Mfano wa chaguo-msingi umebadilishwa kuwa `phi-4-mini` katika nyaraka na sampuli za Moduli 08; kutajwa kwa `phi-3.5` kumebaki kuondolewa ndani ya Moduli 08
- Maboresho ya Router (`Module08/samples/06/router.py`):
  - Ugunduzi wa endpoint kupitia `foundry service status` na uchambuzi wa regex
  - Ukaguzi wa afya wa `/v1/models` wakati wa kuanza
  - Usajili wa mfano unaoweza kusanidiwa na mazingira (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Mahitaji yamesasishwa: `Module08/requirements.txt` sasa inajumuisha `openai` (pamoja na `requests`, `chainlit`)
- Mwongozo wa sampuli ya Chainlit umefafanuliwa na masuala ya utatuzi yameongezwa; azimio la uagizaji kupitia mipangilio ya workspace

### Fixed
- Masuala ya uagizaji yametatuliwa:
  - Router haitegemei tena moduli ya `utils` isiyokuwepo; kazi zimejumuishwa
  - Coordinator hutumia uagizaji wa jamaa (`from .specialists import ...`) na inaitwa kupitia njia ya moduli
  - Usanidi wa VS Code/Pylance kutatua `chainlit` na uagizaji wa kifurushi
- Kosa dogo la tahajia limerekebishwa katika `STUDY_GUIDE.md` na chanjo ya Moduli 08 imeongezwa

### Removed
- `Module08/infra/obs.py` isiyotumika imefutwa na saraka tupu ya `infra/` imeondolewa; mifumo ya uchunguzi imehifadhiwa kama hiari katika nyaraka

### Moved
- Maonyesho ya Moduli 08 yameunganishwa chini ya `Module08/samples` na folda zilizoorodheshwa kwa namba za vipindi
  - Chainlit app imehamishwa hadi `samples/04`
  - Mawakala wamehamishwa hadi `samples/05` na faili za `__init__.py` zimeongezwa kwa azimio la kifurushi

### Docs
- Nyaraka za vipindi vya Moduli 08 na README zote za sampuli zimeboreshwa na marejeleo ya Microsoft Learn na wauzaji wanaoaminika
- `Module08/README.md` imesasishwa na Muhtasari wa Sampuli, usanidi wa router, na vidokezo vya uthibitishaji
- Sehemu ya Windows Foundry Local ya `Module07/README.md` imethibitishwa dhidi ya nyaraka za Learn
- `STUDY_GUIDE.md` imesasishwa:
  - Moduli 08 imeongezwa kwenye muhtasari, ratiba, na tracker ya maendeleo
  - Sehemu ya Marejeleo ya kina imeongezwa (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Usanifu wa kozi na moduli umeanzishwa (Moduli 01–07)
- Usasishaji wa maudhui kwa hatua, usanifu wa muundo, na masomo ya kesi yaliyoongezwa
- Chanjo ya mifumo ya uboreshaji imepanuliwa (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Vipimo vya moshi vya hiari kwa kila sampuli ili kuthibitisha upatikanaji wa Foundry Local
- Kagua tafsiri ili kuoanisha marejeleo ya mifano (mfano, `phi-4-mini`) inapofaa
- Ongeza usanidi mdogo wa pyright ikiwa timu zinapendelea ukali wa workspace nzima

---

