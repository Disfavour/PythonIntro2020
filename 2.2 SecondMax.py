a = int(input())
max1 = a
a = int(input())
if a == 0:
    max2 = max1
else:
    max2 = min(max1, a)
    max1 = max(max1, a)
while a:
    if max1 < a:
        max2 = max1
        max1 = a
    elif max1 > a > max2:
        max2 = a
    a = int(input())
if max1 != max2:
    print(max2)
else:
    print("NO")
