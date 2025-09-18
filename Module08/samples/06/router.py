import os
import sys
import json
import requests
from typing import Dict, Any
from pathlib import Path

# Ensure Module08 utils are importable when running as a script
MODULE08_DIR = Path(__file__).resolve().parents[2]
if str(MODULE08_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE08_DIR))

try:
    from utils.smoke_test import discover_base_url, check_foundry
except Exception:
    # Fallbacks if utils are unavailable
    def discover_base_url(default: str = "http://localhost:8000") -> str:
        return os.environ.get("BASE_URL", default)

    def check_foundry(base_url: str) -> dict:
        r = requests.get(f"{base_url}/v1/models", timeout=5)
        r.raise_for_status()
        return r.json()

BASE_URL = discover_base_url("http://localhost:8000")
API_KEY = os.environ.get("API_KEY", "")
HEADERS = {"Content-Type": "application/json"}
if API_KEY:
    HEADERS["Authorization"] = f"Bearer {API_KEY}"

# Tool registry mapping task -> model (env-overridable)
DEFAULT_TOOLS: Dict[str, Dict[str, Any]] = {
    "general": {"model": os.environ.get("GENERAL_MODEL", "phi-4-mini"), "notes": "default fast chat"},
    "reasoning": {"model": os.environ.get("REASONING_MODEL", "deepseek-r1-distill-qwen-7b"), "notes": "use for step-by-step tasks"},
    "code": {"model": os.environ.get("CODE_MODEL", "qwen2.5-7b-instruct"), "notes": "use for code-related requests"},
}

TOOLS_ENV = os.environ.get("TOOL_REGISTRY")
if TOOLS_ENV:
    try:
        TOOLS: Dict[str, Dict[str, Any]] = json.loads(TOOLS_ENV)
    except Exception:
        TOOLS = DEFAULT_TOOLS
else:
    TOOLS = DEFAULT_TOOLS


def select_tool(user_query: str) -> str:
    q = user_query.lower()
    if any(k in q for k in ["why", "how", "explain", "step-by-step", "reason"]):
        return "reasoning"
    if any(k in q for k in ["code", "python", "function", "class", "bug"]):
        return "code"
    return "general"


def chat(model: str, content: str, max_tokens: int = 256) -> str:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "max_tokens": max_tokens,
    }
    r = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload, headers=HEADERS, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def route_and_run(prompt: str) -> Dict[str, Any]:
    tool_key = select_tool(prompt)
    tool = TOOLS[tool_key]
    model = tool["model"]
    answer = chat(model, prompt)
    return {"tool": tool_key, "model": model, "answer": answer}


if __name__ == "__main__":
    import sys
    # Basic availability check for Foundry Local
    try:
        models_info = check_foundry(BASE_URL)
        available_models = [m.get("id") for m in models_info.get("data", [])]
        print({"base_url": BASE_URL, "available_models": available_models})
    except Exception as e:
        print(f"Warning: Could not reach Foundry Local at {BASE_URL} ({e}). Proceeding anyway...")

    user_prompt = " ".join(sys.argv[1:]) or "Write three JSON bullets of benefits of on-device AI."
    result = route_and_run(user_prompt)
    print(result)
