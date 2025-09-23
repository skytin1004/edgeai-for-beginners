<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T21:47:01+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "he"
}
-->
# יומן שינויים

כל השינויים המשמעותיים ב-EdgeAI למתחילים מתועדים כאן. הפרויקט משתמש ברישומים מבוססי תאריכים ובסגנון Keep a Changelog (נוסף, שונה, תוקן, הוסר, תיעוד, הועבר).

## 2025-09-18

### נוסף
- מודול 08: Microsoft Foundry Local – ערכת כלים מלאה למפתחים
  - שישה מפגשים: הגדרה, אינטגרציה עם Azure AI Foundry, מודלים בקוד פתוח, הדגמות מתקדמות, סוכנים, ומודלים ככלים
  - דוגמאות להפעלה תחת `Module08/samples/01`–`06` עם הוראות cmd ל-Windows
    - `01` צ'אט מהיר REST (`chat_quickstart.py`)
    - `02` התחלה מהירה SDK עם OpenAI/Foundry Local ותמיכה ב-Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI רשימה וביצועים (`list_and_bench.cmd`)
    - `04` הדגמת Chainlit (`app.py`)
    - `05` תזמור רב-סוכנים (`python -m samples.05.agents.coordinator`)
    - `06` נתב מודלים ככלים (`router.py`)
- תמיכה ב-Azure OpenAI בדוגמת SDK של מפגש 2 עם תצורת משתני סביבה
- `.vscode/settings.json` מצביע על `Module08/.venv` ומשפר את ניתוח Python
- `.env` עם רמז `PYTHONPATH` למודעות VS Code/Pylance

### שונה
- מודל ברירת המחדל עודכן ל-`phi-4-mini` בכל מסמכי ודוגמאות מודול 08; הוסרו אזכורים שנותרו ל-`phi-3.5` בתוך מודול 08
- שיפורים בנתב (`Module08/samples/06/router.py`):
  - גילוי נקודות קצה באמצעות `foundry service status` עם ניתוח regex
  - בדיקת בריאות `/v1/models` בעת הפעלה
  - רישום מודלים ניתן לתצורה באמצעות משתני סביבה (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- דרישות עודכנו: `Module08/requirements.txt` כולל כעת `openai` (יחד עם `requests`, `chainlit`)
- הנחיות לדוגמת Chainlit הובהרו ונוספו פתרונות לבעיות; פתרון ייבוא באמצעות הגדרות סביבת עבודה

### תוקן
- נפתרו בעיות ייבוא:
  - הנתב אינו תלוי עוד במודול `utils` שאינו קיים; פונקציות שולבו בקוד
  - המתאם משתמש בייבוא יחסי (`from .specialists import ...`) ומופעל דרך נתיב מודול
  - תצורת VS Code/Pylance לפתרון ייבוא `chainlit` וחבילות
- תיקון טעות קטנה ב-`STUDY_GUIDE.md` והוספת כיסוי למודול 08

### הוסר
- נמחק `Module08/infra/obs.py` שאינו בשימוש והוסר תיקיית `infra/` הריקה; דפוסי תצפית נשמרו כאופציונליים בתיעוד

### הועבר
- הדגמות מודול 08 אוחדו תחת `Module08/samples` עם תיקיות ממוספרות לפי מפגשים
  - אפליקציית Chainlit הועברה ל-`samples/04`
  - סוכנים הועברו ל-`samples/05` ונוספו קבצי `__init__.py` לפתרון חבילות

### תיעוד
- תיעוד מפגשי מודול 08 וכל קובצי README לדוגמאות הועשרו עם הפניות ל-Microsoft Learn ולספקים מהימנים
- `Module08/README.md` עודכן עם סקירת דוגמאות, תצורת נתב וטיפים לאימות
- סעיף Windows Foundry Local ב-`Module07/README.md` אומת מול תיעוד Learn
- `STUDY_GUIDE.md` עודכן:
  - הוספת מודול 08 לסקירה, לוחות זמנים, מעקב התקדמות
  - הוספת סעיף הפניות מקיף (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## היסטורי (סיכום)
- מבנה הקורס והמודולים הוקמו (מודולים 01–07)
- עדכון תוכן באופן איטרטיבי, סטנדרטיזציה של פורמט, והוספת מחקרי מקרה
- הרחבת כיסוי מסגרות אופטימיזציה (Llama.cpp, Olive, OpenVINO, Apple MLX)

## לא פורסם / צבר (הצעות)
- בדיקות עשן אופציונליות לכל דוגמה לאימות זמינות Foundry Local
- סקירת תרגומים להתאמת אזכורי מודלים (לדוגמה, `phi-4-mini`) במידת הצורך
- הוספת תצורת pyright מינימלית אם צוותים מעדיפים מחמירות ברמת סביבת עבודה

---

