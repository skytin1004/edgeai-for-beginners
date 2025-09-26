<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3f3219903847ef3849e482fa30a64ad4",
  "translation_date": "2025-09-26T09:15:51+00:00",
  "source_file": "README.md",
  "language_code": "he"
}
-->
# EdgeAI למתחילים

![תמונת שער הקורס](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.he.png)

[![תורמים ב-GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![בעיות ב-GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![בקשות משיכה ב-GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![ברוכים הבאים ל-PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![צופים ב-GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![מזלגות ב-GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![כוכבים ב-GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

כדי להתחיל להשתמש במשאבים אלו, בצעו את השלבים הבאים:

1. **צרו מזלג למאגר**: לחצו [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **שכפלו את המאגר**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**הצטרפו ל-Azure AI Foundry Discord ופגשו מומחים ומפתחים נוספים**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 תמיכה בריבוי שפות

#### נתמך באמצעות GitHub Action (אוטומטי ומעודכן תמיד)

[ערבית](../ar/README.md) | [בנגלית](../bn/README.md) | [בולגרית](../bg/README.md) | [בורמזית (מיאנמר)](../my/README.md) | [סינית (פשוטה)](../zh/README.md) | [סינית (מסורתית, הונג קונג)](../hk/README.md) | [סינית (מסורתית, מקאו)](../mo/README.md) | [סינית (מסורתית, טייוואן)](../tw/README.md) | [קרואטית](../hr/README.md) | [צ'כית](../cs/README.md) | [דנית](../da/README.md) | [הולנדית](../nl/README.md) | [פינית](../fi/README.md) | [צרפתית](../fr/README.md) | [גרמנית](../de/README.md) | [יוונית](../el/README.md) | [עברית](./README.md) | [הינדית](../hi/README.md) | [הונגרית](../hu/README.md) | [אינדונזית](../id/README.md) | [איטלקית](../it/README.md) | [יפנית](../ja/README.md) | [קוריאנית](../ko/README.md) | [מלאית](../ms/README.md) | [מרטהי](../mr/README.md) | [נפאלית](../ne/README.md) | [נורווגית](../no/README.md) | [פרסית (פרסית)](../fa/README.md) | [פולנית](../pl/README.md) | [פורטוגזית (ברזיל)](../br/README.md) | [פורטוגזית (פורטוגל)](../pt/README.md) | [פנג'אבית (גורמוכי)](../pa/README.md) | [רומנית](../ro/README.md) | [רוסית](../ru/README.md) | [סרבית (קירילית)](../sr/README.md) | [סלובקית](../sk/README.md) | [סלובנית](../sl/README.md) | [ספרדית](../es/README.md) | [סווהילית](../sw/README.md) | [שוודית](../sv/README.md) | [טאגאלוג (פיליפינית)](../tl/README.md) | [תאית](../th/README.md) | [טורקית](../tr/README.md) | [אוקראינית](../uk/README.md) | [אורדו](../ur/README.md) | [וייטנאמית](../vi/README.md)

**אם תרצו להוסיף שפות תרגום נוספות, הרשימה המלאה מופיעה [כאן](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## מבוא

ברוכים הבאים ל-**EdgeAI למתחילים** – המסע המקיף שלכם לעולם המהפכני של בינה מלאכותית בקצה (Edge AI). קורס זה מגשר על הפער בין יכולות AI עוצמתיות לבין פריסה מעשית בעולם האמיתי על גבי מכשירי קצה, ומאפשר לכם לנצל את הפוטנציאל של AI ישירות במקום שבו הנתונים נוצרים וההחלטות צריכות להתקבל.

### מה תלמדו לשלוט בו

הקורס לוקח אתכם מהבסיס ועד ליישומים מוכנים לייצור, כולל:
- **מודלים לשוניים קטנים (SLMs)** המותאמים לפריסה בקצה
- **אופטימיזציה מותאמת לחומרה** לפלטפורמות מגוונות
- **הסקת מסקנות בזמן אמת** עם שמירה על פרטיות
- **אסטרטגיות פריסה לייצור** ליישומים ארגוניים

### למה EdgeAI חשוב

Edge AI מייצג שינוי פרדיגמה שמטפל באתגרים מודרניים קריטיים:
- **פרטיות ואבטחה**: עיבוד נתונים רגישים באופן מקומי ללא חשיפה לענן
- **ביצועים בזמן אמת**: ביטול השהיית רשת ליישומים קריטיים
- **יעילות כלכלית**: הפחתת עלויות רוחב פס ומחשוב בענן
- **תפעול עמיד**: שמירה על פונקציונליות בזמן תקלות רשת
- **עמידה ברגולציות**: עמידה בדרישות ריבונות נתונים

### Edge AI

Edge AI מתייחס להרצת אלגוריתמים של AI ומודלים לשוניים באופן מקומי על חומרה, קרוב למקום שבו הנתונים נוצרים, ללא תלות במשאבי ענן לצורך הסקת מסקנות. זה מפחית השהיה, משפר פרטיות ומאפשר קבלת החלטות בזמן אמת.

### עקרונות ליבה:
- **הסקת מסקנות על המכשיר**: מודלי AI פועלים על מכשירי קצה (טלפונים, נתבים, מיקרו-בקרים, מחשבים תעשייתיים)
- **יכולת עבודה במצב לא מקוון**: פועל ללא חיבור אינטרנט מתמיד
- **השהיה נמוכה**: תגובות מיידיות המתאימות למערכות בזמן אמת
- **ריבונות נתונים**: שמירה על נתונים רגישים באופן מקומי, לשיפור אבטחה ועמידה ברגולציות

### מודלים לשוניים קטנים (SLMs)

מודלים כמו Phi-4, Mistral-7B ו-Gemma הם גרסאות מותאמות של מודלים לשוניים גדולים יותר, שעברו אימון או דיסטילציה לצורך:
- **שימוש מופחת בזיכרון**: ניצול יעיל של זיכרון מוגבל במכשירי קצה
- **דרישות חישוב נמוכות**: מותאם לביצועים על CPU ו-GPU בקצה
- **זמני הפעלה מהירים יותר**: אתחול מהיר ליישומים תגובתיים

מודלים אלו מאפשרים יכולות NLP עוצמתיות תוך עמידה במגבלות של:
- **מערכות משובצות**: מכשירי IoT ובקרים תעשייתיים
- **מכשירים ניידים**: סמארטפונים וטאבלטים עם יכולות עבודה במצב לא מקוון
- **מכשירי IoT**: חיישנים ומכשירים חכמים עם משאבים מוגבלים
- **שרתי קצה**: יחידות עיבוד מקומיות עם משאבי GPU מוגבלים
- **מחשבים אישיים**: תרחישי פריסה על מחשבים שולחניים וניידים

## מודולי הקורס וניווט

| מודול | נושא | תחום מיקוד | תוכן מרכזי | רמה | משך |
|-------|-------|------------|-------------|------|-------|
| [📖 00 ](./introduction.md) | [מבוא ל-EdgeAI](./introduction.md) | יסודות והקשר | סקירת EdgeAI • יישומים בתעשייה • מבוא ל-SLM • מטרות למידה | מתחילים | 1-2 שעות |
| [📚 01](../../Module01) | [יסודות EdgeAI](./Module01/README.md) | השוואה בין ענן לקצה | יסודות EdgeAI • מקרי בוחן בעולם האמיתי • מדריך יישום • פריסה בקצה | מתחילים | 3-4 שעות |
| [🧠 02](../../Module02) | [יסודות מודלי SLM](./Module02/README.md) | משפחות מודלים וארכיטקטורה | משפחת Phi • משפחת Qwen • משפחת Gemma • BitNET • μModel • Phi-Silica | מתחילים | 4-5 שעות |
| [🚀 03](../../Module03) | [תרגול פריסת SLM](./Module03/README.md) | פריסה מקומית ועננית | למידה מתקדמת • סביבה מקומית • פריסה בענן | בינוני | 4-5 שעות |
| [⚙️ 04](../../Module04) | [ערכת כלים לאופטימיזציית מודלים](./Module04/README.md) | אופטימיזציה חוצת פלטפורמות | מבוא • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • סינתזת תהליכים | בינוני | 5-6 שעות |
| [🔧 05](../../Module05) | [SLMOps לייצור](./Module05/README.md) | תפעול בייצור | מבוא ל-SLMOps • דיסטילציית מודלים • כוונון עדין • פריסה לייצור | מתקדם | 5-6 שעות |
| [🤖 06](../../Module06) | [סוכני AI וקריאת פונקציות](./Module06/README.md) | מסגרות סוכנים ו-MCP | מבוא לסוכנים • קריאת פונקציות • פרוטוקול הקשר למודלים | מתקדם | 4-5 שעות |
| [💻 07](../../Module07) | [יישום פלטפורמות](./Module07/README.md) | דוגמאות חוצות פלטפורמות | ערכת כלים ל-AI • Foundry Local • פיתוח ב-Windows | מתקדם | 3-4 שעות |
| [🏭 08](../../Module08) | [ערכת כלים Foundry Local](./Module08/README.md) | דוגמאות מוכנות לייצור | יישומים לדוגמה (ראו פרטים למטה) | מומחה | 8-10 שעות |

### 🏭 **מודול 08: יישומים לדוגמה**

- [01: התחלה מהירה עם REST Chat](./Module08/samples/01/README.md)
- [02: אינטגרציה עם OpenAI SDK](./Module08/samples/02/README.md)
- [03: גילוי מודלים וביצועי Benchmark](./Module08/samples/03/README.md)
- [04: יישום Chainlit RAG](./Module08/samples/04/README.md)
- [05: תזמור רב-סוכנים](./Module08/samples/05/README.md)
- [06: נתב מודלים ככלים](./Module08/samples/06/README.md)
- [07: לקוח API ישיר](./Module08/samples/07/README.md)
- [08: אפליקציית צ'אט ל-Windows 11](./Module08/samples/08/README.md)
- [09: מערכת רב-סוכנים מתקדמת](./Module08/samples/09/README.md)
- [10: מסגרת כלים Foundry](./Module08/samples/10/README.md)

### 📊 **סיכום מסלול הלמידה**
- **משך כולל**: 36-45 שעות
- **מסלול למתחילים**: מודולים 01-02 (7-9 שעות)  
- **מסלול בינוני**: מודולים 03-04 (9-11 שעות)
- **מסלול מתקדם**: מודולים 05-07 (12-15 שעות)
- **מסלול מומחה**: מודול 08 (8-10 שעות)

## מה תבנו

### 🎯 מיומנויות ליבה
- **ארכיטקטורת Edge AI**: תכנון מערכות AI מקומיות עם אינטגרציה לענן
- **אופטימיזציית מודלים**: כיווץ וקוונטיזציה של מודלים לפריסה בקצה (שיפור מהירות ב-85%, הפחתת גודל ב-75%)
- **פריסה רב-פלטפורמית**: Windows, מובייל, מערכות משובצות ומערכות היברידיות ענן-קצה
- **תפעול בייצור**: ניטור, סקיילינג ותחזוקה של Edge AI בייצור

### 🏗️ פרויקטים מעשיים
- **אפליקציות צ'אט Foundry Local**: אפליקציה מקורית ל-Windows 11 עם מעבר בין מודלים
- **מערכות רב-סוכנים**: מתאם עם סוכנים מומחים למשימות מורכבות  
- **יישומי RAG**: עיבוד מסמכים מקומי עם חיפוש וקטורי
- **נתבי מודלים**: בחירה חכמה בין מודלים בהתבסס על ניתוח משימות
- **מסגרות API**: לקוחות מוכנים לייצור עם סטרימינג וניטור בריאות
- **כלים חוצי פלטפורמות**: תבניות אינטגרציה עם LangChain/Semantic Kernel

### 🏢 יישומים בתעשייה
**ייצור** • **בריאות** • **רכבים אוטונומיים** • **ערים חכמות** • **אפליקציות מובייל**

## התחלה מהירה

**מסלול למידה מומלץ** (20-30 שעות בסך הכל):

0. **📖 מבוא** ([Introduction.md](./introduction.md)): יסודות EdgeAI + הקשר תעשייתי + מסגרת למידה  
1. **📚 יסודות** (מודולים 01-02): מושגי EdgeAI + משפחות מודלי SLM  
2. **⚙️ אופטימיזציה** (מודולים 03-04): פריסה + מסגרות כיווץ  
3. **🚀 ייצור** (מודולים 05-06): SLMOps + סוכני AI + קריאה לפונקציות  
4. **💻 יישום** (מודולים 07-08): דוגמאות פלטפורמה + ערכת כלים Foundry Local  

כל מודול כולל תיאוריה, תרגילים מעשיים ודוגמאות קוד מוכנות לייצור.

## השפעה על הקריירה

**תפקידים טכניים**: ארכיטקט פתרונות EdgeAI • מהנדס ML (Edge) • מפתח IoT AI • מפתח AI למובייל  

**תחומי תעשייה**: ייצור 4.0 • טכנולוגיות בריאות • מערכות אוטונומיות • FinTech • אלקטרוניקה צרכנית  

**פרויקטים לתיק עבודות**: מערכות רב-סוכנים • אפליקציות RAG לייצור • פריסה בין-פלטפורמות • אופטימיזציית ביצועים  

## מבנה המאגר

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```
  

## נקודות עיקריות בקורס

✅ **למידה מתקדמת**: תיאוריה → תרגול → פריסה לייצור  
✅ **מחקרי מקרה אמיתיים**: Microsoft, Japan Airlines, יישומים ארגוניים  
✅ **דוגמאות מעשיות**: מעל 50 דוגמאות, 10 הדגמות מקיפות של Foundry Local  
✅ **מיקוד בביצועים**: שיפורי מהירות של 85%, הפחתת גודל של 75%  
✅ **רב-פלטפורמות**: Windows, מובייל, משובץ, ענן-היברידי  
✅ **מוכן לייצור**: ניטור, סקיילינג, אבטחה, מסגרות תאימות  

📖 **[מדריך לימוד זמין](STUDY_GUIDE.md)**: מסלול לימוד מובנה של 20 שעות עם הנחיות לחלוקת זמן וכלי הערכה עצמית.

---

**EdgeAI מייצג את העתיד של פריסת AI**: מקומי תחילה, שומר פרטיות ויעיל. שלוט במיומנויות אלו כדי לבנות את הדור הבא של אפליקציות חכמות.

## קורסים נוספים

הצוות שלנו מציע קורסים נוספים! בדקו:

- [MCP למתחילים](https://github.com/microsoft/mcp-for-beginners)  
- [סוכני AI למתחילים](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Generative AI למתחילים באמצעות .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
- [Generative AI למתחילים באמצעות JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
- [Generative AI למתחילים](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [ML למתחילים](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
- [מדעי הנתונים למתחילים](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
- [AI למתחילים](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
- [סייבר למתחילים](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)  
- [פיתוח אתרים למתחילים](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
- [IoT למתחילים](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [פיתוח XR למתחילים](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [שליטה ב-GitHub Copilot לתכנות AI משותף](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [שליטה ב-GitHub Copilot למפתחי C#/.NET](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [בחרו את הרפתקת Copilot שלכם](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

---

