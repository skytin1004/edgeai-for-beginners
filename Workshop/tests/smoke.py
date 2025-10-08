"""Workshop smoke tests.

Run a minimal end-to-end invocation for key samples to ensure they start and return text.
Intentionally lightweight: avoids large models if aliases overridden via env.

Usage:
  python -m Workshop.tests.smoke

Environment Variables:
  FOUNDRY_LOCAL_ALIAS=phi-4-mini     # Default model alias
  BENCH_MODELS=phi-4-mini            # Models for benchmark tests
  FOUNDRY_LOCAL_ENDPOINT=<url>       # Override service endpoint

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

Requirements:
  - Foundry Local service must be running
  - At least one model loaded (e.g., phi-4-mini)
"""
from __future__ import annotations
import importlib, json, os, sys, traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "samples"
sys.path.append(str(SAMPLES))

# Basic test cases: (module_path, callable_or_None, description)
CASES = [
    ("session01.chat_bootstrap", None, "Bootstrap + chat"),
    ("session02.rag_pipeline", "answer", "RAG answer"),
    ("session06.models_router", "route", "Routing call"),
]

def run_case(mod_name: str, attr: str | None):
    """Run a single test case for a workshop sample.
    
    Args:
        mod_name: Module name to import
        attr: Attribute/function to call (None for module load only)
    
    Returns:
        Test result output
    """
    m = importlib.import_module(f"samples.{mod_name}") if not mod_name.startswith("samples.") else importlib.import_module(mod_name)
    
    if attr:
        if attr == "answer":
            out = getattr(m, attr)("Why use RAG with local inference?")
        elif attr == "route":
            out = getattr(m, attr)("Summarize local inference benefits")
        else:
            out = getattr(m, attr)()
        return out
    else:
        # If script pattern, emulate minimal call by reusing its variables if present
        return {"module_loaded": True, "module": mod_name}

results = []
for mod, attr, desc in CASES:
    try:
        r = run_case(mod, attr)
        results.append({"case": desc, "module": mod, "status": "ok", "sample": str(r)[:120]})
    except Exception as e:  # noqa: BLE001
        traceback.print_exc()
        results.append({"case": desc, "module": mod, "status": "error", "error": str(e)})

print(json.dumps(results, indent=2))
