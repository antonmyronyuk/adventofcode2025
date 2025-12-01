with open("input.txt") as input_file:
    moves = input_file.read().strip().split("\n")

sign_map = {"L": -1, "R": 1}
last_position = 50
num_zeros = num_intermediate_zeros = 0
for move in moves:
    offset_sign = sign_map[move[0]]
    offset_abs = int(move[1:])
    next_position = (last_position + offset_abs * offset_sign) % 100
    num_zeros += next_position == 0
    num_intermediate_zeros += offset_abs // 100
    if last_position == 0:
        pass
    elif next_position == 0 or (last_position - next_position) * offset_sign > 0:
        num_intermediate_zeros += 1

    last_position = next_position

print(num_zeros)  # part 1
print(num_intermediate_zeros)  # part 2
