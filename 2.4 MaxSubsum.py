a = int(input())
sum, maxsum = 0, 0
neg = -9999999999
while a:
    sum += a
    if maxsum < sum:
        maxsum = sum
    elif sum < 0:
        sum = 0

    if a < 0 and a > neg:
        neg = a
    a = int(input())
if maxsum != 0:
    print(maxsum)
else:
    print(neg)
