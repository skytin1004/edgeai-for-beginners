<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-18T17:26:12+00:00",
  "source_file": "Module07/README.md",
  "language_code": "sw"
}
-->
# Sura ya 07: Sampuli za EdgeAI

Edge AI inawakilisha muunganiko wa akili bandia na kompyuta ya ukingo, ikiruhusu usindikaji wa akili moja kwa moja kwenye vifaa bila kutegemea muunganisho wa wingu. Sura hii inachunguza utekelezaji tano tofauti wa EdgeAI kwenye majukwaa na mifumo mbalimbali, ikionyesha uwezo na nguvu ya kuendesha mifano ya AI kwenye ukingo.

## 1. EdgeAI katika NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano inawakilisha hatua kubwa katika kompyuta ya ukingo yenye akili bandia inayopatikana, ikitoa hadi 67 TOPS ya utendaji wa AI katika muundo mdogo wa ukubwa wa kadi ya mkopo. Jukwaa hili lenye nguvu la Edge AI linatoa fursa kwa watengenezaji wa AI ya kizazi kwa wapenzi wa teknolojia, wanafunzi, na watengenezaji wa kitaalamu.

### Vipengele Muhimu
- Inatoa hadi 67 TOPS ya utendaji wa AI—ongezeko la 1.7X ikilinganishwa na toleo lake la awali
- 1024 CUDA cores na hadi 32 Tensor Cores kwa usindikaji wa AI
- CPU ya Arm Cortex-A78AE v8.2 64-bit yenye msingi 6 na masafa ya juu ya 1.5 GHz
- Bei ya $249 pekee, ikiwapa watengenezaji, wanafunzi, na wabunifu jukwaa linalopatikana zaidi na la gharama nafuu

### Matumizi
Jetson Orin Nano ni bora katika kuendesha mifano ya kisasa ya AI ya kizazi ikiwa ni pamoja na vision transformers, mifano mikubwa ya lugha, na mifano ya lugha ya kuona. Imeundwa mahsusi kwa matumizi ya GenAI, na sasa unaweza kuendesha LLM kadhaa kwenye kifaa cha mkononi. Matumizi maarufu ni pamoja na roboti zenye akili bandia, drones za kisasa, kamera zenye akili, na vifaa vya ukingo vinavyojiendesha.

**Jifunze Zaidi**: [Kompyuta ya Super ya NVIDIA Jetson Orin Nano: Jambo Kubwa Lijalo katika EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI katika Programu za Simu za Mkononi na .NET MAUI na ONNX Runtime GenAI

Suluhisho hili linaonyesha jinsi ya kuunganisha AI ya kizazi na Mifano Mikubwa ya Lugha (LLMs) katika programu za simu za mkononi za majukwaa mbalimbali kwa kutumia .NET MAUI (Multi-platform App UI) na ONNX Runtime GenAI. Njia hii inawawezesha watengenezaji wa .NET kujenga programu za simu za mkononi zenye akili bandia zinazofanya kazi asili kwenye vifaa vya Android na iOS.

### Vipengele Muhimu
- Imejengwa kwenye mfumo wa .NET MAUI, ikitoa msingi mmoja wa msimbo kwa programu za Android na iOS
- Muunganisho wa ONNX Runtime GenAI unaruhusu kuendesha mifano ya AI ya kizazi moja kwa moja kwenye vifaa vya mkononi
- Inasaidia viharakishi mbalimbali vya vifaa vilivyotengenezwa mahsusi kwa simu za mkononi, ikiwa ni pamoja na CPU, GPU, na vichakataji maalum vya AI vya simu
- Uboreshaji maalum wa jukwaa kama CoreML kwa iOS na NNAPI kwa Android kupitia ONNX Runtime
- Inatekeleza mzunguko kamili wa AI ya kizazi ikiwa ni pamoja na usindikaji wa awali na baada, inference, usindikaji wa logits, utafutaji na sampuli, na usimamizi wa KV cache

### Faida za Maendeleo
Njia ya .NET MAUI inawawezesha watengenezaji kutumia ujuzi wao wa C# na .NET wakati wa kujenga programu za AI za majukwaa mbalimbali. Mfumo wa ONNX Runtime GenAI unasaidia miundo mbalimbali ya mifano ikiwa ni pamoja na Llama, Mistral, Phi, Gemma, na mingine mingi. Kernel za ARM64 zilizoboreshwa zinaharakisha kuzidisha kwa matriki ya INT4 iliyokadiriwa, kuhakikisha utendaji mzuri kwenye vifaa vya mkononi huku ukihifadhi uzoefu wa maendeleo wa .NET.

### Matumizi
Suluhisho hili ni bora kwa watengenezaji wanaotaka kujenga programu za simu za mkononi zenye akili bandia kwa kutumia teknolojia za .NET, ikiwa ni pamoja na chatbots zenye akili, programu za utambuzi wa picha, zana za kutafsiri lugha, na mifumo ya mapendekezo ya kibinafsi inayofanya kazi kikamilifu kwenye kifaa kwa faragha iliyoboreshwa na uwezo wa kufanya kazi bila mtandao.

**Jifunze Zaidi**: [.NET MAUI ONNX Runtime GenAI Mfano](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI katika Azure na Injini ya Mifano Midogo ya Lugha

Suluhisho la EdgeAI la Microsoft linalotegemea Azure linazingatia kupeleka Mifano Midogo ya Lugha (SLMs) kwa ufanisi katika mazingira ya mseto ya wingu-ukingo. Njia hii inaunganisha huduma za AI za kiwango cha wingu na mahitaji ya utekelezaji wa ukingo.

### Faida za Muundo
- Muunganisho wa moja kwa moja na huduma za Azure AI
- Endesha SLMs/LLMs na mifano ya multi-modal kwenye kifaa na wingu kwa ONNX Runtime
- Imeboreshwa kwa utekelezaji wa kiwango cha biashara
- Msaada wa masasisho ya modeli endelevu na usimamizi

### Matumizi
Utekelezaji wa EdgeAI wa Azure ni bora katika hali zinazohitaji utekelezaji wa AI wa kiwango cha biashara na uwezo wa usimamizi wa wingu. Hii ni pamoja na usindikaji wa hati zenye akili, uchanganuzi wa wakati halisi, na mtiririko wa kazi wa AI wa mseto unaotumia rasilimali za kompyuta za wingu na ukingo.

**Jifunze Zaidi**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI na Windows ML

Windows ML inawakilisha mfumo wa kisasa wa Microsoft ulioboreshwa kwa inference ya modeli kwenye kifaa na utekelezaji rahisi, ukiwa msingi wa Windows AI Foundry. Jukwaa hili linawawezesha watengenezaji kuunda programu za Windows zenye akili bandia zinazotumia uwezo kamili wa vifaa vya PC.

### Uwezo wa Jukwaa
- Inafanya kazi kwenye PC zote za Windows 11 zinazotumia toleo la 24H2 (build 26100) au zaidi
- Inafanya kazi kwenye vifaa vyote vya PC vya x64 na ARM64, hata PC ambazo hazina NPUs au GPUs
- Inawawezesha watengenezaji kuleta mifano yao wenyewe na kuitekeleza kwa ufanisi kwenye ekosistimu ya washirika wa silicon ikiwa ni pamoja na AMD, Intel, NVIDIA, na Qualcomm ikijumuisha CPU, GPU, NPU
- Kwa kutumia API za miundombinu, watengenezaji hawahitaji tena kuunda matoleo mengi ya programu yao ili kulenga silicon tofauti

### Faida za Watengenezaji
Windows ML inaficha vifaa na watoa huduma wa utekelezaji, hivyo unaweza kuzingatia kuandika msimbo wako. Zaidi ya hayo, Windows ML inasasisha kiotomatiki ili kusaidia NPUs, GPUs, na CPUs za hivi karibuni zinapozinduliwa. Jukwaa linatoa mfumo wa umoja wa maendeleo ya AI katika ekosistimu tofauti ya vifaa vya Windows.

**Jifunze Zaidi**: 
- [Muhtasari wa Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Mwongozo wa Maendeleo ya Windows EdgeAI](../windowdeveloper.md) - Mwongozo wa kina wa maendeleo ya Windows Edge AI

## 5. EdgeAI na Programu za Foundry Local

Foundry Local inawawezesha watengenezaji kujenga programu za Retrieval Augmented Generation (RAG) kwa kutumia rasilimali za ndani katika .NET, ikichanganya mifano ya lugha ya ndani na uwezo wa utafutaji wa semantiki. Njia hii inatoa suluhisho za AI zinazozingatia faragha zinazofanya kazi kikamilifu kwenye miundombinu ya ndani.

### Muundo wa Kiufundi
- Inachanganya modeli ya lugha ya Phi-3, Local Embeddings, na Semantic Kernel kuunda hali ya RAG
- Inatumia embeddings kama vectors (arrays) za thamani za namba zinazowakilisha maudhui na maana yake ya semantiki
- Semantic Kernel hufanya kazi kama mratibu mkuu, ikijumuisha Phi-3 na Vipengele Smart kuunda mtiririko wa RAG usio na mshono
- Msaada kwa hifadhidata za vector za ndani ikiwa ni pamoja na SQLite na Qdrant

### Faida za Utekelezaji
RAG, au Retrieval Augmented Generation, ni njia ya kusema "tafuta baadhi ya vitu na uviweke kwenye prompt". Utekelezaji huu wa ndani unahakikisha faragha ya data huku ukitoa majibu yenye akili yanayozingatia hifadhidata za maarifa maalum. Njia hii ni muhimu hasa kwa hali za biashara zinazohitaji uhuru wa data na uwezo wa kufanya kazi bila mtandao.

**Jifunze Zaidi**: [Sampuli za Foundry Local RAG](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Rasilimali za Maendeleo ya Windows EdgeAI

Kwa watengenezaji wanaolenga jukwaa la Windows, tumetengeneza mwongozo wa kina unaofunika ekosistimu kamili ya Windows EdgeAI. Rasilimali hii inatoa maelezo ya kina kuhusu Windows AI Foundry, ikiwa ni pamoja na API, zana, na mbinu bora za maendeleo ya EdgeAI kwenye Windows.

### Jukwaa la Windows AI Foundry
Jukwaa la Windows AI Foundry linatoa seti kamili ya zana na API zilizotengenezwa mahsusi kwa maendeleo ya Edge AI kwenye vifaa vya Windows. Hii ni pamoja na msaada maalum kwa vifaa vilivyoharakishwa na NPU, muunganisho wa Windows ML, na mbinu za uboreshaji maalum wa jukwaa.

**Mwongozo wa Kina**: [Mwongozo wa Maendeleo ya Windows EdgeAI](../windowdeveloper.md)

Mwongozo huu unafunika:
- Muhtasari wa jukwaa la Windows AI Foundry na vipengele vyake
- API ya Phi Silica kwa inference yenye ufanisi kwenye vifaa vya NPU
- API za Maono ya Kompyuta kwa usindikaji wa picha na OCR
- Muunganisho wa Windows ML na mbinu za uboreshaji
- CLI ya Foundry Local kwa maendeleo na majaribio ya ndani
- Mikakati ya uboreshaji wa vifaa kwa vifaa vya Windows
- Mifano ya utekelezaji wa vitendo na mbinu bora

### Zana ya AI kwa Maendeleo ya Edge AI
Kwa watengenezaji wanaotumia Visual Studio Code, kiendelezi cha AI Toolkit kinatoa mazingira kamili ya maendeleo yaliyoundwa mahsusi kwa ajili ya kujenga, kujaribu, na kupeleka programu za Edge AI. Zana hii inarahisisha mtiririko mzima wa maendeleo ya Edge AI ndani ya VS Code.

**Mwongozo wa Maendeleo**: [Zana ya AI kwa Maendeleo ya Edge AI](../aitoolkit.md)

Mwongozo wa Zana ya AI unafunika:
- Ugunduzi wa modeli na uteuzi kwa utekelezaji wa ukingo
- Mtiririko wa majaribio na uboreshaji wa ndani
- Muunganisho wa ONNX na Ollama kwa mifano ya ukingo
- Mbinu za ubadilishaji wa modeli na upunguzaji wa ukubwa
- Maendeleo ya mawakala kwa hali za ukingo
- Tathmini ya utendaji na ufuatiliaji
- Maandalizi ya utekelezaji na mbinu bora

## Hitimisho

Utekelezaji huu tano wa EdgeAI unaonyesha ukomavu na utofauti wa suluhisho za AI za ukingo zinazopatikana leo. Kutoka kwa vifaa vya ukingo vilivyoharakishwa na vifaa kama Jetson Orin Nano hadi mifumo ya programu kama ONNX Runtime GenAI na Windows ML, watengenezaji wana chaguo nyingi za kupeleka programu zenye akili kwenye ukingo.

Kitu cha kawaida katika majukwaa haya yote ni demokrasia ya uwezo wa AI, ikifanya ujifunzaji wa mashine wa kisasa kupatikana kwa watengenezaji wa viwango tofauti vya ujuzi na hali za matumizi. Ikiwa unajenga programu za simu za mkononi, programu za desktop, au mifumo iliyojengwa, suluhisho hizi za EdgeAI zinatoa msingi wa kizazi kijacho cha programu zenye akili zinazofanya kazi kwa ufanisi na faragha kwenye ukingo.

Kila jukwaa linatoa faida za kipekee: Jetson Orin Nano kwa kompyuta ya ukingo iliyoharakishwa na vifaa, ONNX Runtime GenAI kwa maendeleo ya simu za mkononi za majukwaa mbalimbali, Azure EdgeAI kwa muunganisho wa wingu-ukingo wa biashara, Windows ML kwa programu za asili za Windows, na Foundry Local kwa utekelezaji wa RAG unaozingatia faragha. Pamoja, yanawakilisha ekosistimu kamili ya maendeleo ya EdgeAI.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.