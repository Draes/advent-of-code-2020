import math


def read_file_data(path):
    with open(path) as fp:
        return list(map(str.rstrip, fp))


def search_value(value):
    start, end = 0, math.pow(2, len(value))
    for partition in value:
        if partition in {"F", "L"}:
            end -= (end - start) / 2
        if partition in {"B", "R"}:
            start += (end - start) / 2
    return int(start)


# alternative with binary conversion
def search_value_binary(value):
    binary_value = value.replace("B", "1") \
        .replace("F", "0") \
        .replace("R", "1") \
        .replace("L", "0")
    return int(binary_value, 2)


def main():
    seats = read_file_data("day05_input.txt")
    seat_ids = list(map(lambda s: search_value(s[:7]) * 8 + search_value(s[7:]), seats))
    seat_ids.sort()

    max_seat = max(seat_ids)
    print(f"Part1: {max_seat}")

    missing_seats = list(filter(lambda s: s not in seat_ids, range(min(seat_ids), max_seat)))
    print(f"Part2: {missing_seats}")


if __name__ == "__main__":
    main()
