<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:31:03+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pa"
}
-->
# AGENTS.md

## ਪ੍ਰੋਜੈਕਟ ਝਲਕ

EdgeAI for Beginners ਇੱਕ ਵਿਸਤ੍ਰਿਤ ਸਿੱਖਿਆ ਪ੍ਰਾਪਤ ਕਰਨ ਵਾਲਾ ਸੰਗ੍ਰਹਿ ਹੈ ਜੋ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲ (SLMs) ਨਾਲ Edge AI ਵਿਕਾਸ ਸਿਖਾਉਂਦਾ ਹੈ। ਕੋਰਸ ਵਿੱਚ EdgeAI ਦੇ ਮੂਲ ਤੱਤ, ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ, ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ ਤਕਨੀਕਾਂ, ਅਤੇ Microsoft Foundry Local ਅਤੇ ਵੱਖ-ਵੱਖ AI ਫਰੇਮਵਰਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਉਤਪਾਦਨ-ਤਿਆਰ ਕਾਰਜਾਂ ਦੀਆਂ ਅਮਲਵਾਰੀਆਂ ਨੂੰ ਕਵਰ ਕੀਤਾ ਗਿਆ ਹੈ।

**ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ:**
- Python 3.8+ (AI/ML ਨਮੂਨਿਆਂ ਲਈ ਮੁੱਖ ਭਾਸ਼ਾ)
- .NET C# (AI/ML ਨਮੂਨੇ)
- JavaScript/Node.js ਨਾਲ Electron (ਡੈਸਕਟਾਪ ਐਪਲੀਕੇਸ਼ਨ ਲਈ)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI ਫਰੇਮਵਰਕ: LangChain, Semantic Kernel, Chainlit
- ਮਾਡਲ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**ਸੰਗ੍ਰਹਿ ਦੀ ਕਿਸਮ:** ਸਿੱਖਿਆ ਸਮੱਗਰੀ ਸੰਗ੍ਰਹਿ ਜਿਸ ਵਿੱਚ 8 ਮੋਡੀਊਲ ਅਤੇ 10 ਵਿਸਤ੍ਰਿਤ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਹਨ

**ਆਰਕੀਟੈਕਚਰ:** ਬਹੁ-ਮੋਡੀਊਲ ਸਿੱਖਣ ਦਾ ਰਾਹ ਜਿਸ ਵਿੱਚ Edge AI ਡਿਪਲੌਇਮੈਂਟ ਪੈਟਰਨਾਂ ਨੂੰ ਦਰਸਾਉਣ ਵਾਲੇ ਅਮਲਵਾਰ ਨਮੂਨੇ ਸ਼ਾਮਲ ਹਨ

## ਸੰਗ੍ਰਹਿ ਦੀ ਬਣਤਰ

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

## ਸੈਟਅੱਪ ਕਮਾਂਡ

### ਸੰਗ੍ਰਹਿ ਸੈਟਅੱਪ

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python ਨਮੂਨਾ ਸੈਟਅੱਪ (Module08 ਅਤੇ Python ਨਮੂਨੇ)

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

### Node.js ਨਮੂਨਾ ਸੈਟਅੱਪ (Sample 08 - Windows Chat App)

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

### Foundry Local ਸੈਟਅੱਪ

Module08 ਨਮੂਨਿਆਂ ਨੂੰ ਚਲਾਉਣ ਲਈ Foundry Local ਦੀ ਲੋੜ ਹੈ:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## ਵਿਕਾਸ ਵਰਕਫਲੋ

### ਸਮੱਗਰੀ ਵਿਕਾਸ

ਇਹ ਸੰਗ੍ਰਹਿ ਮੁੱਖ ਤੌਰ 'ਤੇ **Markdown ਸਿੱਖਿਆ ਸਮੱਗਰੀ** ਸ਼ਾਮਲ ਕਰਦੀ ਹੈ। ਤਬਦੀਲੀਆਂ ਕਰਦੇ ਸਮੇਂ:

1. `.md` ਫਾਈਲਾਂ ਨੂੰ ਸਹੀ ਮੋਡੀਊਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਸੋਧੋ
2. ਮੌਜੂਦਾ ਫਾਰਮੈਟਿੰਗ ਪੈਟਰਨਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
3. ਕੋਡ ਉਦਾਹਰਣਾਂ ਨੂੰ ਸਹੀ ਅਤੇ ਟੈਸਟ ਕੀਤਾ ਹੋਣਾ ਯਕੀਨੀ ਬਣਾਓ
4. ਜੇ ਜ਼ਰੂਰੀ ਹੋਵੇ ਤਾਂ ਸੰਬੰਧਿਤ ਅਨੁਵਾਦਿਤ ਸਮੱਗਰੀ ਨੂੰ ਅਪਡੇਟ ਕਰੋ (ਜਾਂ ਆਟੋਮੇਸ਼ਨ ਨੂੰ ਇਸਦਾ ਧਿਆਨ ਰੱਖਣ ਦਿਓ)

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ

Python ਨਮੂਨਿਆਂ ਲਈ (ਨਮੂਨੇ 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron ਨਮੂਨਾ ਲਈ (ਨਮੂਨਾ 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟਿੰਗ

Python ਨਮੂਨਿਆਂ ਵਿੱਚ ਆਟੋਮੈਟਿਕ ਟੈਸਟ ਨਹੀਂ ਹਨ ਪਰ ਇਨ੍ਹਾਂ ਨੂੰ ਚਲਾਕੇ ਵੈਰੀਫਾਈ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron ਨਮੂਨੇ ਵਿੱਚ ਟੈਸਟ ਇੰਫਰਾਸਟਰਕਚਰ ਹੈ:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## ਟੈਸਟਿੰਗ ਹਦਾਇਤਾਂ

### ਸਮੱਗਰੀ ਵੈਰੀਫਿਕੇਸ਼ਨ

ਸੰਗ੍ਰਹਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਰਕਫਲੋਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ। ਅਨੁਵਾਦਾਂ ਲਈ ਕੋਈ ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ ਦੀ ਲੋੜ ਨਹੀਂ।

**ਸਮੱਗਰੀ ਤਬਦੀਲੀਆਂ ਲਈ ਮੈਨੂਅਲ ਵੈਰੀਫਿਕੇਸ਼ਨ:**
1. `.md` ਫਾਈਲਾਂ ਨੂੰ ਪ੍ਰੀਵਿਊ ਕਰਕੇ Markdown ਰੈਂਡਰਿੰਗ ਦੀ ਸਮੀਖਿਆ ਕਰੋ
2. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਾਰੇ ਲਿੰਕ ਸਹੀ ਟਾਰਗਟਾਂ ਵੱਲ ਇਸ਼ਾਰਾ ਕਰਦੇ ਹਨ
3. ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੇ ਕੋਡ ਸਨਿੱਪਟਾਂ ਨੂੰ ਟੈਸਟ ਕਰੋ
4. ਚੈੱਕ ਕਰੋ ਕਿ ਚਿੱਤਰ ਸਹੀ ਤੌਰ 'ਤੇ ਲੋਡ ਹੋ ਰਹੇ ਹਨ

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟਿੰਗ

**Module08/samples/08 (Electron ਐਪ) ਵਿੱਚ ਵਿਸਤ੍ਰਿਤ ਟੈਸਟਿੰਗ ਹੈ:**
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

**Python ਨਮੂਨਿਆਂ ਨੂੰ ਮੈਨੂਅਲ ਟੈਸਟ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## ਕੋਡ ਸਟਾਈਲ ਹਦਾਇਤਾਂ

### Markdown ਸਮੱਗਰੀ

- ਸਿਰਲੇਖ ਹਾਇਰਾਰਕੀ ਦੀ ਸਥਿਰ ਵਰਤੋਂ ਕਰੋ (# ਟਾਈਟਲ ਲਈ, ## ਮੁੱਖ ਸੈਕਸ਼ਨ ਲਈ, ### ਉਪ-ਸੈਕਸ਼ਨ ਲਈ)
- ਕੋਡ ਬਲਾਕਾਂ ਵਿੱਚ ਭਾਸ਼ਾ ਨਿਰਧਾਰਕ ਸ਼ਾਮਲ ਕਰੋ: ```python, ```bash, ```javascript
- ਟੇਬਲਾਂ, ਸੂਚੀਆਂ, ਅਤੇ ਜ਼ੋਰ ਦੇਣ ਲਈ ਮੌਜੂਦਾ ਫਾਰਮੈਟਿੰਗ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ਲਾਈਨਾਂ ਨੂੰ ਪੜ੍ਹਨ ਯੋਗ ਰੱਖੋ (~80-100 ਅੱਖਰਾਂ ਦਾ ਲਕਸ਼ ਰੱਖੋ, ਪਰ ਸਖ਼ਤ ਨਹੀਂ)
- ਅੰਦਰੂਨੀ ਹਵਾਲਿਆਂ ਲਈ ਰਿਲੇਟਿਵ ਲਿੰਕ ਦੀ ਵਰਤੋਂ ਕਰੋ

### Python ਕੋਡ ਸਟਾਈਲ

- PEP 8 ਕਨਵੈਂਸ਼ਨ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ਜਿੱਥੇ ਜ਼ਰੂਰੀ ਹੋਵੇ, ਟਾਈਪ ਹਿੰਟ ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਫੰਕਸ਼ਨ ਅਤੇ ਕਲਾਸਾਂ ਲਈ ਡੌਕਸਟ੍ਰਿੰਗ ਸ਼ਾਮਲ ਕਰੋ
- ਅਰਥਪੂਰਨ ਵੈਰੀਏਬਲ ਨਾਮਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕੇਂਦਰਿਤ ਅਤੇ ਸੰਖੇਪ ਰੱਖੋ

### JavaScript/Node.js ਕੋਡ ਸਟਾਈਲ

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**ਮੁੱਖ ਕਨਵੈਂਸ਼ਨ:**
- ESLint ਕਨਫਿਗਰੇਸ਼ਨ ਨਮੂਨਾ 08 ਵਿੱਚ ਦਿੱਤਾ ਗਿਆ ਹੈ
- Prettier ਕੋਡ ਫਾਰਮੈਟਿੰਗ ਲਈ
- ਆਧੁਨਿਕ ES6+ ਸਿੰਟੈਕਸ ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਕੋਡਬੇਸ ਵਿੱਚ ਮੌਜੂਦਾ ਪੈਟਰਨਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ

## ਪੁਲ ਰਿਕਵੇਸਟ ਹਦਾਇਤਾਂ

### ਸਿਰਲੇਖ ਫਾਰਮੈਟ
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### ਜਮ੍ਹਾਂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

**ਸਮੱਗਰੀ ਤਬਦੀਲੀਆਂ ਲਈ:**
- ਸਾਰੇ ਸੋਧੇ ਹੋਏ Markdown ਫਾਈਲਾਂ ਨੂੰ ਪ੍ਰੀਵਿਊ ਕਰੋ
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਲਿੰਕ ਅਤੇ ਚਿੱਤਰ ਕੰਮ ਕਰਦੇ ਹਨ
- ਟਾਈਪੋ ਅਤੇ ਵਿਆਕਰਣ ਦੀਆਂ ਗਲਤੀਆਂ ਦੀ ਜਾਂਚ ਕਰੋ

**ਨਮੂਨਾ ਕੋਡ ਤਬਦੀਲੀਆਂ ਲਈ (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python ਨਮੂਨਾ ਤਬਦੀਲੀਆਂ ਲਈ:**
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਨਮੂਨਾ ਸਫਲਤਾਪੂਰਵਕ ਚਲਦਾ ਹੈ
- ਗਲਤੀ ਸੰਭਾਲਣ ਦੀ ਜਾਂਚ ਕਰੋ
- Foundry Local ਨਾਲ ਅਨੁਕੂਲਤਾ ਦੀ ਜਾਂਚ ਕਰੋ

### ਸਮੀਖਿਆ ਪ੍ਰਕਿਰਿਆ

- ਸਿੱਖਿਆ ਸਮੱਗਰੀ ਤਬਦੀਲੀਆਂ ਦੀ ਸਹੀਤਾ ਅਤੇ ਸਪਸ਼ਟਤਾ ਲਈ ਸਮੀਖਿਆ ਕੀਤੀ ਜਾਂਦੀ ਹੈ
- ਕੋਡ ਨਮੂਨਿਆਂ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਲਈ ਟੈਸਟਿੰਗ ਕੀਤੀ ਜਾਂਦੀ ਹੈ
- ਅਨੁਵਾਦ ਅਪਡੇਟ GitHub Actions ਦੁਆਰਾ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਸੰਭਾਲੇ ਜਾਂਦੇ ਹਨ

## ਅਨੁਵਾਦ ਪ੍ਰਣਾਲੀ

**ਮਹੱਤਵਪੂਰਨ:** ਇਹ ਸੰਗ੍ਰਹਿ GitHub Actions ਦੁਆਰਾ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ।

- ਅਨੁਵਾਦ `/translations/` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਹਨ (50+ ਭਾਸ਼ਾਵਾਂ)
- `co-op-translator.yml` ਵਰਕਫਲੋ ਦੁਆਰਾ ਆਟੋਮੈਟਿਕ
- **ਅਨੁਵਾਦ ਫਾਈਲਾਂ ਨੂੰ ਮੈਨੂਅਲ ਤੌਰ 'ਤੇ ਸੋਧੋ ਨਾ ਕਰੋ** - ਇਹਨਾਂ ਨੂੰ ਓਵਰਰਾਈਟ ਕੀਤਾ ਜਾਵੇਗਾ
- ਰੂਟ ਅਤੇ ਮੋਡੀਊਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਸਿਰਫ਼ ਅੰਗਰੇਜ਼ੀ ਸਰੋਤ ਫਾਈਲਾਂ ਸੋਧੋ
- `main` ਸ਼ਾਖਾ ਵਿੱਚ ਪੁਸ਼ ਕਰਨ 'ਤੇ ਅਨੁਵਾਦ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਜਨਰੇਟ ਹੁੰਦੇ ਹਨ

## Foundry Local ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਜ਼ਿਆਦਾਤਰ Module08 ਨਮੂਨਿਆਂ ਨੂੰ Microsoft Foundry Local ਚਲਾਉਣ ਦੀ ਲੋੜ ਹੈ:

### Foundry Local ਸ਼ੁਰੂ ਕਰਨਾ
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

### Foundry Local ਦੀ ਪੁਸ਼ਟੀ ਕਰਨਾ
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### ਨਮੂਨਿਆਂ ਲਈ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

ਜ਼ਿਆਦਾਤਰ ਨਮੂਨੇ ਇਹ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਵਰਤਦੇ ਹਨ:
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

## ਬਿਲਡ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ

### ਸਮੱਗਰੀ ਡਿਪਲੌਇਮੈਂਟ

ਇਹ ਸੰਗ੍ਰਹਿ ਮੁੱਖ ਤੌਰ 'ਤੇ ਦਸਤਾਵੇਜ਼ ਹੈ - ਸਮੱਗਰੀ ਲਈ ਕੋਈ ਬਿਲਡ ਪ੍ਰਕਿਰਿਆ ਦੀ ਲੋੜ ਨਹੀਂ।

### ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਬਿਲਡਿੰਗ

**Electron ਐਪਲੀਕੇਸ਼ਨ (Module08/samples/08):**
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

**Python ਨਮੂਨੇ:**
ਕੋਈ ਬਿਲਡ ਪ੍ਰਕਿਰਿਆ ਨਹੀਂ - ਨਮੂਨਿਆਂ ਨੂੰ ਸਿੱਧੇ Python interpreter ਨਾਲ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ।

## ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਸਮੱਸਿਆ ਹੱਲ

### Foundry Local ਚਲ ਨਹੀਂ ਰਿਹਾ
**ਸਮੱਸਿਆ:** ਨਮੂਨੇ ਕਨੈਕਸ਼ਨ ਗਲਤੀਆਂ ਨਾਲ ਫੇਲ ਹੋ ਜਾਂਦੇ ਹਨ

**ਹੱਲ:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਸਮੱਸਿਆਵਾਂ
**ਸਮੱਸਿਆ:** ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਗਲਤੀਆਂ

**ਹੱਲ:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron ਬਿਲਡ ਸਮੱਸਿਆਵਾਂ
**ਸਮੱਸਿਆ:** npm install ਜਾਂ ਬਿਲਡ ਫੇਲ

**ਹੱਲ:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### ਅਨੁਵਾਦ ਵਰਕਫਲੋ ਸੰਘਰਸ਼

**ਸਮੱਸਿਆ:** ਅਨੁਵਾਦ PR ਤੁਹਾਡੇ ਤਬਦੀਲੀਆਂ ਨਾਲ ਸੰਘਰਸ਼ ਕਰਦਾ ਹੈ

**ਹੱਲ:**
- ਸਿਰਫ਼ ਅੰਗਰੇਜ਼ੀ ਸਰੋਤ ਫਾਈਲਾਂ ਸੋਧੋ
- ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਰਕਫਲੋ ਨੂੰ ਅਨੁਵਾਦ ਸੰਭਾਲਣ ਦਿਓ
- ਜੇ ਸੰਘਰਸ਼ ਹੁੰਦਾ ਹੈ, ਤਾਂ ਅਨੁਵਾਦਾਂ ਦੇ ਮਰਜ ਹੋਣ ਤੋਂ ਬਾਅਦ `main` ਨੂੰ ਆਪਣੀ ਸ਼ਾਖਾ ਵਿੱਚ ਮਰਜ ਕਰੋ

## ਵਾਧੂ ਸਰੋਤ

### ਸਿੱਖਣ ਦੇ ਰਾਹ

- **ਬਿਗਿਨਰ ਪਾਥ:** ਮੋਡੀਊਲ 01-02 (7-9 ਘੰਟੇ)
- **ਇੰਟਰਮੀਡੀਏਟ ਪਾਥ:** ਮੋਡੀਊਲ 03-04 (9-11 ਘੰਟੇ)
- **ਐਡਵਾਂਸਡ ਪਾਥ:** ਮੋਡੀਊਲ 05-07 (12-15 ਘੰਟੇ)
- **ਐਕਸਪਰਟ ਪਾਥ:** ਮੋਡੀਊਲ 08 (8-10 ਘੰਟੇ)

### ਮੁੱਖ ਮੋਡੀਊਲ ਸਮੱਗਰੀ

- **Module01:** EdgeAI ਦੇ ਮੂਲ ਤੱਤ ਅਤੇ ਹਕੀਕਤੀ ਕੇਸ ਸਟਡੀਜ਼
- **Module02:** ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਪਰਿਵਾਰ ਅਤੇ ਆਰਕੀਟੈਕਚਰ
- **Module03:** ਸਥਾਨਕ ਅਤੇ ਕਲਾਉਡ ਡਿਪਲੌਇਮੈਂਟ ਰਣਨੀਤੀਆਂ
- **Module04:** ਕਈ ਫਰੇਮਵਰਕਾਂ ਨਾਲ ਮਾਡਲ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ
- **Module05:** SLMOps - ਉਤਪਾਦਨ ਕਾਰਜ
- **Module06:** AI ਏਜੰਟ ਅਤੇ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ
- **Module07:** ਪਲੇਟਫਾਰਮ-ਵਿਸ਼ੇਸ਼ ਅਮਲਵਾਰੀਆਂ
- **Module08:** Foundry Local ਟੂਲਕਿਟ ਨਾਲ 10 ਵਿਸਤ੍ਰਿਤ ਨਮੂਨੇ

### ਬਾਹਰੀ ਨਿਰਭਰਤਾਵਾਂ

- [Microsoft Foundry Local](https://foundry.microsoft.com/) - ਸਥਾਨਕ AI ਮਾਡਲ ਰਨਟਾਈਮ
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ ਫਰੇਮਵਰਕ
- [Microsoft Olive](https://microsoft.github.io/Olive/) - ਮਾਡਲ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ ਟੂਲਕਿਟ
- [OpenVINO](https://docs.openvino.ai/) - Intel ਦਾ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ ਟੂਲਕਿਟ

## ਪ੍ਰੋਜੈਕਟ-ਵਿਸ਼ੇਸ਼ ਨੋਟਸ

### Module08 ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ

ਸੰਗ੍ਰਹਿ ਵਿੱਚ 10 ਵਿਸਤ੍ਰਿਤ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਸ਼ਾਮਲ ਹਨ:

1. **01-REST Chat Quickstart** - ਬੁਨਿਆਦੀ OpenAI SDK ਇੰਟੀਗ੍ਰੇਸ਼ਨ
2. **02-OpenAI SDK Integration** - ਉੱਚ-ਸਤਰੀ SDK ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ
3. **03-Model Discovery & Benchmarking** - ਮਾਡਲ ਤੁਲਨਾ ਟੂਲ
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - ਬੁਨਿਆਦੀ ਏਜੰਟ ਕੋਆਰਡੀਨੇਸ਼ਨ
6. **06-Models-as-Tools Router** - ਸਮਰਥ ਮਾਡਲ ਰਾਊਟਿੰਗ
7. **07-Direct API Client** - ਨੀਵਾਂ API ਇੰਟੀਗ੍ਰੇਸ਼ਨ
8. **08-Windows 11 Chat App** - ਮੂਲ Electron ਡੈਸਕਟਾਪ ਐਪਲੀਕੇਸ਼ਨ
9. **09-Advanced Multi-Agent System** - ਜਟਿਲ ਏਜੰਟ ਕੋਆਰਡੀਨੇਸ਼ਨ
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਹਰ ਨਮੂਨਾ Foundry Local ਨਾਲ Edge AI ਵਿਕਾਸ ਦੇ ਵੱਖ-ਵੱਖ ਪਹਲੂਆਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ।

### ਕਾਰਗੁਜ਼ਾਰੀ ਦੇ ਵਿਚਾਰ

- SLMs ਨੂੰ Edge ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਅਪਟਿਮਾਈਜ਼ ਕੀਤਾ ਗਿਆ ਹੈ (2-16GB RAM)
- ਸਥਾਨਕ ਇੰਫਰੈਂਸ 50-500ms ਜਵਾਬ ਸਮੇਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
- ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ ਤਕਨੀਕਾਂ 75% ਆਕਾਰ ਘਟਾਉਣ ਅਤੇ 85% ਕਾਰਗੁਜ਼ਾਰੀ ਰਿਟੇਨਸ਼ਨ ਪ੍ਰਾਪਤ ਕਰਦੀਆਂ ਹਨ
- ਸਥਾਨਕ ਮਾਡਲਾਂ ਨਾਲ ਰੀਅਲ-ਟਾਈਮ ਗੱਲਬਾਤ ਦੀ ਸਮਰਥਾ

### ਸੁਰੱਖਿਆ ਅਤੇ ਗੋਪਨੀਯਤਾ

- ਸਾਰਾ ਪ੍ਰੋਸੈਸਿੰਗ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਹੁੰਦਾ ਹੈ - ਕੋਈ ਡਾਟਾ ਕਲਾਉਡ ਨੂੰ ਨਹੀਂ ਭੇਜਿਆ ਜਾਂਦਾ
- ਗੋਪਨੀਯਤਾ-ਸੰਵੇਦਨਸ਼ੀਲ ਕਾਰਜਾਂ ਲਈ ਉਚਿਤ (ਹੈਲਥਕੇਅਰ, ਫਾਇਨੈਂਸ)
- ਡਾਟਾ ਸਾਰਵਭੌਮਤਾ ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਦਾ ਹੈ
- Foundry Local ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਥਾਨਕ ਹਾਰਡਵੇਅਰ 'ਤੇ ਚਲਦਾ ਹੈ

---

**ਇਹ ਇੱਕ ਸਿੱਖਿਆ ਸੰਗ੍ਰਹਿ ਹੈ ਜੋ Edge AI ਵਿਕਾਸ ਸਿਖਾਉਣ 'ਤੇ ਕੇਂਦਰਿਤ ਹੈ। ਮੁੱਖ ਯੋਗਦਾਨ ਪੈਟਰਨ ਸਿੱਖਿਆ ਸਮੱਗਰੀ ਵਿੱਚ ਸੁਧਾਰ ਅਤੇ Edge AI ਸੰਕਲਪਾਂ ਨੂੰ ਦਰਸਾਉਣ ਵਾਲੇ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨ ਸ਼ਾਮਲ/ਵਧਾਉਣ ਹਨ।**

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।