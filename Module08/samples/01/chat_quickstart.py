import os
import sys
import json
import requests

BASE_URL = os.environ.get("FOUNDry_BASE_URL", os.environ.get("BASE_URL", "http://localhost:8000"))
MODEL = os.environ.get("FOUNDry_MODEL", os.environ.get("MODEL", "phi-4-mini"))
API_KEY = os.environ.get("FOUNDry_API_KEY", os.environ.get("API_KEY", ""))

def main():
    prompt = " ".join(sys.argv[1:]) or "Say hello from Foundry Local."
    payload = {"model": MODEL, "messages": [{"role": "user", "content": prompt}], "max_tokens": 128}
    headers = {"Content-Type": "application/json"}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    r = requests.post(f"{BASE_URL}/v1/chat/completions", json=payload, headers=headers, timeout=60)
    r.raise_for_status()
    data = r.json()
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
