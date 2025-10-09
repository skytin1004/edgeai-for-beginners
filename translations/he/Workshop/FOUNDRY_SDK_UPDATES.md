<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T16:38:19+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "he"
}
-->
# עדכונים ל-SDK המקומי של Foundry

## סקירה כללית

עודכנו מחברות ה-Workshop והכלים כך שישתמשו בצורה נכונה ב-**SDK המקומי הרשמי של Foundry עבור Python**, בהתאם לדפוסים מ:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## קבצים שעודכנו

### 1. `Workshop/samples/workshop_utils.py`

**שינויים:**
- ✅ נוספה טיפול בשגיאות ייבוא עבור חבילת `foundry-local-sdk`
- ✅ שופרה התיעוד עם דפוסים רשמיים של ה-SDK
- ✅ שופרה הלוגים עם סמלים יוניקוד (✓, ✗, ⚠)
- ✅ נוספו docstrings מקיפים עם דוגמאות
- ✅ שופרו הודעות שגיאה עם הפניות לפקודות CLI
- ✅ עודכנו הערות כך שיתאימו לתיעוד הרשמי של ה-SDK

**שיפורים מרכזיים:**

#### טיפול בשגיאות ייבוא
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### שיפור פונקציית `get_client()`
- נוספה תיעוד מפורטת על דפוסי האתחול של ה-SDK
- הובהר ש-`FoundryLocalManager` מפעיל את השירות באופן אוטומטי
- הוסבר פתרון שמות מודלים לגרסאות מותאמות חומרה
- שופרה הלוגים עם מידע על נקודות קצה
- הודעות שגיאה טובות יותר עם הצעות לפתרון בעיות

#### שיפור פונקציית `chat_once()`
- נוספה docstring מקיפה עם דוגמאות שימוש
- הובהרה תאימות ל-SDK של OpenAI
- תועד תמיכה בזרימה (באמצעות kwargs)
- שופרו הודעות שגיאה עם הצעות לפקודות CLI
- נוספו הערות על בדיקת זמינות מודלים

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**שינויים:**
- ✅ עודכנו כל תאי ה-Markdown עם הפניות ל-SDK
- ✅ שופרו הערות קוד עם הסברים על דפוסי SDK
- ✅ שופרה תיעוד התאים וההסברים
- ✅ נוספה הדרכה לפתרון בעיות
- ✅ עודכן קטלוג המודלים (הוחלף 'gpt-oss-20b' ב-'phi-3.5-mini')
- ✅ שופרה פורמט הפלט עם אינדיקטורים חזותיים
- ✅ נוספו קישורים והפניות ל-SDK לאורך כל המחברת

**עדכונים תא-אחר-תא:**

#### תא 1 (כותרת)
- נוספו קישורים לתיעוד ה-SDK
- הוזכרו מאגרי GitHub רשמיים

#### תא 2 (תרחיש)
- עוצב מחדש עם שלבים ממוספרים
- הובהר דפוס ניתוב מבוסס כוונה
- הודגשו יתרונות הביצוע המקומי

#### תא 3 (התקנת תלות)
- נוספו הסברים על מה כל חבילה מספקת
- תועדו יכולות ה-SDK (פתרון שמות, אופטימיזציה חומרה)

#### תא 4 (הגדרת סביבה)
- שופרו docstrings של פונקציות
- נוספו הערות inline שמסבירות דפוסי SDK
- תועד מבנה קטלוג המודלים
- הובהרה התאמת עדיפות/יכולת

#### תא 5 (בדיקת קטלוג)
- נוספו סימני בדיקה חזותיים (✓)
- פורמט הפלט שופר

#### תא 6 (בדיקת זיהוי כוונה)
- עוצב מחדש כטבלה
- מציג גם כוונה וגם מודל שנבחר

#### תא 7 (פונקציית ניתוב)
- הסבר מקיף על דפוסי SDK
- תועד זרימת האתחול
- נרשמו כל התכונות (ניסיון חוזר, מעקב, שגיאות)
- נוספה הפניה ל-SDK

#### תא 8 (דמו קבוצתי)
- שופרו ההסברים על מה לצפות
- נוספה סעיף פתרון בעיות
- נכללו פקודות CLI לאיתור באגים
- פורמט הפלט שופר

### 3. `Workshop/notebooks/session06_README.md` (קובץ חדש)

**נוצרה תיעוד מקיף המכסה:**

1. **סקירה כללית**: דיאגרמת ארכיטקטורה והסבר רכיבים
2. **אינטגרציית SDK**: דוגמאות קוד בהתאם לדפוסים רשמיים
3. **דרישות מוקדמות**: הוראות הגדרה שלב-אחר-שלב
4. **שימוש**: איך להריץ ולהתאים את המחברת
5. **שמות מודלים**: הסבר על גרסאות מותאמות חומרה
6. **פתרון בעיות**: בעיות נפוצות ופתרונות
7. **הרחבה**: איך להוסיף כוונות, מודלים ולוגיקה מותאמת אישית
8. **טיפים לביצועים**: שיטות עבודה מומלצות לשימוש בייצור
9. **משאבים**: קישורים לתיעוד רשמי וקהילה

## יישום דפוסי SDK

### דפוס רשמי (מתוך תיעוד Foundry Local)

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

### היישום שלנו (ב-workshop_utils)

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

**יתרונות הגישה שלנו:**
- ✅ עוקב בדיוק אחרי דפוסי SDK רשמיים
- ✅ מוסיף caching למניעת אתחול חוזר
- ✅ כולל לוגיקת ניסיון חוזר ליציבות בייצור
- ✅ תומך במעקב אחר שימוש בטוקנים
- ✅ מספק הודעות שגיאה טובות יותר
- ✅ נשאר תואם לדוגמאות רשמיות

## שינויים בקטלוג המודלים

### לפני
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### אחרי
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**סיבה:** הוחלף 'gpt-oss-20b' (שם לא סטנדרטי) ב-'phi-3.5-mini' (שם רשמי של Foundry Local).

## תלות

### קובץ requirements.txt מעודכן

קובץ requirements.txt של ה-Workshop כבר כולל:
```
foundry-local-sdk
openai>=1.30.0
```

אלו החבילות היחידות הנדרשות לאינטגרציה עם Foundry Local.

## בדיקת העדכונים

### 1. ודא ש-Foundry Local פועל

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. בדוק מודלים זמינים

```bash
foundry model ls
```

ודא שהמודלים הבאים זמינים או יורדו אוטומטית:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. הרץ את המחברת

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

או פתח ב-VS Code והרץ את כל התאים.

### 4. התנהגות צפויה

**תא 1 (התקנה):** מתקין חבילות בהצלחה  
**תא 2 (הגדרה):** אין שגיאות, ייבוא עובד  
**תא 3 (אימות):** מציג ✓ עם רשימת מודלים  
**תא 4 (בדיקת כוונה):** מציג תוצאות זיהוי כוונה  
**תא 5 (נתב):** מציג ✓ פונקציית ניתוב מוכנה  
**תא 6 (ביצוע):** מנתב פקודות למודלים, מציג תוצאות  

### 5. פתרון בעיות חיבור

אם מופיעה שגיאה `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## משתני סביבה

משתני הסביבה הבאים נתמכים:

| משתנה | ברירת מחדל | תיאור |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | הגדר ל-`1` כדי להדפיס שימוש בטוקנים |
| `RETRY_ON_FAIL` | `1` | הפעל לוגיקת ניסיון חוזר |
| `RETRY_BACKOFF` | `1.0` | עיכוב ניסיון חוזר ראשוני (שניות) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | עקוף נקודת קצה שירות |

### דוגמאות שימוש

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## מעבר מדפוס ישן

אם יש לך קוד קיים שמשתמש בקריאות API ישירות, כך תוכל לעבור:

### לפני (API ישיר)
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

### אחרי (SDK)
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

### יתרונות המעבר
- ✅ ניהול שירות אוטומטי
- ✅ פתרון שמות מודלים
- ✅ בחירת אופטימיזציה חומרה
- ✅ טיפול שגיאות טוב יותר
- ✅ תאימות ל-SDK של OpenAI
- ✅ תמיכה בזרימה

## הפניות

### תיעוד רשמי
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **מקור SDK עבור Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **הפניה CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **API REST**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **פתרון בעיות**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### משאבי Workshop
- **README של Session 06**: `Workshop/notebooks/session06_README.md`
- **כלי Workshop**: `Workshop/samples/workshop_utils.py`
- **מחברת לדוגמה**: `Workshop/notebooks/session06_models_router.ipynb`

### קהילה
- **Discord**: https://aka.ms/foundry-local-discord
- **בעיות GitHub**: https://github.com/microsoft/Foundry-Local/issues

## צעדים הבאים

1. **סקור שינויים**: קרא את הקבצים המעודכנים  
2. **בדוק מחברת**: הרץ את session06_models_router.ipynb  
3. **אמת SDK**: ודא ש-foundry-local-sdk מותקן  
4. **בדוק שירות**: אשר ש-Foundry Local פועל  
5. **חקור תיעוד**: קרא את session06_README.md החדש  

## סיכום

עדכונים אלו מבטיחים שחומרי ה-Workshop עוקבים אחרי **דפוסי SDK המקומי הרשמי של Foundry** בדיוק כפי שמתועד במאגר GitHub. כל דוגמאות הקוד, התיעוד והכלים כעת מתאימים לשיטות העבודה המומלצות של Microsoft לפריסת מודלים AI מקומיים.

השינויים משפרים:
- ✅ **דיוק**: שימוש בדפוסי SDK רשמיים  
- ✅ **תיעוד**: הסברים ודוגמאות מקיפים  
- ✅ **טיפול שגיאות**: הודעות טובות יותר והדרכה לפתרון בעיות  
- ✅ **תחזוקה**: עוקב אחרי מוסכמות רשמיות  
- ✅ **חוויית משתמש**: הוראות ברורות ועזרה באיתור באגים  

---

**עודכן:** 8 באוקטובר, 2025  
**גרסת SDK:** foundry-local-sdk (עדכנית)  
**ענף Workshop:** Reactor

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.