<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T12:58:14+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "de"
}
-->
# Sitzung 6 Beispiel: Modelle als Werkzeuge

Dieses Beispiel implementiert einen minimalen Router + Tool-Registry, der ein Modell basierend auf der Benutzeranfrage auswählt und den OpenAI-kompatiblen Endpunkt von Foundry Local aufruft.

## Dateien
- `router.py`: einfache Registrierung und heuristische Weiterleitung; Endpunkt-Erkennung + Gesundheitsprüfung.

## Ausführen (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Hinweise
- Der Router verwendet einfache Schlüsselwort-Heuristiken, um zwischen den Werkzeugen `general`, `reasoning` und `code` zu wählen und gibt `/v1/models` beim Start aus.
- Konfiguration über Umgebungsvariablen:
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

## Referenzen
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integration mit Inferenz-SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

