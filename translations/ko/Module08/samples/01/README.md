<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T12:27:54+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "ko"
}
-->
# 세션 1 샘플: REST를 통한 간단한 채팅

Python `requests`를 사용하여 Foundry Local에 최소한의 채팅 요청을 실행합니다.

## 사전 준비
- 모델(예: `phi-4-mini`)을 실행 중인 Foundry Local 서비스
- `pip install -r ../../requirements.txt`

## 실행 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## 참고 자료
- Foundry Local (학습): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI 호환 API 개요: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

