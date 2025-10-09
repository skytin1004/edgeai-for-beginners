<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-09T16:39:29+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "he"
}
-->
# מדריך התחלה מהירה לסדנה

## דרישות מקדימות

### 1. התקנת Foundry Local

עקוב אחר מדריך ההתקנה הרשמי:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. התקנת תלותים ב-Python

מתוך ספריית הסדנה:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## הפעלת דוגמאות מהסדנה

### מפגש 01: צ'אט בסיסי

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**משתני סביבה:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### מפגש 02: צינור RAG

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**משתני סביבה:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### מפגש 02: הערכת RAG (Ragas)

```bash
python rag_eval_ragas.py
```

**הערה**: דורש התקנת תלותים נוספים דרך `requirements.txt`

### מפגש 03: ביצועי מערכת

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**משתני סביבה:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**פלט**: JSON עם נתוני זמן תגובה, תפוקה ומדדי טוקן ראשון

### מפגש 04: השוואת מודלים

```bash
cd Workshop/samples/session04
python model_compare.py
```

**משתני סביבה:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### מפגש 05: תזמור רב-סוכנים

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**משתני סביבה:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### מפגש 06: ניתוב מודלים

```bash
cd Workshop/samples/session06
python models_router.py
```

**בודק לוגיקת ניתוב** עם מספר כוונות (קוד, סיכום, סיווג)

### מפגש 06: צינור עבודה

```bash
python models_pipeline.py
```

**צינור עבודה מורכב רב-שלבי** עם תכנון, ביצוע ושיפור

## סקריפטים

### ייצוא דוח ביצועים

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**פלט**: טבלת Markdown + נתוני JSON

### בדיקת CLI בתיעוד Markdown

```bash
python lint_markdown_cli.py --verbose
```

**מטרה**: זיהוי תבניות CLI מיושנות בתיעוד

## בדיקות

### בדיקות בסיסיות

```bash
cd Workshop
python -m tests.smoke
```

**בדיקות**: פונקציונליות בסיסית של דוגמאות מרכזיות

## פתרון בעיות

### שירות לא פעיל

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### שגיאות ייבוא מודולים

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### שגיאות חיבור

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### מודל לא נמצא

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## הפניה למשתני סביבה

### הגדרות ליבה
| משתנה | ברירת מחדל | תיאור |
|-------|------------|-------|
| `FOUNDRY_LOCAL_ALIAS` | משתנה | כינוי מודל לשימוש |
| `FOUNDRY_LOCAL_ENDPOINT` | אוטומטי | עקיפת נקודת שירות |
| `SHOW_USAGE` | `0` | הצגת סטטיסטיקות שימוש בטוקנים |
| `RETRY_ON_FAIL` | `1` | הפעלת לוגיקת ניסיון חוזר |
| `RETRY_BACKOFF` | `1.0` | עיכוב ראשוני לניסיון חוזר (שניות) |

### מפגש ספציפי
| משתנה | ברירת מחדל | תיאור |
|-------|------------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | מודל הטמעה |
| `RAG_QUESTION` | ראה דוגמה | שאלה לבדיקה ב-RAG |
| `BENCH_MODELS` | משתנה | מודלים מופרדים בפסיקים |
| `BENCH_ROUNDS` | `3` | מספר סבבי ביצועים |
| `BENCH_PROMPT` | ראה דוגמה | הנחיה לביצועים |
| `BENCH_STREAM` | `0` | מדידת זמן תגובה לטוקן ראשון |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | מודל סוכן ראשי |
| `AGENT_MODEL_EDITOR` | ראשי | מודל סוכן עורך |
| `SLM_ALIAS` | `phi-4-mini` | מודל שפה קטן |
| `LLM_ALIAS` | `qwen2.5-7b` | מודל שפה גדול |
| `COMPARE_PROMPT` | ראה דוגמה | הנחיה להשוואה |

## מודלים מומלצים

### פיתוח ובדיקות
- **phi-4-mini** - איזון בין איכות למהירות
- **qwen2.5-0.5b** - מהיר מאוד לסיווג
- **gemma-2-2b** - איכות טובה, מהירות בינונית

### תרחישי ייצור
- **phi-4-mini** - שימוש כללי
- **deepseek-coder-1.3b** - יצירת קוד
- **qwen2.5-7b** - תגובות באיכות גבוהה

## תיעוד SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## קבלת עזרה

1. בדוק מצב שירות: `foundry service status`  
2. צפה ביומנים: בדוק יומני שירות Foundry Local  
3. עיין בתיעוד SDK: https://github.com/microsoft/Foundry-Local  
4. עיין בקוד דוגמאות: כל הדוגמאות כוללות הערות מפורטות

## צעדים הבאים

1. השלם את כל מפגשי הסדנה לפי הסדר  
2. נסה מודלים שונים  
3. שנה דוגמאות לצרכים שלך  
4. עיין ב-`SDK_MIGRATION_NOTES.md` לדפוסים מתקדמים  

---

**עודכן לאחרונה**: 2025-01-08  
**גרסת סדנה**: אחרונה  
**SDK**: Foundry Local Python SDK  

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.