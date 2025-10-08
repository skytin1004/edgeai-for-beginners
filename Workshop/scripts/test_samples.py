#!/usr/bin/env python3
"""Quick test runner for Workshop samples.

This script runs a smoke test on all samples to ensure they can initialize
properly and don't have runtime errors during setup.

Usage:
    python test_samples.py
    python test_samples.py --session 01
    python test_samples.py --quick

Environment Variables:
    FOUNDRY_LOCAL_ALIAS=phi-4-mini    # Model to use for testing
    TEST_TIMEOUT=30                   # Timeout per sample in seconds
"""
from __future__ import annotations
import os
import sys
import time
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

WORKSHOP_ROOT = Path(__file__).parent.parent

# Test configurations for each sample
TEST_CONFIGS = {
    "session01": {
        "chat_bootstrap.py": {
            "args": ["Test message"],
            "timeout": 30,
            "required_output": ["INFO", "Using model"],
        }
    },
    "session02": {
        "rag_pipeline.py": {
            "env": {"RAG_QUESTION": "What is RAG?"},
            "timeout": 45,
            "required_output": ["INFO", "RESULT"],
        }
    },
    "session03": {
        "benchmark_oss_models.py": {
            "env": {
                "BENCH_MODELS": "phi-4-mini",
                "BENCH_ROUNDS": "1",
            },
            "timeout": 60,
            "required_output": ["INFO", "Benchmarking"],
        }
    },
    "session04": {
        "model_compare.py": {
            "env": {
                "SLM_ALIAS": "phi-4-mini",
                "LLM_ALIAS": "phi-4-mini",  # Use same for testing
            },
            "timeout": 45,
            "required_output": ["INFO", "Comparing"],
        }
    },
    "session05": {
        "agents_orchestrator.py": {
            "env": {"AGENT_QUESTION": "What is AI?"},
            "timeout": 60,
            "required_output": ["INFO", "Initializing"],
        }
    },
    "session06": {
        "models_router.py": {
            "timeout": 45,
            "required_output": ["INFO", "Testing router"],
        }
    },
}


class TestResult:
    """Test result container."""
    
    def __init__(self, session: str, sample: str):
        self.session = session
        self.sample = sample
        self.success = False
        self.duration = 0.0
        self.error: Optional[str] = None
        self.output: Optional[str] = None
    
    def __str__(self) -> str:
        status = "✓ PASS" if self.success else "✗ FAIL"
        duration = f"({self.duration:.1f}s)"
        result = f"{status} {self.session}/{self.sample} {duration}"
        
        if self.error:
            result += f"\n  Error: {self.error}"
        
        return result


def run_sample_test(
    session: str,
    sample: str,
    config: Dict,
    quick: bool = False
) -> TestResult:
    """Run test for a single sample.
    
    Args:
        session: Session directory name
        sample: Sample filename
        config: Test configuration
        quick: Run in quick mode (shorter timeout)
    
    Returns:
        TestResult object
    """
    result = TestResult(session, sample)
    sample_path = WORKSHOP_ROOT / "samples" / session / sample
    
    if not sample_path.exists():
        result.error = "Sample file not found"
        return result
    
    # Prepare environment
    env = os.environ.copy()
    env.update(config.get("env", {}))
    
    # Set quick mode timeout if specified
    timeout = config.get("timeout", 30)
    if quick:
        timeout = min(timeout, 15)
    
    # Prepare command
    cmd = [sys.executable, str(sample_path)]
    cmd.extend(config.get("args", []))
    
    try:
        start = time.time()
        
        # Run sample
        proc = subprocess.run(
            cmd,
            cwd=sample_path.parent,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        result.duration = time.time() - start
        result.output = proc.stdout + proc.stderr
        
        # Check for required output patterns
        required = config.get("required_output", [])
        for pattern in required:
            if pattern not in result.output:
                result.error = f"Missing expected output: {pattern}"
                return result
        
        # Check exit code
        if proc.returncode != 0:
            # Some samples may fail if dependencies are missing
            if "ERROR" in result.output and "Import" in result.output:
                result.error = "Missing dependencies (expected for some samples)"
            elif "ERROR" in result.output and "Failed to initialize" in result.output:
                result.error = "Foundry Local not running"
            else:
                result.error = f"Non-zero exit code: {proc.returncode}"
            return result
        
        result.success = True
        
    except subprocess.TimeoutExpired:
        result.error = f"Timeout after {timeout}s"
    except Exception as e:
        result.error = f"Execution error: {e}"
    
    return result


def main():
    """Main test runner."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test Workshop samples")
    parser.add_argument("--session", help="Test specific session only")
    parser.add_argument("--quick", "-q", action="store_true", help="Quick mode (shorter timeouts)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show sample output")
    args = parser.parse_args()
    
    print("[INFO] Workshop Sample Test Runner")
    print(f"[INFO] Workshop root: {WORKSHOP_ROOT}")
    
    # Check if Foundry Local is available
    print("[INFO] Checking Foundry Local status...")
    try:
        result = subprocess.run(
            ["foundry", "service", "status"],
            capture_output=True,
            timeout=5
        )
        if result.returncode == 0:
            print("[INFO] ✓ Foundry Local is available")
        else:
            print("[WARN] ⚠ Foundry Local may not be running")
            print("[INFO] Some tests may fail - run: foundry service start")
    except Exception:
        print("[WARN] ⚠ Could not check Foundry Local status")
    
    print()
    
    # Filter sessions
    configs_to_test = TEST_CONFIGS
    if args.session:
        session_key = f"session{args.session.zfill(2)}"
        if session_key in TEST_CONFIGS:
            configs_to_test = {session_key: TEST_CONFIGS[session_key]}
        else:
            print(f"[ERROR] Session '{args.session}' not configured for testing")
            sys.exit(1)
    
    # Run tests
    results: List[TestResult] = []
    for session, samples in configs_to_test.items():
        print(f"[INFO] Testing {session}...")
        
        for sample, config in samples.items():
            print(f"  Running {sample}...", end=" ", flush=True)
            
            result = run_sample_test(session, sample, config, quick=args.quick)
            results.append(result)
            
            if result.success:
                print(f"✓ ({result.duration:.1f}s)")
            else:
                print(f"✗ {result.error}")
            
            if args.verbose and result.output:
                print(f"\n{result.output}\n")
        
        print()
    
    # Print summary
    print("=" * 60)
    print("[TEST SUMMARY]")
    print("=" * 60)
    
    total = len(results)
    passed = sum(1 for r in results if r.success)
    failed = total - passed
    
    print(f"Total tests: {total}")
    print(f"Passed: {passed} ✓")
    print(f"Failed: {failed} ✗")
    
    if failed > 0:
        print("\nFailed tests:")
        for result in results:
            if not result.success:
                print(f"  - {result.session}/{result.sample}")
                print(f"    {result.error}")
    
    print()
    
    if failed > 0:
        print("[INFO] Note: Some failures may be expected if optional dependencies")
        print("[INFO] (like ragas, sentence-transformers) are not installed.")
        print("[INFO] Install all dependencies with: pip install -r Workshop/requirements.txt")
    
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
