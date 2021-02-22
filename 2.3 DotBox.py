from math import *
x, y, z = eval(input())
try:
    x1, y1, z1 = eval(input())
except SyntaxError:
    print(0)
else:
    xmin = min(x, x1)
    xmax = max(x, x1)
    ymin = min(y, y1)
    ymax = max(y, y1)
    zmin = min(z, z1)
    zmax = max(z, z1)
    while True:
        try:
            x, y, z = eval(input())
        except SyntaxError:
            break

        if xmax < x:
            xmax = x
        elif xmin > x:
            xmin = x

        if ymax < y:
            ymax = y
        elif ymin > y:
            ymin = y

        if zmax < z:
            zmax = z
        elif zmin > z:
            zmin = z
    if xmax == xmin or ymax == ymin or zmax == zmin:
        print(0)
    else:
        V = (fabs(xmax) + fabs(xmin)) * (fabs(ymax) + fabs(ymin))* (fabs(zmax) + fabs(zmin))
        print(V)
