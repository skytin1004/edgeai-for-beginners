<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T18:34:46+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "it"
}
-->
# Sessione 6 Esempio: Modelli come Strumenti

Questo esempio implementa un router minimale + registro degli strumenti che seleziona un modello basandosi sul prompt dell'utente e chiama l'endpoint compatibile con OpenAI di Foundry Local.

## File
- `router.py`: registro semplice e routing euristico; scoperta degli endpoint + controllo dello stato.

## Esecuzione (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Note
- Il router utilizza semplici euristiche basate su parole chiave per scegliere tra gli strumenti `general`, `reasoning` e `code` e stampa `/v1/models` all'avvio.
- Configurazione tramite variabili d'ambiente:
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

## Riferimenti
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrazione con SDK di inferenza: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

