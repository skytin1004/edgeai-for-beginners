<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T17:48:29+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "mr"
}
-->
# Windows वर Foundry Local (प्रमाणित)

ही मार्गदर्शिका Microsoft Foundry Local Windows वर स्थापित, चालवणे आणि समाकलित करण्यास मदत करते. सर्व चरण आणि आदेश Microsoft Learn दस्तऐवजांनुसार प्रमाणित आहेत.

- सुरुवात करा: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- आर्किटेक्चर: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI संदर्भ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs समाकलित करा: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF मॉडेल्स संकलित करा (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: स्थानिक विरुद्ध क्लाउड: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows वर स्थापित / अपग्रेड करा

- स्थापित:
```cmd
winget install Microsoft.FoundryLocal
```
- अपग्रेड:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- आवृत्ती तपासा:
```cmd
foundry --version
```

## 2) CLI मूलभूत गोष्टी (तीन श्रेणी)

- मॉडेल:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- सेवा:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- कॅशे:
```cmd
foundry cache --help
foundry cache list
```

टीप:
- सेवा OpenAI-सुसंगत REST API उघडते. एंडपॉइंट पोर्ट डायनॅमिकली नियुक्त केला जातो; `foundry service status` वापरून तो शोधा.
- सोयीसाठी SDKs वापरा; ते समर्थित ठिकाणी एंडपॉइंट शोध आपोआप हाताळतात.

## 3) स्थानिक एंडपॉइंट शोधा (डायनॅमिक पोर्ट)

Foundry Local प्रत्येक वेळी सेवा सुरू झाल्यावर डायनॅमिक पोर्ट नियुक्त करते:
```cmd
foundry service status
```
नमूद केलेला `http://localhost:<PORT>` OpenAI-सुसंगत पथांसह (`/v1/chat/completions` उदाहरणार्थ) तुमचा `base_url` म्हणून वापरा.

## 4) OpenAI Python SDK द्वारे जलद चाचणी

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
संदर्भ:
- SDK समाकलन: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) तुमचे स्वतःचे मॉडेल आणा (Olive सह संकलित करा)

जर तुम्हाला कॅटलॉगमध्ये नसलेले मॉडेल आवश्यक असेल, तर ते Olive वापरून Foundry Local साठी ONNX मध्ये संकलित करा.

उच्च-स्तरीय प्रवाह (चरणांसाठी दस्तऐवज पहा):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
दस्तऐवज:
- BYOM संकलन: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) समस्या निवारण

- सेवा स्थिती आणि लॉग तपासा:
```cmd
foundry service status
foundry service diag
```
- कॅशे साफ करा किंवा हलवा:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- नवीनतम प्रीव्ह्यूमध्ये अपडेट करा:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) संबंधित Windows विकसक अनुभव

- Windows स्थानिक विरुद्ध क्लाउड AI पर्याय, ज्यामध्ये Foundry Local आणि Windows ML समाविष्ट आहे:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit Foundry Local सह (चॅट एंडपॉइंट URL मिळवण्यासाठी `foundry service status` वापरा):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

