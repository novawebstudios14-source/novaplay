"""Capture an explicitly reached, contiguous EE code region for local analysis.

Usage: capture-region.py <RAM dump> <game directory> <base hex> <end hex> <reached PC hex>
The output contains game bytes and must remain local.
"""
from pathlib import Path
import binascii
import sys
if len(sys.argv)!=6:
    raise SystemExit(__doc__)
ram=Path(sys.argv[1]).read_bytes();game=Path(sys.argv[2])
base,end,pc=(int(v,16) for v in sys.argv[3:])
if base%0x4000 or end%0x4000 or pc%4 or not 0<=base<=pc<end<=min(len(ram),0x2000000):
    raise SystemExit('Invalid aligned EE region or entry')
blob=ram[base:end]
if not any(blob[pc-base:pc-base+64]):
    raise SystemExit('No loaded instructions at reached entry')
stem=f'{base:08X}_{binascii.crc32(blob)&0xffffffff:08X}'
out=game/'overlays';out.mkdir(parents=True,exist_ok=True)
(out/(stem+'.bin')).write_bytes(blob)
token=f'{stem}:{pc-base:x}'
entries=game/'entries.txt'
known=set(entries.read_text().split()) if entries.exists() else set()
if token not in known:
    with entries.open('a') as f:f.write(token+'\n')
print('Captured',len(blob),'bytes as',stem,'with reached entry',token)
