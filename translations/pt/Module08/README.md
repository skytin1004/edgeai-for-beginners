<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T12:50:34+00:00",
  "source_file": "Module08/README.md",
  "language_code": "pt"
}
-->
# Módulo 08: Prática com Microsoft Foundry Local - Kit Completo para Desenvolvedores

## Visão Geral

O Microsoft Foundry Local representa a próxima geração de desenvolvimento de IA na edge, oferecendo aos desenvolvedores ferramentas poderosas para criar, implementar e escalar aplicações de IA localmente, mantendo uma integração perfeita com o Azure AI Foundry. Este módulo fornece uma cobertura abrangente do Foundry Local, desde a instalação até o desenvolvimento avançado de agentes.

**Principais Tecnologias:**
- CLI e SDK do Microsoft Foundry Local
- Integração com Azure AI Foundry
- Inferência de modelos no dispositivo
- Cache e otimização de modelos locais
- Arquiteturas baseadas em agentes

## Objetivos de Aprendizagem do Módulo

Ao concluir este módulo, você será capaz de:

- **Dominar a Configuração do Foundry Local**: Instalar, configurar e otimizar o Foundry Local para desenvolvimento no Windows 11
- **Implementar Modelos Diversos**: Executar modelos phi, qwen, deepseek e GPT-OSS-20B localmente com comandos CLI
- **Criar Soluções de Produção**: Desenvolver aplicações de IA com engenharia avançada de prompts e integração de dados
- **Aproveitar o Ecossistema Open-Source**: Integrar modelos do Hugging Face e contribuições da comunidade
- **Comparar Arquiteturas de IA**: Compreender os trade-offs entre LLMs e SLMs e estratégias de implementação
- **Desenvolver Agentes de IA**: Criar agentes inteligentes usando a arquitetura e capacidades de grounding do Foundry Local
- **Implementar Modelos como Ferramentas**: Criar soluções de IA modulares e personalizáveis para aplicações empresariais

## Estrutura da Sessão

### [1: Introdução ao Foundry Local](./01.FoundryLocalSetup.md)
**Foco**: Instalação, configuração CLI, cache de modelos e aceleração de hardware

**O que Você Vai Aprender:**
- Instalação completa do Foundry Local no Windows 11
- Configuração da CLI e estrutura de comandos
- Estratégias de cache de modelos para desempenho ideal
- Configuração e otimização de aceleração de hardware
- Implementação prática dos modelos phi, qwen, deepseek e GPT-OSS-20B

**Duração**: 2-3 horas  
**Pré-requisitos**: Windows 11, conhecimento básico de linha de comando

---

### [2: Construir Soluções de IA com Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Foco**: Engenharia avançada de prompts, integração de dados e tarefas acionáveis

**O que Você Vai Aprender:**
- Técnicas avançadas de engenharia de prompts
- Padrões e melhores práticas de integração de dados
- Construção de tarefas acionáveis de IA com Foundry Local
- Fluxos de trabalho de integração perfeita com Azure AI Foundry
- Otimização de desempenho e monitoramento

**Duração**: 2-3 horas  
**Pré-requisitos**: Conclusão da Sessão 1, conta Azure (opcional)

---

### [3: Modelos Open-Source no Foundry Local](./03.OpenSourceModels.md)
**Foco**: Integração com Hugging Face, estratégias de seleção de modelos e adições da comunidade

**O que Você Vai Aprender:**
- Integração de modelos do Hugging Face com Foundry Local
- Estratégias e implementação de "traga seu próprio modelo" (BYOM)
- Insights da série Model Mondays e contribuições da comunidade
- Implementação e otimização de modelos personalizados
- Critérios de avaliação e seleção de modelos da comunidade

**Duração**: 2-3 horas  
**Pré-requisitos**: Conclusão das Sessões 1-2, conta Hugging Face

---

### [4: Explorar Modelos de Ponta - LLMs, SLMs e Inferência no Dispositivo](./04.CuttingEdgeModels.md)
**Foco**: Comparação de modelos, EdgeAI com Phi e ONNX Runtime, demonstrações avançadas

**O que Você Vai Aprender:**
- Comparação abrangente entre LLMs e SLMs e casos de uso
- Trade-offs entre inferência local e na nuvem e frameworks de decisão
- Implementação de EdgeAI com Phi e ONNX Runtime
- Desenvolvimento e implementação do aplicativo Chainlit RAG Chat
- Técnicas de otimização de inferência com WebGPU
- Integração e capacidades do SDK AI PC

**Duração**: 3-4 horas  
**Pré-requisitos**: Conclusão das Sessões 1-3, compreensão de conceitos de inferência

---

### [5: Criar Agentes de IA Rápido com Foundry Local](./05.AIPoweredAgents.md)
**Foco**: Desenvolvimento rápido de apps GenAI, prompts de sistema, grounding e arquiteturas de agentes

**O que Você Vai Aprender:**
- Arquitetura e padrões de design de agentes do Foundry Local
- Engenharia de prompts de sistema para comportamento de agentes
- Técnicas de grounding para respostas confiáveis de agentes
- Fluxos de trabalho de desenvolvimento rápido de aplicações GenAI
- Orquestração de agentes e sistemas multi-agentes
- Estratégias de implementação em produção para agentes de IA

**Duração**: 3-4 horas  
**Pré-requisitos**: Conclusão das Sessões 1-4, compreensão básica de agentes de IA

---

### [6: Foundry Local - Modelos como Ferramentas](./06.ModelsAsTools.md)
**Foco**: Soluções de IA modulares, implementação no dispositivo e escalabilidade empresarial

**O que Você Vai Aprender:**
- Tratar modelos de IA como ferramentas modulares e personalizáveis
- Implementação no dispositivo sem dependência da nuvem
- Inferência de baixa latência, custo eficiente e preservação de privacidade
- Padrões de integração com SDK, API e CLI
- Personalização de modelos para casos de uso específicos
- Estratégias de escalabilidade do local para Azure AI Foundry
- Arquiteturas de aplicações de IA prontas para empresas

**Duração**: 3-4 horas  
**Pré-requisitos**: Todas as sessões anteriores, experiência em desenvolvimento empresarial útil

## Pré-requisitos

### Requisitos do Sistema
- **Sistema Operativo**: Windows 11 (22H2 ou posterior)
- **Memória**: 16GB RAM (32GB recomendados para modelos maiores)
- **Armazenamento**: 50GB de espaço livre para cache de modelos
- **Hardware**: Dispositivo com NPU recomendado (Copilot+ PC), GPU opcional
- **Rede**: Internet de alta velocidade para downloads iniciais de modelos

### Ambiente de Desenvolvimento
- Visual Studio Code com extensão AI Toolkit
- Python 3.10+ e pip
- Git para controlo de versão
- PowerShell ou Prompt de Comando
- Azure CLI (opcional para integração na nuvem)

### Conhecimentos Necessários
- Compreensão básica de conceitos de IA/ML
- Familiaridade com linha de comando
- Noções básicas de programação em Python
- Conceitos de API REST
- Conhecimento básico de prompts e inferência de modelos

## Cronograma do Módulo

**Tempo Estimado Total**: 15-20 horas

| Sessão | Área de Foco | Tempo | Complexidade |
|--------|--------------|-------|--------------|
|  1 | Configuração & Básicos | 2-3 horas | Iniciante |
|  2 | Soluções de IA | 2-3 horas | Intermediário |
|  3 | Open Source | 2-3 horas | Intermediário |
|  4 | Modelos Avançados | 3-4 horas | Avançado |
|  5 | Agentes de IA | 3-4 horas | Avançado |
|  6 | Ferramentas Empresariais | 3-4 horas | Especialista |

## Recursos Principais

### Documentação Primária
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Documentação do Azure AI Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Série Model Mondays](https://aka.ms/model-mondays)

### Recursos da Comunidade
- [Discussões da Comunidade Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Exemplos do Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Comunidade de Desenvolvedores de IA da Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence)

## Resultados de Aprendizagem

Ao concluir este módulo, você estará preparado para:

### Domínio Técnico
- **Implementar e Gerir**: Instalações do Foundry Local em ambientes de desenvolvimento e produção
- **Integrar Modelos**: Trabalhar perfeitamente com diversas famílias de modelos da Microsoft, Hugging Face e fontes da comunidade
- **Criar Aplicações**: Desenvolver aplicações de IA prontas para produção com recursos avançados e otimizações
- **Desenvolver Agentes**: Implementar agentes de IA sofisticados com grounding, raciocínio e integração de ferramentas

### Compreensão Estratégica
- **Decisões de Arquitetura**: Fazer escolhas informadas entre implementação local e na nuvem
- **Otimização de Desempenho**: Otimizar o desempenho de inferência em diferentes configurações de hardware
- **Escalabilidade Empresarial**: Projetar aplicações que escalam de protótipos locais para implementações empresariais
- **Privacidade e Segurança**: Implementar soluções de IA que preservam a privacidade com inferência local

### Capacidades de Inovação
- **Prototipagem Rápida**: Construir e testar conceitos de aplicações de IA rapidamente
- **Integração Comunitária**: Aproveitar modelos open-source e contribuir para o ecossistema
- **Padrões Avançados**: Implementar padrões de IA de ponta, incluindo RAG, agentes e integração de ferramentas
- **Desenvolvimento Preparado para o Futuro**: Criar aplicações prontas para tecnologias e padrões emergentes de IA

## Como Começar

1. **Prepare o Ambiente**: Certifique-se de ter o Windows 11 com as especificações de hardware recomendadas
2. **Instale os Pré-requisitos**: Configure as ferramentas de desenvolvimento e dependências
3. **Comece com a Sessão 1**: Inicie com a instalação e configuração básica do Foundry Local
4. **Progrida Sequencialmente**: Complete as sessões na ordem para uma progressão de aprendizagem ideal
5. **Pratique Continuamente**: Aplique os conceitos através de exercícios práticos e projetos

## Métricas de Sucesso

Acompanhe seu progresso ao longo do módulo:

- [ ] Instalar e configurar com sucesso o Foundry Local
- [ ] Implementar e executar pelo menos 4 famílias de modelos diferentes
- [ ] Construir uma solução completa de IA com integração de dados
- [ ] Integrar pelo menos 2 modelos open-source
- [ ] Criar um aplicativo funcional de chat RAG
- [ ] Desenvolver e implementar um agente de IA
- [ ] Implementar uma arquitetura de modelos como ferramentas

## Início Rápido para Exemplos

### 1) Configuração do ambiente (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Iniciar um modelo local (novo terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Executar o demo Chainlit (Sessão 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Executar o coordenador multi-agente (Sessão 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Se ocorrerem erros de conexão, valide o Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Configuração do router (Sessão 6)
O router realiza uma verificação rápida de saúde e suporta configuração baseada em ambiente:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Este módulo representa o estado da arte no desenvolvimento de IA na edge, combinando ferramentas empresariais da Microsoft com a flexibilidade e inovação do ecossistema open-source. Ao dominar o Foundry Local, você estará na vanguarda do desenvolvimento de aplicações de IA.

Para Azure OpenAI (Sessão 2), veja o README de exemplo para variáveis de ambiente necessárias e configurações de versão da API.

## Visão Geral dos Exemplos

- `samples/01`: Chat REST rápido com Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integração com OpenAI SDK (`sdk_quickstart.py`).
- `samples/03`: Descoberta de modelos + benchmark rápido (`list_and_bench.cmd`).
- `samples/04`: Demo Chainlit RAG (`app.py`).
- `samples/05`: Orquestração multi-agente (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router de Modelos como Ferramentas (`python samples\06\router.py`).

---

