<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T20:27:01+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "fi"
}
-->
# Foundry Local Windowsilla (Vahvistettu)

Tämä opas auttaa sinua asentamaan, käyttämään ja integroimaan Microsoft Foundry Localin Windowsilla. Kaikki vaiheet ja komennot on vahvistettu Microsoft Learn -dokumentaation perusteella.

- Aloita: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkkitehtuuri: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-viite: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK-integrointi: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF-mallien kääntäminen (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Paikallinen vs pilvi: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Asenna / Päivitä Windowsilla

- Asenna:
```cmd
winget install Microsoft.FoundryLocal
```
- Päivitä:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versiotarkistus:
```cmd
foundry --version
```

## 2) CLI-perusteet (Kolme kategoriaa)

- Malli:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Palvelu:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Välimuisti:
```cmd
foundry cache --help
foundry cache list
```

Huomioita:
- Palvelu tarjoaa OpenAI-yhteensopivan REST-rajapinnan. Endpoint-portti määritetään dynaamisesti; käytä `foundry service status` sen löytämiseksi.
- Käytä SDK:ita helppouden vuoksi; ne hoitavat endpointin automaattisen tunnistamisen, jos tuettu.

## 3) Paikallisen endpointin löytäminen (Dynaaminen portti)

Foundry Local määrittää dynaamisen portin aina, kun palvelu käynnistyy:
```cmd
foundry service status
```
Käytä ilmoitettua `http://localhost:<PORT>` osoitteena `base_url` OpenAI-yhteensopivilla poluilla (esimerkiksi `/v1/chat/completions`).

## 4) Pikatesti OpenAI Python SDK:lla

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
Viitteet:
- SDK-integrointi: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Oma malli (Käännä Olive-työkalulla)

Jos tarvitset mallin, jota ei ole katalogissa, käännä se ONNX-muotoon Foundry Localia varten Olive-työkalulla.

Korkean tason prosessi (katso dokumentaatio vaiheista):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentaatio:
- BYOM-kääntäminen: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Vianmääritys

- Tarkista palvelun tila ja lokit:
```cmd
foundry service status
foundry service diag
```
- Tyhjennä tai siirrä välimuisti:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Päivitä uusimpaan esikatseluun:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Liittyvä Windows-kehittäjäkokemus

- Windowsin paikalliset vs pilvi-AI-vaihtoehdot, mukaan lukien Foundry Local ja Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit Foundry Localin kanssa (käytä `foundry service status` saadaksesi chat-endpointin URL-osoitteen):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

