<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-08T20:56:33+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "pt"
}
-->
# Exemplos do Workshop - Resumo da Atualização do SDK Local Foundry

## Visão Geral

Todos os exemplos em Python no diretório `Workshop/samples` foram atualizados para seguir as melhores práticas do SDK Local Foundry e garantir consistência em todo o workshop.

**Data**: 8 de outubro de 2025  
**Escopo**: 9 ficheiros Python em 6 sessões do workshop  
**Foco Principal**: Tratamento de erros, documentação, padrões do SDK, experiência do utilizador

---

## Ficheiros Atualizados

### Sessão 01: Primeiros Passos
- ✅ `chat_bootstrap.py` - Exemplos básicos de chat e streaming

### Sessão 02: Soluções RAG
- ✅ `rag_pipeline.py` - Implementação de RAG com embeddings
- ✅ `rag_eval_ragas.py` - Avaliação de RAG com métricas RAGAS

### Sessão 03: Modelos Open Source
- ✅ `benchmark_oss_models.py` - Benchmarking de múltiplos modelos

### Sessão 04: Modelos de Ponta
- ✅ `model_compare.py` - Comparação entre SLM e LLM

### Sessão 05: Agentes com IA
- ✅ `agents_orchestrator.py` - Coordenação de múltiplos agentes

### Sessão 06: Modelos como Ferramentas
- ✅ `models_router.py` - Roteamento baseado em intenções
- ✅ `models_pipeline.py` - Pipeline com múltiplas etapas roteadas

### Infraestrutura de Suporte
- ✅ `workshop_utils.py` - Já segue as melhores práticas (sem alterações necessárias)

---

## Principais Melhorias

### 1. Tratamento de Erros Aprimorado

**Antes:**
```python
manager, client, model_id = get_client(alias)
```
  
**Depois:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```
  
**Benefícios:**
- Tratamento de erros mais elegante com mensagens claras
- Dicas práticas para resolução de problemas
- Códigos de saída adequados para scripts

### 2. Melhor Gestão de Imports

**Antes:**
```python
from sentence_transformers import SentenceTransformer
```
  
**Depois:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```
  
**Benefícios:**
- Orientação clara quando faltam dependências
- Prevenção de erros de importação enigmáticos
- Instruções de instalação amigáveis ao utilizador

### 3. Documentação Abrangente

**Adicionado a todos os exemplos:**
- Documentação de variáveis de ambiente em docstrings
- Links de referência ao SDK
- Exemplos de uso
- Documentação detalhada de funções/parâmetros
- Dicas de tipos para melhor suporte em IDEs

**Exemplo:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```
  

### 4. Feedback Melhorado ao Utilizador

**Adicionado logging informativo:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```
  
**Indicadores de progresso:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```
  
**Saída estruturada:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```
  

### 5. Benchmarking Robusto

**Melhorias na Sessão 03:**
- Tratamento de erros por modelo (continua em caso de falha)
- Relatórios detalhados de progresso
- Execução adequada de rondas de aquecimento
- Suporte à medição de latência do primeiro token
- Separação clara das etapas

### 6. Dicas de Tipos Consistentes

**Adicionado em todo o código:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```
  
**Benefícios:**
- Melhor autocompletar em IDEs
- Detecção precoce de erros
- Código autoexplicativo

### 7. Roteador de Modelos Aprimorado

**Melhorias na Sessão 06:**
- Documentação abrangente de deteção de intenções
- Explicação do algoritmo de seleção de modelos
- Logs detalhados de roteamento
- Formatação de saída de testes
- Recuperação de erros em testes em lote

### 8. Orquestração de Múltiplos Agentes

**Melhorias na Sessão 05:**
- Relatórios de progresso etapa por etapa
- Tratamento de erros por agente
- Estrutura clara do pipeline
- Documentação melhorada de gestão de memória

---

## Lista de Verificação de Testes

### Pré-requisitos
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```
  

### Testar Cada Exemplo

#### Sessão 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```
  
#### Sessão 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```
  
#### Sessão 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```
  
#### Sessão 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```
  
#### Sessão 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```
  
#### Sessão 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```
  

---

## Referência de Variáveis de Ambiente

### Global (Todos os Exemplos)
| Variável | Descrição | Padrão |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias do modelo a usar | Varia por exemplo |
| `FOUNDRY_LOCAL_ENDPOINT` | Substituir endpoint do serviço | Detetado automaticamente |
| `SHOW_USAGE` | Mostrar uso de tokens | `0` |
| `RETRY_ON_FAIL` | Ativar lógica de repetição | `1` |
| `RETRY_BACKOFF` | Atraso inicial na repetição | `1.0` |

### Específico do Exemplo
| Variável | Usado Por | Descrição |
|----------|---------|-------------|
| `EMBED_MODEL` | Sessão 02 | Nome do modelo de embedding |
| `RAG_QUESTION` | Sessão 02 | Pergunta de teste para RAG |
| `BENCH_MODELS` | Sessão 03 | Modelos separados por vírgula para benchmarking |
| `BENCH_ROUNDS` | Sessão 03 | Número de rondas de benchmarking |
| `BENCH_PROMPT` | Sessão 03 | Prompt de teste para benchmarks |
| `BENCH_STREAM` | Sessão 03 | Medir latência do primeiro token |
| `SLM_ALIAS` | Sessão 04 | Modelo de linguagem pequeno |
| `LLM_ALIAS` | Sessão 04 | Modelo de linguagem grande |
| `COMPARE_PROMPT` | Sessão 04 | Prompt de teste para comparação |
| `AGENT_MODEL_PRIMARY` | Sessão 05 | Modelo principal do agente |
| `AGENT_MODEL_EDITOR` | Sessão 05 | Modelo editor do agente |
| `AGENT_QUESTION` | Sessão 05 | Pergunta de teste para agentes |
| `PIPELINE_TASK` | Sessão 06 | Tarefa para pipeline |

---

## Alterações Disruptivas

**Nenhuma** - Todas as alterações são retrocompatíveis.

Os scripts existentes continuarão a funcionar. As novas funcionalidades incluem:
- Variáveis de ambiente opcionais
- Mensagens de erro aprimoradas (não quebram a funcionalidade)
- Logging adicional (pode ser suprimido)
- Dicas de tipos melhoradas (sem impacto em tempo de execução)

---

## Melhores Práticas Implementadas

### 1. Utilizar Sempre Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```
  
### 2. Padrão de Tratamento de Erros Adequado
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```
  
### 3. Logging Informativo
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```
  
### 4. Dicas de Tipos
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```
  
### 5. Docstrings Abrangentes
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```
  
### 6. Suporte a Variáveis de Ambiente
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```
  
### 7. Degradação Elegante
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```
  

---

## Problemas Comuns e Soluções

### Problema: Erros de Importação
**Solução:** Instalar dependências em falta  
```bash
pip install sentence-transformers ragas datasets numpy
```
  

### Problema: Erros de Conexão
**Solução:** Garantir que o Foundry Local está em execução  
```bash
foundry service status
foundry model run phi-4-mini
```
  

### Problema: Modelo Não Encontrado
**Solução:** Verificar modelos disponíveis  
```bash
foundry model ls
foundry model download <alias>
```
  

### Problema: Desempenho Lento
**Solução:** Utilizar modelos menores ou ajustar parâmetros  
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```
  

---

## Próximos Passos

### 1. Testar Todos os Exemplos
Executar a lista de verificação de testes acima para verificar se todos os exemplos funcionam corretamente.

### 2. Atualizar Documentação
- Atualizar os ficheiros markdown das sessões com novos exemplos
- Adicionar secção de resolução de problemas ao README principal
- Criar guia de referência rápida

### 3. Criar Testes de Integração
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```
  

### 4. Adicionar Benchmarks de Desempenho
Acompanhar melhorias de desempenho provenientes das melhorias no tratamento de erros.

### 5. Feedback do Utilizador
Recolher feedback dos participantes do workshop sobre:
- Clareza das mensagens de erro
- Completude da documentação
- Facilidade de uso

---

## Recursos

- **SDK Local Foundry**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Referência Rápida**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **Notas de Migração**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **Repositório Principal**: https://github.com/microsoft/Foundry-Local  

---

## Manutenção

### Adicionar Novos Exemplos
Seguir estes padrões ao criar novos exemplos:

1. Utilizar `workshop_utils` para gestão de clientes
2. Adicionar tratamento de erros abrangente
3. Incluir suporte a variáveis de ambiente
4. Adicionar dicas de tipos e docstrings
5. Fornecer logging informativo
6. Incluir exemplos de uso em docstrings
7. Linkar à documentação do SDK

### Rever Atualizações
Ao rever atualizações de exemplos, verificar:
- [ ] Tratamento de erros em todas as operações de I/O
- [ ] Dicas de tipos em funções públicas
- [ ] Docstrings abrangentes
- [ ] Documentação de variáveis de ambiente
- [ ] Feedback informativo ao utilizador
- [ ] Links de referência ao SDK
- [ ] Estilo de código consistente

---

**Resumo**: Todos os exemplos em Python do Workshop agora seguem as melhores práticas do SDK Local Foundry, com tratamento de erros aprimorado, documentação abrangente e experiência do utilizador melhorada. Sem alterações disruptivas - toda a funcionalidade existente foi preservada e aprimorada.

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.