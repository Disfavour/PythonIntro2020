a, b = input(), input()
if b in a:
    print("YES")
else:
    c = [[] for _ in range(len(b))]
    j = 0
    for i in b:
        tmp = a.find(i)
        while tmp >= 0:
            c[j].append(tmp)
            tmp = a.find(i, tmp + 1)
        j += 1
    d = []
    for i in range(0, len(c) - 1):
        f = []
        for item in c[i]:
            for item2 in c[i + 1]:
                if item2 >= item:
                    f.append(abs(item - item2))
        d.append(f)
    c.clear()
    for item1 in d:
        if item == d[0]:
            continue
        flag = 0
        for item2 in d[0]:
            if item2 in item1:
                flag += 1
        if flag == 0:
            print("NO")
            break

    if flag > 0:
        print("YES")
