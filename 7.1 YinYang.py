def YinYang(*seq):
    a = []
    for item in seq:
        for i in item:
            if i % 2 == 0:
                yield i
            else:
                a.append(i)
    yield from a
