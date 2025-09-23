<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-23T01:23:15+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "sl"
}
-->
# Foundry Local na Windows (Preverjeno)

Ta vodič vam pomaga namestiti, zagnati in integrirati Microsoft Foundry Local na Windows. Vsi koraki in ukazi so preverjeni glede na dokumentacijo Microsoft Learn.

- Začetek: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arhitektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Referenca: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integracija SDK-jev: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompilacija HF modelov (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokalno vs oblak: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Namestitev / Nadgradnja na Windows

- Namestitev:
```cmd
winget install Microsoft.FoundryLocal
```
- Nadgradnja:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Preverjanje verzije:
```cmd
foundry --version
```

## 2) Osnove CLI (Tri kategorije)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Storitev:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Predpomnilnik:
```cmd
foundry cache --help
foundry cache list
```

Opombe:
- Storitev omogoča REST API, združljiv z OpenAI. Vrata za dostop so dinamično dodeljena; uporabite `foundry service status`, da jih odkrijete.
- Uporabite SDK-je za lažjo uporabo; ti samodejno odkrijejo dostopne točke, kjer je to podprto.

## 3) Odkrijte lokalno dostopno točko (Dinamična vrata)

Foundry Local dodeli dinamična vrata ob vsakem zagonu storitve:
```cmd
foundry service status
```
Uporabite poročani `http://localhost:<PORT>` kot vaš `base_url` z OpenAI združljivimi potmi (na primer, `/v1/chat/completions`).

## 4) Hitri test prek OpenAI Python SDK

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
Reference:
- Integracija SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Prinesite svoj model (Kompilacija z Olive)

Če potrebujete model, ki ni v katalogu, ga kompilirajte v ONNX za Foundry Local z uporabo Olive.

Visok nivo poteka (glejte dokumentacijo za korake):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentacija:
- Kompilacija BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Odpravljanje težav

- Preverite status storitve in dnevnike:
```cmd
foundry service status
foundry service diag
```
- Počistite ali premaknite predpomnilnik:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Posodobite na najnovejšo predogledno različico:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Povezana izkušnja za razvijalce na Windows

- Izbire med lokalno in oblačno AI na Windows, vključno s Foundry Local in Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit z Foundry Local (uporabite `foundry service status`, da pridobite URL dostopne točke za klepet):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

