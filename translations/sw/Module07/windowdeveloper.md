<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T13:58:21+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "sw"
}
-->
# Mwongozo wa Maendeleo ya Windows Edge AI

## Utangulizi

Karibu kwenye Maendeleo ya Windows Edge AI - mwongozo wako wa kina wa kujenga programu za akili zinazotumia nguvu ya AI kwenye kifaa kupitia jukwaa la Windows AI Foundry la Microsoft. Mwongozo huu umeundwa mahsusi kwa watengenezaji wa Windows wanaotaka kuunganisha uwezo wa kisasa wa Edge AI kwenye programu zao huku wakitumia kikamilifu kasi ya vifaa vya Windows.

### Faida ya Windows AI

Windows AI Foundry ni jukwaa lililounganishwa, la kuaminika, na salama linalosaidia mzunguko mzima wa maendeleo ya AI - kutoka kuchagua na kurekebisha modeli hadi kuboresha na kupeleka kwenye CPU, GPU, NPU, na miundombinu ya wingu mseto. Jukwaa hili linapanua maendeleo ya AI kwa kutoa:

- **Urahisi wa Vifaa**: Uwezo wa kupeleka bila shida kwenye vifaa vya AMD, Intel, NVIDIA, na Qualcomm
- **Akili ya Kifaa**: AI inayohifadhi faragha inayofanya kazi kikamilifu kwenye vifaa vya ndani
- **Utendaji Bora**: Modeli zilizoboreshwa kwa usanidi wa vifaa vya Windows
- **Tayari kwa Biashara**: Vipengele vya usalama wa kiwango cha uzalishaji na kufuata kanuni

### Kwa Nini Windows kwa Edge AI?

**Msaada wa Vifaa Vyote**
Windows ML hutoa uboreshaji wa vifaa kiotomatiki katika mfumo mzima wa Windows, kuhakikisha programu zako za AI zinafanya kazi kwa ufanisi bila kujali usanifu wa vifaa vya msingi.

**Mazingira ya AI Yaliyounganishwa**
Injini ya Windows ML iliyojengwa ndani huondoa mahitaji ya usanidi mgumu, ikiruhusu watengenezaji kuzingatia mantiki ya programu badala ya masuala ya miundombinu.

**Copilot+ Uboreshaji wa PC**
API zilizoundwa mahsusi kwa vifaa vya Windows vya kizazi kijacho vilivyo na Vitengo vya Usindikaji wa Neural (NPUs) vinavyotoa utendaji wa kipekee kwa kila watt.

**Ecosystem ya Watengenezaji**
Zana tajiri ikiwa ni pamoja na ujumuishaji wa Visual Studio, nyaraka za kina, na programu za mfano zinazoharakisha mzunguko wa maendeleo.

## Malengo ya Kujifunza

Kwa kukamilisha mwongozo huu wa maendeleo ya Windows Edge AI, utakuwa na ujuzi muhimu wa kujenga programu za AI tayari kwa uzalishaji kwenye jukwaa la Windows.

### Ujuzi wa Kiufundi wa Msingi

**Ustadi wa Windows AI Foundry**
- Elewa usanifu na vipengele vya jukwaa la Windows AI Foundry
- Elekeza mzunguko mzima wa maendeleo ya AI ndani ya mfumo wa Windows
- Tekeleza mbinu bora za usalama kwa programu za AI kwenye kifaa
- Boreshaji programu kwa usanidi tofauti wa vifaa vya Windows

**Ujuzi wa Ujumuishaji wa API**
- Elewa API za Windows AI kwa programu za maandishi, maono, na multimodal
- Tekeleza ujumuishaji wa modeli ya lugha ya Phi Silica kwa kizazi cha maandishi na uamuzi
- Peleka uwezo wa maono ya kompyuta kwa kutumia API za usindikaji wa picha zilizojengwa ndani
- Rekebisha modeli zilizofunzwa awali kwa kutumia mbinu za LoRA (Low-Rank Adaptation)

**Utekelezaji wa Foundry Local**
- Vinjari, tathmini, na peleka modeli za lugha za chanzo huria kwa kutumia Foundry Local CLI
- Elewa uboreshaji wa modeli na upunguzaji kwa utekelezaji wa ndani
- Tekeleza uwezo wa AI nje ya mtandao unaofanya kazi bila muunganisho wa intaneti
- Dhibiti mzunguko wa maisha ya modeli na masasisho katika mazingira ya uzalishaji

**Utekelezaji wa Windows ML**
- Leta modeli za ONNX zilizobinafsishwa kwenye programu za Windows kwa kutumia Windows ML
- Tumia kasi ya vifaa kiotomatiki kwenye usanifu wa CPU, GPU, na NPU
- Tekeleza utabiri wa wakati halisi kwa matumizi bora ya rasilimali
- Buni programu za AI zinazoweza kupanuka kwa kategoria mbalimbali za vifaa vya Windows

### Ujuzi wa Maendeleo ya Programu

**Maendeleo ya Windows ya Msalaba**
- Jenga programu zinazotumia AI kwa kutumia .NET MAUI kwa utekelezaji wa Windows wa ulimwengu
- Unganisha uwezo wa AI kwenye Win32, UWP, na Programu za Wavuti Zinazoendelea
- Tekeleza miundo ya UI inayojibika inayobadilika kulingana na hali za usindikaji wa AI
- Shughulikia operesheni za AI zisizo za wakati mmoja kwa mifumo sahihi ya uzoefu wa mtumiaji

**Uboreshaji wa Utendaji**
- Profaili na boresha utendaji wa utabiri wa AI katika usanidi tofauti wa vifaa
- Tekeleza usimamizi mzuri wa kumbukumbu kwa modeli kubwa za lugha
- Buni programu zinazopungua kwa neema kulingana na uwezo wa vifaa vilivyopo
- Tumia mikakati ya kuhifadhi kwa operesheni za AI zinazotumika mara kwa mara

**Uwezo wa Uzalishaji**
- Tekeleza utunzaji wa makosa wa kina na mifumo ya kurudi nyuma
- Buni telemetry na ufuatiliaji wa utendaji wa programu za AI
- Tumia mbinu bora za usalama kwa uhifadhi wa modeli za AI za ndani na utekelezaji
- Panga mikakati ya utekelezaji kwa programu za biashara na watumiaji

### Uelewa wa Kibiashara na Mkakati

**Usanifu wa Programu za AI**
- Buni usanifu mseto unaoboreshwa kati ya usindikaji wa AI wa ndani na wa wingu
- Tathmini faida na hasara kati ya ukubwa wa modeli, usahihi, na kasi ya utabiri
- Panga usanifu wa mtiririko wa data unaohifadhi faragha huku ukiruhusu akili
- Tekeleza suluhisho za AI za gharama nafuu zinazopanuka kulingana na mahitaji ya watumiaji

**Nafasi ya Soko**
- Elewa faida za ushindani za programu za AI za asili za Windows
- Tambua matumizi ambapo AI kwenye kifaa inatoa uzoefu bora wa mtumiaji
- Buni mikakati ya kuingia sokoni kwa programu za Windows zilizoimarishwa na AI
- Weka programu ili kutumia faida za mfumo wa Windows

## Sampuli za Windows App SDK AI

Windows App SDK hutoa sampuli za kina zinazoonyesha ujumuishaji wa AI katika mifumo mbalimbali na hali za utekelezaji. Sampuli hizi ni marejeleo muhimu kwa kuelewa mifumo ya maendeleo ya Windows AI.

### Sampuli za Windows AI Foundry

| Sampuli | Mfumo | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Ujumuishaji wa API za Windows AI | Programu kamili ya WinUI inayoonyesha API za Windows AI, uboreshaji wa ARM64, utekelezaji wa kifurushi |

**Teknolojia Muhimu:**
- API za Windows AI
- Mfumo wa WinUI 3
- Uboreshaji wa jukwaa la ARM64
- Utangamano wa Copilot+ PC
- Utekelezaji wa programu ya kifurushi

**Mahitaji ya Awali:**
- Windows 11 na Copilot+ PC inapendekezwa
- Visual Studio 2022
- Usanidi wa ujenzi wa ARM64
- Windows App SDK 1.8.1+

### Sampuli za Windows ML

#### Sampuli za C++

| Sampuli | Aina | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Programu ya Console | Windows ML ya Msingi | Ugunduzi wa EP, chaguo za mstari wa amri, usanidi wa modeli |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Programu ya Console | Utekelezaji wa Mfumo | Runtime ya pamoja, alama ndogo ya utekelezaji |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Programu ya Console | Utekelezaji wa Kujitegemea | Utekelezaji wa pekee, hakuna utegemezi wa runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Matumizi ya Maktaba | WindowsML katika maktaba ya pamoja, usimamizi wa kumbukumbu |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Mafunzo ya ResNet | Ubadilishaji wa modeli, usanidi wa EP, Mafunzo ya Build 2025 |

#### Sampuli za C#

**Programu za Console**

| Sampuli | Aina | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Programu ya Console | Ujumuishaji wa Msingi wa C# | Matumizi ya msaidizi wa pamoja, interface ya mstari wa amri |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Mafunzo ya ResNet | Ubadilishaji wa modeli, usanidi wa EP, Mafunzo ya Build 2025 |

**Programu za GUI**

| Sampuli | Mfumo | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI ya Desktop | Uainishaji wa picha na interface ya WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI ya Kawaida | Uainishaji wa picha na Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI ya Kisasa | Uainishaji wa picha na interface ya WinUI 3 |

#### Sampuli za Python

| Sampuli | Lugha | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Uainishaji wa Picha | Viunganishi vya WinML Python, usindikaji wa picha kwa kundi |

### Mahitaji ya Awali ya Sampuli

**Mahitaji ya Mfumo:**
- Kompyuta ya Windows 11 inayoendesha toleo la 24H2 (build 26100) au zaidi
- Visual Studio 2022 na mizigo ya C++ na .NET
- Windows App SDK 1.8.1 au zaidi
- Python 3.10-3.13 kwa sampuli za Python kwenye vifaa vya x64 na ARM64

**Mahitaji Mahususi ya Windows AI Foundry:**
- Copilot+ PC inapendekezwa kwa utendaji bora
- Usanidi wa ujenzi wa ARM64 kwa sampuli za Windows AI
- Utambulisho wa kifurushi unahitajika (programu zisizopakiwa hazihitajiwi tena)

### Mtiririko wa Kawaida wa Sampuli

Sampuli nyingi za Windows ML hufuata muundo huu wa kawaida:

1. **Anzisha Mazingira** - Unda mazingira ya ONNX Runtime
2. **Sajili Watoa Huduma za Utekelezaji** - Gundua na sajili kasi za vifaa vilivyopo (CPU, GPU, NPU)
3. **Pakia Modeli** - Pakia modeli ya ONNX, kwa hiari sanidi kwa vifaa lengwa
4. **Tayarisha Ingizo** - Badilisha picha/data kuwa muundo wa ingizo wa modeli
5. **Fanya Utabiri** - Tekeleza modeli na pata utabiri
6. **Chakata Matokeo** - Tumia softmax na onyesha utabiri wa juu

### Faili za Modeli Zinazotumika

| Modeli | Kusudi | Imejumuishwa | Maelezo |
|-------|---------|----------|-------|
| SqueezeNet | Uainishaji wa picha nyepesi | ✅ Imejumuishwa | Imefunzwa awali, tayari kutumika |
| ResNet-50 | Uainishaji wa picha wa usahihi wa juu | ❌ Inahitaji ubadilishaji | Tumia [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) kwa ubadilishaji |

### Msaada wa Vifaa

Sampuli zote hugundua na kutumia vifaa vilivyopo kiotomatiki:
- **CPU** - Msaada wa ulimwengu wote katika vifaa vyote vya Windows
- **GPU** - Ugunduzi wa kiotomatiki na uboreshaji kwa vifaa vya picha vilivyopo
- **NPU** - Inatumia Vitengo vya Usindikaji wa Neural kwenye vifaa vinavyoungwa mkono (Copilot+ PCs)

## Vipengele vya Jukwaa la Windows AI Foundry

### 1. API za Windows AI

API za Windows AI hutoa uwezo wa AI tayari kutumika unaotumia modeli kwenye kifaa, zilizoboreshwa kwa ufanisi na utendaji kwenye vifaa vya Copilot+ PC bila mahitaji makubwa ya usanidi.

#### Makundi ya API Muhimu

**Modeli ya Lugha ya Phi Silica**
- Modeli ndogo lakini yenye nguvu ya lugha kwa kizazi cha maandishi na uamuzi
- Imeboreshwa kwa utabiri wa wakati halisi na matumizi madogo ya nguvu
- Msaada wa kurekebisha kwa kutumia mbinu za LoRA
- Ujumuishaji na utafutaji wa semantic wa Windows na upatikanaji wa maarifa

**API za Maono ya Kompyuta**
- **Utambuzi wa Maandishi (OCR)**: Toa maandishi kutoka kwa picha kwa usahihi wa juu
- **Azimio la Picha ya Juu**: Panua picha kwa kutumia modeli za AI za ndani
- **Ugawaji wa Picha**: Tambua na tenga vitu maalum kwenye picha
- **Maelezo ya Picha**: Tengeneza maelezo ya maandishi ya kina kwa maudhui ya kuona
- **Kuondoa Vitu**: Ondoa vitu visivyohitajika kutoka kwa picha kwa kutumia uchoraji wa AI

**Uwezo wa Multimodal**
- **Ujumuishaji wa Maono-Lugha**: Changanya uelewa wa maandishi na picha
- **Utafutaji wa Semantic**: Ruhusu maswali ya lugha asilia katika maudhui ya multimedia
- **Upatikanaji wa Maarifa**: Jenga uzoefu wa utafutaji wa akili kwa data ya ndani

### 2. Foundry Local

Foundry Local huwapa watengenezaji ufikiaji wa haraka wa modeli za lugha za chanzo huria tayari kutumika kwenye Windows Silicon, ikitoa uwezo wa kuvinjari, kujaribu, kuingiliana, na kupeleka modeli kwenye programu za ndani.

#### Sampuli za Programu za Foundry Local

Hifadhi ya [Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) hutoa sampuli za kina katika lugha na mifumo mbalimbali ya programu, ikionyesha mifumo tofauti ya ujumuishaji na matumizi.

| Sampuli | Lugha/Mfumo | Eneo la Kuzingatia | Vipengele Muhimu |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Utekelezaji wa RAG | Ujumuishaji wa Semantic Kernel, hifadhi ya vekta ya Qdrant, embeddings za JINA, uingizaji wa hati, gumzo la kutiririsha |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Programu ya Gumzo ya Desktop | Gumzo la msalaba-jukwaa, kubadilisha modeli za ndani/wingu, ujumuishaji wa OpenAI SDK, kutiririsha kwa wakati halisi |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Ujumuishaji wa Msingi | Matumizi rahisi ya SDK, usanidi wa modeli, utendaji wa gumzo la msingi |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Ujumuishaji wa Msingi | Matumizi ya SDK ya Python, majibu ya kutiririsha, API inayolingana na OpenAI |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Ujumuishaji wa Mifumo | Matumizi ya SDK ya kiwango cha chini, operesheni za async, mteja wa HTTP wa reqwest |

#### Makundi ya Sampuli kwa Matumizi

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Utekelezaji kamili wa RAG kwa kutumia Semantic Kernel, hifadhi ya vekta ya Qdrant,
- **Vipengele**: Uchaguzi wa modeli, majibu ya mtiririko, kushughulikia makosa, usambazaji wa majukwaa mbalimbali  
- **Muundo**: Mchakato mkuu wa Electron, mawasiliano ya IPC, maandiko ya awali salama  

**Mifano ya Ujumuishaji wa SDK**  
- **JavaScript (Node.js)**: Mwingiliano wa msingi wa modeli na majibu ya mtiririko  
- **Python**: Matumizi ya API inayolingana na OpenAI kwa mtiririko wa async  
- **Rust**: Ujumuishaji wa kiwango cha chini kwa kutumia reqwest na tokio kwa operesheni za async  

#### Mahitaji ya Awali kwa Sampuli za Foundry Local  

**Mahitaji ya Mfumo:**  
- Windows 11 ikiwa na Foundry Local imewekwa  
- Node.js v16+ kwa sampuli za JavaScript/Electron  
- .NET 8.0+ kwa sampuli za C#  
- Python 3.10+ kwa sampuli za Python  
- Rust 1.70+ kwa sampuli za Rust  

**Usakinishaji:**  
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```
  

#### Usanidi Maalum wa Sampuli  

**Sampuli ya dotNET RAG:**  
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```
  
**Sampuli ya Electron Chat:**  
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```
  
**Sampuli za JavaScript/Python/Rust:**  
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```
  

#### Vipengele Muhimu  

**Katalogi ya Modeli**  
- Mkusanyiko wa kina wa modeli za chanzo huria zilizoboreshwa  
- Modeli zilizoboreshwa kwa CPU, GPU, na NPU kwa usambazaji wa haraka  
- Msaada kwa familia maarufu za modeli kama Llama, Mistral, Phi, na modeli maalum za sekta  

**Ujumuishaji wa CLI**  
- Kiolesura cha mstari wa amri kwa usimamizi wa modeli na usambazaji  
- Michakato ya kiotomatiki ya uboreshaji na upunguzaji  
- Ujumuishaji na mazingira maarufu ya maendeleo na mifumo ya CI/CD  

**Usambazaji wa Kifaa cha Ndani**  
- Operesheni kamili ya nje ya mtandao bila utegemezi wa wingu  
- Msaada kwa miundo maalum ya modeli na usanidi  
- Huduma ya modeli yenye ufanisi na uboreshaji wa kiotomatiki wa vifaa  

### 3. Windows ML  

Windows ML inahudumu kama jukwaa kuu la AI na mazingira ya utekelezaji wa inferensi kwenye Windows, ikiruhusu watengenezaji kusambaza modeli maalum kwa ufanisi katika mfumo mpana wa vifaa vya Windows.  

#### Faida za Muundo  

**Msaada wa Vifaa vya Kila Mahali**  
- Uboreshaji wa kiotomatiki kwa silikoni za AMD, Intel, NVIDIA, na Qualcomm  
- Msaada kwa utekelezaji wa CPU, GPU, na NPU na ubadilishaji wa uwazi  
- Abstrakta ya vifaa inayotoa kazi ya uboreshaji maalum ya jukwaa  

**Uwezo wa Modeli**  
- Msaada kwa muundo wa modeli wa ONNX na ubadilishaji wa kiotomatiki kutoka mifumo maarufu  
- Usambazaji wa modeli maalum na utendaji wa kiwango cha uzalishaji  
- Ujumuishaji na miundo ya programu za Windows zilizopo  

**Ujumuishaji wa Biashara**  
- Inalingana na mifumo ya usalama na kufuata ya Windows  
- Msaada kwa zana za usambazaji na usimamizi wa biashara  
- Ujumuishaji na mifumo ya usimamizi na ufuatiliaji wa vifaa vya Windows  

## Mtiririko wa Maendeleo  

### Awamu ya 1: Usanidi wa Mazingira na Zana  

**Maandalizi ya Mazingira ya Maendeleo**  
1. Sakinisha Visual Studio 2022 ikiwa na mzigo wa C++ na .NET  
2. Sakinisha Windows App SDK 1.8.1 au toleo jipya zaidi  
3. Sanidi zana za CLI za Windows AI Foundry  
4. Sanidi kiendelezi cha AI Toolkit kwa Visual Studio Code  
5. Weka zana za ufuatiliaji wa utendaji na uwasifu  
6. Hakikisha usanidi wa ARM64 kwa uboreshaji wa Copilot+ PC  

**Usanidi wa Hifadhi ya Sampuli**  
1. Clone hifadhi ya [Windows App SDK Samples](https://github.com/microsoft/WindowsAppSDK-Samples)  
2. Nenda kwenye `Samples/WindowsAIFoundry/cs-winui` kwa mifano ya API ya Windows AI  
3. Nenda kwenye `Samples/WindowsML` kwa mifano kamili ya Windows ML  
4. Tathmini [mahitaji ya ujenzi](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) kwa majukwaa lengwa  

**Uchunguzi wa AI Dev Gallery**  
- Chunguza programu za sampuli na utekelezaji wa marejeleo  
- Jaribu API za Windows AI kwa maonyesho ya mwingiliano  
- Tathmini msimbo wa chanzo kwa mbinu bora na mifumo  
- Tambua sampuli zinazofaa kwa matumizi yako maalum  

### Awamu ya 2: Uchaguzi wa Modeli na Ujumuishaji  

**Uchambuzi wa Mahitaji**  
- Tambua mahitaji ya kiutendaji kwa uwezo wa AI  
- Weka vikwazo vya utendaji na malengo ya uboreshaji  
- Tathmini mahitaji ya faragha na usalama  
- Panga muundo wa usambazaji na mikakati ya kupanua  

**Tathmini ya Modeli**  
- Tumia Foundry Local kujaribu modeli za chanzo huria kwa matumizi yako  
- Pima API za Windows AI dhidi ya mahitaji ya modeli maalum  
- Tathmini faida na hasara kati ya ukubwa wa modeli, usahihi, na kasi ya inferensi  
- Tengeneza mbinu za ujumuishaji kwa modeli zilizochaguliwa  

### Awamu ya 3: Maendeleo ya Programu  

**Ujumuishaji wa Msingi**  
- Tekeleza ujumuishaji wa API za Windows AI kwa kushughulikia makosa ipasavyo  
- Buni miolesura ya mtumiaji inayokidhi mtiririko wa usindikaji wa AI  
- Tekeleza mikakati ya akiba na uboreshaji kwa inferensi ya modeli  
- Ongeza telemetry na ufuatiliaji kwa utendaji wa operesheni za AI  

**Upimaji na Uthibitishaji**  
- Jaribu programu kwenye usanidi tofauti wa vifaa vya Windows  
- Thibitisha vipimo vya utendaji chini ya hali mbalimbali za mzigo  
- Tekeleza upimaji wa kiotomatiki kwa uaminifu wa utendaji wa AI  
- Fanya upimaji wa uzoefu wa mtumiaji na vipengele vilivyoboreshwa na AI  

### Awamu ya 4: Uboreshaji na Usambazaji  

**Uboreshaji wa Utendaji**  
- Wasifu utendaji wa programu kwenye usanidi lengwa wa vifaa  
- Boresha matumizi ya kumbukumbu na mikakati ya kupakia modeli  
- Tekeleza tabia ya adaptive kulingana na uwezo wa vifaa vilivyopo  
- Rekebisha uzoefu wa mtumiaji kwa hali tofauti za utendaji  

**Usambazaji wa Uzalishaji**  
- Funga programu ikiwa na utegemezi sahihi wa modeli za AI  
- Tekeleza mifumo ya masasisho kwa modeli na mantiki ya programu  
- Sanidi ufuatiliaji na uchanganuzi kwa mazingira ya uzalishaji  
- Panga mikakati ya usambazaji kwa biashara na watumiaji wa kawaida  

## Mifano ya Utekelezaji wa Kivitendo  

### Mfano 1: Programu ya Usindikaji wa Nyaraka za Kijasusi  

Tengeneza programu ya Windows inayosindika nyaraka kwa kutumia uwezo mbalimbali wa AI:  

**Teknolojia Zilizotumika:**  
- Phi Silica kwa muhtasari wa nyaraka na kujibu maswali  
- API za OCR kwa uchimbaji wa maandishi kutoka nyaraka zilizochanganuliwa  
- API za Maelezo ya Picha kwa uchambuzi wa chati na michoro  
- Modeli maalum za ONNX kwa uainishaji wa nyaraka  

**Mbinu ya Utekelezaji:**  
- Buni muundo wa modular wenye vipengele vya AI vinavyoweza kuunganishwa  
- Tekeleza usindikaji wa async kwa vikundi vikubwa vya nyaraka  
- Ongeza viashiria vya maendeleo na msaada wa kughairi operesheni za muda mrefu  
- Jumuisha uwezo wa nje ya mtandao kwa usindikaji wa nyaraka nyeti  

### Mfano 2: Mfumo wa Usimamizi wa Hesabu ya Rejareja  

Unda mfumo wa hesabu unaotumia AI kwa programu za rejareja:  

**Teknolojia Zilizotumika:**  
- Ugawaji wa Picha kwa utambuzi wa bidhaa  
- Modeli za maono maalum kwa uainishaji wa chapa na kategoria  
- Usambazaji wa Foundry Local wa modeli za lugha maalum za rejareja  
- Ujumuishaji na mifumo ya POS na hesabu iliyopo  

**Mbinu ya Utekelezaji:**  
- Jenga ujumuishaji wa kamera kwa uchanganuzi wa bidhaa wa wakati halisi  
- Tekeleza utambuzi wa barcode na bidhaa kwa kutumia maono ya kuona  
- Ongeza maswali ya hesabu ya lugha asilia kwa kutumia modeli za lugha za ndani  
- Buni muundo unaoweza kupanuka kwa usambazaji wa maduka mengi  

### Mfano 3: Msaidizi wa Uandishi wa Nyaraka za Huduma za Afya  

Tengeneza zana ya uandishi wa nyaraka za huduma za afya inayohifadhi faragha:  

**Teknolojia Zilizotumika:**  
- Phi Silica kwa kizazi cha maelezo ya matibabu na msaada wa maamuzi ya kliniki  
- OCR kwa kubadilisha rekodi za matibabu zilizoandikwa kwa mkono kuwa za kidijitali  
- Modeli maalum za lugha za matibabu zinazotolewa kupitia Windows ML  
- Hifadhi ya vector ya ndani kwa urejeshaji wa maarifa ya matibabu  

**Mbinu ya Utekelezaji:**  
- Hakikisha operesheni kamili ya nje ya mtandao kwa faragha ya mgonjwa  
- Tekeleza uthibitishaji wa istilahi za matibabu na mapendekezo  
- Ongeza ukaguzi wa kumbukumbu kwa kufuata kanuni  
- Buni ujumuishaji na mifumo ya rekodi za afya za kielektroniki iliyopo  

## Mikakati ya Uboreshaji wa Utendaji  

### Maendeleo Yanayozingatia Vifaa  

**Uboreshaji wa NPU**  
- Buni programu ili kutumia uwezo wa NPU kwenye PC za Copilot+  
- Tekeleza kurudi kwa neema kwa GPU/CPU kwenye vifaa visivyo na NPU  
- Boresha miundo ya modeli kwa kasi maalum ya NPU  
- Fuatilia matumizi ya NPU na sifa za joto  

**Usimamizi wa Kumbukumbu**  
- Tekeleza mikakati ya kupakia na kuhifadhi modeli kwa ufanisi  
- Tumia ramani ya kumbukumbu kwa modeli kubwa ili kupunguza muda wa kuanza  
- Buni programu zinazojali kumbukumbu kwa vifaa vyenye rasilimali ndogo  
- Tekeleza upunguzaji wa modeli kwa uboreshaji wa kumbukumbu  

**Ufanisi wa Betri**  
- Boresha operesheni za AI kwa matumizi ya nguvu ya chini  
- Tekeleza usindikaji wa adaptive kulingana na hali ya betri  
- Buni usindikaji wa nyuma wa ufanisi kwa operesheni za AI zinazoendelea  
- Tumia zana za uwasifu wa nguvu ili kuboresha matumizi ya nishati  

### Mawazo ya Kupanuka  

**Multi-Threading**  
- Buni operesheni za AI salama kwa nyuzi kwa usindikaji wa pamoja  
- Tekeleza usambazaji wa kazi kwa ufanisi kwenye cores zilizopo  
- Tumia mifumo ya async/await kwa operesheni za AI zisizozuia  
- Panga uboreshaji wa pool ya nyuzi kwa usanidi tofauti wa vifaa  

**Mikakati ya Akiba**  
- Tekeleza akiba ya akili kwa operesheni za AI zinazotumika mara kwa mara  
- Buni mikakati ya kubatilisha akiba kwa masasisho ya modeli  
- Tumia akiba ya kudumu kwa operesheni za usindikaji wa awali ghali  
- Tekeleza akiba ya kusambazwa kwa hali za watumiaji wengi  

## Mbinu Bora za Usalama na Faragha  

### Ulinzi wa Data  

**Usindikaji wa Ndani**  
- Hakikisha data nyeti haiondoki kwenye kifaa cha ndani  
- Tekeleza hifadhi salama kwa modeli za AI na data ya muda mfupi  
- Tumia vipengele vya usalama vya Windows kwa sandboxing ya programu  
- Tumia usimbaji fiche kwa modeli zilizohifadhiwa na matokeo ya usindikaji wa kati  

**Usalama wa Modeli**  
- Thibitisha uadilifu wa modeli kabla ya kupakia na utekelezaji  
- Tekeleza mifumo salama ya masasisho ya modeli  
- Tumia modeli zilizotiwa saini ili kuzuia uharibifu  
- Tekeleza udhibiti wa ufikiaji kwa faili za modeli na usanidi  

### Mawazo ya Ufuataji  

**Ulinganifu wa Kanuni**  
- Buni programu zinazokidhi mahitaji ya GDPR, HIPAA, na kanuni nyingine  
- Tekeleza ukaguzi wa kumbukumbu kwa michakato ya maamuzi ya AI  
- Toa vipengele vya uwazi kwa matokeo yanayotokana na AI  
- Ruhusu udhibiti wa mtumiaji juu ya usindikaji wa data ya AI  

**Usalama wa Biashara**  
- Jumuisha na sera za usalama za biashara za Windows  
- Msaada wa usambazaji unaosimamiwa kupitia zana za usimamizi wa biashara  
- Tekeleza udhibiti wa ufikiaji kulingana na majukumu kwa vipengele vya AI  
- Toa udhibiti wa kiutawala kwa utendaji wa AI  

## Utatuzi wa Matatizo na Ufuatiliaji  

### Changamoto za Kawaida za Maendeleo  

**Masuala ya Usanidi wa Ujenzi**  
- Hakikisha usanidi wa jukwaa la ARM64 kwa sampuli za API za Windows AI  
- Thibitisha utangamano wa toleo la Windows App SDK (1.8.1+ inahitajika)  
- Angalia kwamba kitambulisho cha kifurushi kimewekwa ipasavyo (kinahitajika kwa API za Windows AI)  
- Thibitisha kwamba zana za ujenzi zinaunga mkono toleo lengwa la mfumo  

**Masuala ya Kupakia Modeli**  
- Thibitisha utangamano wa modeli za ONNX na Windows ML  
- Angalia uadilifu wa faili za modeli na mahitaji ya muundo  
- Thibitisha mahitaji ya uwezo wa vifaa kwa modeli maalum  
- Fuatilia masuala ya ugawaji wa kumbukumbu wakati wa kupakia modeli  
- Hakikisha usajili wa mtoa huduma wa utekelezaji kwa kasi ya vifaa  

**Mawazo ya Hali ya Usambazaji**  
- **Hali ya Kujitegemea**: Inasaidiwa kikamilifu na ukubwa mkubwa wa usambazaji  
- **Hali Inayotegemea Mfumo**: Alama ndogo lakini inahitaji mazingira ya pamoja  
- **Programu Zisizopakiwa**: Hazisaidiwi tena kwa API za Windows AI  
- Tumia `dotnet run -p:Platform=ARM64 -p:SelfContained=true` kwa usambazaji wa ARM64 wa kujitegemea  

**Matatizo ya Utendaji**  
- Wasifu utendaji wa programu kwenye usanidi tofauti wa vifaa  
- Tambua vizuizi katika mifumo ya usindikaji wa AI  
- Boresha operesheni za usindikaji wa data kabla na baada  
- Tekeleza ufuatiliaji wa utendaji na tahadhari  

**Ugumu wa Ujumuishaji**  
- Fuatilia masuala ya ujumuishaji wa API kwa kushughulikia makosa ipasavyo  
- Thibitisha miundo ya data ya pembejeo na mahitaji ya usindikaji wa awali  
- Jaribu hali za ukingo na hali za makosa kwa kina  
- Tekeleza ukaguzi wa kina kwa utatuzi wa masuala ya uzalishaji  

### Zana na Mbinu za Ufuatiliaji  

**Ujumuishaji wa Visual Studio**  
- Tumia debugger ya AI Toolkit kwa uchambuzi wa utekelezaji wa modeli  
- Tekeleza uwasifu wa utendaji kwa operesheni za AI  
- Fuatilia operesheni za AI za async kwa kushughulikia vizuizi ipasavyo  
- Tumia zana za uwasifu wa kumbukumbu kwa uboreshaji  

**Zana za Windows AI Foundry**  
- Tumia CLI ya Foundry Local kwa upimaji na uthibitishaji wa modeli  
- Tumia zana za upimaji wa API za Windows AI kwa uthibitishaji wa ujumuishaji  
- Tekeleza ukaguzi maalum kwa ufuatiliaji wa operesheni za AI  
- Unda upimaji wa kiotomatiki kwa uaminifu wa utendaji wa AI  

## Kuandaa Programu Zako kwa Teknolojia za Baadaye  

### Teknolojia Zinazochipuka  

**Vifaa vya Kizazi Kijacho**  
- Buni programu ili kutumia uwezo wa NPU wa baadaye  
- Panga kwa ukubwa wa modeli ulioongezeka na ugumu  
- Tekeleza miundo ya adaptive kwa vifaa vinavyoendelea  
- Fikiria algoriti zinazofaa kwa quantum kwa utangamano wa baadaye  

**Uwezo wa AI wa Juu**  
- Jiandae kwa ujumuishaji wa AI wa multimodal katika aina zaidi za data  
- Panga kwa ushirikiano wa AI wa wakati halisi kati ya vifaa v
- [Hifadhi ya Sampuli za Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Zana za Maendeleo
- [Zana ya AI kwa Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Sampuli za Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Zana za Kubadilisha Miundo](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Usaidizi wa Kiufundi
- [Nyaraka za Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Nyaraka za ONNX Runtime](https://onnxruntime.ai/docs/)
- [Nyaraka za Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Ripoti Masuala - Sampuli za Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Jamii na Usaidizi
- [Jamii ya Watengenezaji wa Windows](https://developer.microsoft.com/en-us/windows/)
- [Blogu ya Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Mafunzo ya AI ya Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Mwongozo huu umeundwa kuendana na maendeleo ya haraka ya mfumo wa Windows AI. Sasisho za mara kwa mara huhakikisha ulinganifu na uwezo wa hivi karibuni wa jukwaa na mbinu bora za maendeleo.*

[08. Kufanya Kazi na Microsoft Foundry Local - Zana Kamili ya Watengenezaji](../Module08/README.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.