<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:38:48+00:00",
  "source_file": "AGENTS.md",
  "language_code": "he"
}
-->
# AGENTS.md

## סקירת הפרויקט

EdgeAI for Beginners הוא מאגר חינוכי מקיף המלמד פיתוח Edge AI עם מודלים לשוניים קטנים (SLMs). הקורס מכסה את יסודות EdgeAI, פריסת מודלים, טכניקות אופטימיזציה ויישומים מוכנים לייצור באמצעות Microsoft Foundry Local ומגוון מסגרות AI.

**טכנולוגיות מרכזיות:**
- Python 3.8+ (שפת תכנות ראשית לדוגמאות AI/ML)
- .NET C# (דוגמאות AI/ML)
- JavaScript/Node.js עם Electron (ליישומי שולחן עבודה)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- מסגרות AI: LangChain, Semantic Kernel, Chainlit
- אופטימיזציית מודלים: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**סוג המאגר:** מאגר תוכן חינוכי עם 8 מודולים ו-10 יישומים לדוגמה מקיפים

**ארכיטקטורה:** מסלול למידה רב-מודולי עם דוגמאות מעשיות המדגימות דפוסי פריסה של Edge AI

## מבנה המאגר

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## פקודות התקנה

### התקנת המאגר

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### התקנת דוגמאות Python (מודול 08 ודוגמאות Python)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### התקנת דוגמאות Node.js (דוגמה 08 - אפליקציית צ'אט ל-Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### התקנת Foundry Local

Foundry Local נדרש להפעלת דוגמאות מודול 08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## תהליך פיתוח

### פיתוח תוכן

מאגר זה מכיל בעיקר **תוכן חינוכי ב-Markdown**. בעת ביצוע שינויים:

1. ערכו קבצי `.md` בתיקיות המודולים המתאימות
2. עקבו אחר דפוסי העיצוב הקיימים
3. ודאו שדוגמאות הקוד מדויקות ונבדקו
4. עדכנו את התוכן המתורגם המתאים אם נדרש (או תנו לאוטומציה לטפל בכך)

### פיתוח יישומי דוגמה

לדוגמאות Python (דוגמאות 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

לדוגמת Electron (דוגמה 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### בדיקת יישומי דוגמה

לדוגמאות Python אין בדיקות אוטומטיות אך ניתן לאמת אותן על ידי הפעלתן:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

לדוגמת Electron יש תשתית בדיקות:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## הוראות בדיקה

### אימות תוכן

המאגר משתמש בתהליכי תרגום אוטומטיים. אין צורך בבדיקות ידניות לתרגומים.

**אימות ידני לשינויים בתוכן:**
1. בדקו את עיצוב Markdown על ידי תצוגה מקדימה של קבצי `.md`
2. ודאו שכל הקישורים מצביעים על יעדים תקינים
3. בדקו כל קטעי קוד הכלולים בתיעוד
4. ודאו שהתמונות נטענות כראוי

### בדיקת יישומי דוגמה

**מודול 08/דוגמאות/08 (אפליקציית Electron) כוללת בדיקות מקיפות:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**דוגמאות Python צריכות להיבדק ידנית:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## הנחיות סגנון קוד

### תוכן Markdown

- השתמשו בהיררכיית כותרות עקבית (# לכותרת, ## לסעיפים ראשיים, ### לסעיפים משנה)
- כללו קטעי קוד עם מצייני שפה: ```python, ```bash, ```javascript
- עקבו אחר העיצוב הקיים לטבלאות, רשימות והדגשות
- שמרו על שורות קריאות (שאפו ל-80-100 תווים, אך לא באופן מחמיר)
- השתמשו בקישורים יחסיים להפניות פנימיות

### סגנון קוד Python

- עקבו אחר מוסכמות PEP 8
- השתמשו ברמזי סוג כאשר מתאים
- כללו docstrings לפונקציות ולמחלקות
- השתמשו בשמות משתנים משמעותיים
- שמרו על פונקציות ממוקדות ותמציתיות

### סגנון קוד JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**מוסכמות מרכזיות:**
- תצורת ESLint מסופקת בדוגמה 08
- Prettier לעיצוב קוד
- השתמשו בתחביר מודרני ES6+
- עקבו אחר הדפוסים הקיימים בקוד

## הנחיות Pull Request

### פורמט כותרת
```
[ModuleXX] Brief description of change
```
או
```
[Module08/samples/XX] Description for sample changes
```

### לפני הגשה

**לשינויים בתוכן:**
- תצוגה מקדימה של כל קבצי Markdown ששונו
- ודאו שהקישורים והתמונות עובדים
- בדקו שגיאות כתיב ודקדוק

**לשינויים בקוד לדוגמה (מודול 08/דוגמאות/08):**
```bash
npm run lint
npm test
```

**לשינויים בדוגמאות Python:**
- בדקו שהדוגמה פועלת בהצלחה
- ודאו שטיפול בשגיאות עובד
- בדקו תאימות ל-Foundry Local

### תהליך סקירה

- שינויים בתוכן חינוכי נבדקים לדיוק ובהירות
- דוגמאות קוד נבדקות לפונקציונליות
- עדכוני תרגום מטופלים אוטומטית על ידי GitHub Actions

## מערכת תרגום

**חשוב:** מאגר זה משתמש בתרגום אוטומטי באמצעות GitHub Actions.

- תרגומים נמצאים בתיקיית `/translations/` (50+ שפות)
- מתבצע אוטומטית באמצעות `co-op-translator.yml` workflow
- **אין לערוך ידנית קבצי תרגום** - הם יוחלפו
- ערכו רק קבצי מקור באנגלית בתיקיות השורש והמודולים
- תרגומים נוצרים אוטומטית בעת דחיפה ל-main branch

## אינטגרציה עם Foundry Local

רוב דוגמאות מודול 08 דורשות ש-Foundry Local יפעל:

### הפעלת Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### אימות Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### משתני סביבה לדוגמאות

רוב הדוגמאות משתמשות במשתני סביבה אלו:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## בנייה ופריסה

### פריסת תוכן

מאגר זה הוא בעיקר תיעוד - אין צורך בתהליך בנייה לתוכן.

### בניית יישומי דוגמה

**אפליקציית Electron (מודול 08/דוגמאות/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**דוגמאות Python:**
אין תהליך בנייה - הדוגמאות מופעלות ישירות עם מפרש Python.

## בעיות נפוצות ופתרון תקלות

### Foundry Local לא פועל
**בעיה:** דוגמאות נכשלות עם שגיאות חיבור

**פתרון:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### בעיות בסביבת Python Virtual
**בעיה:** שגיאות ייבוא מודולים

**פתרון:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### בעיות בניית Electron
**בעיה:** npm install או כשלי בנייה

**פתרון:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### קונפליקטים בתהליך תרגום
**בעיה:** PR תרגום מתנגש עם השינויים שלכם

**פתרון:**
- ערכו רק קבצי מקור באנגלית
- תנו לתהליך התרגום האוטומטי לטפל בתרגומים
- אם מתרחשים קונפליקטים, מיזגו את `main` לענף שלכם לאחר שהתמזגו התרגומים

## משאבים נוספים

### מסלולי למידה
- **מסלול מתחילים:** מודולים 01-02 (7-9 שעות)
- **מסלול ביניים:** מודולים 03-04 (9-11 שעות)
- **מסלול מתקדם:** מודולים 05-07 (12-15 שעות)
- **מסלול מומחים:** מודול 08 (8-10 שעות)

### תוכן מרכזי במודולים
- **מודול 01:** יסודות EdgeAI ומקרי מבחן בעולם האמיתי
- **מודול 02:** משפחות וארכיטקטורות של מודלים לשוניים קטנים (SLM)
- **מודול 03:** אסטרטגיות פריסה מקומיות וענניות
- **מודול 04:** אופטימיזציית מודלים עם מסגרות שונות
- **מודול 05:** SLMOps - תפעול בייצור
- **מודול 06:** סוכני AI וקריאת פונקציות
- **מודול 07:** יישומים ספציפיים לפלטפורמות
- **מודול 08:** ערכת כלים Foundry Local עם 10 דוגמאות מקיפות

### תלות חיצונית
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - סביבת ריצה למודלים AI מקומיים
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - מסגרת אופטימיזציה
- [Microsoft Olive](https://microsoft.github.io/Olive/) - ערכת כלים לאופטימיזציית מודלים
- [OpenVINO](https://docs.openvino.ai/) - ערכת אופטימיזציה של אינטל

## הערות ספציפיות לפרויקט

### יישומי דוגמה במודול 08

המאגר כולל 10 יישומי דוגמה מקיפים:

1. **01-REST Chat Quickstart** - אינטגרציה בסיסית עם OpenAI SDK
2. **02-OpenAI SDK Integration** - תכונות מתקדמות של SDK
3. **03-Model Discovery & Benchmarking** - כלי השוואת מודלים
4. **04-Chainlit RAG Application** - יצירה מוגברת על ידי אחזור
5. **05-Multi-Agent Orchestration** - תיאום סוכנים בסיסי
6. **06-Models-as-Tools Router** - ניתוב מודלים חכם
7. **07-Direct API Client** - אינטגרציה ברמת API נמוכה
8. **08-Windows 11 Chat App** - אפליקציית שולחן עבודה Electron מקורית
9. **09-Advanced Multi-Agent System** - תיאום סוכנים מורכב
10. **10-Foundry Tools Framework** - אינטגרציה עם LangChain/Semantic Kernel

כל דוגמה מדגימה היבטים שונים של פיתוח Edge AI עם Foundry Local.

### שיקולי ביצועים

- SLMs מותאמים לפריסה בקצה (2-16GB RAM)
- הסקה מקומית מספקת זמני תגובה של 50-500ms
- טכניקות כימות משיגות הפחתת גודל של 75% עם שמירה על 85% ביצועים
- יכולות שיחה בזמן אמת עם מודלים מקומיים

### אבטחה ופרטיות

- כל העיבוד מתבצע מקומית - אין שליחת נתונים לענן
- מתאים ליישומים רגישים לפרטיות (בריאות, פיננסים)
- עומד בדרישות ריבונות נתונים
- Foundry Local פועל כולו על חומרה מקומית

---

**זהו מאגר חינוכי המתמקד בהוראת פיתוח Edge AI. דפוס התרומה העיקרי הוא שיפור תוכן חינוכי והוספה/שיפור של יישומי דוגמה המדגימים מושגי Edge AI.**

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.