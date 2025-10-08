<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-08T20:53:59+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "pt"
}
-->
# Sessão 6: Foundry Local – Modelos como Ferramentas

## Resumo

Trate os modelos como ferramentas compostas dentro de uma camada operacional de IA local. Esta sessão mostra como encadear múltiplas chamadas especializadas de SLM/LLM, encaminhar tarefas seletivamente e expor uma superfície unificada de SDK para aplicações. Irá construir um roteador de modelos leve + planeador de tarefas, integrá-lo num script de aplicação e delinear o caminho de escalonamento para o Azure AI Foundry para cargas de trabalho em produção.

## Objetivos de Aprendizagem

- **Conceber** modelos como ferramentas atómicas com capacidades declaradas
- **Encaminhar** pedidos com base em intenção / pontuação heurística
- **Encadear** saídas em tarefas de múltiplos passos (decompor → resolver → refinar)
- **Integrar** uma API de cliente unificada para aplicações downstream
- **Escalar** o design para a cloud (mesmo contrato compatível com OpenAI)

## Pré-requisitos

- Sessões 1–5 concluídas
- Múltiplos modelos locais em cache (ex.: `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Fragmento de Ambiente Multiplataforma

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Acesso remoto/VM a partir de macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Fluxo de Demonstração (30 min)

### 1. Declaração de Capacidade de Ferramentas (5 min)

Crie `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Deteção de Intenção e Encaminhamento (8 min)

Crie `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Encadeamento de Tarefas de Múltiplos Passos (7 min)

Crie `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Projeto Inicial: Adaptar `06-models-as-tools` (5 min)

Melhorias:
- Adicionar suporte a tokens em streaming (atualização progressiva da interface)
- Adicionar pontuação de confiança: sobreposição lexical ou rubrica de prompt
- Exportar JSON de rastreio (intenção → modelo → latência → uso de tokens)
- Implementar reutilização de cache para subpassos repetidos

### 5. Caminho de Escalamento para Azure (5 min)

| Camada | Local (Foundry) | Cloud (Azure AI Foundry) | Estratégia de Transição |
|--------|-----------------|--------------------------|--------------------------|
| Encaminhamento | Python heurístico | Microsserviço durável | Containerizar e implementar API |
| Modelos | SLMs em cache | Implementações geridas | Mapear nomes locais para IDs de implementação |
| Observabilidade | Estatísticas CLI/manual | Registo central e métricas | Adicionar eventos de rastreio estruturados |
| Segurança | Apenas host local | Autenticação/rede Azure | Introduzir cofre de chaves para segredos |
| Custo | Recursos do dispositivo | Faturação por consumo | Adicionar limites de orçamento |

## Lista de Verificação de Validação

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Esperar seleção de modelo baseada em intenção e saída final refinada.

## Resolução de Problemas

| Problema | Causa | Solução |
|----------|-------|---------|
| Todas as tarefas encaminhadas para o mesmo modelo | Regras fracas | Enriquecer conjunto de regex INTENT_RULES |
| Pipeline falha a meio do passo | Modelo não carregado | Executar `foundry model run <model>` |
| Baixa coesão de saída | Sem fase de refinamento | Adicionar passo de sumarização/validação |

## Referências

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentação do Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Padrões de Qualidade de Prompt: Ver Sessão 2

---

**Duração da Sessão**: 30 min  
**Dificuldade**: Avançado

## Cenário de Exemplo e Mapeamento de Workshop

| Scripts / Notebooks do Workshop | Cenário | Objetivo | Fonte de Dataset / Catálogo |
|---------------------------------|---------|----------|-----------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Assistente de desenvolvimento lidando com prompts de intenção mista (refatorar, resumir, classificar) | Intenção heurística → encaminhamento de alias de modelo com uso de tokens | `CATALOG` inline + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Planeamento e refinamento de múltiplos passos para tarefa complexa de assistência em codificação | Decompor → execução especializada → passo de refinamento de sumarização | Mesmo `CATALOG`; passos derivados da saída do plano |

### Narrativa do Cenário

Uma ferramenta de produtividade de engenharia recebe tarefas heterogéneas: refatorar código, resumir notas arquiteturais, classificar feedback. Para minimizar latência e uso de recursos, um modelo geral pequeno planeia e resume, um modelo especializado em código lida com a refatoração, e um modelo leve capaz de classificação rotula o feedback. O script de pipeline demonstra encadeamento + refinamento; o script de roteador isola o encaminhamento adaptativo de um único prompt.

### Instantâneo do Catálogo

```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Exemplos de Prompts de Teste

```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Extensão de Rastreio (Opcional)

Adicionar linhas JSON de rastreio por passo para `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heurística de Escalamento (Ideia)

Se o plano contiver palavras-chave como "otimizar", "segurança", ou o comprimento do passo for > 280 caracteres → escalar para um modelo maior (ex.: `gpt-oss-20b`) apenas para esse passo.

### Melhorias Opcionais

| Área | Melhoria | Valor | Dica |
|------|----------|-------|------|
| Cache | Reutilizar objetos de gestor + cliente | Menor latência, menos overhead | Usar `workshop_utils.get_client` |
| Métricas de Uso | Capturar tokens e latência por passo | Perfilagem e otimização | Cronometrar cada chamada roteada; armazenar na lista de rastreio |
| Encaminhamento Adaptativo | Confiança / custo consciente | Melhor equilíbrio qualidade-custo | Adicionar pontuação: se prompt > N caracteres ou regex corresponder ao domínio → escalar para modelo maior |
| Registo Dinâmico de Capacidades | Catálogo de recarregamento dinâmico | Sem necessidade de reiniciar ou reimplementar | Carregar `catalog.json` em tempo de execução; monitorizar timestamp do ficheiro |
| Estratégia de Fallback | Robustez em falhas | Maior disponibilidade | Tentar primário → em exceção fallback para alias |
| Pipeline em Streaming | Feedback antecipado | Melhoria de UX | Transmitir cada passo e armazenar buffer para entrada de refinamento final |
| Embeddings de Intenção Vetorial | Encaminhamento mais detalhado | Maior precisão de intenção | Incorporar prompt, agrupar e mapear centróide → capacidade |
| Exportação de Rastreio | Encadeamento auditável | Conformidade/relatórios | Emitir linhas JSON: passo, intenção, modelo, latência_ms, tokens |
| Simulação de Custo | Estimativa pré-cloud | Planeamento de orçamento | Atribuir custo notional/token por modelo e agregar por tarefa |
| Modo Determinístico | Reproducibilidade | Benchmarking estável | Ambiente: `temperature=0`, número fixo de passos |

#### Exemplo de Estrutura de Rastreio

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Esboço de Escalamento Adaptativo

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Recarregamento Dinâmico do Catálogo de Modelos

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```


Iterar gradualmente—evitar sobreengenharia em protótipos iniciais.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.