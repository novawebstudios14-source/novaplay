#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 2 ]; then
  echo 'usage: build-local.sh <ps2-web-recomp checkout> <own game ISO or ZIP>' >&2
  exit 2
fi
engine=$(realpath "$1")
image=$(realpath "$2")
[ -f "$image" ] || { echo 'Game image missing' >&2; exit 1; }
cd "$engine"
# No finished build is assumed: inspect every exploration result.
bash scripts/port.sh bomba-geomatrix-2026 "$image" --native-only --frames 3600 --rounds 16
log=games/bomba-geomatrix-2026/explore.log
if ! grep -q 'frame limit reached' "$log"; then
  echo 'Runner stopped before its frame limit. Inspect explore.log; browser build not certified.' >&2
  exit 1
fi
printf '%s\n' 'Native test reached its frame limit. Inspect the frames and controls before building for web.'
