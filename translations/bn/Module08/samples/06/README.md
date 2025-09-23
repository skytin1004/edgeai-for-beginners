<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T17:47:41+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "bn"
}
-->
# সেশন ৬ উদাহরণ: টুল হিসেবে মডেল

এই উদাহরণটি একটি ন্যূনতম রাউটার + টুল রেজিস্ট্রি বাস্তবায়ন করে যা ব্যবহারকারীর প্রম্পটের উপর ভিত্তি করে একটি মডেল নির্বাচন করে এবং Foundry Local-এর OpenAI-সামঞ্জস্যপূর্ণ এন্ডপয়েন্ট কল করে।

## ফাইলসমূহ
- `router.py`: সহজ রেজিস্ট্রি এবং হিউরিস্টিক রাউটিং; এন্ডপয়েন্ট আবিষ্কার + স্বাস্থ্য পরীক্ষা।

## রান (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## নোটসমূহ
- রাউটারটি `general`, `reasoning`, এবং `code` টুলগুলোর মধ্যে নির্বাচন করতে সহজ কীওয়ার্ড হিউরিস্টিক ব্যবহার করে এবং শুরুতে `/v1/models` প্রিন্ট করে।
- পরিবেশ ভেরিয়েবল ব্যবহার করে কনফিগার করুন:
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

## রেফারেন্সসমূহ
- Foundry Local (শিখুন): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ইনফারেন্স SDK-এর সাথে ইন্টিগ্রেশন: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

