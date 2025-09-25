<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50d80c321803b5170d9a9cd9bbfb37a3",
  "translation_date": "2025-09-25T01:01:36+00:00",
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
- Kuhifadhi na kuboresha modeli kwa ndani
- Miundombinu ya msingi wa mawakala

## Malengo ya Kujifunza

Kwa kukamilisha moduli hii, utaweza:

- **Kumiliki Foundry Local**: Kusakinisha, kusanidi, na kuboresha kwa maendeleo ya Windows 11
- **Kupeleka Modeli Tofauti**: Kuendesha modeli za phi, qwen, deepseek, na GPT kwa ndani kwa kutumia amri za CLI
- **Kujenga Suluhisho za Uzalishaji**: Kuunda programu za AI kwa kutumia uhandisi wa hali ya juu wa maelekezo na muunganisho wa data
- **Kufaidika na Mfumo wa Chanzo Huria**: Kuunganisha modeli za Hugging Face na michango ya jamii
- **Kuendeleza Mawakala wa AI**: Kujenga mawakala wenye akili na uwezo wa kuunganisha na kuratibu
- **Kutumia Mifumo ya Biashara**: Kuunda suluhisho za AI zenye moduli na zinazoweza kupanuka kwa ajili ya kupelekwa uzalishaji

## Muundo wa Kipindi

### [1: Kuanza na Foundry Local](./01.FoundryLocalSetup.md)
**Lengo**: Usakinishaji, usanidi wa CLI, upelekaji wa modeli, na uboreshaji wa vifaa

**Mada Muhimu**: Usakinishaji kamili • Amri za CLI • Kuhifadhi modeli • Kuongeza kasi ya vifaa • Upelekaji wa modeli nyingi

**Mfano**: [Mwongozo wa Haraka wa REST Chat](./samples/01/README.md) • [Muunganisho wa OpenAI SDK](./samples/02/README.md) • [Ugunduzi wa Modeli na Upimaji](./samples/03/README.md)

**Muda**: Saa 2-3 | **Kiwango**: Mwanzoni

---

### [2: Kujenga Suluhisho za AI na Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Lengo**: Uhandisi wa hali ya juu wa maelekezo, muunganisho wa data, na muunganisho wa wingu

**Mada Muhimu**: Uhandisi wa maelekezo • Muunganisho wa data • Mifumo ya Azure • Uboreshaji wa utendaji • Ufuatiliaji

**Mfano**: [Programu ya Chainlit RAG](./samples/04/README.md)

**Muda**: Saa 2-3 | **Kiwango**: Kati

---

### [3: Modeli za Chanzo Huria Foundry Local](./03.OpenSourceModels.md)
**Lengo**: Muunganisho wa Hugging Face, mikakati ya BYOM, na modeli za jamii

**Mada Muhimu**: Muunganisho wa HuggingFace • Kuleta modeli yako mwenyewe • Maarifa ya Model Mondays • Michango ya jamii • Uchaguzi wa modeli

**Mfano**: [Uratibu wa Mawakala Wengi](./samples/05/README.md)

**Muda**: Saa 2-3 | **Kiwango**: Kati

---

### [4: Kuchunguza Modeli za Kisasa](./04.CuttingEdgeModels.md)
**Lengo**: LLMs vs SLMs, utekelezaji wa EdgeAI, na maonyesho ya hali ya juu

**Mada Muhimu**: Ulinganisho wa modeli • Utoaji wa ukingoni vs wingu • Phi + ONNX Runtime • Programu ya Chainlit RAG • Uboreshaji wa WebGPU

**Mfano**: [Router ya Modeli-kama-Zana](./samples/06/README.md)

**Muda**: Saa 3-4 | **Kiwango**: Juu

---

### [5: Kujenga Mawakala Wenye Nguvu za AI Haraka](./05.AIPoweredAgents.md)
**Lengo**: Miundombinu ya mawakala, maelekezo ya mfumo, uunganishaji, na uratibu

**Mada Muhimu**: Mifumo ya kubuni mawakala • Uhandisi wa maelekezo ya mfumo • Mbinu za uunganishaji • Mifumo ya mawakala wengi • Upelekaji wa uzalishaji

**Mfano**: [Uratibu wa Mawakala Wengi](./samples/05/README.md) • [Mfumo wa Mawakala Wengi wa Hali ya Juu](./samples/09/README.md)

**Muda**: Saa 3-4 | **Kiwango**: Juu

---

### [6: Foundry Local - Modeli kama Zana](./06.ModelsAsTools.md)
**Lengo**: Suluhisho za AI zenye moduli, upanuzi wa biashara, na mifumo ya uzalishaji

**Mada Muhimu**: Modeli kama zana • Upelekaji kwenye kifaa • Muunganisho wa SDK/API • Miundombinu ya biashara • Mikakati ya upanuzi

**Mfano**: [Router ya Modeli-kama-Zana](./samples/06/README.md) • [Mfumo wa Zana za Foundry](./samples/10/README.md)

**Muda**: Saa 3-4 | **Kiwango**: Mtaalamu

---

### [7: Mifumo ya Muunganisho wa API Moja kwa Moja](./samples/07/README.md)
**Lengo**: Muunganisho wa REST API bila utegemezi wa SDK kwa udhibiti wa juu zaidi

**Mada Muhimu**: Utekelezaji wa mteja wa HTTP • Uthibitishaji maalum • Ufuatiliaji wa afya ya modeli • Majibu ya mtiririko • Kushughulikia makosa ya uzalishaji

**Mfano**: [Mteja wa API Moja kwa Moja](./samples/07/README.md)

**Muda**: Saa 2-3 | **Kiwango**: Kati

---

### [8: Programu ya Mazungumzo ya Asili ya Windows 11](./samples/08/README.md)
**Lengo**: Kujenga programu za kisasa za mazungumzo za asili kwa muunganisho wa Foundry Local

**Mada Muhimu**: Maendeleo ya Electron • Mfumo wa Ubunifu wa Fluent • Muunganisho wa asili wa Windows • Mtiririko wa wakati halisi • Ubunifu wa kiolesura cha mazungumzo

**Mfano**: [Programu ya Mazungumzo ya Windows 11](./samples/08/README.md)

**Muda**: Saa 3-4 | **Kiwango**: Juu

---

### [9: Uratibu wa Mawakala Wengi wa Hali ya Juu](./samples/09/README.md)
**Lengo**: Uratibu wa mawakala wa hali ya juu, ugawaji wa kazi maalum, na mifumo ya AI ya kushirikiana

**Mada Muhimu**: Uratibu wa mawakala wenye akili • Mifumo ya kupiga kazi • Mawasiliano kati ya mawakala • Uratibu wa mifumo ya kazi • Mbinu za uhakikisho wa ubora

**Mfano**: [Mfumo wa Mawakala Wengi wa Hali ya Juu](./samples/09/README.md)

**Muda**: Saa 4-5 | **Kiwango**: Mtaalamu

---

### [10: Foundry Local kama Mfumo wa Zana](./samples/10/README.md)
**Lengo**: Miundombinu inayozingatia zana kwa kuunganisha Foundry Local kwenye programu na mifumo iliyopo

**Mada Muhimu**: Muunganisho wa LangChain • Kazi za Semantic Kernel • Mifumo ya REST API • Zana za CLI • Muunganisho wa Jupyter • Mifumo ya upelekaji uzalishaji

**Mfano**: [Mfumo wa Zana za Foundry](./samples/10/README.md)

**Muda**: Saa 4-5 | **Kiwango**: Mtaalamu

## Mahitaji ya Awali

### Mahitaji ya Mfumo
- **Mfumo wa Uendeshaji**: Windows 11 (22H2 au zaidi)
- **Kumbukumbu**: RAM ya 16GB (32GB inapendekezwa kwa modeli kubwa)
- **Hifadhi**: Nafasi ya bure ya 50GB kwa kuhifadhi modeli
- **Vifaa**: Kifaa chenye NPU kinapendekezwa (Copilot+ PC), GPU ni hiari
- **Mtandao**: Intaneti ya kasi ya juu kwa upakuaji wa modeli wa awali

### Mazingira ya Maendeleo
- Visual Studio Code na kiendelezi cha AI Toolkit
- Python 3.10+ na pip
- Git kwa udhibiti wa toleo
- PowerShell au Command Prompt
- Azure CLI (hiari kwa muunganisho wa wingu)

### Maarifa ya Awali
- Uelewa wa msingi wa dhana za AI/ML
- Uzoefu wa kutumia amri za mstari
- Msingi wa programu ya Python
- Dhana za REST API
- Maarifa ya msingi ya maelekezo na utoaji wa modeli

## Ratiba ya Moduli

**Muda wa Jumla Uliokadiriwa**: Saa 30-38

| Kipindi | Eneo la Kuzingatia | Sampuli | Muda | Ugumu |
|---------|--------------------|---------|------|-------|
|  1 | Usakinishaji & Msingi | 01, 02, 03 | Saa 2-3 | Mwanzoni |
|  2 | Suluhisho za AI | 04 | Saa 2-3 | Kati |
|  3 | Chanzo Huria | 05 | Saa 2-3 | Kati |
|  4 | Modeli za Juu | 06 | Saa 3-4 | Juu |
|  5 | Mawakala wa AI | 05, 09 | Saa 3-4 | Juu |
|  6 | Zana za Biashara | 06, 10 | Saa 3-4 | Mtaalamu |
|  7 | Muunganisho wa API Moja kwa Moja | 07 | Saa 2-3 | Kati |
|  8 | Programu ya Mazungumzo ya Windows 11 | 08 | Saa 3-4 | Juu |
|  9 | Mawakala Wengi wa Hali ya Juu | 09 | Saa 4-5 | Mtaalamu |
| 10 | Mfumo wa Zana | 10 | Saa 4-5 | Mtaalamu |

## Rasilimali Muhimu

**Nyaraka Rasmi:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Msimbo wa chanzo na sampuli rasmi
- [Nyaraka za Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Mwongozo kamili wa usanidi na matumizi
- [Mfululizo wa Model Mondays](https://aka.ms/model-mondays) - Muhtasari wa modeli za kila wiki na mafunzo

**Jamii & Usaidizi:**
- [Majadiliano ya Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Maswali na majibu ya jamii na maombi ya vipengele
- [Jamii ya Waendelezaji wa Microsoft AI](https://techcommunity.microsoft.com/category/artificialintelligence) - Habari za hivi karibuni na mbinu bora

## Matokeo ya Kujifunza

Baada ya kukamilisha moduli hii, utaweza:

### Ustadi wa Kiufundi
- **Kupeleka na Kusimamia**: Usakinishaji wa Foundry Local katika mazingira ya maendeleo na uzalishaji
- **Kuunganisha Modeli**: Kufanya kazi bila mshono na familia tofauti za modeli kutoka Microsoft, Hugging Face, na vyanzo vya jamii
- **Kujenga Programu**: Kuunda programu za AI tayari kwa uzalishaji zenye vipengele vya hali ya juu na uboreshaji
- **Kuendeleza Mawakala**: Kutekeleza mawakala wa AI wa hali ya juu wenye uunganishaji, uamuzi, na ujumuishaji wa zana

### Uelewa wa Kistratejia
- **Maamuzi ya Miundombinu**: Kufanya chaguo sahihi kati ya upelekaji wa ndani vs wingu
- **Uboreshaji wa Utendaji**: Kuboresha utendaji wa utoaji wa modeli kwenye usanidi tofauti wa vifaa
- **Upanuzi wa Biashara**: Kubuni programu zinazopanuka kutoka kwa prototipu za ndani hadi upelekaji wa biashara
- **Faragha na Usalama**: Kutekeleza suluhisho za AI zinazohifadhi faragha kwa utoaji wa ndani

### Uwezo wa Ubunifu
- **Uundaji wa Haraka**: Kujenga na kujaribu dhana za programu za AI haraka kwa kutumia mifumo yote 10 ya sampuli
- **Muunganisho wa Jamii**: Kufaidika na modeli za chanzo huria na kuchangia kwenye mfumo
- **Mifumo ya Juu**: Kutekeleza mifumo ya AI ya kisasa ikijumuisha RAG, mawakala, na ujumuishaji wa zana
- **Ustadi wa Mfumo**: Muunganisho wa kiwango cha mtaalamu na LangChain, Semantic Kernel, Chainlit, na Electron
- **Upelekaji wa Uzalishaji**: Kupeleka suluhisho za AI zinazopanuka kutoka prototipu za ndani hadi mifumo ya biashara
- **Maendeleo Tayari kwa Teknolojia ya Baadaye**: Kujenga programu tayari kwa teknolojia na mifumo ya AI inayojitokeza

## Kuanza

1. **Usanidi wa Mazingira**: Hakikisha Windows 11 na vifaa vinavyopendekezwa (angalia Mahitaji ya Awali)
2. **Sakinisha Foundry Local**: Fuata Kipindi cha 1 kwa usakinishaji kamili na usanidi
3. **Endesha Sampuli 01**: Anza na muunganisho wa msingi wa REST API ili kuthibitisha usanidi
4. **Endelea na Sampuli**: Kamilisha sampuli 01-10 kwa ustadi wa kina

## Vipimo vya Mafanikio

Fuata maendeleo yako kupitia mifumo yote 10 ya sampuli kamili:

### Kiwango cha Msingi (Sampuli 01-03)
- [ ] Kusakinisha na kusanidi Foundry Local kwa mafanikio
- [ ] Kukamilisha muunganisho wa REST API (Sampuli 01)
- [ ] Kutekeleza muunganisho wa OpenAI SDK (Sampuli 02)
- [ ] Kufanya ugunduzi wa modeli na upimaji (Sampuli 03)

### Kiwango cha Programu (Sampuli 04-06)
- [ ] Kupeleka na kuendesha angalau familia 4 tofauti za modeli
- [ ] Kujenga programu ya mazungumzo ya RAG inayofanya kazi (Sampuli 04)
- [ ] Kuunda mfumo wa uratibu wa mawakala wengi (Sampuli 05)
- [ ] Kutekeleza mfumo wa uelekezaji wa modeli wenye akili (Sampuli 06)

### Kiwango cha Muunganisho wa Juu (Sampuli 07-10)
- [ ] Kujenga mteja wa API tayari kwa uzalishaji (Sampuli 07)
- [ ] Kuendeleza programu ya mazungumzo ya asili ya Windows 11 (Sampuli 08)
- [ ] Kutekeleza mfumo wa mawakala wengi wa hali ya juu (Sampuli 09)
- [ ] Kuunda mfumo wa zana kamili (Sampuli 10)

### Viashiria vya Ustadi
- [ ] Kuendesha mifumo yote 10 bila makosa
- [ ] Kubinafsisha angalau mifumo 3 kwa matumizi maalum
- [ ] Kupeleka mifumo 2+ katika mazingira yanayofanana na uzalishaji
- [ ] Kuchangia maboresho au nyongeza kwenye msimbo wa sampuli
- [ ] Kuunganisha mifumo ya Foundry Local kwenye miradi ya kibinafsi/kitaalamu

## Mwongozo wa Kuanza Haraka - Sampuli Zote 10

### Usanidi wa Mazingira (Inahitajika kwa Sampuli Zote)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Sampuli za Msingi (01-06)

**Sampuli 01: Mwongozo wa Haraka wa REST Chat**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Sampuli 02: Muunganisho wa OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Sampuli 03: Ugunduzi wa Modeli na Upimaji**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Sampuli 04: Programu ya Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Sampuli 05: Uratibu wa Mawakala Wengi**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Sampuli 06: Router ya Modeli-kama-Zana**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b-instruct

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Sampuli za Muunganisho wa Juu (07-10)

**Sampuli 07: Mteja wa API Moja kwa Moja**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Sampuli 08: Programu ya Mazungumzo ya Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Sampuli 09: Mfumo wa Mawakala
Moduli huu unawakilisha maendeleo ya kisasa katika teknolojia ya AI ya ukingo, ukichanganya zana za Microsoft za kiwango cha biashara na urahisi na ubunifu wa mfumo wa wazi. Kwa kufahamu Foundry Local kupitia sampuli 10 za kina, utakuwa katika mstari wa mbele wa maendeleo ya matumizi ya AI.

**Njia Kamili ya Kujifunza:**
- **Msingi** (Sampuli 01-03): Muunganisho wa API na usimamizi wa modeli
- **Matumizi** (Sampuli 04-06): RAG, mawakala, na usambazaji wa akili
- **Ya Juu** (Sampuli 07-10): Miundombinu ya uzalishaji na muunganisho wa biashara

Kwa muunganisho wa Azure OpenAI (Kikao cha 2), angalia faili za README za sampuli husika kwa vigezo vya mazingira vinavyohitajika na mipangilio ya toleo la API.

---

