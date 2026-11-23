#!/usr/bin/env bash
# Audit the trusted Lean code: build, forbidden-token scan, optional kernel replay.
# Usage: scripts/lean_audit.sh [--replay]
# Exit 0 only if the build succeeds and no forbidden token is found in trusted files
# (everything under lean/PvsNP/ except lean/PvsNP/WIP/, plus lean/PvsNP.lean).
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PATH="$HOME/.elan/bin:$PATH"
cd "$ROOT/lean" || exit 1
fail=0

echo "== lake build =="
lake build 2>&1 | tail -n 60
if [ "${PIPESTATUS[0]}" -ne 0 ]; then echo "BUILD FAILED"; fail=1; fi

echo "== forbidden tokens in trusted files =="
PATTERN='\bsorry\b|\badmit\b|native_decide|ofReduceBool|implemented_by|@\[extern|^[[:space:]]*(private[[:space:]]+|protected[[:space:]]+)?axiom\b|^[[:space:]]*unsafe\b|set_option[[:space:]]+debug|set_option[[:space:]]+(trust|backward)'
hits=$(grep -rnE "$PATTERN" PvsNP.lean PvsNP --include='*.lean' 2>/dev/null | grep -v '^PvsNP/WIP/' || true)
if [ -n "$hits" ]; then echo "$hits"; echo "FORBIDDEN TOKENS FOUND"; fail=1; else echo "none"; fi

echo "== root module must not import WIP =="
if grep -nE '^(public[[:space:]]+)?import[[:space:]]+PvsNP\.WIP' PvsNP.lean PvsNP -r --include='*.lean' | grep -v '^PvsNP/WIP/'; then
  echo "TRUSTED CODE IMPORTS WIP"; fail=1; else echo "ok"; fi

if [ "${1:-}" = "--replay" ]; then
  # Replays each trusted module through the kernel separately (leanchecker on the
  # import-only root module segfaults on v4.36.0; per-module replay works).
  echo "== leanchecker kernel replay, per trusted module =="
  for f in $(find PvsNP -name '*.lean' -not -path 'PvsNP/WIP/*' | sort); do
    m=$(echo "${f%.lean}" | tr '/' '.')
    if lake env leanchecker "$m" >/dev/null 2>&1; then echo "ok  $m"; else echo "FAIL $m"; fail=1; fi
  done
fi

[ $fail -eq 0 ] && echo "AUDIT PASSED" || echo "AUDIT FAILED"
exit $fail
