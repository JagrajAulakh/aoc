def findSum(prev, targ):
    for i in range(25):
        for j in range(25):
            if i != j and prev[i]+prev[j] == targ:
                return True
    return False

lines = [int(x) for x in open("9.txt", 'r').read().strip().split("\n")]


# for i in range(25, len(lines)):
#     prev = lines[i-25:i]

#     if not findSum(prev, lines[i]):
#         print(lines[i])
#         break

targ = 217430975

for i in range(len(lines)):
    j = i
    s = 0
    seq = []
    found = False
    while j < len(lines) and s < targ:
        s += lines[j]
        seq.append(lines[j])
        if s == targ:
            print(s, targ, i, j, lines[i] + lines[j])
            print(max(seq) + min(seq))
            found = True
            break
        j += 1

    if found: break


