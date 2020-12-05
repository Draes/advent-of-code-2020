import functools


def read_file_data(path):
    with open(path) as fp:
        return list(map(str.rstrip, fp))


file_data = read_file_data("day03_input.txt")
x_max, y_max = len(file_data[0]), len(file_data)
tree = "#"


def process_slope(slope_x, slope_y):
    found_trees, x, y = 0, 0, 0
    for i in range(y_max):
        x = (x + slope_x) % x_max
        y += slope_y
        if y < y_max and file_data[y][x] == tree:
            found_trees += 1
    return found_trees


def main():
    # Part 1
    print(process_slope(3, 1))

    # Part 2
    slopes = {(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)}
    results = list(map(lambda a: process_slope(a[0], a[1]), slopes))
    print(functools.reduce(lambda a, b: a * b, results))


if __name__ == "__main__":
    main()
