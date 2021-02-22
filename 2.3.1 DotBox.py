from math import *
c = tuple()
while True:
    try:
        a = eval(input())
    except SyntaxError:
        break
    c += a
c = list(c)
x, y, z = [], [], []
for x1 in c[::3]:
    x.append(x1)
for y1 in c[1::3]:
    y.append(y1)
for z1 in c[2::3]:
    z.append(z1)
if min(x) == max(x) or min(y) == max(y) or min(z) == max(z):
    print(0)
else:
    V = (fabs(min(x))+fabs(max(x))) * (fabs(min(y))+fabs(max(y))) * (fabs(min(z))+fabs(max(z)))
    print(V)
