a, b, c = eval(input())
if a != 0:
    D = (b ** 2 - 4 * a * c)
    if D > 0:
        D = D ** (1/2)
        x1 = (-b + D) / (2 * a)
        x2 = (-b - D) / (2 * a)
        print(min(x1, x2), max(x1, x2))
    elif D == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print(0)
elif b != 0:
    x = c / b
    print(x)
elif b == 0:
    print(-1)
