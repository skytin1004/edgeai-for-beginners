<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T19:24:11+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "sv"
}
-->
# Foundry Local på Windows (Verifierad)

Den här guiden hjälper dig att installera, köra och integrera Microsoft Foundry Local på Windows. Alla steg och kommandon är verifierade mot Microsoft Learn-dokumentation.

- Kom igång: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkitektur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-referens: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrera SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompilera HF-modeller (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokalt vs moln: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Installera / Uppgradera på Windows

- Installera:
```cmd
winget install Microsoft.FoundryLocal
```
- Uppgradera:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versionskontroll:
```cmd
foundry --version
```

## 2) CLI-grunder (Tre kategorier)

- Modell:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Tjänst:
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

Kommentarer:
- Tjänsten exponerar ett OpenAI-kompatibelt REST API. Porten för endpointen tilldelas dynamiskt; använd `foundry service status` för att upptäcka den.
- Använd SDK:erna för enkelhet; de hanterar endpoint-upptäckt automatiskt där det stöds.

## 3) Upptäck den lokala endpointen (Dynamisk port)

Foundry Local tilldelar en dynamisk port varje gång tjänsten startar:
```cmd
foundry service status
```
Använd den rapporterade `http://localhost:<PORT>` som din `base_url` med OpenAI-kompatibla sökvägar (till exempel `/v1/chat/completions`).

## 4) Snabbtest via OpenAI Python SDK

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
Referenser:
- SDK-integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Ta med din egen modell (Kompilera med Olive)

Om du behöver en modell som inte finns i katalogen, kompilera den till ONNX för Foundry Local med Olive.

Översikt (se dokumentationen för steg):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentation:
- BYOM-kompilering: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Felsökning

- Kontrollera tjänstens status och loggar:
```cmd
foundry service status
foundry service diag
```
- Rensa eller flytta cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Uppdatera till senaste förhandsversion:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Relaterad Windows-utvecklarupplevelse

- Val mellan lokal och molnbaserad AI på Windows, inklusive Foundry Local och Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit med Foundry Local (använd `foundry service status` för att få chat-endpointens URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

