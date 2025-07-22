<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f921854683b0ba903972831f6e61c28f",
  "translation_date": "2025-07-22T05:24:57+00:00",
  "source_file": "Module07/README.md",
  "language_code": "ko"
}
-->
# Chapter 07 : EdgeAI 샘플

Edge AI는 인공지능과 엣지 컴퓨팅의 융합을 의미하며, 클라우드 연결에 의존하지 않고 디바이스에서 직접 지능형 처리를 가능하게 합니다. 이 장에서는 다양한 플랫폼과 프레임워크에서 실행되는 다섯 가지 독특한 EdgeAI 구현 사례를 탐구하며, 엣지에서 AI 모델을 실행하는 유연성과 강력함을 보여줍니다.

## 1. NVIDIA Jetson Orin Nano에서의 EdgeAI

NVIDIA Jetson Orin Nano는 접근 가능한 엣지 AI 컴퓨팅에서 획기적인 발전을 이루며, 신용카드 크기의 컴팩트한 형태로 최대 67 TOPS의 AI 성능을 제공합니다. 이 강력한 엣지 AI 플랫폼은 취미 활동가, 학생, 전문 개발자 모두를 위한 생성형 AI 개발을 민주화합니다.

### 주요 특징
- 최대 67 TOPS의 AI 성능 제공—이전 모델 대비 1.7배 향상
- AI 처리를 위한 1024 CUDA 코어와 최대 32 Tensor 코어
- 최대 주파수 1.5 GHz의 6코어 Arm Cortex-A78AE v8.2 64비트 CPU
- 단 $249의 가격으로 개발자, 학생, 제작자에게 가장 저렴하고 접근 가능한 플랫폼 제공

### 응용 분야
Jetson Orin Nano는 비전 트랜스포머, 대형 언어 모델, 비전-언어 모델을 포함한 최신 생성형 AI 모델 실행에 뛰어납니다. 특히 GenAI 사용 사례를 위해 설계되었으며, 이제 손바닥 크기의 디바이스에서 여러 LLM을 실행할 수 있습니다. 인기 있는 사용 사례로는 AI 기반 로봇, 스마트 드론, 지능형 카메라, 자율 엣지 디바이스 등이 있습니다.

**자세히 알아보기**: [NVIDIA의 Jetson Orin Nano 슈퍼컴퓨터: EdgeAI의 다음 큰 혁신](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. .NET MAUI와 ONNX Runtime GenAI를 활용한 모바일 애플리케이션에서의 EdgeAI

이 솔루션은 .NET MAUI(멀티 플랫폼 앱 UI)와 ONNX Runtime GenAI를 사용하여 생성형 AI와 대형 언어 모델(LLM)을 크로스 플랫폼 모바일 애플리케이션에 통합하는 방법을 보여줍니다. 이를 통해 .NET 개발자는 Android와 iOS 디바이스에서 네이티브로 실행되는 정교한 AI 기반 모바일 애플리케이션을 구축할 수 있습니다.

### 주요 특징
- Android와 iOS 애플리케이션 모두를 위한 단일 코드베이스를 제공하는 .NET MAUI 프레임워크 기반
- ONNX Runtime GenAI 통합으로 모바일 디바이스에서 생성형 AI 모델 실행 가능
- CPU, GPU, 특화된 모바일 AI 프로세서를 포함한 다양한 하드웨어 가속기 지원
- ONNX Runtime을 통해 iOS의 CoreML 및 Android의 NNAPI와 같은 플랫폼별 최적화 지원
- 전처리 및 후처리, 추론, 로짓 처리, 검색 및 샘플링, KV 캐시 관리 등 생성형 AI 루프 전체 구현

### 개발 혜택
.NET MAUI 접근법은 개발자가 기존 C# 및 .NET 기술을 활용하여 크로스 플랫폼 AI 애플리케이션을 구축할 수 있도록 합니다. ONNX Runtime GenAI 프레임워크는 Llama, Mistral, Phi, Gemma 등 다양한 모델 아키텍처를 지원합니다. 최적화된 ARM64 커널은 INT4 양자화 행렬 곱셈을 가속화하여 모바일 하드웨어에서 효율적인 성능을 제공하며, 익숙한 .NET 개발 경험을 유지합니다.

### 사용 사례
이 솔루션은 .NET 기술을 사용하여 AI 기반 모바일 애플리케이션을 구축하려는 개발자에게 적합합니다. 지능형 챗봇, 이미지 인식 앱, 언어 번역 도구, 개인화된 추천 시스템 등 디바이스에서 완전히 실행되어 프라이버시를 강화하고 오프라인 기능을 제공하는 애플리케이션을 포함합니다.

**자세히 알아보기**: [.NET MAUI ONNX Runtime GenAI 예제](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. Azure에서의 EdgeAI와 소형 언어 모델 엔진

Microsoft의 Azure 기반 EdgeAI 솔루션은 클라우드-엣지 하이브리드 환경에서 소형 언어 모델(SLM)을 효율적으로 배포하는 데 중점을 둡니다. 이 접근법은 클라우드 규모의 AI 서비스와 엣지 배포 요구 사항 간의 격차를 연결합니다.

### 아키텍처 장점
- Azure AI 서비스와의 원활한 통합
- ONNX Runtime을 통해 디바이스와 클라우드에서 SLM/LLM 및 멀티모달 모델 실행
- 엔터프라이즈 규모 배포에 최적화
- 지속적인 모델 업데이트 및 관리 지원

### 사용 사례
Azure EdgeAI 구현은 클라우드 관리 기능을 갖춘 엔터프라이즈급 AI 배포가 필요한 시나리오에서 뛰어납니다. 여기에는 지능형 문서 처리, 실시간 분석, 클라우드와 엣지 컴퓨팅 리소스를 모두 활용하는 하이브리드 AI 워크플로우가 포함됩니다.

**자세히 알아보기**: [Azure EdgeAI SLM 엔진](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. Windows ML을 활용한 EdgeAI

Windows ML은 성능이 뛰어난 디바이스 내 모델 추론과 간소화된 배포를 위해 최적화된 Microsoft의 최첨단 런타임으로, Windows AI Foundry의 기반 역할을 합니다. 이 플랫폼은 개발자가 PC 하드웨어 전체를 활용하는 AI 기반 Windows 애플리케이션을 만들 수 있도록 합니다.

### 플랫폼 기능
- Windows 11 버전 24H2(빌드 26100) 이상을 실행하는 모든 PC에서 작동
- NPUs나 GPUs가 없는 PC를 포함한 모든 x64 및 ARM64 PC 하드웨어에서 작동
- AMD, Intel, NVIDIA, Qualcomm을 포함한 CPU, GPU, NPU를 아우르는 실리콘 파트너 생태계 전반에 걸쳐 모델을 효율적으로 배포 가능
- 인프라 API를 활용하여 개발자가 다양한 실리콘을 대상으로 여러 빌드를 생성할 필요 없음

### 개발자 혜택
Windows ML은 하드웨어와 실행 제공자를 추상화하여 개발자가 코드 작성에 집중할 수 있도록 합니다. 또한 Windows ML은 최신 NPU, GPU, CPU가 출시될 때마다 자동으로 업데이트됩니다. 이 플랫폼은 다양한 Windows 하드웨어 생태계 전반에서 AI 개발을 위한 통합 프레임워크를 제공합니다.

**자세히 알아보기**: [Windows ML 개요](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)

## 5. Foundry Local 애플리케이션을 활용한 EdgeAI

Foundry Local은 .NET을 사용하여 로컬 리소스에서 검색 증강 생성(RAG) 애플리케이션을 구축할 수 있도록 하며, 로컬 언어 모델과 의미 검색 기능을 결합합니다. 이 접근법은 완전히 로컬 인프라에서 작동하는 프라이버시 중심 AI 솔루션을 제공합니다.

### 기술 아키텍처
- Phi-3 언어 모델, 로컬 임베딩, 의미 커널을 결합하여 RAG 시나리오 생성
- 콘텐츠와 그 의미론적 의미를 나타내는 부동 소수점 값 배열(벡터)로 임베딩 사용
- 의미 커널은 Phi-3 및 스마트 컴포넌트를 통합하여 원활한 RAG 파이프라인을 생성하는 주요 오케스트레이터 역할
- SQLite 및 Qdrant을 포함한 로컬 벡터 데이터베이스 지원

### 구현 혜택
RAG, 즉 검색 증강 생성은 "어떤 정보를 찾아서 프롬프트에 넣는 것"을 의미하는 간단한 방식입니다. 이 로컬 구현은 데이터 프라이버시를 보장하면서 사용자 정의 지식 기반에 근거한 지능형 응답을 제공합니다. 이 접근법은 데이터 주권과 오프라인 운영 기능이 필요한 엔터프라이즈 시나리오에서 특히 유용합니다.

**자세히 알아보기**: [Foundry Local RAG 샘플](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## 결론

이 다섯 가지 EdgeAI 구현 사례는 오늘날 이용 가능한 엣지 AI 솔루션의 성숙도와 다양성을 보여줍니다. Jetson Orin Nano와 같은 하드웨어 가속 엣지 디바이스부터 ONNX Runtime GenAI 및 Windows ML과 같은 소프트웨어 프레임워크까지, 개발자는 엣지에서 지능형 애플리케이션을 배포할 수 있는 전례 없는 옵션을 갖게 되었습니다.

이 플랫폼들 간의 공통점은 AI 기능의 민주화로, 다양한 기술 수준과 사용 사례를 가진 개발자들이 정교한 머신러닝을 활용할 수 있도록 합니다. 모바일 애플리케이션, 데스크톱 소프트웨어, 임베디드 시스템을 구축하든, 이러한 EdgeAI 솔루션은 엣지에서 효율적이고 프라이버시를 유지하며 작동하는 차세대 지능형 애플리케이션을 위한 기반을 제공합니다.

각 플랫폼은 고유한 장점을 제공합니다: Jetson Orin Nano는 하드웨어 가속 엣지 컴퓨팅을, ONNX Runtime GenAI는 크로스 플랫폼 모바일 개발을, Azure EdgeAI는 엔터프라이즈 클라우드-엣지 통합을, Windows ML은 Windows 네이티브 애플리케이션을, Foundry Local은 프라이버시 중심 RAG 구현을 지원합니다. 이들은 함께 EdgeAI 개발을 위한 포괄적인 생태계를 대표합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.