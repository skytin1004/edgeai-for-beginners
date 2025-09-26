<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "02b037f55de779607eb12edcc7a7fcf2",
  "translation_date": "2025-09-26T18:51:29+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "sw"
}
-->
# Foundry Local kwenye Windows & Mac

Mwongozo huu unakusaidia kusakinisha, kuendesha, na kuunganisha Microsoft Foundry Local kwenye Windows na Mac. Hatua zote na amri zimehakikiwa kulingana na nyaraka za Microsoft Learn.

- Anza: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Muundo: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Marejeleo ya CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Unganisha SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kusanya HF Models (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Sakinisha / Sasisha kwenye Windows

- Sakinisha:
```cmd
winget install Microsoft.FoundryLocal
```
- Sasisha:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Angalia toleo:
```cmd
foundry --version
```
     
**Sakinisha / Mac**

**MacOS**: 
Fungua terminal na endesha amri ifuatayo:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Misingi ya CLI (Makundi Matatu)

- Modeli:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Huduma:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Maelezo:
- Huduma inatoa API ya REST inayofanana na OpenAI. Bandari ya mwisho inatolewa kwa njia ya nguvu; tumia `foundry service status` kugundua.
- Tumia SDKs kwa urahisi; zinashughulikia ugunduzi wa bandari kiotomatiki pale inapowezekana.

## 3) Gundua Endpoint ya Local (Dynamic Port)

Foundry Local inatoa bandari ya nguvu kila mara huduma inapoanza:
```cmd
foundry service status
```
Tumia `http://localhost:<PORT>` iliyoripotiwa kama `base_url` yako na njia zinazofanana na OpenAI (kwa mfano, `/v1/chat/completions`).

## 4) Jaribio la Haraka kupitia OpenAI Python SDK

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
Marejeleo:
- SDK Integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Leta Modeli Yako (Kusanya na Olive)

Ikiwa unahitaji modeli ambayo haipo kwenye katalogi, iunganishe kwa ONNX kwa Foundry Local ukitumia Olive.

Mtiririko wa kiwango cha juu (tazama nyaraka kwa hatua):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Nyaraka:
- BYOM compile: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Utatuzi wa Matatizo

- Angalia hali ya huduma na kumbukumbu:
```cmd
foundry service status
foundry service diag
```
- Futa au hamisha cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Sasisha hadi toleo la hivi karibuni la preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Uzoefu Husika wa Mjenzi wa Windows

- Chaguo za AI za local vs cloud kwenye Windows, ikijumuisha Foundry Local na Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit na Foundry Local (tumia `foundry service status` kupata URL ya endpoint ya mazungumzo):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

