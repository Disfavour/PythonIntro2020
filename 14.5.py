from fractions import Fraction
import re


def to_dict(stroka):
    d = {}
    for item in finder.findall(stroka):
        if "x" not in item:
            d[0] = Fraction(item)
        elif item[-1] == "x":
            item = item[:-1]
            if number.search(item):
                d[1] = Fraction(item)
            else:
                d[1] = Fraction(item + "1")
        else:
            n, s = item.split("x")
            str = ""
            for j in s:
                str += from_hz[j]
            if number.search(n):
                d[int(str)] = Fraction(n)
            else:
                d[int(str)] = Fraction(n + "1")
    return d


def plus(d1, d2):
    d = {}
    dlina = max(max(d1), max(d2))
    for i in range(dlina + 1):
        if i in d1 and i in d2:
            d[i] = d1[i] + d2[i]
        elif i in d1:
            d[i] = d1[i]
        elif i in d2:
            d[i] = d2[i]
    return d


def minus(d1, d2):
    d = {}
    dlina = max(max(d1), max(d2))
    for i in range(dlina + 1):
        if i in d1 and i in d2:
            if d1[i] - d2[i] != 0:
                d[i] = d1[i] - d2[i]
            else:
                pass
        elif i in d1:
            d[i] = d1[i]
        elif i in d2:
            d[i] = -d2[i]
    return d


def mul(d1, d2):
    d = {}
    dlina = max(max(d1), max(d2))
    for i in range(dlina + 1):
        if i not in d1:
            continue
        for j in range(dlina + 1):
            if j in d2:
                if i + j in d:
                    d[i + j] += d1[i] * d2[j]
                else:
                    d[i + j] = d1[i] * d2[j]
    return d


def del1(d1, d2):

    """dlina = abs(max(d1) - max(d2))
    l1 = []
    l2 = []
    l3 = [0 for i in range(dlina)]"""

    d3 = {}
    """for i in range(max(d1)):
        if i in d1:
            l1.append(d1[i])
        else:
            l1.append(0)
    for i in range(max(d2)):
        if i in d2:
            l2.append(d2[i])
        else:
            l2.append(0)"""

    while len(d1) > 0 and max(d1) >= max(d2):
        d3[max(d1) - max(d2)] = d1[max(d1)] / d2[max(d2)]
        d1 = minus(d1, mul(d2, {max(d1) - max(d2): d1[max(d1)] / d2[max(d2)]}))

    return d1, d3






def draw(d):
    tmp = reversed(sorted([i for i in d]))
    answer = ""
    for i in tmp:
        if i == 0:
            if d[i] < 0:
                answer += str(d[i])
            else:
                answer += "+" + str(d[i])
        elif i == 1:
            if d[i] < 0:
                answer += str(d[i]) + "x"
            else:
                answer += "+" + str(d[i]) + "x"
        else:
            st2 = ""
            for j in str(i):
                st2 += to_hz[j]
            if d[i] < 0:
                answer += str(d[i]) + "x" + st2
            else:
                answer += "+" + str(d[i]) + "x" + st2

    answer = edinica.sub(r"\1\3", answer)
    if answer.startswith("+"):
        answer = answer[1:]
    if answer == "":
        print(0)
    else:
        print(answer)





a = [input() for i in range(3)]
to_hz = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"}
from_hz = {unnormal: normal for normal, unnormal in to_hz.items()}

edinica = re.compile(r"([+-]?)(1)(x)")
finder = re.compile(r"([+-]?[0123456789/]*x(?:[²³⁴⁵⁶⁷⁸⁹]+)?|[+-]?[0123456789/]+)")
stepen = re.compile(r"[+-]?[0123456789/]*x([²³⁴⁵⁶⁷⁸⁹]+)")
number = re.compile(r"([+-]?[0123456789])")

first = to_dict(a[0])
second = to_dict(a[2])

if a[1] == "+":
    ans = plus(first, second)
    draw(ans)
elif a[1] == "-":
    ans = minus(first, second)
    draw(ans)
elif a[1] == "*":
    ans = mul(first, second)
    draw(ans)
elif a[1] == "/":
    ans = del1(first, second)
    draw(ans[1])
elif a[1] == "%":
    ans = del1(first, second)
    draw(ans[0])
