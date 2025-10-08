<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8bcf70fe61c9007c880f9753cc9c3e01",
  "translation_date": "2025-10-08T19:05:23+00:00",
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

이 리소스를 사용하여 시작하려면 다음 단계를 따르세요:

1. **저장소 포크하기**: 클릭 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **저장소 클론하기**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Azure AI Foundry Discord에 가입하여 전문가 및 다른 개발자들과 만나보세요**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 다국어 지원

#### GitHub Action을 통한 지원 (자동화 및 항상 최신 상태 유지)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](./README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

**추가 번역 언어를 지원하고 싶다면 [여기](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)를 참조하세요.**

## 소개

**초보자를 위한 EdgeAI**에 오신 것을 환영합니다. 이 과정은 강력한 AI 기능과 실제 엣지 디바이스 배포 간의 격차를 해소하여 데이터가 생성되고 의사결정이 이루어지는 곳에서 AI의 잠재력을 직접 활용할 수 있도록 돕는 종합적인 여정을 제공합니다.

### 배우게 될 내용

이 과정은 기본 개념부터 실무에 바로 적용 가능한 구현까지 다룹니다:
- 엣지 배포에 최적화된 **소형 언어 모델(SLM)**
- 다양한 플랫폼에서의 **하드웨어 최적화**
- **실시간 추론** 및 개인정보 보호 기능
- 기업 애플리케이션을 위한 **프로덕션 배포** 전략

### EdgeAI가 중요한 이유

EdgeAI는 현대의 중요한 과제를 해결하는 패러다임 전환을 의미합니다:
- **개인정보 보호 및 보안**: 민감한 데이터를 클라우드에 노출하지 않고 로컬에서 처리
- **실시간 성능**: 네트워크 지연을 제거하여 시간에 민감한 애플리케이션에 적합
- **비용 효율성**: 대역폭 및 클라우드 컴퓨팅 비용 절감
- **탄력적 운영**: 네트워크 장애 시에도 기능 유지
- **규제 준수**: 데이터 주권 요구사항 충족

### Edge AI란?

Edge AI는 AI 알고리즘과 언어 모델을 클라우드 리소스에 의존하지 않고 데이터가 생성되는 하드웨어에서 로컬로 실행하는 것을 의미합니다. 이는 지연 시간을 줄이고, 개인정보 보호를 강화하며, 실시간 의사결정을 가능하게 합니다.

### 핵심 원칙:
- **디바이스 내 추론**: AI 모델이 엣지 디바이스(스마트폰, 라우터, 마이크로컨트롤러, 산업용 PC)에서 실행
- **오프라인 기능**: 지속적인 인터넷 연결 없이도 작동
- **낮은 지연 시간**: 실시간 시스템에 적합한 즉각적인 응답
- **데이터 주권**: 민감한 데이터를 로컬에 유지하여 보안 및 규정 준수 강화

### 소형 언어 모델(SLM)

Phi-4, Mistral-7B, Gemma와 같은 SLM은 더 큰 LLM을 엣지 디바이스에 맞게 훈련하거나 축소한 최적화된 버전입니다:
- **메모리 사용량 감소**: 제한된 엣지 디바이스 메모리의 효율적 사용
- **낮은 연산 요구**: CPU 및 엣지 GPU 성능에 최적화
- **빠른 시작 시간**: 응답성 높은 애플리케이션을 위한 신속한 초기화

이 모델들은 다음과 같은 제약 조건을 충족하면서 강력한 NLP 기능을 제공합니다:
- **임베디드 시스템**: IoT 디바이스 및 산업용 컨트롤러
- **모바일 디바이스**: 오프라인 기능을 갖춘 스마트폰 및 태블릿
- **IoT 디바이스**: 제한된 리소스를 가진 센서 및 스마트 디바이스
- **엣지 서버**: 제한된 GPU 리소스를 가진 로컬 처리 장치
- **개인용 컴퓨터**: 데스크톱 및 노트북 배포 시나리오

## 코스 모듈 및 탐색

| 모듈 | 주제 | 초점 영역 | 주요 내용 | 수준 | 소요 시간 |
|------|------|-----------|-----------|------|-----------|
| [📖 00 ](./introduction.md) | [EdgeAI 소개](./introduction.md) | 기초 및 배경 | EdgeAI 개요 • 산업 응용 • SLM 소개 • 학습 목표 | 초급 | 1-2시간 |
| [📚 01](../../Module01) | [EdgeAI 기본](./Module01/README.md) | 클라우드와 엣지 AI 비교 | EdgeAI 기본 • 실제 사례 연구 • 구현 가이드 • 엣지 배포 | 초급 | 3-4시간 |
| [🧠 02](../../Module02) | [SLM 모델 기초](./Module02/README.md) | 모델 계열 및 아키텍처 | Phi 계열 • Qwen 계열 • Gemma 계열 • BitNET • μModel • Phi-Silica | 초급 | 4-5시간 |
| [🚀 03](../../Module03) | [SLM 배포 실습](./Module03/README.md) | 로컬 및 클라우드 배포 | 고급 학습 • 로컬 환경 • 클라우드 배포 | 중급 | 4-5시간 |
| [⚙️ 04](../../Module04) | [모델 최적화 도구](./Module04/README.md) | 크로스 플랫폼 최적화 | 소개 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 워크플로우 통합 | 중급 | 5-6시간 |
| [🔧 05](../../Module05) | [SLMOps 프로덕션](./Module05/README.md) | 프로덕션 운영 | SLMOps 소개 • 모델 디스틸레이션 • 파인튜닝 • 프로덕션 배포 | 고급 | 5-6시간 |
| [🤖 06](../../Module06) | [AI 에이전트 및 함수 호출](./Module06/README.md) | 에이전트 프레임워크 및 MCP | 에이전트 소개 • 함수 호출 • 모델 컨텍스트 프로토콜 | 고급 | 4-5시간 |
| [💻 07](../../Module07) | [플랫폼 구현](./Module07/README.md) | 크로스 플랫폼 샘플 | AI 도구 키트 • Foundry Local • Windows 개발 | 고급 | 3-4시간 |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | 프로덕션 준비 샘플 | 샘플 애플리케이션 (아래 세부 정보 참조) | 전문가 | 8-10시간 |

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

### 🎓 **워크숍: 실습 학습 경로**

프로덕션 준비 구현을 포함한 종합적인 실습 워크숍 자료:

- **[워크숍 가이드](./Workshop/Readme.md)** - 완전한 학습 목표, 결과 및 리소스 탐색
- **Python 샘플** (6개 세션) - 모범 사례, 오류 처리 및 포괄적인 문서화로 업데이트
- **Jupyter 노트북** (8개 인터랙티브) - 벤치마크 및 성능 모니터링과 함께 단계별 튜토리얼
- **세션 가이드** - 각 워크숍 세션에 대한 자세한 마크다운 가이드
- **검증 도구** - 코드 품질을 확인하고 스모크 테스트를 실행하는 스크립트

**구축할 내용:**
- 스트리밍 지원 로컬 AI 채팅 애플리케이션
- 품질 평가(RAGAS)를 포함한 RAG 파이프라인
- 다중 모델 벤치마킹 및 비교 도구
- 다중 에이전트 오케스트레이션 시스템
- 작업 기반 선택을 통한 지능형 모델 라우팅

### 📊 **학습 경로 요약**
- **총 소요 시간**: 36-45시간
- **초급 경로**: 모듈 01-02 (7-9시간)  
- **중급 경로**: 모듈 03-04 (9-11시간)
- **고급 경로**: 모듈 05-07 (12-15시간)
- **전문가 경로**: 모듈 08 (8-10시간)

## 구축할 내용

### 🎯 핵심 역량
- **Edge AI 아키텍처**: 클라우드 통합이 가능한 로컬 우선 AI 시스템 설계
- **모델 최적화**: 엣지 배포를 위해 모델을 양자화하고 압축 (85% 속도 향상, 75% 크기 감소)
- **다중 플랫폼 배포**: Windows, 모바일, 임베디드 및 클라우드-엣지 하이브리드 시스템
- **프로덕션 운영**: 모니터링, 확장 및 프로덕션에서의 Edge AI 유지 관리

### 🏗️ 실용적인 프로젝트
- **Foundry Local 채팅 앱**: 모델 전환이 가능한 Windows 11 네이티브 애플리케이션
- **다중 에이전트 시스템**: 복잡한 워크플로우를 위한 전문 에이전트 코디네이터  
- **RAG 애플리케이션**: 벡터 검색을 활용한 로컬 문서 처리
- **모델 라우터**: 작업 분석을 기반으로 한 지능형 모델 선택
- **API 프레임워크**: 스트리밍 및 상태 모니터링 기능을 갖춘 프로덕션 준비 클라이언트
- **크로스 플랫폼 도구**: LangChain/Semantic Kernel 통합 패턴

### 🏢 산업 응용 분야
**제조업** • **헬스케어** • **자율주행 차량** • **스마트 시티** • **모바일 앱**

## 빠른 시작

**추천 학습 경로** (총 20-30시간):

0. **📖 소개** ([Introduction.md](./introduction.md)): EdgeAI 기초 + 산업 맥락 + 학습 프레임워크
1. **📚 기초** (모듈 01-02): EdgeAI 개념 + SLM 모델 계열
2. **⚙️ 최적화** (모듈 03-04): 배포 + 양자화 프레임워크  
3. **🚀 프로덕션** (모듈 05-06): SLMOps + AI 에이전트 + 함수 호출
4. **💻 구현** (모듈 07-08): 플랫폼 샘플 + Foundry Local 툴킷

각 모듈에는 이론, 실습 과제, 프로덕션 준비 코드 샘플이 포함되어 있습니다.

## 경력 영향

**기술 역할**: EdgeAI 솔루션 아키텍트 • ML 엔지니어 (Edge) • IoT AI 개발자 • 모바일 AI 개발자

**산업 분야**: 제조업 4.0 • 헬스케어 기술 • 자율 시스템 • 핀테크 • 소비자 전자제품

**포트폴리오 프로젝트**: 멀티 에이전트 시스템 • 프로덕션 RAG 앱 • 크로스 플랫폼 배포 • 성능 최적화

## 리포지토리 구조

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## 과정 하이라이트

✅ **점진적 학습**: 이론 → 실습 → 프로덕션 배포  
✅ **실제 사례 연구**: Microsoft, Japan Airlines, 기업 구현 사례  
✅ **실습 샘플**: 50개 이상의 예제, 10개의 종합적인 Foundry Local 데모  
✅ **성능 중심**: 85% 속도 개선, 75% 크기 감소  
✅ **멀티 플랫폼**: Windows, 모바일, 임베디드, 클라우드-엣지 하이브리드  
✅ **프로덕션 준비**: 모니터링, 확장, 보안, 규정 준수 프레임워크

📖 **[학습 가이드 제공](STUDY_GUIDE.md)**: 시간 배분 지침 및 자기 평가 도구를 포함한 구조화된 20시간 학습 경로.

---

**EdgeAI는 AI 배포의 미래를 대표합니다**: 로컬 우선, 개인정보 보호, 효율성. 이러한 기술을 마스터하여 차세대 지능형 애플리케이션을 구축하세요.

## 기타 과정

우리 팀은 다른 과정도 제공합니다! 확인해보세요:

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

## 도움 받기

AI 앱을 구축하다가 막히거나 질문이 있다면 다음을 방문하세요:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

제품 피드백을 제공하거나 빌드 중 오류가 발생하면 다음을 방문하세요:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.