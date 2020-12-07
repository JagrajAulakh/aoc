f = open("6.txt", 'r')

lines = f.read().strip().split("\n\n")

tot = []

for group in lines:
    s = []
    sp = group.split("\n")

    for line in sp:
        tmp = set()
        for i in line:
            tmp.add(i)
        s.append(tmp)

    sub = s[0]
    for i in s[1:]:
        tmp = sub-i
        for j in list(sub):
            if j in tmp:
                sub.remove(j)
    tot.append(len(list(sub)))

print(sum(tot))
