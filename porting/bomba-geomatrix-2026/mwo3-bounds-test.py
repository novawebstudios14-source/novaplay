"""An MWo3 module's mutable data must not become translated instructions."""
from pathlib import Path
import re,struct,subprocess,sys,tempfile
recompiler=Path(sys.argv[1]).resolve()
with tempfile.TemporaryDirectory() as d:
    p=Path(d);elf=bytearray(0x108);elf[:7]=b'\x7fELF\x01\x01\x01'
    struct.pack_into('<HHIIIIIHHHHHH',elf,16,2,8,1,0x100000,52,0,0,52,32,1,40,0,0)
    struct.pack_into('<8I',elf,52,1,0x100,0x100000,0,8,8,5,4)
    struct.pack_into('<2I',elf,0x100,0x03e00008,0)
    (p/'game.elf').write_bytes(elf);(p/'overlays').mkdir()
    blob=bytearray(128);blob[:4]=b'MWo3';struct.pack_into('<III',blob,8,0x800000,8,56)
    struct.pack_into('<2I',blob,64,0x03e00008,0)
    # A stack-looking mutable datum must be rejected as an executable entry.
    struct.pack_into('<2I',blob,80,0x27bdfff0,0x03e00008)
    (p/'overlays/00800000_test.bin').write_bytes(blob)
    (p/'entries').write_text('00800000_test:40\n00800000_test:50\n')
    subprocess.run([str(recompiler),str(p/'game.elf'),'--entries',str(p/'entries'),'--overlays',str(p/'overlays'),'--out',str(p/'out')],check=True,capture_output=True)
    table=(p/'out/table.cpp').read_text()
    match=re.search(r'm_00800000_test_checks\[\] = \{([^}]+)\}',table)
    assert match, 'Small valid MWo3 module was dropped'
    values=[int(x,16) for x in re.findall(r'0x([A-Fa-f0-9]+)u',match.group(1))]
    assert values[::2]==[64,68], values
print('MWo3 text bounds exclude mutable data and accept small modules')
