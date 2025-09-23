<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb6eadc312d5658a0cd71c0085b43742",
  "translation_date": "2025-09-22T23:16:31+00:00",
  "source_file": "Module07/README.md",
  "language_code": "sw"
}
-->
# Sura ya 07: Sampuli za EdgeAI

Edge AI inawakilisha muunganiko wa akili bandia na kompyuta ya ukingo, ikiruhusu usindikaji wa akili moja kwa moja kwenye vifaa bila kutegemea muunganisho wa wingu. Sura hii inachunguza utekelezaji tano tofauti wa EdgeAI kwenye majukwaa na mifumo mbalimbali, ikionyesha uwezo na nguvu ya kuendesha mifano ya AI kwenye ukingo.

## 1. EdgeAI katika NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano ni hatua kubwa katika kompyuta ya ukingo yenye akili, ikitoa hadi 67 TOPS ya utendaji wa AI katika kifaa kidogo saizi ya kadi ya mkopo. Jukwaa hili lenye nguvu la Edge AI linatoa fursa kwa wanafunzi, wabunifu, na watengenezaji wa kitaalamu kuunda AI ya kizazi kipya.

### Vipengele Muhimu
- Inatoa hadi 67 TOPS ya utendaji wa AI—ongezeko la 1.7X ikilinganishwa na mtangulizi wake
- 1024 CUDA cores na hadi 32 Tensor Cores kwa usindikaji wa AI
- CPU ya Arm Cortex-A78AE v8.2 64-bit yenye msingi 6 na masafa ya juu ya 1.5 GHz
- Bei ya $249 pekee, ikiwapa watengenezaji, wanafunzi, na wabunifu jukwaa la bei nafuu na linalopatikana zaidi

### Matumizi
Jetson Orin Nano ni bora kwa kuendesha mifano ya kisasa ya AI ya kizazi kama vile vision transformers, mifano mikubwa ya lugha, na mifano ya lugha na maono. Imeundwa mahsusi kwa matumizi ya GenAI, na sasa unaweza kuendesha LLM kadhaa kwenye kifaa cha mkononi. Matumizi maarufu ni pamoja na roboti zenye akili, drones za kisasa, kamera za akili, na vifaa vya ukingo vya kujitegemea.

**Jifunze Zaidi**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI katika Programu za Simu za Mkononi na .NET MAUI na ONNX Runtime GenAI

Suluhisho hili linaonyesha jinsi ya kuunganisha Generative AI na Large Language Models (LLMs) katika programu za simu za mkononi za majukwaa mbalimbali kwa kutumia .NET MAUI (Multi-platform App UI) na ONNX Runtime GenAI. Njia hii inawawezesha watengenezaji wa .NET kujenga programu za simu za mkononi zenye akili zinazofanya kazi asili kwenye vifaa vya Android na iOS.

### Vipengele Muhimu
- Imejengwa kwenye mfumo wa .NET MAUI, ikitoa msingi mmoja wa msimbo kwa programu za Android na iOS
- ONNX Runtime GenAI inawezesha kuendesha mifano ya AI ya kizazi moja kwa moja kwenye vifaa vya mkononi
- Inasaidia viendeshi vya vifaa mbalimbali vilivyotengenezwa kwa simu za mkononi, ikiwa ni pamoja na CPU, GPU, na viendeshi maalum vya AI vya simu
- Uboreshaji maalum wa jukwaa kama CoreML kwa iOS na NNAPI kwa Android kupitia ONNX Runtime
- Inatekeleza mzunguko kamili wa AI ya kizazi ikiwa ni pamoja na usindikaji wa awali na baada, inference, usindikaji wa logits, utafutaji na sampuli, na usimamizi wa KV cache

### Faida za Maendeleo
Njia ya .NET MAUI inawawezesha watengenezaji kutumia ujuzi wao wa C# na .NET wakati wa kujenga programu za AI za majukwaa mbalimbali. Mfumo wa ONNX Runtime GenAI unasaidia miundo mbalimbali ya mifano ikiwa ni pamoja na Llama, Mistral, Phi, Gemma, na mingine mingi. Kernel za ARM64 zilizoboreshwa zinaharakisha kuzidisha kwa matriki za INT4 zilizokadiriwa, kuhakikisha utendaji mzuri kwenye vifaa vya mkononi huku ukihifadhi uzoefu wa maendeleo wa .NET.

### Matumizi
Suluhisho hili ni bora kwa watengenezaji wanaotaka kujenga programu za simu za mkononi zenye akili kwa kutumia teknolojia za .NET, ikiwa ni pamoja na chatbots zenye akili, programu za kutambua picha, zana za kutafsiri lugha, na mifumo ya mapendekezo ya kibinafsi inayofanya kazi kikamilifu kwenye kifaa kwa faragha iliyoboreshwa na uwezo wa kufanya kazi bila mtandao.

**Jifunze Zaidi**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI katika Azure na Injini ya Small Language Models

Suluhisho la EdgeAI la Microsoft linalotegemea Azure linazingatia kupeleka Small Language Models (SLMs) kwa ufanisi katika mazingira ya mseto ya wingu-ukingo. Njia hii inaunganisha huduma za AI za kiwango cha wingu na mahitaji ya utekelezaji wa ukingo.

### Faida za Muundo
- Muunganisho wa moja kwa moja na huduma za Azure AI
- Kuendesha SLMs/LLMs na mifano ya multi-modal kwenye kifaa na wingu kwa kutumia ONNX Runtime
- Imeboreshwa kwa utekelezaji wa kiwango cha biashara
- Msaada wa masasisho ya modeli na usimamizi endelevu

### Matumizi
Utekelezaji wa Azure EdgeAI ni bora katika hali zinazohitaji utekelezaji wa AI wa kiwango cha biashara na uwezo wa usimamizi wa wingu. Hii inajumuisha usindikaji wa hati zenye akili, uchanganuzi wa wakati halisi, na mtiririko wa kazi wa AI wa mseto unaotumia rasilimali za wingu na ukingo.

**Jifunze Zaidi**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI na Windows ML

Windows ML inawakilisha mfumo wa kisasa wa Microsoft ulioboreshwa kwa inference ya modeli kwenye kifaa na utekelezaji rahisi, ukiwa msingi wa Windows AI Foundry. Jukwaa hili linawawezesha watengenezaji kuunda programu za Windows zenye akili zinazotumia uwezo wa vifaa vya PC.

### Uwezo wa Jukwaa
- Inafanya kazi kwenye PC zote za Windows 11 zinazotumia toleo la 24H2 (build 26100) au zaidi
- Inafanya kazi kwenye vifaa vyote vya PC vya x64 na ARM64, hata PC ambazo hazina NPUs au GPUs
- Inawawezesha watengenezaji kuleta mifano yao wenyewe na kuitekeleza kwa ufanisi kwenye ekosistimu ya washirika wa silicon ikiwa ni pamoja na AMD, Intel, NVIDIA, na Qualcomm ikijumuisha CPU, GPU, NPU
- Kwa kutumia API za miundombinu, watengenezaji hawahitaji tena kuunda matoleo mengi ya programu yao ili kulenga silicon tofauti

### Faida kwa Watengenezaji
Windows ML inaficha vifaa na watoa huduma wa utekelezaji, hivyo unaweza kuzingatia kuandika msimbo wako. Zaidi ya hayo, Windows ML inasasishwa kiotomatiki ili kusaidia NPUs, GPUs, na CPUs za hivi karibuni zinapozinduliwa. Jukwaa linatoa mfumo wa umoja wa maendeleo ya AI kwenye ekosistimu tofauti ya vifaa vya Windows.

**Jifunze Zaidi**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Mwongozo wa kina wa maendeleo ya Windows Edge AI

## 5. EdgeAI na Foundry Local Applications

Foundry Local inawawezesha watengenezaji kujenga programu za Retrieval Augmented Generation (RAG) kwa kutumia rasilimali za ndani katika .NET, ikichanganya mifano ya lugha ya ndani na uwezo wa utafutaji wa semantiki. Njia hii inatoa suluhisho za AI zinazozingatia faragha zinazofanya kazi kikamilifu kwenye miundombinu ya ndani.

### Muundo wa Kiufundi
- Inachanganya modeli ya lugha ya Phi, Local Embeddings, na Semantic Kernel kuunda hali ya RAG
- Inatumia embeddings kama vectors (arrays) za thamani za namba zinazowakilisha maudhui na maana yake ya semantiki
- Semantic Kernel hufanya kazi kama mratibu mkuu, ikijumuisha Phi na Smart Components kuunda mtiririko wa RAG usio na mshono
- Msaada kwa hifadhidata za vector za ndani ikiwa ni pamoja na SQLite na Qdrant

### Faida za Utekelezaji
RAG, au Retrieval Augmented Generation, ni njia ya "kutafuta taarifa na kuziingiza kwenye prompt". Utekelezaji huu wa ndani unahakikisha faragha ya data huku ukitoa majibu yenye akili yanayozingatia hifadhidata za maarifa maalum. Njia hii ni muhimu hasa kwa hali za biashara zinazohitaji uhuru wa data na uwezo wa kufanya kazi bila mtandao.

**Jifunze Zaidi**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local inatoa seva ya REST inayolingana na OpenAI inayotumia ONNX Runtime kuendesha mifano kwa ndani kwenye Windows. Hapa kuna muhtasari wa haraka uliothibitishwa; angalia nyaraka rasmi kwa maelezo kamili.

- Anza: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Muundo: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Marejeleo ya CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Mwongozo kamili wa Windows katika repo hii: [foundrylocal.md](./foundrylocal.md)

Sakinisha au sasisha kwenye Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Chunguza kategoria za CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Endesha modeli na gundua endpoint inayobadilika:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Ukaguzi wa haraka wa REST kuorodhesha mifano (badilisha PORT kutoka status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Vidokezo:
- Muunganisho wa SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Leta modeli yako mwenyewe (compile): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Rasilimali za Maendeleo ya Windows EdgeAI

Kwa watengenezaji wanaolenga jukwaa la Windows, tumetengeneza mwongozo wa kina unaofunika ekosistimu kamili ya Windows EdgeAI. Rasilimali hii inatoa maelezo ya kina kuhusu Windows AI Foundry, ikiwa ni pamoja na API, zana, na mbinu bora za maendeleo ya EdgeAI kwenye Windows.

### Jukwaa la Windows AI Foundry
Jukwaa la Windows AI Foundry linatoa suite kamili ya zana na API zilizoundwa mahsusi kwa maendeleo ya Edge AI kwenye vifaa vya Windows. Hii inajumuisha msaada maalum kwa vifaa vilivyoharakishwa na NPU, muunganisho wa Windows ML, na mbinu za uboreshaji maalum wa jukwaa.

**Mwongozo wa Kina**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Mwongozo huu unafunika:
- Muhtasari wa jukwaa la Windows AI Foundry na vipengele vyake
- API ya Phi Silica kwa inference yenye ufanisi kwenye vifaa vya NPU
- API za Computer Vision kwa usindikaji wa picha na OCR
- Muunganisho wa Windows ML runtime na uboreshaji
- CLI ya Foundry Local kwa maendeleo na majaribio ya ndani
- Mikakati ya uboreshaji wa vifaa kwa vifaa vya Windows
- Mifano ya utekelezaji wa vitendo na mbinu bora

### Zana ya AI kwa Maendeleo ya Edge AI
Kwa watengenezaji wanaotumia Visual Studio Code, kiendelezi cha AI Toolkit kinatoa mazingira kamili ya maendeleo yaliyoundwa mahsusi kwa kujenga, kujaribu, na kupeleka programu za Edge AI. Zana hii inarahisisha mtiririko mzima wa maendeleo ya Edge AI ndani ya VS Code.

**Mwongozo wa Maendeleo**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

Mwongozo wa AI Toolkit unafunika:
- Ugunduzi wa modeli na uteuzi kwa utekelezaji wa ukingo
- Mtiririko wa majaribio na uboreshaji wa ndani
- Muunganisho wa ONNX na Ollama kwa mifano ya ukingo
- Mbinu za ubadilishaji wa modeli na quantization
- Maendeleo ya mawakala kwa hali za ukingo
- Tathmini ya utendaji na ufuatiliaji
- Maandalizi ya utekelezaji na mbinu bora

## Hitimisho

Utekelezaji huu tano wa EdgeAI unaonyesha ukomavu na utofauti wa suluhisho za AI za ukingo zinazopatikana leo. Kutoka kwa vifaa vya ukingo vilivyoharakishwa na vifaa kama Jetson Orin Nano hadi mifumo ya programu kama ONNX Runtime GenAI na Windows ML, watengenezaji wana chaguo nyingi za kupeleka programu zenye akili kwenye ukingo.

Kipengele cha kawaida katika majukwaa haya yote ni demokrasia ya uwezo wa AI, ikifanya ujifunzaji wa mashine wa kisasa kupatikana kwa watengenezaji wa viwango tofauti vya ujuzi na matumizi. Ikiwa unajenga programu za simu za mkononi, programu za desktop, au mifumo iliyojengwa, suluhisho hizi za EdgeAI zinatoa msingi wa kizazi kijacho cha programu zenye akili zinazofanya kazi kwa ufanisi na kwa faragha kwenye ukingo.

Kila jukwaa linatoa faida za kipekee: Jetson Orin Nano kwa kompyuta ya ukingo iliyoharakishwa na vifaa, ONNX Runtime GenAI kwa maendeleo ya simu za mkononi za majukwaa mbalimbali, Azure EdgeAI kwa muunganisho wa wingu-ukingo wa biashara, Windows ML kwa programu za asili za Windows, na Foundry Local kwa utekelezaji wa RAG unaozingatia faragha. Pamoja, yanawakilisha ekosistimu kamili kwa maendeleo ya EdgeAI.

---

