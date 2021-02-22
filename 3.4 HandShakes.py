a = input()
F = []
if a:
    F.append(set(eval(a)))
    a = input()
    while a:
        a = set(eval(a))
        flag = 0

        for item in tuple(F):

            if not item.isdisjoint(a):
                flag += 1

                if flag == 1:
                    item.update(a)
                    tmp = item

                else:
                    tmp.update(item)
                    F.remove(item)

        if flag == 0:
            F.append(a)
        a = input()
    if len(F) == 1:
        print("YES")
    else:
        print("NO")
