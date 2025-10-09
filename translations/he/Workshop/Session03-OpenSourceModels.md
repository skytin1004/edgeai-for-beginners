<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-09T16:53:06+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "he"
}
-->
# מפגש 3: מודלים בקוד פתוח ב-Foundry Local

## תקציר

גלו כיצד לשלב מודלים של Hugging Face ומודלים בקוד פתוח אחרים ב-Foundry Local. למדו אסטרטגיות בחירה, תהליכי תרומה לקהילה, מתודולוגיית השוואת ביצועים, וכיצד להרחיב את Foundry עם רישום מודלים מותאמים אישית. מפגש זה משתלב עם נושאי החקר השבועיים של "Model Mondays" ומספק כלים להערכה ולהפעלה של מודלים בקוד פתוח באופן מקומי לפני מעבר להרחבה ב-Azure.

## מטרות למידה

בסיום המפגש תוכלו:

- **לגלות ולהעריך**: לזהות מודלים מועמדים (mistral, gemma, qwen, deepseek) תוך שקלול איכות מול משאבים.
- **לטעון ולהפעיל**: להשתמש ב-Foundry Local CLI להורדה, שמירה והפעלה של מודלים מהקהילה.
- **למדוד ביצועים**: ליישם מדדים עקביים של זמן תגובה + קצב עיבוד טוקנים + איכות.
- **להרחיב**: לרשום או להתאים מעטפת מודל מותאמת אישית בהתאם לדפוסים תואמי SDK.
- **להשוות**: ליצור השוואות מובנות לבחירת SLM מול מודלים בגודל בינוני.

## דרישות מקדימות

- השלמת מפגשים 1 ו-2
- סביבת Python עם `foundry-local-sdk` מותקן
- לפחות 15GB פנויים בדיסק עבור שמירת מודלים מרובים
- אופציונלי: האצת GPU/WebGPU מופעלת (`foundry config list`)

### התחלה מהירה בסביבה חוצת פלטפורמות

Windows PowerShell:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
macOS / Linux:  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
בעת מדידת ביצועים מ-macOS מול שירות מארח ב-Windows, הגדירו:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## זרימת הדגמה (30 דקות)

### 1. טעינת מודלים של Hugging Face דרך CLI (8 דקות)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```
  

### 2. הפעלה ובדיקה מהירה (5 דקות)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  

### 3. סקריפט מדידת ביצועים (8 דקות)

צרו `samples/03-oss-models/benchmark_models.py`:  
```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```
  
הפעילו:  
```powershell
python samples/03-oss-models/benchmark_models.py
```
  

### 4. השוואת ביצועים (5 דקות)

דונו בשיקולים: זמן טעינה, צריכת זיכרון (צפו ב-Task Manager / `nvidia-smi` / מוניטור משאבי מערכת), איכות הפלט מול מהירות. השתמשו בסקריפט מדידת הביצועים (מפגש 3) עבור זמן תגובה וקצב עיבוד; חזרו על המדידה לאחר הפעלת האצת GPU.

### 5. פרויקט התחלתי (4 דקות)

צרו מחולל דוחות השוואת מודלים (הרחיבו את סקריפט מדידת הביצועים עם ייצוא Markdown).

## פרויקט התחלתי: הרחבת `03-huggingface-models`

שפרו את הדוגמה הקיימת על ידי:

1. הוספת איגוד מדדי ביצועים + ייצוא CSV/Markdown.
2. יישום דירוג איכות פשוט (סט זוגות הנחיות + קובץ הערות ידני).
3. הכנסת קובץ JSON (`models.json`) לרשימת מודלים ניתנת להתאמה וסט הנחיות.

## רשימת בדיקה לאימות

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
כל המודלים המיועדים צריכים להופיע ולהגיב לבקשת צ'אט בדיקה.

## תרחיש לדוגמה ומיפוי לסדנה

| סקריפט סדנה | תרחיש | מטרה | מקור הנחיות / מערך נתונים |
|-------------|--------|------|--------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | צוות פלטפורמת קצה הבוחר SLM ברירת מחדל עבור מסכם מוטמע | הפקת השוואה של זמן תגובה + p95 + טוקנים לשנייה בין מודלים מועמדים | משתנה `PROMPT` פנימי + רשימת `BENCH_MODELS` בסביבה |

### נרטיב תרחיש
צוות הנדסת מוצר חייב לבחור מודל סיכום קל משקל ברירת מחדל עבור תכונת סיכום הערות פגישות לא מקוונת. הם מבצעים מדידות ביצועים מבוקרות ודטרמיניסטיות (temperature=0) על סט הנחיות קבוע (ראו דוגמה למטה) ואוספים מדדי זמן תגובה + קצב עיבוד עם ובלי האצת GPU.

### דוגמת סט הנחיות JSON (ניתן להרחבה)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
חזרו על כל הנחיה עבור כל מודל, אספו זמן תגובה לכל הנחיה כדי לגזור מדדי התפלגות ולזהות חריגות.

## מסגרת לבחירת מודלים

| ממד | מדד | חשיבות |
|-----|-----|--------|
| זמן תגובה | ממוצע / p95 | עקביות חוויית משתמש |
| קצב עיבוד | טוקנים לשנייה | יכולת הרחבה באצווה ובזרימה |
| זיכרון | גודל תושב | התאמה למכשיר ותחרותיות |
| איכות | הנחיות מדד | התאמה למשימה |
| טביעת רגל | שמירת דיסק | הפצה ועדכונים |
| רישיון | הרשאת שימוש | תאימות מסחרית |

## הרחבה עם מודל מותאם אישית

דפוס ברמה גבוהה (פסאודו):  
```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```
  
עיינו במאגר הרשמי עבור ממשקי מתאמים מתפתחים:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  

## פתרון בעיות

| בעיה | סיבה | פתרון |
|------|------|-------|
| OOM על mistral-7b | זיכרון RAM/GPU לא מספיק | עצרו מודלים אחרים; נסו גרסה קטנה יותר |
| תגובה ראשונה איטית | טעינה קרה | שמרו על חימום עם הנחיה קלה תקופתית |
| הורדה נתקעת | אי יציבות רשת | נסו שוב; הורידו מראש בשעות שפל |

## מקורות

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Model Mondays: https://aka.ms/model-mondays  
- גילוי מודלים של Hugging Face: https://huggingface.co/models  

---

**משך המפגש**: 30 דקות (+ צלילה מעמיקה אופציונלית)  
**רמת קושי**: בינונית  

### שיפורים אופציונליים

| שיפור | יתרון | כיצד |
|-------|-------|------|
| זמן תגובה לטוקן ראשון בזרימה | מדידת תגובתיות נתפסת | הריצו מדידה עם `BENCH_STREAM=1` (סקריפט משופר ב-`Workshop/samples/session03`) |
| מצב דטרמיניסטי | השוואות יציבות ברגרסיה | `temperature=0`, סט הנחיות קבוע, שמרו פלטי JSON תחת בקרת גרסאות |
| דירוג איכות מדד | מוסיף ממד איכותי | תחזקו `prompts.json` עם מאפיינים צפויים; דרגו ציונים (1–5) ידנית או באמצעות מודל משני |
| ייצוא CSV / Markdown | דוח ניתן לשיתוף | הרחיבו את הסקריפט לכתיבת `benchmark_report.md` עם טבלה והדגשות |
| תגי יכולות מודל | מסייע בניתוב אוטומטי מאוחר יותר | תחזקו `models.json` עם `{alias: {capabilities:[], size_mb:..}}` |
| שלב חימום מטמון | הפחתת הטיה של טעינה קרה | בצעו סבב חימום אחד לפני לולאת המדידה (כבר מיושם) |
| דיוק אחוזון | זמן תגובה חזק בקצה | השתמשו ב-numpy אחוזון (כבר בסקריפט שעבר שינוי) |
| הערכת עלות טוקן | השוואה כלכלית | עלות משוערת = (טוקנים לשנייה * ממוצע טוקנים לבקשה) * מדד אנרגיה |
| דילוג אוטומטי על מודלים שנכשלו | עמידות בהרצות אצווה | עטפו כל מדידה ב-try/except וסמנו שדה סטטוס |

#### קטע ייצוא Markdown מינימלי

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  

#### דוגמת סט הנחיות דטרמיניסטי

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
חזרו על הרשימה הסטטית במקום הנחיות אקראיות עבור מדדים השוואתיים בין גרסאות.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.