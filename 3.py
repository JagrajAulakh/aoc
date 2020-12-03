f = open("3.txt", "r")

grid = f.read().strip().split("\n")

m = 1
t = [ [1,1], [3,1], [5,1], [7,1], [1,2] ]
for i in t:
    trees = 0
    x = 0
    y = 0
    while y < len(grid):
        if grid[y][x] == "#":
            trees += 1
        y += i[1]
        x = (x+i[0]) % len(grid[0])

    m *= trees
    print(trees)

print(m)
