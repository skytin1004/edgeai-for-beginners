<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T16:43:16+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "he"
}
-->
# מפגש 5: בניית סוכנים מבוססי AI במהירות עם Foundry Local

## תקציר

תכננו ותזמנו סוכני AI מרובי תפקידים באמצעות Foundry Local, המציע זמן ריצה מהיר ושומר פרטיות. במפגש זה תלמדו להגדיר תפקידי סוכנים, אסטרטגיות זיכרון, דפוסי קריאה לכלים וגרפי ביצוע. המפגש מציג תבניות בסיס שתוכלו להרחיב באמצעות Chainlit או LangGraph. פרויקט ההתחלה מרחיב את דוגמת ארכיטקטורת הסוכן הקיימת להוספת שכבת זיכרון מתמשך + ווים להערכה.

## מטרות למידה

- **הגדרת תפקידים**: הנחיות מערכת והגדרת גבולות יכולת  
- **מימוש זיכרון**: זיכרון קצר-טווח (שיחה), זיכרון ארוך-טווח (וקטורי / קבצים), לוחות זמניים  
- **תכנון תהליכי עבודה**: שלבים עוקבים, מתפצלים ומקבילים  
- **שילוב כלים**: דפוס קריאה לכלים באמצעות פונקציות קלות משקל  
- **הערכה**: מעקב בסיסי + ניקוד תוצאות מבוסס קריטריונים  

## דרישות מוקדמות

- השלמת מפגשים 1–4  
- Python עם `foundry-local-sdk`, `openai`, אופציונלי `chainlit`  
- מודלים מקומיים פועלים (לפחות `phi-4-mini`)  

### קטע קוד לסביבת עבודה חוצת פלטפורמות

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
  
אם מפעילים סוכנים מ-macOS מול שירות מארח מרוחק ב-Windows:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## זרימת הדגמה (30 דקות)

### 1. הגדרת תפקידי סוכן וזיכרון (7 דקות)

צרו `samples/05-agents/agents_core.py`:  

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
  

### 2. תבנית CLI לתכנון (3 דקות)

```powershell
python samples/05-agents/agents_core.py
```
  

### 3. הוספת קריאה לכלים (7 דקות)

הרחיבו עם `samples/05-agents/tools.py`:  

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
  
שנו את `agents_core.py` כך שיאפשר תחביר פשוט לקריאה לכלים: המשתמש כותב `#tool:get_time` והסוכן משלב את פלט הכלי בהקשר לפני יצירת התגובה.  

### 4. תהליך עבודה מתוזמר (6 דקות)

צרו `samples/05-agents/orchestrator.py`:  

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
  

### 5. פרויקט התחלה: הרחבת `05-agent-architecture` (7 דקות)

הוסיפו:  
1. שכבת זיכרון מתמשך (לדוגמה, הוספת שורות JSON של שיחות)  
2. קריטריונים פשוטים להערכה: עובדתיות / בהירות / סגנון  
3. ממשק Chainlit אופציונלי (שני טאבים: שיחה ומעקב)  
4. מכונת מצבים בסגנון LangGraph (אופציונלי, אם מוסיפים תלות) להחלטות מתפצלות  

## רשימת בדיקות לאימות

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```
  
צפו בפלט צינור מובנה עם הערה על הזרקת כלים.  

## סקירה של אסטרטגיות זיכרון

| שכבה | מטרה | דוגמה |  
|-------|---------|---------|  
| קצר-טווח | המשכיות שיחה | N ההודעות האחרונות |  
| אפיזודי | זיכרון מפגש | JSON לכל מפגש |  
| סמנטי | שליפה ארוכת-טווח | מאגר וקטורים של סיכומים |  
| לוח זמני | שלבי חשיבה | שרשרת מחשבות פרטית |  

## ווים להערכה (קונספטואלי)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```
  

## פתרון בעיות

| בעיה | סיבה | פתרון |  
|-------|------|------------|  
| תשובות חוזרות | חלון הקשר גדול/קטן מדי | כווננו את פרמטר חלון הזיכרון |  
| כלי לא הופעל | תחביר שגוי | השתמשו בפורמט `#tool:tool_name` |  
| תזמור איטי | מודלים מרובים קרים | הריצו פקודות חימום מראש |  

## מקורות

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- LangGraph (קונספט אופציונלי): https://github.com/langchain-ai/langgraph  
- Chainlit: https://docs.chainlit.io  

---

**משך המפגש**: 30 דקות  
**רמת קושי**: מתקדם  

## תרחיש לדוגמה ומיפוי סדנה

| סקריפט סדנה | תרחיש | מטרה | דוגמת הנחיה |  
|-----------------|----------|-----------|----------------|  
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | בוט מחקר ידע המפיק סיכומים ידידותיים למנהלים | צינור דו-סוכני (מחקר → ליטוש עריכתי) עם מודלים נפרדים אופציונליים | הסבר מדוע הסקת קצה חשובה לצורך עמידה בתקנות. |  
| (מורחב) קונספט `tools.py` | הוספת כלים להערכת זמן ומספר אסימונים | הדגמת דפוס קריאה קל לכלים | #tool:get_time |  

### נרטיב תרחיש
צוות תיעוד הציות זקוק לתדריכים פנימיים מהירים המבוססים על ידע מקומי, מבלי לשלוח טיוטות לשירותי ענן. סוכן מחקר אוסף נקודות עובדתיות תמציתיות; סוכן עורך משכתב אותן לבהירות מנהלית. ניתן להקצות כינויים למודלים נפרדים כדי לייעל את זמן התגובה (SLM מהיר) לעומת שיפור סגנוני (מודל גדול יותר רק כשנדרש).  

### דוגמה לסביבת עבודה מרובת מודלים
```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```
  

### מבנה מעקב (אופציונלי)
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
  
שמרו כל שלב לקובץ JSONL לצורך ניקוד קריטריונים מאוחר יותר.  

### שיפורים אופציונליים

| נושא | שיפור | יתרון | סקיצה ליישום |  
|-------|------------|---------|-----------------------|  
| תפקידי מודלים מרובים | מודלים נפרדים לכל סוכן (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | התמחות ומהירות | בחרו משתני סביבה לכינויים, קראו ל-`chat_once` עם כינוי לכל תפקיד |  
| מעקב מובנה | מעקב JSON לכל פעולה (כלי, קלט, זמן תגובה, אסימונים) | ניפוי באגים והערכה | הוסיפו מילון לרשימה; כתבו `.jsonl` בסיום |  
| זיכרון מתמשך | הקשר שיחה נטען מחדש | המשכיות מפגש | שמרו את `Agent.memory` ל-`sessions/<ts>.json` |  
| רישום כלים | גילוי כלים דינמי | הרחבה | תחזקו מילון `TOOLS` ובדקו שמות/תיאורים |  
| ניסיונות חוזרים והשהיה | שרשראות ארוכות עמידות | הפחתת כשלים זמניים | עטפו את `act` עם try/except + השהיה אקספוננציאלית |  
| ניקוד קריטריונים | תוויות איכות אוטומטיות | מעקב אחר שיפורים | מעבר שני עם מודל: "דרג בהירות 1-5" |  
| זיכרון וקטורי | שליפה סמנטית | הקשר עשיר לטווח ארוך | הטמיעו סיכומים, שלפו את ה-top-k להודעת מערכת |  
| תגובות זורמות | תגובה מהירה יותר למשתמש | שיפור חוויית משתמש | השתמשו בזרימה ברגע שתהיה זמינה ושחררו אסימונים חלקיים |  
| בדיקות דטרמיניסטיות | שליטה ברגרסיה | CI יציב | הריצו עם `temperature=0`, זרעי הנחיה קבועים |  
| הסתעפות מקבילה | חקר מהיר יותר | תפוקה | השתמשו ב-`concurrent.futures` לשלבי סוכן עצמאיים |  

#### דוגמה לרשומת מעקב

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```
  

#### הנחיית הערכה פשוטה

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```
  
שמרו זוגות (`answer`, `rating`) לבניית גרף איכות היסטורי.  

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.