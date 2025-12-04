with open("input.txt") as input_file:
    grid = [list(line) for line in input_file.read().strip().split("\n")]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
n, m = len(grid), len(grid[0])
counts = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == "@":
            counts[i][j] = 0
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == "@":
                    counts[i][j] += 1

initial_accessible_rolls = sum(0 <= counts[i][j] < 4 for i in range(n) for j in range(m))
found = initial_accessible_rolls > 0
total_accessible_rolls = 0
while found:
    found = False
    for i in range(n):
        for j in range(m):
            if 0 <= counts[i][j] < 4:
                found = True
                counts[i][j] = -1
                total_accessible_rolls += 1
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and counts[ni][nj] > 0:
                        counts[ni][nj] -= 1

print(initial_accessible_rolls)  # part 1
print(total_accessible_rolls)  # part 2
