<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T18:34:24+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "br"
}
-->
# Sessão 5 Exemplo: Orquestração Multi-Agente

Este exemplo demonstra o padrão coordenador + especialistas usando o endpoint compatível com OpenAI do Foundry Local.

## Executar (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validar
```cmd
curl http://localhost:8000/v1/models
```

## Solução de Problemas
- Se o VS Code marcar `import specialists` como não resolvido em `coordinator.py`, certifique-se de executar como um módulo e que o interpretador aponta para `Module08/.venv`:
	- Executar: `python -m samples.05.agents.coordinator`
	- Selecionar interpretador: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referências
- Foundry Local (Aprenda): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Visão geral do Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Exemplo de chamada de função (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

