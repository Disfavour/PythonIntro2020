a = input()
b = []
d = []
while a:
    f = a.split()
    if len(f) == 4:
        c = f[:4]
    else:
        c = f[:2]
        c.append(" ".join(f[2:-1]))
        c.append(f[-1])
    k = f[-1].split(":")
    c.append(int(k[0]) * 3600 + int(k[1]) * 60 + int(k[2]))
    b.append(c)
    a = input()
b.sort(key=lambda x: x[4])

#print(b)

last = b[0]
d = [[]]
d[0].append(b[0])

i = 0
for item in b[1:]:
    if item[4] == last[4]:
        d[i].append(item)
    else:
        i += 1
        d.append([])
        d[i].append(item)
    if len(d) > 3:
        break
    last = item
d = d[:3]

for item in d:
    item.sort(key=lambda x: x[1])

#print(d)

len0 = len(d[0][0][0])
len1 = len(d[0][0][1])
len2 = len(d[0][0][2])
len3 = len(d[0][0][3])
for item1 in d:
    for item2 in item1:
        if len0 < len(item2[0]):
            len0 = len(item2[0])
        if len1 < len(item2[1]):
            len1 = len(item2[1])
        if len2 < len(item2[2]):
            len2 = len(item2[2])
        if len3 < len(item2[3]):
            len3 = len(item2[3])

template = "{0} {1} {2} {3}"


for i in d:
    for j in i:
        #print("{:<len0} {:<len1} {:<len2} {:<len3}".format(*j))
        print("{:<{width[0]}} {:<{width[1]}} {:<{width[2]}} {:<{width[3]}}".format(*j, width=[len0, len1, len2, len3]))
