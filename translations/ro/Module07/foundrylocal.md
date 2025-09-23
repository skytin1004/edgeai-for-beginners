<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-23T01:22:35+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "ro"
}
-->
# Foundry Local pe Windows (Validat)

Acest ghid te ajută să instalezi, rulezi și integrezi Microsoft Foundry Local pe Windows. Toți pașii și comenzile sunt validate conform documentației Microsoft Learn.

- Începe: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arhitectură: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referință CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrare SDK-uri: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Compilare modele HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Instalare / Upgrade pe Windows

- Instalare:
```cmd
winget install Microsoft.FoundryLocal
```
- Upgrade:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Verificare versiune:
```cmd
foundry --version
```

## 2) Bazele CLI (Trei Categorii)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Serviciu:
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

Note:
- Serviciul expune un API REST compatibil cu OpenAI. Portul endpoint-ului este alocat dinamic; folosește `foundry service status` pentru a-l descoperi.
- Folosește SDK-urile pentru comoditate; acestea gestionează automat descoperirea endpoint-ului acolo unde este suportat.

## 3) Descoperirea Endpoint-ului Local (Port Dinamic)

Foundry Local alocă un port dinamic de fiecare dată când serviciul pornește:
```cmd
foundry service status
```
Folosește `http://localhost:<PORT>` raportat ca `base_url` împreună cu căile compatibile OpenAI (de exemplu, `/v1/chat/completions`).

## 4) Test Rapid prin OpenAI Python SDK

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
Referințe:
- Integrare SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Adaugă Modelul Tău (Compilează cu Olive)

Dacă ai nevoie de un model care nu este în catalog, compilează-l în ONNX pentru Foundry Local folosind Olive.

Flux de nivel înalt (vezi documentația pentru pași):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Documentație:
- Compilare BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Depanare

- Verifică statusul serviciului și logurile:
```cmd
foundry service status
foundry service diag
```
- Șterge sau mută cache-ul:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Actualizează la cea mai recentă versiune preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Experiența Dezvoltatorului Windows Asociată

- Alegeri AI local vs cloud pe Windows, inclusiv Foundry Local și Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit cu Foundry Local (folosește `foundry service status` pentru a obține URL-ul endpoint-ului de chat):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

