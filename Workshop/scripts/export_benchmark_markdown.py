#!/usr/bin/env python3
"""Export Benchmark Results to Markdown

Runs a lightweight multi-model benchmark (mirrors logic in
`samples/session03/benchmark_oss_models.py`) and writes:
  - A Markdown table (default: benchmark_report.md)
  - A JSON metrics file (benchmark_report.json)

Metrics:
  alias, latency_avg, latency_p95, tokens_per_sec_avg, rounds,
  (optional) first_token_latency_avg (when BENCH_STREAM=1)

Usage:
  python export_benchmark_markdown.py \
      --models "phi-4-mini,qwen2.5-0.5b" \
      --prompt "Explain RAG briefly." \
      --rounds 3 \
      --output benchmark_report.md

Environment Variables:
  BENCH_STREAM=1                    # Measure first token latency (streaming)
  FOUNDRY_LOCAL_ENDPOINT=<url>      # Override service endpoint

SDK Reference:
  https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

Dependencies: foundry-local-sdk, openai, (optional) numpy
"""
from __future__ import annotations

import argparse, os, time, statistics, json, sys
from pathlib import Path
from typing import List, Dict, Any

try:
    import numpy as _np  # optional
except Exception:  # pragma: no cover
    _np = None

# Attempt relative import from samples path if executed from repo root.
try:  # pragma: no cover - import resolution differs by invocation cwd
    from samples.workshop_utils import get_client, chat_once  # type: ignore
except Exception:  # pragma: no cover
    # Fallback: manually append samples directory relative to this script
    import sys as _sys
    from pathlib import Path as _Path
    candidate = _Path(__file__).resolve().parents[1] / "samples"
    if str(candidate) not in _sys.path:
        _sys.path.append(str(candidate))
    try:
        import workshop_utils  # type: ignore
        get_client = workshop_utils.get_client  # type: ignore
        chat_once = workshop_utils.chat_once  # type: ignore
    except Exception as e:  # final failure
        print("ERROR: Unable to import workshop_utils after adjusting PYTHONPATH. Run script from 'Workshop' directory.")
        raise


def benchmark_model(alias: str, prompt: str, rounds: int, measure_stream: bool) -> Dict[str, Any]:
    """Benchmark a single model with warmup and multiple rounds.
    
    Args:
        alias: Model alias to benchmark
        prompt: Test prompt
        rounds: Number of benchmark iterations
        measure_stream: Whether to measure first-token latency
    
    Returns:
        Dictionary with benchmark metrics
    """
    endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
    
    # warm load + warmup round (not timed in summary)
    get_client(alias, endpoint=endpoint)  # ensure loaded
    chat_once(alias, messages=[{"role": "user", "content": prompt}], max_tokens=60, temperature=0.2)

    latencies: List[float] = []
    tps: List[float] = []
    first_token_latencies: List[float] = []

    for _ in range(rounds):
        start = time.time()
        _, usage = chat_once(
            alias,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=120,
            temperature=0.2,
        )
        end = time.time()
        latency = end - start
        latencies.append(latency)
        if usage and getattr(usage, 'total_tokens', None):
            tt = usage.total_tokens
            if tt and latency > 0:
                tps.append(tt / latency)

        if measure_stream:
            # measure first token latency via streaming request
            endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
            _, client, model_id = get_client(alias, endpoint=endpoint)
            t0 = time.time()
            stream = client.chat.completions.create(
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                stream=True,
                max_tokens=40,
                temperature=0.2,
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta and getattr(chunk.choices[0].delta, 'content', None):
                    first_token_latencies.append(time.time() - t0)
                    break

    if _np and len(latencies) > 1:
        p95 = float(_np.percentile(latencies, 95))
    else:
        p95 = statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0]

    result: Dict[str, Any] = {
        "alias": alias,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": p95,
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "rounds": rounds,
    }
    if first_token_latencies:
        result["first_token_latency_avg"] = statistics.mean(first_token_latencies)
    return result


def format_markdown(summary: List[Dict[str, Any]]) -> str:
    headers = ["Model", "Avg Latency (s)", "p95 (s)", "Tokens/sec", "Rounds", "First Token (s)"]
    lines = ["|" + "|".join(headers) + "|", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in summary:
        lines.append(
            "|{alias}|{avg:.2f}|{p95:.2f}|{tps}|{rounds}|{ft}|".format(
                alias=row["alias"],
                avg=row["latency_avg"],
                p95=row["latency_p95"],
                tps=(f"{row['tokens_per_sec_avg']:.1f}" if row.get("tokens_per_sec_avg") else "-") ,
                rounds=row["rounds"],
                ft=(f"{row['first_token_latency_avg']:.2f}" if row.get("first_token_latency_avg") else "-")
            )
        )
    hints = (
        "\n**Interpretation**: Lower latency numbers are better; tokens/sec reflects throughput. "
        "First token latency (if present) approximates perceived responsiveness. Capture baseline before GPU enablement, then re-run for comparison."
    )
    return "\n".join(lines) + "\n" + hints + "\n"


def parse_args(argv: List[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export benchmark results to Markdown & JSON")
    p.add_argument("--models", required=True, help="Comma-separated model aliases")
    p.add_argument("--prompt", required=True, help="Benchmark prompt text")
    p.add_argument("--rounds", type=int, default=3, help="Benchmark rounds per model (default 3)")
    p.add_argument("--output", default="benchmark_report.md", help="Markdown output file path")
    p.add_argument("--json", default="benchmark_report.json", help="JSON output file path")
    p.add_argument("--fail-on-empty", action="store_true", help="Return non-zero exit if no models processed")
    return p.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    models = [m.strip() for m in args.models.split(',') if m.strip()]
    if not models:
        print("No models specified after parsing --models")
        return 1 if args.fail_on_empty else 0
    measure_stream = os.getenv("BENCH_STREAM", "0") == "1"
    summary: List[Dict[str, Any]] = []
    for alias in models:
        try:
            summary.append(benchmark_model(alias, args.prompt, args.rounds, measure_stream))
        except Exception as e:  # pragma: no cover
            print(f"WARN: Benchmark failed for {alias}: {e}")
    if not summary:
        print("No successful benchmark results.")
        return 1 if args.fail_on_empty else 0

    # Write JSON
    Path(args.json).write_text(json.dumps(summary, indent=2), encoding="utf-8")
    # Write Markdown
    md = format_markdown(summary)
    Path(args.output).write_text(md, encoding="utf-8")
    print(f"Wrote {args.output} and {args.json}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
