with open("input.txt") as input_file:
    ranges_raw, ingredients_raw = input_file.read().strip().split("\n\n")
    ranges = [list(map(int, row.split("-"))) for row in ranges_raw.split("\n")]
    ingredients = list(map(int, ingredients_raw.split("\n")))


def merge_ranges(ranges):
    merged_ranges = []
    for start, end in sorted(ranges):
        if merged_ranges and merged_ranges[-1][1] >= start:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
        else:
            merged_ranges.append([start, end])
    return merged_ranges


merged_ranges = merge_ranges(ranges)
print(sum(start <= i <= end for i in ingredients for start, end in merged_ranges))  # part 1
print(sum(end - start + 1 for start, end in merged_ranges))  # part 2
