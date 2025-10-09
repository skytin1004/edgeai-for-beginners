<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-09T09:35:03+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "mr"
}
-->
# सत्र ३: फाउंड्री लोकलमधील ओपन-सोर्स मॉडेल्स

## सारांश

फाउंड्री लोकलमध्ये Hugging Face आणि इतर ओपन-सोर्स मॉडेल्स कसे आणायचे ते शोधा. निवड धोरणे, समुदाय योगदान कार्यप्रवाह, कार्यक्षमता तुलना पद्धती आणि सानुकूल मॉडेल नोंदणीसह फाउंड्री कशी विस्तारित करायची याबद्दल जाणून घ्या. हे सत्र साप्ताहिक "मॉडेल मंडे" अन्वेषण थीमशी जुळते आणि तुम्हाला ओपन-सोर्स मॉडेल्सचे मूल्यांकन आणि स्थानिक पातळीवर कार्यान्वित करण्यासाठी सुसज्ज करते, Azure वर स्केल करण्यापूर्वी.

## शिकण्याची उद्दिष्टे

सत्राच्या शेवटी तुम्ही हे करू शकाल:

- **शोधा आणि मूल्यांकन करा**: गुणवत्ता वि संसाधन व्यापार-बंद वापरून उमेदवार मॉडेल्स (mistral, gemma, qwen, deepseek) ओळखा.
- **लोड करा आणि चालवा**: फाउंड्री लोकल CLI वापरून समुदाय मॉडेल्स डाउनलोड, कॅश आणि लाँच करा.
- **बेंचमार्क**: सुसंगत विलंबता + टोकन थ्रूपुट + गुणवत्ता मेट्रिक्स लागू करा.
- **विस्तार करा**: SDK-सुसंगत पॅटर्नचे अनुसरण करून सानुकूल मॉडेल व्रॅपर नोंदणी किंवा अनुकूलित करा.
- **तुलना करा**: SLM वि मध्यम आकाराचे LLM निवड निर्णयांसाठी संरचित तुलना तयार करा.

## पूर्वअट

- सत्र १ आणि २ पूर्ण केलेले असणे आवश्यक आहे
- `foundry-local-sdk` सह Python वातावरण स्थापित केलेले असावे
- अनेक मॉडेल कॅशेससाठी किमान १५GB मोकळी जागा
- पर्यायी: GPU/WebGPU प्रवेग सक्षम (`foundry config list`)

### क्रॉस-प्लॅटफॉर्म वातावरण जलद प्रारंभ

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

जेव्हा macOS वरून Windows होस्ट सेवेसाठी बेंचमार्किंग करत असाल, तेव्हा सेट करा:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## डेमो फ्लो (३० मिनिटे)

### १. CLI द्वारे Hugging Face मॉडेल्स लोड करा (८ मिनिटे)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```

### २. चालवा आणि जलद तपासणी करा (५ मिनिटे)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### ३. बेंचमार्क स्क्रिप्ट (८ मिनिटे)

`samples/03-oss-models/benchmark_models.py` तयार करा:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

चालवा:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### ४. कार्यक्षमता तुलना (५ मिनिटे)

व्यापार-बंदांवर चर्चा करा: लोड वेळ, मेमरी फूटप्रिंट (Task Manager / `nvidia-smi` / OS रिसोर्स मॉनिटर पाहा), आउटपुट गुणवत्ता वि गती. विलंबता आणि थ्रूपुटसाठी Python बेंचमार्क स्क्रिप्ट (सत्र ३) वापरा; GPU प्रवेग सक्षम केल्यानंतर पुन्हा प्रयत्न करा.

### ५. स्टार्टर प्रकल्प (४ मिनिटे)

मॉडेल तुलना अहवाल जनरेटर तयार करा (बेंचमार्किंग स्क्रिप्टला मार्कडाउन निर्यातसह विस्तारित करा).

## स्टार्टर प्रकल्प: `03-huggingface-models` विस्तारित करा

अस्तित्वात असलेल्या नमुन्याला पुढीलप्रमाणे सुधारित करा:

1. बेंचमार्क एकत्रीकरण + CSV/Markdown आउटपुट जोडा.
2. साधे गुणात्मक स्कोअरिंग अंमलात आणा (प्रॉम्प्ट जोडी संच + मॅन्युअल अॅनोटेशन स्टब फाइल).
3. JSON कॉन्फिग (`models.json`) सादर करा प्लग करण्यायोग्य मॉडेल सूची आणि प्रॉम्प्ट संचासाठी.

## प्रमाणीकरण तपासणी यादी

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

सर्व लक्ष्य मॉडेल्स दिसावीत आणि प्रॉम्प्ट चॅट विनंतीला प्रतिसाद द्यावा.

## नमुना परिस्थिती आणि कार्यशाळा मॅपिंग

| कार्यशाळा स्क्रिप्ट | परिस्थिती | उद्दिष्ट | प्रॉम्प्ट / डेटासेट स्रोत |
|---------------------|------------|----------|---------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | एम्बेडेड समरीझरसाठी डिफॉल्ट SLM निवडणारी एज प्लॅटफॉर्म टीम | उमेदवार मॉडेल्समध्ये विलंबता + p95 + टोकन/सेकंद तुलना तयार करा | Inline `PROMPT` var + environment `BENCH_MODELS` सूची |

### परिस्थितीचे वर्णन
उत्पादन अभियांत्रिकीला ऑफलाइन मीटिंग-नोट्स वैशिष्ट्यासाठी डिफॉल्ट हलके समरीकरण मॉडेल निवडायचे आहे. ते निश्चित प्रॉम्प्ट संचावर (खालील उदाहरण पहा) नियंत्रित निर्धारक बेंचमार्क चालवतात आणि GPU प्रवेगासह आणि त्याशिवाय विलंबता + थ्रूपुट मेट्रिक्स गोळा करतात.

### उदाहरण प्रॉम्प्ट संच JSON (वाढवता येण्याजोगा)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

प्रत्येक मॉडेलसाठी प्रत्येक प्रॉम्प्ट लूप करा, वितरण मेट्रिक्स काढण्यासाठी प्रति-प्रॉम्प्ट विलंबता कॅप्चर करा आणि अपवाद शोधा.

## मॉडेल निवड फ्रेमवर्क

| परिमाण | मेट्रिक | का महत्त्वाचे आहे |
|--------|---------|--------------------|
| विलंबता | सरासरी / p95 | वापरकर्ता अनुभवाची सुसंगतता |
| थ्रूपुट | टोकन/सेकंद | बॅच आणि स्ट्रीमिंग स्केलेबिलिटी |
| मेमरी | निवासी आकार | डिव्हाइस फिट आणि एकत्रितता |
| गुणवत्ता | रुब्रिक प्रॉम्प्ट्स | कार्यासाठी उपयुक्तता |
| फूटप्रिंट | डिस्क कॅशे | वितरण आणि अद्यतने |
| परवाना | वापर परवानगी | व्यावसायिक अनुपालन |

## सानुकूल मॉडेलसह विस्तार

उच्च-स्तरीय पॅटर्न (छद्म):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

अधिकृत रेपो सल्ला घ्या विकसित होणाऱ्या अडॅप्टर इंटरफेससाठी:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## समस्या निवारण

| समस्या | कारण | उपाय |
|--------|-------|------|
| mistral-7b वर OOM | अपुरी RAM/GPU | इतर मॉडेल्स थांबवा; लहान प्रकार वापरा |
| पहिला प्रतिसाद मंद | कोल्ड लोड | हलक्या प्रॉम्प्टसह वेळोवेळी उबदार ठेवा |
| डाउनलोड थांबते | नेटवर्क अस्थिरता | पुन्हा प्रयत्न करा; ऑफ-पीक दरम्यान प्रीफेच करा |

## संदर्भ

- फाउंड्री लोकल SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- मॉडेल मंडे: https://aka.ms/model-mondays
- Hugging Face मॉडेल शोध: https://huggingface.co/models

---

**सत्र कालावधी**: ३० मिनिटे (+ पर्यायी सखोल अभ्यास)  
**अडचण पातळी**: मध्यम

### पर्यायी सुधारणा

| सुधारणा | फायदा | कसे |
|---------|-------|-----|
| स्ट्रीमिंग फर्स्ट-टोकन विलंबता | जाणवलेली प्रतिसादक्षमता मोजते | `BENCH_STREAM=1` सह बेंचमार्क चालवा (`Workshop/samples/session03` मधील सुधारित स्क्रिप्ट) |
| निर्धारक मोड | स्थिर पुनरावृत्ती तुलना | `temperature=0`, निश्चित प्रॉम्प्ट संच, JSON आउटपुट आवृत्ती नियंत्रणाखाली कॅप्चर करा |
| गुणवत्ता रुब्रिक स्कोअरिंग | गुणात्मक परिमाण जोडते | अपेक्षित पैलूंसह `prompts.json` राखा; स्कोअर्स (१–५) मॅन्युअली किंवा दुय्यम मॉडेलद्वारे अॅनोटेट करा |
| CSV / Markdown निर्यात | शेअर करण्यायोग्य अहवाल | `benchmark_report.md` टेबल आणि हायलाइट्ससह लिहिण्यासाठी स्क्रिप्ट विस्तारित करा |
| मॉडेल क्षमता टॅग | नंतर स्वयंचलित रूटिंगसाठी मदत करते | `{alias: {capabilities:[], size_mb:..}}` सह `models.json` राखा |
| कॅशे वॉर्मअप टप्पा | कोल्ड-स्टार्ट पूर्वग्रह कमी करा | वेळ लूप चालवण्यापूर्वी एक उबदार फेरी अंमलात आणा (आधीच अंमलात आणले आहे) |
| टक्केवारी अचूकता | मजबूत शेपटी विलंबता | numpy टक्केवारी वापरा (आधीच पुनर्रचित स्क्रिप्टमध्ये) |
| टोकन खर्च अंदाज | आर्थिक तुलना | अंदाजे खर्च = (टोकन/सेकंद * प्रति विनंती सरासरी टोकन) * ऊर्जा अनुमान |
| अयशस्वी मॉडेल्स आपोआप वगळणे | बॅच रनमध्ये लवचिकता | प्रत्येक बेंचमार्क try/except मध्ये लपेटा आणि स्थिती फील्ड चिन्हांकित करा |

#### किमान मार्कडाउन निर्यात स्निपेट

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### निर्धारक प्रॉम्प्ट संच उदाहरण

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

प्रतिबद्धांमध्ये तुलनात्मक मेट्रिक्ससाठी यादृच्छिक प्रॉम्प्ट्सऐवजी स्थिर सूची लूप करा.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.