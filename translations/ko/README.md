<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a189d7d9d47816a518ca119d79dc19b",
  "translation_date": "2025-09-22T12:14:26+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
# EdgeAI 초보자를 위한 가이드

![코스 커버 이미지](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ko.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

다음 단계를 따라 이 리소스를 시작하세요:

1. **저장소 포크하기**: 클릭 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **저장소 클론하기**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Azure AI Foundry Discord에 가입하여 전문가 및 다른 개발자들과 만나기**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 다국어 지원

#### GitHub Action을 통한 지원 (자동화 및 항상 최신 상태 유지)

[아랍어](../ar/README.md) | [벵골어](../bn/README.md) | [불가리아어](../bg/README.md) | [버마어 (미얀마)](../my/README.md) | [중국어 (간체)](../zh/README.md) | [중국어 (번체, 홍콩)](../hk/README.md) | [중국어 (번체, 마카오)](../mo/README.md) | [중국어 (번체, 대만)](../tw/README.md) | [크로아티아어](../hr/README.md) | [체코어](../cs/README.md) | [덴마크어](../da/README.md) | [네덜란드어](../nl/README.md) | [핀란드어](../fi/README.md) | [프랑스어](../fr/README.md) | [독일어](../de/README.md) | [그리스어](../el/README.md) | [히브리어](../he/README.md) | [힌디어](../hi/README.md) | [헝가리어](../hu/README.md) | [인도네시아어](../id/README.md) | [이탈리아어](../it/README.md) | [일본어](../ja/README.md) | [한국어](./README.md) | [말레이어](../ms/README.md) | [마라티어](../mr/README.md) | [네팔어](../ne/README.md) | [노르웨이어](../no/README.md) | [페르시아어 (파르시)](../fa/README.md) | [폴란드어](../pl/README.md) | [포르투갈어 (브라질)](../br/README.md) | [포르투갈어 (포르투갈)](../pt/README.md) | [펀자브어 (구르무키)](../pa/README.md) | [루마니아어](../ro/README.md) | [러시아어](../ru/README.md) | [세르비아어 (키릴)](../sr/README.md) | [슬로바키아어](../sk/README.md) | [슬로베니아어](../sl/README.md) | [스페인어](../es/README.md) | [스와힐리어](../sw/README.md) | [스웨덴어](../sv/README.md) | [타갈로그어 (필리핀어)](../tl/README.md) | [태국어](../th/README.md) | [터키어](../tr/README.md) | [우크라이나어](../uk/README.md) | [우르두어](../ur/README.md) | [베트남어](../vi/README.md)

**추가 번역 언어를 원하시면 [여기](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)에서 지원되는 언어를 확인하세요**

## 소개

**EdgeAI 초보자를 위한 가이드**에 오신 것을 환영합니다. 이 과정은 Edge 인공지능의 혁신적인 세계로 여러분을 안내하며, 강력한 AI 기능과 실질적인 엣지 디바이스 배포 간의 격차를 연결합니다. 데이터를 생성하고 결정을 내려야 하는 바로 그곳에서 AI의 잠재력을 활용할 수 있도록 돕습니다.

### 학습 목표

이 과정은 기본 개념부터 실무 구현까지 다루며 다음을 포함합니다:
- **엣지 배포에 최적화된 소형 언어 모델(SLMs)**
- 다양한 플랫폼에서의 **하드웨어 최적화**
- **실시간 추론** 및 개인정보 보호 기능
- **기업 애플리케이션을 위한 배포 전략**

### EdgeAI의 중요성

Edge AI는 현대의 주요 과제를 해결하는 패러다임 전환을 제공합니다:
- **개인정보 보호 및 보안**: 민감한 데이터를 클라우드에 노출하지 않고 로컬에서 처리
- **실시간 성능**: 네트워크 지연을 제거하여 시간에 민감한 애플리케이션 지원
- **비용 효율성**: 대역폭 및 클라우드 컴퓨팅 비용 절감
- **탄력적인 운영**: 네트워크 장애 시에도 기능 유지
- **규제 준수**: 데이터 주권 요구사항 충족

### Edge AI

Edge AI는 AI 알고리즘과 언어 모델을 하드웨어에서 로컬로 실행하여 데이터가 생성되는 가까운 곳에서 클라우드 리소스 없이 추론을 수행하는 것을 의미합니다. 이는 지연 시간을 줄이고 개인정보를 강화하며 실시간 의사 결정을 가능하게 합니다.

### 핵심 원칙:
- **디바이스 내 추론**: AI 모델이 엣지 디바이스(휴대폰, 라우터, 마이크로컨트롤러, 산업용 PC)에서 실행
- **오프라인 기능**: 지속적인 인터넷 연결 없이 작동
- **저지연**: 실시간 시스템에 적합한 즉각적인 응답
- **데이터 주권**: 민감한 데이터를 로컬에 유지하여 보안 및 규정 준수 강화

### 소형 언어 모델(SLMs)

Phi-4, Mistral-7B, Gemma와 같은 SLMs는 더 큰 LLMs의 최적화된 버전으로, 다음을 위해 훈련되거나 축소되었습니다:
- **메모리 사용량 감소**: 엣지 디바이스의 제한된 메모리를 효율적으로 사용
- **컴퓨팅 요구 감소**: CPU 및 엣지 GPU 성능에 최적화
- **빠른 시작 시간**: 응답성 높은 애플리케이션을 위한 빠른 초기화

이들은 다음과 같은 제약을 충족하면서 강력한 NLP 기능을 제공합니다:
- **임베디드 시스템**: IoT 디바이스 및 산업용 컨트롤러
- **모바일 디바이스**: 오프라인 기능을 갖춘 스마트폰 및 태블릿
- **IoT 디바이스**: 제한된 리소스를 가진 센서 및 스마트 디바이스
- **엣지 서버**: 제한된 GPU 리소스를 가진 로컬 처리 장치
- **개인용 컴퓨터**: 데스크톱 및 노트북 배포 시나리오

## 코스 구조

### [모듈 01: EdgeAI 기본 및 변혁](./Module01/README.md)
**주제**: 엣지 AI 배포의 변혁적 변화

#### 챕터 구성:
- [**섹션 1: EdgeAI 기본**](./Module01/01.EdgeAIFundamentals.md)
  - 전통적인 클라우드 AI와 엣지 AI 비교
  - 엣지 컴퓨팅의 과제와 제약
  - 주요 기술: 모델 양자화, 압축 최적화, 소형 언어 모델(SLMs)
  - 하드웨어 가속: NPU, GPU 최적화, CPU 최적화
  - 장점: 개인정보 보호, 저지연, 오프라인 기능, 비용 효율성

- [**섹션 2: 실제 사례 연구**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Mu 모델 생태계
  - 일본항공 AI 보고 시스템 사례 연구
  - 시장 영향 및 미래 방향
  - 배포 고려사항 및 모범 사례

- [**섹션 3: 실용적 구현 가이드**](./Module01/03.PracticalImplementationGuide.md)
  - 개발 환경 설정 (Python 3.10+, .NET 8+)
  - 하드웨어 요구사항 및 권장 구성
  - 핵심 모델 패밀리 리소스
  - 양자화 및 최적화 도구 (Llama.cpp, Microsoft Olive, Apple MLX)
  - 평가 및 검증 체크리스트

- [**섹션 4: 엣지 AI 배포 하드웨어 플랫폼**](./Module01/04.EdgeDeployment.md)
  - 엣지 AI 배포 고려사항 및 요구사항
  - Intel 엣지 AI 하드웨어 및 최적화 기술
  - 모바일 및 임베디드 시스템을 위한 Qualcomm AI 솔루션
  - NVIDIA Jetson 및 엣지 컴퓨팅 플랫폼
  - NPU 가속이 포함된 Windows AI PC 플랫폼
  - 하드웨어별 최적화 전략

---

### [모듈 02: 소형 언어 모델 기초](./Module02/README.md)
**주제**: SLM 이론적 원칙, 구현 전략 및 생산 배포

#### 챕터 구성:
- [**섹션 1: Microsoft Phi 모델 패밀리 기초**](./Module02/01.PhiFamily.md)
  - 디자인 철학의 진화 (Phi-1에서 Phi-4까지)
  - 효율성 중심의 아키텍처 설계
  - 특화된 기능 (추론, 멀티모달, 엣지 배포)

- [**섹션 2: Qwen 패밀리 기초**](./Module02/02.QwenFamily.md)
  - 오픈 소스 우수성 (Qwen 1.0에서 Qwen3까지) - Hugging Face에서 제공
  - 사고 모드 기능을 갖춘 고급 추론 아키텍처
  - 확장 가능한 배포 옵션 (0.5B-235B 파라미터)

- [**섹션 3: Gemma 패밀리 기초**](./Module02/03.GemmaFamily.md)
  - 연구 중심의 혁신 (Gemma 3 & 3n)
  - 멀티모달 우수성
  - 모바일 중심 아키텍처

- [**섹션 4: BitNET 패밀리 기초**](./Module02/04.BitNETFamily.md)
  - 혁신적인 양자화 기술 (1.58-bit)
  - https://github.com/microsoft/BitNet에서 제공되는 특화된 추론 프레임워크
  - 극한의 효율성을 통한 지속 가능한 AI 리더십

- [**섹션 5: Microsoft Mu 모델 기초**](./Module02/05.mumodel.md)
  - Windows 11에 내장된 디바이스 중심 아키텍처
  - Windows 11 설정과의 시스템 통합
  - 개인정보 보호를 위한 오프라인 작동

- [**섹션 6: Phi-Silica 기초**](./Module02/06.phisilica.md)
  - Windows 11 Copilot+ PC에 내장된 NPU 최적화 아키텍처
  - 뛰어난 효율성 (650 토큰/초, 1.5W)
  - Windows App SDK와의 개발자 통합

---

### [모듈 03: 소형 언어 모델 배포](./Module03/README.md)
**주제**: 이론부터 생산 환경까지 SLM 전체 라이프사이클 배포

#### 챕터 구성:
- [**섹션 1: SLM 고급 학습**](./Module03/01.SLMAdvancedLearning.md)
  - 파라미터 분류 프레임워크 (Micro SLM 100M-1.4B, Medium SLM 14B-30B)
  - 고급 최적화 기술 (양자화 방법, BitNET 1-bit 양자화)
  - 모델 획득 전략 (Phi 모델을 위한 Azure AI Foundry, 선택된 모델을 위한 Hugging Face)

- [**섹션 2: 로컬 환경 배포**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama 범용 플랫폼 배포
  - Microsoft Foundry 로컬 엔터프라이즈급 솔루션
  - 프레임워크 비교 분석

- [**섹션 3: 컨테이너화된 클라우드 배포**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM 고성능 추론 배포
  - Ollama 컨테이너 오케스트레이션
  - ONNX Runtime 엣지 최적화 구현

---

### [모듈 04: 모델 형식 변환 및 양자화](./Module04/README.md)
**주제**: 플랫폼 전반에 걸친 엣지 배포를 위한 완전한 모델 최적화 도구

#### 챕터 구성:
- [**섹션 1: 모델 형식 변환 및 양자화 기초**](./Module04/01.Introduce.md)
  - 정밀도 분류 프레임워크 (초저, 저, 중간 정밀도)
  - GGUF 및 ONNX 형식의 장점과 사용 사례
  - 운영 효율성을 위한 양자화의 이점
  - 성능 벤치마크 및 메모리 사용량 비교
- [**섹션 2: Llama.cpp 구현 가이드**](./Module04/02.Llamacpp.md)
  - 크로스 플랫폼 설치 (Windows, macOS, Linux)
  - GGUF 형식 변환 및 양자화 수준 (Q2_K에서 Q8_0까지)
  - 하드웨어 가속 (CUDA, Metal, OpenCL, Vulkan)
  - Python 통합 및 REST API 배포

- [**섹션 3: Microsoft Olive 최적화 스위트**](./Module04/03.MicrosoftOlive.md)
  - 40개 이상의 내장 컴포넌트를 활용한 하드웨어 인식 모델 최적화
  - 동적 및 정적 양자화를 통한 자동 최적화
  - Azure ML 워크플로와의 엔터프라이즈 통합
  - 인기 모델 지원 (Llama, Phi, 선택된 Qwen 모델, Gemma)

- [**섹션 4: OpenVINO Toolkit 최적화 스위트**](./Module04/04.openvino.md)
  - 인텔의 크로스 플랫폼 AI 배포를 위한 오픈소스 툴킷
  - 고급 최적화를 위한 Neural Network Compression Framework (NNCF)
  - 대규모 언어 모델 배포를 위한 OpenVINO GenAI
  - CPU, GPU, VPU 및 AI 가속기를 통한 하드웨어 가속

- [**섹션 5: Apple MLX 프레임워크 심층 분석**](./Module04/05.AppleMLX.md)
  - Apple Silicon을 위한 통합 메모리 아키텍처
  - LLaMA, Mistral, Phi, 선택된 Qwen 모델 지원
  - LoRA 미세 조정 및 모델 맞춤화
  - 4비트/8비트 양자화를 활용한 Hugging Face 통합

- [**섹션 6: Edge AI 개발 워크플로 통합**](./Module04/06.workflow-synthesis.md)
  - 여러 최적화 프레임워크를 통합하는 통합 워크플로 아키텍처
  - 프레임워크 선택 의사결정 트리 및 성능 트레이드오프 분석
  - 프로덕션 준비 검증 및 종합적인 배포 전략
  - 신흥 하드웨어 및 모델 아키텍처를 위한 미래 대비 전략

---

### [모듈 05: SLMOps - 소형 언어 모델 운영](./Module05/README.md)
**주제**: 증류에서 프로덕션 배포까지의 SLM 전체 수명 주기 운영

#### 챕터 구성:
- [**섹션 1: SLMOps 소개**](./Module05/01.IntroduceSLMOps.md)
  - AI 운영에서의 SLMOps 패러다임 전환
  - 비용 효율성과 프라이버시 우선 아키텍처
  - 전략적 비즈니스 영향 및 경쟁 우위
  - 실제 구현 시 도전 과제와 해결책

- [**섹션 2: 모델 증류 - 이론에서 실습까지**](./Module05/02.SLMOps-Distillation.md)
  - 교사 모델에서 학생 모델로의 지식 전이
  - 2단계 증류 프로세스 구현
  - Azure ML 증류 워크플로와 실용적인 예제
  - 85% 추론 시간 단축과 92% 정확도 유지

- [**섹션 3: 미세 조정 - 특정 작업을 위한 모델 맞춤화**](./Module05/03.SLMOps-Finetuing.md)
  - 매개변수 효율적인 미세 조정 (PEFT) 기술
  - LoRA 및 QLoRA 고급 방법
  - Microsoft Olive를 활용한 미세 조정 구현
  - 다중 어댑터 학습 및 하이퍼파라미터 최적화

- [**섹션 4: 배포 - 프로덕션 준비 구현**](./Module05/04.SLMOps.Deployment.md)
  - 프로덕션을 위한 모델 변환 및 양자화
  - Foundry Local 배포 구성
  - 성능 벤치마킹 및 품질 검증
  - 75% 크기 축소와 프로덕션 모니터링

---

### [모듈 06: SLM 에이전트 시스템 - AI 에이전트 및 함수 호출](./Module06/README.md)
**주제**: SLM 에이전트 시스템 구현, 기초부터 고급 함수 호출 및 모델 컨텍스트 프로토콜 통합까지

#### 챕터 구성:
- [**섹션 1: AI 에이전트와 소형 언어 모델 기초**](./Module06/01.IntroduceAgent.md)
  - 에이전트 분류 프레임워크 (반사형, 모델 기반, 목표 기반, 학습 에이전트)
  - SLM 기본 원리 및 최적화 전략 (GGUF, 양자화, 엣지 프레임워크)
  - SLM과 LLM의 트레이드오프 분석 (10-30배 비용 절감, 70-80% 작업 효율성)
  - Ollama, VLLM, Microsoft 엣지 솔루션을 활용한 실용적 배포

- [**섹션 2: 소형 언어 모델에서의 함수 호출**](./Module06/02.FunctionCalling.md)
  - 체계적인 워크플로 구현 (의도 감지, JSON 출력, 외부 실행)
  - 플랫폼별 구현 (Phi-4-mini, 선택된 Qwen 모델, Microsoft Foundry Local)
  - 고급 예제 (다중 에이전트 협업, 동적 도구 선택)
  - 프로덕션 고려 사항 (속도 제한, 감사 로깅, 보안 조치)

- [**섹션 3: 모델 컨텍스트 프로토콜 (MCP) 통합**](./Module06/03.IntroduceMCP.md)
  - 프로토콜 아키텍처 및 계층적 시스템 설계
  - 다중 백엔드 지원 (개발용 Ollama, 프로덕션용 vLLM)
  - 연결 프로토콜 (STDIO 및 SSE 모드)
  - 실제 응용 사례 (웹 자동화, 데이터 처리, API 통합)

---

### [모듈 07: EdgeAI 구현 샘플](./Module07/README.md)
**주제**: 다양한 플랫폼과 프레임워크를 아우르는 포괄적인 EdgeAI 구현

#### 챕터 구성:
- [**Visual Studio Code용 AI 툴킷**](./Module07/aitoolkit.md)
  - VS Code 내에서의 포괄적인 Edge AI 개발 환경
  - 엣지 배포를 위한 모델 카탈로그 및 검색
  - 로컬 테스트, 최적화 및 에이전트 개발 워크플로
  - 엣지 시나리오에 대한 성능 모니터링 및 평가

- [**Windows EdgeAI 개발 가이드**](./Module07/windowdeveloper.md)
  - Windows AI Foundry 플랫폼의 포괄적인 개요
  - 효율적인 NPU 추론을 위한 Phi Silica API
  - 이미지 처리 및 OCR을 위한 Computer Vision API
  - 로컬 개발 및 테스트를 위한 Foundry Local CLI

- [**NVIDIA Jetson Orin Nano에서의 EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 신용카드 크기의 폼 팩터에서 67 TOPS AI 성능
  - 생성 AI 모델 지원 (비전 트랜스포머, LLM, 비전-언어 모델)
  - 로봇, 드론, 지능형 카메라, 자율 장치에서의 응용
  - 민주화된 AI 개발을 위한 $249의 경제적인 플랫폼

- [**.NET MAUI 및 ONNX Runtime GenAI를 활용한 모바일 애플리케이션에서의 EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 단일 C# 코드베이스를 활용한 크로스 플랫폼 모바일 AI
  - 하드웨어 가속 지원 (CPU, GPU, 모바일 AI 프로세서)
  - 플랫폼별 최적화 (iOS용 CoreML, Android용 NNAPI)
  - 완전한 생성 AI 루프 구현

- [**Azure에서 소형 언어 모델 엔진을 활용한 EdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 클라우드-엣지 하이브리드 배포 아키텍처
  - ONNX Runtime과의 Azure AI 서비스 통합
  - 엔터프라이즈 규모 배포 및 지속적인 모델 관리
  - 지능형 문서 처리를 위한 하이브리드 AI 워크플로

- [**Windows ML을 활용한 EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - 고성능 온디바이스 추론을 위한 Windows AI Foundry 기반
  - 범용 하드웨어 지원 (AMD, Intel, NVIDIA, Qualcomm 실리콘)
  - 자동 하드웨어 추상화 및 최적화
  - 다양한 Windows 하드웨어 생태계를 위한 통합 프레임워크

- [**Foundry Local 애플리케이션을 활용한 EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 로컬 리소스를 활용한 프라이버시 중심 RAG 구현
  - 의미론적 검색을 위한 Phi-4 언어 모델 통합 (Phi 모델 전용)
  - 로컬 벡터 데이터베이스 지원 (SQLite, Qdrant)
  - 데이터 주권 및 오프라인 작동 기능

### [모듈 08: Microsoft Foundry Local – 완전한 개발자 툴킷](./Module08/README.md)
**주제**: Foundry Local을 활용한 로컬 AI 구축, 실행 및 통합; Azure AI Foundry와의 확장 및 하이브리드화

#### 챕터 구성:
- [**1: Foundry Local 시작하기**](./Module08/01.FoundryLocalSetup.md)
- [**2: Azure AI Foundry를 활용한 AI 솔루션 구축**](./Module08/02.AzureAIFoundryIntegration.md)
- [**3: 오픈소스 모델 Foundry Local**](./Module08/03.OpenSourceModels.md)
- [**4: 최첨단 모델 및 온디바이스 추론**](./Module08/04.CuttingEdgeModels.md)
- [**5: Foundry Local을 활용한 AI 기반 에이전트**](./Module08/05.AIPoweredAgents.md)
- [**6: 도구로서의 모델**](./Module08/06.ModelsAsTools.md)

## 강의 학습 목표

이 포괄적인 EdgeAI 강의를 완료하면, 프로덕션 준비가 된 EdgeAI 솔루션을 설계, 구현 및 배포할 수 있는 전문성을 갖추게 됩니다. 체계적인 접근 방식을 통해 이론적 기초와 실질적인 구현 기술을 모두 마스터할 수 있습니다.

### 기술 역량

**기초 지식**
- 클라우드 기반 AI 아키텍처와 엣지 기반 AI 아키텍처의 근본적인 차이를 이해
- 리소스 제약 환경을 위한 모델 양자화, 압축 및 최적화 원리 숙달
- 하드웨어 가속 옵션 (NPU, GPU, CPU) 및 배포 시 고려 사항 이해

**구현 기술**
- 다양한 엣지 플랫폼 (모바일, 임베디드, IoT, 엣지 서버)에서 소형 언어 모델 배포
- Llama.cpp, Microsoft Olive, ONNX Runtime, Apple MLX와 같은 최적화 프레임워크 적용
- 초당 응답 요구 사항을 충족하는 실시간 추론 시스템 구현

**프로덕션 전문성**
- 엔터프라이즈 애플리케이션을 위한 확장 가능한 EdgeAI 아키텍처 설계
- 배포된 시스템에 대한 모니터링, 유지보수 및 업데이트 전략 구현
- 프라이버시를 보장하는 EdgeAI 구현을 위한 보안 모범 사례 적용

### 전략적 역량

**의사결정 프레임워크**
- EdgeAI 기회를 평가하고 비즈니스 애플리케이션에 적합한 사용 사례 식별
- 모델 정확도, 추론 속도, 전력 소비 및 하드웨어 비용 간의 트레이드오프 평가
- 특정 배포 제약 조건에 따라 적합한 SLM 계열 및 구성 선택

**시스템 아키텍처**
- 기존 인프라와 통합되는 종합적인 EdgeAI 솔루션 설계
- 최적의 성능과 비용 효율성을 위한 하이브리드 엣지-클라우드 아키텍처 계획
- 실시간 AI 애플리케이션을 위한 데이터 흐름 및 처리 파이프라인 구현

### 산업 응용

**실질적인 배포 시나리오**
- **제조업**: 품질 관리 시스템, 예측 유지보수 및 프로세스 최적화
- **헬스케어**: 프라이버시를 보장하는 진단 도구 및 환자 모니터링 시스템
- **운송**: 자율 차량 의사결정 및 교통 관리
- **스마트 시티**: 지능형 인프라 및 자원 관리 시스템
- **소비자 전자제품**: AI 기반 모바일 애플리케이션 및 스마트 홈 디바이스

## 학습 결과 개요

### 모듈 01 학습 결과:
- 클라우드와 엣지 AI 아키텍처의 근본적인 차이를 이해
- 엣지 배포를 위한 핵심 최적화 기술 숙달
- 실제 응용 사례 및 성공 사례 인식
- EdgeAI 솔루션 구현을 위한 실질적인 기술 습득

### 모듈 02 학습 결과:
- 다양한 SLM 설계 철학과 배포 시 고려 사항에 대한 깊은 이해
- 계산 제약 및 성능 요구 사항에 기반한 전략적 의사결정 능력 숙달
- 배포 유연성 트레이드오프 이해
- 효율적인 AI 아키텍처에 대한 미래 대비 통찰력 보유

### 모듈 03 학습 결과:
- 전략적 모델 선택 능력
- 최적화 기술 숙달
- 배포 유연성 숙달
- 프로덕션 준비 구성 능력

### 모듈 04 학습 결과:
- 양자화 경계 및 실제 응용에 대한 깊은 이해
- 여러 최적화 프레임워크 (Llama.cpp, Olive, OpenVINO, MLX) 실습 경험
- OpenVINO 및 NNCF를 활용한 Intel 하드웨어 최적화 숙달
- 다양한 플랫폼에서 하드웨어 인식 최적화 선택 능력
- 크로스 플랫폼 엣지 컴퓨팅 환경을 위한 프로덕션 배포 기술
- 최적의 Edge AI 솔루션을 위한 전략적 프레임워크 선택 및 워크플로 통합

### 모듈 05 학습 결과:
- SLMOps 패러다임 및 운영 원리 숙달
- 지식 전이 및 효율성 최적화를 위한 모델 증류 구현
- 도메인별 모델 맞춤화를 위한 미세 조정 기술 적용
- 모니터링 및 유지보수 전략을 포함한 프로덕션 준비 SLM 솔루션 배포

### 모듈 06 학습 결과:
- AI 에이전트 및 소형 언어 모델 아키텍처의 기초 개념 이해
- 여러 플랫폼 및 프레임워크에서 함수 호출 구현 숙달
- 외부 도구와의 표준화된 상호작용을 위한 모델 컨텍스트 프로토콜 (MCP) 통합
- 최소한의 인간 개입으로 복잡한 에이전트 시스템 구축

### 모듈 07 학습 결과:
- 포괄적인 Edge AI 개발 워크플로를 위한 Visual Studio Code용 AI 툴킷 숙달
- Windows AI Foundry 플랫폼 및 NPU 최적화 전략에 대한 전문성 획득
- 다양한 EdgeAI 플랫폼 및 구현 전략에 대한 실습 경험
- NVIDIA, 모바일, Azure 및 Windows 플랫폼 전반에 걸친 하드웨어별 최적화 기술 숙달
- 성능, 비용 및 프라이버시 요구 사항 간의 배포 트레이드오프 이해
- 다양한 생태계에서 실제 EdgeAI 애플리케이션을 구축하기 위한 실질적인 기술 개발

## 기대되는 강의 결과

이 강의를 성공적으로 완료하면, 전문 환경에서 EdgeAI 이니셔티브를 주도할 수 있는 지식, 기술 및 자신감을 갖추게 됩니다.

### 전문 준비도

**기술 리더십**
- **솔루션 아키텍처**: 엔터프라이즈 요구 사항을 충족하는 포괄적인 EdgeAI 시스템 설계
- **성능 최적화**: 정확도, 속도 및 리소스 소비 간의 최적 균형 달성
- **크로스 플랫폼 배포**: Windows, Linux, 모바일 및 임베디드 플랫폼 전반에 걸친 솔루션 구현
- **프로덕션 운영**: 엔터프라이즈급 신뢰성을 갖춘 EdgeAI 시스템 유지 및 확장

**산업 전문성**
- **기술 평가**: 특정 비즈니스 과제를 위한 EdgeAI 솔루션 평가 및 추천
- **구현 계획**: EdgeAI 프로젝트를 위한 현실적인 일정 및 리소스 요구 사항 개발
- **위험 관리**: EdgeAI 배포에서 기술적 및 운영적 위험을 식별하고 완화
- **ROI 최적화**: EdgeAI 구현을 통해 측정 가능한 비즈니스 가치를 입증

### 경력 발전 기회

**전문 직무**
- EdgeAI 솔루션 아키텍트
- 머신 러닝 엔지니어 (Edge 전문화)
- IoT AI 개발자
- 모바일 AI 애플리케이션 개발자
- 엔터프라이즈 AI 컨설턴트

**산업 분야**
- 스마트 제조 및 산업 4.0
- 자율주행 차량 및 교통
- 헬스케어 기술 및 의료 기기
- 금융 기술 및 보안
- 소비자 전자제품 및 모바일 애플리케이션

### 인증 및 검증

**포트폴리오 개발**
- 실질적인 역량을 보여주는 EdgeAI 프로젝트를 끝까지 완성
- 다양한 하드웨어 플랫폼에서 프로덕션 준비 솔루션 배포
- 최적화 전략 및 성능 개선 사항을 문서화

**지속적인 학습 경로**
- 고급 AI 전문화의 기초 마련
- 클라우드-엣지 하이브리드 아키텍처 준비
- 신흥 AI 기술 및 프레임워크로의 관문

이 과정은 AI 기술 배포의 최전선에 여러분을 위치시키며, 지능형 기능이 현대 생활을 이끄는 장치와 시스템에 원활하게 통합되도록 합니다.

## 파일 구조 트리 다이어그램

```
edgeai-for-beginners/
├── imgs/
│   └── cover.png
├── Module01/ (EdgeAI Fundamentals and Transformation)
│   ├── 01.EdgeAIFundamentals.md
│   ├── 02.RealWorldCaseStudies.md
│   ├── 03.PracticalImplementationGuide.md
│   ├── 04.EdgeDeployment.md
│   └── README.md
├── Module02/ (Small Language Model Foundations)
│   ├── 01.PhiFamily.md
│   ├── 02.QwenFamily.md
│   ├── 03.GemmaFamily.md
│   ├── 04.BitNETFamily.md
│   ├── 05.mumodel.md
│   ├── 06.phisilica.md
│   └── README.md
├── Module03/ (SLM Deployment Practice)
│   ├── 01.SLMAdvancedLearning.md
│   ├── 02.DeployingSLMinLocalEnv.md
│   ├── 03.DeployingSLMinCloud.md
│   └── README.md
├── Module04/ (Model Format Conversion and Quantization)
│   ├── 01.Introduce.md
│   ├── 02.Llamacpp.md
│   ├── 03.MicrosoftOlive.md
│   ├── 04.openvino.md
│   ├── 05.AppleMLX.md
│   ├── 06.workflow-synthesis.md
│   └── README.md
├── Module05/ (SLMOps - Small Language Model Operations)
│   ├── 01.IntroduceSLMOps.md
│   ├── 02.SLMOps-Distillation.md
│   ├── 03.SLMOps-Finetuing.md
│   ├── 04.SLMOps.Deployment.md
│   └── README.md
├── Module06/ (SLM Agentic Systems)
│   ├── 01.IntroduceAgent.md
│   ├── 02.FunctionCalling.md
│   ├── 03.IntroduceMCP.md
│   └── README.md
├── Module07/ (EdgeAI Implementation Samples)
│   ├── aitoolkit.md
│   ├── windowdeveloper.md
│   └── README.md
├── Module08/ (Hands on with Foundry Local)
│   ├── 01.FoundryLocalSetup.md
│   ├── 02.AzureAIFoundryIntegration.md
│   ├── 03.OpenSourceModels.md
│   ├── 04.CuttingEdgeModels.md
│   ├── 05.AIPoweredAgents.md
│   ├── 06.ModelsAsTools.md
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## 과정 특징

- **점진적 학습**: 기본 개념에서 고급 배포까지 점진적으로 발전
- **이론과 실습 통합**: 각 모듈은 이론적 기초와 실질적 운영을 포함
- **실제 사례 연구**: Microsoft, Alibaba, Google 등 실제 사례 기반
- **실습 기회**: 구성 파일 작성, API 테스트 절차, 배포 스크립트 완성
- **성능 벤치마크**: 추론 속도, 메모리 사용량, 리소스 요구 사항에 대한 상세 비교
- **기업 수준 고려사항**: 보안 관행, 준수 프레임워크, 데이터 보호 전략

## 시작하기

추천 학습 경로:
1. **Module01**로 시작하여 EdgeAI의 기본 이해를 구축
2. **Module02**로 진행하여 다양한 SLM 모델 계열을 심층적으로 이해
3. **Module03**을 학습하여 실질적인 배포 기술을 마스터
4. **Module04**를 통해 고급 모델 최적화, 형식 변환, 프레임워크 통합 학습
5. **Module05**를 완료하여 프로덕션 준비 구현을 위한 SLMOps 마스터
6. **Module06**을 탐구하여 SLM 에이전트 시스템 및 함수 호출 기능 이해
7. **Module07**을 마무리하여 AI 툴킷과 다양한 EdgeAI 구현 샘플에 대한 실질적 경험 획득
8. **Module08**을 탐구하여 Foundry Local 개발자 툴킷(로컬 우선 개발 및 하이브리드 Azure 통합)을 완벽히 이해

각 모듈은 독립적으로 완성될 수 있도록 설계되었지만, 순차적 학습이 최상의 결과를 제공합니다.

## 학습 가이드

포괄적인 [학습 가이드](STUDY_GUIDE.md)가 제공되어 학습 경험을 극대화할 수 있도록 도와줍니다. 학습 가이드는 다음을 제공합니다:

- **구조화된 학습 경로**: 20시간 내에 과정을 완료할 수 있는 최적화된 일정
- **시간 배분 가이드**: 읽기, 연습, 프로젝트 간의 균형을 맞추기 위한 구체적인 권장 사항
- **핵심 개념 집중**: 각 모듈의 우선 학습 목표
- **자기 평가 도구**: 이해도를 테스트할 수 있는 질문과 연습 문제
- **미니 프로젝트 아이디어**: 학습을 강화하기 위한 실질적 응용

이 학습 가이드는 집중 학습(1주)과 파트타임 학습(3주) 모두를 수용할 수 있도록 설계되었으며, 하루 10시간만 투자할 수 있는 경우에도 시간을 효과적으로 배분하는 방법에 대한 명확한 지침을 제공합니다.

---

**EdgeAI의 미래는 모델 아키텍처, 양자화 기술, 배포 전략의 지속적인 개선에 달려 있으며, 이는 범용 기능보다 효율성과 전문화를 우선시합니다. 이 패러다임 전환을 수용하는 조직은 AI의 변혁적 잠재력을 활용하면서 데이터와 운영에 대한 통제력을 유지할 수 있는 유리한 위치에 설 것입니다.**

## 기타 과정

저희 팀은 다른 과정도 제공합니다! 확인해보세요:

- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents For Beginners](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners using JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML for Beginners](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Data Science for Beginners](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI for Beginners](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT for Beginners](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for AI Paired Programming](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

