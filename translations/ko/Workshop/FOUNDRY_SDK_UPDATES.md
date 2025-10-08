<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T19:07:36+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "ko"
}
-->
# Foundry Local SDK 업데이트

## 개요

**공식 Foundry Local Python SDK**를 올바르게 사용하기 위해 Workshop 노트북과 유틸리티를 다음 패턴에 따라 업데이트했습니다:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## 수정된 파일

### 1. `Workshop/samples/workshop_utils.py`

**변경 사항:**
- ✅ `foundry-local-sdk` 패키지에 대한 import 오류 처리 추가
- ✅ 공식 SDK 패턴을 활용한 문서화 강화
- ✅ 유니코드 심볼(✓, ✗, ⚠)을 사용한 로깅 개선
- ✅ 예제를 포함한 포괄적인 docstring 추가
- ✅ CLI 명령어를 참조하는 더 나은 오류 메시지 추가
- ✅ 공식 SDK 문서와 일치하도록 주석 업데이트

**주요 개선 사항:**

#### Import 오류 처리
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### 개선된 `get_client()` 함수
- SDK 초기화 패턴에 대한 자세한 문서 추가
- `FoundryLocalManager`가 서비스를 자동으로 시작한다는 점 명시
- 하드웨어 최적화된 변형으로 모델 별칭 해석 설명
- 엔드포인트 정보와 함께 로깅 개선
- 문제 해결 단계를 제안하는 더 나은 오류 메시지 추가

#### 개선된 `chat_once()` 함수
- 사용 예제를 포함한 포괄적인 docstring 추가
- OpenAI SDK 호환성 명시
- 스트리밍 지원 문서화(kwarg를 통해)
- CLI 명령어 제안을 포함한 개선된 오류 메시지 추가
- 모델 가용성 확인에 대한 주석 추가

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**변경 사항:**
- ✅ SDK 참조를 포함한 모든 마크다운 셀 업데이트
- ✅ SDK 패턴 설명을 포함한 코드 주석 개선
- ✅ 셀 문서화 및 설명 강화
- ✅ 문제 해결 가이드 추가
- ✅ 모델 카탈로그 업데이트('gpt-oss-20b'를 'phi-3.5-mini'로 교체)
- ✅ 시각적 표시를 활용한 출력 형식 개선
- ✅ SDK 링크 및 참조 추가

**셀별 업데이트:**

#### 셀 1 (제목)
- SDK 문서 링크 추가
- 공식 GitHub 저장소 참조

#### 셀 2 (시나리오)
- 번호 매기기 형식으로 재구성
- 의도 기반 라우팅 패턴 명확화
- 로컬 실행의 이점 강조

#### 셀 3 (의존성 설치)
- 각 패키지가 제공하는 기능 설명 추가
- SDK 기능 문서화(별칭 해석, 하드웨어 최적화)

#### 셀 4 (환경 설정)
- 함수 docstring 강화
- SDK 패턴을 설명하는 인라인 주석 추가
- 모델 카탈로그 구조 문서화
- 우선순위/기능 매칭 명확화

#### 셀 5 (카탈로그 확인)
- 시각적 체크 표시(✓) 추가
- 출력 형식 개선

#### 셀 6 (의도 감지 테스트)
- 출력 형식을 테이블 스타일로 재구성
- 의도와 선택된 모델 모두 표시

#### 셀 7 (라우팅 함수)
- 포괄적인 SDK 패턴 설명
- 초기화 흐름 문서화
- 모든 기능 나열(재시도, 추적, 오류)
- SDK 참조 링크 추가

#### 셀 8 (배치 데모)
- 기대 결과에 대한 설명 강화
- 문제 해결 섹션 추가
- 디버깅을 위한 CLI 명령어 포함
- 출력 디스플레이 형식 개선

### 3. `Workshop/notebooks/session06_README.md` (새 파일)

**포괄적인 문서 작성:**

1. **개요**: 아키텍처 다이어그램 및 구성 요소 설명
2. **SDK 통합**: 공식 패턴을 따르는 코드 예제
3. **사전 요구사항**: 단계별 설정 지침
4. **사용법**: 노트북 실행 및 사용자 정의 방법
5. **모델 별칭**: 하드웨어 최적화된 변형 설명
6. **문제 해결**: 일반적인 문제와 해결책
7. **확장**: 의도, 모델 및 사용자 정의 로직 추가 방법
8. **성능 팁**: 프로덕션 사용을 위한 모범 사례
9. **리소스**: 공식 문서 및 커뮤니티 링크

## SDK 패턴 구현

### 공식 패턴 (Foundry Local 문서에서 발췌)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### 워크숍 유틸리티에서의 구현

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**우리 접근 방식의 이점:**
- ✅ 공식 SDK 패턴을 정확히 따름
- ✅ 반복 초기화를 방지하기 위한 캐싱 추가
- ✅ 프로덕션 안정성을 위한 재시도 로직 추가
- ✅ 토큰 사용량 추적 지원
- ✅ 더 나은 오류 메시지 제공
- ✅ 공식 예제와의 호환성 유지

## 모델 카탈로그 변경 사항

### 변경 전
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### 변경 후
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**이유:** 'gpt-oss-20b'(비표준 별칭)를 'phi-3.5-mini'(공식 Foundry Local 별칭)로 교체.

## 의존성

### 업데이트된 requirements.txt

워크숍 requirements.txt에는 이미 다음이 포함되어 있습니다:
```
foundry-local-sdk
openai>=1.30.0
```

Foundry Local 통합에 필요한 패키지는 이것뿐입니다.

## 업데이트 테스트

### 1. Foundry Local 실행 확인

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. 사용 가능한 모델 확인

```bash
foundry model ls
```

다음 모델이 사용 가능하거나 자동 다운로드되어야 합니다:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. 노트북 실행

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

또는 VS Code에서 열어 모든 셀을 실행하세요.

### 4. 예상 동작

**셀 1 (설치):** 패키지가 성공적으로 설치됨  
**셀 2 (설정):** 오류 없이 실행, import 성공  
**셀 3 (확인):** 모델 목록과 함께 ✓ 표시  
**셀 4 (의도 테스트):** 의도 감지 결과 표시  
**셀 5 (라우터):** ✓ 라우트 함수 준비 완료 표시  
**셀 6 (실행):** 프롬프트를 모델로 라우팅하고 결과 표시  

### 5. 연결 오류 문제 해결

`APIConnectionError: Connection error`가 표시되면:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## 환경 변수

다음 환경 변수를 지원합니다:

| 변수 | 기본값 | 설명 |
|------|--------|------|
| `SHOW_USAGE` | `0` | 토큰 사용량을 출력하려면 `1`로 설정 |
| `RETRY_ON_FAIL` | `1` | 재시도 로직 활성화 |
| `RETRY_BACKOFF` | `1.0` | 초기 재시도 지연(초) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | 서비스 엔드포인트 재정의 |

### 사용 예제

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## 기존 패턴에서의 마이그레이션

기존 코드가 직접 API 호출을 사용하는 경우, 다음과 같이 마이그레이션할 수 있습니다:

### 이전 (직접 API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### 이후 (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### 마이그레이션의 이점
- ✅ 자동 서비스 관리
- ✅ 모델 별칭 해석
- ✅ 하드웨어 최적화 선택
- ✅ 더 나은 오류 처리
- ✅ OpenAI SDK 호환성
- ✅ 스트리밍 지원

## 참고 자료

### 공식 문서
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local  
- **Python SDK 소스**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **CLI 참조**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **문제 해결**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### 워크숍 리소스
- **세션 06 README**: `Workshop/notebooks/session06_README.md`  
- **워크숍 유틸리티**: `Workshop/samples/workshop_utils.py`  
- **샘플 노트북**: `Workshop/notebooks/session06_models_router.ipynb`  

### 커뮤니티
- **Discord**: https://aka.ms/foundry-local-discord  
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues  

## 다음 단계

1. **변경 사항 검토**: 업데이트된 파일을 읽어보세요  
2. **노트북 테스트**: session06_models_router.ipynb 실행  
3. **SDK 확인**: foundry-local-sdk가 설치되었는지 확인  
4. **서비스 확인**: Foundry Local이 실행 중인지 확인  
5. **문서 탐색**: 새로운 session06_README.md 읽기  

## 요약

이번 업데이트는 워크숍 자료가 GitHub 저장소에 문서화된 **공식 Foundry Local SDK 패턴**을 정확히 따르도록 보장합니다. 모든 코드 예제, 문서 및 유틸리티는 이제 Microsoft의 로컬 AI 모델 배포를 위한 권장 모범 사례와 일치합니다.

이번 변경 사항은 다음을 개선합니다:
- ✅ **정확성**: 공식 SDK 패턴 사용  
- ✅ **문서화**: 포괄적인 설명 및 예제  
- ✅ **오류 처리**: 더 나은 메시지 및 문제 해결 가이드  
- ✅ **유지보수성**: 공식 규칙 준수  
- ✅ **사용자 경험**: 명확한 지침 및 디버깅 지원  

---

**업데이트 날짜:** 2025년 10월 8일  
**SDK 버전:** foundry-local-sdk (최신)  
**워크숍 브랜치:** Reactor  

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.