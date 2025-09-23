<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T12:58:17+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "pt"
}
-->
# Exemplo da Sessão 4: Demonstração Chainlit RAG

Execute a aplicação mínima do Chainlit com o Foundry Local.

## Pré-requisitos
- Windows 11, Python 3.10+
- Foundry Local instalado e um modelo disponível (por exemplo, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Executar (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Validar
```cmd
curl http://localhost:8000/v1/models
```

## Resolução de Problemas
- Se o VS Code mostrar "chainlit could not be resolved":
	- Selecione o interpretador `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Certifique-se de que as dependências estão instaladas: `pip install -r Module08\requirements.txt`

## Referências
- Guia de utilização do Open WebUI (aplicação de chat com Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Aprender): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

