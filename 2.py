def xor(a, b):

    return (a or b) and not (a and b)
f = open("./2.txt", 'r')

lines = f.read().strip().split("\n")

print(len(lines))

tot = 0

for line in lines:
    a,password = line.strip().split(": ")

    nums,char = a.split(" ")
    low,high = nums.split("-")
    low = int(low)
    high = int(high)

    count = 0
    # print(low, high, char, password, len(password))
    if (len(password) >= high and len(password) >= low):
        low-=1
        high-=1
        if xor(password[low] == char, password[high] == char):
            tot += 1
    # for c in password:
    #     if c == char:
    #         count += 1
    # if low <= count <= high:
        # tot += 1

print(tot)
