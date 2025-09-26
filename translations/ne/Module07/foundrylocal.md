<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "02b037f55de779607eb12edcc7a7fcf2",
  "translation_date": "2025-09-26T18:30:16+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "ne"
}
-->
# Windows र Mac मा Foundry Local

यो गाइडले तपाईंलाई Windows र Mac मा Microsoft Foundry Local स्थापना, चलाउने, र एकीकृत गर्न मद्दत गर्दछ। सबै चरणहरू र कमाण्डहरू Microsoft Learn डकुमेन्ट्ससँग प्रमाणित छन्।

- सुरु गर्नुहोस्: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- आर्किटेक्चर: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI सन्दर्भ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs एकीकृत गर्नुहोस्: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF मोडेलहरू कम्पाइल गर्नुहोस् (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## १) Windows मा स्थापना / अपग्रेड गर्नुहोस्

- स्थापना:
```cmd
winget install Microsoft.FoundryLocal
```
- अपग्रेड:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- संस्करण जाँच:
```cmd
foundry --version
```
     
**स्थापना / Mac**

**MacOS**: 
टर्मिनल खोल्नुहोस् र निम्न कमाण्ड चलाउनुहोस्:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## २) CLI आधारभूत (तीन श्रेणीहरू)

- मोडेल:
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
- क्यास:
```cmd
foundry cache --help
foundry cache list
```

नोटहरू:
- सेवा OpenAI-संगत REST API प्रदान गर्दछ। एन्डप्वइन्ट पोर्ट गतिशील रूपमा छुट्याइन्छ; `foundry service status` प्रयोग गरेर यसलाई पत्ता लगाउनुहोस्।
- सुविधा को लागि SDKs प्रयोग गर्नुहोस्; तिनीहरूले एन्डप्वइन्ट डिस्कभरी स्वचालित रूपमा ह्यान्डल गर्छन् जहाँ समर्थित छ।

## ३) स्थानीय एन्डप्वइन्ट पत्ता लगाउनुहोस् (डायनामिक पोर्ट)

Foundry Local ले प्रत्येक पटक सेवा सुरु हुँदा गतिशील पोर्ट छुट्याउँछ:
```cmd
foundry service status
```
रिपोर्ट गरिएको `http://localhost:<PORT>` लाई OpenAI-संगत पथहरूसँग `base_url` को रूपमा प्रयोग गर्नुहोस् (उदाहरणका लागि, `/v1/chat/completions`)।

## ४) OpenAI Python SDK मार्फत छिटो परीक्षण

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
सन्दर्भहरू:
- SDK एकीकरण: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## ५) आफ्नो मोडेल ल्याउनुहोस् (Olive प्रयोग गरेर कम्पाइल गर्नुहोस्)

यदि तपाईंलाई क्याटलगमा उपलब्ध मोडेल चाहिएको छैन भने, Olive प्रयोग गरेर Foundry Local को लागि यसलाई ONNX मा कम्पाइल गर्नुहोस्।

उच्च-स्तरीय प्रवाह (चरणहरूको लागि डकुमेन्ट्स हेर्नुहोस्):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
डकुमेन्ट्स:
- BYOM कम्पाइल: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## ६) समस्या समाधान

- सेवा स्थिति र लगहरू जाँच गर्नुहोस्:
```cmd
foundry service status
foundry service diag
```
- क्यास खाली गर्नुहोस् वा सार्नुहोस्:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- पछिल्लो प्रिभ्यूमा अपडेट गर्नुहोस्:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## ७) सम्बन्धित Windows डेभलपर अनुभव

- Windows स्थानीय बनाम क्लाउड AI विकल्पहरू, जसमा Foundry Local र Windows ML समावेश छन्:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit Foundry Local सँग (च्याट एन्डप्वइन्ट URL प्राप्त गर्न `foundry service status` प्रयोग गर्नुहोस्):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

