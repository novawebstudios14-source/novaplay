"""Regression: a reached dynamic entry beyond declared code windows was lost."""
from pathlib import Path
import importlib.util
import struct
import subprocess
import sys
import tempfile
engine=Path(sys.argv[1]).resolve()
with tempfile.TemporaryDirectory() as d:
    root=Path(d)
    elf=bytearray(84)
    struct.pack_into('<I',elf,28,52)
    struct.pack_into('<HH',elf,42,32,1)
    # A declared window at 0x10000 stops before the reached 0x60010 entry.
    struct.pack_into('<8I',elf,52,1,0,0x10000,0,0,0x4000,5,16)
    ram=bytearray(0x64000)
    struct.pack_into('<4I',ram,0x60010,0x3c030058,0x03e00008,0xa0642a32,0)
    (root/'game.elf').write_bytes(elf)
    (root/'ram.bin').write_bytes(ram)
    (root/'misses').write_text('60010\n')
    subprocess.run([sys.executable,str(engine/'scripts/windows.py'),'capture',str(root/'game.elf'),str(root/'ram.bin'),str(root/'overlays'),str(root/'misses')],check=True)
    token=(root/'misses').read_text().strip()
    stem,offset=token.split(':')
    assert stem.startswith('00060000_') and int(offset,16)==0x10
    blob=(root/'overlays'/(stem+'.bin')).read_bytes()
    assert len(blob)==0x4000 and blob[0x10:0x20]==ram[0x60010:0x60020]
print('Reached overlay entry beyond declared windows captured correctly')
