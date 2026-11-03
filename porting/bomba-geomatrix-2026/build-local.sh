#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
  echo 'usage: build-local.sh <ps2-web-recomp checkout> <own extracted ISO> [--skip-opening]' >&2
  exit 2
fi
profile=$(cd "$(dirname "$0")" && pwd)
engine=$(realpath "$1")
image=$(realpath "$2")
python3 "$profile/verify-iso.py" "$image"
if git -C "$engine" apply --check "$profile/runtime-fixes.patch"; then
  git -C "$engine" apply "$profile/runtime-fixes.patch"
elif ! git -C "$engine" apply --reverse --check "$profile/runtime-fixes.patch"; then
  echo 'The engine does not match the expected patch state. Use the pinned revision in README.' >&2
  exit 1
fi
cp "$profile/entry-hints.py" "$engine/scripts/novaplay_hints.py"
cp "$profile/observed-entries.txt" "$engine/scripts/observed-entries.txt"
extra=()
if [ "${3:-}" = '--skip-opening' ]; then
  extra=(--pnach "$profile/skip-opening-experimental.pnach")
elif [ -n "${3:-}" ]; then
  echo 'Unknown option' >&2; exit 2
fi
if [ -z "${CXX:-}" ] && [ -x "$engine/tools/emsdk/upstream/bin/clang++" ]; then
  export CXX="$engine/tools/emsdk/upstream/bin/clang++"
fi
cd "$engine"
# Inspect results: a completed compilation or frame limit does not certify gameplay.
bash scripts/port.sh bomba-geomatrix-2026 "$image" --native-only --frames 3600 --rounds 16 "${extra[@]}"
if ! grep -q 'frame limit reached' games/bomba-geomatrix-2026/explore.log; then
  echo 'Runner stopped early. Inspect explore.log; gameplay not certified.' >&2
  exit 1
fi
printf '%s\n' 'Native test reached its frame limit. Inspect frames and controls before building for web.'
