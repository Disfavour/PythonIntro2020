import math
import sys


a = eval(input())
x, y = eval(input())

norm = []

for x1, y1, r in a:
    norm.append([x1 - x, y1 - y, r])

sp = []

for x, y, r in norm:
    delta = math.asin(r / math.hypot(x, y))
    if x >= 0 and y >= 0:
        if x == 0:
            fi = 0
        else:
            fi = math.atan(y / x)
        """if fi - delta >= 0:
            sp.append([fi + delta, fi - delta])
        else:
            sp.append([fi + delta, math.pi * 2 - (fi - delta)])"""
        sp.append([fi + delta, fi - delta])

    elif x < 0 and y >= 0:
        if y == 0:
            fi = math.pi
        else:
            fi = math.atan(math.fabs(x) / y) + math.pi * 0.5
        sp.append([fi + delta, fi - delta])

    elif x <= 0 and y < 0:
        if x == 0:
            fi == math.pi * 1.5
        else:
            fi = math.atan(math.fabs(y / x)) + math.pi
        sp.append([fi + delta, fi - delta])
    else:
        fi = math.atan(math.fabs(y / x)) + math.pi * 1.5
        """if fi + delta < math.pi * 2:
            sp.append([fi + delta, fi - delta])
        else:
            sp.append([fi + delta - math.pi * 2, fi - delta])"""
        sp.append([fi + delta, fi - delta])

#print(sp)
#print(sorted(sp, key=lambda x: x[0]))
sp1 = sorted(sp, key=lambda x: x[0])
start = sp1[0]
prev_left = start[0]
for left, right in sp1[1:]:
    if right > prev_left:
        print("NO")
        sys.exit()
    prev_left = left

print("YES")



"""for x, y, r in norm:
    midline = math.hypot(x, y)
    th = math.acos(r / midline)
    d = math.atan(math.fabs(y / x))
    d1 = d + th
    d2 = d - th
    if x >= 0 and y >= 0:"""




