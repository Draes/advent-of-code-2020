import re

BAG_PATTERN = "(?:([0-9]+) ([a-z]+ [a-z]+) bag)"


def read_file_data(path):
    with open(path) as fp:
        return list(map(str.rstrip, fp))


def build_bag(contents):
    number, bag = contents
    return {
        "number": int(number),
        "bag": bag
    }


def map_bag(bag):
    bag, contents = bag.split("bags contain")
    search = re.findall(BAG_PATTERN, contents)
    return bag.strip(), list(map(build_bag, search))


def has_gold(bags, bag):
    if bag == "shiny gold":
        return True
    if bag == "no other":
        return False

    for b in bags.get(bag):
        if has_gold(bags, b["bag"]):
            return True
    return False


def count_bags(bags, bag, total=0):
    if len(bag) == 0:
        return total

    inner_bags = [b["number"] * count_bags(bags, bags.get(b["bag"]), 1) for b in bag]
    return total + sum(inner_bags)


def main():
    file = read_file_data("day07_input.txt")
    bags = dict([map_bag(line) for line in file])

    # remove shiny gold from search to not count itself
    keys = list(bags.keys())
    keys.remove("shiny gold")

    # Part1
    print(sum(has_gold(bags, bag) for bag in keys))

    # Part2
    print(count_bags(bags, bags.get("shiny gold")))


if __name__ == "__main__":
    main()
