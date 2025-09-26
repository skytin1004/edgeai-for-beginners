<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bad055c54c7952c482113fd7fe1d43c1",
  "translation_date": "2025-09-26T18:47:23+00:00",
  "source_file": "Module08/README.md",
  "language_code": "he"
}
-->
# מודול 08: עבודה מעשית עם Microsoft Foundry Local - ערכת כלים מלאה למפתחים

## סקירה כללית

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) מייצג את הדור הבא של פיתוח AI בקצה, ומספק למפתחים כלים עוצמתיים לבנייה, פריסה והרחבה של יישומי AI באופן מקומי תוך שמירה על אינטגרציה חלקה עם Azure AI Foundry. מודול זה מספק כיסוי מקיף של Foundry Local, החל מהתקנה ועד פיתוח מתקדם של סוכנים.

**טכנולוגיות מרכזיות:**
- Microsoft Foundry Local CLI ו-SDK
- אינטגרציה עם Azure AI Foundry
- הסקת מודלים על המכשיר
- מטמון ואופטימיזציה של מודלים מקומיים
- ארכיטקטורות מבוססות סוכנים

## מטרות למידה

עם סיום המודול, תוכלו:

- **לשלוט ב-Foundry Local**: להתקין, להגדיר ולבצע אופטימיזציה לפיתוח ב-Windows 11
- **לפרוס מודלים מגוונים**: להריץ מודלים כמו phi, qwen, deepseek ו-GPT באופן מקומי באמצעות פקודות CLI
- **לבנות פתרונות ייצור**: ליצור יישומי AI עם הנדסת הנחיות מתקדמת ואינטגרציית נתונים
- **לנצל את האקוסיסטם הפתוח**: לשלב מודלים של Hugging Face ותרומות קהילתיות
- **לפתח סוכני AI**: לבנות סוכנים חכמים עם יכולות עיגון ותזמור
- **ליישם דפוסים ארגוניים**: ליצור פתרונות AI מודולריים וניתנים להרחבה לפריסה בייצור

## מבנה המפגשים

### [1: התחלה עם Foundry Local](./01.FoundryLocalSetup.md)
**מיקוד**: התקנה, הגדרת CLI, פריסת מודלים ואופטימיזציה של חומרה

**נושאים מרכזיים**: התקנה מלאה • פקודות CLI • מטמון מודלים • האצת חומרה • פריסת מודלים מרובים

**דוגמה**: [מדריך מהיר לצ'אט REST](./samples/01/README.md) • [אינטגרציה עם OpenAI SDK](./samples/02/README.md) • [גילוי מודלים וביצועי Benchmark](./samples/03/README.md)

**משך**: 2-3 שעות | **רמה**: מתחילים

---

### [2: בניית פתרונות AI עם Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**מיקוד**: הנדסת הנחיות מתקדמת, אינטגרציית נתונים וקישוריות לענן

**נושאים מרכזיים**: הנדסת הנחיות • אינטגרציית נתונים • זרימות עבודה ב-Azure • אופטימיזציית ביצועים • ניטור

**דוגמה**: [יישום Chainlit RAG](./samples/04/README.md)

**משך**: 2-3 שעות | **רמה**: בינונית

---

### [3: מודלים בקוד פתוח ב-Foundry Local](./03.OpenSourceModels.md)
**מיקוד**: אינטגרציה עם Hugging Face, אסטרטגיות BYOM ומודלים קהילתיים

**נושאים מרכזיים**: אינטגרציה עם Hugging Face • הבאת מודלים משלכם • תובנות Model Mondays • תרומות קהילתיות • בחירת מודלים

**דוגמה**: [תזמור רב-סוכנים](./samples/05/README.md)

**משך**: 2-3 שעות | **רמה**: בינונית

---

### [4: חקר מודלים מתקדמים](./04.CuttingEdgeModels.md)
**מיקוד**: LLMs מול SLMs, יישום EdgeAI ודמואים מתקדמים

**נושאים מרכזיים**: השוואת מודלים • הסקה בקצה מול ענן • Phi + ONNX Runtime • יישום Chainlit RAG • אופטימיזציית WebGPU

**דוגמה**: [נתב מודלים ככלים](./samples/06/README.md)

**משך**: 3-4 שעות | **רמה**: מתקדמת

---

### [5: בניית סוכני AI במהירות](./05.AIPoweredAgents.md)
**מיקוד**: ארכיטקטורות סוכנים, הנחיות מערכת, עיגון ותזמור

**נושאים מרכזיים**: דפוסי עיצוב סוכנים • הנדסת הנחיות מערכת • טכניקות עיגון • מערכות רב-סוכנים • פריסה בייצור

**דוגמה**: [תזמור רב-סוכנים](./samples/05/README.md) • [מערכת רב-סוכנים מתקדמת](./samples/09/README.md)

**משך**: 3-4 שעות | **רמה**: מתקדמת

---

### [6: Foundry Local - מודלים ככלים](./06.ModelsAsTools.md)
**מיקוד**: פתרונות AI מודולריים, הרחבה ארגונית ודפוסי ייצור

**נושאים מרכזיים**: מודלים ככלים • פריסה על המכשיר • אינטגרציה SDK/API • ארכיטקטורות ארגוניות • אסטרטגיות הרחבה

**דוגמה**: [נתב מודלים ככלים](./samples/06/README.md) • [מסגרת כלים של Foundry](./samples/10/README.md)

**משך**: 3-4 שעות | **רמה**: מומחה

---

### [7: דפוסי אינטגרציה ישירה עם API](./samples/07/README.md)
**מיקוד**: אינטגרציה עם REST API בלבד ללא תלות ב-SDK לשליטה מרבית

**נושאים מרכזיים**: יישום לקוח HTTP • אימות מותאם אישית • ניטור בריאות מודלים • תגובות סטרימינג • טיפול בשגיאות בייצור

**דוגמה**: [לקוח API ישיר](./samples/07/README.md)

**משך**: 2-3 שעות | **רמה**: בינונית

---

### [8: יישום צ'אט מקומי ב-Windows 11](./samples/08/README.md)
**מיקוד**: בניית יישומי צ'אט מודרניים עם אינטגרציה של Foundry Local

**נושאים מרכזיים**: פיתוח Electron • Fluent Design System • אינטגרציה מקומית עם Windows • סטרימינג בזמן אמת • עיצוב ממשק צ'אט

**דוגמה**: [יישום צ'אט ב-Windows 11](./samples/08/README.md)

**משך**: 3-4 שעות | **רמה**: מתקדמת

---

### [9: תזמור רב-סוכנים מתקדם](./samples/09/README.md)
**מיקוד**: תיאום סוכנים מתוחכם, הקצאת משימות מיוחדות וזרימות עבודה שיתופיות

**נושאים מרכזיים**: תיאום סוכנים חכם • דפוסי קריאת פונקציות • תקשורת בין סוכנים • תזמור זרימות עבודה • מנגנוני הבטחת איכות

**דוגמה**: [מערכת רב-סוכנים מתקדמת](./samples/09/README.md)

**משך**: 4-5 שעות | **רמה**: מומחה

---

### [10: Foundry Local כמסגרת כלים](./samples/10/README.md)
**מיקוד**: ארכיטקטורה מבוססת כלים לשילוב Foundry Local ביישומים ומסגרות קיימות

**נושאים מרכזיים**: אינטגרציה עם LangChain • פונקציות Semantic Kernel • מסגרות REST API • כלי CLI • אינטגרציה עם Jupyter • דפוסי פריסה בייצור

**דוגמה**: [מסגרת כלים של Foundry](./samples/10/README.md)

**משך**: 4-5 שעות | **רמה**: מומחה

## דרישות מוקדמות

### דרישות מערכת
- **מערכת הפעלה**: Windows 11 (22H2 או גרסה מאוחרת יותר)
- **זיכרון**: 16GB RAM (מומלץ 32GB למודלים גדולים יותר)
- **אחסון**: 50GB שטח פנוי למטמון מודלים
- **חומרה**: מכשיר עם NPU מומלץ (Copilot+ PC), GPU אופציונלי
- **רשת**: אינטרנט מהיר להורדת מודלים ראשונית

### סביבת פיתוח
- Visual Studio Code עם הרחבת AI Toolkit
- Python 3.10+ ו-pip
- Git לניהול גרסאות
- PowerShell או Command Prompt
- Azure CLI (אופציונלי לאינטגרציה עם הענן)

### ידע מוקדם
- הבנה בסיסית של מושגי AI/ML
- היכרות עם שורת הפקודה
- יסודות תכנות ב-Python
- מושגי REST API
- ידע בסיסי בהנחיות והסקת מודלים

## ציר זמן של המודול

**זמן כולל משוער**: 30-38 שעות

| מפגש | תחום מיקוד | דוגמאות | זמן | מורכבות |
|---------|------------|---------|------|------------|
|  1 | התקנה ובסיס | 01, 02, 03 | 2-3 שעות | מתחילים |
|  2 | פתרונות AI | 04 | 2-3 שעות | בינונית |
|  3 | קוד פתוח | 05 | 2-3 שעות | בינונית |
|  4 | מודלים מתקדמים | 06 | 3-4 שעות | מתקדמת |
|  5 | סוכני AI | 05, 09 | 3-4 שעות | מתקדמת |
|  6 | כלים ארגוניים | 06, 10 | 3-4 שעות | מומחה |
|  7 | אינטגרציה ישירה עם API | 07 | 2-3 שעות | בינונית |
|  8 | יישום צ'אט ב-Windows 11 | 08 | 3-4 שעות | מתקדמת |
|  9 | תזמור רב-סוכנים מתקדם | 09 | 4-5 שעות | מומחה |
| 10 | מסגרת כלים | 10 | 4-5 שעות | מומחה |

## משאבים מרכזיים

**תיעוד רשמי:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - קוד מקור ודוגמאות רשמיות
- [תיעוד Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - מדריך התקנה ושימוש מלא
- [סדרת Model Mondays](https://aka.ms/model-mondays) - הדגשות מודלים שבועיות ומדריכים

**קהילה ותמיכה:**
- [דיונים על Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - שאלות ותשובות קהילתיות ובקשות תכונה
- [קהילת מפתחים של Microsoft AI](https://techcommunity.microsoft.com/category/artificialintelligence) - חדשות אחרונות ופרקטיקות מומלצות

## תוצאות למידה

עם סיום המודול, תהיו מצוידים ל:

### שליטה טכנית
- **לפרוס ולנהל**: התקנות Foundry Local בסביבות פיתוח וייצור
- **לשלב מודלים**: לעבוד בצורה חלקה עם משפחות מודלים מגוונות ממיקרוסופט, Hugging Face ומקורות קהילתיים
- **לבנות יישומים**: ליצור יישומי AI מוכנים לייצור עם תכונות מתקדמות ואופטימיזציות
- **לפתח סוכנים**: ליישם סוכני AI מתוחכמים עם עיגון, הסקה ואינטגרציית כלים

### הבנה אסטרטגית
- **החלטות ארכיטקטורה**: לקבל החלטות מושכלות בין פריסה מקומית לפריסה בענן
- **אופטימיזציית ביצועים**: לבצע אופטימיזציה לביצועי הסקה על פני תצורות חומרה שונות
- **הרחבה ארגונית**: לעצב יישומים שמתרחבים מפרוטוטיפים מקומיים לפריסות ארגוניות
- **פרטיות ואבטחה**: ליישם פתרונות AI שמגנים על פרטיות עם הסקה מקומית

### יכולות חדשנות
- **פיתוח מהיר**: לבנות ולבדוק רעיונות ליישומי AI במהירות על פני כל 10 דפוסי הדוגמאות
- **אינטגרציה קהילתית**: לנצל מודלים בקוד פתוח ולתרום לאקוסיסטם
- **דפוסים מתקדמים**: ליישם דפוסי AI מתקדמים כולל RAG, סוכנים ואינטגרציית כלים
- **שליטה במסגרות**: אינטגרציה ברמה מומחית עם LangChain, Semantic Kernel, Chainlit ו-Electron
- **פריסה בייצור**: לפרוס פתרונות AI ניתנים להרחבה מפרוטוטיפים מקומיים למערכות ארגוניות
- **פיתוח מוכן לעתיד**: לבנות יישומים מוכנים לטכנולוגיות ודפוסי AI מתקדמים

## התחלה

1. **הגדרת סביבה**: ודאו Windows 11 עם חומרה מומלצת (ראו דרישות מוקדמות)
2. **התקנת Foundry Local**: עקבו אחרי מפגש 1 להתקנה והגדרה מלאה
3. **הרצת דוגמה 01**: התחילו עם אינטגרציה בסיסית של REST API כדי לוודא את ההגדרה
4. **התקדמות דרך הדוגמאות**: השלימו דוגמאות 01-10 לשליטה מקיפה

## מדדי הצלחה

עקבו אחרי ההתקדמות שלכם דרך כל 10 הדוגמאות המקיפות:

### רמת יסוד (דוגמאות 01-03)
- [ ] התקנה והגדרה מוצלחת של Foundry Local
- [ ] השלמת אינטגרציה עם REST API (דוגמה 01)
- [ ] יישום תאימות עם OpenAI SDK (דוגמה 02)
- [ ] ביצוע גילוי מודלים וביצועי Benchmark (דוגמה 03)

### רמת יישום (דוגמאות 04-06)
- [ ] פריסה והרצה של לפחות 4 משפחות מודלים שונות
- [ ] בניית יישום צ'אט RAG פונקציונלי (דוגמה 04)
- [ ] יצירת מערכת תזמור רב-סוכנים (דוגמה 05)
- [ ] יישום נתב מודלים חכם (דוגמה 06)

### רמת אינטגרציה מתקדמת (דוגמאות 07-10)
- [ ] בניית לקוח API מוכן לייצור (דוגמה 07)
- [ ] פיתוח יישום צ'אט מקומי ב-Windows 11 (דוגמה 08)
- [ ] יישום מערכת רב-סוכנים מתקדמת (דוגמה 09)
- [ ] יצירת מסגרת כלים מקיפה (דוגמה 10)

### מדדי שליטה
- [ ] הרצת כל 10 הדוגמאות ללא שגיאות
- [ ] התאמה אישית של לפחות 3 דוגמאות למקרי שימוש ספציפיים
- [ ] פריסת 2+ דוגמאות בסביבות דמויות ייצור
- [ ] תרומה לשיפורים או הרחבות לקוד הדוגמאות
- [ ] שילוב דפוסי Foundry Local בפרויקטים אישיים/מקצועיים

## מדריך התחלה מהירה - כל 10 הדוגמאות

### הגדרת סביבה (נדרש לכל הדוגמאות)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### דוגמאות יסוד מרכזיות (01-06)

**דוגמה 01: מדריך מהיר לצ'אט REST**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**דוגמה 02: אינטגרציה עם OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**דוגמה 03: גילוי מודלים וביצועי Benchmark**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**דוגמה 04: יישום Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**דוגמה 05: תזמור רב-סוכנים**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**דוגמה 06: נתב מודלים ככלים**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b-instruct

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### דוגמאות אינטגרציה מתקדמות (07-10)

**דוגמה 07: לקוח API ישיר**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**דוגמה 08: יישום צ'אט ב-Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**דוגמה 09: מערכת רב-סוכנים מתקדמת**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**דוגמה 10: מסגרת כלים של Foundry**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### פתרון בעיות נפוצות

**שגיאות חיבור ל-Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**בעיות טעינת מודלים**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**בעיות תלות**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## סיכום
מודול זה מייצג את חזית הפיתוח של AI בקצה, ומשלב את הכלים הארגוניים ברמה הגבוהה של Microsoft עם הגמישות והחדשנות של עולם הקוד הפתוח. על ידי שליטה ב-Foundry Local דרך כל 10 הדוגמאות המקיפות, תמצאו את עצמכם בחזית פיתוח יישומי AI.

**מסלול לימוד מלא:**
- **בסיס** (דוגמאות 01-03): שילוב API וניהול מודלים
- **יישומים** (דוגמאות 04-06): RAG, סוכנים וניתוב חכם
- **מתקדמים** (דוגמאות 07-10): מסגרות ייצור ואינטגרציה ארגונית

לשילוב Azure OpenAI (מפגש 2), עיינו בקבצי README של הדוגמאות הבודדות לקבלת משתני סביבה נדרשים והגדרות גרסת API.

---

