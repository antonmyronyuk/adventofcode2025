from collections import deque

with open("input.txt") as input_file:
    field = [list(row) for row in input_file.read().strip().split("\n")]

n, m = len(field), len(field[0])
si, sj = next((i, j) for i in range(n) for j in range(m) if field[i][j] == "S")
pipes = set()
splits = set()
queue = deque([(si + 1, sj)])
while queue:
    i, j = queue.popleft()
    if (i, j) in pipes:
        continue

    pipes.add((i, j))
    ni = i + 1
    if ni >= n:
        continue

    if field[ni][j] == ".":
        queue.append((ni, j))
    else:
        splits.add((ni, j))
        for dj in (1, -1):
            nj = j + dj
            if 0 <= nj < m:
                queue.append((ni, nj))

print(len(splits))  # part 1

path_counts = [[0] * m for _ in range(n)]
ordered_pipes = sorted(pipes)
pi, pj = ordered_pipes.pop(0)
path_counts[pi][pj] = 1
for i, j in ordered_pipes:
    path_counts[i][j] = (
        path_counts[i - 1][j]
        + (path_counts[i - 1][j - 1] if j > 0 and field[i][j - 1] == "^" else 0)
        + (path_counts[i - 1][j + 1] if j < m - 1 and field[i][j + 1] == "^" else 0)
    )

print(sum(path_counts[n - 1]))  # part 2
