<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-09T11:00:21+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "pa"
}
-->
# ਸੈਸ਼ਨ 6: Foundry Local – ਮਾਡਲਾਂ ਨੂੰ ਟੂਲ ਵਜੋਂ ਵਰਤਣਾ

## ਸਾਰ

ਮਾਡਲਾਂ ਨੂੰ ਇੱਕ ਸਥਾਨਕ AI ਓਪਰੇਟਿੰਗ ਲੇਅਰ ਦੇ ਅੰਦਰ ਸੰਯੋਜਨੀਯ ਟੂਲ ਵਜੋਂ ਵਰਤੋ। ਇਸ ਸੈਸ਼ਨ ਵਿੱਚ ਦਿਖਾਇਆ ਗਿਆ ਹੈ ਕਿ ਕਿਵੇਂ ਕਈ ਵਿਸ਼ੇਸ਼ SLM/LLM ਕਾਲਾਂ ਨੂੰ ਜੋੜਨਾ ਹੈ, ਕੰਮਾਂ ਨੂੰ ਚੁਣਿੰਦਾ ਰੂਪ ਵਿੱਚ ਰੂਟ ਕਰਨਾ ਹੈ, ਅਤੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਇੱਕ ਇਕਰੂਪ SDK ਸਤਹ ਉਘਾੜਨੀ ਹੈ। ਤੁਸੀਂ ਇੱਕ ਹਲਕਾ ਮਾਡਲ ਰਾਊਟਰ + ਟਾਸਕ ਪਲੈਨਰ ਬਣਾਉਗੇ, ਇਸਨੂੰ ਇੱਕ ਐਪ ਸਕ੍ਰਿਪਟ ਵਿੱਚ ਇਕੱਠਾ ਕਰੋਗੇ, ਅਤੇ ਉਤਪਾਦਨ ਵਰਕਲੋਡ ਲਈ Azure AI Foundry ਤੱਕ ਸਕੇਲਿੰਗ ਦਾ ਰਾਹ ਰੇਖਾ ਬਣਾਉਗੇ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

- **ਸਮਝੋ** ਮਾਡਲਾਂ ਨੂੰ ਐਟਾਮਿਕ ਟੂਲ ਵਜੋਂ ਜਿਨ੍ਹਾਂ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਘੋਸ਼ਿਤ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ  
- **ਰੂਟ ਕਰੋ** ਬੇਨਤੀ ਨੂੰ ਇਰਾਦੇ / ਹਿਊਰਿਸਟਿਕ ਸਕੋਰਿੰਗ ਦੇ ਆਧਾਰ 'ਤੇ  
- **ਚੇਨ ਕਰੋ** ਆਉਟਪੁੱਟ ਨੂੰ ਬਹੁ-ਕਦਮ ਕੰਮਾਂ ਵਿੱਚ (ਵੰਡੋ → ਹੱਲ ਕਰੋ → ਸੁਧਾਰੋ)  
- **ਇਕੱਠਾ ਕਰੋ** ਡਾਊਨਸਟ੍ਰੀਮ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਇੱਕ ਇਕਰੂਪ ਕਲਾਇੰਟ API  
- **ਸਕੇਲ ਕਰੋ** ਡਿਜ਼ਾਈਨ ਨੂੰ ਕਲਾਉਡ (ਉਹੀ OpenAI-ਅਨੁਕੂਲ ਸੰਬੰਧ)  

## ਪੂਰਵ ਸ਼ਰਤਾਂ

- ਸੈਸ਼ਨ 1–5 ਪੂਰੇ ਕੀਤੇ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ  
- ਕਈ ਸਥਾਨਕ ਮਾਡਲ ਕੈਸ਼ ਕੀਤੇ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ (ਜਿਵੇਂ ਕਿ `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)  

### ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਵਾਤਾਵਰਣ ਸਨਿੱਪਟ

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
  
Remote/VM ਸੇਵਾ ਪਹੁੰਚ macOS ਤੋਂ:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## ਡੈਮੋ ਫਲੋ (30 ਮਿੰਟ)

### 1. ਟੂਲ ਸਮਰੱਥਾ ਘੋਸ਼ਣਾ (5 ਮਿੰਟ)

`samples/06-tools/models_catalog.py` ਬਣਾਓ:  

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
  

### 2. ਇਰਾਦਾ ਪਛਾਣ ਅਤੇ ਰੂਟਿੰਗ (8 ਮਿੰਟ)

`samples/06-tools/router.py` ਬਣਾਓ:  

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
  

### 3. ਬਹੁ-ਕਦਮ ਟਾਸਕ ਚੇਨਿੰਗ (7 ਮਿੰਟ)

`samples/06-tools/pipeline.py` ਬਣਾਓ:  

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
  

### 4. ਸ਼ੁਰੂਆਤੀ ਪ੍ਰੋਜੈਕਟ: `06-models-as-tools` ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਓ (5 ਮਿੰਟ)

ਸੁਧਾਰ:  
- ਸਟ੍ਰੀਮਿੰਗ ਟੋਕਨ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕਰੋ (ਪ੍ਰਗਤੀਸ਼ੀਲ UI ਅਪਡੇਟ)  
- ਵਿਸ਼ਵਾਸ ਸਕੋਰਿੰਗ ਸ਼ਾਮਲ ਕਰੋ: ਲੈਕਸਿਕਲ ਓਵਰਲੈਪ ਜਾਂ ਪ੍ਰੌੰਪਟ ਰੂਬ੍ਰਿਕ  
- ਟ੍ਰੇਸ JSON ਐਕਸਪੋਰਟ ਕਰੋ (ਇਰਾਦਾ → ਮਾਡਲ → ਲੈਟੈਂਸੀ → ਟੋਕਨ ਵਰਤੋਂ)  
- ਦੁਹਰਾਏ ਗਏ ਉਪ-ਕਦਮਾਂ ਲਈ ਕੈਸ਼ ਦੁਬਾਰਾ ਵਰਤੋ  

### 5. Azure ਤੱਕ ਸਕੇਲਿੰਗ ਰਾਹ (5 ਮਿੰਟ)

| ਲੇਅਰ | ਸਥਾਨਕ (Foundry) | ਕਲਾਉਡ (Azure AI Foundry) | ਸੰਕ੍ਰਮਣ ਰਣਨੀਤੀ |  
|-------|-----------------|--------------------------|---------------------|  
| ਰੂਟਿੰਗ | ਹਿਊਰਿਸਟਿਕ ਪਾਇਥਨ | ਡਿਊਰੇਬਲ ਮਾਈਕਰੋਸਰਵਿਸ | API ਨੂੰ ਕੰਟੇਨਰਾਈਜ਼ ਅਤੇ ਡਿਪਲੌਇ ਕਰੋ |  
| ਮਾਡਲ | SLMs ਕੈਸ਼ ਕੀਤੇ | ਪ੍ਰਬੰਧਿਤ ਡਿਪਲੌਇਮੈਂਟ | ਸਥਾਨਕ ਨਾਮਾਂ ਨੂੰ ਡਿਪਲੌਇਮੈਂਟ ID ਨਾਲ ਮੈਪ ਕਰੋ |  
| ਅਵਲੋਕਨਯੋਗਤਾ | CLI ਅੰਕੜੇ/ਮੈਨੁਅਲ | ਕੇਂਦਰੀ ਲੌਗਿੰਗ ਅਤੇ ਮੈਟ੍ਰਿਕਸ | ਸਟ੍ਰਕਚਰਡ ਟ੍ਰੇਸ ਇਵੈਂਟ ਸ਼ਾਮਲ ਕਰੋ |  
| ਸੁਰੱਖਿਆ | ਸਿਰਫ਼ ਸਥਾਨਕ ਹੋਸਟ | Azure ਪ੍ਰਮਾਣਿਕਤਾ / ਨੈਟਵਰਕਿੰਗ | ਗੁਪਤਾਂ ਲਈ ਕੀ ਵੌਲਟ ਸ਼ਾਮਲ ਕਰੋ |  
| ਲਾਗਤ | ਡਿਵਾਈਸ ਸਰੋਤ | ਖਪਤ ਬਿਲਿੰਗ | ਬਜਟ ਗਾਰਡਰੇਲ ਸ਼ਾਮਲ ਕਰੋ |  

## ਵੈਧਤਾ ਚੈੱਕਲਿਸਟ

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
ਇਰਾਦੇ-ਅਧਾਰਿਤ ਮਾਡਲ ਚੋਣ ਅਤੇ ਅੰਤਮ ਸੁਧਾਰਿਆ ਆਉਟਪੁੱਟ ਦੀ ਉਮੀਦ ਕਰੋ।  

## ਸਮੱਸਿਆ ਨਿਵਾਰਨ

| ਸਮੱਸਿਆ | ਕਾਰਨ | ਠੀਕ |  
|---------|-------|-----|  
| ਸਾਰੇ ਕੰਮ ਇੱਕੋ ਮਾਡਲ ਨੂੰ ਰੂਟ ਕੀਤੇ ਗਏ | ਕਮਜ਼ੋਰ ਨਿਯਮ | INTENT_RULES ਰੈਗੁਲਰ ਐਕਸਪ੍ਰੈਸ਼ਨ ਸੈੱਟ ਨੂੰ ਸੰਮ੍ਰਿੱਧ ਕਰੋ |  
| ਪਾਈਪਲਾਈਨ ਮੱਧ-ਕਦਮ 'ਤੇ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦੀ ਹੈ | ਲੋਡ ਕੀਤਾ ਮਾਡਲ ਗਾਇਬ | `foundry model run <model>` ਚਲਾਓ |  
| ਆਉਟਪੁੱਟ ਸੰਗਠਨ ਘੱਟ ਹੈ | ਕੋਈ ਸੁਧਾਰ ਚਰਣ ਨਹੀਂ | ਸਾਰ/ਪ੍ਰਮਾਣਿਕਤਾ ਪਾਸ ਸ਼ਾਮਲ ਕਰੋ |  

## ਹਵਾਲੇ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry  
- ਪ੍ਰੌੰਪਟ ਗੁਣਵੱਤਾ ਪੈਟਰਨ: ਸੈਸ਼ਨ 2 ਵੇਖੋ  

---

**ਸੈਸ਼ਨ ਦੀ ਮਿਆਦ**: 30 ਮਿੰਟ  
**ਮੁਸ਼ਕਲਾਈ ਪੱਧਰ**: ਮਾਹਰ  

## ਨਮੂਨਾ ਦ੍ਰਿਸ਼ ਅਤੇ ਵਰਕਸ਼ਾਪ ਮੈਪਿੰਗ

| ਵਰਕਸ਼ਾਪ ਸਕ੍ਰਿਪਟ / ਨੋਟਬੁੱਕ | ਦ੍ਰਿਸ਼ | ਉਦੇਸ਼ | ਡਾਟਾਸੈਟ / ਕੈਟਾਲੌਗ ਸਰੋਤ |  
|------------------------------|----------|-----------|---------------------------|  
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | ਡਿਵੈਲਪਰ ਸਹਾਇਕ ਜੋ ਮਿਲੇ-ਜੁਲੇ ਇਰਾਦੇ ਵਾਲੇ ਪ੍ਰੌੰਪਟਾਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ (ਰੀਫੈਕਟਰ, ਸਾਰ, ਵਰਗੀਕਰਨ) | ਹਿਊਰਿਸਟਿਕ ਇਰਾਦਾ → ਮਾਡਲ ਉਪਨਾਮ ਰੂਟਿੰਗ ਟੋਕਨ ਵਰਤੋਂ ਨਾਲ | ਇਨਲਾਈਨ `CATALOG` + ਰੈਗੁਲਰ ਐਕਸਪ੍ਰੈਸ਼ਨ `RULES` |  
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | ਜਟਿਲ ਕੋਡਿੰਗ ਸਹਾਇਕ ਕੰਮ ਲਈ ਬਹੁ-ਕਦਮ ਯੋਜਨਾ ਅਤੇ ਸੁਧਾਰ | ਵੰਡੋ → ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨਾਲ ਕਾਰਜ → ਸਾਰ ਸੁਧਾਰ ਚਰਣ | ਉਹੀ `CATALOG`; ਕਦਮ ਯੋਜਨਾ ਆਉਟਪੁੱਟ ਤੋਂ ਲਏ ਗਏ |  

### ਦ੍ਰਿਸ਼ ਕਹਾਣੀ

ਇੱਕ ਇੰਜੀਨੀਅਰਿੰਗ ਉਤਪਾਦਕਤਾ ਟੂਲ ਨੂੰ ਵੱਖ-ਵੱਖ ਕੰਮ ਮਿਲਦੇ ਹਨ: ਕੋਡ ਨੂੰ ਰੀਫੈਕਟਰ ਕਰੋ, ਆਰਕੀਟੈਕਚਰਲ ਨੋਟਾਂ ਦਾ ਸਾਰ ਲਿਖੋ, ਫੀਡਬੈਕ ਨੂੰ ਵਰਗੀਕ੍ਰਿਤ ਕਰੋ। ਲੈਟੈਂਸੀ ਅਤੇ ਸਰੋਤ ਦੀ ਵਰਤੋਂ ਨੂੰ ਘਟਾਉਣ ਲਈ, ਇੱਕ ਛੋਟਾ ਜਨਰਲ ਮਾਡਲ ਯੋਜਨਾ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਸਾਰ ਲਿਖਦਾ ਹੈ, ਇੱਕ ਕੋਡ-ਵਿਸ਼ੇਸ਼ ਮਾਡਲ ਰੀਫੈਕਟੋਰਿੰਗ ਕਰਦਾ ਹੈ, ਅਤੇ ਇੱਕ ਹਲਕਾ ਵਰਗੀਕਰਨ-ਸਮਰੱਥ ਮਾਡਲ ਫੀਡਬੈਕ ਨੂੰ ਲੇਬਲ ਕਰਦਾ ਹੈ। ਪਾਈਪਲਾਈਨ ਸਕ੍ਰਿਪਟ ਚੇਨਿੰਗ + ਸੁਧਾਰ ਦਿਖਾਉਂਦਾ ਹੈ; ਰਾਊਟਰ ਸਕ੍ਰਿਪਟ ਅਨੁਕੂਲ ਸਿੰਗਲ-ਪ੍ਰੌੰਪਟ ਰੂਟਿੰਗ ਨੂੰ ਅਲੱਗ ਕਰਦਾ ਹੈ।  

### ਕੈਟਾਲੌਗ ਸਨੈਪਸ਼ਾਟ

```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```
  

### ਉਦਾਹਰਣ ਟੈਸਟ ਪ੍ਰੌੰਪਟ

```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```
  

### ਟ੍ਰੇਸ ਐਕਸਟੈਂਸ਼ਨ (ਵਿਕਲਪਿਕ)

`models_pipeline.py` ਲਈ ਪ੍ਰਤੀ-ਕਦਮ ਟ੍ਰੇਸ JSON ਲਾਈਨਾਂ ਸ਼ਾਮਲ ਕਰੋ:  
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```
  

### ਐਸਕਲੇਸ਼ਨ ਹਿਊਰਿਸਟਿਕ (ਵਿਚਾਰ)

ਜੇ ਯੋਜਨਾ ਵਿੱਚ "optimize", "security" ਵਰਗੇ ਕੀਵਰਡ ਸ਼ਾਮਲ ਹਨ ਜਾਂ ਕਦਮ ਦੀ ਲੰਬਾਈ > 280 ਅੱਖਰ ਹੈ → ਉਸ ਕਦਮ ਲਈ ਵੱਡੇ ਮਾਡਲ (ਜਿਵੇਂ ਕਿ `gpt-oss-20b`) ਨੂੰ ਉੱਚਾ ਕਰੋ।  

### ਵਿਕਲਪਿਕ ਸੁਧਾਰ

| ਖੇਤਰ | ਸੁਧਾਰ | ਮੁੱਲ | ਸੰਕੇਤ |  
|------|-------------|-------|------|  
| ਕੈਸ਼ਿੰਗ | ਮੈਨੇਜਰ + ਕਲਾਇੰਟ ਆਬਜੈਕਟ ਦੁਬਾਰਾ ਵਰਤੋ | ਘੱਟ ਲੈਟੈਂਸੀ, ਘੱਟ ਓਵਰਹੈੱਡ | `workshop_utils.get_client` ਵਰਤੋ |  
| ਵਰਤੋਂ ਮੈਟ੍ਰਿਕਸ | ਟੋਕਨ ਅਤੇ ਪ੍ਰਤੀ-ਕਦਮ ਲੈਟੈਂਸੀ ਕੈਪਚਰ ਕਰੋ | ਪ੍ਰੋਫਾਈਲਿੰਗ ਅਤੇ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ | ਹਰ ਰੂਟ ਕੀਤੀ ਕਾਲ ਦਾ ਸਮਾਂ ਲਵੋ; ਟ੍ਰੇਸ ਸੂਚੀ ਵਿੱਚ ਸਟੋਰ ਕਰੋ |  
| ਅਨੁਕੂਲ ਰੂਟਿੰਗ | ਵਿਸ਼ਵਾਸ / ਲਾਗਤ ਸਚੇਤ | ਗੁਣਵੱਤਾ-ਲਾਗਤ ਦਾ ਵਧੀਆ ਸੰਤੁਲਨ | ਸਕੋਰਿੰਗ ਸ਼ਾਮਲ ਕਰੋ: ਜੇ ਪ੍ਰੌੰਪਟ > N ਅੱਖਰ ਜਾਂ ਰੈਗੁਲਰ ਐਕਸਪ੍ਰੈਸ਼ਨ ਡੋਮੇਨ ਨੂੰ ਮਿਲਦਾ ਹੈ → ਵੱਡੇ ਮਾਡਲ ਨੂੰ ਉੱਚਾ ਕਰੋ |  
| ਗਤੀਸ਼ੀਲ ਸਮਰੱਥਾ ਰਜਿਸਟਰੀ | ਕੈਟਾਲੌਗ ਨੂੰ ਗਰਮ ਰੀਲੋਡ ਕਰੋ | ਕੋਈ ਰੀਸਟਾਰਟ ਰੀਡਿਪਲੌਇ ਨਹੀਂ | ਰਨਟਾਈਮ 'ਤੇ `catalog.json` ਲੋਡ ਕਰੋ; ਫਾਈਲ ਟਾਈਮਸਟੈਂਪ ਦੇਖੋ |  
| ਫਾਲਬੈਕ ਰਣਨੀਤੀ | ਅਸਫਲਤਾਵਾਂ ਦੇ ਹੇਠਾਂ ਮਜ਼ਬੂਤੀ | ਵਧੇਰੇ ਉਪਲਬਧਤਾ | ਪ੍ਰਾਇਮਰੀ ਨੂੰ ਕੋਸ਼ਿਸ਼ ਕਰੋ → ਐਕਸਪਸ਼ਨ 'ਤੇ ਫਾਲਬੈਕ ਉਪਨਾਮ |  
| ਸਟ੍ਰੀਮਿੰਗ ਪਾਈਪਲਾਈਨ | ਜਲਦੀ ਫੀਡਬੈਕ | UX ਸੁਧਾਰ | ਹਰ ਕਦਮ ਨੂੰ ਸਟ੍ਰੀਮ ਕਰੋ ਅਤੇ ਅੰਤਮ ਸੁਧਾਰ ਇਨਪੁੱਟ ਨੂੰ ਬਫਰ ਕਰੋ |  
| ਵੈਕਟਰ ਇਰਾਦਾ ਐਮਬੈਡਿੰਗ | ਹੋਰ ਸੁਧਾਰਿਆ ਰੂਟਿੰਗ | ਵਧੇਰੇ ਇਰਾਦੇ ਦੀ ਸਹੀਤਾ | ਪ੍ਰੌੰਪਟ ਨੂੰ ਐਮਬੈਡ ਕਰੋ, ਕਲੱਸਟਰ ਕਰੋ ਅਤੇ ਸੈਂਟਰਾਇਡ ਨੂੰ ਮੈਪ ਕਰੋ → ਸਮਰੱਥਾ |  
| ਟ੍ਰੇਸ ਐਕਸਪੋਰਟ | ਆਡਿਟੇਬਲ ਚੇਨ | ਅਨੁਕੂਲਤਾ/ਰਿਪੋਰਟਿੰਗ | JSON ਲਾਈਨਾਂ ਜਾਰੀ ਕਰੋ: ਕਦਮ, ਇਰਾਦਾ, ਮਾਡਲ, ਲੈਟੈਂਸੀ_ms, ਟੋਕਨ |  
| ਲਾਗਤ ਸਿਮੂਲੇਸ਼ਨ | ਪ੍ਰੀ-ਕਲਾਉਡ ਅਨੁਮਾਨ | ਬਜਟ ਦੀ ਯੋਜਨਾ | ਪ੍ਰਤੀ-ਮਾਡਲ ਨੋਸ਼ਨਲ ਲਾਗਤ/ਟੋਕਨ ਸੌਂਪੋ ਅਤੇ ਪ੍ਰਤੀ-ਕੰਮ ਜੋੜੋ |  
| ਨਿਰਧਾਰਿਤ ਮੋਡ | ਦੁਬਾਰਾ ਪ੍ਰਜਨਨਯੋਗਤਾ | ਸਥਿਰ ਬੈਂਚਮਾਰਕਿੰਗ | Env: `temperature=0`, ਨਿਰਧਾਰਿਤ ਕਦਮ ਗਿਣਤੀ |  

#### ਟ੍ਰੇਸ ਸਟ੍ਰਕਚਰ ਉਦਾਹਰਣ

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```
  

#### ਅਨੁਕੂਲ ਐਸਕਲੇਸ਼ਨ ਸਕੈਚ

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```
  

#### ਮਾਡਲ ਕੈਟਾਲੌਗ ਹੌਟ ਰੀਲੋਡ

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
  

ਧੀਰੇ-ਧੀਰੇ ਦੁਹਰਾਓ—ਸ਼ੁਰੂਆਤੀ ਪ੍ਰੋਟੋਟਾਈਪਾਂ ਨੂੰ ਜ਼ਿਆਦਾ ਇੰਜੀਨੀਅਰਿੰਗ ਨਾ ਕਰੋ।  

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਅਸਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।