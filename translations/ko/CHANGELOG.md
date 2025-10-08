<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T19:02:29+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ko"
}
-->
# 변경 로그

EdgeAI for Beginners의 모든 주요 변경 사항은 여기에 기록됩니다. 이 프로젝트는 날짜 기반 항목과 Keep a Changelog 스타일(추가됨, 변경됨, 수정됨, 제거됨, 문서, 이동됨)을 사용합니다.

## 2025-10-08

### 추가됨 - 워크숍 종합 업데이트
- **워크숍 README.md 완전 재작성**:
  - Edge AI의 가치 제안(프라이버시, 성능, 비용)을 설명하는 포괄적인 소개 추가
  - 상세한 역량을 포함한 6개의 핵심 학습 목표 생성
  - 결과물 및 역량 매트릭스를 포함한 학습 결과 표 추가
  - 산업 관련성을 위한 경력 준비 기술 섹션 포함
  - 사전 요구 사항 및 3단계 설정을 포함한 빠른 시작 가이드 추가
  - Python 샘플에 대한 리소스 표 생성(8개의 파일과 실행 시간 포함)
  - Jupyter 노트북 표 추가(난이도 등급이 있는 8개의 노트북)
  - "사용 시기" 가이드를 포함한 주요 문서 7개의 문서화 표 생성
  - 다양한 기술 수준에 맞는 학습 경로 추천 추가

- **워크숍 검증 및 테스트 인프라**:
  - `scripts/validate_samples.py` 생성 - 구문, 가져오기 및 모범 사례에 대한 종합적인 검증 도구
  - `scripts/test_samples.py` 생성 - 모든 Python 샘플에 대한 스모크 테스트 실행기
  - `scripts/README.md`에 검증 문서 추가

- **포괄적인 문서화**:
  - `SAMPLES_UPDATE_SUMMARY.md` 생성 - 모든 개선 사항을 다룬 400줄 이상의 상세 가이드
  - `UPDATE_COMPLETE.md` 생성 - 업데이트 완료에 대한 요약 보고서
  - `QUICK_REFERENCE.md` 생성 - 워크숍을 위한 빠른 참조 카드

### 변경됨 - 워크숍 Python 샘플 현대화
- **8개의 모든 Python 샘플이 모범 사례로 업데이트됨**:
  - 모든 I/O 작업에 대해 try-except 블록을 사용한 오류 처리 강화
  - 타입 힌트 및 포괄적인 docstring 추가
  - 일관된 [INFO]/[ERROR]/[RESULT] 로깅 패턴 구현
  - 설치 힌트를 포함한 선택적 가져오기 보호
  - 모든 샘플에서 사용자 피드백 개선

- **session01/chat_bootstrap.py**:
  - 포괄적인 오류 메시지를 사용한 클라이언트 초기화 강화
  - 청크 유효성 검사를 통한 스트리밍 오류 처리 개선
  - 서비스 이용 불가에 대한 예외 처리 추가

- **session02/rag_pipeline.py**:
  - 설치 힌트를 포함한 sentence-transformers 가져오기 보호 추가
  - 임베딩 및 생성 작업에 대한 오류 처리 강화
  - 구조화된 결과를 사용한 출력 형식 개선

- **session02/rag_eval_ragas.py**:
  - 선택적 가져오기(ragas, datasets)를 사용자 친화적인 오류 메시지로 보호
  - 평가 지표에 대한 오류 처리 추가
  - 평가 결과에 대한 출력 형식 개선

- **session03/benchmark_oss_models.py**:
  - 우아한 강등 구현(모델 실패 시 계속 진행)
  - 상세한 진행 상황 보고 및 모델별 오류 처리 추가
  - 포괄적인 오류 복구를 통한 통계 계산 개선

- **session04/model_compare.py**:
  - 타입 힌트 추가(Tuple 반환 타입)
  - 구조화된 JSON 결과를 사용한 출력 형식 개선
  - 모델별 오류 처리 및 복구 구현

- **session05/agents_orchestrator.py**:
  - Agent.act()에 포괄적인 docstring 추가
  - 단계별 로깅을 사용한 파이프라인 오류 처리 추가
  - 메모리 관리 및 상태 추적 개선

- **session06/models_router.py**:
  - 모든 라우팅 구성 요소에 대한 함수 문서화 강화
  - route() 함수에서 상세한 로깅 추가
  - 구조화된 결과를 사용한 테스트 출력 개선

- **session06/models_pipeline.py**:
  - chat() 헬퍼 함수에 대한 오류 처리 추가
  - 파이프라인()에 단계 로깅 및 진행 상황 보고 추가
  - main()에 포괄적인 오류 복구 추가

### 문서 - 워크숍 문서 개선
- 워크숍 섹션을 강조하는 메인 README.md 업데이트
- 포괄적인 워크숍 섹션을 포함한 STUDY_GUIDE.md 개선:
  - 학습 목표 및 학습 초점 영역
  - 자기 평가 질문
  - 시간 추정이 포함된 실습
  - 집중 및 파트타임 학습을 위한 시간 할당
  - 진행 추적 템플릿에 워크숍 추가
- 시간 할당 가이드를 20시간에서 30시간으로 업데이트(워크숍 포함)
- README에 워크숍 샘플 설명 및 학습 결과 추가

### 수정됨
- 워크숍 샘플 전반에 걸친 일관되지 않은 오류 처리 패턴 해결
- 적절한 보호 장치를 사용하여 선택적 종속성 가져오기 오류 수정
- 주요 함수에서 누락된 타입 힌트 수정
- 오류 시 사용자 피드백 부족 문제 해결
- 종합적인 테스트 인프라로 검증 문제 해결

---

## 2025-09-23

### 변경됨 - 주요 모듈 08 현대화
- **Microsoft Foundry-Local 저장소 패턴과의 포괄적인 정렬**
  - 모든 코드 예제를 최신 `FoundryLocalManager` 및 OpenAI SDK 통합을 사용하도록 업데이트
  - 더 이상 사용되지 않는 수동 `requests` 호출을 적절한 SDK 사용으로 대체
  - 공식 Microsoft 문서 및 샘플과 구현 패턴 정렬

- **05.AIPoweredAgents.md 현대화**:
  - 최신 SDK 패턴을 사용하도록 다중 에이전트 오케스트레이션 업데이트
  - 고급 기능(피드백 루프, 성능 모니터링)을 사용한 코디네이터 구현 강화
  - 포괄적인 오류 처리 및 서비스 상태 확인 추가
  - 로컬 샘플(`samples/05/multi_agent_orchestration.ipynb`)에 대한 적절한 참조 통합
  - 더 이상 사용되지 않는 `functions` 대신 최신 `tools` 매개변수를 사용하는 함수 호출 예제 업데이트
  - 모니터링 및 통계 추적을 포함한 프로덕션 준비 패턴 추가

- **06.ModelsAsTools.md 완전 재작성**:
  - 기본 도구 레지스트리를 지능형 모델 라우터 구현으로 대체
  - 다양한 작업 유형(일반, 추론, 코드, 창의적)을 위한 키워드 기반 모델 선택 추가
  - 유연한 모델 할당이 가능한 환경 기반 구성 통합
  - 포괄적인 서비스 상태 모니터링 및 오류 처리로 강화
  - 요청 모니터링 및 성능 추적을 포함한 프로덕션 배포 패턴 추가
  - `samples/06/router.py` 및 `samples/06/model_router.ipynb`의 로컬 구현과 정렬

- **문서 구조 개선**:
  - 현대화 및 SDK 정렬을 강조하는 개요 섹션 추가
  - 가독성을 높이기 위한 이모지 및 더 나은 서식 추가
  - 문서 전반에 걸쳐 로컬 샘플 파일에 대한 적절한 참조 추가
  - 프로덕션 준비 구현 가이드 및 모범 사례 포함

### 추가됨
- 최신 SDK 통합을 강조하는 모듈 08 파일의 포괄적인 개요 섹션
- 고급 기능(다중 에이전트 시스템, 지능형 라우팅)을 보여주는 아키텍처 하이라이트
- 실습 경험을 위한 로컬 샘플 구현에 대한 직접 참조
- 모니터링 및 오류 처리 패턴을 사용한 프로덕션 배포 가이드
- 고급 기능 및 벤치마크가 포함된 대화형 Jupyter 노트북 예제

### 수정됨
- 문서와 실제 샘플 구현 간의 정렬 불일치 해결
- 모듈 08 전반에 걸친 오래된 SDK 사용 패턴 수정
- 포괄적인 로컬 샘플 라이브러리에 대한 누락된 참조 수정
- 다양한 섹션 간의 일관되지 않은 구현 접근 방식 해결

---

## 2025-09-18

### 추가됨
- 모듈 08: Microsoft Foundry Local – 완전한 개발자 도구 키트
  - 여섯 개의 세션: 설정, Azure AI Foundry 통합, 오픈 소스 모델, 최첨단 데모, 에이전트, 모델-도구
  - Windows cmd 지침이 포함된 `Module08/samples/01`–`06`에서 실행 가능한 샘플
    - `01` REST 빠른 채팅(`chat_quickstart.py`)
    - `02` OpenAI/Foundry Local 및 Azure OpenAI 지원을 포함한 SDK 빠른 시작(`sdk_quickstart.py`)
    - `03` CLI 목록 및 벤치(`list_and_bench.cmd`)
    - `04` Chainlit 데모(`app.py`)
    - `05` 다중 에이전트 오케스트레이션(`python -m samples.05.agents.coordinator`)
    - `06` 모델-도구 라우터(`router.py`)
- 환경 변수 구성을 사용한 세션 2 SDK 샘플에서 Azure OpenAI 지원
- Python 분석 해상도를 개선하기 위해 `Module08/.venv`를 가리키는 `.vscode/settings.json`
- VS Code/Pylance 인식을 위한 `PYTHONPATH` 힌트가 포함된 `.env`

### 변경됨
- 모듈 08 문서 및 샘플 전반에 걸쳐 기본 모델을 `phi-4-mini`로 업데이트; 모듈 08 내의 남아 있는 `phi-3.5` 언급 제거
- 라우터(`Module08/samples/06/router.py`) 개선:
  - 정규식 구문 분석을 사용한 `foundry service status`를 통한 엔드포인트 검색
  - 시작 시 `/v1/models` 상태 확인
  - 환경 구성 가능한 모델 레지스트리(`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- 요구 사항 업데이트: `Module08/requirements.txt`에 `openai` 추가(`requests`, `chainlit`과 함께)
- Chainlit 샘플 가이드를 명확히 하고 문제 해결 추가; 작업 공간 설정을 통한 가져오기 해결

### 수정됨
- 가져오기 문제 해결:
  - 라우터가 더 이상 존재하지 않는 `utils` 모듈에 의존하지 않음; 함수가 인라인으로 통합됨
  - 코디네이터가 상대적 가져오기(`from .specialists import ...`)를 사용하며 모듈 경로를 통해 호출됨
  - VS Code/Pylance 구성을 통해 `chainlit` 및 패키지 가져오기 해결
- `STUDY_GUIDE.md`의 사소한 오타 수정 및 모듈 08 적용 범위 추가

### 제거됨
- 사용되지 않는 `Module08/infra/obs.py` 삭제 및 빈 `infra/` 디렉토리 제거; 문서에서 선택적으로 관찰 가능성 패턴 유지

### 이동됨
- 모듈 08 데모를 세션 번호가 있는 폴더로 `Module08/samples`에 통합
  - Chainlit 앱을 `samples/04`로 이동
  - 에이전트를 `samples/05`로 이동하고 패키지 해상도를 위한 `__init__.py` 파일 추가

### 문서
- 모듈 08 세션 문서 및 모든 샘플 README에 Microsoft Learn 및 신뢰할 수 있는 공급업체 참조 추가
- `Module08/README.md`를 샘플 개요, 라우터 구성 및 검증 팁으로 업데이트
- `Module07/README.md` Windows Foundry Local 섹션을 Learn 문서와 검증
- `STUDY_GUIDE.md` 업데이트:
  - 개요, 일정, 진행 상황 추적기에 모듈 08 추가
  - 포괄적인 참조 섹션 추가(Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## 과거 (요약)
- 과정 아키텍처 및 모듈(모듈 01–07) 설립
- 점진적인 콘텐츠 현대화, 서식 표준화 및 사례 연구 추가
- 최적화 프레임워크 범위 확장(Llama.cpp, Olive, OpenVINO, Apple MLX)

## 미발표 / 백로그 (제안)
- Foundry Local 가용성을 검증하기 위한 선택적 샘플별 스모크 테스트
- 모델 참조(예: `phi-4-mini`)와 일치하도록 번역 검토
- 팀이 작업 공간 전체의 엄격성을 선호하는 경우 최소 pyright 구성 추가

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.