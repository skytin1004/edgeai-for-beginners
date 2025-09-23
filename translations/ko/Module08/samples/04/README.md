<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T12:28:30+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "ko"
}
-->
# Session 4 Sample: Chainlit RAG Demo

Foundry Local을 사용하여 최소한의 Chainlit 앱 실행.

## 사전 준비
- Windows 11, Python 3.10+
- Foundry Local 설치 및 사용 가능한 모델 (예: `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## 실행 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## 검증
```cmd
curl http://localhost:8000/v1/models
```

## 문제 해결
- VS Code에서 "chainlit could not be resolved" 메시지가 표시될 경우:
	- 인터프리터를 선택하세요: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- 종속성이 설치되었는지 확인하세요: `pip install -r Module08\requirements.txt`

## 참고 자료
- Open WebUI 사용 방법 (Open WebUI를 사용한 채팅 앱): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (학습): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

