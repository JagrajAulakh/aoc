lines = [x for x in open('7.txt', 'r').read().strip().split("\n")]

bags = {}

for line in lines:
    key,contains = line.split(" contain ")
    key = key[:key.rfind(" ")]
    if 'no other bags' in contains:
        bags[key] = []
        continue

    tmp = []
    for i in contains.split(", "):
        space = i.find(" ")
        tmp.append([int(i[:space]), i[space+1:i.rfind(" ")]])
    bags[key] = tmp


#############################
# PART ONE
#############################

count = 0
keys = list(bags.keys())

tocheck = ['shiny gold']
checked = set()
while tocheck:
    s = tocheck.pop(0)
    c = 0
    for k in keys:
        for i in bags[k]:
            if i[1] == s and k not in checked:
                c += 1
                tocheck.append(k)
                checked.add(k)
                break
    count += c
print(count)


#############################
# PART TWO
#############################
def countInside(key):
    if not bags[key]:
        return 1

    c = 1
    for i in bags[key]:
        c += i[0] * countInside(i[1])
    return c

print(countInside('shiny gold') - 1)

