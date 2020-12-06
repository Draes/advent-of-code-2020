def count_group_answers(group):
    joined = ''.join(group)
    return sum([joined.count(i) == len(group) for i in set(joined)])


def main():
    data = open('day06_input.txt').read().split('\n\n')

    lines = [len(set(line.replace('\n', ''))) for line in data]
    part1 = sum(lines)
    print(f"Part1: {part1}")

    lines = [line.split('\n') for line in data]
    part2 = sum(map(count_group_answers, lines))
    print(f"Part2: {part2}")


if __name__ == "__main__":
    main()
