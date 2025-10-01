<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f0c6af41a1ae2c5a770c8170da8bd6e",
  "translation_date": "2025-10-01T01:28:19+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "ro"
}
-->
# Sesiunea 6 Exemplu: Modele ca Instrumente

Acest exemplu implementează un router minimal + registru de instrumente care selectează un model pe baza solicitării utilizatorului și apelează endpoint-ul compatibil OpenAI al Foundry Local.

## Fișiere
- `router.py`: registru simplu și rutare euristică; descoperirea endpoint-ului + verificarea stării de funcționare.

## Executare (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Note
- Routerul folosește euristici simple bazate pe cuvinte cheie pentru a alege între instrumentele `general`, `reasoning` și `code` și afișează `/v1/models` la pornire.
- Configurare prin variabile de mediu:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## Referințe
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrare cu SDK-uri de inferență: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.