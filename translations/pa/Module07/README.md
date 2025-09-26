<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:31:29+00:00",
  "source_file": "Module07/README.md",
  "language_code": "pa"
}
-->
# ਚੈਪਟਰ 07 : EdgeAI ਨਮੂਨੇ

Edge AI ਕਿਨਾਰੇ ਕੰਪਿਊਟਿੰਗ ਨਾਲ ਕਲਾਉਡ ਕਨੈਕਟਿਵਿਟੀ ਤੋਂ ਬਿਨਾਂ ਸਿੱਧੇ ਡਿਵਾਈਸਾਂ 'ਤੇ ਸਮਰੱਥ ਪ੍ਰੋਸੈਸਿੰਗ ਨੂੰ ਯੋਗ ਬਣਾਉਂਦੀ ਹੈ। ਇਹ ਚੈਪਟਰ ਵੱਖ-ਵੱਖ ਪਲੇਟਫਾਰਮਾਂ ਅਤੇ ਫਰੇਮਵਰਕਾਂ 'ਤੇ ਪੰਜ ਵਿਲੱਖਣ EdgeAI ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ, ਜੋ ਕਿਨਾਰੇ 'ਤੇ AI ਮਾਡਲ ਚਲਾਉਣ ਦੀ ਵਰਤੋਂ ਅਤੇ ਤਾਕਤ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ।

## 1. NVIDIA Jetson Orin Nano ਵਿੱਚ EdgeAI

NVIDIA Jetson Orin Nano ਕਿਨਾਰੇ AI ਕੰਪਿਊਟਿੰਗ ਵਿੱਚ ਇੱਕ ਬ੍ਰੇਕਥਰੂ ਹੈ, ਜੋ 67 TOPS ਤੱਕ AI ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਇੱਕ ਛੋਟੇ, ਕਰੈਡਿਟ-ਕਾਰਡ-ਆਕਾਰ ਦੇ ਰੂਪ ਵਿੱਚ ਪੇਸ਼ ਕਰਦਾ ਹੈ। ਇਹ ਸ਼ਕਤੀਸ਼ਾਲੀ Edge AI ਪਲੇਟਫਾਰਮ ਹੌਬੀਸਟ, ਵਿਦਿਆਰਥੀਆਂ ਅਤੇ ਪੇਸ਼ੇਵਰ ਡਿਵੈਲਪਰਾਂ ਲਈ ਜਨਰੇਟਿਵ AI ਵਿਕਾਸ ਨੂੰ ਲੋਕਤੰਤਰਤ ਕਰਦਾ ਹੈ।

### ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ
- 67 TOPS ਤੱਕ AI ਪ੍ਰਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ—ਇਸਦੇ ਪੂਰਵਜ ਨਾਲੋਂ 1.7X ਸੁਧਾਰ
- 1024 CUDA ਕੋਰ ਅਤੇ 32 Tensor ਕੋਰ AI ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ
- 6-ਕੋਰ Arm Cortex-A78AE v8.2 64-ਬਿਟ CPU 1.5 GHz ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਫ੍ਰੀਕਵੈਂਸੀ ਨਾਲ
- ਸਿਰਫ $249 ਦੀ ਕੀਮਤ, ਡਿਵੈਲਪਰਾਂ, ਵਿਦਿਆਰਥੀਆਂ ਅਤੇ ਮੈਕਰਾਂ ਲਈ ਸਭ ਤੋਂ ਸਸਤੀ ਅਤੇ ਪਹੁੰਚਯੋਗ ਪਲੇਟਫਾਰਮ

### ਐਪਲੀਕੇਸ਼ਨ
Jetson Orin Nano ਆਧੁਨਿਕ ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਨੂੰ ਚਲਾਉਣ ਵਿੱਚ ਸ਼ਾਨਦਾਰ ਹੈ, ਜਿਸ ਵਿੱਚ ਵਿਜ਼ਨ ਟ੍ਰਾਂਸਫਾਰਮਰ, ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ, ਅਤੇ ਵਿਜ਼ਨ-ਭਾਸ਼ਾ ਮਾਡਲ ਸ਼ਾਮਲ ਹਨ। ਇਹ ਖਾਸ ਤੌਰ 'ਤੇ GenAI ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਹੁਣ ਤੁਸੀਂ ਕਈ LLMs ਨੂੰ ਹਥੇਲੀ ਦੇ ਆਕਾਰ ਦੇ ਡਿਵਾਈਸ 'ਤੇ ਚਲਾ ਸਕਦੇ ਹੋ। ਪ੍ਰਸਿੱਧ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਵਿੱਚ AI-ਚਲਿਤ ਰੋਬੋਟਿਕਸ, ਸਮਾਰਟ ਡ੍ਰੋਨ, ਇੰਟੈਲੀਜੈਂਟ ਕੈਮਰੇ, ਅਤੇ ਸਵੈ-ਚਾਲਤ ਕਿਨਾਰੇ ਡਿਵਾਈਸ ਸ਼ਾਮਲ ਹਨ।

**ਹੋਰ ਜਾਣੋ**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. .NET MAUI ਅਤੇ ONNX Runtime GenAI ਨਾਲ ਮੋਬਾਈਲ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ EdgeAI

ਇਹ ਹੱਲ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਵੇਂ .NET MAUI (ਮਲਟੀ-ਪਲੇਟਫਾਰਮ ਐਪ UI) ਅਤੇ ONNX Runtime GenAI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਨਰੇਟਿਵ AI ਅਤੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਨੂੰ ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਮੋਬਾਈਲ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ ਪਹੁੰਚ .NET ਡਿਵੈਲਪਰਾਂ ਨੂੰ Android ਅਤੇ iOS ਡਿਵਾਈਸਾਂ 'ਤੇ ਨੈਟਿਵ ਤੌਰ 'ਤੇ ਚਲਣ ਵਾਲੀਆਂ ਸੁਧਾਰਤ AI-ਚਲਿਤ ਮੋਬਾਈਲ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਯੋਗ ਬਣਾਉਂਦੀ ਹੈ।

### ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ
- .NET MAUI ਫਰੇਮਵਰਕ 'ਤੇ ਬਣਾਇਆ ਗਿਆ, ਜੋ Android ਅਤੇ iOS ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਇੱਕ ਸਿੰਗਲ ਕੋਡਬੇਸ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
- ONNX Runtime GenAI ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਨੂੰ ਸਿੱਧੇ ਮੋਬਾਈਲ ਡਿਵਾਈਸਾਂ 'ਤੇ ਚਲਾਉਣ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ
- ਮੋਬਾਈਲ ਡਿਵਾਈਸਾਂ ਲਈ CPU, GPU, ਅਤੇ ਵਿਸ਼ੇਸ਼ ਮੋਬਾਈਲ AI ਪ੍ਰੋਸੈਸਰ ਸਮੇਤ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਐਕਸਲੇਰੇਟਰਾਂ ਦਾ ਸਮਰਥਨ
- ONNX Runtime ਰਾਹੀਂ iOS ਲਈ CoreML ਅਤੇ Android ਲਈ NNAPI ਵਰਗੀਆਂ ਪਲੇਟਫਾਰਮ-ਵਿਸ਼ੇਸ਼ ਸੁਧਾਰਾਂ
- ਪੂਰੀ ਜਨਰੇਟਿਵ AI ਲੂਪ ਨੂੰ ਲਾਗੂ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਪ੍ਰੀ ਅਤੇ ਪੋਸਟ ਪ੍ਰੋਸੈਸਿੰਗ, ਇੰਫਰੈਂਸ, ਲੌਜਿਟਸ ਪ੍ਰੋਸੈਸਿੰਗ, ਖੋਜ ਅਤੇ ਸੈਂਪਲਿੰਗ, ਅਤੇ KV ਕੈਸ਼ ਮੈਨੇਜਮੈਂਟ ਸ਼ਾਮਲ ਹਨ

### ਵਿਕਾਸ ਦੇ ਫਾਇਦੇ
.NET MAUI ਪਹੁੰਚ ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਆਪਣੇ ਮੌਜੂਦਾ C# ਅਤੇ .NET ਹੁਨਰਾਂ ਨੂੰ ਵਰਤਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ ਜਦੋਂ ਕਿ ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ। ONNX Runtime GenAI ਫਰੇਮਵਰਕ ਕਈ ਮਾਡਲ ਆਰਕੀਟੈਕਚਰਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ Llama, Mistral, Phi, Gemma, ਅਤੇ ਹੋਰ ਕਈ ਸ਼ਾਮਲ ਹਨ। ARM64 ਕਰਨਲਾਂ ਨੂੰ ਸੁਧਾਰਿਆ ਗਿਆ ਹੈ ਜੋ INT4 ਕੁਆਂਟਾਈਜ਼ਡ ਮੈਟ੍ਰਿਕਸ ਮਲਟੀਪਲੀਕੇਸ਼ਨ ਨੂੰ ਤੇਜ਼ ਕਰਦੇ ਹਨ, ਮੋਬਾਈਲ ਹਾਰਡਵੇਅਰ 'ਤੇ ਕੁਸ਼ਲ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹਨ ਜਦੋਂ ਕਿ ਜਾਣ-ਪਛਾਣ ਵਾਲੇ .NET ਵਿਕਾਸ ਅਨੁਭਵ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦੇ ਹਨ।

### ਵਰਤੋਂ ਦੇ ਕੇਸ
ਇਹ ਹੱਲ ਉਹ ਡਿਵੈਲਪਰਾਂ ਲਈ ਆਦਰਸ਼ ਹੈ ਜੋ .NET ਤਕਨਾਲੋਜੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ AI-ਚਲਿਤ ਮੋਬਾਈਲ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹਨ, ਜਿਸ ਵਿੱਚ ਇੰਟੈਲੀਜੈਂਟ ਚੈਟਬੋਟ, ਚਿੱਤਰ ਪਛਾਣ ਐਪਸ, ਭਾਸ਼ਾ ਅਨੁਵਾਦ ਟੂਲ, ਅਤੇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਡਿਵਾਈਸ 'ਤੇ ਚਲਣ ਵਾਲੇ ਪੈਰਸਨਲਾਈਜ਼ਡ ਰਿਕਮੈਂਡੇਸ਼ਨ ਸਿਸਟਮ ਸ਼ਾਮਲ ਹਨ ਜੋ ਗੋਪਨੀਯਤਾ ਅਤੇ ਆਫਲਾਈਨ ਸਮਰੱਥਾ ਨੂੰ ਵਧਾਉਂਦੇ ਹਨ।

**ਹੋਰ ਜਾਣੋ**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. Azure ਵਿੱਚ EdgeAI ਨਾਲ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲ ਇੰਜਨ

Microsoft ਦਾ Azure-ਅਧਾਰਤ EdgeAI ਹੱਲ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲ (SLMs) ਨੂੰ ਕਲਾਉਡ-ਕਿਨਾਰੇ ਹਾਈਬ੍ਰਿਡ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਕੁਸ਼ਲਤਾਪੂਰਵਕ ਤੈਨਾਤ ਕਰਨ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦਾ ਹੈ। ਇਹ ਪਹੁੰਚ ਕਲਾਉਡ-ਪੈਮਾਨੇ AI ਸੇਵਾਵਾਂ ਅਤੇ ਕਿਨਾਰੇ ਤੈਨਾਤੀ ਦੀਆਂ ਜ਼ਰੂਰਤਾਂ ਦੇ ਵਿਚਕਾਰ ਪੂਲ ਬਣਾਉਂਦੀ ਹੈ।

### ਆਰਕੀਟੈਕਚਰ ਦੇ ਫਾਇਦੇ
- Azure AI ਸੇਵਾਵਾਂ ਨਾਲ ਬੇਰੋਕਟੋਕ ਇੰਟਿਗ੍ਰੇਸ਼ਨ
- ONNX Runtime ਨਾਲ SLMs/LLMs ਅਤੇ ਮਲਟੀ-ਮੋਡਲ ਮਾਡਲਾਂ ਨੂੰ ਡਿਵਾਈਸ 'ਤੇ ਅਤੇ ਕਲਾਉਡ ਵਿੱਚ ਚਲਾਓ
- ਇੰਟਰਪ੍ਰਾਈਜ਼-ਪੈਮਾਨੇ ਤੈਨਾਤੀ ਲਈ ਸੁਧਾਰਿਆ ਗਿਆ
- ਮਾਡਲ ਅਪਡੇਟ ਅਤੇ ਮੈਨੇਜਮੈਂਟ ਲਈ ਲਗਾਤਾਰ ਸਮਰਥਨ

### ਵਰਤੋਂ ਦੇ ਕੇਸ
Azure EdgeAI ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਉਹ ਸਥਿਤੀਆਂ ਵਿੱਚ ਸ਼ਾਨਦਾਰ ਹੈ ਜਿਨ੍ਹਾਂ ਨੂੰ ਕਲਾਉਡ ਮੈਨੇਜਮੈਂਟ ਸਮਰਥਨ ਦੇ ਨਾਲ ਇੰਟਰਪ੍ਰਾਈਜ਼-ਗ੍ਰੇਡ AI ਤੈਨਾਤੀ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਇਸ ਵਿੱਚ ਇੰਟੈਲੀਜੈਂਟ ਦਸਤਾਵੇਜ਼ ਪ੍ਰੋਸੈਸਿੰਗ, ਰੀਅਲ-ਟਾਈਮ ਵਿਸ਼ਲੇਸ਼ਣ, ਅਤੇ ਹਾਈਬ੍ਰਿਡ AI ਵਰਕਫਲੋਜ਼ ਸ਼ਾਮਲ ਹਨ ਜੋ ਕਲਾਉਡ ਅਤੇ ਕਿਨਾਰੇ ਕੰਪਿਊਟਿੰਗ ਸਰੋਤਾਂ ਦਾ ਲਾਭ ਲੈਂਦੇ ਹਨ।

**ਹੋਰ ਜਾਣੋ**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. Windows ML ਨਾਲ EdgeAI](./windowdeveloper.md)

Windows ML Microsoft ਦਾ ਕਿਨਾਰੇ 'ਤੇ ਮਾਡਲ ਇੰਫਰੈਂਸ ਲਈ ਅਨੁਕੂਲਤ ਰਨਟਾਈਮ ਹੈ ਜੋ PC ਹਾਰਡਵੇਅਰ 'ਤੇ ਸਧਾਰਨ ਤੈਨਾਤੀ ਨੂੰ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਪਲੇਟਫਾਰਮ ਡਿਵੈਲਪਰਾਂ ਨੂੰ Windows ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ ਜੋ PC ਹਾਰਡਵੇਅਰ ਦੇ ਪੂਰੇ ਸਪੈਕਟ੍ਰਮ ਦਾ ਲਾਭ ਲੈਂਦੇ ਹਨ।

### ਪਲੇਟਫਾਰਮ ਸਮਰੱਥਾਵਾਂ
- ਸਾਰੇ Windows 11 PCs 'ਤੇ ਕੰਮ ਕਰਦਾ ਹੈ ਜੋ ਵਰਜਨ 24H2 (ਬਿਲਡ 26100) ਜਾਂ ਵੱਧ 'ਤੇ ਚੱਲਦੇ ਹਨ
- ਸਾਰੇ x64 ਅਤੇ ARM64 PC ਹਾਰਡਵੇਅਰ 'ਤੇ ਕੰਮ ਕਰਦਾ ਹੈ, ਭਾਵੇਂ PCs ਵਿੱਚ NPUs ਜਾਂ GPUs ਨਾ ਹੋਣ
- ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਆਪਣੇ ਮਾਡਲ ਲਿਆਉਣ ਅਤੇ AMD, Intel, NVIDIA ਅਤੇ Qualcomm ਸਮੇਤ ਸਿਲਿਕਨ ਭਾਈਚਾਰਾ ਪ੍ਰਣਾਲੀ 'ਤੇ ਕੁਸ਼ਲਤਾਪੂਰਵਕ ਤੈਨਾਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ
- ਇੰਫਰਾਸਟਰਕਚਰ APIs ਦਾ ਲਾਭ ਲੈ ਕੇ, ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਸਿਲਿਕਨ ਨੂੰ ਟਾਰਗਟ ਕਰਨ ਲਈ ਆਪਣੇ ਐਪ ਦੀਆਂ ਕਈ ਬਿਲਡ ਬਣਾਉਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ

### ਡਿਵੈਲਪਰ ਫਾਇਦੇ
Windows ML ਹਾਰਡਵੇਅਰ ਅਤੇ ਐਗਜ਼ਿਕਿਊਸ਼ਨ ਪ੍ਰੋਵਾਈਡਰਾਂ ਨੂੰ ਅਬਸਟਰੈਕਟ ਕਰਦਾ ਹੈ, ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੇ ਕੋਡ ਲਿਖਣ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰ ਸਕੋ। ਇਸ ਤੋਂ ਇਲਾਵਾ, Windows ML ਆਪਣੇ ਆਪ ਨੂੰ ਨਵੇਂ NPUs, GPUs, ਅਤੇ CPUs ਦਾ ਸਮਰਥਨ ਕਰਨ ਲਈ ਅਪਡੇਟ ਕਰਦਾ ਹੈ ਜਦੋਂ ਉਹ ਜਾਰੀ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਪਲੇਟਫਾਰਮ Windows ਹਾਰਡਵੇਅਰ ਭਾਈਚਾਰਾ ਵਿੱਚ AI ਵਿਕਾਸ ਲਈ ਇੱਕ ਇਕਰੂਪ ਫਰੇਮਵਰਕ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

**ਹੋਰ ਜਾਣੋ**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md) - Windows Edge AI ਵਿਕਾਸ ਲਈ ਵਿਸਤ੍ਰਿਤ ਗਾਈਡ

## [5. Foundry Local Applications ਨਾਲ EdgeAI](./foundrylocal.md)

Foundry Local Windows ਅਤੇ Mac ਡਿਵੈਲਪਰਾਂ ਨੂੰ .NET ਵਿੱਚ Retrieval Augmented Generation (RAG) ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜੋ ਸਥਾਨਕ ਸਰੋਤਾਂ ਨੂੰ ਸੈਮੈਂਟਿਕ ਖੋਜ ਸਮਰੱਥਾਵਾਂ ਨਾਲ ਜੋੜਦਾ ਹੈ। ਇਹ ਪਹੁੰਚ ਗੋਪਨੀਯਤਾ-ਕੇਂਦਰਿਤ AI ਹੱਲ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ ਜੋ ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਥਾਨਕ ਢਾਂਚੇ 'ਤੇ ਕੰਮ ਕਰਦੀ ਹੈ।

### ਤਕਨੀਕੀ ਆਰਕੀਟੈਕਚਰ
- Phi ਭਾਸ਼ਾ ਮਾਡਲ, ਸਥਾਨਕ ਐਮਬੈਡਿੰਗ, ਅਤੇ ਸੈਮੈਂਟਿਕ Kernel ਨੂੰ ਜੋੜਦਾ ਹੈ RAG ਸਥਿਤੀ ਬਣਾਉਣ ਲਈ
- ਸਮੱਗਰੀ ਅਤੇ ਇਸਦੇ ਸੈਮੈਂਟਿਕ ਅਰਥ ਨੂੰ ਦਰਸਾਉਣ ਵਾਲੇ ਫਲੋਟਿੰਗ-ਪੌਇੰਟ ਮੁੱਲਾਂ ਦੇ ਐਰੇ (ਵੇਕਟਰ) ਵਜੋਂ ਐਮਬੈਡਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ
- ਸੈਮੈਂਟਿਕ Kernel ਮੁੱਖ ਆਰਕੈਸਟਰੇਟਰ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ, Phi ਅਤੇ Smart Components ਨੂੰ ਜੋੜ ਕੇ ਇੱਕ ਸਧਾਰਨ RAG ਪਾਈਪਲਾਈਨ ਬਣਾਉਂਦਾ ਹੈ
- ਸਥਾਨਕ ਵੇਕਟਰ ਡਾਟਾਬੇਸਾਂ ਲਈ ਸਮਰਥਨ ਜਿਸ ਵਿੱਚ SQLite ਅਤੇ Qdrant ਸ਼ਾਮਲ ਹਨ

### ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਦੇ ਫਾਇਦੇ
RAG, ਜਾਂ Retrieval Augmented Generation, ਸਿਰਫ "ਕੁਝ ਚੀਜ਼ਾਂ ਨੂੰ ਖੋਜੋ ਅਤੇ ਇਸਨੂੰ ਪ੍ਰੋਮਪਟ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ" ਦਾ ਇੱਕ ਸਧਾਰਨ ਤਰੀਕਾ ਹੈ। ਇਹ ਸਥਾਨਕ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਡਾਟਾ ਗੋਪਨੀਯਤਾ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਜਦੋਂ ਕਿ ਕਸਟਮ ਨੋਲੇਜ ਬੇਸਾਂ 'ਤੇ ਅਧਾਰਿਤ ਸਮਰੱਥ ਜਵਾਬ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ। ਇਹ ਪਹੁੰਚ ਖਾਸ ਤੌਰ 'ਤੇ ਇੰਟਰਪ੍ਰਾਈਜ਼ ਸਥਿਤੀਆਂ ਲਈ ਮੁੱਲਵਾਨ ਹੈ ਜਿਨ੍ਹਾਂ ਨੂੰ ਡਾਟਾ ਸਾਰਵਭੌਮਤਾ ਅਤੇ ਆਫਲਾਈਨ ਢੰਗ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

**ਹੋਰ ਜਾਣੋ**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local Windows 'ਤੇ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਮਾਡਲ ਚਲਾਉਣ ਲਈ ONNX Runtime ਦੁਆਰਾ ਸੰਚਾਲਿਤ OpenAI-ਅਨੁਕੂਲ REST ਸਰਵਰ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਹੇਠਾਂ ਇੱਕ ਤੇਜ਼, ਪ੍ਰਮਾਣਿਤ ਸਾਰ ਹੈ; ਪੂਰੇ ਵੇਰਵੇ ਲਈ ਅਧਿਕਾਰਤ ਦਸਤਾਵੇਜ਼ ਵੇਖੋ।

- ਸ਼ੁਰੂ ਕਰੋ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- ਆਰਕੀਟੈਕਚਰ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI ਰੈਫਰੈਂਸ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- ਇਸ ਰਿਪੋ ਵਿੱਚ ਪੂਰੀ Windows ਗਾਈਡ: [foundrylocal.md](./foundrylocal.md)

Windows 'ਤੇ ਇੰਸਟਾਲ ਜਾਂ ਅਪਗ੍ਰੇਡ ਕਰੋ (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

CLI ਸ਼੍ਰੇਣੀਆਂ ਦੀ ਜਾਂਚ ਕਰੋ:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

ਮਾਡਲ ਚਲਾਓ ਅਤੇ ਡਾਇਨਾਮਿਕ ਐਂਡਪੌਇੰਟ ਦੀ ਖੋਜ ਕਰੋ:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ ਦੇਖਣ ਲਈ ਤੇਜ਼ REST ਜਾਂਚ (PORT ਨੂੰ ਸਥਿਤੀ ਤੋਂ ਬਦਲੋ):
```cmd
curl -s http://localhost:PORT/v1/models
```

ਸੁਝਾਅ:
- SDK ਇੰਟਿਗ੍ਰੇਸ਼ਨ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- ਆਪਣਾ ਮਾਡਲ ਲਿਆਓ (ਕੰਪਾਇਲ): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI ਵਿਕਾਸ ਸਰੋਤ

Windows ਪਲੇਟਫਾਰਮ ਨੂੰ ਟਾਰਗਟ ਕਰਨ ਵਾਲੇ ਡਿਵੈਲਪਰਾਂ ਲਈ, ਅਸੀਂ Windows EdgeAI ਭਾਈਚਾਰਾ ਨੂੰ ਕਵਰ ਕਰਨ ਵਾਲੀ ਇੱਕ ਵਿਸਤ੍ਰਿਤ ਗਾਈਡ ਬਣਾਈ ਹੈ। ਇਹ ਸਰੋਤ Windows AI Foundry, APIs, ਟੂਲ, ਅਤੇ Windows 'ਤੇ EdgeAI ਵਿਕਾਸ ਲਈ ਸ੍ਰੇਸ਼ਠ ਅਭਿਆਸਾਂ ਬਾਰੇ ਵਿਸਤ੍ਰਿਤ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

### Windows AI Foundry ਪਲੇਟਫਾਰਮ
Windows AI Foundry ਪਲੇਟਫਾਰਮ Windows ਡਿਵਾਈਸਾਂ 'ਤੇ Edge AI ਵਿਕਾਸ ਲਈ ਖਾਸ ਤੌਰ 'ਤੇ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਟੂਲ ਅਤੇ APIs ਦਾ ਇੱਕ ਵਿਸਤ੍ਰਿਤ ਸੂਟ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਸ ਵਿੱਚ NPU-ਐਕਸਲੇਰੇਟਡ ਹਾਰਡਵੇਅਰ ਲਈ ਵਿਸ਼ੇਸ਼ ਸਮਰਥਨ, Windows ML ਇੰਟਿਗ੍ਰੇਸ਼ਨ, ਅਤੇ ਪਲੇਟਫਾਰਮ-ਵਿਸ਼ੇਸ਼ ਸੁਧਾਰ ਤਕਨੀਕਾਂ ਸ਼ਾਮਲ ਹਨ।

**ਵਿਸਤ੍ਰਿਤ ਗਾਈਡ**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

ਇਹ ਗਾਈਡ ਕਵਰ ਕਰਦੀ ਹੈ:
- Windows AI Foundry ਪਲੇਟਫਾਰਮ ਦਾ ਝਲਕ ਅਤੇ ਘਟਕੇ
- NPU ਹਾਰਡਵੇਅਰ 'ਤੇ ਕੁਸ਼ਲ ਇੰਫਰੈਂਸ ਲਈ Phi Silica API
- ਚਿੱਤਰ ਪ੍ਰੋਸੈਸਿੰਗ ਅਤੇ OCR ਲਈ ਕੰਪਿਊਟਰ ਵਿਜ

---

