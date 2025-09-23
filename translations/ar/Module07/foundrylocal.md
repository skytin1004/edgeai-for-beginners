<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T14:26:44+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "ar"
}
-->
# Foundry Local على ويندوز (تم التحقق)

هذا الدليل يساعدك في تثبيت وتشغيل ودمج Microsoft Foundry Local على نظام ويندوز. جميع الخطوات والأوامر تم التحقق منها وفقًا لوثائق Microsoft Learn.

- البدء: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- الهندسة المعمارية: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- مرجع CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- دمج SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- تجميع نماذج HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: محلي مقابل السحابة: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) التثبيت / الترقية على ويندوز

- التثبيت:
```cmd
winget install Microsoft.FoundryLocal
```
- الترقية:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- التحقق من الإصدار:
```cmd
foundry --version
```

## 2) أساسيات CLI (ثلاث فئات)

- النموذج:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- الخدمة:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- التخزين المؤقت:
```cmd
foundry cache --help
foundry cache list
```

ملاحظات:
- الخدمة توفر واجهة REST API متوافقة مع OpenAI. يتم تخصيص منفذ نقطة النهاية ديناميكيًا؛ استخدم `foundry service status` لاكتشافه.
- استخدم SDKs للراحة؛ فهي تتعامل مع اكتشاف نقطة النهاية تلقائيًا حيثما كان ذلك مدعومًا.

## 3) اكتشاف نقطة النهاية المحلية (المنفذ الديناميكي)

يقوم Foundry Local بتخصيص منفذ ديناميكي في كل مرة يتم فيها بدء الخدمة:
```cmd
foundry service status
```
استخدم `http://localhost:<PORT>` المبلغ عنه كـ `base_url` مع المسارات المتوافقة مع OpenAI (على سبيل المثال، `/v1/chat/completions`).

## 4) اختبار سريع عبر OpenAI Python SDK

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
المراجع:
- دمج SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) استخدم النموذج الخاص بك (تجميع باستخدام Olive)

إذا كنت بحاجة إلى نموذج غير موجود في الكتالوج، قم بتجميعه إلى ONNX لـ Foundry Local باستخدام Olive.

التدفق العام (راجع الوثائق للخطوات):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
الوثائق:
- تجميع BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) استكشاف الأخطاء وإصلاحها

- تحقق من حالة الخدمة والسجلات:
```cmd
foundry service status
foundry service diag
```
- مسح أو نقل التخزين المؤقت:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- التحديث إلى أحدث معاينة:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) تجربة المطورين ذات الصلة بويندوز

- خيارات الذكاء الاصطناعي المحلي مقابل السحابة على ويندوز، بما في ذلك Foundry Local و Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- أدوات الذكاء الاصطناعي في VS Code مع Foundry Local (استخدم `foundry service status` للحصول على عنوان URL لنقطة نهاية الدردشة):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

