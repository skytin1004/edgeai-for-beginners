<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T21:54:38+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "he"
}
-->
# Foundry Local על Windows (מאומת)

מדריך זה מסייע לך להתקין, להפעיל ולשלב את Microsoft Foundry Local על Windows. כל השלבים והפקודות אומתו מול מסמכי Microsoft Learn.

- התחלה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started  
- ארכיטקטורה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture  
- עזרי CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli  
- שילוב SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks  
- קומפילציה של מודלים HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models  
- Windows AI: מקומי מול ענן: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers  

## 1) התקנה / שדרוג על Windows

- התקנה:  
```cmd
winget install Microsoft.FoundryLocal
```
  
- שדרוג:  
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
  
- בדיקת גרסה:  
```cmd
foundry --version
```
  

## 2) יסודות CLI (שלוש קטגוריות)

- מודל:  
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
  
- שירות:  
```cmd
foundry service --help
foundry service status
foundry service ps
```
  
- מטמון:  
```cmd
foundry cache --help
foundry cache list
```
  

הערות:  
- השירות חושף API REST תואם OpenAI. פורט נקודת הקצה מוקצה באופן דינמי; השתמש ב-`foundry service status` כדי לגלות אותו.  
- השתמש ב-SDKs לנוחות; הם מטפלים בגילוי נקודת הקצה באופן אוטומטי כאשר נתמך.  

## 3) גילוי נקודת הקצה המקומית (פורט דינמי)

Foundry Local מקצה פורט דינמי בכל פעם שהשירות מתחיל:  
```cmd
foundry service status
```
  
השתמש בכתובת `http://localhost:<PORT>` שדווחה כ-`base_url` שלך עם נתיבים תואמי OpenAI (לדוגמה, `/v1/chat/completions`).  

## 4) בדיקה מהירה באמצעות OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
  
הפניות:  
- שילוב SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks  

## 5) הבאת מודל משלך (קומפילציה עם Olive)

אם אתה זקוק למודל שאינו נמצא בקטלוג, ניתן לקמפל אותו ל-ONNX עבור Foundry Local באמצעות Olive.  

תהליך ברמה גבוהה (ראה מסמכים לשלבים):  
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
  
מסמכים:  
- קומפילציה BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models  

## 6) פתרון בעיות

- בדוק את מצב השירות ואת הלוגים:  
```cmd
foundry service status
foundry service diag
```
  
- נקה או העבר מטמון:  
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
  
- עדכן לגרסת התצוגה האחרונה:  
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
  

## 7) חוויית פיתוח קשורה ל-Windows

- בחירות AI מקומי מול ענן ב-Windows, כולל Foundry Local ו-Windows ML:  
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers  
- ערכת כלים AI של VS Code עם Foundry Local (השתמש ב-`foundry service status` כדי לקבל את כתובת נקודת הקצה של הצ'אט):  
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components  

---

