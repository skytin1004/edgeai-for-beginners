<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T18:22:21+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "br"
}
-->
# Registro de Alterações

Todas as mudanças importantes no EdgeAI for Beginners estão documentadas aqui. Este projeto utiliza entradas baseadas em datas e o estilo Keep a Changelog (Adicionado, Alterado, Corrigido, Removido, Documentação, Movido).

## 2025-09-18

### Adicionado
- Módulo 08: Microsoft Foundry Local – Kit de Ferramentas Completo para Desenvolvedores
  - Seis sessões: configuração, integração com Azure AI Foundry, modelos de código aberto, demonstrações avançadas, agentes e modelos como ferramentas
  - Exemplos executáveis em `Module08/samples/01`–`06` com instruções para cmd no Windows
    - `01` Chat rápido via REST (`chat_quickstart.py`)
    - `02` Introdução ao SDK com suporte ao OpenAI/Foundry Local e Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista e benchmark (`list_and_bench.cmd`)
    - `04` Demonstração Chainlit (`app.py`)
    - `05` Orquestração multiagente (`python -m samples.05.agents.coordinator`)
    - `06` Roteador de Modelos como Ferramentas (`router.py`)
- Suporte ao Azure OpenAI no exemplo de SDK da Sessão 2 com configuração de variáveis de ambiente
- `.vscode/settings.json` apontando para `Module08/.venv` para melhorar a resolução de análise Python
- `.env` com sugestão de `PYTHONPATH` para reconhecimento no VS Code/Pylance

### Alterado
- Modelo padrão atualizado para `phi-4-mini` em toda a documentação e exemplos do Módulo 08; removidas as menções restantes ao `phi-3.5` dentro do Módulo 08
- Melhorias no roteador (`Module08/samples/06/router.py`):
  - Descoberta de endpoint via `foundry service status` com análise regex
  - Verificação de saúde em `/v1/models` na inicialização
  - Registro de modelos configurável via ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos atualizados: `Module08/requirements.txt` agora inclui `openai` (junto com `requests`, `chainlit`)
- Orientações para o exemplo Chainlit esclarecidas e adicionadas soluções de problemas; resolução de importação via configurações de workspace

### Corrigido
- Problemas de importação resolvidos:
  - O roteador não depende mais de um módulo `utils` inexistente; funções foram incorporadas
  - O coordenador usa importação relativa (`from .specialists import ...`) e é invocado via caminho de módulo
  - Configuração do VS Code/Pylance para resolver `chainlit` e importações de pacotes
- Corrigido pequeno erro de digitação em `STUDY_GUIDE.md` e adicionada cobertura do Módulo 08

### Removido
- Excluído `Module08/infra/obs.py` não utilizado e removido o diretório vazio `infra/`; padrões de observabilidade mantidos como opcionais na documentação

### Movido
- Demonstrações do Módulo 08 consolidadas em `Module08/samples` com pastas numeradas por sessão
  - Aplicativo Chainlit movido para `samples/04`
  - Agentes movidos para `samples/05` e adicionados arquivos `__init__.py` para resolução de pacotes

### Documentação
- Documentação das sessões do Módulo 08 e todos os READMEs dos exemplos enriquecidos com referências do Microsoft Learn e fornecedores confiáveis
- `Module08/README.md` atualizado com Visão Geral dos Exemplos, configuração do roteador e dicas de validação
- Seção do Foundry Local no Windows em `Module07/README.md` validada contra a documentação do Learn
- `STUDY_GUIDE.md` atualizado:
  - Adicionado Módulo 08 ao resumo, cronogramas, rastreador de progresso
  - Adicionada seção abrangente de Referências (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumo)
- Arquitetura do curso e módulos estabelecidos (Módulos 01–07)
- Modernização iterativa de conteúdo, padronização de formatação e adição de estudos de caso
- Cobertura expandida de frameworks de otimização (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Não lançado / Pendências (propostas)
- Testes opcionais por exemplo para validar a disponibilidade do Foundry Local
- Revisar traduções para alinhar referências de modelos (ex.: `phi-4-mini`) onde apropriado
- Adicionar configuração mínima do pyright caso as equipes prefiram rigor em todo o workspace

---

