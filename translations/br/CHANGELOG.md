<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T10:20:46+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "br"
}
-->
# Changelog

Todas as alterações relevantes no EdgeAI for Beginners estão documentadas aqui. Este projeto utiliza entradas baseadas em datas e segue o estilo Keep a Changelog (Adicionado, Alterado, Corrigido, Removido, Documentação, Movido).

## 2025-10-08

### Adicionado - Atualização Abrangente do Workshop
- **Reescrita completa do README.md do Workshop**:
  - Adicionada introdução abrangente explicando a proposta de valor do Edge AI (privacidade, desempenho, custo)
  - Criados 6 objetivos principais de aprendizado com competências detalhadas
  - Adicionada tabela de resultados de aprendizado com entregáveis e matriz de competências
  - Incluída seção de habilidades voltadas para o mercado para relevância na indústria
  - Adicionado guia de início rápido com pré-requisitos e configuração em 3 etapas
  - Criadas tabelas de recursos para exemplos em Python (8 arquivos com tempos de execução)
  - Adicionada tabela de notebooks Jupyter (8 notebooks com classificações de dificuldade)
  - Criada tabela de documentação (7 documentos principais com orientações "Quando Usar")
  - Adicionadas recomendações de trilhas de aprendizado para diferentes níveis de habilidade

- **Infraestrutura de validação e testes do Workshop**:
  - Criado `scripts/validate_samples.py` - Ferramenta abrangente de validação para sintaxe, imports e boas práticas
  - Criado `scripts/test_samples.py` - Executor de testes rápidos para todos os exemplos em Python
  - Adicionada documentação de validação ao `scripts/README.md`

- **Documentação abrangente**:
  - Criado `SAMPLES_UPDATE_SUMMARY.md` - Guia detalhado com mais de 400 linhas cobrindo todas as melhorias
  - Criado `UPDATE_COMPLETE.md` - Resumo executivo da conclusão da atualização
  - Criado `QUICK_REFERENCE.md` - Cartão de referência rápida para o Workshop

### Alterado - Modernização dos Exemplos em Python do Workshop
- **Todos os 8 exemplos em Python atualizados com boas práticas**:
  - Melhorado o tratamento de erros com blocos try-except em todas as operações de I/O
  - Adicionados type hints e docstrings abrangentes
  - Implementado padrão consistente de logging [INFO]/[ERROR]/[RESULT]
  - Protegidos imports opcionais com dicas de instalação
  - Melhorado o feedback ao usuário em todos os exemplos

- **session01/chat_bootstrap.py**:
  - Melhorada a inicialização do cliente com mensagens de erro abrangentes
  - Melhorado o tratamento de erros de streaming com validação de chunks
  - Adicionado tratamento de exceções para indisponibilidade de serviço

- **session02/rag_pipeline.py**:
  - Adicionados guardas de importação para sentence-transformers com dicas de instalação
  - Melhorado o tratamento de erros em operações de embedding e geração
  - Melhorado o formato de saída com resultados estruturados

- **session02/rag_eval_ragas.py**:
  - Protegidos imports opcionais (ragas, datasets) com mensagens de erro amigáveis
  - Adicionado tratamento de erros para métricas de avaliação
  - Melhorado o formato de saída para resultados de avaliação

- **session03/benchmark_oss_models.py**:
  - Implementada degradação graciosa (continua em caso de falhas de modelos)
  - Adicionado relatório detalhado de progresso e tratamento de erros por modelo
  - Melhorado o cálculo de estatísticas com recuperação abrangente de erros

- **session04/model_compare.py**:
  - Adicionados type hints (tipos Tuple para retornos)
  - Melhorado o formato de saída com resultados estruturados em JSON
  - Implementado tratamento de erros por modelo com recuperação

- **session05/agents_orchestrator.py**:
  - Melhorado Agent.act() com docstrings abrangentes
  - Adicionado tratamento de erros no pipeline com logging etapa por etapa
  - Melhorada a gestão de memória e rastreamento de estado

- **session06/models_router.py**:
  - Melhorada a documentação das funções para todos os componentes de roteamento
  - Adicionado logging detalhado na função route()
  - Melhorada a saída de testes com resultados estruturados

- **session06/models_pipeline.py**:
  - Adicionado tratamento de erros à função auxiliar chat()
  - Melhorado pipeline() com logging de etapas e relatórios de progresso
  - Melhorado main() com recuperação abrangente de erros

### Documentação - Melhoria na Documentação do Workshop
- Atualizado o README.md principal com uma seção do Workshop destacando a trilha prática de aprendizado
- Melhorado o STUDY_GUIDE.md com uma seção abrangente do Workshop, incluindo:
  - Objetivos de aprendizado e áreas de foco para estudo
  - Perguntas de autoavaliação
  - Exercícios práticos com estimativas de tempo
  - Alocação de tempo para estudo concentrado e em meio período
  - Adicionado o Workshop ao modelo de rastreamento de progresso
- Atualizado o guia de alocação de tempo de 20 horas para 30 horas (incluindo o Workshop)
- Adicionadas descrições dos exemplos do Workshop e resultados de aprendizado ao README

### Corrigido
- Resolvido padrão inconsistente de tratamento de erros nos exemplos do Workshop
- Corrigidos erros de importação de dependências opcionais com guardas adequados
- Corrigidos type hints ausentes em funções críticas
- Resolvido feedback insuficiente ao usuário em cenários de erro
- Corrigidos problemas de validação com infraestrutura de testes abrangente

---

## 2025-09-23

### Alterado - Modernização do Módulo 08
- **Alinhamento abrangente com padrões do repositório Microsoft Foundry-Local**:
  - Atualizados todos os exemplos de código para usar o moderno `FoundryLocalManager` e integração com o SDK OpenAI
  - Substituídas chamadas manuais de `requests` obsoletas pelo uso adequado do SDK
  - Alinhados padrões de implementação com a documentação oficial da Microsoft e exemplos

- **Modernização de 05.AIPoweredAgents.md**:
  - Atualizada a orquestração de múltiplos agentes para usar padrões modernos do SDK
  - Melhorada a implementação do coordenador com recursos avançados (loops de feedback, monitoramento de desempenho)
  - Adicionado tratamento de erros abrangente e verificação de saúde do serviço
  - Integradas referências adequadas a exemplos locais (`samples/05/multi_agent_orchestration.ipynb`)
  - Atualizados exemplos de chamadas de função para usar o parâmetro moderno `tools` em vez de `functions` obsoleto
  - Adicionados padrões prontos para produção com monitoramento e rastreamento de estatísticas

- **Reescrita completa de 06.ModelsAsTools.md**:
  - Substituído registro básico de ferramentas por uma implementação inteligente de roteador de modelos
  - Adicionada seleção de modelos baseada em palavras-chave para diferentes tipos de tarefas (geral, raciocínio, código, criativo)
  - Integrada configuração baseada em ambiente com atribuição flexível de modelos
  - Melhorado com monitoramento abrangente de saúde do serviço e tratamento de erros
  - Adicionados padrões de implantação em produção com monitoramento de solicitações e rastreamento de desempenho
  - Alinhado com a implementação local em `samples/06/router.py` e `samples/06/model_router.ipynb`

- **Melhorias na estrutura da documentação**:
  - Adicionadas seções de visão geral destacando a modernização e alinhamento com o SDK
  - Melhorado com emojis e formatação aprimorada para maior legibilidade
  - Incluídas referências adequadas a arquivos de exemplos locais em toda a documentação
  - Adicionado guia de implementação pronta para produção e melhores práticas

### Adicionado
- Seções de visão geral abrangentes nos arquivos do Módulo 08 destacando a integração moderna com o SDK
- Destaques de arquitetura mostrando recursos avançados (sistemas multiagentes, roteamento inteligente)
- Referências diretas a implementações de exemplos locais para experiência prática
- Orientação para implantação em produção com padrões de monitoramento e tratamento de erros
- Exemplos interativos em notebooks Jupyter com recursos avançados e benchmarks

### Corrigido
- Discrepâncias de alinhamento entre documentação e implementações reais de exemplos
- Padrões de uso do SDK desatualizados em todo o Módulo 08
- Referências ausentes à biblioteca abrangente de exemplos locais
- Abordagens de implementação inconsistentes em diferentes seções

---

## 2025-09-18

### Adicionado
- Módulo 08: Microsoft Foundry Local – Kit de Ferramentas Completo para Desenvolvedores
  - Seis sessões: configuração, integração com Azure AI Foundry, modelos open-source, demonstrações avançadas, agentes e modelos como ferramentas
  - Exemplos executáveis em `Module08/samples/01`–`06` com instruções para Windows cmd
    - `01` Chat REST rápido (`chat_quickstart.py`)
    - `02` Início rápido com SDK OpenAI/Foundry Local e suporte ao Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI listar e avaliar (`list_and_bench.cmd`)
    - `04` Demonstração Chainlit (`app.py`)
    - `05` Orquestração de múltiplos agentes (`python -m samples.05.agents.coordinator`)
    - `06` Roteador de Modelos como Ferramentas (`router.py`)
- Suporte ao Azure OpenAI no exemplo do SDK da Sessão 2 com configuração de variáveis de ambiente
- `.vscode/settings.json` apontando para `Module08/.venv` para melhorar a resolução de análise Python
- `.env` com dica de `PYTHONPATH` para reconhecimento no VS Code/Pylance

### Alterado
- Modelo padrão atualizado para `phi-4-mini` em toda a documentação e exemplos do Módulo 08; removidas menções restantes ao `phi-3.5` no Módulo 08
- Melhorias no roteador (`Module08/samples/06/router.py`):
  - Descoberta de endpoint via `foundry service status` com parsing regex
  - Verificação de saúde `/v1/models` na inicialização
  - Registro de modelos configurável via ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos atualizados: `Module08/requirements.txt` agora inclui `openai` (junto com `requests`, `chainlit`)
- Orientações para o exemplo Chainlit esclarecidas e troubleshooting adicionado; resolução de importação via configurações do workspace

### Corrigido
- Resolvidos problemas de importação:
  - Roteador não depende mais de um módulo `utils` inexistente; funções foram incorporadas
  - Coordenador usa importação relativa (`from .specialists import ...`) e é invocado via caminho do módulo
  - Configuração do VS Code/Pylance para resolver `chainlit` e imports de pacotes
- Corrigido pequeno erro de digitação em `STUDY_GUIDE.md` e adicionada cobertura do Módulo 08

### Removido
- Excluído `Module08/infra/obs.py` não utilizado e removido o diretório vazio `infra/`; padrões de observabilidade mantidos como opcionais na documentação

### Movido
- Consolidado os exemplos do Módulo 08 em `Module08/samples` com pastas numeradas por sessão
  - Aplicativo Chainlit movido para `samples/04`
  - Agentes movidos para `samples/05` e adicionados arquivos `__init__.py` para resolução de pacotes

### Documentação
- Documentos das sessões do Módulo 08 e todos os READMEs dos exemplos enriquecidos com referências ao Microsoft Learn e fornecedores confiáveis
- `Module08/README.md` atualizado com Visão Geral dos Exemplos, configuração do roteador e dicas de validação
- Seção do Foundry Local no Windows em `Module07/README.md` validada com os documentos do Learn
- `STUDY_GUIDE.md` atualizado:
  - Adicionado o Módulo 08 ao resumo, cronogramas e rastreador de progresso
  - Adicionada seção abrangente de Referências (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumo)
- Arquitetura do curso e módulos estabelecidos (Módulos 01–07)
- Modernização iterativa de conteúdo, padronização de formatação e adição de estudos de caso
- Expansão da cobertura de frameworks de otimização (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Não lançado / Backlog (propostas)
- Testes rápidos opcionais por exemplo para validar a disponibilidade do Foundry Local
- Revisar traduções para alinhar referências de modelos (e.g., `phi-4-mini`) onde apropriado
- Adicionar configuração mínima do pyright caso as equipes prefiram rigor em todo o workspace

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.