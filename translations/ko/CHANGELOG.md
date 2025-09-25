<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T10:37:30+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ko"
}
-->
# 변경 로그

EdgeAI for Beginners의 모든 주요 변경 사항은 여기에 기록됩니다. 이 프로젝트는 날짜 기반 항목과 Keep a Changelog 스타일(추가됨, 변경됨, 수정됨, 제거됨, 문서화됨, 이동됨)을 사용합니다.

## 2025-09-23

### 변경됨 - 모듈 08 대규모 현대화
- **Microsoft Foundry-Local 저장소 패턴과의 포괄적 정렬**
  - 모든 코드 예제를 최신 `FoundryLocalManager` 및 OpenAI SDK 통합으로 업데이트
  - 사용이 중단된 수동 `requests` 호출을 적절한 SDK 사용으로 대체
  - 공식 Microsoft 문서 및 샘플과 구현 패턴을 정렬

- **05.AIPoweredAgents.md 현대화**:
  - 최신 SDK 패턴을 사용하여 다중 에이전트 오케스트레이션 업데이트
  - 고급 기능(피드백 루프, 성능 모니터링)을 포함한 코디네이터 구현 강화
  - 포괄적인 오류 처리 및 서비스 상태 확인 추가
  - 로컬 샘플(`samples/05/multi_agent_orchestration.ipynb`)에 대한 적절한 참조 통합
  - 사용이 중단된 `functions` 대신 최신 `tools` 매개변수를 사용하는 함수 호출 예제 업데이트
  - 모니터링 및 통계 추적을 포함한 프로덕션 준비 패턴 추가

- **06.ModelsAsTools.md 완전 재작성**:
  - 기본 도구 레지스트리를 지능형 모델 라우터 구현으로 대체
  - 다양한 작업 유형(일반, 추론, 코드, 창의적)에 대한 키워드 기반 모델 선택 추가
  - 유연한 모델 할당이 가능한 환경 기반 구성 통합
  - 포괄적인 서비스 상태 모니터링 및 오류 처리로 강화
  - 요청 모니터링 및 성능 추적을 포함한 프로덕션 배포 패턴 추가
  - 로컬 구현(`samples/06/router.py` 및 `samples/06/model_router.ipynb`)과 정렬

- **문서 구조 개선**:
  - 현대화 및 SDK 정렬을 강조하는 개요 섹션 추가
  - 읽기 용이성을 높이기 위해 이모지와 더 나은 포맷팅으로 강화
  - 문서 전체에 로컬 샘플 파일에 대한 적절한 참조 추가
  - 프로덕션 준비 구현 지침 및 모범 사례 포함

### 추가됨
- 모듈 08 파일에 현대적 SDK 통합을 강조하는 포괄적 개요 섹션
- 고급 기능(다중 에이전트 시스템, 지능형 라우팅)을 보여주는 아키텍처 하이라이트
- 실습 경험을 위한 로컬 샘플 구현에 대한 직접 참조
- 모니터링 및 오류 처리 패턴을 포함한 프로덕션 배포 지침
- 고급 기능 및 벤치마크를 포함한 대화형 Jupyter 노트북 예제

### 수정됨
- 문서와 실제 샘플 구현 간의 정렬 불일치
- 모듈 08 전반에 걸친 사용이 중단된 SDK 사용 패턴
- 포괄적인 로컬 샘플 라이브러리에 대한 누락된 참조
- 섹션 간 일관성 없는 구현 접근 방식

---

## 2025-09-18

### 추가됨
- 모듈 08: Microsoft Foundry Local – 완전한 개발자 도구 키트
  - 여섯 세션: 설정, Azure AI Foundry 통합, 오픈소스 모델, 최첨단 데모, 에이전트, 모델-도구 활용
  - `Module08/samples/01`–`06` 아래 실행 가능한 샘플과 Windows cmd 명령어 포함
    - `01` REST 빠른 채팅 (`chat_quickstart.py`)
    - `02` OpenAI/Foundry Local 및 Azure OpenAI 지원 SDK 빠른 시작 (`sdk_quickstart.py`)
    - `03` CLI 목록 및 벤치마크 (`list_and_bench.cmd`)
    - `04` Chainlit 데모 (`app.py`)
    - `05` 다중 에이전트 오케스트레이션 (`python -m samples.05.agents.coordinator`)
    - `06` 모델-도구 라우터 (`router.py`)
- 세션 2 SDK 샘플에서 환경 변수 구성을 통한 Azure OpenAI 지원
- `.vscode/settings.json`을 `Module08/.venv`로 지정하여 Python 분석 해상도 개선
- `.env`에 VS Code/Pylance 인식을 위한 `PYTHONPATH` 힌트 추가

### 변경됨
- 기본 모델을 모듈 08 문서 및 샘플 전반에서 `phi-4-mini`로 업데이트; 모듈 08 내 남아 있던 `phi-3.5` 언급 제거
- 라우터(`Module08/samples/06/router.py`) 개선:
  - 정규식 분석을 통한 `foundry service status`를 통한 엔드포인트 검색
  - 시작 시 `/v1/models` 상태 확인
  - 환경 구성 가능한 모델 레지스트리(`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- 요구 사항 업데이트: `Module08/requirements.txt`에 `openai` 추가(`requests`, `chainlit`와 함께)
- Chainlit 샘플 지침 명확화 및 문제 해결 추가; 워크스페이스 설정을 통한 가져오기 해상도

### 수정됨
- 가져오기 문제 해결:
  - 라우터가 더 이상 존재하지 않는 `utils` 모듈에 의존하지 않음; 함수가 인라인 처리됨
  - 코디네이터가 상대적 가져오기(`from .specialists import ...`)를 사용하며 모듈 경로를 통해 호출됨
  - VS Code/Pylance 구성을 통해 `chainlit` 및 패키지 가져오기 해결
- `STUDY_GUIDE.md`의 사소한 오타 수정 및 모듈 08 커버리지 추가

### 제거됨
- 사용되지 않는 `Module08/infra/obs.py` 삭제 및 빈 `infra/` 디렉토리 제거; 관측 가능성 패턴은 문서에서 선택 사항으로 유지

### 이동됨
- 모듈 08 데모를 `Module08/samples` 아래 세션 번호 폴더로 통합
  - Chainlit 앱을 `samples/04`로 이동
  - 에이전트를 `samples/05`로 이동하고 패키지 해상도를 위한 `__init__.py` 파일 추가

### 문서화됨
- 모듈 08 세션 문서 및 모든 샘플 README에 Microsoft Learn 및 신뢰할 수 있는 공급업체 참조 추가
- `Module08/README.md`를 샘플 개요, 라우터 구성 및 검증 팁으로 업데이트
- `Module07/README.md` Windows Foundry Local 섹션을 Learn 문서와 검증
- `STUDY_GUIDE.md` 업데이트:
  - 개요, 일정, 진행 추적기에 모듈 08 추가
  - 포괄적인 참조 섹션 추가(Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## 역사적 (요약)
- 코스 아키텍처 및 모듈 설정(모듈 01–07)
- 반복적인 콘텐츠 현대화, 포맷 표준화 및 사례 연구 추가
- 최적화 프레임워크 범위 확장(Llama.cpp, Olive, OpenVINO, Apple MLX)

## 미공개 / 백로그 (제안)
- Foundry Local 가용성을 검증하기 위한 샘플별 선택적 스모크 테스트
- 모델 참조(`phi-4-mini`)를 정렬하기 위한 번역 검토
- 팀이 워크스페이스 전체 엄격성을 선호하는 경우 최소 pyright 구성 추가

---

