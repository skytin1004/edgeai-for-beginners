<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:22:54+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ar"
}
-->
# AGENTS.md

## نظرة عامة على المشروع

EdgeAI للمبتدئين هو مستودع تعليمي شامل يهدف إلى تعليم تطوير الذكاء الاصطناعي الطرفي باستخدام نماذج اللغة الصغيرة (SLMs). يغطي هذا المسار أساسيات EdgeAI، نشر النماذج، تقنيات تحسين الأداء، وتنفيذات جاهزة للإنتاج باستخدام Microsoft Foundry Local ومجموعة متنوعة من أطر الذكاء الاصطناعي.

**التقنيات الرئيسية:**
- Python 3.8+ (اللغة الأساسية لعينات الذكاء الاصطناعي/تعلم الآلة)
- .NET C# (عينات الذكاء الاصطناعي/تعلم الآلة)
- JavaScript/Node.js مع Electron (لتطبيقات سطح المكتب)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- أطر الذكاء الاصطناعي: LangChain، Semantic Kernel، Chainlit
- تحسين النماذج: Llama.cpp، Microsoft Olive، OpenVINO، Apple MLX

**نوع المستودع:** مستودع محتوى تعليمي يحتوي على 8 وحدات و10 تطبيقات نموذجية شاملة

**الهيكلية:** مسار تعلم متعدد الوحدات مع عينات عملية توضح أنماط نشر الذكاء الاصطناعي الطرفي

## هيكل المستودع

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

## أوامر الإعداد

### إعداد المستودع

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### إعداد عينات Python (الوحدة 08 وعينات Python)

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

### إعداد عينات Node.js (العينة 08 - تطبيق الدردشة على Windows)

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

### إعداد Foundry Local

يتطلب تشغيل عينات الوحدة 08 وجود Foundry Local:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## سير العمل التطويري

### تطوير المحتوى

يحتوي هذا المستودع بشكل أساسي على **محتوى تعليمي مكتوب بلغة Markdown**. عند إجراء تغييرات:

1. قم بتحرير ملفات `.md` في أدلة الوحدات المناسبة
2. اتبع أنماط التنسيق الحالية
3. تأكد من دقة واختبار أمثلة التعليمات البرمجية
4. قم بتحديث المحتوى المترجم المقابل إذا لزم الأمر (أو دع الأتمتة تتولى ذلك)

### تطوير تطبيقات العينات

بالنسبة لعينات Python (العينات 01-07، 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

بالنسبة لعينة Electron (العينة 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### اختبار تطبيقات العينات

عينات Python لا تحتوي على اختبارات آلية ولكن يمكن التحقق منها عن طريق تشغيلها:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

عينة Electron تحتوي على بنية اختبار:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## تعليمات الاختبار

### التحقق من المحتوى

يستخدم المستودع سير عمل ترجمة آلي. لا يتطلب اختبار يدوي للترجمات.

**التحقق اليدوي لتغييرات المحتوى:**
1. قم بمراجعة عرض Markdown عن طريق معاينة ملفات `.md`
2. تحقق من أن جميع الروابط تشير إلى أهداف صالحة
3. اختبر أي مقتطفات تعليمات برمجية مضمنة في الوثائق
4. تأكد من تحميل الصور بشكل صحيح

### اختبار تطبيقات العينات

**Module08/samples/08 (تطبيق Electron) يحتوي على اختبارات شاملة:**
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

**يجب اختبار عينات Python يدويًا:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## إرشادات نمط التعليمات البرمجية

### محتوى Markdown

- استخدم تسلسل هرمي متسق للعناوين (# للعنوان، ## للأقسام الرئيسية، ### للأقسام الفرعية)
- قم بتضمين كتل التعليمات البرمجية مع محددات اللغة: ```python، ```bash، ```javascript
- اتبع التنسيق الحالي للجداول، القوائم، والتأكيد
- اجعل الأسطر قابلة للقراءة (هدف ~80-100 حرف، ولكن ليس بشكل صارم)
- استخدم الروابط النسبية للإشارات الداخلية

### نمط تعليمات Python البرمجية

- اتبع اتفاقيات PEP 8
- استخدم تلميحات النوع حيثما كان ذلك مناسبًا
- قم بتضمين docstrings للوظائف والفئات
- استخدم أسماء متغيرات ذات معنى
- اجعل الوظائف مركزة وموجزة

### نمط تعليمات JavaScript/Node.js البرمجية

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**الاتفاقيات الرئيسية:**
- تكوين ESLint متوفر في العينة 08
- Prettier لتنسيق التعليمات البرمجية
- استخدم بناء الجملة الحديث ES6+
- اتبع الأنماط الحالية في قاعدة التعليمات البرمجية

## إرشادات طلب السحب

### تنسيق العنوان
```
[ModuleXX] Brief description of change
```
أو
```
[Module08/samples/XX] Description for sample changes
```

### قبل الإرسال

**لتغييرات المحتوى:**
- قم بمعاينة جميع ملفات Markdown المعدلة
- تحقق من عمل الروابط والصور
- تحقق من الأخطاء الإملائية والنحوية

**لتغييرات التعليمات البرمجية لعينة (Module08/samples/08):**
```bash
npm run lint
npm test
```

**لتغييرات عينات Python:**
- اختبر تشغيل العينة بنجاح
- تحقق من عمل معالجة الأخطاء
- تحقق من التوافق مع Foundry Local

### عملية المراجعة

- يتم مراجعة تغييرات المحتوى التعليمي من حيث الدقة والوضوح
- يتم اختبار عينات التعليمات البرمجية من حيث الوظائف
- يتم التعامل مع تحديثات الترجمة تلقائيًا بواسطة GitHub Actions

## نظام الترجمة

**هام:** يستخدم هذا المستودع ترجمة آلية عبر GitHub Actions.

- توجد الترجمات في دليل `/translations/` (50+ لغة)
- يتم تنفيذها تلقائيًا عبر سير عمل `co-op-translator.yml`
- **لا تقم بتحرير ملفات الترجمة يدويًا** - سيتم الكتابة فوقها
- قم بتحرير ملفات المصدر الإنجليزية فقط في الدليل الرئيسي وأدلة الوحدات
- يتم إنشاء الترجمات تلقائيًا عند الدفع إلى الفرع `main`

## تكامل Foundry Local

تتطلب معظم عينات الوحدة 08 تشغيل Microsoft Foundry Local:

### بدء تشغيل Foundry Local
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

### التحقق من Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### متغيرات البيئة للعينات

تستخدم معظم العينات هذه المتغيرات البيئية:
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

## البناء والنشر

### نشر المحتوى

هذا المستودع هو في الأساس وثائق - لا توجد عملية بناء مطلوبة للمحتوى.

### بناء تطبيقات العينات

**تطبيق Electron (Module08/samples/08):**
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

**عينات Python:**
لا توجد عملية بناء - يتم تشغيل العينات مباشرة باستخدام مترجم Python.

## المشكلات الشائعة واستكشاف الأخطاء وإصلاحها

### Foundry Local غير قيد التشغيل
**المشكلة:** فشل العينات مع أخطاء الاتصال

**الحل:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### مشكلات بيئة Python الافتراضية
**المشكلة:** أخطاء استيراد الوحدات

**الحل:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### مشكلات بناء Electron
**المشكلة:** فشل npm install أو البناء

**الحل:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### تعارضات سير عمل الترجمة
**المشكلة:** تعارض طلبات السحب الخاصة بالترجمة مع تغييراتك

**الحل:**
- قم بتحرير ملفات المصدر الإنجليزية فقط
- دع سير عمل الترجمة الآلي يتولى الترجمة
- إذا حدثت تعارضات، قم بدمج `main` في فرعك بعد دمج الترجمات

## موارد إضافية

### مسارات التعلم
- **مسار المبتدئين:** الوحدات 01-02 (7-9 ساعات)
- **المسار المتوسط:** الوحدات 03-04 (9-11 ساعات)
- **المسار المتقدم:** الوحدات 05-07 (12-15 ساعات)
- **مسار الخبراء:** الوحدة 08 (8-10 ساعات)

### محتوى الوحدات الرئيسية
- **Module01:** أساسيات EdgeAI ودراسات حالة من العالم الحقيقي
- **Module02:** عائلات نماذج اللغة الصغيرة (SLM) والهياكل
- **Module03:** استراتيجيات النشر المحلي والسحابي
- **Module04:** تحسين النماذج باستخدام أطر متعددة
- **Module05:** SLMOps - عمليات الإنتاج
- **Module06:** وكلاء الذكاء الاصطناعي واستدعاء الوظائف
- **Module07:** تنفيذات خاصة بالمنصات
- **Module08:** أدوات Foundry Local مع 10 عينات شاملة

### التبعيات الخارجية
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - تشغيل نماذج الذكاء الاصطناعي محليًا
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - إطار تحسين الأداء
- [Microsoft Olive](https://microsoft.github.io/Olive/) - مجموعة أدوات تحسين النماذج
- [OpenVINO](https://docs.openvino.ai/) - مجموعة أدوات تحسين الأداء من Intel

## ملاحظات خاصة بالمشروع

### تطبيقات عينات الوحدة 08

يتضمن المستودع 10 تطبيقات نموذجية شاملة:

1. **01-REST Chat Quickstart** - تكامل أساسي مع OpenAI SDK
2. **02-OpenAI SDK Integration** - ميزات متقدمة لـ SDK
3. **03-Model Discovery & Benchmarking** - أدوات مقارنة النماذج
4. **04-Chainlit RAG Application** - إنشاء معزز بالاسترجاع
5. **05-Multi-Agent Orchestration** - تنسيق الوكلاء الأساسي
6. **06-Models-as-Tools Router** - توجيه النماذج الذكي
7. **07-Direct API Client** - تكامل API منخفض المستوى
8. **08-Windows 11 Chat App** - تطبيق سطح مكتب Electron أصلي
9. **09-Advanced Multi-Agent System** - تنسيق وكلاء معقد
10. **10-Foundry Tools Framework** - تكامل LangChain/Semantic Kernel

كل عينة توضح جوانب مختلفة من تطوير الذكاء الاصطناعي الطرفي باستخدام Foundry Local.

### اعتبارات الأداء

- تم تحسين SLMs للنشر الطرفي (2-16GB RAM)
- يوفر الاستدلال المحلي أوقات استجابة تتراوح بين 50-500ms
- تقنيات التكميم تحقق تقليل الحجم بنسبة 75% مع الاحتفاظ بنسبة 85% من الأداء
- قدرات المحادثة في الوقت الحقيقي مع النماذج المحلية

### الأمان والخصوصية

- تتم جميع المعالجة محليًا - لا يتم إرسال البيانات إلى السحابة
- مناسب للتطبيقات الحساسة للخصوصية (الرعاية الصحية، المالية)
- يلبي متطلبات سيادة البيانات
- يعمل Foundry Local بالكامل على الأجهزة المحلية

---

**هذا مستودع تعليمي يركز على تعليم تطوير الذكاء الاصطناعي الطرفي. النمط الأساسي للمساهمة هو تحسين المحتوى التعليمي وإضافة/تعزيز تطبيقات العينات التي توضح مفاهيم الذكاء الاصطناعي الطرفي.**

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.