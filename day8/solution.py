import math
from heapq import heappop, heappush

with open("input.txt") as input_file:
    coords = [tuple(map(int, row.split(","))) for row in input_file.read().strip().split("\n")]

distances = []
for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        heappush(distances, (math.dist(coords[i], coords[j]), (i, j)))

n = 0
groups_by_vertexes = {i: frozenset([i]) for i in range(len(coords))}
while distances:
    dist, (i, j) = heappop(distances)
    n += 1
    if groups_by_vertexes[i] != groups_by_vertexes[j]:
        connected_group = groups_by_vertexes[i] | groups_by_vertexes[j]
        for vertex in connected_group:
            groups_by_vertexes[vertex] = connected_group

    if n == 1000:
        group_sizes = [len(group) for group in set(groups_by_vertexes.values())]
        print(math.prod(sorted(group_sizes, reverse=True)[:3]))

    if len(groups_by_vertexes[i]) == len(coords):
        print(coords[i][0] * coords[j][0])
        break
