<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T22:42:05+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "tl"
}
-->
# Foundry Local sa Windows (Validated)

Ang gabay na ito ay tumutulong sa iyo na i-install, patakbuhin, at i-integrate ang Microsoft Foundry Local sa Windows. Ang lahat ng hakbang at mga utos ay na-validate batay sa Microsoft Learn docs.

- Magsimula: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkitektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrate SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Compile HF Models (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) I-install / I-upgrade sa Windows

- I-install:
```cmd
winget install Microsoft.FoundryLocal
```
- I-upgrade:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Suriin ang bersyon:
```cmd
foundry --version
```

## 2) Mga Pangunahing Kaalaman sa CLI (Tatlong Kategorya)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Serbisyo:
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

Mga Tala:
- Ang serbisyo ay nagbibigay ng OpenAI-compatible REST API. Ang port ng endpoint ay dynamic na ina-allocate; gamitin ang `foundry service status` para matuklasan ito.
- Gamitin ang SDKs para sa kaginhawaan; awtomatikong hinahandle nila ang endpoint discovery kung suportado.

## 3) Tuklasin ang Lokal na Endpoint (Dynamic Port)

Ang Foundry Local ay nag-aassign ng dynamic na port tuwing nagsisimula ang serbisyo:
```cmd
foundry service status
```
Gamitin ang naiulat na `http://localhost:<PORT>` bilang iyong `base_url` kasama ang OpenAI-compatible paths (halimbawa, `/v1/chat/completions`).

## 4) Mabilisang Pagsubok gamit ang OpenAI Python SDK

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
Mga Sanggunian:
- SDK Integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Magdala ng Sariling Modelo (Compile gamit ang Olive)

Kung kailangan mo ng modelong wala sa catalog, i-compile ito sa ONNX para sa Foundry Local gamit ang Olive.

High-level flow (tingnan ang docs para sa mga hakbang):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Docs:
- BYOM compile: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Pag-troubleshoot

- Suriin ang status ng serbisyo at mga log:
```cmd
foundry service status
foundry service diag
```
- I-clear o ilipat ang cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Mag-update sa pinakabagong preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Kaugnay na Karanasan ng Windows Developer

- Mga pagpipilian sa Windows local vs cloud AI, kabilang ang Foundry Local at Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit gamit ang Foundry Local (gamitin ang `foundry service status` para makuha ang chat endpoint URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

