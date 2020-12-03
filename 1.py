f = open("1.txt", 'r')

lines = f.read().strip().split("\n")

nums = []

for line in lines:
    i = int(line)
    nums.append(i)
    
for i in nums:
    for j in nums:
        for k in nums:
            if i+j+k == 2020:
                print(i*j*k)
