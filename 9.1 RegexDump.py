from re import *


def analyze(p, str):
    tmp = p.search(str)
    if tmp:
        print(tmp.start(), ": ", tmp.group(), sep="")

        for number, item in enumerate(tmp.groups()):
            if item:
                print(number + 1, "/", tmp.start(number + 1), ": ", item, sep="")

        for key, value in tmp.groupdict().items():
            if value:
                print(key, "/", tmp.start(key), ": ", value, sep="")
    else:
        print("<NONE>")
    

p = compile(input())

str = input()
while str:
    analyze(p, str)
    str = input()
