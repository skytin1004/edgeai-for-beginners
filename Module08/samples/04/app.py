import chainlit as cl
import requests

BASE_URL = "http://localhost:8000"
MODEL = "phi-4-mini"

@cl.on_chat_start
async def start():
    await cl.Message(content="Welcome to Local RAG Chat!").send()

@cl.on_message
async def main(message: cl.Message):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": message.content}],
        "max_tokens": 300
    }
    r = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload, timeout=60)
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"]
    await cl.Message(content=content).send()
