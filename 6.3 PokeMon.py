a = input()
D = dict()
D1 = dict()
while a:
    a = a.split(" / ")

    if not a[0].isdigit():
        if a[0] in D:
            D[a[0]].append(a[1])
        else:
            D[a[0]] = [a[1]]

    else:
        if a[0] in D1:
            D1[a[0]].append(a[1])
        else:
            D1[a[0]] = []
            D1[a[0]].append(a[1])

    a = input()

D2 = dict()
for name, number in D.items():
    D2[name] = len(set([i for j in number for i in D1[j]]))

D2 = {key: value for key, value in reversed(sorted(D2.items(), key=lambda x: x[1]))}

A = max(D2.values())

answer = []
for name, number in D2.items():
    if number == A:
        answer.append(name)
    else:
        break

for item in sorted(answer):
    print(item)
