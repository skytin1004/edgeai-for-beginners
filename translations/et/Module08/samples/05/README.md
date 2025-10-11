<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-10-11T12:56:53+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "et"
}
-->
# Sessioon 5 Näidis: Mitmeagendi Orkestreerimine

See näidis demonstreerib koordinaatori + spetsialistide mustrit, kasutades Foundry Locali OpenAI-ühilduvat lõpp-punkti.

## Käivitamine (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Kontrollimine
```cmd
curl http://localhost:8000/v1/models
```

## Tõrkeotsing
- Kui VS Code märgib `import specialists` lahendamata `coordinator.py` failis, veendu, et käivitad moodulina ja tõlgendaja osutab `Module08/.venv`-ile:
	- Käivita: `python -m samples.05.agents.coordinator`
	- Vali tõlgendaja: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Viited
- Foundry Local (Õpi): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agentide ülevaade: https://learn.microsoft.com/azure/ai-services/agents/overview
- Funktsioonikutsumise näidis (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.