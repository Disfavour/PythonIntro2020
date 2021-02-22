def fcounter(self, *args):
    q = self(*args)
    d = {0: [], 1: [], 2: [], 3: []}

    for item in dir(self):
        if item[0] != "_":
            if callable(getattr(self, item)):
                d[0].append(item)
            else:
                d[1].append(item)

    for item in dir(q):
        if item[0] != "_":
            if callable(getattr(q, item)):
                d[2].append(item)
            else:
                d[3].append(item)

    d[2] = [i for i in d[2] if i not in d[0]]
    d[3] = [i for i in d[3] if i not in d[1]]

    map(sorted, d.values())

    return d[0], d[1], d[2], d[3]
