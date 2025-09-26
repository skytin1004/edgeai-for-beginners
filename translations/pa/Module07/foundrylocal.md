<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "02b037f55de779607eb12edcc7a7fcf2",
  "translation_date": "2025-09-26T18:31:56+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "pa"
}
-->
# Foundry Local Windows ਅਤੇ Mac 'ਤੇ

ਇਹ ਗਾਈਡ ਤੁਹਾਨੂੰ Windows ਅਤੇ Mac 'ਤੇ Microsoft Foundry Local ਨੂੰ ਇੰਸਟਾਲ, ਚਲਾਉਣ ਅਤੇ ਇੰਟਿਗ੍ਰੇਟ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ। ਸਾਰੇ ਕਦਮ ਅਤੇ ਕਮਾਂਡ Microsoft Learn ਡੌਕਸ ਦੇ ਅਨੁਸਾਰ ਪ੍ਰਮਾਣਿਤ ਹਨ।

- ਸ਼ੁਰੂ ਕਰੋ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- ਆਰਕੀਟੈਕਚਰ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI ਰਿਫਰੈਂਸ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs ਨੂੰ ਇੰਟਿਗ੍ਰੇਟ ਕਰੋ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF ਮਾਡਲ (BYOM) ਕੰਪਾਇਲ ਕਰੋ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows 'ਤੇ ਇੰਸਟਾਲ / ਅਪਗ੍ਰੇਡ

- ਇੰਸਟਾਲ:
```cmd
winget install Microsoft.FoundryLocal
```
- ਅਪਗ੍ਰੇਡ:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- ਵਰਜਨ ਚੈੱਕ:
```cmd
foundry --version
```
     
**Mac 'ਤੇ ਇੰਸਟਾਲ**

**MacOS**: 
ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਚਲਾਓ:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI ਬੇਸਿਕਸ (ਤਿੰਨ ਸ਼੍ਰੇਣੀਆਂ)

- ਮਾਡਲ:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- ਸਰਵਿਸ:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- ਕੈਸ਼:
```cmd
foundry cache --help
foundry cache list
```

ਨੋਟਸ:
- ਸਰਵਿਸ OpenAI-ਕੰਪੈਟਿਬਲ REST API ਨੂੰ ਐਕਸਪੋਜ਼ ਕਰਦੀ ਹੈ। ਐਂਡਪੋਇੰਟ ਪੋਰਟ ਡਾਇਨੈਮਿਕ ਤਰੀਕੇ ਨਾਲ ਐਲੋਕੇਟ ਹੁੰਦੀ ਹੈ; ਇਸਨੂੰ ਖੋਜਣ ਲਈ `foundry service status` ਵਰਤੋ।
- ਸਹੂਲਤ ਲਈ SDKs ਵਰਤੋ; ਇਹ ਜਿੱਥੇ ਸਪੋਰਟ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਐਂਡਪੋਇੰਟ ਡਿਸਕਵਰੀ ਨੂੰ ਆਟੋਮੈਟਿਕ ਤਰੀਕੇ ਨਾਲ ਹੈਂਡਲ ਕਰਦੇ ਹਨ।

## 3) ਲੋਕਲ ਐਂਡਪੋਇੰਟ ਖੋਜੋ (ਡਾਇਨੈਮਿਕ ਪੋਰਟ)

Foundry Local ਹਰ ਵਾਰ ਸਰਵਿਸ ਸ਼ੁਰੂ ਹੋਣ 'ਤੇ ਇੱਕ ਡਾਇਨੈਮਿਕ ਪੋਰਟ ਐਲੋਕੇਟ ਕਰਦਾ ਹੈ:
```cmd
foundry service status
```
ਰਿਪੋਰਟ ਕੀਤੇ `http://localhost:<PORT>` ਨੂੰ OpenAI-ਕੰਪੈਟਿਬਲ ਪਾਥਸ ਨਾਲ ਆਪਣੇ `base_url` ਵਜੋਂ ਵਰਤੋ (ਉਦਾਹਰਨ ਲਈ, `/v1/chat/completions`)।

## 4) OpenAI Python SDK ਰਾਹੀਂ ਤੇਜ਼ ਟੈਸਟ

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
ਰਿਫਰੈਂਸ:
- SDK ਇੰਟਿਗ੍ਰੇਸ਼ਨ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) ਆਪਣਾ ਮਾਡਲ ਲਿਆਓ (Olive ਨਾਲ ਕੰਪਾਇਲ ਕਰੋ)

ਜੇ ਤੁਹਾਨੂੰ ਕੈਟਾਲੌਗ ਵਿੱਚ ਮਾਡਲ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ, ਤਾਂ ਇਸਨੂੰ Foundry Local ਲਈ ONNX ਵਿੱਚ ਕੰਪਾਇਲ ਕਰੋ Olive ਦੀ ਵਰਤੋਂ ਕਰਕੇ।

ਉੱਚ-ਸਤ੍ਹਾ ਪ੍ਰਕਿਰਿਆ (ਕਦਮਾਂ ਲਈ ਡੌਕਸ ਵੇਖੋ):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ਡੌਕਸ:
- BYOM ਕੰਪਾਇਲ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) ਟਰਬਲਸ਼ੂਟਿੰਗ

- ਸਰਵਿਸ ਸਟੇਟਸ ਅਤੇ ਲੌਗਸ ਚੈੱਕ ਕਰੋ:
```cmd
foundry service status
foundry service diag
```
- ਕੈਸ਼ ਕਲੀਅਰ ਜਾਂ ਮੂਵ ਕਰੋ:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- ਨਵੀਂ ਪ੍ਰੀਵਿਊ ਵਿੱਚ ਅਪਡੇਟ ਕਰੋ:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) ਸੰਬੰਧਿਤ Windows ਡਿਵੈਲਪਰ ਅਨੁਭਵ

- Windows ਲੋਕਲ ਅਤੇ ਕਲਾਉਡ AI ਚੋਣਾਂ, ਜਿਸ ਵਿੱਚ Foundry Local ਅਤੇ Windows ML ਸ਼ਾਮਲ ਹਨ:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit Foundry Local ਨਾਲ (ਚੈਟ ਐਂਡਪੋਇੰਟ URL ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ `foundry service status` ਵਰਤੋ):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

