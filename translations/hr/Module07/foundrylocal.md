<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-23T01:23:06+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "hr"
}
-->
# Foundry Local na Windowsu (Provjereno)

Ovaj vodič pomaže vam instalirati, pokrenuti i integrirati Microsoft Foundry Local na Windowsu. Svi koraci i naredbe provjereni su prema Microsoft Learn dokumentaciji.

- Početak: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arhitektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Referenca: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integracija SDK-ova: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompilacija HF modela (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokalno vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Instalacija / Nadogradnja na Windowsu

- Instalacija:
```cmd
winget install Microsoft.FoundryLocal
```
- Nadogradnja:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Provjera verzije:
```cmd
foundry --version
```

## 2) Osnove CLI-a (Tri kategorije)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Servis:
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

Napomene:
- Servis pruža REST API kompatibilan s OpenAI-jem. Port za endpoint se dinamički dodjeljuje; koristite `foundry service status` za otkrivanje.
- Koristite SDK-ove radi praktičnosti; oni automatski otkrivaju endpoint gdje je podržano.

## 3) Otkrivanje lokalnog endpointa (Dinamički port)

Foundry Local dodjeljuje dinamički port svaki put kad se servis pokrene:
```cmd
foundry service status
```
Koristite prijavljeni `http://localhost:<PORT>` kao vaš `base_url` s OpenAI-kompatibilnim putanjama (na primjer, `/v1/chat/completions`).

## 4) Brzi test putem OpenAI Python SDK-a

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
- Integracija SDK-a: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Donošenje vlastitog modela (Kompilacija s Olive)

Ako vam je potreban model koji nije u katalogu, kompilirajte ga u ONNX za Foundry Local koristeći Olive.

Visokorazinski tijek (pogledajte dokumentaciju za korake):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentacija:
- Kompilacija BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Rješavanje problema

- Provjera statusa servisa i logova:
```cmd
foundry service status
foundry service diag
```
- Brisanje ili premještanje cachea:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Nadogradnja na najnoviji pregled:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Povezano iskustvo za Windows developere

- Lokalni vs cloud AI izbori na Windowsu, uključujući Foundry Local i Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit s Foundry Local (koristite `foundry service status` za dobivanje URL-a za chat endpoint):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

