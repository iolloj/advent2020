import re
iscontainedin = {}
contains = {}

with open('input.txt', 'r') as f:
    lines = filter(None, f.read().split('\n'))
    for line in lines:
        bigBag = re.findall(r'(.+?) bags contain', line)[0]
        smallBags = re.findall(r'(\d+) (\w+ \w+) bags?', line)
        for ct, bag in smallBags:
            if bigBag not in contains:
                contains[bigBag] = []
            contains[bigBag] += [(ct, bag)]
            if bag in iscontainedin:
                iscontainedin[bag] += [bigBag]
            else:
                iscontainedin[bag] = [bigBag]


def explorer(color):
    count = 0
    toSee = iscontainedin[color]
    seen = []
    while toSee != []:
        currentBag = toSee.pop()
        if currentBag not in seen:
            seen.append(currentBag)
            count += 1
            if currentBag in iscontainedin:
                toSee += iscontainedin[currentBag]
    return count
# part 1
#print(explorer('shiny gold'))
print(contains)
# part 2
def howManyBags(color):
    count = 0
    if color not in contains:
        return 0
    for ct, bag in contains[color]:
        ct = int(ct)
        count += ct * (1 + howManyBags(bag))
    return count
print(howManyBags('shiny gold'))
