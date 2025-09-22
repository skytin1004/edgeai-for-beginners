<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T12:28:17+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "ko"
}
-->
# 세션 6 샘플: 도구로서의 모델

이 샘플은 최소한의 라우터와 도구 레지스트리를 구현하여 사용자 프롬프트에 따라 모델을 선택하고 Foundry Local의 OpenAI 호환 엔드포인트를 호출합니다.

## 파일
- `router.py`: 간단한 레지스트리와 휴리스틱 라우팅; 엔드포인트 검색 및 상태 확인.

## 실행 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## 참고 사항
- 라우터는 간단한 키워드 휴리istics를 사용하여 `general`, `reasoning`, `code` 도구 중에서 선택하며 시작 시 `/v1/models`를 출력합니다.
- 환경 변수를 통해 구성:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-distill-qwen-7b"},"code":{"model":"qwen2.5-7b-instruct"}}
```

## 참고 자료
- Foundry Local (학습): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- 추론 SDK와 통합: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

