from PIL import Image, ImageDraw

with open("input.txt") as input_file:
    coords = [tuple(map(int, row.split(","))) for row in input_file.read().strip().split("\n")]

max_area = 0
for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        (x1, y1), (x2, y2) = coords[i], coords[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        max_area = max(max_area, area)

print(max_area)  # part 1

# pivot points (from the image)
# 94679,50407
# 94679,48332

# upper pivot
# max_inner_area = 0
# pivot_x, pivot_y = 94679, 48332
# target_x, target_y = 0, 0
# for x, y in coords:
#     if x > pivot_x or y > pivot_y or y < 36000:
#         continue
#
#     area = (abs(pivot_x - x) + 1) * (abs(pivot_y - y) + 1)
#     if area > max_inner_area:
#         max_inner_area = area
#         target_x, target_y = x, y
#
# print(max_inner_area)
# print(target_x, target_y)
# 1077517071
# 3957 36456

max_inner_area = 0
pivot_x, pivot_y = 94679, 50407
target_x, target_y = 0, 0
for x, y in coords:
    if x > pivot_x or y < pivot_y or y > 68000 or x <= 5475:
        continue

    area = (abs(pivot_x - x) + 1) * (abs(pivot_y - y) + 1)
    if area > max_inner_area:
        max_inner_area = area
        target_x, target_y = x, y

print(max_inner_area)
print(target_x, target_y)
# 1498673376
# 5664 67242

image = Image.new("RGB", (10000, 10000), "white")
draw = ImageDraw.Draw(image)
# draw.rectangle([(target_x // 10, target_y // 10), (pivot_x // 10, pivot_y // 10)], fill="red", width=2)
draw.rectangle([(target_x // 10, pivot_y // 10), (pivot_x // 10, target_y // 10)], fill="red", width=2)
for x, y in coords:
    draw.circle((x // 10, y // 10), radius=10, fill="black")

for (x1, y1), (x2, y2) in zip(coords, coords[1:] + [coords[0]]):
    draw.line((x1 // 10, y1 // 10, x2 // 10, y2 // 10), fill="black", width=2)

image.show()
