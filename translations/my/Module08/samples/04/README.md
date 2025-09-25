<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "562ac0eae12d808c9f45fbb77eb5c84f",
  "translation_date": "2025-09-25T02:24:05+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "my"
}
-->
# နမူနာ 04: Chainlit ဖြင့် Chat Application များကို ထုတ်လုပ်ခြင်း

Microsoft Foundry Local ကို အသုံးပြု၍ ထုတ်လုပ်မှုအဆင့် chat application များကို တည်ဆောက်ရန် အမျိုးမျိုးသောနည်းလမ်းများကို ပြသထားသော နမူနာတစ်ခုဖြစ်ပြီး၊ ခေတ်မီ web interface များ၊ streaming response များနှင့် နောက်ဆုံးပေါ် browser နည်းပညာများပါဝင်သည်။

## ပါဝင်သောအရာများ

- **🚀 Chainlit Chat App** (`app.py`): Streaming ပါဝင်သော ထုတ်လုပ်မှုအဆင့် chat application
- **🌐 WebGPU Demo** (`webgpu-demo/`): Hardware acceleration ဖြင့် browser-based AI inference
- **🎨 Open WebUI Integration** (`open-webui-guide.md`): ChatGPT နှင့်တူသော professional interface
- **📚 Educational Notebook** (`chainlit_app.ipynb`): Interactive learning materials

## အမြန်စတင်ရန်

### 1. Chainlit Chat Application

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

ဖွင့်ရန်: `http://localhost:8080`

### 2. WebGPU Browser Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

ဖွင့်ရန်: `http://localhost:5173`

### 3. Open WebUI Setup

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

ဖွင့်ရန်: `http://localhost:3000`

## Architecture Patterns

### Local vs Cloud ဆုံးဖြတ်ချက် Matrix

| အခြေအနေ | အကြံပြုချက် | အကြောင်းရင်း |
|----------|----------------|--------|
| **Privacy-Sensitive Data** | 🏠 Local (Foundry) | Data သည် device မှ မထွက်သွားပါ |
| **Complex Reasoning** | ☁️ Cloud (Azure OpenAI) | Model အကြီးများကို အသုံးပြုနိုင်သည် |
| **Real-time Chat** | 🏠 Local (Foundry) | Latency နည်းပြီး response မြန်သည် |
| **Document Analysis** | 🔄 Hybrid | Extraction အတွက် Local၊ Analysis အတွက် Cloud |
| **Code Generation** | 🏠 Local (Foundry) | Privacy + Specialized models |
| **Research Tasks** | ☁️ Cloud (Azure OpenAI) | ကျယ်ပြန့်သော knowledge base လိုအပ်သည် |

### နည်းပညာနှိုင်းယှဉ်မှု

| နည်းပညာ | အသုံးပြုမှု | အကျိုးကျေးဇူး | အားနည်းချက် |
|------------|----------|------|------|
| **Chainlit** | Python developer များ၊ rapid prototyping | Setup လွယ်၊ streaming support | Python-only |
| **WebGPU** | Privacy အများဆုံး၊ offline scenarios | Browser-native၊ server မလိုအပ် | Model size ကနည်း |
| **Open WebUI** | Production deployment၊ teams | Professional UI၊ user management | Docker လိုအပ် |

## လိုအပ်ချက်များ

- **Foundry Local**: Install လုပ်ပြီး run လုပ်ထား ([Download](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ နှင့် virtual environment
- **Model**: အနည်းဆုံး model တစ်ခု load လုပ်ထား (`foundry model run phi-4-mini`)
- **Browser**: WebGPU support ရှိသော Chrome/Edge
- **Docker**: Open WebUI အတွက် (optional)

## Installation & Setup

### 1. Python Environment Setup

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local Setup

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## နမူနာ Applications

### Chainlit Chat Application

**Features:**
- 🚀 **Real-time Streaming**: Token များကို generate လုပ်သည့်အခါမှာပဲ ပြသသည်
- 🛡️ **Robust Error Handling**: Error ဖြစ်ပါက recovery လွယ်ကူ
- 🎨 **Modern UI**: Professional chat interface
- 🔧 **Flexible Configuration**: Environment variables နှင့် auto-detection
- 📱 **Responsive Design**: Desktop နှင့် mobile device များတွင် အလုပ်လုပ်သည်

**Quick Start:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b-instruct
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### WebGPU Browser Demo

**Features:**
- 🌐 **Browser-native AI**: Server မလိုအပ်၊ browser အတွင်း run လုပ်သည်
- ⚡ **WebGPU Acceleration**: Hardware acceleration ရရှိနိုင်သည်
- 🔒 **Maximum Privacy**: Data သည် device မှ မထွက်သွားပါ
- 🎯 **Zero Install**: Compatible browser များတွင် အလုပ်လုပ်သည်
- 🔄 **Graceful Fallback**: WebGPU မရရှိပါက CPU သို့ fallback

**Running:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI Integration

**Features:**
- 🎨 **ChatGPT-like Interface**: Professional၊ ရိုးရှင်းသော UI
- 👥 **Multi-user Support**: User account များနှင့် conversation history
- 📁 **File Processing**: Document များကို upload လုပ်ပြီး analysis
- 🔄 **Model Switching**: Model များကို လွယ်ကူစွာ ပြောင်းနိုင်သည်
- 🐳 **Docker Deployment**: Containerized setup

**Quick Setup:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Configuration Reference

### Environment Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|----------|
| `MODEL` | အသုံးပြုမည့် model alias | `phi-4-mini` | `qwen2.5-7b-instruct` |
| `BASE_URL` | Foundry Local endpoint | Auto-detected | `http://localhost:51211` |
| `API_KEY` | API key (optional for local) | `""` | `your-api-key` |

## Troubleshooting

### Common Issues

**Chainlit Application:**

1. **Service not available:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Port conflicts:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python environment issues:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU Demo:**

1. **WebGPU not supported:**
   - Chrome/Edge 113+ သို့ update လုပ်ပါ
   - WebGPU ကို enable လုပ်ပါ: `chrome://flags/#enable-unsafe-webgpu`
   - GPU status ကိုစစ်ပါ: `chrome://gpu`
   - Demo သည် CPU သို့ automatic fallback လုပ်ပါမည်

2. **Model loading errors:**
   - Model download အတွက် internet connection ရှိကြောင်းသေချာပါ
   - Browser console တွင် CORS error များကိုစစ်ပါ
   - HTTP ဖြင့် serve လုပ်နေကြောင်း verify လုပ်ပါ (file:// မဟုတ်)

**Open WebUI:**

1. **Connection refused:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Models not appearing:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Validation Checklist

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Advanced Usage

### Performance Optimization

**Chainlit:**
- Streaming ကိုအသုံးပြု၍ performance ကိုတိုးတက်စေပါ
- High concurrency အတွက် connection pooling ကို implement လုပ်ပါ
- Model response များကို cache လုပ်ပါ
- Conversation history များကြီးလာပါက memory usage ကို monitor လုပ်ပါ

**WebGPU:**
- Privacy နှင့် speed အတွက် WebGPU ကိုအသုံးပြုပါ
- Model size ကိုသေးစေရန် quantization ကို implement လုပ်ပါ
- Background processing အတွက် Web Workers ကိုအသုံးပြုပါ
- Browser storage တွင် compiled models များကို cache လုပ်ပါ

**Open WebUI:**
- Conversation history အတွက် persistent volumes ကိုအသုံးပြုပါ
- Docker container အတွက် resource limits ကို configure လုပ်ပါ
- User data အတွက် backup strategy များကို implement လုပ်ပါ
- SSL termination အတွက် reverse proxy ကို setup လုပ်ပါ

### Integration Patterns

**Hybrid Local/Cloud:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Multi-Modal Pipeline:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Production Deployment

### Security Considerations

- **API Keys**: Environment variables ကိုအသုံးပြုပါ၊ hardcode မလုပ်ပါနှင့်
- **Network**: Production တွင် HTTPS ကိုအသုံးပြုပါ၊ team access အတွက် VPN ကိုစဉ်းစားပါ
- **Access Control**: Open WebUI အတွက် authentication ကို implement လုပ်ပါ
- **Data Privacy**: Local နှင့် cloud သို့ data သွားလာမှုကို audit လုပ်ပါ
- **Updates**: Foundry Local နှင့် containers များကို update လုပ်ထားပါ

### Monitoring and Maintenance

- **Health Checks**: Endpoint monitoring ကို implement လုပ်ပါ
- **Logging**: Component များမှ logs များကို centralize လုပ်ပါ
- **Metrics**: Response time၊ error rate၊ resource usage များကို track လုပ်ပါ
- **Backup**: Conversation data နှင့် configuration များကို regular backup လုပ်ပါ

## References and Resources

### Documentation
- [Chainlit Documentation](https://docs.chainlit.io/) - Framework guide အပြည့်အစုံ
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Microsoft ရဲ့ official docs
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU integration
- [Open WebUI Documentation](https://docs.openwebui.com/) - Advanced configuration

### Sample Files
- [`app.py`](../../../../../Module08/samples/04/app.py) - Production Chainlit application
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Educational notebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Browser-based AI inference
- [`open-webui-guide.md`](./open-webui-guide.md) - Complete Open WebUI setup

### Related Samples
- [Session 4 Documentation](../../04.CuttingEdgeModels.md) - Session guide အပြည့်အစုံ
- [Foundry Local Samples](https://github.com/microsoft/foundry-local/tree/main/samples) - Official samples

---

