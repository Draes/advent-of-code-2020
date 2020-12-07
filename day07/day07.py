import re


def read_file_data(path):
    with open(path) as fp:
        return list(map(str.rstrip, fp))


def map_bag(bag):
    pattern = "(?:([0-9]+) ([a-z]+ [a-z]+) bag)"
    s = bag.split("bags contain")
    search = re.findall(pattern, s[1])
    return s[0].strip(), list(map(lambda s: {"number": int(s[0]), "bag": s[1]}, search))


def has_gold(bags, bag):
    if bag == "shiny gold":
        return True
    if bag == "no other":
        return False

    for b in bags.get(bag):
        if has_gold(bags, b["bag"]):
            return True
    return False


def count_bags(bags, bag, total):
    if len(bag) == 0:
        return total

    for b in bag:
        total += b["number"] * count_bags(bags, bags.get(b["bag"]), 1)
    return total


def main():
    file = read_file_data("day07_input.txt")
    bags = dict([map_bag(f) for f in file])

    # remove shiny gold from search to not count itself
    keys = list(bags.keys())
    keys.remove("shiny gold")

    # Part1
    print(sum(has_gold(bags, b) for b in keys))

    # Part2
    print(count_bags(bags, bags.get("shiny gold"), 0))


if __name__ == "__main__":
    main()
