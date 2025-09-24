<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T21:16:21+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "br"
}
-->
# Changelog

Todas as alterações importantes no EdgeAI for Beginners estão documentadas aqui. Este projeto utiliza entradas baseadas em datas e o estilo Keep a Changelog (Adicionado, Alterado, Corrigido, Removido, Documentação, Movido).

## 2025-09-23

### Alterado - Modernização do Módulo 08
- **Alinhamento abrangente com os padrões de repositório Microsoft Foundry-Local**
  - Atualizados todos os exemplos de código para usar o moderno `FoundryLocalManager` e integração com OpenAI SDK
  - Substituídas chamadas manuais obsoletas de `requests` por uso adequado do SDK
  - Implementação alinhada com a documentação oficial da Microsoft e exemplos

- **Modernização de 05.AIPoweredAgents.md**:
  - Atualizada a orquestração de múltiplos agentes para usar padrões modernos de SDK
  - Coordenador aprimorado com recursos avançados (loops de feedback, monitoramento de desempenho)
  - Adicionado tratamento abrangente de erros e verificação de saúde do serviço
  - Integradas referências adequadas a exemplos locais (`samples/05/multi_agent_orchestration.ipynb`)
  - Atualizados exemplos de chamadas de função para usar o moderno parâmetro `tools` em vez de `functions` obsoletos
  - Adicionados padrões prontos para produção com monitoramento e rastreamento de estatísticas

- **Reescrita completa de 06.ModelsAsTools.md**:
  - Substituído registro básico de ferramentas por implementação de roteador inteligente de modelos
  - Adicionada seleção de modelos baseada em palavras-chave para diferentes tipos de tarefas (geral, raciocínio, código, criativo)
  - Integrada configuração baseada em ambiente com atribuição flexível de modelos
  - Aprimorado com monitoramento abrangente de saúde do serviço e tratamento de erros
  - Adicionados padrões de implantação em produção com monitoramento de solicitações e rastreamento de desempenho
  - Alinhado com implementação local em `samples/06/router.py` e `samples/06/model_router.ipynb`

- **Melhorias na estrutura da documentação**:
  - Adicionadas seções de visão geral destacando modernização e alinhamento com SDK
  - Aprimorado com emojis e melhor formatação para maior legibilidade
  - Incluídas referências adequadas a arquivos de exemplos locais em toda a documentação
  - Incluídas orientações de implementação pronta para produção e melhores práticas

### Adicionado
- Seções abrangentes de visão geral nos arquivos do Módulo 08 destacando integração moderna com SDK
- Destaques de arquitetura mostrando recursos avançados (sistemas multiagentes, roteamento inteligente)
- Referências diretas a implementações de exemplos locais para experiência prática
- Orientações de implantação em produção com padrões de monitoramento e tratamento de erros
- Exemplos interativos em Jupyter notebook com recursos avançados e benchmarks

### Corrigido
- Discrepâncias de alinhamento entre documentação e implementações reais de exemplos
- Padrões de uso de SDK desatualizados em todo o Módulo 08
- Referências ausentes à biblioteca abrangente de exemplos locais
- Abordagens de implementação inconsistentes em diferentes seções

---

## 2025-09-18

### Adicionado
- Módulo 08: Microsoft Foundry Local – Kit de Ferramentas Completo para Desenvolvedores
  - Seis sessões: configuração, integração com Azure AI Foundry, modelos de código aberto, demonstrações avançadas, agentes e modelos como ferramentas
  - Exemplos executáveis em `Module08/samples/01`–`06` com instruções para cmd no Windows
    - `01` Chat rápido REST (`chat_quickstart.py`)
    - `02` Início rápido com SDK OpenAI/Foundry Local e suporte ao Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista e benchmark (`list_and_bench.cmd`)
    - `04` Demonstração Chainlit (`app.py`)
    - `05` Orquestração de múltiplos agentes (`python -m samples.05.agents.coordinator`)
    - `06` Roteador de Modelos como Ferramentas (`router.py`)
- Suporte ao Azure OpenAI no exemplo de SDK da Sessão 2 com configuração de variáveis de ambiente
- `.vscode/settings.json` apontando para `Module08/.venv` para melhorar a resolução de análise Python
- `.env` com dica `PYTHONPATH` para reconhecimento no VS Code/Pylance

### Alterado
- Modelo padrão atualizado para `phi-4-mini` em toda a documentação e exemplos do Módulo 08; removidas menções restantes a `phi-3.5` no Módulo 08
- Melhorias no roteador (`Module08/samples/06/router.py`):
  - Descoberta de endpoint via `foundry service status` com análise regex
  - Verificação de saúde `/v1/models` na inicialização
  - Registro de modelos configurável por ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos atualizados: `Module08/requirements.txt` agora inclui `openai` (junto com `requests`, `chainlit`)
- Orientações para exemplo Chainlit esclarecidas e adicionada solução de problemas; resolução de importação via configurações de workspace

### Corrigido
- Problemas de importação resolvidos:
  - Roteador não depende mais de um módulo `utils` inexistente; funções foram incorporadas
  - Coordenador usa importação relativa (`from .specialists import ...`) e é invocado via caminho de módulo
  - Configuração do VS Code/Pylance para resolver `chainlit` e importações de pacotes
- Corrigido pequeno erro de digitação em `STUDY_GUIDE.md` e adicionada cobertura do Módulo 08

### Removido
- Excluído `Module08/infra/obs.py` não utilizado e removido o diretório vazio `infra/`; padrões de observabilidade mantidos como opcionais na documentação

### Movido
- Demonstrações do Módulo 08 consolidadas em `Module08/samples` com pastas numeradas por sessão
  - Aplicativo Chainlit movido para `samples/04`
  - Agentes movidos para `samples/05` e adicionados arquivos `__init__.py` para resolução de pacotes

### Documentação
- Documentos das sessões do Módulo 08 e todos os READMEs de exemplos enriquecidos com referências ao Microsoft Learn e fornecedores confiáveis
- `Module08/README.md` atualizado com Visão Geral dos Exemplos, configuração do roteador e dicas de validação
- Seção do Windows Foundry Local em `Module07/README.md` validada contra documentos do Learn
- `STUDY_GUIDE.md` atualizado:
  - Adicionado Módulo 08 à visão geral, cronogramas, rastreador de progresso
  - Adicionada seção abrangente de Referências (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumo)
- Arquitetura do curso e módulos estabelecidos (Módulos 01–07)
- Modernização iterativa de conteúdo, padronização de formatação e adição de estudos de caso
- Cobertura expandida de frameworks de otimização (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Não lançado / Backlog (propostas)
- Testes opcionais por exemplo para validar disponibilidade do Foundry Local
- Revisar traduções para alinhar referências de modelos (ex.: `phi-4-mini`) onde apropriado
- Adicionar configuração mínima do pyright caso as equipes prefiram rigor em todo o workspace

---

