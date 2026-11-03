#!/usr/bin/env python3
"""Add stack-frame entry hints only to overlay images reached by the game.

These are analysis candidates, not proof that an address is executable. The
runtime must still match the overlay image before dispatching translated code.
"""
from pathlib import Path
import struct
import sys

def add_hints(game):
    path = game / 'entries.txt'
    known = set(path.read_text().split()) if path.exists() else set()
    added = []
    # Observed entry points from the earlier run of this exact edition.
    observed = {
        '008C8000_C15730A9': [0x4320],
        '00904000_23D0E535': [0x80],
        '005F8000_C4A90F00': [0x223e0, 0x227b8],
        '008C8000_249D4946': [0xdc70],
    }
    for stem, offsets in observed.items():
        if not (game / 'overlays' / (stem + '.bin')).is_file():
            continue
        for offset in offsets:
            token = f'{stem}:{offset:x}'
            if token not in known:
                known.add(token)
                added.append(token)
    checkpoint = Path(__file__).with_name('observed-entries.txt')
    if checkpoint.is_file():
        for token in checkpoint.read_text().split():
            stem, separator, offset = token.partition(':')
            if not separator or '/' in stem or '\\' in stem:
                continue
            source = game / 'overlays' / (stem + '.bin')
            if source.is_file() and 0 <= int(offset, 16) < source.stat().st_size and token not in known:
                known.add(token)
                added.append(token)
    stems = {token.split(':', 1)[0] for token in known if ':' in token}
    for stem in sorted(stems):
        if '/' in stem or '\\' in stem:
            raise ValueError('Overlay identifier must be a filename stem')
        source = game / 'overlays' / (stem + '.bin')
        if not source.is_file():
            continue
        data = source.read_bytes()
        for offset in range(0, len(data) - 3, 4):
            word = struct.unpack_from('<I', data, offset)[0]
            if word & 0xffff8000 in (0x27bd8000, 0x67bd8000):
                token = f'{stem}:{offset:x}'
                if token not in known:
                    known.add(token)
                    added.append(token)
    if added:
        with path.open('a') as stream:
            stream.write(''.join(token + '\n' for token in added))
    return len(added)

if __name__ == '__main__':
    print('NovaPlay: added', add_hints(Path(sys.argv[1])), 'overlay entry hints')
