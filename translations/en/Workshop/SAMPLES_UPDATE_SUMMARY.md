<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T21:38:34+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "en"
}
-->
# Workshop Samples - Foundry Local SDK Update Summary

## Overview

All Python samples in the `Workshop/samples` directory have been updated to align with Foundry Local SDK best practices and ensure consistency throughout the workshop.

**Date**: October 8, 2025  
**Scope**: 9 Python files across 6 workshop sessions  
**Primary Focus**: Error handling, documentation, SDK patterns, user experience

---

## Updated Files

### Session 01: Getting Started
- ✅ `chat_bootstrap.py` - Basic examples for chat and streaming

### Session 02: RAG Solutions
- ✅ `rag_pipeline.py` - RAG implementation using embeddings
- ✅ `rag_eval_ragas.py` - RAG evaluation with RAGAS metrics

### Session 03: Open Source Models
- ✅ `benchmark_oss_models.py` - Benchmarking multiple models

### Session 04: Cutting Edge Models
- ✅ `model_compare.py` - Comparison between SLM and LLM

### Session 05: AI-Powered Agents
- ✅ `agents_orchestrator.py` - Coordination of multiple agents

### Session 06: Models as Tools
- ✅ `models_router.py` - Model routing based on intent
- ✅ `models_pipeline.py` - Multi-step routed pipeline

### Supporting Infrastructure
- ✅ `workshop_utils.py` - Already adheres to best practices (no changes required)

---

## Key Improvements

### 1. Enhanced Error Handling

**Before:**
```python
manager, client, model_id = get_client(alias)
```
  
**After:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```
  
**Benefits:**
- Graceful error handling with clear error messages
- Actionable troubleshooting tips
- Proper exit codes for scripting

### 2. Better Import Management

**Before:**
```python
from sentence_transformers import SentenceTransformer
```
  
**After:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```
  
**Benefits:**
- Clear guidance for missing dependencies
- Avoids cryptic import errors
- User-friendly installation instructions

### 3. Comprehensive Documentation

**Added to all samples:**
- Documentation for environment variables in docstrings
- SDK reference links
- Usage examples
- Detailed function/parameter descriptions
- Type hints for improved IDE support

**Example:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```
  

### 4. Improved User Feedback

**Added informative logging:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```
  
**Progress indicators:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```
  
**Structured output:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```
  

### 5. Robust Benchmarking

**Session 03 improvements:**
- Per-model error handling (continues execution on failure)
- Detailed progress reporting
- Proper execution of warmup rounds
- Support for first-token latency measurement
- Clear separation of benchmarking stages

### 6. Consistent Type Hints

**Added throughout:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```
  
**Benefits:**
- Improved IDE autocomplete
- Early detection of errors
- Self-documenting code

### 7. Enhanced Model Router

**Session 06 improvements:**
- Detailed documentation for intent detection
- Explanation of model selection algorithm
- Comprehensive routing logs
- Test output formatting
- Error recovery during batch testing

### 8. Multi-Agent Orchestration

**Session 05 improvements:**
- Progress reporting for each stage
- Per-agent error handling
- Clear pipeline structure
- Improved memory management documentation

---

## Testing Checklist

### Prerequisites
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```
  

### Test Each Sample

#### Session 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```
  
#### Session 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```
  
#### Session 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```
  
#### Session 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```
  
#### Session 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```
  
#### Session 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```
  

---

## Environment Variables Reference

### Global (All Samples)
| Variable | Description | Default |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Model alias to use | Varies by sample |
| `FOUNDRY_LOCAL_ENDPOINT` | Override service endpoint | Auto-detected |
| `SHOW_USAGE` | Display token usage | `0` |
| `RETRY_ON_FAIL` | Enable retry logic | `1` |
| `RETRY_BACKOFF` | Initial retry delay | `1.0` |

### Sample-Specific
| Variable | Used By | Description |
|----------|---------|-------------|
| `EMBED_MODEL` | Session 02 | Name of embedding model |
| `RAG_QUESTION` | Session 02 | Test question for RAG |
| `BENCH_MODELS` | Session 03 | Comma-separated list of models to benchmark |
| `BENCH_ROUNDS` | Session 03 | Number of benchmark rounds |
| `BENCH_PROMPT` | Session 03 | Test prompt for benchmarks |
| `BENCH_STREAM` | Session 03 | Measure first-token latency |
| `SLM_ALIAS` | Session 04 | Small language model alias |
| `LLM_ALIAS` | Session 04 | Large language model alias |
| `COMPARE_PROMPT` | Session 04 | Test prompt for comparison |
| `AGENT_MODEL_PRIMARY` | Session 05 | Primary agent model |
| `AGENT_MODEL_EDITOR` | Session 05 | Editor agent model |
| `AGENT_QUESTION` | Session 05 | Test question for agents |
| `PIPELINE_TASK` | Session 06 | Task for pipeline |

---

## Breaking Changes

**None** - All changes are backward compatible.

Existing scripts will continue to function as before. New features include:
- Optional environment variables
- Enhanced error messages (do not disrupt functionality)
- Additional logging (can be suppressed)
- Improved type hints (no runtime impact)

---

## Best Practices Implemented

### 1. Always Use Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```
  
### 2. Proper Error Handling Pattern
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```
  
### 3. Informative Logging
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```
  
### 4. Type Hints
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```
  
### 5. Comprehensive Docstrings
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```
  
### 6. Environment Variable Support
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```
  
### 7. Graceful Degradation
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```
  

---

## Common Issues & Solutions

### Issue: Import Errors  
**Solution:** Install missing dependencies  
```bash
pip install sentence-transformers ragas datasets numpy
```
  

### Issue: Connection Errors  
**Solution:** Ensure Foundry Local is running  
```bash
foundry service status
foundry model run phi-4-mini
```
  

### Issue: Model Not Found  
**Solution:** Check available models  
```bash
foundry model ls
foundry model download <alias>
```
  

### Issue: Slow Performance  
**Solution:** Use smaller models or adjust parameters  
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```
  

---

## Next Steps

### 1. Test All Samples
Follow the testing checklist above to ensure all samples function correctly.

### 2. Update Documentation
- Revise session markdown files with updated examples
- Add a troubleshooting section to the main README
- Create a quick reference guide

### 3. Create Integration Tests
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```
  

### 4. Add Performance Benchmarks
Measure performance improvements resulting from enhanced error handling.

### 5. User Feedback
Gather feedback from workshop participants regarding:
- Clarity of error messages
- Completeness of documentation
- Ease of use

---

## Resources

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Quick Reference**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **Migration Notes**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **Main Repository**: https://github.com/microsoft/Foundry-Local  

---

## Maintenance

### Adding New Samples
When creating new samples, follow these guidelines:
1. Use `workshop_utils` for client management
2. Implement comprehensive error handling
3. Support environment variables
4. Include type hints and docstrings
5. Provide informative logging
6. Add usage examples in docstrings
7. Link to SDK documentation

### Reviewing Updates
When reviewing sample updates, ensure:
- [ ] Error handling is applied to all I/O operations
- [ ] Type hints are added to public functions
- [ ] Docstrings are comprehensive
- [ ] Environment variables are documented
- [ ] User feedback is informative
- [ ] SDK reference links are included
- [ ] Code style is consistent

---

**Summary**: All Workshop Python samples now adhere to Foundry Local SDK best practices, featuring improved error handling, comprehensive documentation, and enhanced user experience. No breaking changes—existing functionality remains intact and is further refined.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations resulting from the use of this translation.