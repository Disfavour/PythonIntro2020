from math import *


def check(f, g):
    s = [False, False]
    if callable(f):
        s[0] = True
    if callable(g):
        s[1] = True
    return s


def ADD(f, g):
    s = check(f, g)
    if all(s):
        u = lambda x, y: x + y
        return lambda x: u(f(x), g(x))
    elif s[0] and not s[1]:
        u = lambda x: x + g
        return lambda x: u(f(x))
    elif any(s):
        u = lambda x: f + x
        return lambda x: u(g(x))
    else:
        return lambda x: f + g


def SUB(f, g):
    s = check(f, g)
    if all(s):
        u = lambda x, y: x - y
        return lambda x: u(f(x), g(x))
    elif s[0] and not s[1]:
        u = lambda x: x - g
        return lambda x: u(f(x))
    elif any(s):
        u = lambda x: f - x
        return lambda x: u(g(x))
    else:
        return lambda x: f - g


def MUL(f, g):
    s = check(f, g)
    if all(s):
        u = lambda x, y: x * y
        return lambda x: u(f(x), g(x))
    elif s[0] and not s[1]:
        u = lambda x: x * g
        return lambda x: u(f(x))
    elif any(s):
        u = lambda x: f * x
        return lambda x: u(g(x))
    else:
        return lambda x: f * g


def DIV(f, g):
    s = check(f, g)
    if all(s):
        u = lambda x, y: x / y
        return lambda x: u(f(x), g(x))
    elif s[0] and not s[1]:
        u = lambda x: x / g
        return lambda x: u(f(x))
    elif any(s):
        u = lambda x: f / x
        return lambda x: u(g(x))
    else:
        return lambda x: f / g


"""f = SUB(sin, cos)
print(f(12), sin(12)-cos(12))

g = DIV(sin, cos)
print(g(pi/6), tan(pi/6))

h = MUL(exp, 0.1)
print(h(2), e**2/10)

t = ADD(lambda s: len(s), sum)
print(t(range(5)))"""

#print(ADD(20, 22)(100500))
