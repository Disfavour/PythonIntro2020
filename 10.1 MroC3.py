from re import *

g = " pass\n"
lines = []
t = compile(r"(class\s[^():]+(?:\(.+\))?:)")


def analyze(f):
    if t.search(f):
        lines.append("".join(t.split(f)[:-1]) + g)


f = 0
a = input()
while a:
    analyze(a)
    a = input()

lines = "".join(lines)

try:
    exec(lines)
except TypeError:
    print("No")
    f = 1
except:
    pass
else:
    print("Yes")
    f = 1
finally:
    if f == 0:
        print("Yes")
