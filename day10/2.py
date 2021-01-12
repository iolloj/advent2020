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


