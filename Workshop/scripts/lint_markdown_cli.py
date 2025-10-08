#!/usr/bin/env python3
"""Markdown CLI Pattern Linter

Purpose:
  Prevent reintroduction of deprecated / unsupported Foundry Local CLI patterns
  in workshop markdown documentation. Fails with non‑zero exit code when any
  disallowed command appears inside a fenced code block.

Checked Scope:
  - All .md files under the repo (default root is two levels up from this script)
  - Only lines within fenced code blocks (``` ... ```). This allows explanatory
    prose mentioning removed commands for historical context.

Deprecated Patterns & Replacements:
  foundry model chat <model>            => foundry model run <model> --prompt "..."
  foundry model list --running          => foundry model list
  foundry model list --cached           => foundry cache list
  foundry model stats                   => (benchmark script + system tools)
  foundry model benchmark               => (benchmark script samples/session03/benchmark_oss_models.py)
  foundry model list --available        => foundry model list

Exit Codes:
  0 = success (no deprecated patterns in code fences)
  1 = deprecated pattern(s) found

Usage:
  python Workshop/scripts/lint_markdown_cli.py            # run from repo root or any directory
  python Workshop/scripts/lint_markdown_cli.py --verbose  # show all scanned files

Add to a pre-commit hook (optional):
  echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
  chmod +x .git/hooks/pre-commit

SDK Reference:
  https://github.com/microsoft/Foundry-Local (official CLI and SDK documentation)

Author: Automated assistant
"""
from __future__ import annotations

import sys
import re
from pathlib import Path
from typing import List, Pattern

DEPRECATED: List[tuple[str, str]] = [
    (r"\bfoundry\s+model\s+chat\b", "Use 'foundry model run <alias> --prompt'"),
    (r"\bfoundry\s+model\s+list\s+--running\b", "Use plain 'foundry model list'"),
    (r"\bfoundry\s+model\s+list\s+--cached\b", "Use 'foundry cache list'"),
    (r"\bfoundry\s+model\s+stats\b", "Use benchmark script + system tools"),
    (r"\bfoundry\s+model\s+benchmark\b", "Use 'samples/session03/benchmark_oss_models.py'"),
    (r"\bfoundry\s+model\s+list\s+--available\b", "Use plain 'foundry model list'"),
]

COMPILED: List[tuple[Pattern[str], str]] = [
    (re.compile(pat, re.IGNORECASE), repl) for pat, repl in DEPRECATED
]

FENCE_PATTERN = re.compile(r"^```")

def scan_markdown(path: Path) -> List[str]:
    """Return list of violation messages for a given markdown file."""
    violations: List[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:  # pragma: no cover
        violations.append(f"ERROR reading {path}: {e}")
        return violations

    in_fence = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        if FENCE_PATTERN.match(line.strip()):
            in_fence = not in_fence
            continue
        if not in_fence:
            continue  # Only enforce inside code fences
        # Skip commented lines in code blocks that explicitly mark legacy examples
        if line.strip().startswith(('#', '//')) and 'legacy' in line.lower():
            continue
        for regex, suggestion in COMPILED:
            if regex.search(line):
                snippet = line.strip()
                if len(snippet) > 160:
                    snippet = snippet[:157] + '...'
                violations.append(
                    f"{path}:{lineno}: Deprecated CLI pattern -> '{snippet}' | Suggestion: {suggestion}"
                )
    return violations

def main(argv: List[str]) -> int:
    verbose = '--verbose' in argv
    # Determine repo root: assume script is at Workshop/scripts/...
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[1] if (len(script_path.parents) >= 2) else Path.cwd()
    md_files = sorted(repo_root.rglob("*.md"))
    if verbose:
        print(f"Scanning {len(md_files)} markdown files from root: {repo_root}")
    all_violations: List[str] = []
    for md in md_files:
        # Skip translation directories to avoid noise
        if 'translations' in md.parts:
            continue
        all_violations.extend(scan_markdown(md))

    if all_violations:
        print("Found deprecated CLI patterns:\n")
        for v in all_violations:
            print(v)
        print(f"\nTotal violations: {len(all_violations)}")
        return 1
    else:
        if verbose:
            print("No deprecated CLI patterns detected.")
        return 0

if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
