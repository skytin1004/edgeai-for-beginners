<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T09:24:43+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "ne"
}
-->
# सत्र ५: फाउन्ड्री लोकलको साथमा छिटो AI-संचालित एजेन्ट निर्माण गर्नुहोस्

## सारांश

फाउन्ड्री लोकलको कम विलम्बता र गोपनीयता-संरक्षण रनटाइम प्रयोग गरेर बहु-भूमिका AI एजेन्टहरू डिजाइन र व्यवस्थापन गर्नुहोस्। तपाईं एजेन्ट भूमिकाहरू, मेमोरी रणनीतिहरू, उपकरण आह्वान ढाँचाहरू, र कार्यान्वयन ग्राफहरू परिभाषित गर्नुहुनेछ। सत्रले चेनलिट वा लांगग्राफसँग विस्तार गर्न सकिने स्काफोल्डिङ ढाँचाहरू प्रस्तुत गर्दछ। स्टार्ट प्रोजेक्टले मेमोरी स्थायित्व + मूल्यांकन हुकहरू थप्नको लागि विद्यमान एजेन्ट आर्किटेक्चर नमूनालाई विस्तार गर्दछ।

## सिकाइका उद्देश्यहरू

- **भूमिका परिभाषित गर्नुहोस्**: प्रणाली प्रॉम्प्टहरू र क्षमता सीमाहरू
- **मेमोरी कार्यान्वयन गर्नुहोस्**: छोटो अवधि (वार्तालाप), लामो अवधि (भेक्टर / फाइल), अस्थायी स्क्र्याचप्याडहरू
- **कार्यप्रवाह स्काफोल्ड गर्नुहोस्**: क्रमिक, शाखा, र समानान्तर एजेन्ट चरणहरू
- **उपकरणहरू एकीकृत गर्नुहोस्**: हल्का तौल कार्य उपकरण आह्वान ढाँचा
- **मूल्यांकन गर्नुहोस्**: आधारभूत ट्रेस + रुब्रिक-आधारित परिणाम स्कोरिङ

## पूर्वशर्तहरू

- सत्र १–४ पूरा भएको हुनुपर्छ
- `foundry-local-sdk`, `openai`, वैकल्पिक `chainlit` सहितको पाइथन
- स्थानीय मोडेलहरू चलिरहेको (कम्तीमा `phi-4-mini`)

### क्रस-प्ल्याटफर्म वातावरण स्निपेट

विन्डोज:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

म्याकओएस:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

यदि म्याकओएसबाट एजेन्टहरूलाई रिमोट विन्डोज होस्ट सेवाको विरुद्धमा चलाउँदै हुनुहुन्छ भने:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## डेमो प्रवाह (३० मिनेट)

### १. एजेन्ट भूमिकाहरू र मेमोरी परिभाषित गर्नुहोस् (७ मिनेट)

`samples/05-agents/agents_core.py` सिर्जना गर्नुहोस्:

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


### २. CLI स्काफोल्डिङ ढाँचा (३ मिनेट)

```powershell
python samples/05-agents/agents_core.py
```


### ३. उपकरण आह्वान थप्नुहोस् (७ मिनेट)

`samples/05-agents/tools.py` प्रयोग गरेर विस्तार गर्नुहोस्:

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


`agents_core.py` परिमार्जन गर्नुहोस् ताकि सरल उपकरण सिंट्याक्सलाई अनुमति दिन सकियोस्: प्रयोगकर्ताले `#tool:get_time` लेख्छन् र एजेन्टले जेनेरेशन अघि सन्दर्भमा उपकरणको आउटपुट विस्तार गर्दछ।

### ४. व्यवस्थित कार्यप्रवाह (६ मिनेट)

`samples/05-agents/orchestrator.py` सिर्जना गर्नुहोस्:

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


### ५. स्टार्ट प्रोजेक्ट: `05-agent-architecture` विस्तार गर्नुहोस् (७ मिनेट)

थप्नुहोस्:
1. स्थायी मेमोरी तह (जस्तै, वार्तालापहरूको JSON लाइनहरू थप्ने)
2. सरल मूल्यांकन रुब्रिक: तथ्यात्मकता / स्पष्टता / शैली प्लेसहोल्डरहरू
3. वैकल्पिक चेनलिट फ्रन्ट-एन्ड (दुई ट्याबहरू: वार्तालाप र ट्रेसहरू)
4. वैकल्पिक लांगग्राफ शैलीको राज्य मेसिन (यदि निर्भरता थप्दै हुनुहुन्छ भने) शाखा निर्णयहरूको लागि

## मान्यकरण चेकलिस्ट

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

उपकरण इंजेक्शन नोटसहित संरचित पाइपलाइन आउटपुट अपेक्षा गर्नुहोस्।

## मेमोरी रणनीतिहरूको अवलोकन

| तह | उद्देश्य | उदाहरण |
|----|---------|---------|
| छोटो अवधि | संवाद निरन्तरता | पछिल्लो N सन्देशहरू |
| एपिसोडिक | सत्र सम्झना | प्रत्येक सत्रको JSON |
| सेम्यान्टिक | लामो अवधि पुनःप्राप्ति | सारांशहरूको भेक्टर स्टोर |
| स्क्र्याचप्याड | तर्क चरणहरू | इनलाइन चेन-अफ-थट (निजी) |

## मूल्यांकन हुकहरू (धारणा)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## समस्या समाधान

| समस्या | कारण | समाधान |
|--------|-------|--------|
| दोहोरिने उत्तरहरू | सन्दर्भ विन्डो धेरै ठूलो/सानो | मेमोरी विन्डो प्यारामिटर ट्युन गर्नुहोस् |
| उपकरण आह्वान भएन | गलत सिंट्याक्स | `#tool:tool_name` ढाँचा प्रयोग गर्नुहोस् |
| सुस्त व्यवस्थापन | धेरै चिसो मोडेलहरू | प्रि-रन वार्मअप प्रॉम्प्टहरू प्रयोग गर्नुहोस् |

## सन्दर्भहरू

- फाउन्ड्री लोकल SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- लांगग्राफ (वैकल्पिक धारणा): https://github.com/langchain-ai/langgraph
- चेनलिट: https://docs.chainlit.io

---

**सत्र अवधि**: ३० मिनेट  
**कठिनाई स्तर**: उन्नत

## नमूना परिदृश्य र कार्यशाला म्यापिङ

| कार्यशाला स्क्रिप्ट | परिदृश्य | उद्देश्य | उदाहरण प्रॉम्प्ट |
|---------------------|----------|----------|-------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | कार्यकारी-अनुकूल सारांश उत्पादन गर्ने ज्ञान अनुसन्धान बोट | दुई-एजेन्ट पाइपलाइन (अनुसन्धान → सम्पादकीय परिष्कृत) वैकल्पिक अलग मोडेलहरूसँग | किन अनुपालनको लागि किनारा अनुमान महत्त्वपूर्ण छ भनेर व्याख्या गर्नुहोस्। |
| (विस्तारित) `tools.py` धारणा | समय र टोकन अनुमान उपकरणहरू थप्नुहोस् | हल्का तौल उपकरण आह्वान ढाँचा प्रदर्शन गर्नुहोस् | #tool:get_time |

### परिदृश्य कथा

अनुपालन दस्तावेजीकरण टोलीलाई क्लाउड सेवाहरूमा ड्राफ्टहरू पठाउन बिना स्थानीय ज्ञानबाट छिटो आन्तरिक संक्षेपहरू आवश्यक छ। अनुसन्धानकर्ता एजेन्टले संक्षिप्त तथ्यात्मक बुलेटहरू संकलन गर्दछ; सम्पादक एजेन्टले कार्यकारी स्पष्टताको लागि पुनर्लेखन गर्दछ। विलम्बता अनुकूलन गर्न (छिटो SLM) बनाम शैलीगत परिष्कृत (ठूलो मोडेल केवल आवश्यक हुँदा) अलग मोडेल उपनामहरू असाइन गर्न सकिन्छ।

### उदाहरण बहु-मोडेल वातावरण

```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### ट्रेस संरचना (वैकल्पिक)

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

प्रत्येक चरणलाई JSONL फाइलमा स्थायी बनाउनुहोस् ताकि पछि रुब्रिक स्कोरिङ गर्न सकियोस्।

### वैकल्पिक सुधारहरू

| विषयवस्तु | सुधार | फाइदा | कार्यान्वयन स्केच |
|-----------|-------|-------|-------------------|
| बहु-मोडेल भूमिकाहरू | प्रत्येक एजेन्टका लागि अलग मोडेलहरू (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | विशेषज्ञता र गति | उपनाम वातावरण भेरिएबलहरू चयन गर्नुहोस्, प्रत्येक भूमिकाको उपनामसँग `chat_once` कल गर्नुहोस् |
| संरचित ट्रेसहरू | प्रत्येक कार्य (उपकरण, इनपुट, विलम्बता, टोकन) को JSON ट्रेस | डिबग र मूल्यांकन | सूचीमा डिक्ट थप्नुहोस्; अन्तमा `.jsonl` लेख्नुहोस् |
| मेमोरी स्थायित्व | पुनःलोड गर्न मिल्ने संवाद सन्दर्भ | सत्र निरन्तरता | `Agent.memory` लाई `sessions/<ts>.json` मा डम्प गर्नुहोस् |
| उपकरण रजिस्ट्री | गतिशील उपकरण खोजी | विस्तारशीलता | `TOOLS` डिक्ट राख्नुहोस् र नाम/वर्णनको निरीक्षण गर्नुहोस् |
| पुनः प्रयास र ब्याकअफ | लामो चेनहरूमा मजबूती | अस्थायी असफलता घटाउनुहोस् | `act` लाई try/except + exponential backoff संग र्‍याप गर्नुहोस् |
| रुब्रिक स्कोरिङ | स्वचालित गुणात्मक लेबलहरू | सुधारहरू ट्र्याक गर्नुहोस् | दोस्रो पास मोडेललाई प्रॉम्प्ट गर्नुहोस्: "स्पष्टता १-५ मा दर दिनुहोस्" |
| भेक्टर मेमोरी | सेम्यान्टिक पुनःप्राप्ति | समृद्ध लामो अवधि सन्दर्भ | सारांशहरू एम्बेड गर्नुहोस्, शीर्ष-k लाई प्रणाली सन्देशमा पुनःप्राप्त गर्नुहोस् |
| स्ट्रिमिङ उत्तरहरू | छिटो अनुभूत प्रतिक्रिया | UX सुधार | स्ट्रिमिङ उपलब्ध भएपछि प्रयोग गर्नुहोस् र आंशिक टोकनहरू फ्लस गर्नुहोस् |
| निर्धारणात्मक परीक्षणहरू | पुनरावृत्ति नियन्त्रण | स्थिर CI | `temperature=0`, निश्चित प्रॉम्प्ट बीजहरूसँग चलाउनुहोस् |
| समानान्तर शाखा | छिटो अन्वेषण | थ्रुपुट | स्वतन्त्र एजेन्ट चरणहरूको लागि `concurrent.futures` प्रयोग गर्नुहोस् |

#### ट्रेस रेकर्ड उदाहरण

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### सरल मूल्यांकन प्रॉम्प्ट

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

(`answer`, `rating`) जोडीहरूलाई स्थायी बनाउनुहोस् ताकि ऐतिहासिक गुणस्तर ग्राफ निर्माण गर्न सकियोस्।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।