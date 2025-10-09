<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T10:42:50+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "it"
}
-->
# Sessione 5: Crea Agenti Potenziati dall'AI Velocemente con Foundry Local

## Abstract

Progetta e orchestra agenti AI multi-ruolo sfruttando il runtime a bassa latenza e rispettoso della privacy di Foundry Local. Definirai i ruoli degli agenti, le strategie di memoria, i modelli di invocazione degli strumenti e i grafici di esecuzione. La sessione introduce modelli di scaffolding che puoi estendere con Chainlit o LangGraph. Il progetto iniziale estende l'architettura esistente degli agenti per aggiungere persistenza della memoria e ganci di valutazione.

## Obiettivi di Apprendimento

- **Definire Ruoli**: Prompt di sistema e limiti di capacità
- **Implementare Memoria**: Breve termine (conversazione), lungo termine (vettore/file), scratchpad effimeri
- **Scaffoldare Workflow**: Passaggi sequenziali, ramificati e paralleli degli agenti
- **Integrare Strumenti**: Modello leggero di chiamata di funzioni
- **Valutare**: Traccia di base + valutazione basata su rubriche

## Prerequisiti

- Completamento delle sessioni 1–4
- Python con `foundry-local-sdk`, `openai`, opzionale `chainlit`
- Modelli locali in esecuzione (almeno `phi-4-mini`)

### Snippet per Ambiente Cross-Platform

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Se esegui agenti da macOS contro un servizio host remoto Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Flusso Demo (30 min)

### 1. Definire Ruoli e Memoria degli Agenti (7 min)

Crea `samples/05-agents/agents_core.py`:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. Modello di Scaffolding CLI (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Aggiungere Invocazione degli Strumenti (7 min)

Estendi con `samples/05-agents/tools.py`:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```

Modifica `agents_core.py` per consentire una sintassi semplice per gli strumenti: l'utente scrive `#tool:get_time` e l'agente espande l'output dello strumento nel contesto prima della generazione.

### 4. Workflow Orchestrato (6 min)

Crea `samples/05-agents/orchestrator.py`:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. Progetto Iniziale: Estendi `05-agent-architecture` (7 min)

Aggiungi:
1. Livello di memoria persistente (ad esempio, append di conversazioni in linee JSON)
2. Rubrica di valutazione semplice: segnaposti per factualità, chiarezza e stile
3. Front-end opzionale Chainlit (due tab: conversazione e tracce)
4. Macchina a stati stile LangGraph opzionale (se aggiungi dipendenza) per decisioni ramificate

## Checklist di Validazione

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Aspettati un output della pipeline strutturato con nota di iniezione degli strumenti.

## Panoramica delle Strategie di Memoria

| Livello      | Scopo               | Esempio              |
|--------------|---------------------|----------------------|
| Breve termine | Continuità dialogo | Ultimi N messaggi    |
| Episodico     | Richiamo sessione  | JSON per sessione    |
| Semantico     | Recupero lungo termine | Archivio vettoriale di riassunti |
| Scratchpad    | Passaggi di ragionamento | Catena di pensiero inline (privata) |

## Ganci di Valutazione (Concettuale)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Risoluzione dei Problemi

| Problema            | Causa                     | Soluzione                     |
|---------------------|---------------------------|--------------------------------|
| Risposte ripetitive | Finestra di contesto troppo grande/piccola | Regola il parametro della finestra di memoria |
| Strumento non invocato | Sintassi errata          | Usa il formato `#tool:tool_name` |
| Orchestrazione lenta | Modelli multipli freddi  | Prompt di riscaldamento pre-esecuzione |

## Riferimenti

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (concetto opzionale): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Durata della Sessione**: 30 min  
**Difficoltà**: Avanzata

## Scenario di Esempio e Mappatura del Workshop

| Script del Workshop | Scenario | Obiettivo | Prompt di Esempio |
|---------------------|----------|-----------|-------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot di ricerca conoscitiva che produce riassunti adatti ai dirigenti | Pipeline a due agenti (ricerca → rifinitura editoriale) con modelli distinti opzionali | Spiega perché l'inferenza edge è importante per la conformità. |
| (Esteso) concetto `tools.py` | Aggiungi strumenti di stima del tempo e dei token | Dimostra il modello leggero di invocazione degli strumenti | #tool:get_time |

### Narrazione dello Scenario
Il team di documentazione per la conformità necessita di briefing interni rapidi basati su conoscenze locali senza inviare bozze a servizi cloud. Un agente ricercatore raccoglie punti fattuali concisi; un agente editor riscrive per chiarezza esecutiva. Alias di modelli distinti possono essere assegnati per ottimizzare la latenza (SLM veloce) rispetto alla rifinitura stilistica (modello più grande solo quando necessario).

### Ambiente Multi-Modello di Esempio
```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### Struttura delle Tracce (Opzionale)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

Persiste ogni passaggio in un file JSONL per successiva valutazione con rubriche.

### Miglioramenti Opzionali

| Tema              | Miglioramento              | Beneficio                     | Schizzo di Implementazione   |
|-------------------|----------------------------|-------------------------------|------------------------------|
| Ruoli Multi-Modello | Modelli distinti per agente (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specializzazione e velocità  | Seleziona alias variabili ambiente, chiama `chat_once` con alias per ruolo |
| Tracce Strutturate | Traccia JSON di ogni atto (strumento, input, latenza, token) | Debug e valutazione          | Aggiungi dizionario a una lista; scrivi `.jsonl` alla fine |
| Persistenza Memoria | Contesto dialogo ricaricabile | Continuità sessione          | Scarica `Agent.memory` in `sessions/<ts>.json` |
| Registro Strumenti | Scoperta dinamica degli strumenti | Estensibilità                | Mantieni dizionario `TOOLS` e ispeziona nomi/descrizioni |
| Retry & Backoff    | Catene lunghe robuste      | Riduci fallimenti transitori  | Avvolgi `act` con try/except + backoff esponenziale |
| Valutazione con Rubrica | Etichette qualitative automatiche | Traccia miglioramenti        | Secondo passaggio con modello: "Valuta chiarezza 1-5" |
| Memoria Vettoriale | Richiamo semantico         | Contesto ricco a lungo termine | Incorpora riassunti, recupera top-k nel messaggio di sistema |
| Risposte in Streaming | Risposta percepita più veloce | Miglioramento UX             | Usa streaming quando disponibile e svuota token parziali |
| Test Deterministici | Controllo regressione     | CI stabile                    | Esegui con `temperature=0`, semi di prompt fissi |
| Ramificazione Parallela | Esplorazione più veloce | Throughput                    | Usa `concurrent.futures` per passaggi indipendenti degli agenti |

#### Esempio di Registro delle Tracce

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Prompt di Valutazione Semplice

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Persiste coppie (`answer`, `rating`) per costruire un grafico storico della qualità.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.