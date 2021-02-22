import random
def randsquare(A, B):
    a = []
    d = ((abs(A[0] - B[0]) ** 2 + abs(A[1] - B[1]) ** 2) ** (1 / 2))
    a = (d ** 2 / 2) ** (1 / 2)
    ca = abs(A[0] - B[0]) / d
    sa = abs(A[1] - B[1]) / d
    if B[0] < A[0]:
        ca = - ca
    if B[1] < A[1]:
        sa = -sa
    x = random.uniform(0, a)
    y = random.uniform(0, a)

    q = 1 / (2 ** (1/2))
    x1 = x * q + y * q
    y1 = - x * q + y * q

    x3 = x1 * ca - y1 * sa + A[0]
    y3 = + x1 * sa + y1 * ca + A[1]
    return (x3, y3)
