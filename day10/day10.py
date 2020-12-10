def read_file_data(path):
    with open(path) as fp:
        return list(map(int, fp))


def calc_costs(tree_stuff, costs, search, total=0):
    if search in costs:
        return costs[search]
    if len(tree_stuff[search]) == 0:
        total = 1

    for c in tree_stuff[search]:
        total += calc_costs(tree_stuff, costs, c)
    costs[search] = total


def build_diff_map(adapters):
    max_index = len(adapters)
    tree_entries = list()
    for i in range(max_index):
        next_adapters = list()
        # since the list is ordered we just need to check the next 3 adapters for compatibility
        for j in range(i + 1, i + 4):
            if j < max_index and adapters[j] - adapters[i] <= 3:
                next_adapters.append(adapters[j])
        tree_entries.append((adapters[i], next_adapters))
    return dict(tree_entries)


def part1(adapters):
    differences = {1: 0, 3: 0}
    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        differences[diff] += 1

    print(differences[1] * differences[3])


def part2(adapters):
    # build diffs map of each possible adapter that can be used next
    diff_map = build_diff_map(adapters)

    # calc costs
    costs = dict()
    keys = list(diff_map.keys())
    keys.reverse()
    for i in keys:
        calc_costs(diff_map, costs, i)

    # combinations since joltage 0
    print(costs[0])


def main():
    adapters = read_file_data("day10_input.txt")
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    part1(adapters)
    part2(adapters)


if __name__ == "__main__":
    main()
