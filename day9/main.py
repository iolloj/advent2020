prefix = 25
with open('input.txt', 'r') as f:
    lines = filter(None, f.read().split('\n'))
    preamble = {i:int(lines[i]) for i in range(prefix)}
    for i, line in enumerate(lines[prefix:]):
        n = int(line)
        isValid = False
        for preambleNum in preamble.values():
            if n - preambleNum in preamble.values():
                isValid = True
                continue
        if not isValid:
            nonValid = n
            print(n)
        del preamble[i]
        preamble[prefix+i] = n
# part 2
tab = [sum([int(line) for line in lines[:j]]) for j in range(2,len(lines))]
for i, d in enumerate(lines):
    nonValid += int(d)
    if nonValid in tab:
        print(int(max((lines[i+1:tab.index(nonValid)+1]))) + int(min((lines[i+1:tab.index(nonValid)+1]))))
