<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb6eadc312d5658a0cd71c0085b43742",
  "translation_date": "2025-09-22T21:38:07+00:00",
  "source_file": "Module07/README.md",
  "language_code": "he"
}
-->
# פרק 07: דוגמאות ל-EdgeAI

Edge AI מייצג את השילוב בין בינה מלאכותית למחשוב קצה, ומאפשר עיבוד חכם ישירות על מכשירים ללא תלות בחיבור לענן. פרק זה מציג חמישה יישומים שונים של EdgeAI בפלטפורמות ובמסגרות שונות, המדגימים את הגמישות והעוצמה של הפעלת מודלים של AI בקצה.

## 1. EdgeAI ב-NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano מייצג פריצת דרך במחשוב קצה AI נגיש, ומספק עד 67 TOPS של ביצועי AI בפלטפורמה קומפקטית בגודל כרטיס אשראי. פלטפורמת Edge AI עוצמתית זו מנגישה את פיתוח ה-AI הגנרטיבי לחובבים, סטודנטים ומפתחים מקצועיים כאחד.

### תכונות עיקריות
- מספק עד 67 TOPS של ביצועי AI—שיפור של פי 1.7 לעומת הדור הקודם
- 1024 ליבות CUDA ועד 32 ליבות Tensor לעיבוד AI
- מעבד 6 ליבות Arm Cortex-A78AE v8.2 64-bit עם תדר מקסימלי של 1.5 GHz
- מחיר של $249 בלבד, מה שהופך אותו לפלטפורמה נגישה ומשתלמת למפתחים, סטודנטים ויוצרים

### יישומים
Jetson Orin Nano מצטיין בהרצת מודלים גנרטיביים מודרניים כמו Vision Transformers, מודלים של שפה גדולה (LLMs) ומודלים של שפה-חזון. הוא תוכנן במיוחד עבור שימושים ב-GenAI, וכעת ניתן להריץ מספר LLMs על מכשיר בגודל כף יד. שימושים פופולריים כוללים רובוטיקה מבוססת AI, רחפנים חכמים, מצלמות אינטליגנטיות ומכשירי קצה אוטונומיים.

**למידע נוסף**: [Jetson Orin Nano של NVIDIA: הדבר הגדול הבא ב-EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI באפליקציות מובייל עם .NET MAUI ו-ONNX Runtime GenAI

הפתרון הזה מדגים כיצד לשלב AI גנרטיבי ומודלים של שפה גדולה (LLMs) באפליקציות מובייל חוצות פלטפורמות באמצעות .NET MAUI (Multi-platform App UI) ו-ONNX Runtime GenAI. גישה זו מאפשרת למפתחי .NET לבנות אפליקציות מובייל מתקדמות מבוססות AI שפועלות באופן טבעי על מכשירי Android ו-iOS.

### תכונות עיקריות
- מבוסס על מסגרת .NET MAUI, המספקת בסיס קוד יחיד לאפליקציות Android ו-iOS
- שילוב ONNX Runtime GenAI מאפשר הרצת מודלים גנרטיביים ישירות על מכשירי מובייל
- תומך במאיצי חומרה שונים המותאמים למכשירי מובייל, כולל CPU, GPU ומעבדי AI ייעודיים
- אופטימיזציות ספציפיות לפלטפורמה כמו CoreML ל-iOS ו-NNAPI ל-Android באמצעות ONNX Runtime
- מיישם את הלולאה המלאה של AI גנרטיבי כולל עיבוד מקדים ומאוחר, הסקה, עיבוד לוגיטים, חיפוש ודגימה, וניהול מטמון KV

### יתרונות פיתוח
הגישה של .NET MAUI מאפשרת למפתחים לנצל את כישורי ה-C# ו-.NET הקיימים שלהם תוך בניית אפליקציות AI חוצות פלטפורמות. מסגרת ONNX Runtime GenAI תומכת בארכיטקטורות מודלים רבות כולל Llama, Mistral, Phi, Gemma ועוד. ליבות ARM64 מותאמות מאיצות כפל מטריצות INT4 כמותי, ומבטיחות ביצועים יעילים על חומרת מובייל תוך שמירה על חוויית פיתוח מוכרת ב-.NET.

### שימושים
פתרון זה אידיאלי למפתחים שרוצים לבנות אפליקציות מובייל מבוססות AI באמצעות טכנולוגיות .NET, כולל צ'אטבוטים אינטליגנטיים, אפליקציות זיהוי תמונה, כלי תרגום שפה ומערכות המלצה מותאמות אישית שפועלות כולן על המכשיר לשיפור פרטיות ויכולת עבודה במצב לא מקוון.

**למידע נוסף**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI ב-Azure עם מנוע מודלים קטנים

הפתרון של EdgeAI מבוסס Azure של Microsoft מתמקד בפריסה יעילה של מודלים קטנים (SLMs) בסביבות היברידיות של ענן-קצה. גישה זו מגשרת על הפער בין שירותי AI בקנה מידה ענני לדרישות פריסה בקצה.

### יתרונות ארכיטקטורה
- שילוב חלק עם שירותי Azure AI
- הרצת SLMs/LLMs ומודלים רב-מודאליים על המכשיר ובענן באמצעות ONNX Runtime
- מותאם לפריסה בקנה מידה ארגוני
- תמיכה בעדכונים וניהול מתמשכים של מודלים

### שימושים
היישום של Azure EdgeAI מצטיין בתרחישים הדורשים פריסת AI ברמה ארגונית עם יכולות ניהול ענן. זה כולל עיבוד מסמכים אינטליגנטי, ניתוח בזמן אמת וזרימות עבודה היברידיות של AI המנצלות גם את מחשוב הענן וגם את מחשוב הקצה.

**למידע נוסף**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI עם Windows ML

Windows ML מייצג את סביבת הריצה המתקדמת של Microsoft, המותאמת להסקת מודלים על המכשיר ולפריסה פשוטה, ומהווה את הבסיס ל-Windows AI Foundry. פלטפורמה זו מאפשרת למפתחים ליצור אפליקציות Windows מבוססות AI המנצלות את מלוא יכולות החומרה של מחשבי PC.

### יכולות פלטפורמה
- פועל על כל מחשבי Windows 11 עם גרסה 24H2 (build 26100) או יותר
- תומך בכל חומרת PC x64 ו-ARM64, כולל מחשבים ללא NPUs או GPUs
- מאפשר למפתחים להביא את המודלים שלהם ולפרוס אותם ביעילות על פני אקוסיסטם השותפים של הסיליקון כולל AMD, Intel, NVIDIA ו-Qualcomm, המשתרעים על CPU, GPU, NPU
- באמצעות APIs תשתיתיים, מפתחים אינם צריכים ליצור גרסאות מרובות של האפליקציה שלהם כדי להתאים לסיליקון שונה

### יתרונות למפתחים
Windows ML מפשט את החומרה וספקי הביצוע, כך שתוכלו להתמקד בכתיבת הקוד שלכם. בנוסף, Windows ML מתעדכן אוטומטית לתמוך ב-NPUs, GPUs ו-CPUs החדשים ביותר עם שחרורם. הפלטפורמה מספקת מסגרת אחידה לפיתוח AI על פני אקוסיסטם החומרה המגוון של Windows.

**למידע נוסף**: 
- [סקירה כללית של Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [מדריך פיתוח EdgeAI ל-Windows](../windowdeveloper.md) - מדריך מקיף לפיתוח Edge AI ב-Windows

## 5. EdgeAI עם Foundry Local Applications

Foundry Local מאפשר למפתחים לבנות אפליקציות RAG (Retrieval Augmented Generation) באמצעות משאבים מקומיים ב-.NET, ומשלב מודלים של שפה מקומית עם יכולות חיפוש סמנטי. גישה זו מספקת פתרונות AI ממוקדי פרטיות שפועלים לחלוטין על תשתית מקומית.

### ארכיטקטורה טכנית
- משלב את מודל השפה Phi, Embeddings מקומיים ו-Semantic Kernel ליצירת תרחיש RAG
- משתמש ב-embeddings כוקטורים (מערכים) של ערכים בנקודה צפה המייצגים תוכן ומשמעות סמנטית שלו
- Semantic Kernel משמש כמתזמר הראשי, ומשלב את Phi ו-Smart Components ליצירת צינור RAG חלק
- תמיכה בבסיסי נתונים וקטוריים מקומיים כולל SQLite ו-Qdrant

### יתרונות יישום
RAG, או Retrieval Augmented Generation, הוא פשוט דרך מתוחכמת לומר "חפש מידע והכנס אותו לפרומפט". יישום מקומי זה מבטיח פרטיות נתונים תוך מתן תגובות אינטליגנטיות המבוססות על בסיסי ידע מותאמים אישית. הגישה חשובה במיוחד לתרחישים ארגוניים הדורשים ריבונות נתונים ויכולת עבודה במצב לא מקוון.

**למידע נוסף**: [דוגמאות Foundry Local RAG](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local מספק שרת REST תואם OpenAI המופעל על ידי ONNX Runtime להרצת מודלים באופן מקומי על Windows. להלן סיכום מהיר ומאומת; ראו את התיעוד הרשמי לפרטים מלאים.

- התחלה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- ארכיטקטורה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- הפניה CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- מדריך Windows מלא במאגר זה: [foundrylocal.md](./foundrylocal.md)

התקנה או שדרוג ב-Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

חקור קטגוריות CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

הרץ מודל וגלה את נקודת הקצה הדינמית:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

בדיקת REST מהירה לרשימת מודלים (החלף PORT מסטטוס):
```cmd
curl -s http://localhost:PORT/v1/models
```

טיפים:
- אינטגרציה SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- הבאת מודל משלך (קומפילציה): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## משאבי פיתוח EdgeAI ל-Windows

עבור מפתחים המתמקדים בפלטפורמת Windows, יצרנו מדריך מקיף המכסה את כל אקוסיסטם EdgeAI של Windows. משאב זה מספק מידע מפורט על Windows AI Foundry, כולל APIs, כלים ושיטות עבודה מומלצות לפיתוח EdgeAI ב-Windows.

### פלטפורמת Windows AI Foundry
פלטפורמת Windows AI Foundry מספקת מערך כלים ו-APIs מקיף המיועד במיוחד לפיתוח Edge AI על מכשירי Windows. זה כולל תמיכה מיוחדת בחומרה מואצת NPU, אינטגרציה של Windows ML וטכניקות אופטימיזציה ספציפיות לפלטפורמה.

**מדריך מקיף**: [מדריך פיתוח EdgeAI ל-Windows](../windowdeveloper.md)

מדריך זה מכסה:
- סקירה כללית של פלטפורמת Windows AI Foundry ורכיביה
- API Phi Silica להסקה יעילה על חומרת NPU
- APIs לראייה ממוחשבת לעיבוד תמונה ו-OCR
- אינטגרציה ואופטימיזציה של סביבת הריצה Windows ML
- CLI Foundry Local לפיתוח ובדיקה מקומיים
- אסטרטגיות אופטימיזציה חומרתית למכשירי Windows
- דוגמאות יישום מעשיות ושיטות עבודה מומלצות

### ערכת כלים ל-AI לפיתוח Edge AI
עבור מפתחים המשתמשים ב-Visual Studio Code, הרחבת AI Toolkit מספקת סביבת פיתוח מקיפה המיועדת במיוחד לבנייה, בדיקה ופריסה של אפליקציות Edge AI. ערכת כלים זו מייעלת את כל זרימת העבודה של פיתוח Edge AI בתוך VS Code.

**מדריך פיתוח**: [ערכת כלים ל-AI לפיתוח Edge AI](../aitoolkit.md)

מדריך ערכת הכלים מכסה:
- גילוי ובחירת מודלים לפריסה בקצה
- זרימות עבודה של בדיקה ואופטימיזציה מקומיות
- אינטגרציה של ONNX ו-Ollama למודלים בקצה
- טכניקות המרה וכימות מודלים
- פיתוח סוכנים לתרחישי קצה
- הערכת ביצועים ומעקב
- הכנה לפריסה ושיטות עבודה מומלצות

## סיכום

חמשת היישומים של EdgeAI הללו מדגימים את הבשלות והמגוון של פתרונות AI בקצה הזמינים כיום. ממכשירי קצה מואצים חומרתית כמו Jetson Orin Nano ועד מסגרות תוכנה כמו ONNX Runtime GenAI ו-Windows ML, למפתחים יש אפשרויות חסרות תקדים לפריסת אפליקציות אינטליגנטיות בקצה.

החוט המקשר בין כל הפלטפורמות הללו הוא הנגשת יכולות AI, מה שהופך את הלמידה המכונה המתקדמת לנגישה למפתחים ברמות מיומנות ושימושים שונים. בין אם מדובר בבניית אפליקציות מובייל, תוכנות שולחניות או מערכות משובצות, פתרונות EdgeAI אלו מספקים את הבסיס לדור הבא של אפליקציות אינטליגנטיות שפועלות ביעילות ובפרטיות בקצה.

כל פלטפורמה מציעה יתרונות ייחודיים: Jetson Orin Nano למחשוב קצה מואץ חומרתית, ONNX Runtime GenAI לפיתוח מובייל חוצה פלטפורמות, Azure EdgeAI לאינטגרציה ענן-קצה ארגונית, Windows ML לאפליקציות מקוריות ל-Windows, ו-Foundry Local ליישומי RAG ממוקדי פרטיות. יחד, הן מייצגות אקוסיסטם מקיף לפיתוח EdgeAI.

---

