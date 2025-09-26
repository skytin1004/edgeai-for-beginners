<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "02b037f55de779607eb12edcc7a7fcf2",
  "translation_date": "2025-09-26T18:53:25+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "hu"
}
-->
# Foundry Local Windows és Mac rendszeren

Ez az útmutató segít telepíteni, futtatni és integrálni a Microsoft Foundry Local-t Windows és Mac rendszeren. Minden lépés és parancs a Microsoft Learn dokumentáció alapján lett ellenőrizve.

- Kezdés: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektúra: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Referencia: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK-k integrálása: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF modellek fordítása (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokális vs Felhő: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Telepítés / Frissítés Windows rendszeren

- Telepítés:
```cmd
winget install Microsoft.FoundryLocal
```
- Frissítés:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Verzió ellenőrzése:
```cmd
foundry --version
```
     
**Telepítés / Mac**

**MacOS**: 
Nyiss meg egy terminált, és futtasd az alábbi parancsot:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI Alapok (Három Kategória)

- Modell:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Szolgáltatás:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Gyorsítótár:
```cmd
foundry cache --help
foundry cache list
```

Megjegyzések:
- A szolgáltatás egy OpenAI-kompatibilis REST API-t biztosít. A végpont portja dinamikusan van kiosztva; használd a `foundry service status` parancsot a felfedezéshez.
- Használd az SDK-kat a kényelem érdekében; ezek automatikusan kezelik a végpont felfedezését, ahol támogatott.

## 3) Lokális Végpont Felfedezése (Dinamikus Port)

A Foundry Local minden indításkor dinamikus portot rendel:
```cmd
foundry service status
```
Használd a jelentett `http://localhost:<PORT>` címet `base_url`-ként OpenAI-kompatibilis útvonalakkal (például `/v1/chat/completions`).

## 4) Gyors Teszt OpenAI Python SDK-val

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
Referenciák:
- SDK Integráció: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Saját Modell Hozása (Fordítás Olive-val)

Ha szükséged van egy modellre, amely nem szerepel a katalógusban, fordítsd ONNX formátumba a Foundry Local számára Olive segítségével.

Magas szintű folyamat (lásd a dokumentációban a lépéseket):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentáció:
- BYOM fordítás: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Hibakeresés

- Szolgáltatás állapotának és naplóinak ellenőrzése:
```cmd
foundry service status
foundry service diag
```
- Gyorsítótár törlése vagy áthelyezése:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Frissítés a legújabb előzetes verzióra:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Kapcsolódó Windows Fejlesztői Élmény

- Windows lokális vs felhő AI választások, beleértve a Foundry Local-t és a Windows ML-t:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit Foundry Local-lal (használd a `foundry service status` parancsot a chat végpont URL-jének megszerzéséhez):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

