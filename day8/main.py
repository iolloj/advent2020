import re
with open('input.txt', 'r') as f:
    lines = filter(None, f.read().split('\n'))
    changedLine = 0
    i = 0
    while i < len(lines):
        i, acc = 0, 0
        seen = []
        alreadyChanged = []
        while i not in seen and i < len(lines):
            print(changedLine, i, len(lines))
            cmd, p = re.findall(r'(\w+) ([+-]\d+)', lines[i])[0]
            seen.append(i)
            if cmd == 'acc':
                acc += int(p)
                i += 1
            elif cmd == 'jmp':
                if changedLine == i:
                    i += 1
                else:
                    i += int(p)
            elif cmd == 'nop':
                if changedLine == i:
                    i += int(p)
                else:
                    i+=1
        changedLine += 1
print(acc)
