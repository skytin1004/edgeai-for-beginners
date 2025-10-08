#!/usr/bin/env python3
"""Validation script for Workshop samples.

This script performs basic validation checks on all Python samples:
- Import validation
- Syntax checking
- Basic linting
- Dependency verification

Usage:
    python validate_samples.py
    python validate_samples.py --session 01
    python validate_samples.py --verbose

Environment Variables:
    SKIP_IMPORT_CHECK=1    # Skip import validation
    SKIP_SYNTAX_CHECK=1    # Skip syntax validation
"""
from __future__ import annotations
import os
import sys
import ast
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple

# Add parent directory to path for imports
WORKSHOP_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(WORKSHOP_ROOT / "samples"))

# Sample files to validate
SAMPLES = {
    "session01": ["chat_bootstrap.py"],
    "session02": ["rag_pipeline.py", "rag_eval_ragas.py"],
    "session03": ["benchmark_oss_models.py"],
    "session04": ["model_compare.py"],
    "session05": ["agents_orchestrator.py"],
    "session06": ["models_router.py", "models_pipeline.py"],
}

# Required imports for each sample
REQUIRED_IMPORTS = {
    "chat_bootstrap.py": ["workshop_utils", "os", "sys"],
    "rag_pipeline.py": ["workshop_utils", "os", "sys", "sentence_transformers", "numpy"],
    "rag_eval_ragas.py": ["workshop_utils", "os", "sys", "sentence_transformers", "ragas", "datasets", "numpy"],
    "benchmark_oss_models.py": ["workshop_utils", "os", "sys", "time", "statistics", "json"],
    "model_compare.py": ["workshop_utils", "os", "sys", "time", "json"],
    "agents_orchestrator.py": ["workshop_utils", "os", "sys", "dataclasses"],
    "models_router.py": ["workshop_utils", "os", "sys", "re"],
    "models_pipeline.py": ["models_router", "workshop_utils", "sys"],
}

# Optional imports (won't cause failures)
OPTIONAL_IMPORTS = [
    "sentence_transformers",
    "ragas",
    "datasets",
    "numpy",
]


class ValidationResult:
    """Results of validation check."""
    
    def __init__(self, sample: str, session: str):
        self.sample = sample
        self.session = session
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.success = True
    
    def add_error(self, msg: str):
        """
        Add an error message to the validation result and mark the validation as failed.

        Parameters:
            msg (str): The error message to add.

        Side Effects:
            Sets self.success to False, indicating that the validation did not pass.
        """
        self.errors.append(msg)
        self.success = False
    
    def add_warning(self, msg: str):
        """Add warning message."""
        self.warnings.append(msg)
    
    def __str__(self) -> str:
        status = "✓ PASS" if self.success else "✗ FAIL"
        lines = [f"{status}: {self.session}/{self.sample}"]
        
        if self.errors:
            lines.append("  Errors:")
            for err in self.errors:
                lines.append(f"    - {err}")
        
        if self.warnings:
            lines.append("  Warnings:")
            for warn in self.warnings:
                lines.append(f"    - {warn}")
        
        return "\n".join(lines)


def check_syntax(filepath: Path) -> Tuple[bool, str]:
    """Check Python syntax.
    
    Args:
        filepath: Path to Python file
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        ast.parse(content)
        return True, ""
    except SyntaxError as e:
        return False, f"Syntax error at line {e.lineno}: {e.msg}"
    except Exception as e:
        return False, f"Parse error: {e}"


def check_imports(filepath: Path, required: List[str], optional: List[str]) -> List[str]:
    """Check if all required imports are present.
    
    Args:
        filepath: Path to Python file
        required: List of required module names
        optional: List of optional module names
    
    Returns:
        List of missing required imports
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        imports = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])
        
        missing = []
        for req in required:
            if req not in imports and req not in optional:
                missing.append(req)
        
        return missing
    except Exception:
        return []


def check_best_practices(filepath: Path) -> List[str]:
    """Check for best practices implementation.
    
    Args:
        filepath: Path to Python file
    
    Returns:
        List of warnings about missing best practices
    """
    warnings = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for error handling
        if 'try:' not in content:
            warnings.append("No try-except blocks found (error handling recommended)")
        
        # Check for type hints
        if 'from typing import' not in content and 'from __future__ import annotations' not in content:
            # Only warn if file has function definitions
            if 'def ' in content:
                warnings.append("No type hints imported (recommended for better IDE support)")
        
        # Check for docstrings
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not ast.get_docstring(node):
                    warnings.append(f"Function '{node.name}' missing docstring")
        
        # Check for SDK reference
        if 'SDK Reference' not in content and 'github.com/microsoft/Foundry-Local' not in content:
            warnings.append("No SDK reference link in docstring")
        
        # Check for environment variable documentation
        if 'Environment' not in content and 'os.getenv' in content:
            warnings.append("Environment variables used but not documented")
    
    except Exception:
        pass
    
    return warnings


def validate_sample(session: str, sample: str, verbose: bool = False) -> ValidationResult:
    """Validate a single sample file.
    
    Args:
        session: Session directory name
        sample: Sample filename
        verbose: Enable verbose output
    
    Returns:
        ValidationResult object
    """
    result = ValidationResult(sample, session)
    filepath = WORKSHOP_ROOT / "samples" / session / sample
    
    if not filepath.exists():
        result.add_error(f"File not found: {filepath}")
        return result
    
    # Check syntax
    if os.getenv("SKIP_SYNTAX_CHECK") != "1":
        is_valid, error = check_syntax(filepath)
        if not is_valid:
            result.add_error(f"Syntax error: {error}")
            return result  # No point continuing if syntax is invalid
    
    # Check imports
    if os.getenv("SKIP_IMPORT_CHECK") != "1":
        required = REQUIRED_IMPORTS.get(sample, [])
        missing = check_imports(filepath, required, OPTIONAL_IMPORTS)
        if missing:
            result.add_error(f"Missing required imports: {', '.join(missing)}")
    
    # Check best practices (warnings only)
    if verbose:
        warnings = check_best_practices(filepath)
        for warning in warnings[:3]:  # Limit to 3 warnings per file
            result.add_warning(warning)
    
    return result


def main():
    """Main validation function."""
    parser = argparse.ArgumentParser(description="Validate Workshop samples")
    parser.add_argument("--session", help="Validate specific session only")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    parser.add_argument("--summary", "-s", action="store_true", help="Show summary only")
    args = parser.parse_args()
    
    print("[INFO] Workshop Sample Validator")
    print(f"[INFO] Workshop root: {WORKSHOP_ROOT}")
    print()
    
    # Filter sessions if specified
    sessions_to_validate = SAMPLES
    if args.session:
        session_key = f"session{args.session.zfill(2)}"
        if session_key in SAMPLES:
            sessions_to_validate = {session_key: SAMPLES[session_key]}
        else:
            print(f"[ERROR] Session '{args.session}' not found")
            sys.exit(1)
    
    # Validate all samples
    results: List[ValidationResult] = []
    for session, samples in sessions_to_validate.items():
        for sample in samples:
            result = validate_sample(session, sample, verbose=args.verbose)
            results.append(result)
            
            if not args.summary:
                print(result)
                print()
    
    # Print summary
    print("=" * 60)
    print("[VALIDATION SUMMARY]")
    print("=" * 60)
    
    total = len(results)
    passed = sum(1 for r in results if r.success)
    failed = total - passed
    
    print(f"Total samples: {total}")
    print(f"Passed: {passed} ✓")
    print(f"Failed: {failed} ✗")
    print()
    
    if failed > 0:
        print("Failed samples:")
        for result in results:
            if not result.success:
                print(f"  - {result.session}/{result.sample}")
                for error in result.errors:
                    print(f"    {error}")
        sys.exit(1)
    else:
        print("[SUCCESS] All samples passed validation!")
        sys.exit(0)


if __name__ == "__main__":
    main()
