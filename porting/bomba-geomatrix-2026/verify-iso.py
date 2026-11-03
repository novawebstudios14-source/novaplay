#!/usr/bin/env python3
"""Validate the boot executable before applying the edition-specific port patch."""
import hashlib,json,struct,sys
from pathlib import Path
EXPECTED='0236a6970622d0ba7c0f180de523403cc571fbf3f402e9f0d9f8cb77e77c7abd'
def verify(path):
    with path.open('rb') as f:
        f.seek(16*2048);pvd=f.read(2048)
        if len(pvd)!=2048 or pvd[:6]!=b'\x01CD001':raise ValueError('Use an extracted ISO 9660 image')
        sector=struct.unpack_from('<I',pvd,158)[0];size=struct.unpack_from('<I',pvd,166)[0]
        if not 34<=size<=1024*1024 or sector*2048+size>path.stat().st_size:raise ValueError('Invalid root directory')
        f.seek(sector*2048);root=f.read(size);at=0;entry=None
        while at<len(root):
            length=root[at]
            if not length:at=(at//2048+1)*2048;continue
            record=root[at:at+length];at+=length
            if len(record)<34 or 33+record[32]>len(record):raise ValueError('Invalid directory record')
            name=record[33:33+record[32]].split(b';')[0].upper()
            if name==b'BPGE_010.26':entry=struct.unpack_from('<I',record,2)[0],struct.unpack_from('<I',record,10)[0];break
        if not entry:raise ValueError('Expected BPGE_010.26 boot executable not found')
        lba,n=entry
        if not 52<=n<=16*1024*1024 or lba*2048+n>path.stat().st_size:raise ValueError('Invalid executable extent')
        f.seek(lba*2048);boot=f.read(n)
    digest=hashlib.sha256(boot).hexdigest()
    if digest!=EXPECTED:raise ValueError('Different boot executable; the opening patch must not be applied')
    if struct.unpack_from('<I',boot,0x175e38-0xff800)[0]!=0x0c235764:raise ValueError('Opening call does not match the reference')
    return {'boot':'BPGE_010.26','sha256':digest,'isoBytes':path.stat().st_size,'openingCallVerified':True}
if __name__=='__main__':
    try:print(json.dumps(verify(Path(sys.argv[1]))))
    except (ValueError,OSError,IndexError,struct.error) as e:print(str(e),file=sys.stderr);sys.exit(1)
