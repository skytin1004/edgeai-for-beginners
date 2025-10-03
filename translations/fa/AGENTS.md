<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:23:20+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fa"
}
-->
# AGENTS.md

## نمای کلی پروژه

EdgeAI for Beginners یک مخزن آموزشی جامع است که توسعه Edge AI با مدل‌های زبان کوچک (SLMs) را آموزش می‌دهد. این دوره شامل اصول EdgeAI، استقرار مدل، تکنیک‌های بهینه‌سازی و پیاده‌سازی‌های آماده تولید با استفاده از Microsoft Foundry Local و چارچوب‌های مختلف هوش مصنوعی است.

**فناوری‌های کلیدی:**
- Python 3.8+ (زبان اصلی برای نمونه‌های AI/ML)
- .NET C# (نمونه‌های AI/ML)
- JavaScript/Node.js با Electron (برای برنامه‌های دسکتاپ)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- چارچوب‌های هوش مصنوعی: LangChain، Semantic Kernel، Chainlit
- بهینه‌سازی مدل: Llama.cpp، Microsoft Olive، OpenVINO، Apple MLX

**نوع مخزن:** مخزن محتوای آموزشی با ۸ ماژول و ۱۰ نمونه برنامه جامع

**معماری:** مسیر یادگیری چندماژولی با نمونه‌های عملی که الگوهای استقرار Edge AI را نشان می‌دهند

## ساختار مخزن

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

## دستورات راه‌اندازی

### راه‌اندازی مخزن

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### راه‌اندازی نمونه‌های Python (ماژول ۰۸ و نمونه‌های Python)

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

### راه‌اندازی نمونه‌های Node.js (نمونه ۰۸ - برنامه چت ویندوز)

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

### راه‌اندازی Foundry Local

Foundry Local برای اجرای نمونه‌های ماژول ۰۸ مورد نیاز است:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## جریان کاری توسعه

### توسعه محتوا

این مخزن عمدتاً شامل **محتوای آموزشی Markdown** است. هنگام ایجاد تغییرات:

1. فایل‌های `.md` را در دایرکتوری‌های ماژول مناسب ویرایش کنید
2. الگوهای قالب‌بندی موجود را دنبال کنید
3. اطمینان حاصل کنید که مثال‌های کد دقیق و آزمایش شده باشند
4. محتوای ترجمه‌شده مربوطه را به‌روزرسانی کنید (یا اجازه دهید اتوماسیون این کار را انجام دهد)

### توسعه نمونه‌های برنامه

برای نمونه‌های Python (نمونه‌های ۰۱-۰۷، ۰۹-۱۰):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

برای نمونه Electron (نمونه ۰۸):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### آزمایش نمونه‌های برنامه

نمونه‌های Python تست‌های خودکار ندارند اما می‌توان با اجرای آن‌ها اعتبارسنجی کرد:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

نمونه Electron دارای زیرساخت تست است:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## دستورالعمل‌های آزمایش

### اعتبارسنجی محتوا

مخزن از جریان‌های کاری ترجمه خودکار استفاده می‌کند. نیازی به آزمایش دستی برای ترجمه‌ها نیست.

**اعتبارسنجی دستی برای تغییرات محتوا:**
1. رندر Markdown را با پیش‌نمایش فایل‌های `.md` بررسی کنید
2. اطمینان حاصل کنید که همه لینک‌ها به اهداف معتبر اشاره دارند
3. هر قطعه کدی که در مستندات گنجانده شده است را آزمایش کنید
4. بررسی کنید که تصاویر به درستی بارگذاری شوند

### آزمایش نمونه‌های برنامه

**ماژول ۰۸/نمونه‌ها/۰۸ (برنامه Electron) دارای آزمایش جامع است:**
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

**نمونه‌های Python باید به صورت دستی آزمایش شوند:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## دستورالعمل‌های سبک کدنویسی

### محتوای Markdown

- از سلسله‌مراتب عنوان ثابت استفاده کنید (# برای عنوان، ## برای بخش‌های اصلی، ### برای زیر‌بخش‌ها)
- بلوک‌های کد را با مشخص‌کننده زبان شامل کنید: ```python, ```bash, ```javascript
- قالب‌بندی موجود برای جداول، لیست‌ها و تأکید را دنبال کنید
- خطوط را خوانا نگه دارید (هدف حدود ۸۰-۱۰۰ کاراکتر، اما سخت‌گیرانه نیست)
- از لینک‌های نسبی برای ارجاعات داخلی استفاده کنید

### سبک کدنویسی Python

- از کنوانسیون‌های PEP 8 پیروی کنید
- در صورت امکان از نوع‌دهی استفاده کنید
- برای توابع و کلاس‌ها توضیحات اضافه کنید
- از نام‌های متغیر معنادار استفاده کنید
- توابع را متمرکز و مختصر نگه دارید

### سبک کدنویسی JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**کنوانسیون‌های کلیدی:**
- پیکربندی ESLint در نمونه ۰۸ ارائه شده است
- Prettier برای قالب‌بندی کد
- از سینتکس مدرن ES6+ استفاده کنید
- الگوهای موجود در کدبیس را دنبال کنید

## دستورالعمل‌های درخواست کشش (Pull Request)

### قالب عنوان
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### قبل از ارسال

**برای تغییرات محتوا:**
- همه فایل‌های Markdown اصلاح‌شده را پیش‌نمایش کنید
- لینک‌ها و تصاویر را بررسی کنید
- خطاهای تایپی و گرامری را بررسی کنید

**برای تغییرات کد نمونه (ماژول ۰۸/نمونه‌ها/۰۸):**
```bash
npm run lint
npm test
```

**برای تغییرات نمونه‌های Python:**
- آزمایش کنید که نمونه به درستی اجرا شود
- بررسی کنید که مدیریت خطا به درستی کار کند
- سازگاری با Foundry Local را بررسی کنید

### فرآیند بررسی

- تغییرات محتوای آموزشی از نظر دقت و وضوح بررسی می‌شوند
- نمونه‌های کد از نظر عملکرد آزمایش می‌شوند
- به‌روزرسانی‌های ترجمه به‌طور خودکار توسط GitHub Actions مدیریت می‌شوند

## سیستم ترجمه

**مهم:** این مخزن از ترجمه خودکار از طریق GitHub Actions استفاده می‌کند.

- ترجمه‌ها در دایرکتوری `/translations/` (بیش از ۵۰ زبان) قرار دارند
- به‌طور خودکار از طریق جریان کاری `co-op-translator.yml` انجام می‌شود
- **فایل‌های ترجمه را به صورت دستی ویرایش نکنید** - آن‌ها بازنویسی خواهند شد
- فقط فایل‌های منبع انگلیسی را در دایرکتوری‌های ریشه و ماژول ویرایش کنید
- ترجمه‌ها به‌طور خودکار با هر بار فشار دادن به شاخه `main` تولید می‌شوند

## یکپارچه‌سازی Foundry Local

بیشتر نمونه‌های ماژول ۰۸ نیاز دارند که Microsoft Foundry Local در حال اجرا باشد:

### راه‌اندازی Foundry Local
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

### تأیید Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### متغیرهای محیطی برای نمونه‌ها

بیشتر نمونه‌ها از این متغیرهای محیطی استفاده می‌کنند:
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

## ساخت و استقرار

### استقرار محتوا

این مخزن عمدتاً مستندات است - فرآیند ساخت برای محتوا مورد نیاز نیست.

### ساخت نمونه‌های برنامه

**برنامه Electron (ماژول ۰۸/نمونه‌ها/۰۸):**
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

**نمونه‌های Python:**
فرآیند ساخت ندارد - نمونه‌ها مستقیماً با مفسر Python اجرا می‌شوند.

## مشکلات رایج و رفع اشکال

### Foundry Local اجرا نمی‌شود
**مشکل:** نمونه‌ها با خطاهای اتصال شکست می‌خورند

**راه‌حل:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### مشکلات محیط مجازی Python
**مشکل:** خطاهای وارد کردن ماژول

**راه‌حل:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### مشکلات ساخت Electron
**مشکل:** شکست نصب npm یا ساخت

**راه‌حل:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### تضادهای جریان کاری ترجمه
**مشکل:** درخواست کشش ترجمه با تغییرات شما تضاد دارد

**راه‌حل:**
- فقط فایل‌های منبع انگلیسی را ویرایش کنید
- اجازه دهید جریان کاری ترجمه خودکار ترجمه‌ها را مدیریت کند
- اگر تضاد رخ داد، شاخه `main` را پس از ادغام ترجمه‌ها به شاخه خود ادغام کنید

## منابع اضافی

### مسیرهای یادگیری
- **مسیر مبتدی:** ماژول‌های ۰۱-۰۲ (۷-۹ ساعت)
- **مسیر متوسط:** ماژول‌های ۰۳-۰۴ (۹-۱۱ ساعت)
- **مسیر پیشرفته:** ماژول‌های ۰۵-۰۷ (۱۲-۱۵ ساعت)
- **مسیر متخصص:** ماژول ۰۸ (۸-۱۰ ساعت)

### محتوای کلیدی ماژول
- **ماژول ۰۱:** اصول EdgeAI و مطالعات موردی دنیای واقعی
- **ماژول ۰۲:** خانواده‌ها و معماری‌های مدل‌های زبان کوچک (SLM)
- **ماژول ۰۳:** استراتژی‌های استقرار محلی و ابری
- **ماژول ۰۴:** بهینه‌سازی مدل با چارچوب‌های مختلف
- **ماژول ۰۵:** SLMOps - عملیات تولید
- **ماژول ۰۶:** عوامل هوش مصنوعی و فراخوانی توابع
- **ماژول ۰۷:** پیاده‌سازی‌های خاص پلتفرم
- **ماژول ۰۸:** ابزار Foundry Local با ۱۰ نمونه جامع

### وابستگی‌های خارجی
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - زمان اجرای مدل هوش مصنوعی محلی
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - چارچوب بهینه‌سازی
- [Microsoft Olive](https://microsoft.github.io/Olive/) - ابزار بهینه‌سازی مدل
- [OpenVINO](https://docs.openvino.ai/) - ابزار بهینه‌سازی Intel

## یادداشت‌های خاص پروژه

### نمونه‌های برنامه ماژول ۰۸

مخزن شامل ۱۰ نمونه برنامه جامع است:

1. **01-REST Chat Quickstart** - یکپارچه‌سازی اولیه OpenAI SDK
2. **02-OpenAI SDK Integration** - ویژگی‌های پیشرفته SDK
3. **03-Model Discovery & Benchmarking** - ابزارهای مقایسه مدل
4. **04-Chainlit RAG Application** - تولید تقویت‌شده با بازیابی
5. **05-Multi-Agent Orchestration** - هماهنگی عوامل پایه
6. **06-Models-as-Tools Router** - مسیریابی هوشمند مدل
7. **07-Direct API Client** - یکپارچه‌سازی سطح پایین API
8. **08-Windows 11 Chat App** - برنامه دسکتاپ بومی Electron
9. **09-Advanced Multi-Agent System** - هماهنگی پیچیده عوامل
10. **10-Foundry Tools Framework** - یکپارچه‌سازی LangChain/Semantic Kernel

هر نمونه جنبه‌های مختلف توسعه Edge AI با Foundry Local را نشان می‌دهد.

### ملاحظات عملکرد

- SLM‌ها برای استقرار در Edge بهینه شده‌اند (۲-۱۶ گیگابایت RAM)
- استنتاج محلی زمان پاسخ ۵۰-۵۰۰ میلی‌ثانیه ارائه می‌دهد
- تکنیک‌های کمیت‌سازی کاهش اندازه ۷۵٪ با حفظ عملکرد ۸۵٪ را به دست می‌آورند
- قابلیت‌های مکالمه بلادرنگ با مدل‌های محلی

### امنیت و حریم خصوصی

- تمام پردازش‌ها به صورت محلی انجام می‌شود - هیچ داده‌ای به ابر ارسال نمی‌شود
- مناسب برای برنامه‌های حساس به حریم خصوصی (سلامت، مالی)
- الزامات حاکمیت داده را برآورده می‌کند
- Foundry Local کاملاً بر روی سخت‌افزار محلی اجرا می‌شود

---

**این یک مخزن آموزشی است که بر آموزش توسعه Edge AI تمرکز دارد. الگوی اصلی مشارکت شامل بهبود محتوای آموزشی و افزودن/تقویت نمونه‌های برنامه است که مفاهیم Edge AI را نشان می‌دهند.**

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.