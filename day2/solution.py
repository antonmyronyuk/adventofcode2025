with open("input.txt") as input_file:
    pairs = input_file.read().strip().split(",")


def is_invalid_number_part1(n) -> bool:
    size = len(str(n))
    div = 10**(size // 2)
    return n // div == n % div


def is_invalid_number_part2(n) -> bool:
    size = len(str(n))
    for ps in range(1, size // 2 + 1):
        prefix = n // 10**(size - ps)
        if int(str(prefix) * (size // ps)) == n:
            return True

    return False


res_part1 = 0
res_part2 = 0
for pair in pairs:
    start, end = list(map(int, pair.split("-")))
    for num in range(start, end + 1):
        if is_invalid_number_part1(num):
            res_part1 += num
        if is_invalid_number_part2(num):
            res_part2 += num

print(res_part1)
print(res_part2)
