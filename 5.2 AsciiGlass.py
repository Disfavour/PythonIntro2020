a = input()
b = []
h0 = -1
jija = 0
while a:
    b.append(a)
    if a.find("#") != -1 and h0 == -1:
        h0 = len(b)
        lens = (a.rfind("#") - a.find("#")) + 1
    if a.count("#") > 2:
        h1 = len(b)
    if a.find("*") != -1 and jija == 0:
        jija = len(b)
    a = input()



vh = len(b)         #высота ведра
vlen = len(b[0])    #длина ведра

h = h1 + 1 - h0     #высота стакана
lens                #длина стакана
if jija != 0:
    jija = (h1 - jija) * (lens - 2)     #колво жижи

    if jija <= vlen:
        jija = 1
    elif jija % vlen == 0:
        jija = jija % vlen
    else:
        jija = (jija // vlen) + 1


art = ["." * vlen for i in range(vh)]

art[vh - 1] = "#" * h + (vlen - h) * "."

art[vh - 1 - lens + 1] = "#" * h + (vlen - h) * "."

for i in range(vh - lens + 1, vh - 1):
    art[i] = "#" + "." * (vlen - 1)

for i in range(len(art) - 1, len(art) - 1 - jija, -1):
    art[i] = "*" * vlen

for i in art:
    print(i)
