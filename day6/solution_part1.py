import math

with open("input.txt") as input_file:
    rows = input_file.read().strip().split("\n")
    num_sets = [list(map(int, row.split())) for row in rows[:-1]]
    operations = rows[-1].split()

op_map = {"+": sum, "*": math.prod}
print(sum(op_map[op](nums) for *nums, op in zip(*num_sets, operations)))
