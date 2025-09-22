<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T18:34:11+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "br"
}
-->
# Sessão 1 Exemplo: Chat Rápido via REST

Execute uma solicitação mínima de chat para o Foundry Local usando `requests` do Python.

## Pré-requisitos
- Serviço Foundry Local executando um modelo (por exemplo, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Executar (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referências
- Foundry Local (Aprenda): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Visão geral da API compatível com OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

