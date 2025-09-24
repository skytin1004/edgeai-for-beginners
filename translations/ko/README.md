<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ff006cd813df4152f5036e7b2bc5ed32",
  "translation_date": "2025-09-24T10:34:26+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
# 초보자를 위한 EdgeAI

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

**추가 번역 언어를 지원받고 싶다면 [여기](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)에서 확인하세요.**

## 소개

**초보자를 위한 EdgeAI**에 오신 것을 환영합니다. 이 과정은 Edge 인공지능의 혁신적인 세계로 여러분을 안내하며, 강력한 AI 기능과 실제적인 엣지 디바이스 배포 간의 격차를 연결합니다. 데이터를 생성하고 결정을 내려야 하는 바로 그곳에서 AI의 잠재력을 활용할 수 있도록 돕습니다.

### 학습 목표

이 과정은 기본 개념부터 실무 구현까지 다루며 다음을 포함합니다:
- **엣지 배포를 위한 소형 언어 모델(SLM)** 최적화
- 다양한 플랫폼에서 **하드웨어 인식 최적화**
- **실시간 추론** 및 개인정보 보호 기능
- **기업 애플리케이션을 위한 생산 배포** 전략

### EdgeAI의 중요성

Edge AI는 현대의 주요 과제를 해결하는 패러다임 전환을 제공합니다:
- **개인정보 보호 및 보안**: 민감한 데이터를 클라우드에 노출하지 않고 로컬에서 처리
- **실시간 성능**: 네트워크 지연을 제거하여 시간에 민감한 애플리케이션 지원
- **비용 효율성**: 대역폭 및 클라우드 컴퓨팅 비용 절감
- **탄력적인 운영**: 네트워크 장애 시에도 기능 유지
- **규제 준수**: 데이터 주권 요구사항 충족

### Edge AI

Edge AI는 AI 알고리즘과 언어 모델을 하드웨어에서 로컬로 실행하여 데이터가 생성되는 가까운 곳에서 클라우드 리소스에 의존하지 않고 추론을 수행하는 것을 의미합니다. 이는 지연 시간을 줄이고 개인정보 보호를 강화하며 실시간 의사 결정을 가능하게 합니다.

### 핵심 원칙:
- **디바이스 내 추론**: AI 모델이 엣지 디바이스(휴대폰, 라우터, 마이크로컨트롤러, 산업용 PC)에서 실행
- **오프라인 기능**: 지속적인 인터넷 연결 없이 작동
- **저지연**: 실시간 시스템에 적합한 즉각적인 응답
- **데이터 주권**: 민감한 데이터를 로컬에 유지하여 보안 및 규정 준수 개선

### 소형 언어 모델(SLM)

Phi-4, Mistral-7B, Gemma와 같은 SLM은 더 큰 LLM을 훈련하거나 증류하여 최적화된 버전으로:
- **메모리 사용량 감소**: 제한된 엣지 디바이스 메모리 효율적 사용
- **컴퓨팅 요구 감소**: CPU 및 엣지 GPU 성능에 최적화
- **빠른 시작 시간**: 응답성 높은 애플리케이션을 위한 빠른 초기화

이들은 다음과 같은 제약을 충족하면서 강력한 NLP 기능을 제공합니다:
- **임베디드 시스템**: IoT 디바이스 및 산업용 컨트롤러
- **모바일 디바이스**: 오프라인 기능을 갖춘 스마트폰 및 태블릿
- **IoT 디바이스**: 제한된 리소스를 가진 센서 및 스마트 디바이스
- **엣지 서버**: 제한된 GPU 리소스를 가진 로컬 처리 장치
- **개인용 컴퓨터**: 데스크톱 및 노트북 배포 시나리오

## 코스 모듈 및 탐색

| 모듈 | 주제 | 초점 영역 | 주요 내용 | 수준 | 소요 시간 |
|--------|-------|------------|-------------|--------|----------|
| [📚 01](../../Module01) | [EdgeAI 기본](./Module01/README.md) | 클라우드 vs 엣지 AI 비교 | EdgeAI 기본 • 실제 사례 연구 • 구현 가이드 • 엣지 배포 | 초급 | 3-4시간 |
| [🧠 02](../../Module02) | [SLM 모델 기초](./Module02/README.md) | 모델 계열 및 아키텍처 | Phi 계열 • Qwen 계열 • Gemma 계열 • BitNET • μModel • Phi-Silica | 초급 | 4-5시간 |
| [🚀 03](../../Module03) | [SLM 배포 실습](./Module03/README.md) | 로컬 및 클라우드 배포 | 고급 학습 • 로컬 환경 • 클라우드 배포 | 중급 | 4-5시간 |
| [⚙️ 04](../../Module04) | [모델 최적화 도구](./Module04/README.md) | 크로스 플랫폼 최적화 | 소개 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 워크플로우 합성 | 중급 | 5-6시간 |
| [🔧 05](../../Module05) | [SLMOps 생산](./Module05/README.md) | 생산 운영 | SLMOps 소개 • 모델 증류 • 미세 조정 • 생산 배포 | 고급 | 5-6시간 |
| [🤖 06](../../Module06) | [AI 에이전트 및 함수 호출](./Module06/README.md) | 에이전트 프레임워크 및 MCP | 에이전트 소개 • 함수 호출 • 모델 컨텍스트 프로토콜 | 고급 | 4-5시간 |
| [💻 07](../../Module07) | [플랫폼 구현](./Module07/README.md) | 크로스 플랫폼 샘플 | AI 도구 키트 • Foundry Local • Windows 개발 | 고급 | 3-4시간 |
| [🏭 08](../../Module08) | [Foundry Local 도구 키트](./Module08/README.md) | 생산 준비 샘플 | 샘플 애플리케이션 (아래 세부 정보 참조) | 전문가 | 8-10시간 |

### 🏭 **모듈 08: 샘플 애플리케이션**

- [01: REST Chat 빠른 시작](./Module08/samples/01/README.md)
- [02: OpenAI SDK 통합](./Module08/samples/02/README.md)
- [03: 모델 탐색 및 벤치마킹](./Module08/samples/03/README.md)
- [04: Chainlit RAG 애플리케이션](./Module08/samples/04/README.md)
- [05: 다중 에이전트 오케스트레이션](./Module08/samples/05/README.md)
- [06: 도구로서의 모델 라우터](./Module08/samples/06/README.md)
- [07: 직접 API 클라이언트](./Module08/samples/07/README.md)
- [08: Windows 11 채팅 앱](./Module08/samples/08/README.md)
- [09: 고급 다중 에이전트 시스템](./Module08/samples/09/README.md)
- [10: Foundry 도구 프레임워크](./Module08/samples/10/README.md)

### 📊 **학습 경로 요약**
- **총 소요 시간**: 36-45시간
- **초급 경로**: 모듈 01-02 (7-9시간)  
- **중급 경로**: 모듈 03-04 (9-11시간)
- **고급 경로**: 모듈 05-07 (12-15시간)
- **전문가 경로**: 모듈 08 (8-10시간)

## 여러분이 만들게 될 것들

### 🎯 핵심 역량
- **Edge AI 아키텍처**: 클라우드 통합을 포함한 로컬 우선 AI 시스템 설계
- **모델 최적화**: 엣지 배포를 위해 모델 양자화 및 압축 (85% 속도 향상, 75% 크기 감소)
- **다중 플랫폼 배포**: Windows, 모바일, 임베디드 및 클라우드-엣지 하이브리드 시스템
- **생산 운영**: Edge AI의 모니터링, 확장 및 유지 관리

### 🏗️ 실무 프로젝트
- **Foundry Local 채팅 앱**: 모델 전환 기능을 갖춘 Windows 11 네이티브 애플리케이션
- **다중 에이전트 시스템**: 복잡한 워크플로를 위한 전문 에이전트 코디네이터  
- **RAG 애플리케이션**: 벡터 검색을 통한 로컬 문서 처리
- **모델 라우터**: 작업 분석에 기반한 모델 지능형 선택
- **API 프레임워크**: 스트리밍 및 상태 모니터링을 포함한 생산 준비 클라이언트
- **크로스 플랫폼 도구**: LangChain/Semantic Kernel 통합 패턴

### 🏢 산업 응용 분야
**제조** • **헬스케어** • **자율주행 차량** • **스마트 시티** • **모바일 앱**

## 빠른 시작

**추천 학습 경로** (총 20-30시간):

1. **📚 기초** (모듈 01-02): EdgeAI 개념 + SLM 모델 계열
2. **⚙️ 최적화** (모듈 03-04): 배포 + 양자화 프레임워크  
3. **🚀 생산** (모듈 05-06): SLMOps + AI 에이전트 + 함수 호출
4. **💻 구현** (모듈 07-08): 플랫폼 샘플 + Foundry Local 도구 키트

각 모듈에는 이론, 실습 과제, 생산 준비 코드 샘플이 포함되어 있습니다.

## 경력 영향
**기술 역할**: EdgeAI 솔루션 아키텍트 • ML 엔지니어 (엣지) • IoT AI 개발자 • 모바일 AI 개발자

**산업 분야**: 제조업 4.0 • 헬스케어 기술 • 자율 시스템 • 핀테크 • 소비자 전자제품

**포트폴리오 프로젝트**: 멀티 에이전트 시스템 • 생산용 RAG 앱 • 크로스 플랫폼 배포 • 성능 최적화

## 저장소 구조

```
edgeai-for-beginners/
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## 코스 하이라이트

✅ **점진적 학습**: 이론 → 실습 → 프로덕션 배포  
✅ **실제 사례 연구**: Microsoft, Japan Airlines, 기업 구현 사례  
✅ **실습 샘플**: 50개 이상의 예제, 10개의 포괄적인 Foundry Local 데모  
✅ **성능 중심**: 85% 속도 개선, 75% 크기 감소  
✅ **멀티 플랫폼**: Windows, 모바일, 임베디드, 클라우드-엣지 하이브리드  
✅ **프로덕션 준비 완료**: 모니터링, 확장, 보안, 컴플라이언스 프레임워크

📖 **[학습 가이드 제공](STUDY_GUIDE.md)**: 20시간 학습 경로, 시간 배분 가이드 및 자기 평가 도구 포함.

---

**EdgeAI는 AI 배포의 미래를 대표합니다**: 로컬 우선, 개인정보 보호, 효율성. 이 기술을 마스터하여 차세대 지능형 애플리케이션을 구축하세요.

## 기타 코스

우리 팀은 다른 코스도 제공합니다! 확인해보세요:

- [MCP 초보자용](https://github.com/microsoft/mcp-for-beginners)
- [AI 에이전트 초보자용](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Generative AI 초보자용 (.NET 사용)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [Generative AI 초보자용 (JavaScript 사용)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [Generative AI 초보자용](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML 초보자용](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [데이터 과학 초보자용](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI 초보자용](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [사이버 보안 초보자용](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [웹 개발 초보자용](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT 초보자용](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR 개발 초보자용](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [GitHub Copilot을 활용한 AI 페어드 프로그래밍 마스터하기](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [C#/.NET 개발자를 위한 GitHub Copilot 마스터하기](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [GitHub Copilot 모험 선택하기](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

