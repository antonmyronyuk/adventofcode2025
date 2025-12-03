with open("input.txt") as input_file:
    banks = [[int(bat) for bat in bank] for bank in input_file.read().strip().split("\n")]


def get_max_battery(bank):
    max_bat, max_pos = 0, -1
    for i, bat in enumerate(bank):
        if bat > max_bat:
            max_bat, max_pos = bat, i
    return max_bat, max_pos


def get_max_voltage(bank, num_batteries):
    bats = []
    start_pos = 0
    for i in range(num_batteries):
        end_pos = len(bank) - num_batteries + i + 1
        bat, bat_pos = get_max_battery(bank[start_pos:end_pos])
        bats.append(bat)
        start_pos += bat_pos + 1

    return sum(bat * 10**i for i, bat in enumerate(reversed(bats)))


print(sum(get_max_voltage(bank, 2) for bank in banks))  # part 1
print(sum(get_max_voltage(bank, 12) for bank in banks))  # part 2
