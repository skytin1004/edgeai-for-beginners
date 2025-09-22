<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T12:20:16+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ko"
}
-->
# 변경 로그

EdgeAI for Beginners의 모든 주요 변경 사항은 여기에 기록됩니다. 이 프로젝트는 날짜 기반 항목과 Keep a Changelog 스타일(추가됨, 변경됨, 수정됨, 제거됨, 문서화됨, 이동됨)을 사용합니다.

## 2025-09-18

### 추가됨
- 모듈 08: Microsoft Foundry Local – 완전한 개발자 도구 키트
  - 여섯 개의 세션: 설정, Azure AI Foundry 통합, 오픈소스 모델, 최첨단 데모, 에이전트, 모델-도구 활용
  - `Module08/samples/01`–`06` 폴더에 실행 가능한 샘플 제공, Windows cmd 명령어 포함
    - `01` REST 빠른 채팅 (`chat_quickstart.py`)
    - `02` SDK 빠른 시작(OpenAI/Foundry Local 및 Azure OpenAI 지원 포함) (`sdk_quickstart.py`)
    - `03` CLI 목록 및 벤치마크 (`list_and_bench.cmd`)
    - `04` Chainlit 데모 (`app.py`)
    - `05` 다중 에이전트 오케스트레이션 (`python -m samples.05.agents.coordinator`)
    - `06` 모델-도구 라우터 (`router.py`)
- Session 2 SDK 샘플에서 환경 변수 설정을 통한 Azure OpenAI 지원 추가
- `.vscode/settings.json` 파일을 `Module08/.venv`로 지정하여 Python 분석 해상도 개선
- `.env` 파일에 VS Code/Pylance 인식을 위한 `PYTHONPATH` 힌트 추가

### 변경됨
- 기본 모델을 `phi-4-mini`로 업데이트하여 모듈 08 문서 및 샘플 전반에 적용; 모듈 08 내 남아 있던 `phi-3.5` 언급 제거
- 라우터 (`Module08/samples/06/router.py`) 개선:
  - `foundry service status`를 통한 엔드포인트 검색 및 정규식 파싱
  - 시작 시 `/v1/models` 상태 확인
  - 환경 변수로 구성 가능한 모델 레지스트리 (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- 요구 사항 업데이트: `Module08/requirements.txt`에 `openai` 추가 (`requests`, `chainlit`와 함께)
- Chainlit 샘플 가이드 명확화 및 문제 해결 추가; 워크스페이스 설정을 통한 import 해상도 개선

### 수정됨
- import 문제 해결:
  - 라우터가 더 이상 존재하지 않는 `utils` 모듈에 의존하지 않음; 함수가 인라인 처리됨
  - Coordinator가 상대 import 사용 (`from .specialists import ...`) 및 모듈 경로를 통해 호출됨
  - VS Code/Pylance 설정을 통해 `chainlit` 및 패키지 import 해상도 개선
- `STUDY_GUIDE.md`의 사소한 오타 수정 및 모듈 08 내용 추가

### 제거됨
- 사용되지 않는 `Module08/infra/obs.py` 삭제 및 빈 `infra/` 디렉터리 제거; 관측 패턴은 문서에서 선택적으로 유지

### 이동됨
- 모듈 08 데모를 `Module08/samples` 폴더로 통합, 세션 번호별 폴더로 정리
  - Chainlit 앱을 `samples/04`로 이동
  - 에이전트를 `samples/05`로 이동하고 패키지 해상도를 위한 `__init__.py` 파일 추가

### 문서화됨
- 모듈 08 세션 문서 및 모든 샘플 README에 Microsoft Learn 및 신뢰할 수 있는 벤더 참조 추가
- `Module08/README.md` 업데이트: 샘플 개요, 라우터 구성, 검증 팁 포함
- `Module07/README.md`의 Windows Foundry Local 섹션을 Learn 문서와 대조하여 검증
- `STUDY_GUIDE.md` 업데이트:
  - 모듈 08을 개요, 일정, 진행 추적기에 추가
  - 포괄적인 참조 섹션 추가(Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## 역사적 (요약)
- 코스 구조 및 모듈 설정 완료 (모듈 01–07)
- 반복적인 콘텐츠 현대화, 형식 표준화, 사례 연구 추가
- 최적화 프레임워크 범위 확장 (Llama.cpp, Olive, OpenVINO, Apple MLX)

## 미발표 / 백로그 (제안)
- Foundry Local 가용성을 확인하기 위한 샘플별 선택적 스모크 테스트 추가
- 모델 참조를 정렬하기 위한 번역 검토 (예: `phi-4-mini`)
- 팀이 워크스페이스 전체 엄격성을 선호하는 경우 최소 pyright 구성 추가

---

