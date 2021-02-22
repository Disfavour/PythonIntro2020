from decimal import *


def f(x):
    return (x ** 2 + y ** 2).sqrt() / v1 + ((1 - x) ** 2 + (1 - y) ** 2).sqrt() / v2


def ternary():
    eps = Decimal("10") ** -(n + 1)
    l, r = Decimal("0"), Decimal("1")
    while r - l > eps:
        x1 = l + (r - l) / 3
        x2 = r - (r - l) / 3
        if f(x1) > f(x2):
            l = x1
        else:
            r = x2

    return l, r


y, v1, v2, n = input().split()
n = int(n)

getcontext().prec = 500
y = Decimal(y)
v1 = Decimal(v1)
v2 = Decimal(v2)

l, r = ternary()
print(str(l)[:2 + n])
