#You will want this import for Step 4
from operator import itemgetter

def countWords(counts,line):
    # You should write this function in Step 1,
    # and improve it in Step 2

    words = line.split()

    for word in words:
        word = word.strip('-?.!,[]—:;"\'')
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def printResults(counts):
    # You will replace this code in Step 3 and 4
    sorted_dict = {}
    sorted_keys = sorted(counts.keys())

    for key in sorted_keys:
        sorted_dict[key] = counts[key]
    for key, value in sorted_dict.items():
        print(key, ':', value)
    pass


# You do not need to modify this function.
# It will call your countWords and printResults functions

def countFile(fname):
    counts={}
    with open(fname) as f:
        for line in f:
            countWords(counts,line)
            pass
        pass
    printResults(counts)
    pass