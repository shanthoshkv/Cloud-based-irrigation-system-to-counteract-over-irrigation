"""Fail if a relative link, src/href, or docs/images/videos path named in a root *.md file does not exist."""
import pathlib, re, sys
from urllib.parse import unquote

REF = re.compile(r'\]\(([^)\s]+)\)|(?:src|href)="([^"]+)"|`((?:docs|images|videos)/[^`]+)`')
bad = []
for md in sorted(pathlib.Path('.').glob('*.md')):
    for m in REF.finditer(md.read_text(encoding='utf-8')):
        ref = next(g for g in m.groups() if g)
        if re.match(r'(https?:|mailto:|#)', ref):
            continue
        path = unquote(ref.split('#')[0])
        if path and not pathlib.Path(path).exists():
            bad.append(f'{md}: missing {path}')
print('\n'.join(bad) or 'all links ok')
sys.exit(1 if bad else 0)
