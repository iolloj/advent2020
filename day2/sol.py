def parser(inputFile):
    f = open(inputFile, "r")
    return f.read().splitlines()

entries = parser('input.txt')
validCounter = 0
for line in entries:
    number, targetLetter, password = line.split()
    lower, upper = [int(e) for e in number.split('-')]
    counterTarget = 0
    for letter in password:
        if targetLetter[0] == letter:
            counterTarget += 1
    if upper >= counterTarget >= lower:
        validCounter += 1
print(validCounter)


counter2 = 0
for line in entries:
    number, targetLetter, password = line.split()
    lower, upper = [int(e)-1 for e in number.split('-')]
    print(password, lower, upper)
    nor = [password[lower] == targetLetter[0], password[upper] == targetLetter[0]]
    if nor[0] != nor[1]:
        counter2 += 1
print(counter2)
