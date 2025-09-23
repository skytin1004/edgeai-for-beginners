<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T20:26:15+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "fi"
}
-->
# Istunto 6 Esimerkki: Mallit työkaluina

Tämä esimerkki toteuttaa yksinkertaisen reitittimen + työkalurekisterin, joka valitsee mallin käyttäjän kehotteen perusteella ja kutsuu Foundry Localin OpenAI-yhteensopivaa päätepistettä.

## Tiedostot
- `router.py`: yksinkertainen rekisteri ja heuristinen reititys; päätepisteen haku + terveystarkistus.

## Suorita (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Huomioita
- Reititin käyttää yksinkertaisia avainsanaheuristiikkoja valitakseen `general`, `reasoning` ja `code` työkalujen välillä ja tulostaa `/v1/models` käynnistyksen yhteydessä.
- Konfiguroi ympäristömuuttujien avulla:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-distill-qwen-7b"},"code":{"model":"qwen2.5-7b-instruct"}}
```

## Viitteet
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrointi inferenssi-SDK:iden kanssa: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

