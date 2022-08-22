def sortFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            lst.append(line)
    lst.sort()
    return lst