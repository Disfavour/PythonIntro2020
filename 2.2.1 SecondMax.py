a = int(input())
c = []
while a:
    c.append(a)
    a = int(input())
c.sort()
b = []
for item in c:
    if item not in b:
        b.append(item)
if len(b) > 1:
    print(b[-2])
else:
    print("NO")
