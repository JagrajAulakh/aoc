lines = [x for x in open("8.txt", 'r').read().strip().split('\n')]


jn = []
for i in range(len(lines)):
    tmp = lines[i].split(" ")[0]
    if tmp == 'nop' or tmp == 'jmp':
        jn.append(i)

while jn:
    i = jn.pop(0)
    tmp = lines[i].split(" ")[0]

    if tmp == 'nop':
        lines[i] = 'jmp' + lines[i][3:]
    elif tmp == 'jmp':
        lines[i] = 'nop' + lines[i][3:]

    checked = set()
    currentIndex = 0
    acc = 0

    while currentIndex not in checked and currentIndex != len(lines)-1:
        checked.add(currentIndex)

        line = lines[currentIndex]
        com,val = line.split(" ")
        if val[0] == "+":
            val = int(val[1:])
        else:
            val = int(val)

        if com == 'acc':
            acc += val
            currentIndex += 1
        elif com == 'jmp':
            currentIndex += val
        else:
            currentIndex += 1

    tmp = lines[i].split(" ")[0]
    if tmp == 'nop':
        lines[i] = 'jmp' + lines[i][3:]
    elif tmp == 'jmp':
        lines[i] = 'nop' + lines[i][3:]

    if currentIndex == len(lines)-1:
        print(acc)
        break
