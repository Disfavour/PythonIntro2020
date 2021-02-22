from decimal import *


def factorial(n):
    sum = 1
    for i in range(2, n + 1):
        sum *= i
    return sum


getcontext().prec = 10000


def PiGen():
    z = 426880 * Decimal("10005").sqrt()
    k = 0
    sum = 0
    while True:
        a = Decimal(str(factorial(6 * k) * (545140134 * k + 13591409)))
        b = Decimal(str(factorial(3 * k) * factorial(k) ** 3 * (-262537412640768000) ** k))
        sum += a / b
        yield z /sum
        k += 1
