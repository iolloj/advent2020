
def parser(inputFile):
    f = open(inputFile, "r")
    return f.read().splitlines()

entries = parser('input.txt')

targetSum = 2020
for entrie in entries[:-1]:
    for entrie2 in entries[:-1]:
        intEntrie = int(entrie)
        intEntrie2 = int(entrie2)
        isPresent = targetSum - intEntrie - intEntrie2
        if str(isPresent) in entries:
            print(isPresent*intEntrie*intEntrie2)


