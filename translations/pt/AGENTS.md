<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-08T20:26:58+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pt"
}
-->
# AGENTS.md

> **Guia do Desenvolvedor para Contribuir com o EdgeAI para Iniciantes**
> 
> Este documento fornece informações abrangentes para desenvolvedores, agentes de IA e colaboradores que trabalham com este repositório. Ele abrange configuração, fluxos de trabalho de desenvolvimento, testes e melhores práticas.
> 
> **Última Atualização**: Outubro de 2025 | **Versão do Documento**: 2.0

## Índice

- [Visão Geral do Projeto](../..)
- [Estrutura do Repositório](../..)
- [Pré-requisitos](../..)
- [Comandos de Configuração](../..)
- [Fluxo de Trabalho de Desenvolvimento](../..)
- [Instruções de Teste](../..)
- [Diretrizes de Estilo de Código](../..)
- [Diretrizes para Pull Requests](../..)
- [Sistema de Tradução](../..)
- [Integração com o Foundry Local](../..)
- [Construção e Implementação](../..)
- [Problemas Comuns e Solução de Problemas](../..)
- [Recursos Adicionais](../..)
- [Notas Específicas do Projeto](../..)
- [Obter Ajuda](../..)

## Visão Geral do Projeto

EdgeAI para Iniciantes é um repositório educacional abrangente que ensina o desenvolvimento de IA de Borda com Modelos de Linguagem Pequenos (SLMs). O curso aborda os fundamentos do EdgeAI, implementação de modelos, técnicas de otimização e implementações prontas para produção usando o Microsoft Foundry Local e vários frameworks de IA.

**Principais Tecnologias:**
- Python 3.8+ (linguagem principal para exemplos de IA/ML)
- .NET C# (exemplos de IA/ML)
- JavaScript/Node.js com Electron (para aplicações desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Frameworks de IA: LangChain, Semantic Kernel, Chainlit
- Otimização de Modelos: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tipo de Repositório:** Repositório de conteúdo educacional com 8 módulos e 10 aplicações de exemplo abrangentes

**Arquitetura:** Caminho de aprendizagem multi-módulo com exemplos práticos demonstrando padrões de implementação de IA de borda

## Estrutura do Repositório

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Pré-requisitos

### Ferramentas Necessárias

- **Python 3.8+** - Para exemplos e notebooks de IA/ML
- **Node.js 16+** - Para a aplicação de exemplo em Electron
- **Git** - Para controle de versão
- **Microsoft Foundry Local** - Para executar modelos de IA localmente

### Ferramentas Recomendadas

- **Visual Studio Code** - Com extensões Python, Jupyter e Pylance
- **Windows Terminal** - Para uma melhor experiência de linha de comando (usuários do Windows)
- **Docker** - Para desenvolvimento em contêiner (opcional)

### Requisitos do Sistema

- **RAM**: Mínimo de 8GB, recomendado 16GB+ para cenários com múltiplos modelos
- **Armazenamento**: 10GB+ de espaço livre para modelos e dependências
- **SO**: Windows 10/11, macOS 11+ ou Linux (Ubuntu 20.04+)
- **Hardware**: CPU com suporte AVX2; GPU (CUDA, Qualcomm NPU) opcional, mas recomendada

### Conhecimentos Necessários

- Compreensão básica de programação em Python
- Familiaridade com interfaces de linha de comando
- Entendimento de conceitos de IA/ML (para desenvolvimento de exemplos)
- Fluxos de trabalho com Git e processos de pull request

## Comandos de Configuração

### Configuração do Repositório

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Configuração de Exemplos em Python (Módulo08 e exemplos em Python)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Configuração de Exemplos em Node.js (Exemplo 08 - Aplicação de Chat para Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Configuração do Foundry Local

O Foundry Local é necessário para executar os exemplos. Faça o download e instale a partir do repositório oficial:

**Instalação:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: Faça o download na [página de lançamentos](https://github.com/microsoft/Foundry-Local/releases)

**Início Rápido:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Nota**: O Foundry Local seleciona automaticamente a melhor variante de modelo para o seu hardware (GPU CUDA, NPU Qualcomm ou CPU).

## Fluxo de Trabalho de Desenvolvimento

### Desenvolvimento de Conteúdo

Este repositório contém principalmente **conteúdo educacional em Markdown**. Ao fazer alterações:

1. Edite os ficheiros `.md` nos diretórios de módulos apropriados
2. Siga os padrões de formatação existentes
3. Certifique-se de que os exemplos de código estão corretos e testados
4. Atualize o conteúdo traduzido correspondente, se necessário (ou deixe a automação cuidar disso)

### Desenvolvimento de Aplicações de Exemplo

Para exemplos em Python (exemplos 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Para o exemplo em Electron (exemplo 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testando Aplicações de Exemplo

Os exemplos em Python não possuem testes automatizados, mas podem ser validados ao executá-los:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

O exemplo em Electron possui infraestrutura de testes:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instruções de Teste

### Validação de Conteúdo

O repositório utiliza fluxos de trabalho de tradução automatizados. Não é necessário realizar testes manuais para traduções.

**Validação manual para alterações de conteúdo:**
1. Revise a renderização do Markdown ao visualizar os ficheiros `.md`
2. Verifique se todos os links apontam para destinos válidos
3. Teste quaisquer trechos de código incluídos na documentação
4. Certifique-se de que as imagens carregam corretamente

### Teste de Aplicações de Exemplo

**O módulo08/exemplos/08 (aplicação Electron) possui testes abrangentes:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Os exemplos em Python devem ser testados manualmente:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Diretrizes de Estilo de Código

### Conteúdo em Markdown

- Use uma hierarquia consistente de cabeçalhos (# para título, ## para seções principais, ### para subseções)
- Inclua blocos de código com especificadores de linguagem: ```python, ```bash, ```javascript
- Siga o formato existente para tabelas, listas e ênfases
- Mantenha as linhas legíveis (cerca de ~80-100 caracteres, mas não é obrigatório)
- Use links relativos para referências internas

### Estilo de Código em Python

- Siga as convenções do PEP 8
- Use anotações de tipo quando apropriado
- Inclua docstrings para funções e classes
- Use nomes de variáveis significativos
- Mantenha as funções focadas e concisas

### Estilo de Código em JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Principais convenções:**
- Configuração do ESLint fornecida no exemplo 08
- Prettier para formatação de código
- Use sintaxe moderna ES6+
- Siga os padrões existentes no código-base

## Diretrizes para Pull Requests

### Fluxo de Contribuição

1. **Faça um fork do repositório** e crie um novo branch a partir do `main`
2. **Faça suas alterações** seguindo as diretrizes de estilo de código
3. **Teste completamente** usando as instruções de teste acima
4. **Faça commits com mensagens claras** seguindo o formato de commits convencionais
5. **Envie para o seu fork** e crie um pull request
6. **Responda ao feedback** dos mantenedores durante a revisão

### Convenção de Nomes de Branch

- `feature/<modulo>-<descrição>` - Para novas funcionalidades ou conteúdo
- `fix/<modulo>-<descrição>` - Para correções de bugs
- `docs/<descrição>` - Para melhorias na documentação
- `refactor/<descrição>` - Para refatoração de código

### Formato de Mensagem de Commit

Siga [Commits Convencionais](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Exemplos:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Formato do Título
```
[ModuleXX] Brief description of change
```
ou
```
[Module08/samples/XX] Description for sample changes
```

### Código de Conduta

Todos os colaboradores devem seguir o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/). Por favor, reveja o [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) antes de contribuir.

### Antes de Submeter

**Para alterações de conteúdo:**
- Visualize todos os ficheiros Markdown modificados
- Verifique se os links e imagens funcionam
- Verifique se há erros de digitação e gramaticais

**Para alterações no código de exemplo (Módulo08/exemplos/08):**
```bash
npm run lint
npm test
```

**Para alterações nos exemplos em Python:**
- Teste se o exemplo é executado com sucesso
- Verifique se o tratamento de erros funciona
- Confirme a compatibilidade com o Foundry Local

### Processo de Revisão

- Alterações no conteúdo educacional são revisadas quanto à precisão e clareza
- Exemplos de código são testados quanto à funcionalidade
- Atualizações de tradução são tratadas automaticamente pelo GitHub Actions

## Sistema de Tradução

**IMPORTANTE:** Este repositório utiliza tradução automatizada via GitHub Actions.

- As traduções estão no diretório `/translations/` (50+ idiomas)
- Automatizado via o fluxo de trabalho `co-op-translator.yml`
- **NÃO edite manualmente os ficheiros de tradução** - eles serão sobrescritos
- Edite apenas os ficheiros de origem em inglês nos diretórios raiz e de módulos
- As traduções são geradas automaticamente ao enviar para o branch `main`

## Integração com o Foundry Local

A maioria dos exemplos do Módulo08 requer o Microsoft Foundry Local em execução.

### Instalação e Configuração

**Instale o Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Instale o SDK Python:**
```bash
pip install foundry-local-sdk openai
```

### Iniciando o Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Uso do SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-3.5-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Verificando o Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Variáveis de Ambiente para Exemplos

A maioria dos exemplos utiliza estas variáveis de ambiente:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-3.5-mini  # or phi-4-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Nota**: Ao usar o `FoundryLocalManager`, o SDK lida automaticamente com a descoberta de serviços e o carregamento de modelos. Os aliases de modelo (como `phi-3.5-mini`) garantem que a melhor variante seja selecionada para o seu hardware.

## Construção e Implementação

### Implementação de Conteúdo

Este repositório é principalmente de documentação - não é necessário processo de construção para o conteúdo.

### Construção de Aplicações de Exemplo

**Aplicação Electron (Módulo08/exemplos/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Exemplos em Python:**
Sem processo de construção - os exemplos são executados diretamente com o interpretador Python.

## Problemas Comuns e Solução de Problemas

> **Dica**: Verifique [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) para problemas conhecidos e soluções.

### Problemas Críticos (Bloqueadores)

#### Foundry Local Não Está em Execução
**Problema:** Exemplos falham com erros de conexão

**Solução:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-3.5-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Problemas Comuns (Moderados)

#### Problemas com Ambiente Virtual Python
**Problema:** Erros de importação de módulos

**Solução:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problemas na Construção do Electron
**Problema:** Falhas no npm install ou na construção

**Solução:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problemas de Fluxo de Trabalho (Menores)

#### Conflitos no Fluxo de Trabalho de Tradução
**Problema:** Conflitos de PR de tradução com as suas alterações

**Solução:**
- Edite apenas os ficheiros de origem em inglês
- Deixe o fluxo de trabalho de tradução automatizado lidar com as traduções
- Se ocorrerem conflitos, faça merge do `main` no seu branch após as traduções serem mescladas

#### Falhas no Download de Modelos
**Problema:** O Foundry Local não consegue baixar os modelos

**Solução:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Recursos Adicionais

### Caminhos de Aprendizagem
- **Caminho para Iniciantes:** Módulos 01-02 (7-9 horas)
- **Caminho Intermediário:** Módulos 03-04 (9-11 horas)
- **Caminho Avançado:** Módulos 05-07 (12-15 horas)
- **Caminho Especialista:** Módulo 08 (8-10 horas)

### Conteúdo Principal dos Módulos
- **Módulo01:** Fundamentos do EdgeAI e estudos de caso do mundo real
- **Módulo02:** Famílias e arquiteturas de Modelos de Linguagem Pequenos (SLM)
- **Módulo03:** Estratégias de implementação local e na nuvem
- **Módulo04:** Otimização de modelos com múltiplos frameworks
- **Módulo05:** SLMOps - operações em produção
- **Módulo06:** Agentes de IA e chamadas de função
- **Módulo07:** Implementações específicas de plataformas
- **Módulo08:** Ferramentas do Foundry Local com 10 exemplos abrangentes

### Dependências Externas
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime local de modelos de IA com API compatível com OpenAI
  - [Documentação](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [SDK Python](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [SDK JavaScript](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework de otimização
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Ferramenta de otimização de modelos
- [OpenVINO](https://docs.openvino.ai/) - Ferramenta de otimização da Intel

## Notas Específicas do Projeto

### Aplicações de Exemplo do Módulo08

O repositório inclui 10 aplicações de exemplo abrangentes:

1. **01-REST Chat Quickstart** - Integração básica com o OpenAI SDK
2. **02-OpenAI SDK Integration** - Funcionalidades avançadas do SDK
3. **03-Model Discovery & Benchmarking** - Ferramentas de comparação de modelos
4. **04-Chainlit RAG Application** - Geração aumentada por recuperação
5. **05-Multi-Agent Orchestration** - Coordenação básica de agentes
6. **06-Models-as-Tools Router** - Roteamento inteligente de modelos
7. **07-Direct API Client** - Integração de API de baixo nível
8. **08-Windows 11 Chat App** - Aplicação desktop nativa em Electron
9. **09-Advanced Multi-Agent System** - Orquestração complexa de agentes
10. **10-Foundry Tools Framework** - Integração LangChain/Semantic Kernel

Cada exemplo demonstra diferentes aspectos do desenvolvimento de IA de borda com o Foundry Local.

### Considerações de Desempenho

- Os SLMs são otimizados para implementação em borda (2-16GB RAM)
- A inferência local proporciona tempos de resposta de 50-500ms  
- Técnicas de quantização alcançam uma redução de tamanho de 75% com retenção de desempenho de 85%  
- Capacidades de conversação em tempo real com modelos locais  

### Segurança e Privacidade  

- Todo o processamento ocorre localmente - nenhum dado é enviado para a nuvem  
- Adequado para aplicações sensíveis à privacidade (saúde, finanças)  
- Cumpre os requisitos de soberania de dados  
- Foundry Local funciona inteiramente em hardware local  

## Obter Ajuda  

### Documentação  

- **README Principal**: [README.md](README.md) - Visão geral do repositório e caminhos de aprendizagem  
- **Guia de Estudo**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Recursos de aprendizagem e cronograma  
- **Suporte**: [SUPPORT.md](SUPPORT.md) - Como obter ajuda  
- **Segurança**: [SECURITY.md](SECURITY.md) - Relatar problemas de segurança  

### Suporte da Comunidade  

- **Problemas no GitHub**: [Relatar bugs ou solicitar funcionalidades](https://github.com/microsoft/edgeai-for-beginners/issues)  
- **Discussões no GitHub**: [Fazer perguntas e partilhar ideias](https://github.com/microsoft/edgeai-for-beginners/discussions)  
- **Problemas no Foundry Local**: [Questões técnicas com o Foundry Local](https://github.com/microsoft/Foundry-Local/issues)  

### Contacto  

- **Responsáveis**: Ver [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)  
- **Problemas de Segurança**: Seguir a divulgação responsável em [SECURITY.md](SECURITY.md)  
- **Suporte Microsoft**: Para suporte empresarial, contactar o serviço de apoio ao cliente da Microsoft  

### Recursos Adicionais  

- **Microsoft Learn**: [Caminhos de Aprendizagem de IA e Aprendizagem Automática](https://learn.microsoft.com/training/browse/?products=ai-services)  
- **Documentação do Foundry Local**: [Documentação Oficial](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)  
- **Exemplos da Comunidade**: Consulte [Discussões no GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) para contribuições da comunidade  

---

**Este é um repositório educacional focado no ensino do desenvolvimento de IA na Edge. O principal padrão de contribuição é melhorar o conteúdo educacional e adicionar/aperfeiçoar aplicações de exemplo que demonstrem conceitos de IA na Edge.**  

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.