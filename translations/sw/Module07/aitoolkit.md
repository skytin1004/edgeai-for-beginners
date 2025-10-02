<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T13:54:37+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "sw"
}
-->
# AI Toolkit kwa Visual Studio Code - Mwongozo wa Maendeleo ya Edge AI

## Utangulizi

Karibu kwenye mwongozo wa kina wa kutumia AI Toolkit kwa Visual Studio Code katika maendeleo ya Edge AI. Kadri akili bandia inavyohama kutoka kwa kompyuta za wingu zilizojikita hadi vifaa vya ukingo vilivyotawanyika, watengenezaji wanahitaji zana zenye nguvu na zilizounganishwa ambazo zinaweza kushughulikia changamoto za kipekee za usambazaji wa ukingo - kuanzia vikwazo vya rasilimali hadi mahitaji ya kufanya kazi bila mtandao.

AI Toolkit kwa Visual Studio Code inaziba pengo hili kwa kutoa mazingira kamili ya maendeleo yaliyoundwa mahsusi kwa ajili ya kujenga, kujaribu, na kuboresha programu za AI zinazofanya kazi kwa ufanisi kwenye vifaa vya ukingo. Ikiwa unajenga kwa ajili ya sensa za IoT, vifaa vya mkononi, mifumo iliyojengwa, au seva za ukingo, zana hii inarahisisha mtiririko wako mzima wa maendeleo ndani ya mazingira ya kawaida ya VS Code.

Mwongozo huu utakuelekeza kupitia dhana muhimu, zana, na mbinu bora za kutumia AI Toolkit katika miradi yako ya Edge AI, kuanzia uteuzi wa modeli ya awali hadi usambazaji wa uzalishaji.

## Muhtasari

AI Toolkit kwa Visual Studio Code ni kiendelezo chenye nguvu kinachorahisisha maendeleo ya mawakala na uundaji wa programu za AI. Zana hii inatoa uwezo wa kina wa kuchunguza, kutathmini, na kusambaza modeli za AI kutoka kwa watoa huduma mbalimbali—ikiwa ni pamoja na Anthropic, OpenAI, GitHub, Google—wakati ikisaidia utekelezaji wa modeli za ndani kwa kutumia ONNX na Ollama.

Kinachotofautisha AI Toolkit ni mbinu yake ya kina kwa mzunguko mzima wa maendeleo ya AI. Tofauti na zana za jadi za maendeleo ya AI zinazolenga vipengele vya pekee, AI Toolkit inatoa mazingira yaliyounganishwa yanayojumuisha ugunduzi wa modeli, majaribio, maendeleo ya mawakala, tathmini, na usambazaji—yote ndani ya mazingira ya kawaida ya VS Code.

Jukwaa hili limeundwa mahsusi kwa ajili ya prototyping ya haraka na usambazaji wa uzalishaji, na vipengele kama kizazi cha maelekezo, vianzilishi vya haraka, ujumuishaji wa zana za MCP (Model Context Protocol), na uwezo wa tathmini wa kina. Kwa maendeleo ya Edge AI, hii inamaanisha unaweza kuendeleza, kujaribu, na kuboresha programu za AI kwa hali za usambazaji wa ukingo kwa ufanisi huku ukidumisha mtiririko mzima wa maendeleo ndani ya VS Code.

## Malengo ya Kujifunza

Mwisho wa mwongozo huu, utaweza:

### Ujuzi wa Msingi
- **Kusakinisha na kusanidi** AI Toolkit kwa Visual Studio Code kwa mtiririko wa kazi wa maendeleo ya Edge AI
- **Kuelekeza na kutumia** kiolesura cha AI Toolkit, ikiwa ni pamoja na Model Catalog, Playground, na Agent Builder
- **Kuchagua na kutathmini** modeli za AI zinazofaa kwa usambazaji wa ukingo kulingana na utendaji na vikwazo vya rasilimali
- **Kubadilisha na kuboresha** modeli kwa kutumia muundo wa ONNX na mbinu za quantization kwa vifaa vya ukingo

### Ujuzi wa Maendeleo ya Edge AI
- **Kubuni na kutekeleza** programu za Edge AI kwa kutumia mazingira ya maendeleo yaliyounganishwa
- **Kufanya majaribio ya modeli** katika hali zinazofanana na ukingo kwa kutumia inference ya ndani na ufuatiliaji wa rasilimali
- **Kuunda na kubinafsisha** mawakala wa AI walioboreshwa kwa hali za usambazaji wa ukingo
- **Kutathmini utendaji wa modeli** kwa kutumia vipimo vinavyohusiana na kompyuta za ukingo (latency, matumizi ya kumbukumbu, usahihi)

### Uboreshaji na Usambazaji
- **Kutumia mbinu za quantization na pruning** kupunguza ukubwa wa modeli huku ukidumisha utendaji unaokubalika
- **Kuboresha modeli** kwa majukwaa maalum ya vifaa vya ukingo ikiwa ni pamoja na CPU, GPU, na NPU
- **Kutekeleza mbinu bora** za maendeleo ya Edge AI ikiwa ni pamoja na usimamizi wa rasilimali na mikakati ya kurudi nyuma
- **Kuandaa modeli na programu** kwa usambazaji wa uzalishaji kwenye vifaa vya ukingo

### Dhana za Juu za Edge AI
- **Kuunganisha na mifumo ya Edge AI** ikiwa ni pamoja na ONNX Runtime, Windows ML, na TensorFlow Lite
- **Kutekeleza usanifu wa modeli nyingi** na hali za kujifunza kwa pamoja kwa mazingira ya ukingo
- **Kutatua masuala ya kawaida ya Edge AI** ikiwa ni pamoja na vikwazo vya kumbukumbu, kasi ya inference, na utangamano wa vifaa
- **Kubuni mikakati ya ufuatiliaji na ukaguzi** kwa programu za Edge AI katika uzalishaji

### Matumizi ya Kivitendo
- **Kujenga suluhisho za Edge AI za mwisho hadi mwisho** kuanzia uteuzi wa modeli hadi usambazaji
- **Kuonyesha umahiri** katika mtiririko wa kazi wa maendeleo maalum ya ukingo na mbinu za uboreshaji
- **Kutumia dhana zilizojifunza** kwa hali halisi za matumizi ya Edge AI ikiwa ni pamoja na IoT, vifaa vya mkononi, na programu zilizojengwa
- **Kutathmini na kulinganisha** mikakati tofauti ya usambazaji wa Edge AI na faida zake

## Vipengele Muhimu kwa Maendeleo ya Edge AI

### 1. Katalogi ya Modeli na Ugunduzi
- **Msaada wa Watoa Huduma Wengi**: Vinjari na pata modeli za AI kutoka Anthropic, OpenAI, GitHub, Google, na watoa huduma wengine
- **Ujumuishaji wa Modeli za Ndani**: Ugunduzi rahisi wa modeli za ONNX na Ollama kwa usambazaji wa ukingo
- **Modeli za GitHub**: Ujumuishaji wa moja kwa moja na mwenyeji wa modeli wa GitHub kwa ufikiaji rahisi
- **Ulinganisho wa Modeli**: Linganisha modeli moja kwa moja ili kupata usawa bora kwa vikwazo vya vifaa vya ukingo

### 2. Uwanja wa Mchezo wa Kuingiliana
- **Mazingira ya Kujaribu Kuingiliana**: Majaribio ya haraka ya uwezo wa modeli katika mazingira yaliyodhibitiwa
- **Msaada wa Modaliti Nyingi**: Jaribu na picha, maandishi, na pembejeo nyingine za kawaida katika hali za ukingo
- **Majaribio ya Wakati Halisi**: Maoni ya haraka kuhusu majibu ya modeli na utendaji
- **Uboreshaji wa Vigezo**: Rekebisha vigezo vya modeli kwa mahitaji ya usambazaji wa ukingo

### 3. Mjenzi wa Maelekezo (Agent Builder)
- **Kizazi cha Lugha Asilia**: Tengeneza maelekezo ya kuanzia kwa kutumia maelezo ya lugha asilia
- **Uboreshaji wa Iterative**: Boresha maelekezo kulingana na majibu ya modeli na utendaji
- **Uchambuzi wa Kazi**: Gawanya kazi ngumu kwa kutumia mnyororo wa maelekezo na matokeo yaliyopangwa
- **Msaada wa Vigezo**: Tumia vigezo katika maelekezo kwa tabia ya mawakala inayobadilika
- **Kizazi cha Msimbo wa Uzalishaji**: Tengeneza msimbo tayari kwa uzalishaji kwa maendeleo ya haraka ya programu

### 4. Uendeshaji wa Wingi na Tathmini
- **Majaribio ya Modeli Nyingi**: Tekeleza maelekezo mengi kwenye modeli zilizochaguliwa kwa wakati mmoja
- **Upimaji wa Ufanisi kwa Wingi**: Jaribu pembejeo na usanidi mbalimbali kwa ufanisi
- **Kesi za Mtihani Maalum**: Endesha mawakala na kesi za mtihani ili kuthibitisha utendaji
- **Ulinganisho wa Utendaji**: Linganisha matokeo kwenye modeli na usanidi tofauti

### 5. Tathmini ya Modeli kwa Dataseti
- **Vipimo vya Kawaida**: Jaribu modeli za AI kwa kutumia tathmini zilizojengwa ndani (F1 score, umuhimu, usawa, mshikamano)
- **Tathmini Maalum**: Unda vipimo vyako vya tathmini kwa hali maalum za matumizi
- **Ujumuishaji wa Dataseti**: Jaribu modeli dhidi ya dataseti za kina
- **Upimaji wa Utendaji**: Pima utendaji wa modeli kwa maamuzi ya usambazaji wa ukingo

### 6. Uwezo wa Kuboresha
- **Ubinafsishaji wa Modeli**: Binafsisha modeli kwa hali maalum za matumizi na nyanja
- **Urekebishaji Maalum**: Rekebisha modeli kwa nyanja maalum na mahitaji
- **Uboreshaji wa Ukingo**: Rekebisha modeli mahsusi kwa vikwazo vya usambazaji wa ukingo
- **Mafunzo Maalum ya Nyanja**: Unda modeli zilizobinafsishwa kwa hali maalum za matumizi ya ukingo

### 7. Ujumuishaji wa Zana za MCP
- **Uunganishaji wa Zana za Nje**: Unganisha mawakala na zana za nje kupitia seva za Model Context Protocol
- **Hatua za Ulimwengu Halisi**: Ruhusu mawakala kuuliza hifadhidata, kufikia API, au kutekeleza mantiki maalum
- **Seva za MCP Zilizopo**: Tumia zana kutoka kwa amri (stdio) au HTTP (matukio yanayotumwa na seva)
- **Maendeleo ya MCP Maalum**: Jenga na tengeneza seva mpya za MCP na majaribio katika Agent Builder

### 8. Maendeleo na Majaribio ya Mawakala
- **Msaada wa Kuita Kazi**: Ruhusu mawakala kuita kazi za nje kwa njia ya nguvu
- **Majaribio ya Uunganishaji wa Wakati Halisi**: Jaribu uunganishaji kwa uendeshaji wa wakati halisi na matumizi ya zana
- **Toleo la Mawakala**: Udhibiti wa toleo kwa mawakala na uwezo wa kulinganisha matokeo ya tathmini
- **Ufuatiliaji na Urekebishaji**: Uwezo wa ufuatiliaji wa ndani na urekebishaji kwa maendeleo ya mawakala

## Mtiririko wa Kazi wa Maendeleo ya Edge AI

### Awamu ya 1: Ugunduzi na Uteuzi wa Modeli
1. **Vinavyotazama Katalogi ya Modeli**: Tumia katalogi ya modeli kupata modeli zinazofaa kwa usambazaji wa ukingo
2. **Linganisho la Utendaji**: Tathmini modeli kulingana na ukubwa, usahihi, na kasi ya inference
3. **Jaribu kwa Ndani**: Tumia modeli za Ollama au ONNX kujaribu kwa ndani kabla ya usambazaji wa ukingo
4. **Tathmini Mahitaji ya Rasilimali**: Tambua mahitaji ya kumbukumbu na hesabu kwa vifaa vya ukingo vinavyolengwa

### Awamu ya 2: Uboreshaji wa Modeli
1. **Badilisha kuwa ONNX**: Badilisha modeli zilizochaguliwa kuwa muundo wa ONNX kwa utangamano wa ukingo
2. **Tumia Quantization**: Punguza ukubwa wa modeli kupitia quantization ya INT8 au INT4
3. **Uboreshaji wa Vifaa**: Boresha kwa vifaa vya ukingo vinavyolengwa (ARM, x86, viharakishi maalum)
4. **Uthibitishaji wa Utendaji**: Thibitisha modeli zilizoboreshwa zinadumisha usahihi unaokubalika

### Awamu ya 3: Maendeleo ya Programu
1. **Ubunifu wa Mawakala**: Tumia Agent Builder kuunda mawakala wa AI walioboreshwa kwa ukingo
2. **Uhandisi wa Maelekezo**: Tengeneza maelekezo yanayofanya kazi kwa ufanisi na modeli ndogo za ukingo
3. **Majaribio ya Uunganishaji**: Jaribu mawakala katika hali zinazofanana na ukingo
4. **Kizazi cha Msimbo**: Tengeneza msimbo wa uzalishaji ulioboreshwa kwa usambazaji wa ukingo

### Awamu ya 4: Tathmini na Majaribio
1. **Tathmini ya Wingi**: Jaribu usanidi mbalimbali ili kupata mipangilio bora ya ukingo
2. **Upimaji wa Utendaji**: Changanua kasi ya inference, matumizi ya kumbukumbu, na usahihi
3. **Simulizi ya Ukingo**: Jaribu katika hali zinazofanana na mazingira ya usambazaji wa ukingo
4. **Majaribio ya Mzigo**: Tathmini utendaji chini ya hali mbalimbali za mzigo

### Awamu ya 5: Maandalizi ya Usambazaji
1. **Uboreshaji wa Mwisho**: Tumia uboreshaji wa mwisho kulingana na matokeo ya majaribio
2. **Ufungaji wa Usambazaji**: Funga modeli na msimbo kwa usambazaji wa ukingo
3. **Nyaraka**: Andika mahitaji ya usambazaji na usanidi
4. **Usanidi wa Ufuatiliaji**: Andaa ufuatiliaji na ukaguzi kwa usambazaji wa ukingo

## Walengwa wa Maendeleo ya Edge AI

### Watengenezaji wa Edge AI
- Watengenezaji wa programu wanaojenga vifaa vya ukingo vinavyotumia AI na suluhisho za IoT
- Watengenezaji wa mifumo iliyojengwa wakijumuisha uwezo wa AI katika vifaa vyenye vikwazo vya rasilimali
- Watengenezaji wa vifaa vya mkononi wanaounda programu za AI kwenye kifaa kwa simu za mkononi na vidonge

### Wahandisi wa Edge AI
- Wahandisi wa AI wanaoboreshaji modeli kwa usambazaji wa ukingo na kusimamia mifumo ya inference
- Wahandisi wa DevOps wanaosambaza na kusimamia modeli za AI kwenye miundombinu ya ukingo iliyotawanyika
- Wahandisi wa utendaji wanaoboreshaji mzigo wa AI kwa vikwazo vya vifaa vya ukingo

### Watafiti na Walimu
- Watafiti wa AI wanaoendeleza modeli na algorithmi bora kwa kompyuta za ukingo
- Walimu wanaofundisha dhana za Edge AI na kuonyesha mbinu za uboreshaji
- Wanafunzi wanaojifunza kuhusu changamoto na suluhisho katika usambazaji wa Edge AI

## Matumizi ya Edge AI

### Vifaa vya IoT vya Kijasiri
- **Utambuzi wa Picha wa Wakati Halisi**: Sambaza modeli za maono ya kompyuta kwenye kamera za IoT na sensa
- **Usindikaji wa Sauti**: Tekeleza utambuzi wa sauti na usindikaji wa lugha asilia kwenye spika za kijasiri
- **Matengenezo ya Kihisia**: Endesha modeli za kugundua hitilafu kwenye vifaa vya ukingo vya viwandani
- **Ufuatiliaji wa Mazingira**: Sambaza modeli za uchambuzi wa data ya sensa kwa matumizi ya mazingira

### Programu za Vifaa vya Mkononi na Vilivyowekwa
- **Tafsiri kwenye Kifaa**: Tekeleza modeli za tafsiri ya lugha zinazofanya kazi bila mtandao
- **Uhalisia Ulioboreshwa**: Sambaza utambuzi wa vitu wa wakati halisi na ufuatiliaji kwa programu za AR
- **Ufuatiliaji wa Afya**: Endesha modeli za uchambuzi wa afya kwenye vifaa vya kuvaa na vifaa vya matibabu
- **Mifumo ya Kujitegemea**: Tekeleza modeli za kufanya maamuzi kwa drones, roboti, na magari

### Miundombinu ya Kompyuta za Ukingo
- **Vituo vya Data vya Ukingo**: Sambaza modeli za AI katika vituo vya data vya ukingo kwa programu za latency ya chini
- **Ujumuishaji wa CDN**: Unganisha uwezo wa usindikaji wa AI katika mitandao ya utoaji wa maudhui
- **Ukingo wa 5G**: Tumia kompyuta za ukingo za 5G kwa programu zinazotumia AI
- **Kompyuta za Fog**: Tekeleza usindikaji wa AI katika mazingira ya kompyuta za fog

## Usakinishaji na Usanidi

### Usakinishaji wa Kiendelezo
Sakinisha kiendelezo cha AI Toolkit moja kwa moja kutoka Soko la Visual Studio Code:

**Kitambulisho cha Kiendelezo**: `ms-windows-ai-studio.windows-ai-studio`

**Mbinu za Usakinishaji**:
1. **Soko la VS Code**: Tafuta "AI Toolkit" katika mwonekano wa Extensions
2. **Amri ya Mstari**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Usakinishaji wa Moja kwa Moja**: Pakua kutoka [Soko la VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Mahitaji ya Awali kwa Maendeleo ya Edge AI
- **Visual Studio Code**: Toleo la hivi karibuni linapendekezwa
- **Mazingira ya Python**
2. Tengeneza maelezo ya kuanzia kwa kutumia maelezo ya lugha asilia  
3. Rudia na boresha maelezo kulingana na majibu ya modeli  
4. Unganisha zana za MCP ili kuboresha uwezo wa wakala  

#### Hatua ya 3: Kupima na Kutathmini  
1. Tumia **Bulk Run** kupima maelezo mengi kwenye modeli zilizochaguliwa  
2. Endesha mawakala na kesi za majaribio ili kuthibitisha utendaji  
3. Tathmini usahihi na utendaji kwa kutumia vipimo vilivyojengwa ndani au vilivyobinafsishwa  
4. Linganisha modeli na usanidi tofauti  

#### Hatua ya 4: Kurekebisha na Kuboresha  
1. Badilisha modeli kwa matumizi maalum ya hali za ukingo  
2. Tumia marekebisho maalum ya kikoa  
3. Boresha kwa vizuizi vya utekelezaji wa ukingo  
4. Toa matoleo na linganisha usanidi tofauti wa wakala  

#### Hatua ya 5: Maandalizi ya Utekelezaji  
1. Tengeneza msimbo tayari kwa uzalishaji kwa kutumia Agent Builder  
2. Sanidi miunganisho ya seva ya MCP kwa matumizi ya uzalishaji  
3. Andaa vifurushi vya utekelezaji kwa vifaa vya ukingo  
4. Sanidi vipimo vya ufuatiliaji na tathmini  

## Mbinu Bora za Maendeleo ya AI ya Ukingo  

### Uchaguzi wa Modeli  
- **Vizuizi vya Ukubwa**: Chagua modeli zinazotoshea ndani ya mipaka ya kumbukumbu ya vifaa lengwa  
- **Kasi ya Utoaji wa Matokeo**: Peana kipaumbele kwa modeli zenye kasi ya utoaji wa matokeo kwa matumizi ya wakati halisi  
- **Mafanikio ya Usahihi**: Linganisha usahihi wa modeli na vizuizi vya rasilimali  
- **Ulinganifu wa Muundo**: Peana kipaumbele kwa muundo wa ONNX au ulioboreshwa kwa vifaa kwa utekelezaji wa ukingo  

### Mbinu za Uboreshaji  
- **Kuantisha**: Tumia kuantisha kwa INT8 au INT4 kupunguza ukubwa wa modeli na kuboresha kasi  
- **Kupunguza**: Ondoa vigezo vya modeli visivyo vya lazima ili kupunguza mahitaji ya hesabu  
- **Uhamishaji wa Maarifa**: Tengeneza modeli ndogo zinazohifadhi utendaji wa zile kubwa  
- **Uharakishaji wa Vifaa**: Tumia NPUs, GPUs, au viharakishi maalum inapopatikana  

### Mtiririko wa Kazi wa Maendeleo  
- **Kupima kwa Kurudia**: Pima mara kwa mara katika hali zinazofanana na ukingo wakati wa maendeleo  
- **Ufuatiliaji wa Utendaji**: Fuata kwa karibu matumizi ya rasilimali na kasi ya utoaji wa matokeo  
- **Udhibiti wa Matoleo**: Fuata matoleo ya modeli na mipangilio ya uboreshaji  
- **Uandishi wa Nyaraka**: Andika nyaraka za maamuzi yote ya uboreshaji na mafanikio ya utendaji  

### Mambo ya Kuzingatia kwa Utekelezaji  
- **Ufuatiliaji wa Rasilimali**: Fuata matumizi ya kumbukumbu, CPU, na nguvu katika uzalishaji  
- **Mikakati ya Mbadala**: Tekeleza mifumo ya mbadala kwa kushindwa kwa modeli  
- **Mifumo ya Sasisho**: Panga sasisho za modeli na usimamizi wa matoleo  
- **Usalama**: Tekeleza hatua za usalama zinazofaa kwa matumizi ya AI ya ukingo  

## Ujumuishaji na Mifumo ya AI ya Ukingo  

### ONNX Runtime  
- **Utekelezaji wa Mifumo Mbalimbali**: Tekeleza modeli za ONNX kwenye majukwaa tofauti ya ukingo  
- **Uboreshaji wa Vifaa**: Tumia uboreshaji maalum wa vifaa wa ONNX Runtime  
- **Msaada wa Simu za Mkononi**: Tumia ONNX Runtime Mobile kwa programu za simu na vidonge  
- **Ujumuishaji wa IoT**: Tekeleza kwenye vifaa vya IoT kwa kutumia usambazaji mwepesi wa ONNX Runtime  

### Windows ML  
- **Vifaa vya Windows**: Boresha kwa vifaa vya ukingo vya msingi wa Windows na PC  
- **Uharakishaji wa NPU**: Tumia Neural Processing Units kwenye vifaa vya Windows  
- **DirectML**: Tumia DirectML kwa uharakishaji wa GPU kwenye majukwaa ya Windows  
- **Ujumuishaji wa UWP**: Unganisha na programu za Universal Windows Platform  

### TensorFlow Lite  
- **Uboreshaji wa Simu za Mkononi**: Tekeleza modeli za TensorFlow Lite kwenye vifaa vya simu na vilivyopachikwa  
- **Wajumbe wa Vifaa**: Tumia wajumbe maalum wa vifaa kwa uharakishaji  
- **Vifaa Vidogo vya Kielektroniki**: Tekeleza kwenye vidhibiti vidogo kwa kutumia TensorFlow Lite Micro  
- **Msaada wa Mifumo Mbalimbali**: Tekeleza kwenye Android, iOS, na mifumo ya Linux iliyopachikwa  

### Azure IoT Edge  
- **Mseto wa Wingu-Ukingo**: Changanya mafunzo ya wingu na utoaji wa matokeo wa ukingo  
- **Utekelezaji wa Moduli**: Tekeleza modeli za AI kama moduli za IoT Edge  
- **Usimamizi wa Vifaa**: Simamia vifaa vya ukingo na sasisho za modeli kwa mbali  
- **Telemetri**: Kusanya data ya utendaji na vipimo vya modeli kutoka kwa utekelezaji wa ukingo  

## Matukio ya Juu ya AI ya Ukingo  

### Utekelezaji wa Modeli Nyingi  
- **Vikundi vya Modeli**: Tekeleza modeli nyingi kwa usahihi ulioboreshwa au urudufu  
- **Upimaji wa A/B**: Pima modeli tofauti kwa wakati mmoja kwenye vifaa vya ukingo  
- **Uchaguzi wa Kiadapta**: Chagua modeli kulingana na hali za sasa za kifaa  
- **Ugawaji wa Rasilimali**: Boresha matumizi ya rasilimali kwenye modeli nyingi zilizotekelezwa  

### Mafunzo ya Pamoja  
- **Mafunzo Yanayosambazwa**: Funza modeli kwenye vifaa vingi vya ukingo  
- **Uhifadhi wa Faragha**: Weka data ya mafunzo ndani ya nchi huku ukishiriki maboresho ya modeli  
- **Mafunzo ya Ushirikiano**: Ruhusu vifaa kujifunza kutoka kwa uzoefu wa pamoja  
- **Uratibu wa Ukingo-Wingu**: Ratibu mafunzo kati ya vifaa vya ukingo na miundombinu ya wingu  

### Usindikaji wa Wakati Halisi  
- **Usindikaji wa Mfululizo**: Shughulikia mfululizo wa data unaoendelea kwenye vifaa vya ukingo  
- **Utoaji wa Matokeo wa Kasi ya Chini**: Boresha kwa ucheleweshaji mdogo wa utoaji wa matokeo  
- **Usindikaji wa Vikundi**: Shughulikia vikundi vya data kwa ufanisi kwenye vifaa vya ukingo  
- **Usindikaji wa Kiadapta**: Rekebisha usindikaji kulingana na uwezo wa sasa wa kifaa  

## Utatuzi wa Shida za Maendeleo ya AI ya Ukingo  

### Masuala ya Kawaida  
- **Vizuizi vya Kumbukumbu**: Modeli kubwa sana kwa kumbukumbu ya kifaa lengwa  
- **Kasi ya Utoaji wa Matokeo**: Utoaji wa matokeo wa modeli ni polepole sana kwa mahitaji ya wakati halisi  
- **Kupungua kwa Usahihi**: Uboreshaji unapunguza usahihi wa modeli kwa kiwango kisichokubalika  
- **Ulinganifu wa Vifaa**: Modeli haipatani na vifaa lengwa  

### Mikakati ya Urekebishaji  
- **Uchambuzi wa Utendaji**: Tumia vipengele vya ufuatiliaji wa AI Toolkit kutambua vizuizi  
- **Ufuatiliaji wa Rasilimali**: Fuata matumizi ya kumbukumbu na CPU wakati wa maendeleo  
- **Kupima kwa Hatua**: Pima uboreshaji hatua kwa hatua ili kutambua masuala  
- **Uigaji wa Vifaa**: Tumia zana za maendeleo kuiga vifaa lengwa  

### Suluhisho za Uboreshaji  
- **Kuantisha Zaidi**: Tumia mbinu za kuantisha za hali ya juu zaidi  
- **Miundo ya Modeli**: Fikiria miundo tofauti ya modeli iliyoboreshwa kwa ukingo  
- **Uboreshaji wa Usindikaji wa Awali**: Boresha usindikaji wa data wa awali kwa vizuizi vya ukingo  
- **Uboreshaji wa Utoaji wa Matokeo**: Tumia uboreshaji maalum wa utoaji wa matokeo wa vifaa  

## Rasilimali na Hatua Zifuatazo  

### Nyaraka Rasmi  
- [Nyaraka za Msanidi wa AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Mwongozo wa Usakinishaji na Usanidi](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Nyaraka za VS Code Intelligent Apps](https://code.visualstudio.com/docs/intelligentapps)  
- [Nyaraka za Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Jamii na Usaidizi  
- [Hifadhi ya GitHub ya AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Masuala ya GitHub na Maombi ya Vipengele](https://aka.ms/AIToolkit/feedback)  
- [Jamii ya Discord ya Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Soko la Ugani la VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Rasilimali za Kiufundi  
- [Nyaraka za ONNX Runtime](https://onnxruntime.ai/)  
- [Nyaraka za Ollama](https://ollama.ai/)  
- [Nyaraka za Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Nyaraka za Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Njia za Kujifunza  
- [Kozi ya Misingi ya AI ya Ukingo](../Module01/README.md)  
- [Mwongozo wa Modeli Ndogo za Lugha](../Module02/README.md)  
- [Mikakati ya Utekelezaji wa Ukingo](../Module03/README.md)  
- [Maendeleo ya AI ya Ukingo wa Windows](./windowdeveloper.md)  

### Rasilimali za Ziada  
- **Takwimu za Hifadhi**: Nyota 1.8k+, matawi 150+, wachangiaji 18+  
- **Leseni**: Leseni ya MIT  
- **Usalama**: Sera za usalama za Microsoft zinatumika  
- **Telemetri**: Inaheshimu mipangilio ya telemetri ya VS Code  

## Hitimisho  

AI Toolkit kwa Visual Studio Code ni jukwaa kamili kwa maendeleo ya kisasa ya AI, likitoa uwezo wa maendeleo ya wakala uliorahisishwa ambao ni muhimu hasa kwa matumizi ya AI ya ukingo. Kwa katalogi yake pana ya modeli inayounga mkono watoa huduma kama Anthropic, OpenAI, GitHub, na Google, pamoja na utekelezaji wa ndani kupitia ONNX na Ollama, zana hii inatoa kubadilika kunakohitajika kwa hali mbalimbali za utekelezaji wa ukingo.  

Nguvu ya zana hii iko katika mbinu yake iliyojumuishwa—kutoka kwa ugunduzi wa modeli na majaribio kwenye Playground hadi maendeleo ya wakala wa hali ya juu na Prompt Builder, uwezo wa tathmini kamili, na ujumuishaji wa zana za MCP. Kwa watengenezaji wa AI ya ukingo, hii inamaanisha kuunda na kupima mawakala wa AI haraka kabla ya utekelezaji wa ukingo, huku wakiwa na uwezo wa kurudia haraka na kuboresha kwa mazingira yenye vizuizi vya rasilimali.  

Faida kuu kwa maendeleo ya AI ya ukingo ni pamoja na:  
- **Majaribio ya Haraka**: Pima modeli na mawakala haraka kabla ya kujitolea kwa utekelezaji wa ukingo  
- **Kubadilika kwa Watoa Huduma Wengi**: Pata modeli kutoka vyanzo mbalimbali ili kupata suluhisho bora za ukingo  
- **Maendeleo ya Ndani**: Pima kwa kutumia ONNX na Ollama kwa maendeleo ya nje ya mtandao na yanayoheshimu faragha  
- **Uwezo wa Uzalishaji**: Tengeneza msimbo tayari kwa uzalishaji na ujumuishaji na zana za nje kupitia MCP  
- **Tathmini Kamili**: Tumia vipimo vilivyojengwa ndani na vilivyobinafsishwa kuthibitisha utendaji wa AI ya ukingo  

Kadri AI inavyoendelea kuelekea hali za utekelezaji wa ukingo, AI Toolkit kwa VS Code inatoa mazingira ya maendeleo na mtiririko wa kazi unaohitajika kujenga, kupima, na kuboresha programu za akili za bandia kwa mazingira yenye vizuizi vya rasilimali. Ikiwa unaunda suluhisho za IoT, programu za AI za simu, au mifumo ya akili iliyopachikwa, seti ya vipengele vya zana hii na mtiririko wa kazi uliounganishwa vinaunga mkono mzunguko mzima wa maendeleo ya AI ya ukingo.  

Kwa maendeleo yanayoendelea na jamii hai (nyota 1.8k+ kwenye GitHub), AI Toolkit inabaki mstari wa mbele wa zana za maendeleo ya AI, ikiendelea kubadilika ili kukidhi mahitaji ya watengenezaji wa AI wa kisasa wanaojenga kwa hali za utekelezaji wa ukingo.  

[Next Foundry Local](./foundrylocal.md)  

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.