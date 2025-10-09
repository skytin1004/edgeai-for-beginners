<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T10:35:09+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "br"
}
-->
# Atualizações do SDK Local Foundry

## Visão Geral

Atualizamos os notebooks e utilitários do Workshop para utilizar corretamente o **SDK Local Python Foundry oficial**, seguindo os padrões de:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Arquivos Modificados

### 1. `Workshop/samples/workshop_utils.py`

**Alterações:**
- ✅ Adicionado tratamento de erro de importação para o pacote `foundry-local-sdk`
- ✅ Documentação aprimorada com padrões oficiais do SDK
- ✅ Melhorias no registro de logs com símbolos Unicode (✓, ✗, ⚠)
- ✅ Adicionadas docstrings abrangentes com exemplos
- ✅ Mensagens de erro mais detalhadas, referenciando comandos CLI
- ✅ Comentários atualizados para corresponder à documentação oficial do SDK

**Principais Melhorias:**

#### Tratamento de Erro de Importação
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Função Aprimorada `get_client()`
- Documentação detalhada sobre o padrão de inicialização do SDK
- Explicado que o `FoundryLocalManager` inicia o serviço automaticamente
- Resolução de alias de modelo para variantes otimizadas para hardware
- Logs aprimorados com informações de endpoint
- Mensagens de erro mais claras sugerindo etapas de solução de problemas

#### Função Aprimorada `chat_once()`
- Adicionada docstring abrangente com exemplos de uso
- Compatibilidade com o SDK OpenAI esclarecida
- Documentado suporte a streaming (via kwargs)
- Mensagens de erro aprimoradas com sugestões de comandos CLI
- Notas adicionadas sobre verificação de disponibilidade de modelos

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Alterações:**
- ✅ Atualizadas todas as células de markdown com referências ao SDK
- ✅ Comentários de código aprimorados com explicações sobre padrões do SDK
- ✅ Documentação e explicações das células melhoradas
- ✅ Adicionadas orientações para solução de problemas
- ✅ Catálogo de modelos atualizado (substituído 'gpt-oss-20b' por 'phi-3.5-mini')
- ✅ Melhor formatação de saída com indicadores visuais
- ✅ Links e referências ao SDK adicionados ao longo do notebook

**Atualizações Célula por Célula:**

#### Célula 1 (Título)
- Links para documentação do SDK adicionados
- Referências aos repositórios oficiais do GitHub

#### Célula 2 (Cenário)
- Reformatação com etapas numeradas
- Padrão de roteamento baseado em intenção esclarecido
- Benefícios da execução local enfatizados

#### Célula 3 (Instalação de Dependências)
- Explicação adicionada sobre o que cada pacote fornece
- Capacidades do SDK documentadas (resolução de alias, otimização de hardware)

#### Célula 4 (Configuração do Ambiente)
- Docstrings de funções aprimoradas
- Comentários inline explicando padrões do SDK adicionados
- Estrutura do catálogo de modelos documentada
- Correspondência de prioridade/capacidade esclarecida

#### Célula 5 (Verificação do Catálogo)
- Adicionados indicadores visuais (✓)
- Saída melhor formatada

#### Célula 6 (Teste de Detecção de Intenção)
- Saída reformulada no estilo de tabela
- Mostra tanto a intenção quanto o modelo selecionado

#### Célula 7 (Função de Roteamento)
- Explicação abrangente sobre padrões do SDK
- Fluxo de inicialização documentado
- Listadas todas as funcionalidades (retries, rastreamento, erros)
- Link de referência ao SDK adicionado

#### Célula 8 (Demonstração em Lote)
- Explicação aprimorada sobre o que esperar
- Seção de solução de problemas adicionada
- Comandos CLI incluídos para depuração
- Exibição de saída melhor formatada

### 3. `Workshop/notebooks/session06_README.md` (Novo Arquivo)

**Documentação abrangente criada cobrindo:**

1. **Visão Geral**: Diagrama de arquitetura e explicação dos componentes
2. **Integração com SDK**: Exemplos de código seguindo padrões oficiais
3. **Pré-requisitos**: Instruções de configuração passo a passo
4. **Uso**: Como executar e personalizar o notebook
5. **Aliases de Modelos**: Explicação sobre variantes otimizadas para hardware
6. **Solução de Problemas**: Problemas comuns e soluções
7. **Extensão**: Como adicionar intenções, modelos e lógica personalizada
8. **Dicas de Desempenho**: Melhores práticas para uso em produção
9. **Recursos**: Links para documentação oficial e comunidade

## Implementação de Padrões do SDK

### Padrão Oficial (dos documentos do Foundry Local)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Nossa Implementação (em workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Benefícios da Nossa Abordagem:**
- ✅ Segue exatamente o padrão oficial do SDK
- ✅ Adiciona cache para evitar inicializações repetidas
- ✅ Inclui lógica de retry para robustez em produção
- ✅ Suporta rastreamento de uso de tokens
- ✅ Fornece mensagens de erro mais detalhadas
- ✅ Permanece compatível com exemplos oficiais

## Alterações no Catálogo de Modelos

### Antes
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Depois
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Motivo:** Substituído 'gpt-oss-20b' (alias não padrão) por 'phi-3.5-mini' (alias oficial do Foundry Local).

## Dependências

### Atualização do requirements.txt

O arquivo requirements.txt do Workshop já inclui:
```
foundry-local-sdk
openai>=1.30.0
```

Esses são os únicos pacotes necessários para integração com o Foundry Local.

## Testando as Atualizações

### 1. Verificar se o Foundry Local está em execução

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Verificar Modelos Disponíveis

```bash
foundry model ls
```

Certifique-se de que esses modelos estão disponíveis ou serão baixados automaticamente:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Executar o Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Ou abra no VS Code e execute todas as células.

### 4. Comportamento Esperado

**Célula 1 (Instalação):** Pacotes instalados com sucesso  
**Célula 2 (Configuração):** Sem erros, importações funcionando  
**Célula 3 (Verificação):** Mostra ✓ com lista de modelos  
**Célula 4 (Teste de Intenção):** Mostra resultados de detecção de intenção  
**Célula 5 (Roteador):** Mostra ✓ Função de roteamento pronta  
**Célula 6 (Execução):** Roteia prompts para modelos, mostra resultados  

### 5. Solução de Problemas de Erros de Conexão

Se você vir `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Variáveis de Ambiente

As seguintes variáveis de ambiente são suportadas:

| Variável | Padrão | Descrição |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Defina como `1` para imprimir uso de tokens |
| `RETRY_ON_FAIL` | `1` | Habilitar lógica de retry |
| `RETRY_BACKOFF` | `1.0` | Atraso inicial de retry (segundos) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Substituir endpoint do serviço |

### Exemplos de Uso

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migração do Padrão Antigo

Se você tem código existente usando chamadas diretas à API, veja como migrar:

### Antes (API Direta)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Depois (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Benefícios da Migração
- ✅ Gerenciamento automático de serviços
- ✅ Resolução de alias de modelos
- ✅ Seleção de otimização de hardware
- ✅ Melhor tratamento de erros
- ✅ Compatibilidade com SDK OpenAI
- ✅ Suporte a streaming

## Referências

### Documentação Oficial
- **GitHub Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Fonte do SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Referência CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **API REST**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Solução de Problemas**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Recursos do Workshop
- **README da Sessão 06**: `Workshop/notebooks/session06_README.md`
- **Utils do Workshop**: `Workshop/samples/workshop_utils.py`
- **Notebook de Exemplo**: `Workshop/notebooks/session06_models_router.ipynb`

### Comunidade
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues no GitHub**: https://github.com/microsoft/Foundry-Local/issues

## Próximos Passos

1. **Revisar Alterações**: Leia os arquivos atualizados  
2. **Testar Notebook**: Execute o session06_models_router.ipynb  
3. **Verificar SDK**: Certifique-se de que o foundry-local-sdk está instalado  
4. **Checar Serviço**: Confirme que o Foundry Local está em execução  
5. **Explorar Documentação**: Leia o novo session06_README.md  

## Resumo

Essas atualizações garantem que os materiais do Workshop sigam os **padrões oficiais do SDK Local Foundry** exatamente como documentado no repositório GitHub. Todos os exemplos de código, documentação e utilitários agora estão alinhados com as melhores práticas recomendadas pela Microsoft para implantação local de modelos de IA.

As mudanças melhoram:
- ✅ **Correção**: Utiliza padrões oficiais do SDK  
- ✅ **Documentação**: Explicações e exemplos abrangentes  
- ✅ **Tratamento de Erros**: Mensagens e orientações de solução de problemas melhores  
- ✅ **Manutenção**: Segue convenções oficiais  
- ✅ **Experiência do Usuário**: Instruções mais claras e ajuda para depuração  

---

**Atualizado:** 8 de outubro de 2025  
**Versão do SDK:** foundry-local-sdk (mais recente)  
**Branch do Workshop:** Reactor  

---

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.