turing = []
data = input()
while " " in data:
    turing.append(data.split())
    data = input()
else:
    seq = list(data)

alpha = turing.pop(0)

for i in range(len(turing)):
    for j in range(1, len(turing[0])):
        turing[i][j] = turing[i][j].split(",")

state = pos = 0

for i in range(100000):
    col = alpha.index(seq[pos]) + 1
    row = state
    if turing[row][col][0]:
        seq[pos] = turing[row][col][0]
    if turing[row][col][1] == "L":
        pos -= 1
        if pos < 0:
            seq.insert(0, "_")
            pos = 0
    if turing[row][col][1] == "R":
        pos += 1
        if pos == len(seq):
            seq.append("_")
    if turing[row][col][2]:
        if turing[row][col][2] == "!":
            seq = [item if item != "_" else " " for item in seq]
            print("".join(seq).strip())
            break
        else:
            state = int(turing[row][col][2])
