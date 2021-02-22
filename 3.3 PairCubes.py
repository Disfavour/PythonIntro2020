n = int(input())
a = n ** (1 / 3)
j = 0
b = n % 9
if n % 9 > 4:
    b = (n % 9) - 9
# print(b)
if abs(b) > 2:
    print("NO")
else:
    flag = 0
    l = []
    m = []
    #print(int(a), a * 2 ** (2/3), int(2 ** (2 / 3) * a) + 1)
    for i in range(int(a), int(2 ** (2 / 3) * a) + 2):
        if n % i == 0:
            flag = 1
            m.append(i)
            #print(flag, "1")
    #print("stage 1 clear", m, "m", flag)
    m1 = []
    for item in m:
        if (item ** 2 - n / item) % 3 == 0:
            l.append(int((item ** 2 - n / item) / 3))
            flag = 2
            #print(flag, "2")
            m1.append(item)
    m.clear()
    #print("stage 2 clear", flag)
    #print(l, "l")
    #print(m1, "m")

    for i in range(len(m1)):
        #print(m1[i] ** 2 - 4 * l[i])
        if (m1[i] ** 2 - 4 * l[i]) ** (1 / 2) % 1 == 0:
            flag += 1
            #print(flag, "3")
    if flag >= 3:
        print("YES")
    else:
        print("NO")

    """for i in range(a):
        for j in range(i):
            if i ** 3 + j ** 3 == n:
                print("YES")
                break
        if i ** 3 + j ** 3 == n:
            break
    if i ** 3 + j ** 3 != n:
        print("NO")
        """
