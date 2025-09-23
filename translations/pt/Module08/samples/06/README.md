<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T12:58:06+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "pt"
}
-->
# Sessão 6 Exemplo: Modelos como Ferramentas

Este exemplo implementa um router minimalista + registo de ferramentas que seleciona um modelo com base no prompt do utilizador e chama o endpoint compatível com OpenAI do Foundry Local.

## Ficheiros
- `router.py`: registo simples e roteamento heurístico; descoberta de endpoint + verificação de saúde.

## Executar (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Notas
- O router utiliza heurísticas simples de palavras-chave para escolher entre as ferramentas `general`, `reasoning` e `code`, e imprime `/v1/models` ao iniciar.
- Configuração através de variáveis de ambiente:
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

## Referências
- Foundry Local (Aprender): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integração com SDKs de inferência: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

