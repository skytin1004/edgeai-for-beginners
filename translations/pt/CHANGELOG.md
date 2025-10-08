<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T20:26:25+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "pt"
}
-->
# Registo de Alterações

Todas as alterações relevantes ao EdgeAI for Beginners estão documentadas aqui. Este projeto utiliza entradas baseadas em datas e o estilo Keep a Changelog (Adicionado, Alterado, Corrigido, Removido, Documentação, Movido).

## 2025-10-08

### Adicionado - Atualização Abrangente do Workshop
- **Reescrita completa do README.md do Workshop**:
  - Adicionada introdução abrangente explicando a proposta de valor do Edge AI (privacidade, desempenho, custo)
  - Criados 6 objetivos principais de aprendizagem com competências detalhadas
  - Adicionada tabela de resultados de aprendizagem com entregáveis e matriz de competências
  - Incluída secção de competências orientadas para a carreira, relevante para a indústria
  - Adicionado guia de início rápido com pré-requisitos e configuração em 3 passos
  - Criadas tabelas de recursos para exemplos em Python (8 ficheiros com tempos de execução)
  - Adicionada tabela de notebooks Jupyter (8 notebooks com classificações de dificuldade)
  - Criada tabela de documentação (7 documentos principais com orientação "Quando Usar")
  - Adicionadas recomendações de percurso de aprendizagem para diferentes níveis de competência

- **Infraestrutura de validação e teste do Workshop**:
  - Criado `scripts/validate_samples.py` - Ferramenta abrangente de validação para sintaxe, importações e boas práticas
  - Criado `scripts/test_samples.py` - Executor de testes rápidos para todos os exemplos em Python
  - Adicionada documentação de validação ao `scripts/README.md`

- **Documentação abrangente**:
  - Criado `SAMPLES_UPDATE_SUMMARY.md` - Guia detalhado com mais de 400 linhas cobrindo todas as melhorias
  - Criado `UPDATE_COMPLETE.md` - Resumo executivo da conclusão da atualização
  - Criado `QUICK_REFERENCE.md` - Cartão de referência rápida para o Workshop

### Alterado - Modernização dos Exemplos em Python do Workshop
- **Todos os 8 exemplos em Python atualizados com boas práticas**:
  - Melhorada a gestão de erros com blocos try-except em todas as operações de I/O
  - Adicionadas dicas de tipo e docstrings abrangentes
  - Implementado padrão consistente de registo [INFO]/[ERROR]/[RESULT]
  - Protegidas importações opcionais com dicas de instalação
  - Melhorado o feedback ao utilizador em todos os exemplos

- **session01/chat_bootstrap.py**:
  - Melhorada a inicialização do cliente com mensagens de erro abrangentes
  - Melhorada a gestão de erros de streaming com validação de fragmentos
  - Adicionada melhor gestão de exceções para indisponibilidade de serviço

- **session02/rag_pipeline.py**:
  - Adicionados guardas de importação para sentence-transformers com dicas de instalação
  - Melhorada a gestão de erros nas operações de incorporação e geração
  - Melhorado o formato de saída com resultados estruturados

- **session02/rag_eval_ragas.py**:
  - Protegidas importações opcionais (ragas, datasets) com mensagens de erro amigáveis
  - Adicionada gestão de erros para métricas de avaliação
  - Melhorado o formato de saída para resultados de avaliação

- **session03/benchmark_oss_models.py**:
  - Implementada degradação graciosa (continua em caso de falhas de modelos)
  - Adicionado relatório detalhado de progresso e gestão de erros por modelo
  - Melhorado o cálculo de estatísticas com recuperação abrangente de erros

- **session04/model_compare.py**:
  - Adicionadas dicas de tipo (tipos de retorno Tuple)
  - Melhorado o formato de saída com resultados JSON estruturados
  - Implementada gestão de erros por modelo com recuperação

- **session05/agents_orchestrator.py**:
  - Melhorado Agent.act() com docstrings abrangentes
  - Adicionada gestão de erros na pipeline com registo etapa por etapa
  - Melhorada a gestão de memória e rastreamento de estado

- **session06/models_router.py**:
  - Melhorada a documentação das funções para todos os componentes de roteamento
  - Adicionado registo detalhado na função route()
  - Melhorada a saída de teste com resultados estruturados

- **session06/models_pipeline.py**:
  - Adicionada gestão de erros à função auxiliar chat()
  - Melhorada pipeline() com registo de etapas e relatório de progresso
  - Melhorada main() com recuperação abrangente de erros

### Documentação - Melhoria da Documentação do Workshop
- Atualizado o README.md principal com uma secção do Workshop destacando o percurso de aprendizagem prático
- Melhorado o STUDY_GUIDE.md com uma secção abrangente do Workshop incluindo:
  - Objetivos de aprendizagem e áreas de foco de estudo
  - Perguntas de autoavaliação
  - Exercícios práticos com estimativas de tempo
  - Alocação de tempo para estudo concentrado e a tempo parcial
  - Adicionado o Workshop ao modelo de rastreamento de progresso
- Atualizado o guia de alocação de tempo de 20 horas para 30 horas (incluindo o Workshop)
- Adicionadas descrições dos exemplos do Workshop e resultados de aprendizagem ao README

### Corrigido
- Resolvidos padrões inconsistentes de gestão de erros nos exemplos do Workshop
- Corrigidos erros de importação de dependências opcionais com guardas adequados
- Corrigidas dicas de tipo ausentes em funções críticas
- Resolvido feedback insuficiente ao utilizador em cenários de erro
- Corrigidos problemas de validação com infraestrutura de testes abrangente

---

## 2025-09-23

### Alterado - Modernização Importante do Módulo 08
- **Alinhamento abrangente com padrões do repositório Microsoft Foundry-Local**:
  - Atualizados todos os exemplos de código para usar o moderno `FoundryLocalManager` e integração com o SDK OpenAI
  - Substituídas chamadas manuais obsoletas de `requests` por uso adequado do SDK
  - Alinhados padrões de implementação com documentação oficial da Microsoft e exemplos

- **Modernização de 05.AIPoweredAgents.md**:
  - Atualizada orquestração multi-agente para usar padrões modernos de SDK
  - Melhorada a implementação do coordenador com funcionalidades avançadas (circuitos de feedback, monitorização de desempenho)
  - Adicionada gestão abrangente de erros e verificação de saúde do serviço
  - Integradas referências adequadas a exemplos locais (`samples/05/multi_agent_orchestration.ipynb`)
  - Atualizados exemplos de chamadas de funções para usar o parâmetro moderno `tools` em vez de `functions` obsoletos
  - Adicionados padrões prontos para produção com monitorização e rastreamento de estatísticas

- **Reescrita completa de 06.ModelsAsTools.md**:
  - Substituído registo básico de ferramentas por implementação inteligente de roteador de modelos
  - Adicionada seleção de modelos baseada em palavras-chave para diferentes tipos de tarefas (geral, raciocínio, código, criativo)
  - Integrada configuração baseada em ambiente com atribuição flexível de modelos
  - Melhorada com monitorização abrangente de saúde do serviço e gestão de erros
  - Adicionados padrões de implementação em produção com monitorização de pedidos e rastreamento de desempenho
  - Alinhado com implementação local em `samples/06/router.py` e `samples/06/model_router.ipynb`

- **Melhorias na estrutura da documentação**:
  - Adicionadas secções de visão geral destacando modernização e alinhamento com SDK
  - Melhorado com emojis e formatação para maior legibilidade
  - Incluídas referências adequadas a ficheiros de exemplos locais em toda a documentação
  - Incluída orientação para implementação pronta para produção e melhores práticas

### Adicionado
- Secções abrangentes de visão geral nos ficheiros do Módulo 08 destacando integração moderna com SDK
- Destaques de arquitetura mostrando funcionalidades avançadas (sistemas multi-agente, roteamento inteligente)
- Referências diretas a implementações de exemplos locais para experiência prática
- Orientação para implementação em produção com padrões de monitorização e gestão de erros
- Exemplos interativos de notebooks Jupyter com funcionalidades avançadas e benchmarks

### Corrigido
- Discrepâncias de alinhamento entre documentação e implementações reais de exemplos
- Padrões de uso de SDK obsoletos em todo o Módulo 08
- Referências ausentes à biblioteca abrangente de exemplos locais
- Abordagens de implementação inconsistentes em diferentes secções

---

## 2025-09-18

### Adicionado
- Módulo 08: Microsoft Foundry Local – Kit de Ferramentas Completo para Desenvolvedores
  - Seis sessões: configuração, integração Azure AI Foundry, modelos open-source, demos avançadas, agentes e modelos-como-ferramentas
  - Exemplos executáveis em `Module08/samples/01`–`06` com instruções para cmd no Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart com suporte OpenAI/Foundry Local e Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orquestração multi-agente (`python -m samples.05.agents.coordinator`)
    - `06` Roteador Models-as-Tools (`router.py`)
- Suporte Azure OpenAI no exemplo SDK da Sessão 2 com configuração de variáveis de ambiente
- `.vscode/settings.json` apontando para `Module08/.venv` para melhorar a resolução de análise Python
- `.env` com dica `PYTHONPATH` para reconhecimento no VS Code/Pylance

### Alterado
- Modelo padrão atualizado para `phi-4-mini` em toda a documentação e exemplos do Módulo 08; removidas menções restantes a `phi-3.5` no Módulo 08
- Melhorias no roteador (`Module08/samples/06/router.py`):
  - Descoberta de endpoints via `foundry service status` com análise regex
  - Verificação de saúde `/v1/models` na inicialização
  - Registo de modelos configurável por ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos atualizados: `Module08/requirements.txt` agora inclui `openai` (junto com `requests`, `chainlit`)
- Orientação para exemplo Chainlit clarificada e adicionada resolução de problemas; resolução de importação via configurações de workspace

### Corrigido
- Resolvidos problemas de importação:
  - O roteador já não depende de um módulo inexistente `utils`; funções foram incorporadas
  - O coordenador usa importação relativa (`from .specialists import ...`) e é invocado via caminho de módulo
  - Configuração do VS Code/Pylance para resolver `chainlit` e importações de pacotes
- Corrigido pequeno erro de digitação em `STUDY_GUIDE.md` e adicionada cobertura do Módulo 08

### Removido
- Eliminado `Module08/infra/obs.py` não utilizado e removido o diretório vazio `infra/`; padrões de observabilidade mantidos como opcionais na documentação

### Movido
- Consolidado demos do Módulo 08 em `Module08/samples` com pastas numeradas por sessão
  - Movido app Chainlit para `samples/04`
  - Movidos agentes para `samples/05` e adicionados ficheiros `__init__.py` para resolução de pacotes

### Documentação
- Documentação das sessões do Módulo 08 e todos os READMEs dos exemplos enriquecidos com referências ao Microsoft Learn e fornecedores confiáveis
- `Module08/README.md` atualizado com Visão Geral dos Exemplos, configuração do roteador e dicas de validação
- Secção Windows Foundry Local do `Module07/README.md` validada contra documentos do Learn
- `STUDY_GUIDE.md` atualizado:
  - Adicionado Módulo 08 à visão geral, cronogramas, rastreador de progresso
  - Adicionada secção abrangente de Referências (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumo)
- Arquitetura do curso e módulos estabelecidos (Módulos 01–07)
- Modernização iterativa de conteúdo, padronização de formatação e adição de estudos de caso
- Cobertura expandida de frameworks de otimização (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Não Lançado / Pendente (propostas)
- Testes rápidos opcionais por exemplo para validar disponibilidade do Foundry Local
- Rever traduções para alinhar referências de modelos (ex.: `phi-4-mini`) onde apropriado
- Adicionar configuração mínima do pyright caso as equipas prefiram rigor em todo o workspace

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.