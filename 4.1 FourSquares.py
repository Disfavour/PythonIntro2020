N = int(input())
for x in range(int(N ** (1 / 2) / 4), int(N ** (1 / 2)) + 1):
    for y in range(int((((N - x * x)) / 3) ** (1 / 2)), x + 1):
        if not (x * x + y * y <= N):
            break
        for z in range(int((((N - x * x - y * y)) / 2) ** (1 / 2)), y + 1):
            if not (x * x + y * y + z * z <= N):
                break
            if N - x * x - y * y - z * z <= z * z:
                t = int((N - x * x - y * y - z * z) ** (1 / 2))
                if x * x + y * y + z * z + t * t == N:
                    print(x, y, z, t, sep=" ")
