import os
from openai import OpenAI

# Mode selection:
# - Foundry Local (default): uses BASE_URL and API_KEY
# - Azure OpenAI: set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY (and optionally, API version)

azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
azure_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
azure_api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")

if azure_endpoint and azure_api_key:
    # Azure OpenAI path
    # MODEL should be the Azure deployment name
    model = os.environ.get("MODEL", "your-deployment-name")
    client = OpenAI(
        base_url=f"{azure_endpoint}/openai",
        api_key=azure_api_key,
        default_query={"api-version": azure_api_version},
    )
else:
    # Foundry Local / OpenAI-compatible path
    base_url = os.environ.get("BASE_URL", "http://localhost:8000")
    model = os.environ.get("MODEL", "phi-4-mini")
    api_key = os.environ.get("API_KEY", "")
    client = OpenAI(base_url=f"{base_url}/v1", api_key=api_key)

resp = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Say hello from the SDK quickstart."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
