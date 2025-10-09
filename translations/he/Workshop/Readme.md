<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "48d0fb38be925084a6ebd957d4b045e5",
  "translation_date": "2025-10-09T16:49:48+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "he"
}
-->
# EdgeAI למתחילים - סדנה

> **מסלול למידה מעשי לבניית יישומי Edge AI מוכנים לייצור**
>
> שלוט בפריסת AI מקומית עם Microsoft Foundry Local, החל מהשלמת שיחה ראשונה ועד לתזמור רב-סוכנים ב-6 מפגשים מתקדמים.

---

## 🎯 מבוא

ברוכים הבאים ל**סדנת EdgeAI למתחילים** - המדריך המעשי שלכם לבניית יישומים חכמים שפועלים לחלוטין על חומרה מקומית. הסדנה הזו הופכת את התיאוריה של Edge AI לכישורים מעשיים באמצעות תרגילים מאתגרים בהדרגה, תוך שימוש ב-Microsoft Foundry Local ובמודלים שפתיים קטנים (SLMs).

### למה הסדנה הזו?

**מהפכת Edge AI כבר כאן**

ארגונים ברחבי העולם עוברים מ-AI תלוי ענן למחשוב קצה בשלושה סיבות קריטיות:

1. **פרטיות וציות** - עיבוד נתונים רגישים באופן מקומי ללא העברה לענן (HIPAA, GDPR, תקנות פיננסיות)
2. **ביצועים** - ביטול השהיית רשת (50-500ms מקומי לעומת 500-2000ms סבב ענן)
3. **שליטה בעלויות** - הסרת עלויות API לפי טוקן והרחבה ללא הוצאות ענן

**אבל Edge AI שונה**

הרצת AI באופן מקומי דורשת כישורים חדשים:
- בחירת מודלים ואופטימיזציה למגבלות משאבים
- ניהול שירותים מקומיים והאצת חומרה
- הנדסת הנחיות למודלים קטנים יותר
- דפוסי פריסה לייצור במכשירי קצה

**הסדנה הזו מספקת את הכישורים הללו**

ב-6 מפגשים ממוקדים (כ-3 שעות בסך הכל), תתקדמו מ-"Hello World" לפריסת מערכות רב-סוכנים מוכנות לייצור - הכל פועל באופן מקומי על המחשב שלכם.

---

## 📚 מטרות למידה

עם סיום הסדנה, תוכלו:

### מיומנויות ליבה
1. **לפרוס ולנהל שירותי AI מקומיים**
   - התקנה וקונפיגורציה של Microsoft Foundry Local
   - בחירת מודלים מתאימים לפריסת קצה
   - ניהול מחזור חיים של מודלים (הורדה, טעינה, שמירה במטמון)
   - ניטור שימוש במשאבים ואופטימיזציה לביצועים

2. **לבנות יישומים מבוססי AI**
   - יישום השלמות שיחה תואמות OpenAI באופן מקומי
   - עיצוב הנחיות אפקטיביות למודלים שפתיים קטנים
   - טיפול בתגובות זורמות לשיפור חוויית המשתמש
   - שילוב מודלים מקומיים ביישומים קיימים

3. **ליצור מערכות RAG (הפקת תשובות מבוססת חיפוש)**
   - בניית חיפוש סמנטי עם הטמעות
   - עיגון תשובות LLM בידע ספציפי לתחום
   - הערכת איכות RAG עם מדדים סטנדרטיים בתעשייה
   - הרחבה מפרוטוטיפ לייצור

4. **לאופטימיזציה של ביצועי מודלים**
   - ביצוע בדיקות למודלים שונים עבור המקרה שלכם
   - מדידת השהייה, תפוקה וזמן טוקן ראשון
   - בחירת מודלים אופטימליים על בסיס איזון מהירות/איכות
   - השוואת SLM לעומת LLM בתרחישים אמיתיים

5. **לתזמר מערכות רב-סוכנים**
   - עיצוב סוכנים מיוחדים למשימות שונות
   - יישום זיכרון סוכן וניהול הקשר
   - תיאום סוכנים בתהליכים מורכבים
   - ניתוב בקשות בצורה חכמה בין מודלים שונים

6. **לפרוס פתרונות מוכנים לייצור**
   - יישום טיפול בשגיאות ולוגיקת ניסיונות חוזרים
   - ניטור שימוש בטוקנים ומשאבי מערכת
   - בניית ארכיטקטורות ניתנות להרחבה עם דפוסי מודלים ככלים
   - תכנון מסלולי מעבר מקצה להיברידי (קצה + ענן)

---

## 🎓 תוצאות למידה

### מה תבנו

בסיום הסדנה, תיצרו:

| מפגש | תוצר | מיומנויות שהודגמו |
|------|-------|--------------------|
| **1** | יישום צ'אט עם תגובות זורמות | הגדרת שירות, השלמות בסיסיות, חוויית משתמש זורמת |
| **2** | מערכת RAG עם הערכה | הטמעות, חיפוש סמנטי, מדדי איכות |
| **3** | סוויטת בדיקות למודלים מרובים | מדידת ביצועים, השוואת מודלים |
| **4** | משווה SLM לעומת LLM | ניתוח איזונים, אסטרטגיות אופטימיזציה |
| **5** | מתזמר רב-סוכנים | עיצוב סוכנים, ניהול זיכרון, תיאום |
| **6** | מערכת ניתוב חכמה | זיהוי כוונה, בחירת מודלים, יכולת הרחבה |

### מטריצת מיומנויות

| רמת מיומנות | מפגש 1-2 | מפגש 3-4 | מפגש 5-6 |
|-------------|----------|----------|----------|
| **מתחילים** | ✅ הגדרה ובסיס | ⚠️ מאתגר | ❌ מתקדם מדי |
| **בינוניים** | ✅ סקירה מהירה | ✅ למידה עיקרית | ⚠️ מטרות מתקדמות |
| **מתקדמים** | ✅ קל ומהיר | ✅ שיפור | ✅ דפוסי ייצור |

### מיומנויות מוכנות לקריירה

**לאחר הסדנה, תהיו מוכנים:**

✅ **לבנות יישומים מבוססי פרטיות**
- אפליקציות בריאות המטפלות ב-PHI/PII באופן מקומי
- שירותים פיננסיים עם דרישות ציות
- מערכות ממשלתיות עם דרישות ריבונות נתונים

✅ **לאופטימיזציה לסביבות קצה**
- מכשירי IoT עם משאבים מוגבלים
- אפליקציות מובייל עם גישה ראשונית לא מקוונת
- מערכות בזמן אמת עם השהייה נמוכה

✅ **לעצב ארכיטקטורות חכמות**
- מערכות רב-סוכנים לתהליכים מורכבים
- פריסות היברידיות קצה-ענן
- תשתיות AI אופטימליות מבחינת עלות

✅ **להוביל יוזמות Edge AI**
- להעריך את היתכנות Edge AI לפרויקטים
- לבחור מודלים ומסגרות מתאימים
- לתכנן פתרונות AI מקומיים ניתנים להרחבה

---

## 🗺️ מבנה הסדנה

### סקירת מפגשים (6 מפגשים × 30 דקות = 3 שעות)

| מפגש | נושא | מיקוד | משך |
|------|------|-------|------|
| **1** | התחלה עם Foundry Local | התקנה, אימות, השלמות ראשונות | 30 דקות |
| **2** | בניית פתרונות AI עם RAG | הנדסת הנחיות, הטמעות, הערכה | 30 דקות |
| **3** | מודלים בקוד פתוח | גילוי מודלים, בדיקות, בחירה | 30 דקות |
| **4** | מודלים מתקדמים | SLM לעומת LLM, אופטימיזציה, מסגרות | 30 דקות |
| **5** | סוכנים מבוססי AI | עיצוב סוכנים, תזמור, זיכרון | 30 דקות |
| **6** | מודלים ככלים | ניתוב, שרשור, אסטרטגיות הרחבה | 30 דקות |

---

## 🚀 התחלה מהירה

### דרישות מוקדמות

**דרישות מערכת:**
- **מערכת הפעלה**: Windows 10/11, macOS 11+, או Linux (Ubuntu 20.04+)
- **RAM**: מינימום 8GB, מומלץ 16GB+
- **אחסון**: לפחות 10GB פנויים למודלים
- **מעבד**: מעבד מודרני עם תמיכה ב-AVX2
- **GPU** (אופציונלי): תואם CUDA או Qualcomm NPU להאצה

**דרישות תוכנה:**
- **Python 3.8+** ([הורדה](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([מדריך התקנה](../../../Workshop))
- **Git** ([הורדה](https://git-scm.com/downloads))
- **Visual Studio Code** (מומלץ) ([הורדה](https://code.visualstudio.com/))

### הגדרה ב-3 שלבים

#### 1. התקנת Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**אימות התקנה:**
```bash
foundry --version
foundry service status
```

#### 2. שיבוט מאגר והתקנת תלותים

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. הרצת דוגמה ראשונה

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ הצלחה!** אתם אמורים לראות תגובה זורמת על Edge AI.

---

## 📦 משאבי הסדנה

### דוגמאות Python

דוגמאות מעשיות מדורגות המדגימות כל מושג:

| מפגש | דוגמה | תיאור | זמן ריצה |
|------|-------|-------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | צ'אט בסיסי וזורם | ~30 שניות |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG עם הטמעות | ~45 שניות |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | הערכת איכות RAG | ~60 שניות |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | בדיקות למודלים מרובים | ~2-3 דקות |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | השוואת SLM לעומת LLM | ~45 שניות |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | מערכת רב-סוכנים | ~60 שניות |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | ניתוב מבוסס כוונה | ~45 שניות |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | צינור רב-שלבי | ~60 שניות |

### מחברות Jupyter

חקירה אינטראקטיבית עם הסברים והדמיות:

| מפגש | מחברת | תיאור | רמת קושי |
|------|-------|-------|----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | יסודות צ'אט וזרימה | ⭐ מתחילים |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | בניית מערכת RAG | ⭐⭐ בינוניים |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | הערכת איכות RAG | ⭐⭐ בינוניים |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | בדיקות מודלים | ⭐⭐ בינוניים |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | השוואת מודלים | ⭐⭐ בינוניים |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | תזמור סוכנים | ⭐⭐⭐ מתקדמים |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | ניתוב כוונה | ⭐⭐⭐ מתקדמים |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | תזמור צינור | ⭐⭐⭐ מתקדמים |

### תיעוד

מדריכים ועמודי עזר מקיפים:

| מסמך | תיאור | מתי להשתמש |
|------|-------|------------|
| [QUICK_START.md](./QUICK_START.md) | מדריך הגדרה מהיר | התחלה מאפס |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | דף עזר לפקודות ו-API | צריך תשובות מהירות |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | דפוסי SDK ודוגמאות | כתיבת קוד |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | מדריך משתני סביבה | קונפיגורציה לדוגמאות |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | שיפורים אחרונים בדוגמאות | הבנת שינויים |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | מדריך מעבר | שדרוג קוד |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | בעיות נפוצות ותיקונים | פתרון בעיות |

---

## 🎓 המלצות למסלול למידה

### למתחילים (3-4 שעות)
1. ✅ מפגש 1: התחלה (מיקוד בהגדרה וצ'אט בסיסי)
2. ✅ מפגש 2: יסודות RAG (דלגו על הערכה בהתחלה)
3. ✅ מפגש 3: בדיקות פשוטות (רק 2 מודלים)
4. ⏭️ דלגו על מפגשים 4-6 לעת עתה
5. 🔄 חזרו למפגשים 4-6 לאחר בניית יישום ראשון

### למפתחים בינוניים (3 שעות)
1. ⚡ מפגש 1: אימות הגדרה מהיר
2. ✅ מפגש 2: מערכת RAG מלאה עם הערכה
3. ✅ מפגש 3: סוויטת בדיקות מלאה
4. ✅ מפגש 4: אופטימיזציה למודלים
5. ✅ מפגשים 5-6: מיקוד בדפוסי ארכיטקטורה

### למשתמשים מתקדמים (2-3 שעות)
1. ⚡ מפגשים 1-3: סקירה מהירה ואימות
2. ✅ מפגש 4: צלילה עמוקה לאופטימיזציה
3. ✅ מפגש 5: ארכיטקטורה רב-סוכנים
4. ✅ מפגש 6: דפוסי ייצור והרחבה
5. 🚀 הרחבה: בניית לוגיקת ניתוב מותאמת ופריסות היברידיות

---

## חבילת מפגשי סדנה (מעבדות ממוקדות של 30 דקות)

אם אתם עוקבים אחרי פורמט הסדנה המכווץ של 6 מפגשים, השתמשו במדריכים ייעודיים אלו (כל אחד מתאים ומשלים את מסמכי המודול הרחבים לעיל):

| מפגש סדנה | מדריך | מיקוד עיקרי |
|-----------|-------|------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | התקנה, אימות, הרצת phi & GPT-OSS-20B, האצה |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | הנדסת הנחיות, דפוסי RAG, עיגון CSV ומסמכים, מעבר |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | אינטגרציה עם Hugging Face, בדיקות, בחירת מודלים |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM לעומת LLM, WebGPU, Chainlit RAG, האצת ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | תפקידי סוכנים, זיכרון, כלים, תזמור |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | ניתוב, שרשור, מסלול הרחבה ל-Azure |
כל קובץ מפגש כולל: תקציר, מטרות למידה, זרימת הדגמה של 30 דקות, פרויקט התחלתי, רשימת בדיקות אימות, פתרון בעיות והפניות ל-SDK הרשמי של Foundry Local Python.

### סקריפטים לדוגמה

התקנת תלותים לסדנה (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

אם מפעילים את שירות Foundry Local במחשב או VM שונה (Windows) מ-macOS, יש לייצא את נקודת הקצה:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| מפגש | סקריפט(ים) | תיאור |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | שירות Bootstrap וצ'אט זורם |
| 2 | `samples/session02/rag_pipeline.py` | RAG מינימלי (הטמעות בזיכרון) |
|   | `samples/session02/rag_eval_ragas.py` | הערכת RAG עם מדדי ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | בדיקת ביצועים של עיכוב ותפוקה למודלים מרובים |
| 4 | `samples/session04/model_compare.py` | השוואת SLM מול LLM (עיכוב ותוצאות דוגמה) |
| 5 | `samples/session05/agents_orchestrator.py` | צנרת מחקר → עריכה עם שני סוכנים |
| 6 | `samples/session06/models_router.py` | הדגמת ניתוב מבוסס כוונה |
|   | `samples/session06/models_pipeline.py` | שרשרת תכנון/ביצוע/שיפור מרובת שלבים |

### משתני סביבה (משותפים לכל הדוגמאות)

| משתנה | מטרה | דוגמה |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | כינוי ברירת מחדל למודל יחיד לדוגמאות בסיסיות | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | מודל SLM מפורש מול מודל גדול יותר להשוואה | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | רשימת כינויים לבדיקת ביצועים | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | חזרות בדיקת ביצועים לכל מודל | `3` |
| `BENCH_PROMPT` | הנחיה המשמשת בבדיקת ביצועים | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | מודל הטמעות של sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | החלפת שאלה לבדיקה בצנרת RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | החלפת שאלה בצנרת הסוכנים | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | כינוי מודל לסוכן מחקר | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | כינוי מודל לסוכן עריכה (יכול להיות שונה) | `gpt-oss-20b` |
| `SHOW_USAGE` | כאשר `1`, מציג שימוש בטוקנים לכל השלמה | `1` |
| `RETRY_ON_FAIL` | כאשר `1`, מנסה שוב במקרה של שגיאות צ'אט זמניות | `1` |
| `RETRY_BACKOFF` | שניות להמתנה לפני ניסיון חוזר | `1.0` |

אם משתנה לא מוגדר, הסקריפטים יחזרו לערכי ברירת מחדל הגיוניים. לדוגמאות עם מודל יחיד, בדרך כלל צריך רק את `FOUNDRY_LOCAL_ALIAS`.

### מודול עזר

כל הדוגמאות כעת חולקות את `samples/workshop_utils.py`, המספק:

* יצירת `FoundryLocalManager` + לקוח OpenAI עם מטמון
* פונקציית עזר `chat_once()` עם ניסיון חוזר אופציונלי + הדפסת שימוש
* דיווח פשוט על שימוש בטוקנים (ניתן להפעיל באמצעות `SHOW_USAGE=1`)

זה מפחית כפילויות ומדגיש שיטות עבודה מומלצות לאורקסטרציה יעילה של מודלים מקומיים.

## שיפורים אופציונליים (בין מפגשים)

| נושא | שיפור | מפגשים | סביבה / מתג |
|-------|-------------|----------|--------------|
| דטרמיניזם | טמפרטורה קבועה + סטים יציבים של הנחיות | 1–6 | הגדר `temperature=0`, `top_p=1` |
| נראות שימוש בטוקנים | הוראת עלות/יעילות עקבית | 1–6 | `SHOW_USAGE=1` |
| זרימת טוקן ראשון | מדד עיכוב נתפס | 1,3,4,6 | `BENCH_STREAM=1` (בדיקת ביצועים) |
| עמידות בניסיונות חוזרים | טיפול בהתחלות קרות זמניות | כל המפגשים | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| סוכנים מרובי מודלים | התמחות תפקידים הטרוגנית | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| ניתוב אדפטיבי | כוונה + היוריסטיקות עלות | 6 | הרחב את הניתוב עם לוגיקת הסלמה |
| זיכרון וקטורי | זיכרון סמנטי לטווח ארוך | 2,5,6 | שלב אינדקס הטמעות FAISS/Chroma |
| ייצוא מעקב | ביקורת והערכה | 2,5,6 | הוסף שורות JSON לכל שלב |
| מדדי איכות | מעקב איכותני | 3–6 | הנחיות ניקוד משניות |
| בדיקות עשן | אימות מהיר לפני סדנה | כל המפגשים | `python Workshop/tests/smoke.py` |

### התחלה מהירה דטרמיניסטית

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

צפו בספירת טוקנים יציבה על פני קלטים זהים חוזרים.

### הערכת RAG (מפגש 2)

השתמשו ב-`rag_eval_ragas.py` כדי לחשב רלוונטיות תשובה, נאמנות ודיוק הקשר על מערך נתונים סינתטי קטן:

```powershell
python samples/session02/rag_eval_ragas.py
```

הרחיבו על ידי אספקת JSONL גדול יותר של שאלות, הקשרים ואמיתות קרקע, ואז המרה ל-Dataset של Hugging Face.

## נספח דיוק פקודות CLI

הסדנה משתמשת בכוונה רק בפקודות CLI מתועדות / יציבות של Foundry Local.

### פקודות יציבות שהוזכרו

| קטגוריה | פקודה | מטרה |
|----------|---------|---------|
| ליבה | `foundry --version` | הצגת גרסה מותקנת |
| ליבה | `foundry init` | אתחול תצורה |
| שירות | `foundry service start` | הפעלת שירות מקומי (אם לא אוטומטי) |
| שירות | `foundry status` | הצגת מצב השירות |
| מודלים | `foundry model list` | רשימת קטלוג / מודלים זמינים |
| מודלים | `foundry model download <alias>` | הורדת משקלי מודל למטמון |
| מודלים | `foundry model run <alias>` | הפעלת מודל מקומי; ניתן לשלב עם `--prompt` להשלמה חד-פעמית |
| מודלים | `foundry model unload <alias>` / `foundry model stop <alias>` | פריקת מודל מהזיכרון (אם נתמך) |
| מטמון | `foundry cache list` | רשימת מודלים במטמון (שהורדו) |
| מערכת | `foundry system info` | צילום יכולות חומרה והאצה |
| מערכת | `foundry system gpu-info` | מידע דיאגנוסטי על GPU |
| תצורה | `foundry config list` | הצגת ערכי תצורה נוכחיים |
| תצורה | `foundry config set <key> <value>` | עדכון תצורה |

### תבנית הנחיה חד-פעמית

במקום פקודת המשנה המיושנת `model chat`, השתמשו ב:

```powershell
foundry model run <alias> --prompt "Your question here"
```

זה מבצע מחזור הנחיה/תגובה יחיד ואז יוצא.

### דפוסים שהוסרו / נמנעו

| מיושן / לא מתועד | תחליף / הנחיות |
|---------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | השתמשו ב-`foundry model list` רגיל + פעילות אחרונה / לוגים |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | השתמשו בסקריפט בדיקת ביצועים + כלים מערכתיים (מנהל משימות / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### בדיקות ביצועים וטלהמטריה

- עיכוב, p95, טוקנים לשנייה: `samples/session03/benchmark_oss_models.py`
- עיכוב טוקן ראשון (זרימה): הגדר `BENCH_STREAM=1`
- שימוש במשאבים: מוניטורים מערכתיים (מנהל משימות, Activity Monitor, `nvidia-smi`) + `foundry system info`.

כאשר פקודות טלהמטריה CLI חדשות יתייצבו, ניתן יהיה לשלב אותן עם עריכות מינימליות בקבצי המפגשים.

### שומר לינט אוטומטי

לינטר אוטומטי מונע החזרה של דפוסי CLI מיושנים בתוך בלוקים של קוד מסומן בקבצי Markdown:

סקריפט: `Workshop/scripts/lint_markdown_cli.py`

דפוסים מיושנים נחסמים בתוך בלוקים של קוד.

תחליפים מומלצים:
| מיושן | תחליף |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | סקריפט בדיקת ביצועים + כלים מערכתיים |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

הרצה מקומית:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` רץ על כל push ו-PR.

וו אופציונלי לפני התחייבות:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## טבלת מעבר מהירה CLI → SDK

| משימה | פקודת CLI חד-שורתית | מקבילה ב-SDK (Python) | הערות |
|------|---------------|-------------------------|-------|
| הרצת מודל פעם אחת (הנחיה) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | ה-SDK מאתחל שירות ומטמון אוטומטית |
| הורדת מודל (מטמון) | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | המנהל בוחר את הגרסה הטובה ביותר אם הכינוי ממפה למספר בניות |
| רשימת קטלוג | `foundry model list` | `# use manager for each alias or maintain known list` | ה-CLI מאגד; ה-SDK כרגע לפי אתחול כינוי |
| רשימת מודלים במטמון | `foundry cache list` | `manager.list_cached_models()` | לאחר אתחול המנהל (כל כינוי) |
| הפעלת האצת GPU | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | התצורה היא תוצאה חיצונית |
| קבלת URL של נקודת קצה | (מרומז) | `manager.endpoint` | משמש ליצירת לקוח תואם OpenAI |
| חימום מודל | `foundry model run <alias>` ואז הנחיה ראשונה | `chat_once(alias, messages=[...])` (עזר) | פונקציות עזר מטפלות בחימום עיכוב קר ראשוני |
| מדידת עיכוב | `python benchmark_oss_models.py` | `import benchmark_oss_models` (או סקריפט ייצוא חדש) | העדיפו סקריפט למדדים עקביים |
| עצירת מודל / פריקתו | `foundry model unload <alias>` | (לא נחשף – הפעל מחדש את השירות / התהליך) | בדרך כלל לא נדרש לזרימת הסדנה |
| קבלת שימוש בטוקנים | (צפו בפלט) | `resp.usage.total_tokens` | מסופק אם ה-backend מחזיר אובייקט שימוש |

## ייצוא Markdown של בדיקות ביצועים

השתמשו בסקריפט `Workshop/scripts/export_benchmark_markdown.py` כדי להריץ בדיקת ביצועים חדשה (אותו לוגיקה כמו `samples/session03/benchmark_oss_models.py`) ולייצר טבלת Markdown ידידותית ל-GitHub יחד עם JSON גולמי.

### דוגמה

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

קבצים שנוצרו:
| קובץ | תוכן |
|------|----------|
| `benchmark_report.md` | טבלת Markdown + רמזים לפרשנות |
| `benchmark_report.json` | מערך מדדים גולמי (להשוואות / מעקב מגמות) |

הגדירו `BENCH_STREAM=1` בסביבה כדי לכלול עיכוב טוקן ראשון אם נתמך.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.