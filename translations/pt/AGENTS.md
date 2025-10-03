<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:31:51+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pt"
}
-->
# AGENTS.md

## Visão Geral do Projeto

EdgeAI for Beginners é um repositório educacional abrangente que ensina o desenvolvimento de Edge AI com Modelos de Linguagem Pequenos (SLMs). O curso aborda os fundamentos do EdgeAI, implementação de modelos, técnicas de otimização e implementações prontas para produção utilizando Microsoft Foundry Local e vários frameworks de IA.

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

**Arquitetura:** Caminho de aprendizagem multi-módulo com exemplos práticos demonstrando padrões de implementação de Edge AI

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

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Configuração de Exemplos em Node.js (Exemplo 08 - Aplicação de Chat no Windows)

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

Foundry Local é necessário para executar os exemplos do Módulo08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Fluxo de Trabalho de Desenvolvimento

### Desenvolvimento de Conteúdo

Este repositório contém principalmente **conteúdo educacional em Markdown**. Ao fazer alterações:

1. Edite os ficheiros `.md` nos diretórios dos módulos apropriados
2. Siga os padrões de formatação existentes
3. Certifique-se de que os exemplos de código estão corretos e testados
4. Atualize o conteúdo traduzido correspondente, se necessário (ou deixe a automação tratar disso)

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

### Testar Aplicações de Exemplo

Os exemplos em Python não possuem testes automatizados, mas podem ser validados executando-os:
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

O repositório utiliza fluxos de trabalho de tradução automatizados. Não é necessário teste manual para traduções.

**Validação manual para alterações de conteúdo:**
1. Revise a renderização do Markdown ao pré-visualizar os ficheiros `.md`
2. Verifique se todos os links apontam para destinos válidos
3. Teste quaisquer trechos de código incluídos na documentação
4. Certifique-se de que as imagens carregam corretamente

### Teste de Aplicações de Exemplo

**Module08/samples/08 (aplicação Electron) possui testes abrangentes:**
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

- Use hierarquia consistente de cabeçalhos (# para título, ## para seções principais, ### para subseções)
- Inclua blocos de código com especificadores de linguagem: ```python, ```bash, ```javascript
- Siga a formatação existente para tabelas, listas e ênfase
- Mantenha as linhas legíveis (aproximadamente 80-100 caracteres, mas não estritamente)
- Use links relativos para referências internas

### Estilo de Código em Python

- Siga as convenções do PEP 8
- Utilize dicas de tipo quando apropriado
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

**Convenções principais:**
- Configuração do ESLint fornecida no exemplo 08
- Prettier para formatação de código
- Utilize sintaxe moderna ES6+
- Siga os padrões existentes na base de código

## Diretrizes para Pull Requests

### Formato do Título
```
[ModuleXX] Brief description of change
```
ou
```
[Module08/samples/XX] Description for sample changes
```

### Antes de Submeter

**Para alterações de conteúdo:**
- Pré-visualize todos os ficheiros Markdown modificados
- Verifique se os links e imagens funcionam
- Corrija erros ortográficos e gramaticais

**Para alterações de código de exemplo (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Para alterações de exemplos em Python:**
- Teste se o exemplo executa com sucesso
- Verifique se o tratamento de erros funciona
- Confirme a compatibilidade com Foundry Local

### Processo de Revisão

- Alterações no conteúdo educacional são revisadas quanto à precisão e clareza
- Exemplos de código são testados quanto à funcionalidade
- Atualizações de tradução são tratadas automaticamente por GitHub Actions

## Sistema de Tradução

**IMPORTANTE:** Este repositório utiliza tradução automatizada via GitHub Actions.

- As traduções estão no diretório `/translations/` (50+ idiomas)
- Automatizado através do workflow `co-op-translator.yml`
- **NÃO edite manualmente os ficheiros de tradução** - eles serão sobrescritos
- Edite apenas os ficheiros fonte em inglês na raiz e nos diretórios dos módulos
- As traduções são geradas automaticamente ao fazer push para a branch `main`

## Integração com Foundry Local

A maioria dos exemplos do Módulo08 requer que o Microsoft Foundry Local esteja em execução:

### Iniciar Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Verificar Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Variáveis de Ambiente para Exemplos

A maioria dos exemplos utiliza estas variáveis de ambiente:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Construção e Implementação

### Implementação de Conteúdo

Este repositório é principalmente documentação - não é necessário processo de construção para o conteúdo.

### Construção de Aplicações de Exemplo

**Aplicação Electron (Module08/samples/08):**
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

## Problemas Comuns e Soluções

### Foundry Local Não Está em Execução
**Problema:** Os exemplos falham com erros de conexão

**Solução:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problemas com Ambiente Virtual Python
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

### Problemas na Construção do Electron
**Problema:** Falhas no npm install ou na construção

**Solução:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Conflitos no Workflow de Tradução
**Problema:** PR de tradução conflita com suas alterações

**Solução:**
- Edite apenas os ficheiros fonte em inglês
- Deixe o workflow de tradução automatizado tratar das traduções
- Se ocorrerem conflitos, faça merge da branch `main` na sua branch após as traduções serem mescladas

## Recursos Adicionais

### Caminhos de Aprendizagem
- **Caminho para Iniciantes:** Módulos 01-02 (7-9 horas)
- **Caminho Intermediário:** Módulos 03-04 (9-11 horas)
- **Caminho Avançado:** Módulos 05-07 (12-15 horas)
- **Caminho para Especialistas:** Módulo 08 (8-10 horas)

### Conteúdo Principal dos Módulos
- **Module01:** Fundamentos de EdgeAI e estudos de caso reais
- **Module02:** Famílias e arquiteturas de Modelos de Linguagem Pequenos (SLM)
- **Module03:** Estratégias de implementação local e na nuvem
- **Module04:** Otimização de modelos com múltiplos frameworks
- **Module05:** SLMOps - operações em produção
- **Module06:** Agentes de IA e chamadas de função
- **Module07:** Implementações específicas de plataformas
- **Module08:** Toolkit Foundry Local com 10 exemplos abrangentes

### Dependências Externas
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Runtime local de modelos de IA
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework de otimização
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit de otimização de modelos
- [OpenVINO](https://docs.openvino.ai/) - Toolkit de otimização da Intel

## Notas Específicas do Projeto

### Aplicações de Exemplo do Módulo08

O repositório inclui 10 aplicações de exemplo abrangentes:

1. **01-REST Chat Quickstart** - Integração básica com OpenAI SDK
2. **02-OpenAI SDK Integration** - Funcionalidades avançadas do SDK
3. **03-Model Discovery & Benchmarking** - Ferramentas de comparação de modelos
4. **04-Chainlit RAG Application** - Geração aumentada por recuperação
5. **05-Multi-Agent Orchestration** - Coordenação básica de agentes
6. **06-Models-as-Tools Router** - Roteamento inteligente de modelos
7. **07-Direct API Client** - Integração de API de baixo nível
8. **08-Windows 11 Chat App** - Aplicação desktop nativa em Electron
9. **09-Advanced Multi-Agent System** - Orquestração complexa de agentes
10. **10-Foundry Tools Framework** - Integração LangChain/Semantic Kernel

Cada exemplo demonstra diferentes aspetos do desenvolvimento de Edge AI com Foundry Local.

### Considerações de Desempenho

- SLMs são otimizados para implementação em edge (2-16GB RAM)
- Inferência local oferece tempos de resposta de 50-500ms
- Técnicas de quantização reduzem o tamanho em 75% com retenção de 85% de desempenho
- Capacidades de conversação em tempo real com modelos locais

### Segurança e Privacidade

- Todo o processamento ocorre localmente - nenhum dado é enviado para a nuvem
- Adequado para aplicações sensíveis à privacidade (saúde, finanças)
- Atende aos requisitos de soberania de dados
- Foundry Local funciona inteiramente em hardware local

---

**Este é um repositório educacional focado em ensinar o desenvolvimento de Edge AI. O padrão principal de contribuição é melhorar o conteúdo educacional e adicionar/aperfeiçoar aplicações de exemplo que demonstrem conceitos de Edge AI.**

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.