<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T14:27:07+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "ur"
}
-->
# ونڈوز پر فاؤنڈری لوکل (تصدیق شدہ)

یہ گائیڈ آپ کو ونڈوز پر Microsoft Foundry Local انسٹال، چلانے اور انٹیگریٹ کرنے میں مدد دیتی ہے۔ تمام مراحل اور کمانڈز Microsoft Learn ڈاکیومنٹس کے مطابق تصدیق شدہ ہیں۔

- شروعات کریں: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- آرکیٹیکچر: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI حوالہ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs انٹیگریٹ کریں: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF ماڈلز کمپائل کریں (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- ونڈوز AI: لوکل بمقابلہ کلاؤڈ: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) ونڈوز پر انسٹال / اپ گریڈ کریں

- انسٹال:
```cmd
winget install Microsoft.FoundryLocal
```
- اپ گریڈ:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- ورژن چیک کریں:
```cmd
foundry --version
```


## 2) CLI بنیادی باتیں (تین کیٹیگریز)

- ماڈل:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- سروس:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- کیش:
```cmd
foundry cache --help
foundry cache list
```


نوٹس:
- سروس ایک OpenAI-مطابق REST API فراہم کرتی ہے۔ اینڈ پوائنٹ پورٹ ڈائنامکلی الاٹ کیا جاتا ہے؛ اسے دریافت کرنے کے لیے `foundry service status` استعمال کریں۔
- سہولت کے لیے SDKs استعمال کریں؛ یہ سپورٹڈ جگہوں پر اینڈ پوائنٹ دریافت خودکار طور پر ہینڈل کرتے ہیں۔

## 3) لوکل اینڈ پوائنٹ دریافت کریں (ڈائنامک پورٹ)

فاؤنڈری لوکل ہر بار سروس شروع ہونے پر ایک ڈائنامک پورٹ الاٹ کرتا ہے:
```cmd
foundry service status
```
رپورٹ شدہ `http://localhost:<PORT>` کو OpenAI-مطابق راستوں کے ساتھ اپنے `base_url` کے طور پر استعمال کریں (مثال کے طور پر، `/v1/chat/completions`)۔

## 4) OpenAI Python SDK کے ذریعے فوری ٹیسٹ

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
حوالہ جات:
- SDK انٹیگریشن: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) اپنا ماڈل لائیں (Olive کے ساتھ کمپائل کریں)

اگر آپ کو کیٹلاگ میں موجود ماڈل کی ضرورت نہیں ہے، تو اسے Olive کے ذریعے ONNX میں فاؤنڈری لوکل کے لیے کمپائل کریں۔

اعلی سطحی فلو (مراحل کے لیے ڈاکیومنٹس دیکھیں):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ڈاکیومنٹس:
- BYOM کمپائل: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) خرابیوں کا ازالہ

- سروس اسٹیٹس اور لاگز چیک کریں:
```cmd
foundry service status
foundry service diag
```
- کیش صاف کریں یا منتقل کریں:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- تازہ ترین پریویو پر اپ ڈیٹ کریں:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```


## 7) متعلقہ ونڈوز ڈویلپر تجربہ

- ونڈوز لوکل بمقابلہ کلاؤڈ AI کے انتخاب، بشمول Foundry Local اور Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS کوڈ AI ٹول کٹ کے ساتھ Foundry Local (چیٹ اینڈ پوائنٹ URL حاصل کرنے کے لیے `foundry service status` استعمال کریں):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

