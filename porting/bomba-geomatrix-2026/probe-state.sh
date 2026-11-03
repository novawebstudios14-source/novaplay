#!/usr/bin/env bash
# Resume a known local checkpoint and translate newly reached overlay entries.
set -euo pipefail
if [ "$#" -lt 4 ]; then
  echo 'usage: probe-state.sh <engine> <state> <output-directory> <run-frames> [runner-options...]' >&2
  exit 2
fi
engine=$(realpath "$1"); state=$(realpath "$2")
mkdir -p "$3"; output=$(realpath "$3"); frames=$4; shift 4
cd "$engine"
game=games/bomba-geomatrix-2026
elf=$game/patched/BPGE_010.26
for round in $(seq 1 16); do
  echo "Probe round $round"
  rm -f "$output/misses.txt"
  PS2_PROGRESS=1 PS2_DUMP="$output/ram.bin" timeout 180 \
    build/native-bomba-geomatrix-2026/ps2run "$elf" \
    --disc "$game/disc.iso" --memcard "$game/checkpoint.ps2" \
    --load-state "$state" --run "$frames" --misses "$output/misses.txt" \
    --frames-dir "$output" --frame-every 30 "$@" > "$output/runner.log" 2>&1 || {
      tail -n 12 "$output/runner.log"; exit 1;
    }
  tail -n 1 "$output/runner.log"
  if grep -q 'frame limit reached' "$output/runner.log"; then exit 0; fi
  if [ ! -s "$output/misses.txt" ]; then exit 1; fi
  python3 scripts/windows.py capture "$elf" "$output/ram.bin" "$game/overlays" "$output/misses.txt"
  cat "$output/misses.txt" >> "$game/entries.txt"
  python3 scripts/novaplay_hints.py "$game"
  build/tools/eerecomp "$elf" --entries "$game/entries.txt" --overlays "$game/overlays" \
    --out generated/bomba-geomatrix-2026 > "$output/translation.log"
  PATH=/root/.local/bin:$PATH ninja -C build/native-bomba-geomatrix-2026 ps2run > "$output/build.log" 2>&1
 done
exit 1
