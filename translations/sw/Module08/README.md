<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-23T00:47:07+00:00",
  "source_file": "Module08/README.md",
  "language_code": "sw"
}
-->
# Moduli 08: Kufanya Kazi na Microsoft Foundry Local - Zana Kamili ya Mwandishi

## Muhtasari

Microsoft Foundry Local inawakilisha kizazi kipya cha maendeleo ya AI ya ukingoni, ikiwapa waendelezaji zana zenye nguvu za kujenga, kupeleka, na kupanua programu za AI kwa ndani huku ikidumisha muunganisho wa bila mshono na Azure AI Foundry. Moduli hii inatoa mafunzo ya kina kuhusu Foundry Local kuanzia usakinishaji hadi maendeleo ya mawakala wa hali ya juu.

**Teknolojia Muhimu:**
- Microsoft Foundry Local CLI na SDK
- Muunganisho wa Azure AI Foundry
- Utoaji wa modeli kwenye kifaa
- Uboreshaji na uhifadhi wa modeli kwa ndani
- Miundombinu ya msingi wa mawakala

## Malengo ya Kujifunza ya Moduli

Kwa kukamilisha moduli hii, utaweza:

- **Kumiliki Usanidi wa Foundry Local**: Kusakinisha, kusanidi, na kuboresha Foundry Local kwa maendeleo ya Windows 11
- **Kupeleka Modeli Tofauti**: Kuendesha modeli za phi, qwen, deepseek, na GPT-OSS-20B kwa ndani kwa kutumia amri za CLI
- **Kujenga Suluhisho za Uzalishaji**: Kuunda programu za AI kwa kutumia uhandisi wa hali ya juu wa maelekezo na muunganisho wa data
- **Kufaidika na Mfumo wa Chanzo Huria**: Kuunganisha modeli za Hugging Face na nyongeza zinazoendeshwa na jamii
- **Kulinganisha Miundombinu ya AI**: Kuelewa faida na hasara za LLMs dhidi ya SLMs na mikakati ya kupeleka
- **Kuendeleza Mawakala wa AI**: Kujenga mawakala wenye akili kwa kutumia miundombinu ya Foundry Local na uwezo wa msingi
- **Kutumia Modeli kama Zana**: Kuunda suluhisho za AI zinazoweza kubadilishwa kwa matumizi ya biashara

## Muundo wa Kipindi

### [1: Kuanza na Foundry Local](./01.FoundryLocalSetup.md)
**Lengo**: Usakinishaji, usanidi wa CLI, uhifadhi wa modeli, na uboreshaji wa vifaa

**Unachojifunza:**
- Usakinishaji kamili wa Foundry Local kwenye Windows 11
- Usanidi wa CLI na muundo wa amri
- Mikakati ya uhifadhi wa modeli kwa utendaji bora
- Usanidi wa uboreshaji wa vifaa na vifaa vya kuongeza kasi
- Utekelezaji wa modeli za phi, qwen, deepseek, na GPT-OSS-20B kwa vitendo

**Muda**: Saa 2-3  
**Mahitaji ya Awali**: Windows 11, maarifa ya msingi ya mstari wa amri

---

### [2: Kujenga Suluhisho za AI na Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Lengo**: Uhandisi wa hali ya juu wa maelekezo, muunganisho wa data, na kazi zinazoweza kutekelezwa

**Unachojifunza:**
- Mbinu za hali ya juu za uhandisi wa maelekezo
- Mifumo ya muunganisho wa data na mbinu bora
- Kujenga kazi za AI zinazoweza kutekelezwa kwa Foundry Local
- Mifumo ya kazi ya muunganisho wa bila mshono wa Azure AI Foundry
- Uboreshaji wa utendaji na ufuatiliaji

**Muda**: Saa 2-3  
**Mahitaji ya Awali**: Kukamilisha Kipindi cha 1, akaunti ya Azure (hiari)

---

### [3: Modeli za Chanzo Huria Foundry Local](./03.OpenSourceModels.md)
**Lengo**: Muunganisho wa Hugging Face, mikakati ya kuchagua modeli, na nyongeza zinazoendeshwa na jamii

**Unachojifunza:**
- Muunganisho wa modeli za Hugging Face na Foundry Local
- Mikakati ya "leta modeli yako mwenyewe" (BYOM) na utekelezaji
- Maarifa kutoka mfululizo wa Model Mondays na michango ya jamii
- Utekelezaji wa modeli maalum na uboreshaji
- Vigezo vya kuchagua na kutathmini modeli za jamii

**Muda**: Saa 2-3  
**Mahitaji ya Awali**: Kukamilisha Vipindi vya 1-2, akaunti ya Hugging Face

---

### [4: Kuchunguza Modeli za Kisasa - LLMs, SLMs, na Utoaji wa Kifaa](./04.CuttingEdgeModels.md)
**Lengo**: Kulinganisha modeli, EdgeAI na Phi na ONNX Runtime, maonyesho ya hali ya juu

**Unachojifunza:**
- Kulinganisha kwa kina LLMs dhidi ya SLMs na matumizi yao
- Faida na hasara za utoaji wa ndani dhidi ya wingu na mifumo ya maamuzi
- Utekelezaji wa EdgeAI na Phi na ONNX Runtime
- Maendeleo na utekelezaji wa Chainlit RAG Chat App
- Mbinu za uboreshaji wa utoaji wa WebGPU
- Muunganisho wa AI PC SDK na uwezo wake

**Muda**: Saa 3-4  
**Mahitaji ya Awali**: Kukamilisha Vipindi vya 1-3, uelewa wa dhana za utoaji

---

### [5: Kujenga Mawakala Wenye Nguvu za AI Haraka kwa Foundry Local](./05.AIPoweredAgents.md)
**Lengo**: Maendeleo ya haraka ya programu za GenAI, maelekezo ya mfumo, msingi, na miundombinu ya mawakala

**Unachojifunza:**
- Miundombinu ya mawakala wa Foundry Local na mifumo ya muundo
- Uhandisi wa maelekezo ya mfumo kwa tabia ya mawakala
- Mbinu za msingi kwa majibu ya kuaminika ya mawakala
- Mifumo ya kazi ya maendeleo ya haraka ya programu za GenAI
- Uratibu wa mawakala na mifumo ya mawakala wengi
- Mikakati ya kupeleka mawakala wa AI kwa uzalishaji

**Muda**: Saa 3-4  
**Mahitaji ya Awali**: Kukamilisha Vipindi vya 1-4, uelewa wa msingi wa mawakala wa AI

---

### [6: Foundry Local - Modeli kama Zana](./06.ModelsAsTools.md)
**Lengo**: Suluhisho za AI zinazoweza kubadilishwa, utoaji wa kifaa, na upanuzi wa biashara

**Unachojifunza:**
- Kutumia modeli za AI kama zana zinazoweza kubadilishwa
- Utoaji wa kifaa bila utegemezi wa wingu
- Utoaji wa kasi ya chini, gharama nafuu, na uhifadhi wa faragha
- Mifumo ya muunganisho wa SDK, API, na CLI
- Kubadilisha modeli kwa matumizi maalum
- Mikakati ya upanuzi kutoka kwa prototipu za ndani hadi Azure AI Foundry
- Miundombinu ya programu za AI tayari kwa biashara

**Muda**: Saa 3-4  
**Mahitaji ya Awali**: Vipindi vyote vilivyopita, uzoefu wa maendeleo ya biashara ni muhimu

## Mahitaji ya Awali

### Mahitaji ya Mfumo
- **Mfumo wa Uendeshaji**: Windows 11 (22H2 au baadaye)
- **Kumbukumbu**: RAM ya 16GB (32GB inapendekezwa kwa modeli kubwa)
- **Hifadhi**: Nafasi ya GB 50 kwa uhifadhi wa modeli
- **Vifaa**: Kifaa chenye NPU kinapendekezwa (Copilot+ PC), GPU ni hiari
- **Mtandao**: Intaneti ya kasi kwa upakuaji wa modeli wa awali

### Mazingira ya Maendeleo
- Visual Studio Code na kiendelezi cha AI Toolkit
- Python 3.10+ na pip
- Git kwa udhibiti wa toleo
- PowerShell au Command Prompt
- Azure CLI (hiari kwa muunganisho wa wingu)

### Maarifa ya Awali
- Uelewa wa msingi wa dhana za AI/ML
- Uzoefu wa mstari wa amri
- Msingi wa programu ya Python
- Dhana za REST API
- Maarifa ya msingi ya maelekezo na utoaji wa modeli

## Ratiba ya Moduli

**Muda wa Jumla Uliokadiriwa**: Saa 15-20

| Kipindi | Eneo la Kuzingatia | Muda | Ugumu |
|---------|--------------------|------|-------|
|  1 | Usanidi & Msingi | Saa 2-3 | Mwanzoni |
|  2 | Suluhisho za AI | Saa 2-3 | Kati |
|  3 | Chanzo Huria | Saa 2-3 | Kati |
|  4 | Modeli za Kisasa | Saa 3-4 | Juu |
|  5 | Mawakala wa AI | Saa 3-4 | Juu |
|  6 | Zana za Biashara | Saa 3-4 | Mtaalamu |

## Rasilimali Muhimu

### Nyaraka za Msingi
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Series](https://aka.ms/model-mondays)

### Rasilimali za Jamii
- [Majadiliano ya Jamii ya Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Mifano ya Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Jamii ya Waendelezaji wa Microsoft AI](https://techcommunity.microsoft.com/category/artificialintelligence)

## Matokeo ya Kujifunza

Baada ya kukamilisha moduli hii, utaweza:

### Ustadi wa Kiufundi
- **Kusakinisha na Kusimamia**: Usakinishaji wa Foundry Local katika mazingira ya maendeleo na uzalishaji
- **Kuunganisha Modeli**: Kufanya kazi bila mshono na familia tofauti za modeli kutoka Microsoft, Hugging Face, na vyanzo vya jamii
- **Kujenga Programu**: Kuunda programu za AI tayari kwa uzalishaji zenye vipengele vya hali ya juu na uboreshaji
- **Kuendeleza Mawakala**: Kutekeleza mawakala wa AI wenye akili na uwezo wa msingi, uamuzi, na muunganisho wa zana

### Uelewa wa Kistratejia
- **Maamuzi ya Miundombinu**: Kufanya chaguo sahihi kati ya utoaji wa ndani dhidi ya wingu
- **Uboreshaji wa Utendaji**: Kuboresha utendaji wa utoaji katika usanidi tofauti wa vifaa
- **Upanuzi wa Biashara**: Kubuni programu zinazopanuka kutoka prototipu za ndani hadi utekelezaji wa biashara
- **Faragha na Usalama**: Kutekeleza suluhisho za AI zinazohifadhi faragha kwa utoaji wa ndani

### Uwezo wa Ubunifu
- **Maendeleo ya Haraka**: Kujenga na kujaribu dhana za programu za AI haraka
- **Muunganisho wa Jamii**: Kufaidika na modeli za chanzo huria na kuchangia kwenye mfumo
- **Mifumo ya Hali ya Juu**: Kutekeleza mifumo ya AI ya kisasa ikijumuisha RAG, mawakala, na muunganisho wa zana
- **Maendeleo Tayari kwa Teknolojia ya Baadaye**: Kujenga programu tayari kwa teknolojia na mifumo ya AI inayojitokeza

## Kuanza

1. **Andaa Mazingira Yako**: Hakikisha Windows 11 na vipimo vya vifaa vinavyopendekezwa
2. **Sakinisha Mahitaji ya Awali**: Sanidi zana za maendeleo na utegemezi
3. **Anza na Kipindi cha 1**: Anza na usakinishaji wa Foundry Local na usanidi wa msingi
4. **Endelea kwa Utaratibu**: Kamilisha vipindi kwa mpangilio kwa maendeleo bora ya kujifunza
5. **Fanya Mazoezi Mara kwa Mara**: Tumia dhana kupitia mazoezi ya vitendo na miradi

## Vipimo vya Mafanikio

Fuata maendeleo yako kupitia moduli:

- [ ] Kusakinisha na kusanidi Foundry Local kwa mafanikio
- [ ] Kupeleka na kuendesha angalau familia 4 tofauti za modeli
- [ ] Kujenga suluhisho kamili la AI na muunganisho wa data
- [ ] Kuunganisha angalau modeli 2 za chanzo huria
- [ ] Kuunda programu ya mazungumzo ya RAG inayofanya kazi
- [ ] Kuendeleza na kupeleka wakala wa AI
- [ ] Kutekeleza miundombinu ya modeli-kama-zana

## Kuanza Haraka kwa Sampuli

### 1) Usanidi wa Mazingira (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Anzisha modeli ya ndani (terminal mpya)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Endesha demo ya Chainlit (Kipindi cha 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Endesha uratibu wa mawakala wengi (Kipindi cha 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Ikiwa utaona makosa ya muunganisho, thibitisha Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Usanidi wa router (Kipindi cha 6)
Router hufanya ukaguzi wa haraka wa afya na inasaidia usanidi wa msingi wa mazingira:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Moduli hii inawakilisha kilele cha maendeleo ya AI ya ukingoni, ikichanganya zana za Microsoft za daraja la biashara na kubadilika na ubunifu wa mfumo wa chanzo huria. Kwa kumiliki Foundry Local, utakuwa mbele katika maendeleo ya programu za AI.

Kwa Azure OpenAI (Kipindi cha 2), angalia README ya sampuli kwa vigezo vya mazingira vinavyohitajika na mipangilio ya toleo la API.

## Muhtasari wa Sampuli

- `samples/01`: Mazungumzo ya haraka ya REST kwa Foundry Local (`chat_quickstart.py`).
- `samples/02`: Muunganisho wa SDK ya OpenAI (`sdk_quickstart.py`).
- `samples/03`: Ugunduzi wa modeli + benchi ya haraka (`list_and_bench.cmd`).
- `samples/04`: Demo ya Chainlit RAG (`app.py`).
- `samples/05`: Uratibu wa mawakala wengi (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router ya modeli-kama-zana (`python samples\06\router.py`).

---

