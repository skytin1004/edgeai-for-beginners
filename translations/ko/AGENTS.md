<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:27:21+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ko"
}
-->
# AGENTS.md

## 프로젝트 개요

EdgeAI for Beginners는 소형 언어 모델(SLM)을 활용한 Edge AI 개발을 교육하는 포괄적인 학습 자료 저장소입니다. 이 과정은 EdgeAI의 기본 개념, 모델 배포, 최적화 기술, Microsoft Foundry Local 및 다양한 AI 프레임워크를 활용한 실무 구현을 다룹니다.

**주요 기술:**
- Python 3.8+ (AI/ML 샘플의 주요 언어)
- .NET C# (AI/ML 샘플)
- JavaScript/Node.js 및 Electron (데스크톱 애플리케이션용)
- Microsoft Foundry Local SDK
- Microsoft Windows ML
- VSCode AI Toolkit
- OpenAI SDK
- AI 프레임워크: LangChain, Semantic Kernel, Chainlit
- 모델 최적화: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**저장소 유형:** 8개의 모듈과 10개의 포괄적인 샘플 애플리케이션을 포함한 교육 콘텐츠 저장소

**아키텍처:** Edge AI 배포 패턴을 실습 샘플로 보여주는 다중 모듈 학습 경로

## 저장소 구조

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## 설정 명령어

### 저장소 설정

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python 샘플 설정 (Module08 및 Python 샘플)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js 샘플 설정 (샘플 08 - Windows 채팅 앱)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local 설정

Module08 샘플을 실행하려면 Foundry Local이 필요합니다:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## 개발 워크플로

### 콘텐츠 개발

이 저장소는 주로 **Markdown 교육 콘텐츠**를 포함합니다. 변경 시:

1. 적절한 모듈 디렉터리에서 `.md` 파일을 편집합니다.
2. 기존 형식 패턴을 따릅니다.
3. 코드 예제가 정확하고 테스트되었는지 확인합니다.
4. 필요한 경우 해당 번역 콘텐츠를 업데이트합니다 (또는 자동화에 맡깁니다).

### 샘플 애플리케이션 개발

Python 샘플 (샘플 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron 샘플 (샘플 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### 샘플 애플리케이션 테스트

Python 샘플은 자동화된 테스트가 없지만 실행하여 검증할 수 있습니다:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron 샘플은 테스트 인프라를 포함합니다:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## 테스트 지침

### 콘텐츠 검증

저장소는 자동 번역 워크플로를 사용합니다. 번역에 대한 수동 테스트는 필요하지 않습니다.

**콘텐츠 변경에 대한 수동 검증:**
1. `.md` 파일을 미리 보기로 렌더링하여 검토합니다.
2. 모든 링크가 유효한 대상에 연결되는지 확인합니다.
3. 문서에 포함된 코드 스니펫을 테스트합니다.
4. 이미지가 올바르게 로드되는지 확인합니다.

### 샘플 애플리케이션 테스트

**Module08/samples/08 (Electron 앱)는 포괄적인 테스트를 포함합니다:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python 샘플은 수동 테스트가 필요합니다:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## 코드 스타일 지침

### Markdown 콘텐츠

- 일관된 제목 계층 구조 사용 (#는 제목, ##는 주요 섹션, ###는 하위 섹션)
- 언어 지정자를 포함한 코드 블록 사용: ```python, ```bash, ```javascript
- 표, 목록, 강조 표시에 기존 형식을 따릅니다.
- 읽기 쉽게 줄을 유지합니다 (~80-100자 목표, 엄격하지 않음)
- 내부 참조에 상대 링크 사용

### Python 코드 스타일

- PEP 8 규칙 준수
- 적절한 경우 타입 힌트 사용
- 함수 및 클래스에 docstring 포함
- 의미 있는 변수 이름 사용
- 함수는 집중적이고 간결하게 유지

### JavaScript/Node.js 코드 스타일

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**주요 규칙:**
- 샘플 08에 제공된 ESLint 구성 사용
- 코드 포맷팅을 위한 Prettier 사용
- 최신 ES6+ 문법 사용
- 코드베이스의 기존 패턴을 따릅니다.

## Pull Request 지침

### 제목 형식
```
[ModuleXX] Brief description of change
```
 또는 ```
[Module08/samples/XX] Description for sample changes
```

### 제출 전

**콘텐츠 변경의 경우:**
- 수정된 모든 Markdown 파일을 미리 보기로 확인합니다.
- 링크와 이미지가 작동하는지 확인합니다.
- 오타 및 문법 오류를 확인합니다.

**샘플 코드 변경 (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python 샘플 변경의 경우:**
- 샘플이 성공적으로 실행되는지 테스트합니다.
- 오류 처리가 작동하는지 확인합니다.
- Foundry Local과의 호환성을 확인합니다.

### 검토 프로세스

- 교육 콘텐츠 변경은 정확성과 명확성을 검토합니다.
- 코드 샘플은 기능성을 테스트합니다.
- 번역 업데이트는 GitHub Actions에 의해 자동으로 처리됩니다.

## 번역 시스템

**중요:** 이 저장소는 GitHub Actions를 통한 자동 번역을 사용합니다.

- 번역은 `/translations/` 디렉터리에 있습니다 (50개 이상의 언어)
- `co-op-translator.yml` 워크플로를 통해 자동화됩니다.
- **번역 파일을 수동으로 편집하지 마십시오** - 덮어쓰기가 발생합니다.
- 루트 및 모듈 디렉터리의 영어 원본 파일만 편집합니다.
- 번역은 `main` 브랜치로 푸시 시 자동으로 생성됩니다.

## Foundry Local 통합

대부분의 Module08 샘플은 Microsoft Foundry Local 실행이 필요합니다:

### Foundry Local 시작
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Foundry Local 확인
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### 샘플용 환경 변수

대부분의 샘플은 다음 환경 변수를 사용합니다:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## 빌드 및 배포

### 콘텐츠 배포

이 저장소는 주로 문서로 구성되어 있어 콘텐츠에 대한 빌드 프로세스가 필요하지 않습니다.

### 샘플 애플리케이션 빌드

**Electron 애플리케이션 (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python 샘플:**
빌드 프로세스 없음 - Python 인터프리터로 직접 실행됩니다.

## 일반적인 문제 및 문제 해결

### Foundry Local 실행되지 않음
**문제:** 샘플이 연결 오류로 실패함

**해결 방법:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python 가상 환경 문제
**문제:** 모듈 가져오기 오류

**해결 방법:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron 빌드 문제
**문제:** npm 설치 또는 빌드 실패

**해결 방법:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### 번역 워크플로 충돌
**문제:** 번역 PR이 변경 사항과 충돌함

**해결 방법:**
- 영어 원본 파일만 편집합니다.
- 자동 번역 워크플로에 번역을 맡깁니다.
- 충돌이 발생하면 번역이 병합된 후 `main`을 브랜치에 병합합니다.

## 추가 자료

### 학습 경로
- **초급 경로:** 모듈 01-02 (7-9시간)
- **중급 경로:** 모듈 03-04 (9-11시간)
- **고급 경로:** 모듈 05-07 (12-15시간)
- **전문가 경로:** 모듈 08 (8-10시간)

### 주요 모듈 콘텐츠
- **Module01:** EdgeAI 기본 개념 및 실제 사례 연구
- **Module02:** 소형 언어 모델(SLM) 계열 및 아키텍처
- **Module03:** 로컬 및 클라우드 배포 전략
- **Module04:** 다양한 프레임워크를 활용한 모델 최적화
- **Module05:** SLMOps - 운영 환경
- **Module06:** AI 에이전트 및 함수 호출
- **Module07:** 플랫폼별 구현
- **Module08:** Foundry Local 툴킷과 10개의 포괄적인 샘플

### 외부 종속성
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - 로컬 AI 모델 런타임
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - 최적화 프레임워크
- [Microsoft Olive](https://microsoft.github.io/Olive/) - 모델 최적화 툴킷
- [OpenVINO](https://docs.openvino.ai/) - Intel의 최적화 툴킷

## 프로젝트별 참고 사항

### Module08 샘플 애플리케이션

저장소에는 10개의 포괄적인 샘플 애플리케이션이 포함되어 있습니다:

1. **01-REST Chat Quickstart** - 기본 OpenAI SDK 통합
2. **02-OpenAI SDK Integration** - 고급 SDK 기능
3. **03-Model Discovery & Benchmarking** - 모델 비교 도구
4. **04-Chainlit RAG Application** - 검색 증강 생성
5. **05-Multi-Agent Orchestration** - 기본 에이전트 조정
6. **06-Models-as-Tools Router** - 지능형 모델 라우팅
7. **07-Direct API Client** - 저수준 API 통합
8. **08-Windows 11 Chat App** - 네이티브 Electron 데스크톱 애플리케이션
9. **09-Advanced Multi-Agent System** - 복잡한 에이전트 조정
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel 통합

각 샘플은 Foundry Local을 활용한 Edge AI 개발의 다양한 측면을 보여줍니다.

### 성능 고려 사항

- SLM은 엣지 배포를 위해 최적화됨 (2-16GB RAM)
- 로컬 추론은 50-500ms 응답 시간을 제공
- 양자화 기술로 75% 크기 감소와 85% 성능 유지 달성
- 로컬 모델을 활용한 실시간 대화 기능

### 보안 및 개인정보 보호

- 모든 처리는 로컬에서 이루어짐 - 클라우드로 데이터 전송 없음
- 개인정보 보호가 중요한 애플리케이션(의료, 금융)에 적합
- 데이터 주권 요구 사항 충족
- Foundry Local은 완전히 로컬 하드웨어에서 실행됨

---

**이 저장소는 Edge AI 개발을 교육하는 데 중점을 둡니다. 주요 기여 패턴은 교육 콘텐츠를 개선하고 Edge AI 개념을 보여주는 샘플 애플리케이션을 추가/강화하는 것입니다.**

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.