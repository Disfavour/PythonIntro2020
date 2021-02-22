from decimal import *
from decimal import localcontext

a = input()
b = int(input())
getcontext().prec = b + 5

def f(a):
    return lambda x: eval(a)


def find(g, c, d):
    p = (c + d) / Decimal("2")
    #print(c, d, p, round(c, b), round(d, b), round(c, b) == round(d, b))
    """with localcontext() as ctx:
        ctx.prec = b
        print(c, d)"""
    if Decimal(g(p)) == Decimal("0") or round(c, b) == round(d, b):
        return p

    elif Decimal(str(g(c))) < 0 and Decimal(str(g(d))) > 0:
        if Decimal(g(p)) > 0:
            return find(g, c, p)
        elif Decimal(g(p)) < 0:
            return find(g, p, d)
    elif Decimal(str(g(c))) > 0 and Decimal(str(g(d))) < 0:
        if Decimal(g(p)) > 0:
            return find(g, p, d)
        elif Decimal(g(p)) < 0:
            return find(g, c, p)



g = f(a)
c = Decimal("-1.5")
d = Decimal("1.5")
t = Decimal(str(find(g, c, d)))
#print(t, type(t))
#print(round(t, b))

with localcontext() as ctx:
    ctx.prec = b
    print(f'{t:.{b}f}')
