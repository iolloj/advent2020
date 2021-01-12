with open('input.txt', 'r') as f:
    ans = f.read().split('\n\n')
    ans = map(lambda x: filter(None, x.split('\n')), ans)
    count = 0
    for group in ans:
        dic = {}
        n = len(group)
        for person in group:
            if person != '':
                for char in person:
                    if char not in dic:
                        dic[char] = 1
                    else:
                        dic[char] += 1
            everyoneAns = [e for e in dic.keys() if dic[e] == n]
            count += len(everyoneAns)
    print(count)
