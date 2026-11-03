"""Extract the original MWo3 code modules, excluding mutable data from hints.

Usage: extract-mwo3.py <verified ISO> <output directory> <entries file>
Commercial bytes remain local. Module text is defined by its own header.
"""
from pathlib import Path
import binascii,json,struct,sys
iso=Path(sys.argv[1]);out=Path(sys.argv[2]);entries=Path(sys.argv[3])
with iso.open('rb') as f:
    f.seek(16*2048);pvd=f.read(2048)
    if pvd[:6]!=b'\x01CD001':raise ValueError('Not ISO9660')
    root_lba=struct.unpack_from('<I',pvd,158)[0];root_size=struct.unpack_from('<I',pvd,166)[0]
    if not 34<=root_size<=1024*1024:raise ValueError('Invalid root')
    f.seek(root_lba*2048);root=f.read(root_size);at=0;extent=None
    while at<len(root):
        n=root[at]
        if not n:at=(at//2048+1)*2048;continue
        r=root[at:at+n];at+=n
        if len(r)<34 or 33+r[32]>len(r):raise ValueError('Invalid record')
        name=r[33:33+r[32]].split(b';')[0].upper()
        if name==b'OVER.AFS':extent=(struct.unpack_from('<I',r,2)[0],struct.unpack_from('<I',r,10)[0]);break
    if not extent:raise ValueError('OVER.AFS not found')
    lba,n=extent
    if not 8<=n<=64*1024*1024 or lba*2048+n>iso.stat().st_size:raise ValueError('Invalid AFS extent')
    f.seek(lba*2048);afs=f.read(n)
if afs[:4]!=b'AFS\0':raise ValueError('Invalid AFS magic')
count=struct.unpack_from('<I',afs,4)[0]
if not 0<count<=4096 or 8+count*8>len(afs):raise ValueError('Invalid AFS table')
out.mkdir(parents=True,exist_ok=True);tokens=[];manifest=[]
for i in range(count):
    off,size=struct.unpack_from('<II',afs,8+i*8)
    if off+size>len(afs) or size<64:raise ValueError('Invalid archive member')
    blob=afs[off:off+size]
    if blob[:4]!=b'MWo3':continue
    base,text,data=struct.unpack_from('<III',blob,8)
    if base>=0x2000000:continue # empty reserved-memory overlay, not EE RAM code
    if size%4 or 64+text>size or base+size>0x2000000:raise ValueError('Invalid module text')
    stem=f'{base:08X}_{binascii.crc32(blob)&0xffffffff:08X}'
    (out/(stem+'.bin')).write_bytes(blob)
    candidates=[]
    for offset in range(64,64+text,4):
        word=struct.unpack_from('<I',blob,offset)[0]
        if word&0xffff8000 in (0x27bd8000,0x67bd8000):candidates.append(offset)
    # Text entry is a candidate even for leaf modules without a stack frame.
    if text:candidates.append(64)
    tokens.extend(f'{stem}:{offset:x}' for offset in sorted(set(candidates)))
    manifest.append({'member':i,'name':stem,'base':hex(base),'textBegin':64,'textBytes':text,'dataBytes':data,'fileBytes':size,'entryHints':len(set(candidates))})
extra=Path(__file__).with_name('mwo3-extra-entries.txt')
if extra.is_file():
    by_name={m['name']:m for m in manifest}
    for token in extra.read_text().split():
        stem,sep,off=token.partition(':')
        if not sep or stem not in by_name:continue
        at=int(off,16);m=by_name[stem]
        if at%4==0 and 64<=at<64+m['textBytes'] and token not in tokens:tokens.append(token)
entries.write_text('\n'.join(tokens)+'\n')
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Extracted',len(manifest),'original MWo3 modules and',len(tokens),'text-only entry hints')
