seq1, seq2 = input().split()
len1, len2 = len(seq1), len(seq2)

prev = [i for i in range(len2 + 1)]

for i in range(len1):
    cur = []
    cur.append(i + 1)
    for j in range(len2):
        cost = 0 if seq1[i] == seq2[j] else 1
        cur.append(min(cur[j] + 1, prev[j + 1] + 1, prev[j] + cost))
    prev = cur

print(cur[-1])

