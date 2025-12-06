import itertools
import math

with open("input.txt") as input_file:
    field = [list(row) for row in input_file.read().split("\n") if row]

op_map = {"+": sum, "*": math.prod}
transposed = zip(*field)
rows = ["".join(row).strip() for row in transposed]
groups = [list(group) for cond, group in itertools.groupby(rows, lambda x: not x) if not cond]
res = 0
for group in groups:
    op = group[0][-1]
    nums = [int(row.replace("*", "").replace("+", "")) for row in group]
    res += op_map[op](nums)

print(res)
