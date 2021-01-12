with open('input.txt', 'r') as f:
    lines = [0] + filter(None, f.read().split('\n'))
    lines = map(lambda x: int(x), lines)
    lines.sort()
    count1, count3 = 0, 1
    for i in range(len(lines)-1):
        diff = lines[i+1] - lines[i]
        if diff  == 1:
            count1 += 1
        elif lines[i+1] - lines[i] == 3:
            count3 += 1
    print(count1*count3)

# Part 2
availAdapt = {}
for i, line in enumerate(lines) :
    maxindex = min(i+4, len(lines))
    availAdapt[line] = [lines[k] for k in range(i + 1, maxindex)  if lines[k] - line <=3]

alreadyComputed = {}
def count(start):
    if start == lines[-1]:
        return 1
    res = 0
    for i in availAdapt[start]:
        if i not in alreadyComputed:
            alreadyComputed[i] = count(i)
        res += alreadyComputed[i] 
    return res

print(count(lines[0]))
