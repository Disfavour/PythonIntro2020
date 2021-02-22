import re
import sys


start = re.compile(r"^ПРОЦ")
end = re.compile(r"\sКНЦ;$")

def analyze(ans):
    #print(ans)
    #print(start.match(ans), end.search(ans))
    if start.match(ans) and end.search(ans):
        return ans
    else:
        return False

a = input().strip().split()
b = bytes.fromhex(input())

alphabet = "ПABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНЕОРСТУФХЦЧШЩЫЭЮЯ()[]+-*/%;.,>=<\"!:"
d1 = {}
alp = alphabet.encode("koi8-r")

for item1 in a:
    for item2 in a:
        if item1 != item2:
            try:
                tmp = alp.decode(item1).encode(item2)
            except UnicodeDecodeError:
                pass
            except UnicodeEncodeError:
                pass
            else:
                d1[tmp] = [item1, item2]
                #print(d1[tmp])




for stroka in d1:
    if stroka[:1] == b[:1]:
        decoder = d1[stroka]
        #decoder.reverse()
        try:
            tmp = b.decode(decoder[1]).encode(decoder[0]).decode("koi8-r")
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass
        else:
            tmp = analyze(tmp)
            if tmp:
                print(tmp)
                sys.exit()

d2 = {}

for stroka in tuple(d1):
    for item1 in a:
        for item2 in a:
            if item1 != item2:
                try:
                    tmp = stroka.decode(item1).encode(item2)
                except UnicodeDecodeError:
                    pass
                except UnicodeEncodeError:
                    pass
                else:
                    if item1 != d1[stroka][-1]:
                        d2[tmp] = d1[stroka] + [item1, item2]
                    #print(d2[tmp])

for stroka in d2:
    if stroka[:1] == b[:1]:
        decoder = d2[stroka]
        #decoder.reverse()
        try:
            tmp = b.decode(decoder[3]).encode(decoder[2]).decode(decoder[1]).encode(decoder[0]).decode("koi8-r")
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass
        else:
            tmp = analyze(tmp)
            if tmp:
                print(tmp)
                sys.exit()

d3 = {}

for stroka in tuple(d2):
    for item1 in a:
        for item2 in a:
            if item1 != item2:
                try:
                    tmp = stroka.decode(item1).encode(item2)
                except UnicodeDecodeError:
                    pass
                except UnicodeEncodeError:
                    pass
                else:
                    if item1 != d2[stroka][-1]:
                        d3[tmp] = d2[stroka] + [item1, item2]
                    #print(d3[tmp])


for stroka in d3:
    if stroka[:1] == b[:1]:
        decoder = d3[stroka]
        #decoder.reverse()
        try:
            tmp = b.decode(decoder[5]).encode(decoder[4]).decode(decoder[3]).encode(decoder[2]).decode(decoder[1]).encode(decoder[0]).decode("koi8-r")
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass
        else:
            tmp = analyze(tmp)
            if tmp:
                print(tmp)
                sys.exit()

d4 = {}

for stroka in tuple(d3):
    for item1 in a:
        for item2 in a:
            if item1 != item2:
                try:
                    tmp = stroka.decode(item1).encode(item2)
                except UnicodeDecodeError:
                    pass
                except UnicodeEncodeError:
                    pass
                else:
                    if item1 != d3[stroka][-1]:
                        d4[tmp] = d3[stroka] + [item1, item2]
                    #print(d4[tmp])


for stroka in d4:
    if stroka[:1] == b[:1]:
        decoder = d4[stroka]
        #decoder.reverse()
        try:
            tmp = b.decode(decoder[7]).encode(decoder[6]).decode(decoder[5]).encode(decoder[4]).decode(decoder[3]).encode(decoder[2]).decode(decoder[1]).encode(decoder[0]).decode("koi8-r")
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass
        else:
            tmp = analyze(tmp)
            if tmp:
                print(tmp)
                sys.exit()
