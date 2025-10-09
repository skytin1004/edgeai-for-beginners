<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c8a73e11384e3462674273498d0f9a6",
  "translation_date": "2025-10-09T12:54:34+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "th"
}
-->
# เซสชันที่ 1: เริ่มต้นใช้งาน Foundry Local

## บทคัดย่อ

เริ่มต้นการเดินทางของคุณกับ Foundry Local โดยการติดตั้งและตั้งค่าบน Windows 11 เรียนรู้วิธีการตั้งค่า CLI เปิดใช้งานการเร่งความเร็วฮาร์ดแวร์ และแคชโมเดลเพื่อการประมวลผลในเครื่องที่รวดเร็วขึ้น เซสชันนี้จะพาคุณไปสู่การรันโมเดลต่างๆ เช่น Phi, Qwen, DeepSeek และ GPT-OSS-20B ด้วยคำสั่ง CLI ที่สามารถทำซ้ำได้

## วัตถุประสงค์การเรียนรู้

เมื่อจบเซสชันนี้ คุณจะสามารถ:

- **ติดตั้งและตั้งค่า**: ตั้งค่า Foundry Local บน Windows 11 ด้วยการตั้งค่าประสิทธิภาพที่เหมาะสม
- **เชี่ยวชาญการใช้งาน CLI**: ใช้ Foundry Local CLI สำหรับการจัดการและการปรับใช้โมเดล
- **เปิดใช้งานการเร่งความเร็วฮาร์ดแวร์**: ตั้งค่าการเร่งความเร็ว GPU ด้วย ONNXRuntime หรือ WebGPU
- **ปรับใช้โมเดลหลายตัว**: รันโมเดล phi-4, GPT-OSS-20B, Qwen และ DeepSeek ในเครื่อง
- **สร้างแอปแรกของคุณ**: ปรับตัวอย่างที่มีอยู่ให้ใช้ Foundry Local Python SDK

# ทดสอบโมเดล (การป้อนคำถามแบบไม่โต้ตอบ)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 หรือใหม่กว่า)
# แสดงรายการโมเดลในแคตตาล็อก (โมเดลที่โหลดแล้วจะปรากฏหลังจากรัน)
foundry model list
## NOTE: ขณะนี้ยังไม่มี `--running` flag โดยเฉพาะ; หากต้องการดูว่าโมเดลใดที่ถูกโหลด ให้เริ่มแชทหรือดูบันทึกการให้บริการ
- ติดตั้ง Python 3.10+ แล้ว
- Visual Studio Code พร้อมส่วนขยาย Python
- สิทธิ์ผู้ดูแลระบบสำหรับการติดตั้ง

### (ตัวเลือก) ตัวแปรสภาพแวดล้อม

สร้างไฟล์ `.env` (หรือกำหนดใน shell) เพื่อทำให้สคริปต์สามารถพกพาได้:
# เปรียบเทียบคำตอบ (การป้อนคำถามแบบไม่โต้ตอบ)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| ตัวแปร | วัตถุประสงค์ | ตัวอย่าง |
|--------|---------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | ชื่อเล่นโมเดลที่ต้องการ (แคตตาล็อกจะเลือกตัวเลือกที่ดีที่สุดโดยอัตโนมัติ) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | กำหนดค่า endpoint (หากไม่กำหนดจะใช้ค่าจาก manager โดยอัตโนมัติ) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | เปิดใช้งานการสตรีมเดโม | `true` |

> หาก `FOUNDRY_LOCAL_ENDPOINT=auto` (หรือไม่ได้กำหนดค่า) เราจะดึงค่าจาก SDK manager

## ลำดับการสาธิต (30 นาที)

### 1. ติดตั้ง Foundry Local และตรวจสอบการตั้งค่า CLI (10 นาที)

# แสดงรายการโมเดลที่แคชไว้
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (ตัวอย่าง / หากรองรับ)**

หากมีแพ็กเกจ macOS แบบ native ให้ตรวจสอบเอกสารทางการสำหรับข้อมูลล่าสุด:

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

หากยังไม่มีไบนารี native สำหรับ macOS คุณยังสามารถ:
1. ใช้ Windows 11 ARM/Intel VM (Parallels / UTM) และทำตามขั้นตอนของ Windows 
2. รันโมเดลผ่าน container (หากมีการเผยแพร่ภาพ container) และตั้งค่า `FOUNDRY_LOCAL_ENDPOINT` ไปยังพอร์ตที่เปิดใช้งาน

**สร้างสภาพแวดล้อมเสมือน Python (ข้ามแพลตฟอร์ม)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

อัปเกรด pip และติดตั้ง dependencies หลัก:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### ขั้นตอน 1.2: ตรวจสอบการติดตั้ง

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### ขั้นตอน 1.3: ตั้งค่าสภาพแวดล้อม

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### การเริ่มต้นใช้งาน SDK (แนะนำ)

แทนที่จะเริ่มบริการและรันโมเดลด้วยตนเอง **Foundry Local Python SDK** สามารถช่วยเริ่มต้นทุกอย่างได้:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

หากคุณต้องการควบคุมอย่างชัดเจน คุณยังสามารถใช้ CLI + OpenAI client ตามที่แสดงในภายหลัง

### 2. เปิดใช้งานการเร่งความเร็ว GPU (5 นาที)

#### ขั้นตอน 2.1: ตรวจสอบความสามารถของฮาร์ดแวร์

```powershell
# Check available compute providers
foundry system info

# List GPU capabilities
foundry system gpu-info
```

#### ขั้นตอน 2.2: ตั้งค่าการเร่งความเร็วฮาร์ดแวร์

```powershell
# Enable ONNX Runtime GPU (if NVIDIA GPU available)
foundry config set compute.onnx.enable_gpu true

# Enable WebGPU for broader hardware support
foundry config set compute.webgpu.enabled true

# Verify configuration
foundry config list
```

### 3. รันโมเดลในเครื่องผ่าน CLI (10 นาที)

#### ขั้นตอน 3.1: ปรับใช้โมเดล Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### ขั้นตอน 3.2: ปรับใช้ GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### ขั้นตอน 3.3: โหลดโมเดลเพิ่มเติม

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. โครงการเริ่มต้น: ปรับ 01-run-phi สำหรับ Foundry Local (5 นาที)

#### ขั้นตอน 4.1: สร้างแอปพลิเคชันแชทพื้นฐาน

สร้าง `samples/01-foundry-quickstart/chat_quickstart.py` (อัปเดตให้ใช้ manager หากมี):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### ขั้นตอน 4.2: ทดสอบแอปพลิเคชัน

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## แนวคิดสำคัญที่ครอบคลุม

### 1. สถาปัตยกรรม Foundry Local

- **Local Inference Engine**: รันโมเดลทั้งหมดในอุปกรณ์ของคุณ
- **ความเข้ากันได้กับ OpenAI SDK**: การผสานรวมที่ราบรื่นกับโค้ด OpenAI ที่มีอยู่
- **การจัดการโมเดล**: ดาวน์โหลด แคช และรันโมเดลหลายตัวได้อย่างมีประสิทธิภาพ
- **การปรับแต่งฮาร์ดแวร์**: ใช้การเร่งความเร็ว GPU, NPU และ CPU

### 2. อ้างอิงคำสั่ง CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. การผสานรวม Python SDK

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## การแก้ไขปัญหาทั่วไป

### ปัญหา 1: "ไม่พบคำสั่ง Foundry"

**วิธีแก้ไข:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### ปัญหา 2: "ไม่สามารถโหลดโมเดลได้"

**วิธีแก้ไข:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### ปัญหา 3: "การเชื่อมต่อถูกปฏิเสธที่ localhost:5273"

**วิธีแก้ไข:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## เคล็ดลับการเพิ่มประสิทธิภาพ

### 1. กลยุทธ์การเลือกโมเดล

- **Phi-4-mini**: เหมาะสำหรับงานทั่วไป ใช้หน่วยความจำน้อย
- **Qwen2.5-0.5b**: การประมวลผลเร็วที่สุด ใช้ทรัพยากรน้อย
- **GPT-OSS-20B**: คุณภาพสูงสุด ต้องการทรัพยากรมาก
- **DeepSeek-Coder**: ปรับแต่งสำหรับงานเขียนโปรแกรม

### 2. การปรับแต่งฮาร์ดแวร์

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. การติดตามประสิทธิภาพ

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### การปรับปรุงเพิ่มเติม (ตัวเลือก)

| การปรับปรุง | คืออะไร | วิธีการ |
|-------------|---------|---------|
| Utilities ร่วมกัน | ลบโค้ด client/bootstrap ที่ซ้ำซ้อน | ใช้ `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| การมองเห็นการใช้ Token | สอนการคิดต้นทุน/ประสิทธิภาพตั้งแต่ต้น | ตั้งค่า `SHOW_USAGE=1` เพื่อแสดง token ที่ใช้ |
| การเปรียบเทียบที่กำหนดได้ | การวัดผลและการตรวจสอบย้อนกลับที่เสถียร | ใช้ `temperature=0`, `top_p=1`, ข้อความ prompt ที่สม่ำเสมอ |
| ความล่าช้าของ Token แรก | ตัวชี้วัดการตอบสนองที่รับรู้ | ปรับสคริปต์ benchmark ด้วยการสตรีม (`BENCH_STREAM=1`) |
| การลองใหม่เมื่อเกิดข้อผิดพลาดชั่วคราว | การสาธิตที่ทนทานในกรณีเริ่มต้นเย็น | `RETRY_ON_FAIL=1` (ค่าเริ่มต้น) และปรับ `RETRY_BACKOFF` |
| การทดสอบเบื้องต้น | ตรวจสอบความถูกต้องของฟังก์ชันหลักอย่างรวดเร็ว | รัน `python Workshop/tests/smoke.py` ก่อนการเวิร์กชอป |
| โปรไฟล์ชื่อเล่นโมเดล | เปลี่ยนชุดโมเดลระหว่างเครื่องได้อย่างรวดเร็ว | รักษา `.env` ด้วย `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| ประสิทธิภาพการแคช | หลีกเลี่ยงการอุ่นเครื่องซ้ำในรอบการรันหลายตัวอย่าง | Utilities cache managers; ใช้ซ้ำในสคริปต์/โน้ตบุ๊ก |
| การอุ่นเครื่องครั้งแรก | ลดความล่าช้าสูงสุด p95 | ใช้ prompt เล็กๆ หลังจากสร้าง `FoundryLocalManager` |

ตัวอย่างการอุ่นเครื่องที่กำหนดได้ (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

คุณควรเห็นผลลัพธ์ที่คล้ายกันและจำนวน token ที่เหมือนกันในครั้งที่สอง ยืนยันความเสถียร

## ขั้นตอนถัดไป

หลังจากจบเซสชันนี้:

1. **สำรวจเซสชันที่ 2**: สร้างโซลูชัน AI ด้วย Azure AI Foundry RAG
2. **ลองโมเดลต่างๆ**: ทดลองกับ Qwen, DeepSeek และกลุ่มโมเดลอื่นๆ
3. **เพิ่มประสิทธิภาพ**: ปรับแต่งการตั้งค่าสำหรับฮาร์ดแวร์ของคุณ
4. **สร้างแอปพลิเคชันของคุณเอง**: ใช้ Foundry Local SDK ในโครงการของคุณ

## ทรัพยากรเพิ่มเติม

### เอกสาร
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### โค้ดตัวอย่าง
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### ชุมชน
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**ระยะเวลาเซสชัน**: 30 นาทีสำหรับการปฏิบัติ + 15 นาทีสำหรับถาม-ตอบ  
**ระดับความยาก**: ผู้เริ่มต้น  
**ข้อกำหนดเบื้องต้น**: Windows 11, Python 3.10+, สิทธิ์ผู้ดูแลระบบ  

## ตัวอย่างสถานการณ์และการจับคู่เวิร์กชอป

| สคริปต์/โน้ตบุ๊กเวิร์กชอป | สถานการณ์ | เป้าหมาย | ตัวอย่างอินพุต | ชุดข้อมูลที่ต้องการ |
|----------------------------|-----------|----------|----------------|---------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | ทีม IT ภายในที่ประเมินการประมวลผลในเครื่องสำหรับพอร์ทัลการประเมินความเป็นส่วนตัว | พิสูจน์ว่า SLM ในเครื่องตอบสนองภายในเวลาน้อยกว่าหนึ่งวินาทีใน prompt มาตรฐาน | "List two benefits of local inference." | ไม่มี (prompt เดี่ยว) |
| โค้ดการปรับ Quickstart | นักพัฒนาที่กำลังย้ายสคริปต์ OpenAI ที่มีอยู่ไปยัง Foundry Local | แสดงความเข้ากันได้แบบ drop-in | "Give two benefits of local inference." | มีเพียง prompt ในตัว |

### เรื่องราวสถานการณ์
ทีมความปลอดภัยและการปฏิบัติตามกฎระเบียบต้องตรวจสอบว่าข้อมูลต้นแบบที่ละเอียดอ่อนสามารถประมวลผลในเครื่องได้หรือไม่ พวกเขารันสคริปต์ bootstrap ด้วย prompt หลายตัว (ความเป็นส่วนตัว, ความล่าช้า, ต้นทุน) โดยใช้โหมด deterministic temperature=0 เพื่อจับผลลัพธ์พื้นฐานสำหรับการเปรียบเทียบในภายหลัง (การวัดผลในเซสชันที่ 3 และการเปรียบเทียบ SLM กับ LLM ในเซสชันที่ 4)

### ชุด Prompt ขั้นต่ำในรูปแบบ JSON (ตัวเลือก)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

ใช้รายการนี้เพื่อสร้างลูปการประเมินที่สามารถทำซ้ำได้หรือเพื่อเริ่มต้นการทดสอบการถดถอยในอนาคต

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้