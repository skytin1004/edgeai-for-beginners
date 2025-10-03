<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:23:54+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ur"
}
-->
# AGENTS.md

## پروجیکٹ کا جائزہ

EdgeAI for Beginners ایک جامع تعلیمی ذخیرہ ہے جو چھوٹے زبان ماڈلز (SLMs) کے ساتھ Edge AI کی ترقی سکھاتا ہے۔ یہ کورس EdgeAI کی بنیادی باتیں، ماڈل کی تعیناتی، اصلاحی تکنیک، اور Microsoft Foundry Local اور مختلف AI فریم ورک کے استعمال سے پروڈکشن کے لیے تیار نفاذات کا احاطہ کرتا ہے۔

**اہم ٹیکنالوجیز:**
- Python 3.8+ (AI/ML نمونوں کے لیے بنیادی زبان)
- .NET C# (AI/ML نمونوں کے لیے)
- JavaScript/Node.js کے ساتھ Electron (ڈیسک ٹاپ ایپلیکیشنز کے لیے)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI فریم ورک: LangChain، Semantic Kernel، Chainlit
- ماڈل کی اصلاح: Llama.cpp، Microsoft Olive، OpenVINO، Apple MLX

**ذخیرہ کی قسم:** تعلیمی مواد کا ذخیرہ جس میں 8 ماڈیولز اور 10 جامع نمونہ ایپلیکیشنز شامل ہیں

**آرکیٹیکچر:** عملی نمونوں کے ساتھ کثیر ماڈیول سیکھنے کا راستہ جو Edge AI کی تعیناتی کے نمونوں کو ظاہر کرتا ہے

## ذخیرہ کی ساخت

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

## سیٹ اپ کمانڈز

### ذخیرہ کی سیٹ اپ

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python نمونہ سیٹ اپ (Module08 اور Python نمونے)

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

### Node.js نمونہ سیٹ اپ (نمونہ 08 - Windows چیٹ ایپ)

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

### Foundry Local سیٹ اپ

Module08 کے نمونوں کو چلانے کے لیے Foundry Local کی ضرورت ہے:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## ترقیاتی ورک فلو

### مواد کی ترقی

یہ ذخیرہ بنیادی طور پر **Markdown تعلیمی مواد** پر مشتمل ہے۔ تبدیلیاں کرتے وقت:

1. مناسب ماڈیول ڈائریکٹریز میں `.md` فائلوں میں ترمیم کریں
2. موجودہ فارمیٹنگ کے نمونوں کی پیروی کریں
3. کوڈ کے نمونے درست اور آزمائے ہوئے ہونے کو یقینی بنائیں
4. اگر ضروری ہو تو متعلقہ ترجمہ شدہ مواد کو اپ ڈیٹ کریں (یا خودکار نظام کو اس کا خیال رکھنے دیں)

### نمونہ ایپلیکیشن کی ترقی

Python نمونوں کے لیے (نمونے 01-07، 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron نمونہ کے لیے (نمونہ 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### نمونہ ایپلیکیشنز کی جانچ

Python نمونوں کے لیے خودکار ٹیسٹ نہیں ہیں لیکن انہیں چلانے سے تصدیق کی جا سکتی ہے:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron نمونہ کے پاس ٹیسٹ انفراسٹرکچر موجود ہے:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## جانچ کی ہدایات

### مواد کی تصدیق

ذخیرہ خودکار ترجمہ ورک فلو استعمال کرتا ہے۔ ترجموں کے لیے کوئی دستی جانچ کی ضرورت نہیں۔

**مواد کی تبدیلیوں کے لیے دستی تصدیق:**
1. `.md` فائلوں کو پیش نظارہ کرکے Markdown رینڈرنگ کا جائزہ لیں
2. تصدیق کریں کہ تمام لنکس درست مقامات کی طرف اشارہ کرتے ہیں
3. دستاویزات میں شامل کوڈ کے نمونوں کو آزمائیں
4. چیک کریں کہ تصاویر صحیح طریقے سے لوڈ ہو رہی ہیں

### نمونہ ایپلیکیشن کی جانچ

**Module08/samples/08 (Electron ایپ) کے پاس جامع جانچ موجود ہے:**
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

**Python نمونوں کو دستی طور پر جانچنا چاہیے:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## کوڈ اسٹائل کے رہنما اصول

### Markdown مواد

- مستقل سرخی کی درجہ بندی استعمال کریں (# عنوان کے لیے، ## اہم حصوں کے لیے، ### ذیلی حصوں کے لیے)
- کوڈ بلاکس میں زبان کے وضاحت کنندہ شامل کریں: ```python, ```bash, ```javascript
- جدولوں، فہرستوں، اور زور دینے کے لیے موجودہ فارمیٹنگ کی پیروی کریں
- لائنوں کو پڑھنے کے قابل رکھیں (تقریباً 80-100 حروف کا ہدف، لیکن سخت نہیں)
- اندرونی حوالوں کے لیے نسبتی لنکس استعمال کریں

### Python کوڈ اسٹائل

- PEP 8 کنونشنز کی پیروی کریں
- جہاں مناسب ہو، قسم کے اشارے استعمال کریں
- فنکشنز اور کلاسز کے لیے ڈاکسٹرنگز شامل کریں
- معنی خیز متغیر نام استعمال کریں
- فنکشنز کو مرکوز اور مختصر رکھیں

### JavaScript/Node.js کوڈ اسٹائل

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**اہم کنونشنز:**
- نمونہ 08 میں فراہم کردہ ESLint کنفیگریشن
- کوڈ فارمیٹنگ کے لیے Prettier
- جدید ES6+ نحو استعمال کریں
- کوڈ بیس میں موجودہ نمونوں کی پیروی کریں

## پل ریکویسٹ کے رہنما اصول

### عنوان کی شکل
```
[ModuleXX] Brief description of change
```
یا
```
[Module08/samples/XX] Description for sample changes
```

### جمع کرانے سے پہلے

**مواد کی تبدیلیوں کے لیے:**
- تمام ترمیم شدہ Markdown فائلوں کا پیش نظارہ کریں
- تصدیق کریں کہ لنکس اور تصاویر کام کر رہی ہیں
- ٹائپوز اور گرامر کی غلطیوں کی جانچ کریں

**نمونہ کوڈ کی تبدیلیوں کے لیے (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python نمونہ کی تبدیلیوں کے لیے:**
- تصدیق کریں کہ نمونہ کامیابی سے چل رہا ہے
- غلطی کے ہینڈلنگ کی تصدیق کریں
- Foundry Local کے ساتھ مطابقت کی جانچ کریں

### جائزہ لینے کا عمل

- تعلیمی مواد کی تبدیلیوں کا درستگی اور وضاحت کے لیے جائزہ لیا جاتا ہے
- کوڈ کے نمونوں کو فعالیت کے لیے جانچا جاتا ہے
- ترجمہ کی اپ ڈیٹس خودکار طور پر GitHub Actions کے ذریعے ہینڈل کی جاتی ہیں

## ترجمہ کا نظام

**اہم:** یہ ذخیرہ GitHub Actions کے ذریعے خودکار ترجمہ استعمال کرتا ہے۔

- ترجمے `/translations/` ڈائریکٹری میں ہیں (50+ زبانیں)
- `co-op-translator.yml` ورک فلو کے ذریعے خودکار
- **ترجمہ فائلوں کو دستی طور پر ترمیم نہ کریں** - وہ اووررائٹ ہو جائیں گی
- صرف جڑ اور ماڈیول ڈائریکٹریز میں انگریزی سورس فائلوں میں ترمیم کریں
- ترجمے `main` برانچ پر پش کرنے پر خودکار طور پر تیار کیے جاتے ہیں

## Foundry Local انضمام

زیادہ تر Module08 نمونوں کو Microsoft Foundry Local کے چلنے کی ضرورت ہے:

### Foundry Local شروع کرنا
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

### Foundry Local کی تصدیق کرنا
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### نمونوں کے لیے ماحول کے متغیرات

زیادہ تر نمونے ان ماحول کے متغیرات استعمال کرتے ہیں:
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

## تعمیر اور تعیناتی

### مواد کی تعیناتی

یہ ذخیرہ بنیادی طور پر دستاویزات پر مشتمل ہے - مواد کے لیے کوئی تعمیراتی عمل درکار نہیں۔

### نمونہ ایپلیکیشن کی تعمیر

**Electron ایپلیکیشن (Module08/samples/08):**
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

**Python نمونے:**
کوئی تعمیراتی عمل نہیں - نمونے براہ راست Python انٹرپریٹر کے ساتھ چلائے جاتے ہیں۔

## عام مسائل اور خرابیوں کا ازالہ

### Foundry Local نہیں چل رہا
**مسئلہ:** نمونے کنکشن کی غلطیوں کے ساتھ ناکام ہو رہے ہیں

**حل:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python ورچوئل ماحول کے مسائل
**مسئلہ:** ماڈیول درآمد کی غلطیاں

**حل:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron تعمیراتی مسائل
**مسئلہ:** npm انسٹال یا تعمیر کی ناکامیاں

**حل:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### ترجمہ ورک فلو کے تنازعات
**مسئلہ:** ترجمہ PR آپ کی تبدیلیوں کے ساتھ تنازعہ پیدا کر رہا ہے

**حل:**
- صرف انگریزی سورس فائلوں میں ترمیم کریں
- خودکار ترجمہ ورک فلو کو ترجموں کا خیال رکھنے دیں
- اگر تنازعات پیدا ہوں، تو ترجمے کے ضم ہونے کے بعد `main` کو اپنی برانچ میں ضم کریں

## اضافی وسائل

### سیکھنے کے راستے
- **ابتدائی راستہ:** ماڈیولز 01-02 (7-9 گھنٹے)
- **درمیانی راستہ:** ماڈیولز 03-04 (9-11 گھنٹے)
- **اعلیٰ راستہ:** ماڈیولز 05-07 (12-15 گھنٹے)
- **ماہر راستہ:** ماڈیول 08 (8-10 گھنٹے)

### اہم ماڈیول مواد
- **Module01:** EdgeAI کی بنیادی باتیں اور حقیقی دنیا کے کیس اسٹڈیز
- **Module02:** چھوٹے زبان ماڈل (SLM) خاندان اور آرکیٹیکچر
- **Module03:** مقامی اور کلاؤڈ تعیناتی کی حکمت عملی
- **Module04:** متعدد فریم ورک کے ساتھ ماڈل کی اصلاح
- **Module05:** SLMOps - پروڈکشن آپریشنز
- **Module06:** AI ایجنٹس اور فنکشن کالنگ
- **Module07:** پلیٹ فارم مخصوص نفاذات
- **Module08:** Foundry Local ٹول کٹ کے ساتھ 10 جامع نمونے

### بیرونی انحصار
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - مقامی AI ماڈل رن ٹائم
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - اصلاحی فریم ورک
- [Microsoft Olive](https://microsoft.github.io/Olive/) - ماڈل کی اصلاحی ٹول کٹ
- [OpenVINO](https://docs.openvino.ai/) - Intel کی اصلاحی ٹول کٹ

## پروجیکٹ کے مخصوص نوٹس

### Module08 نمونہ ایپلیکیشنز

ذخیرہ میں 10 جامع نمونہ ایپلیکیشنز شامل ہیں:

1. **01-REST چیٹ کوئیک اسٹارٹ** - بنیادی OpenAI SDK انضمام
2. **02-OpenAI SDK انضمام** - جدید SDK خصوصیات
3. **03-ماڈل دریافت اور بینچ مارکنگ** - ماڈل موازنہ کے اوزار
4. **04-Chainlit RAG ایپلیکیشن** - بازیافت-اضافہ شدہ جنریشن
5. **05-ملٹی ایجنٹ آرکیسٹریشن** - بنیادی ایجنٹ کوآرڈینیشن
6. **06-ماڈلز-ایز-ٹولز روٹر** - ذہین ماڈل روٹنگ
7. **07-ڈائریکٹ API کلائنٹ** - کم سطح API انضمام
8. **08-Windows 11 چیٹ ایپ** - مقامی Electron ڈیسک ٹاپ ایپلیکیشن
9. **09-اعلیٰ ملٹی ایجنٹ سسٹم** - پیچیدہ ایجنٹ آرکیسٹریشن
10. **10-Foundry ٹولز فریم ورک** - LangChain/Semantic Kernel انضمام

ہر نمونہ Foundry Local کے ساتھ Edge AI کی ترقی کے مختلف پہلوؤں کو ظاہر کرتا ہے۔

### کارکردگی کے تحفظات

- SLMs کو Edge تعیناتی کے لیے بہتر بنایا گیا ہے (2-16GB RAM)
- مقامی انفرنس 50-500ms کے ردعمل کے اوقات فراہم کرتا ہے
- کوانٹائزیشن تکنیک 75% سائز میں کمی کے ساتھ 85% کارکردگی برقرار رکھتی ہیں
- مقامی ماڈلز کے ساتھ حقیقی وقت کی گفتگو کی صلاحیتیں

### سیکیورٹی اور پرائیویسی

- تمام پروسیسنگ مقامی طور پر ہوتی ہے - کوئی ڈیٹا کلاؤڈ کو نہیں بھیجا جاتا
- پرائیویسی حساس ایپلیکیشنز (صحت کی دیکھ بھال، مالیات) کے لیے موزوں
- ڈیٹا خودمختاری کی ضروریات کو پورا کرتا ہے
- Foundry Local مکمل طور پر مقامی ہارڈویئر پر چلتا ہے

---

**یہ ایک تعلیمی ذخیرہ ہے جو Edge AI کی ترقی سکھانے پر مرکوز ہے۔ بنیادی شراکت کا نمونہ تعلیمی مواد کو بہتر بنانا اور Edge AI کے تصورات کو ظاہر کرنے والے نمونہ ایپلیکیشنز کو شامل/بہتر کرنا ہے۔**

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔