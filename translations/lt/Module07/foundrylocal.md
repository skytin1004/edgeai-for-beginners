<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-23T01:23:46+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "lt"
}
-->
# Foundry Local Windows platformoje (Patvirtinta)

Šis vadovas padės jums įdiegti, paleisti ir integruoti Microsoft Foundry Local Windows platformoje. Visi žingsniai ir komandos patvirtinti pagal Microsoft Learn dokumentaciją.

- Pradėti: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektūra: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI nuoroda: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK integracija: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF modelių kompiliavimas (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: vietinis vs debesų sprendimas: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Įdiegimas / Atnaujinimas Windows platformoje

- Įdiegimas:
```cmd
winget install Microsoft.FoundryLocal
```
- Atnaujinimas:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versijos patikrinimas:
```cmd
foundry --version
```

## 2) CLI pagrindai (Trys kategorijos)

- Modelis:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Paslauga:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Talpykla:
```cmd
foundry cache --help
foundry cache list
```

Pastabos:
- Paslauga teikia OpenAI suderinamą REST API. Prievado numeris priskiriamas dinamiškai; naudokite `foundry service status`, kad jį sužinotumėte.
- Naudokite SDK, kad būtų patogiau; jie automatiškai aptinka galinius taškus, kur tai palaikoma.

## 3) Vietinio galinio taško aptikimas (Dinaminis prievadas)

Foundry Local kiekvieną kartą paleidžiant paslaugą priskiria dinaminį prievadą:
```cmd
foundry service status
```
Naudokite nurodytą `http://localhost:<PORT>` kaip savo `base_url` su OpenAI suderinamais keliais (pvz., `/v1/chat/completions`).

## 4) Greitas testavimas naudojant OpenAI Python SDK

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
Nuorodos:
- SDK integracija: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Naudokite savo modelį (Kompiliavimas su Olive)

Jei jums reikia modelio, kurio nėra kataloge, kompiliuokite jį į ONNX formatą Foundry Local naudojant Olive.

Aukšto lygio procesas (žr. dokumentaciją dėl žingsnių):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentacija:
- BYOM kompiliavimas: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Trikčių šalinimas

- Paslaugos būsenos ir žurnalų patikrinimas:
```cmd
foundry service status
foundry service diag
```
- Talpyklos išvalymas arba perkėlimas:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Atnaujinimas į naujausią peržiūrą:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Susijusi Windows kūrėjų patirtis

- Windows vietinio ir debesų AI pasirinkimai, įskaitant Foundry Local ir Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI įrankių rinkinys su Foundry Local (naudokite `foundry service status`, kad gautumėte pokalbių galinio taško URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

