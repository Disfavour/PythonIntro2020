import sys
import io
import zipfile
import re

ans = [0, 0]

find = re.compile(r"\sfile_size=(\d+)")

data = sys.stdin.read()
data = bytes.fromhex(data)

with io.BytesIO(data) as f:
    f = zipfile.ZipFile(f)
    #print(f.infolist())
    s = f.infolist()

for i in s:
    tmp = str(i)
    tmp = find.search(tmp)
    if tmp:
        ans[0] += 1
        ans[1] += int(tmp.group(1))

print(*ans)
