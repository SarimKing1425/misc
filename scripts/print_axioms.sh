#!/usr/bin/env bash
# Print the axioms of the given declarations and fail if any is outside the whitelist
# {propext, Classical.choice, Quot.sound}.  Usage: scripts/print_axioms.sh PvsNP.sanity [More.Decls ...]
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PATH="$HOME/.elan/bin:$PATH"
cd "$ROOT/lean" || exit 1
[ $# -ge 1 ] || { echo "usage: $0 Decl [Decl ...]"; exit 2; }
tmp=".lake/print_axioms_tmp.lean"
{ echo "import PvsNP"; for d in "$@"; do echo "#print axioms $d"; done; } > "$tmp"
out=$(lake env lean "$tmp" 2>&1); status=$?
echo "$out"
[ $status -eq 0 ] || { echo "LEAN ERROR"; exit 1; }
bad=$(echo "$out" | tr ',[]' '\n\n\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' \
  | grep -vE "^$|depends on axioms:|does not depend on any axioms|^(propext|Classical\.choice|Quot\.sound)$" \
  | grep -vE "^'.*'$" || true)
if echo "$out" | grep -q "sorryAx"; then echo "USES sorryAx"; exit 1; fi
if [ -n "$bad" ]; then echo "NON-WHITELISTED AXIOMS:"; echo "$bad"; exit 1; fi
echo "AXIOMS OK"
