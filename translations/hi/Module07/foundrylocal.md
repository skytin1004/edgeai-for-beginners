<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T13:42:00+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "hi"
}
-->
# Windows पर Foundry Local (सत्यापित)

यह गाइड आपको Windows पर Microsoft Foundry Local को इंस्टॉल, चलाने और इंटीग्रेट करने में मदद करता है। सभी चरण और कमांड Microsoft Learn डॉक्यूमेंट्स के अनुसार सत्यापित हैं।

- शुरुआत करें: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- आर्किटेक्चर: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI संदर्भ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs को इंटीग्रेट करें: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF मॉडल्स को कंपाइल करें (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local बनाम Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows पर इंस्टॉल / अपग्रेड करें

- इंस्टॉल:
```cmd
winget install Microsoft.FoundryLocal
```
- अपग्रेड:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- वर्जन जांचें:
```cmd
foundry --version
```

## 2) CLI बेसिक्स (तीन श्रेणियां)

- मॉडल:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- सर्विस:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- कैश:
```cmd
foundry cache --help
foundry cache list
```

नोट्स:
- सर्विस OpenAI-संगत REST API को एक्सपोज़ करती है। एंडपॉइंट पोर्ट डायनामिक रूप से अलॉट किया जाता है; इसे खोजने के लिए `foundry service status` का उपयोग करें।
- सुविधा के लिए SDKs का उपयोग करें; ये स्वचालित रूप से एंडपॉइंट डिस्कवरी को संभालते हैं जहां समर्थित हो।

## 3) लोकल एंडपॉइंट खोजें (डायनामिक पोर्ट)

Foundry Local हर बार सर्विस शुरू होने पर डायनामिक पोर्ट असाइन करता है:
```cmd
foundry service status
```
रिपोर्ट किए गए `http://localhost:<PORT>` को OpenAI-संगत पाथ्स (जैसे, `/v1/chat/completions`) के साथ अपने `base_url` के रूप में उपयोग करें।

## 4) OpenAI Python SDK के माध्यम से त्वरित परीक्षण

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
- SDK इंटीग्रेशन: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) अपना मॉडल लाएं (Olive के साथ कंपाइल करें)

यदि आपको कैटलॉग में उपलब्ध मॉडल की आवश्यकता नहीं है, तो इसे Olive का उपयोग करके Foundry Local के लिए ONNX में कंपाइल करें।

उच्च-स्तरीय प्रक्रिया (चरणों के लिए डॉक देखें):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
डॉक:
- BYOM कंपाइल: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) समस्या निवारण

- सर्विस स्टेटस और लॉग्स जांचें:
```cmd
foundry service status
foundry service diag
```
- कैश को साफ करें या स्थानांतरित करें:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- नवीनतम प्रीव्यू में अपडेट करें:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) संबंधित Windows डेवलपर अनुभव

- Windows लोकल बनाम क्लाउड AI विकल्प, जिसमें Foundry Local और Windows ML शामिल हैं:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit Foundry Local के साथ (चैट एंडपॉइंट URL प्राप्त करने के लिए `foundry service status` का उपयोग करें):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

