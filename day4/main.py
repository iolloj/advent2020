def parser(inputFile):
    f = open(inputFile, 'r')
    return f.read().split('\n\n')
ans = 0
"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""
integers = ['{}'.format(i) for i in range(10)]
def cond(key, value):
    if key == 'byr' and 1920 <= int(value) <=2002:
        return True
    elif key == 'iyr' and 2010 <= int(value) <= 2020:
        return True
    elif key == 'eyr' and 2020 <= int(value) <= 2030:
        return True
    elif key == 'hgt':
        if value[-2:] == 'cm':
            return(150<= int(value[:-2]) <= 193)
        if value[-2:] == 'in':
            return(59<= int(value[:-2]) <=76)
    elif key == 'hcl':
        for i in value[1:]:
            if not (i in integers or i in list('abcdef')):
                return False
        return(value[0] == '#' and len(value) == 7)
    elif key == 'ecl':
        return(value in  ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    elif key == 'pid':
        for i in value:
            if i not in integers:
                return False
        return(len(value) == 9)
    else:
        return False
lines = parser('input.txt')
for line in lines:
    line = line.replace('\n', ' ')
    data = line.split(' ')
    fields = {}
    #print(line, data)
    for e in data:
        if e is not '':
            key, value = e.split(':')
            if cond(key, value):
                fields[key] =  value
    if len(fields.keys()) == 7:
        ans += 1
        #print('this one is ok')
print(ans)
