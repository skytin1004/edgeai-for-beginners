<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T11:25:02+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "pt"
}
-->
# Registo de Alterações

Todas as alterações relevantes ao EdgeAI for Beginners estão documentadas aqui. Este projeto utiliza entradas baseadas em datas e o estilo Keep a Changelog (Adicionado, Alterado, Corrigido, Removido, Documentação, Movido).

## 2025-09-23

### Alterado - Modernização significativa do Módulo 08
- **Alinhamento abrangente com os padrões de repositório Microsoft Foundry-Local**
  - Atualização de todos os exemplos de código para utilizar `FoundryLocalManager` moderno e integração com o SDK OpenAI
  - Substituição de chamadas manuais obsoletas de `requests` por uso adequado do SDK
  - Alinhamento dos padrões de implementação com a documentação oficial da Microsoft e exemplos

- **Modernização de 05.AIPoweredAgents.md**:
  - Atualização da orquestração multi-agente para utilizar padrões modernos do SDK
  - Melhoria na implementação do coordenador com funcionalidades avançadas (circuitos de feedback, monitorização de desempenho)
  - Adição de tratamento de erros abrangente e verificação de saúde do serviço
  - Integração de referências adequadas a exemplos locais (`samples/05/multi_agent_orchestration.ipynb`)
  - Atualização de exemplos de chamadas de funções para utilizar o parâmetro moderno `tools` em vez de `functions` obsoletos
  - Adição de padrões prontos para produção com monitorização e rastreamento de estatísticas

- **Reescrita completa de 06.ModelsAsTools.md**:
  - Substituição do registo básico de ferramentas por uma implementação de router inteligente de modelos
  - Adição de seleção de modelos baseada em palavras-chave para diferentes tipos de tarefas (geral, raciocínio, código, criativo)
  - Integração de configuração baseada em ambiente com atribuição flexível de modelos
  - Melhorado com monitorização abrangente de saúde do serviço e tratamento de erros
  - Adição de padrões de implementação em produção com monitorização de pedidos e rastreamento de desempenho
  - Alinhado com a implementação local em `samples/06/router.py` e `samples/06/model_router.ipynb`

- **Melhorias na estrutura da documentação**:
  - Adição de secções de visão geral destacando a modernização e alinhamento com o SDK
  - Melhorado com emojis e formatação mais clara para maior legibilidade
  - Inclusão de referências adequadas a ficheiros de exemplos locais em toda a documentação
  - Inclusão de orientações para implementação em produção e melhores práticas

### Adicionado
- Secções de visão geral abrangentes nos ficheiros do Módulo 08 destacando a integração moderna com o SDK
- Destaques de arquitetura mostrando funcionalidades avançadas (sistemas multi-agente, roteamento inteligente)
- Referências diretas a implementações de exemplos locais para experiência prática
- Orientações para implementação em produção com padrões de monitorização e tratamento de erros
- Exemplos interativos em Jupyter notebooks com funcionalidades avançadas e benchmarks

### Corrigido
- Discrepâncias de alinhamento entre a documentação e as implementações reais dos exemplos
- Padrões de uso do SDK desatualizados em todo o Módulo 08
- Referências ausentes à biblioteca abrangente de exemplos locais
- Abordagens de implementação inconsistentes em diferentes secções

---

## 2025-09-18

### Adicionado
- Módulo 08: Microsoft Foundry Local – Kit de Ferramentas Completo para Desenvolvedores
  - Seis sessões: configuração, integração com Azure AI Foundry, modelos open-source, demos de ponta, agentes e modelos como ferramentas
  - Exemplos executáveis em `Module08/samples/01`–`06` com instruções para cmd no Windows
    - `01` Chat rápido REST (`chat_quickstart.py`)
    - `02` Início rápido com SDK OpenAI/Foundry Local e suporte Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista e benchmark (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orquestração multi-agente (`python -m samples.05.agents.coordinator`)
    - `06` Router de Modelos como Ferramentas (`router.py`)
- Suporte Azure OpenAI no exemplo do SDK da Sessão 2 com configuração de variáveis de ambiente
- `.vscode/settings.json` apontando para `Module08/.venv` para melhorar a resolução de análise Python
- `.env` com sugestão de `PYTHONPATH` para reconhecimento no VS Code/Pylance

### Alterado
- Modelo padrão atualizado para `phi-4-mini` em toda a documentação e exemplos do Módulo 08; removidas menções restantes a `phi-3.5` no Módulo 08
- Melhorias no Router (`Module08/samples/06/router.py`):
  - Descoberta de endpoints via `foundry service status` com análise regex
  - Verificação de saúde `/v1/models` na inicialização
  - Registo de modelos configurável por ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos atualizados: `Module08/requirements.txt` agora inclui `openai` (junto com `requests`, `chainlit`)
- Orientações para o exemplo Chainlit clarificadas e adicionada resolução de problemas; resolução de importações via configurações de workspace

### Corrigido
- Problemas de importação resolvidos:
  - Router já não depende de um módulo inexistente `utils`; funções foram incorporadas
  - Coordenador utiliza importação relativa (`from .specialists import ...`) e é invocado via caminho de módulo
  - Configuração do VS Code/Pylance para resolver `chainlit` e importações de pacotes
- Corrigido pequeno erro de digitação em `STUDY_GUIDE.md` e adicionada cobertura do Módulo 08

### Removido
- Eliminado `Module08/infra/obs.py` não utilizado e removido o diretório vazio `infra/`; padrões de observabilidade mantidos como opcionais na documentação

### Movido
- Demos do Módulo 08 consolidadas em `Module08/samples` com pastas numeradas por sessão
  - Aplicação Chainlit movida para `samples/04`
  - Agentes movidos para `samples/05` e adicionados ficheiros `__init__.py` para resolução de pacotes

### Documentação
- Documentação das sessões do Módulo 08 e todos os READMEs dos exemplos enriquecidos com referências ao Microsoft Learn e fornecedores confiáveis
- `Module08/README.md` atualizado com Visão Geral dos Exemplos, configuração do router e dicas de validação
- Secção do Foundry Local no Windows em `Module07/README.md` validada contra a documentação do Learn
- `STUDY_GUIDE.md` atualizado:
  - Adicionado Módulo 08 à visão geral, cronogramas, rastreador de progresso
  - Adicionada secção abrangente de Referências (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumo)
- Arquitetura do curso e módulos estabelecidos (Módulos 01–07)
- Modernização iterativa de conteúdo, padronização de formatação e adição de estudos de caso
- Cobertura expandida de frameworks de otimização (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Não lançado / Pendente (propostas)
- Testes opcionais por exemplo para validar a disponibilidade do Foundry Local
- Revisão de traduções para alinhar referências de modelos (ex.: `phi-4-mini`) onde apropriado
- Adicionar configuração mínima do pyright caso as equipas prefiram rigor em todo o workspace

---

