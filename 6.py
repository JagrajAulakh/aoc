f = open("6.txt", 'r')

lines = f.read().strip().split("\n\n")

tot = []

for group in lines:
    s = dict()
    sp = group.split("\n")
    target = len(sp)
    for i in sp[0]:
        s[i] = 1

    for line in sp[1:]:
        for i in line:
            if i in s.keys():
                s[i] += 1
    tmp = 0
    for i in s.values():
        if i == target:
            tmp += 1
    tot.append(tmp)
    print(s, sp, target, tmp)

print(sum(tot))
