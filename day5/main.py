dic1 = {'F':0, 'B':1}
dic2 = {'L':0, 'R':1}
def binary(boardPass, dic):
    if len(boardPass) == 0: return 0
    return dic[boardPass[-1]] + 2 * binary(boardPass[:-1], dic)

with open('input.txt', 'r') as f:
    txt = f.read().splitlines()
    seats = map(lambda x: 8 * binary(x[:-3], dic1) + binary(x[-3:], dic2), txt)
    N = max(seats)
    print(N)
    for i in range(N):
        if i not in seats:
            if i-1 in seats and i+1 in seats:
                print(i)
