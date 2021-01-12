def parser(inputFile):
    f = open(inputFile, "r")
    return f.read().splitlines()

entries = parser('input.txt')
j = 0
i = 0
counter = 0
while i < len(entries):
    if entries[i][j] == '#':
        counter += 1
    i += 1
    j = (j + 3)%len(entries[0])
print(counter)

directions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
productCounter = 1
for steps in directions:
    j = 0
    i = 0
    counter2 = 0
    while i < len(entries):
        if entries[i][j] == '#':
            counter2 += 1
        j = (j + steps[0])%len(entries[i])
        i += steps[1]
    productCounter *= counter2
print(productCounter)

