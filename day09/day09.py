import itertools as it

RANGE_SIZE = 25


def read_file_data(path):
    with open(path) as fp:
        return list(map(int, fp))


def contains_sum(numbers, value):
    for a, b in it.combinations(numbers, 2):
        if a + b == value:
            return True


def find_sequence(numbers, value):
    sequence = list()
    for n in numbers:
        sequence.append(n)
        if len(sequence) > 1 and sum(sequence) == value:
            sequence.sort()
            smallest, largest = sequence[0], sequence[-1]
            print(f"{smallest} + {largest} = {smallest + largest}")


def part2(numbers, value):
    [find_sequence(numbers[i:], value) for i in range(len(numbers))]


def part1(entries):
    for i in range(len(entries)):
        numbers, value = entries[i:RANGE_SIZE + i], entries[RANGE_SIZE + i]
        if not contains_sum(numbers, value):
            return entries[RANGE_SIZE + i]


def main():
    entries = read_file_data("day09_input.txt")

    invalid_number = part1(entries)
    print(invalid_number)

    part2(entries, invalid_number)


if __name__ == "__main__":
    main()
