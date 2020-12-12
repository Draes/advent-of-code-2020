SEARCH_DIRECTIONS = [
    (1, 0), (-1, 0), (0, 1), (0, -1),
    (1, 1), (1, -1), (- 1, 1), (-1, -1)
]


def read_file_data(path):
    with open(path) as fp:
        return list(map(lambda a: list(a.rstrip()), fp))


def count_occupied_seats(seats):
    total = 0
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == '#':
                total += 1
    return total


# ----------------- Part 1 -----------------
def get_adjacent_part1(seats, position, increment):
    y, x = position[0] + increment[0], position[1] + increment[1]
    if 0 <= x < len(seats[0]) and 0 <= y < len(seats):
        if seats[y][x] == '#':
            return 1
    return 0


def part1(seats, position):
    y, x = position
    if seats[y][x] == '.':
        return '.'

    occupied_adjacent = sum(get_adjacent_part1(seats, position, direction) for direction in SEARCH_DIRECTIONS)
    if occupied_adjacent == 0 and seats[y][x] == 'L':
        return '#'

    if occupied_adjacent >= 4 and seats[y][x] == '#':
        return 'L'
    return seats[y][x]


# ----------------- Part 2 -----------------
def get_adjacent_part2(seats, position, increment):
    y, x = position[0] + increment[0], position[1] + increment[1]

    if 0 <= x < len(seats[0]) and 0 <= y < len(seats):
        if seats[y][x] == 'L':
            return 0
        if seats[y][x] == '#':
            return 1
        return get_adjacent_part2(seats, (y, x), increment)
    return 0


def part2(seats, position):
    y, x = position
    if seats[y][x] == '.':
        return '.'

    occupied_adjacent = sum(get_adjacent_part2(seats, position, direction) for direction in SEARCH_DIRECTIONS)
    if occupied_adjacent == 0 and seats[y][x] == 'L':
        return '#'
    if occupied_adjacent >= 5 and seats[y][x] == '#':
        return 'L'
    return seats[y][x]


# ----------------- Main -----------------
def find_equilibrium(seats, update):
    max_x, max_y = len(seats[0]), len(seats)
    while True:
        print(".", end="")
        new = []
        for y in range(max_y):
            line = [update(seats, (y, x)) for x in range(max_x)]
            new.append(line)

        if seats != new:
            seats = new
        else:
            print(count_occupied_seats(new))
            break


def main():
    seats = read_file_data("day11_input.txt")
    find_equilibrium(seats, part1)
    find_equilibrium(seats, part2)


if __name__ == "__main__":
    main()
