import requests
BASE_URL = "http://localhost:8000"
MODEL = "phi-4-mini"
headers = {"Content-Type": "application/json", "Authorization": "Bearer local-key"}

def chat(messages, max_tokens=300, temperature=0.4):
    r = requests.post(f"{BASE_URL}/v1/chat/completions", json={
        "model": MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }, headers=headers, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

class RetrievalAgent:
    SYSTEM = "You retrieve relevant snippets from knowledge sources based on a query."
    def run(self, query: str) -> str:
        messages = [{"role": "system", "content": self.SYSTEM},
                    {"role": "user", "content": f"Retrieve key facts for: {query}"}]
        return chat(messages)

class ReasoningAgent:
    SYSTEM = "You analyze inputs step by step and produce structured conclusions."
    def run(self, context: str, question: str) -> str:
        messages = [
            {"role": "system", "content": self.SYSTEM},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}\nThink step-by-step and produce a concise answer."}
        ]
        return chat(messages)

class ExecutionAgent:
    SYSTEM = "You transform decisions into actionable steps (JSON with actions)."
    def run(self, decision: str) -> str:
        messages = [
            {"role": "system", "content": self.SYSTEM},
            {"role": "user", "content": f"Turn this decision into 3 executable steps as JSON:\n{decision}"}
        ]
        return chat(messages)
