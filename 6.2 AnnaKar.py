N, W = eval(input())
a = input()
D = dict()
template = ",*()[]{}-=_.;%\$@^&\|#':?!" + "\""

while a:
    for k in template:
        if k in a:
            a = a.replace(k, " ")

    for item in a.lower().split():
        if item.isalpha() and len(item) >= W:
            if item in D:
                D[item] += 1
            else:
                D[item] = 1

    a = input()

D = {key: value for key, value in reversed(sorted(D.items(), key=lambda x: x[1]))}

last = 0
D1 = dict()
for word, number in D.items():
    if last == number or last == 0:
        if number in D1:
            D1[number].append(word)
        else:
            if len(D1.keys()) == N:
                break
            else:
                D1[number] = [word]

for item in D1.values():
    item.sort()

D1 = {k: v for k, v in sorted(D1.items(), key=lambda item: item[0])}

for number, word in D1.items():
    for item in word:
        print(number, ": ", item, sep="")
