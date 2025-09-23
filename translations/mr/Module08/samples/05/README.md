<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T17:47:30+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "mr"
}
-->
# सत्र ५ नमुना: मल्टी-एजंट ऑर्केस्ट्रेशन

हा नमुना Foundry Local च्या OpenAI-सुसंगत एन्डपॉइंट वापरून समन्वयक + विशेषज्ञ पद्धतीचे प्रदर्शन करतो.

## चालवा (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## सत्यापित करा
```cmd
curl http://localhost:8000/v1/models
```

## समस्या निराकरण
- जर VS Code मध्ये `import specialists` `coordinator.py` मध्ये अनसुलझले म्हणून दाखवत असेल, तर खात्री करा की तुम्ही मॉड्यूल म्हणून चालवत आहात आणि इंटरप्रिटर `Module08/.venv` कडे निर्देशित आहे:
	- चालवा: `python -m samples.05.agents.coordinator`
	- इंटरप्रिटर निवडा: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## संदर्भ
- Foundry Local (शिका): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents आढावा: https://learn.microsoft.com/azure/ai-services/agents/overview
- फंक्शन कॉलिंग नमुना (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

