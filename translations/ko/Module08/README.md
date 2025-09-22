<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T12:21:42+00:00",
  "source_file": "Module08/README.md",
  "language_code": "ko"
}
-->
# Module 08: Microsoft Foundry Local - 완벽한 개발자 도구 체험

## 개요

Microsoft Foundry Local은 엣지 AI 개발의 차세대 기술로, 개발자들이 강력한 도구를 활용해 AI 애플리케이션을 로컬에서 구축, 배포, 확장할 수 있도록 지원하며 Azure AI Foundry와의 원활한 통합을 유지합니다. 이 모듈은 Foundry Local의 설치부터 고급 에이전트 개발까지 포괄적으로 다룹니다.

**핵심 기술:**
- Microsoft Foundry Local CLI 및 SDK
- Azure AI Foundry 통합
- 디바이스 내 모델 추론
- 로컬 모델 캐싱 및 최적화
- 에이전트 기반 아키텍처

## 모듈 학습 목표

이 모듈을 완료하면 다음을 수행할 수 있습니다:

- **Foundry Local 설정 숙달**: Windows 11 개발을 위한 Foundry Local 설치, 구성 및 최적화
- **다양한 모델 배포**: phi, qwen, deepseek, GPT-OSS-20B 모델을 CLI 명령어로 로컬에서 실행
- **생산 솔루션 구축**: 고급 프롬프트 엔지니어링 및 데이터 통합을 활용한 AI 애플리케이션 생성
- **오픈소스 생태계 활용**: Hugging Face 모델 및 커뮤니티 추가 기능 통합
- **AI 아키텍처 비교**: LLM과 SLM의 장단점 및 배포 전략 이해
- **AI 에이전트 개발**: Foundry Local의 아키텍처와 그라운딩 기능을 활용한 지능형 에이전트 구축
- **모델을 도구로 구현**: 엔터프라이즈 애플리케이션을 위한 모듈형, 맞춤형 AI 솔루션 생성

## 세션 구조

### [1: Foundry Local 시작하기](./01.FoundryLocalSetup.md)
**중점**: 설치, CLI 설정, 모델 캐싱 및 하드웨어 가속

**학습 내용:**
- Windows 11에서 Foundry Local 설치 완료
- CLI 구성 및 명령어 구조
- 최적 성능을 위한 모델 캐싱 전략
- 하드웨어 가속 설정 및 최적화
- phi, qwen, deepseek, GPT-OSS-20B 모델의 실습 배포

**소요 시간**: 2-3시간  
**사전 요구 사항**: Windows 11, 기본 명령줄 지식

---

### [2: Azure AI Foundry를 활용한 AI 솔루션 구축](./02.AzureAIFoundryIntegration.md)
**중점**: 고급 프롬프트 엔지니어링, 데이터 통합 및 실행 가능한 작업

**학습 내용:**
- 고급 프롬프트 엔지니어링 기술
- 데이터 통합 패턴 및 모범 사례
- Foundry Local을 활용한 실행 가능한 AI 작업 생성
- Azure AI Foundry 통합 워크플로우
- 성능 최적화 및 모니터링

**소요 시간**: 2-3시간  
**사전 요구 사항**: 세션 1 완료, Azure 계정(선택 사항)

---

### [3: Foundry Local에서 오픈소스 모델 활용](./03.OpenSourceModels.md)
**중점**: Hugging Face 통합, 모델 선택 전략 및 커뮤니티 추가 기능

**학습 내용:**
- Foundry Local과 Hugging Face 모델 통합
- BYOM(Bring-Your-Own-Model) 전략 및 구현
- Model Mondays 시리즈 통찰 및 커뮤니티 기여
- 맞춤형 모델 배포 및 최적화
- 커뮤니티 모델 평가 및 선택 기준

**소요 시간**: 2-3시간  
**사전 요구 사항**: 세션 1-2 완료, Hugging Face 계정

---

### [4: 최첨단 모델 탐구 - LLM, SLM 및 디바이스 내 추론](./04.CuttingEdgeModels.md)
**중점**: 모델 비교, Phi 및 ONNX Runtime을 활용한 EdgeAI, 고급 데모

**학습 내용:**
- LLM과 SLM의 포괄적 비교 및 사용 사례
- 로컬 vs 클라우드 추론의 장단점 및 의사결정 프레임워크
- Phi 및 ONNX Runtime을 활용한 EdgeAI 구현
- Chainlit RAG 채팅 앱 개발 및 배포
- WebGPU 추론 최적화 기술
- AI PC SDK 통합 및 기능

**소요 시간**: 3-4시간  
**사전 요구 사항**: 세션 1-3 완료, 추론 개념 이해

---

### [5: Foundry Local로 AI 에이전트 빠르게 구축하기](./05.AIPoweredAgents.md)
**중점**: 빠른 GenAI 앱 개발, 시스템 프롬프트, 그라운딩 및 에이전트 아키텍처

**학습 내용:**
- Foundry Local 에이전트 아키텍처 및 설계 패턴
- 에이전트 행동을 위한 시스템 프롬프트 엔지니어링
- 신뢰할 수 있는 에이전트 응답을 위한 그라운딩 기술
- 빠른 GenAI 애플리케이션 개발 워크플로우
- 에이전트 오케스트레이션 및 다중 에이전트 시스템
- AI 에이전트의 생산 배포 전략

**소요 시간**: 3-4시간  
**사전 요구 사항**: 세션 1-4 완료, AI 에이전트 기본 이해

---

### [6: Foundry Local - 모델을 도구로 활용하기](./06.ModelsAsTools.md)
**중점**: 모듈형 AI 솔루션, 디바이스 내 배포 및 엔터프라이즈 확장

**학습 내용:**
- AI 모델을 모듈형, 맞춤형 도구로 활용
- 클라우드 의존 없이 디바이스 내 배포
- 저지연, 비용 효율적, 프라이버시를 보장하는 추론
- SDK, API 및 CLI 통합 패턴
- 특정 사용 사례를 위한 모델 맞춤화
- 로컬에서 Azure AI Foundry로 확장 전략
- 엔터프라이즈 준비 AI 애플리케이션 아키텍처

**소요 시간**: 3-4시간  
**사전 요구 사항**: 이전 세션 모두 완료, 엔터프라이즈 개발 경험 유용

## 사전 요구 사항

### 시스템 요구 사항
- **운영 체제**: Windows 11 (22H2 이상)
- **메모리**: 16GB RAM (대형 모델의 경우 32GB 권장)
- **저장 공간**: 모델 캐싱을 위한 50GB의 여유 공간
- **하드웨어**: NPU 지원 디바이스 권장 (Copilot+ PC), GPU 선택 사항
- **네트워크**: 초기 모델 다운로드를 위한 고속 인터넷

### 개발 환경
- AI Toolkit 확장이 포함된 Visual Studio Code
- Python 3.10+ 및 pip
- 버전 관리를 위한 Git
- PowerShell 또는 명령 프롬프트
- Azure CLI (클라우드 통합 선택 사항)

### 지식 요구 사항
- AI/ML 개념의 기본 이해
- 명령줄 사용 능숙
- Python 프로그래밍 기초
- REST API 개념
- 프롬프트 및 모델 추론 기본 지식

## 모듈 일정

**총 예상 시간**: 15-20시간

| 세션 | 중점 영역 | 시간 | 난이도 |
|------|----------|------|--------|
|  1 | 설정 및 기본 | 2-3시간 | 초급 |
|  2 | AI 솔루션 | 2-3시간 | 중급 |
|  3 | 오픈소스 | 2-3시간 | 중급 |
|  4 | 고급 모델 | 3-4시간 | 고급 |
|  5 | AI 에이전트 | 3-4시간 | 고급 |
|  6 | 엔터프라이즈 도구 | 3-4시간 | 전문가 |

## 주요 자료

### 주요 문서
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local 문서](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays 시리즈](https://aka.ms/model-mondays)

### 커뮤니티 자료
- [Foundry Local 커뮤니티 토론](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry 샘플](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI 개발자 커뮤니티](https://techcommunity.microsoft.com/category/artificialintelligence)

## 학습 결과

이 모듈을 완료하면 다음을 수행할 수 있습니다:

### 기술 숙련도
- **배포 및 관리**: 개발 및 생산 환경에서 Foundry Local 설치 및 관리
- **모델 통합**: Microsoft, Hugging Face 및 커뮤니티 소스의 다양한 모델을 원활하게 활용
- **애플리케이션 구축**: 고급 기능과 최적화를 갖춘 생산 준비 AI 애플리케이션 생성
- **에이전트 개발**: 그라운딩, 추론 및 도구 통합을 갖춘 정교한 AI 에이전트 구현

### 전략적 이해
- **아키텍처 결정**: 로컬 vs 클라우드 배포 간의 정보에 입각한 선택
- **성능 최적화**: 다양한 하드웨어 구성에서 추론 성능 최적화
- **엔터프라이즈 확장**: 로컬 프로토타입에서 엔터프라이즈 배포로 확장 가능한 애플리케이션 설계
- **프라이버시 및 보안**: 로컬 추론을 활용한 프라이버시 보장 AI 솔루션 구현

### 혁신 역량
- **빠른 프로토타이핑**: AI 애플리케이션 개념을 신속하게 구축 및 테스트
- **커뮤니티 통합**: 오픈소스 모델 활용 및 생태계 기여
- **고급 패턴**: RAG, 에이전트 및 도구 통합을 포함한 최첨단 AI 패턴 구현
- **미래 대비 개발**: 신흥 AI 기술 및 패턴에 대비한 애플리케이션 구축

## 시작하기

1. **환경 준비**: 권장 하드웨어 사양을 갖춘 Windows 11 준비
2. **필수 항목 설치**: 개발 도구 및 종속성 설정
3. **세션 1 시작**: Foundry Local 설치 및 기본 설정부터 시작
4. **순차적으로 진행**: 최적의 학습 진행을 위해 세션을 순서대로 완료
5. **지속적인 연습**: 실습과 프로젝트를 통해 개념 적용

## 성공 지표

모듈 진행 상황을 추적하세요:

- [ ] Foundry Local 설치 및 구성 성공
- [ ] 최소 4개의 다른 모델 패밀리 배포 및 실행
- [ ] 데이터 통합을 포함한 완전한 AI 솔루션 구축
- [ ] 최소 2개의 오픈소스 모델 통합
- [ ] 기능적인 RAG 채팅 애플리케이션 생성
- [ ] AI 에이전트 개발 및 배포
- [ ] 모델을 도구로 활용하는 아키텍처 구현

## 샘플 빠른 시작

### 1) 환경 설정 (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) 로컬 모델 시작 (새 터미널)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Chainlit 데모 실행 (세션 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) 다중 에이전트 코디네이터 실행 (세션 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

연결 오류가 발생하면 Foundry Local을 확인하세요:
```cmd
curl http://localhost:8000/v1/models
```

### 라우터 구성 (세션 6)
라우터는 빠른 상태 확인을 수행하며 환경 기반 구성을 지원합니다:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

이 모듈은 Microsoft의 엔터프라이즈급 도구와 오픈소스 생태계의 유연성과 혁신을 결합한 엣지 AI 개발의 최첨단을 대표합니다. Foundry Local을 숙달함으로써 AI 애플리케이션 개발의 최전선에 설 수 있습니다.

Azure OpenAI(세션 2)를 위해 필요한 환경 변수 및 API 버전 설정은 샘플 README를 참조하세요.

## 샘플 개요

- `samples/01`: Foundry Local로 빠른 REST 채팅 (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK 통합 (`sdk_quickstart.py`).
- `samples/03`: 모델 탐색 + 빠른 벤치마크 (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG 데모 (`app.py`).
- `samples/05`: 다중 에이전트 오케스트레이션 (`python -m samples.05.agents.coordinator`).
- `samples/06`: 모델을 도구로 활용하는 라우터 (`python samples\06\router.py`).

---

