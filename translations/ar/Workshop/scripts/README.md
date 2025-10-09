<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-09T07:02:55+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "ar"
}
-->
# نصوص ورشة العمل

يحتوي هذا الدليل على نصوص الأتمتة والدعم المستخدمة للحفاظ على الجودة والاتساق عبر مواد ورشة العمل.

## المحتويات

| الملف | الغرض |
|------|-------|
| `lint_markdown_cli.py` | يتحقق من أكواد Markdown لمنع أنماط أوامر Foundry Local CLI القديمة. |
| `export_benchmark_markdown.py` | يشغل اختبارات قياس الأداء متعددة النماذج ويصدر تقارير بصيغة Markdown وJSON. |

## 1. مدقق أنماط Markdown CLI

يقوم `lint_markdown_cli.py` بفحص جميع ملفات `.md` غير المترجمة للبحث عن أنماط Foundry Local CLI المحظورة **داخل كتل الأكواد المغلقة** (``` ... ```). يمكن للنصوص التوضيحية أن تذكر الأوامر القديمة للسياق التاريخي.

### الأنماط القديمة (محظورة داخل كتل الأكواد)

يقوم المدقق بحظر أنماط CLI القديمة. استخدم البدائل الحديثة بدلاً منها.

### البدائل المطلوبة
| القديم | استخدم بدلاً منه |
|-------|------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | نصوص قياس الأداء + أدوات النظام (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### رموز الخروج
| الرمز | المعنى |
|------|--------|
| 0 | لم يتم اكتشاف أي انتهاكات |
| 1 | تم العثور على نمط أو أكثر من الأنماط القديمة |

### التشغيل محليًا
من جذر المستودع (موصى به):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### خطاف ما قبل الالتزام (اختياري)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
يمنع الالتزامات التي تحتوي على أنماط قديمة.

### تكامل CI
يقوم سير عمل GitHub Action (`.github/workflows/markdown-cli-lint.yml`) بتشغيل المدقق عند كل دفع أو طلب سحب إلى الفروع `main` و`Reactor`. يجب إصلاح الوظائف الفاشلة قبل الدمج.

### إضافة أنماط قديمة جديدة
1. افتح `lint_markdown_cli.py`.
2. أضف زوجًا `(regex, suggestion)` إلى قائمة `DEPRECATED`. استخدم سلسلة نصية خامة وقم بتضمين حدود الكلمات `\b` حيثما كان ذلك مناسبًا.
3. قم بتشغيل المدقق محليًا للتحقق من الكشف.
4. قم بالالتزام والدفع؛ سيقوم CI بفرض القاعدة الجديدة.

مثال على الإضافة:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### السماح بذكرات توضيحية
نظرًا لأن التنفيذ يتم فقط داخل كتل الأكواد المغلقة، يمكنك وصف الأوامر القديمة في النص السردي بأمان. إذا كنت *تحتاج* إلى عرضها داخل كتلة مغلقة للمقارنة، أضف كتلة مغلقة **بدون** علامات ثلاثية (مثل التراجع أو الاقتباس) أو أعد كتابتها بشكل شبه صوري.

### تخطي ملفات محددة (متقدم)
إذا لزم الأمر، قم بتغليف الأمثلة القديمة في ملف منفصل خارج المستودع أو أعد تسميته بامتداد مختلف أثناء الكتابة. يتم تخطي النسخ المترجمة تلقائيًا (المسارات التي تحتوي على `translations`).

### استكشاف الأخطاء وإصلاحها
| المشكلة | السبب | الحل |
|---------|-------|------|
| المدقق يحدد سطرًا قمت بتحديثه | النمط واسع جدًا | قم بتضييق النمط بإضافة حدود كلمات إضافية (`\b`) أو نقاط ارتكاز |
| فشل CI ولكن النجاح محليًا | إصدار Python مختلف أو تغييرات غير ملتزمة | أعد التشغيل محليًا، تأكد من أن شجرة العمل نظيفة، تحقق من إصدار Python في سير العمل (3.11) |
| الحاجة إلى تجاوز مؤقت | إصلاح عاجل | قم بتطبيق الإصلاح فورًا بعد ذلك؛ ضع في اعتبارك استخدام فرع مؤقت وطلب سحب متابعة (تجنب إضافة مفاتيح تجاوز) |

### المبرر
الحفاظ على الوثائق متوافقة مع واجهة CLI المستقرة *الحالية* يمنع الاحتكاك في الورشة، ويجنب ارتباك المتعلمين، ويركز قياس الأداء من خلال نصوص Python المحدثة بدلاً من أوامر CLI المتغيرة.

---
يتم الحفاظ عليه كجزء من أدوات جودة الورشة. لتحسينات (مثل اقتراحات الإصلاح التلقائي أو إنشاء تقارير HTML)، افتح قضية أو قدم طلب سحب.

## 2. نص التحقق من العينات

يقوم `validate_samples.py` بالتحقق من جميع ملفات العينات Python للتأكد من صحة بناء الجملة، الواردات، والامتثال لأفضل الممارسات.

### الاستخدام
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### ما الذي يتحقق منه
- ✅ صحة بناء الجملة في Python
- ✅ وجود الواردات المطلوبة
- ✅ تنفيذ معالجة الأخطاء (وضع تفصيلي)
- ✅ استخدام التلميحات النوعية (وضع تفصيلي)
- ✅ توثيق الوظائف (وضع تفصيلي)
- ✅ روابط مرجعية لـ SDK (وضع تفصيلي)

### متغيرات البيئة
- `SKIP_IMPORT_CHECK=1` - تخطي التحقق من الواردات
- `SKIP_SYNTAX_CHECK=1` - تخطي التحقق من بناء الجملة

### رموز الخروج
- `0` - جميع العينات اجتازت التحقق
- `1` - فشلت عينة واحدة أو أكثر

## 3. مشغل اختبار العينات

يقوم `test_samples.py` بتشغيل اختبارات أولية على جميع العينات للتحقق من أنها تعمل بدون أخطاء.

### الاستخدام
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### المتطلبات الأساسية
- تشغيل خدمة Foundry Local: `foundry service start`
- تحميل النماذج: `foundry model run phi-4-mini`
- تثبيت التبعيات: `pip install -r requirements.txt`

### ما الذي يختبره
- ✅ يمكن للعينات التنفيذ بدون أخطاء وقت التشغيل
- ✅ يتم إنشاء المخرجات المطلوبة
- ✅ معالجة الأخطاء بشكل صحيح عند الفشل
- ✅ الأداء (وقت التنفيذ)

### متغيرات البيئة
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - النموذج المستخدم للاختبار
- `TEST_TIMEOUT=30` - المهلة لكل عينة بالثواني

### حالات الفشل المتوقعة
قد تفشل بعض الاختبارات إذا لم يتم تثبيت التبعيات الاختيارية (مثل `ragas`, `sentence-transformers`). قم بالتثبيت باستخدام:
```bash
pip install sentence-transformers ragas datasets
```

### رموز الخروج
- `0` - جميع الاختبارات اجتازت
- `1` - فشل اختبار واحد أو أكثر

## 4. مُصدر Markdown لقياس الأداء

النص: `export_benchmark_markdown.py`

يُنشئ جدول أداء قابل للتكرار لمجموعة من النماذج.

### الاستخدام
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### المخرجات
| الملف | الوصف |
|------|-------|
| `benchmark_report.md` | جدول Markdown (المتوسط، p95، الرموز/الثانية، أول رمز اختياري) |
| `benchmark_report.json` | مصفوفة المقاييس الخام للمقارنة والتاريخ |

### الخيارات
| العلم | الوصف | الافتراضي |
|------|-------|----------|
| `--models` | أسماء النماذج مفصولة بفواصل | (مطلوب) |
| `--prompt` | النص المستخدم في كل جولة | (مطلوب) |
| `--rounds` | الجولات لكل نموذج | 3 |
| `--output` | ملف إخراج Markdown | `benchmark_report.md` |
| `--json` | ملف إخراج JSON | `benchmark_report.json` |
| `--fail-on-empty` | خروج غير صفري إذا فشلت جميع القياسات | معطل |

متغير البيئة `BENCH_STREAM=1` يضيف قياس زمن أول رمز.

### ملاحظات
- يعيد استخدام `workshop_utils` لتوحيد إعداد النماذج والتخزين المؤقت.
- إذا تم تشغيله من دليل عمل مختلف، يحاول النص إيجاد مسارات بديلة لتحديد موقع `workshop_utils`.
- للمقارنة بين وحدات معالجة الرسومات: قم بالتشغيل مرة واحدة، قم بتمكين التسريع عبر إعدادات CLI، أعد التشغيل وقارن JSON.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.