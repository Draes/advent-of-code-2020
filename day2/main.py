import re


def parse_inputs(input):
    min, max, char, passw = re.split("-| |: ", input)
    return {
        "min": int(min),
        "max": int(max),
        "char": char[0],
        "passw": passw
    }


def read_file_data(path):
    with open(path) as fp:
        return list(map(parse_inputs, map(str.rstrip, fp)))


def part_1(entries):
    valid_passwords = 0
    for e in entries:
        char_count = len(list(filter(lambda c: c == e["char"], e["passw"])))
        if e["min"] <= char_count <= e["max"]:
            valid_passwords += 1
    print(f'Part1: {valid_passwords}')


def part_2(entries):
    valid_passwords = 0
    for e in entries:
        char_at_min, char_at_max = e["passw"][e["min"] - 1], e["passw"][e["max"] - 1]
        if (char_at_min == e["char"] or char_at_max == e["char"]) and char_at_min != char_at_max:
            valid_passwords += 1
    print(f'Part2: {valid_passwords}')


entries = read_file_data("input.txt")
part_1(entries)
part_2(entries)
