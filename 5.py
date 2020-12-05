
f = open("5.txt", 'r')

lines = f.read().strip().split("\n")

high = 0

t = set()

for line in lines:
    row = line[:-3]
    col = line[-3:]

    row = row.replace("F", "0").replace("B", "1")
    row = int(row, 2)

    col = col.replace("L", "0").replace("R", "1")
    col = int(col, 2)

    sid = row*8 + col

    t.add(sid)
    high = max(high, sid)

print("high:", high)

t = list(t)
for i in range(len(t)):
    if t[i] != i+t[0]:
        print(t[0]+i)
        break
