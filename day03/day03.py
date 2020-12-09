import functools

TREE = "#"


def read_file_data(path):
    with open(path) as fp:
        return list(map(str.rstrip, fp))


def process_slope(file_data, limits, slope):
    x_max, y_max = limits
    slope_x, slope_y = slope
    found_trees = x = y = 0

    for i in range(y_max):
        x = (x + slope_x) % x_max
        y += slope_y
        if y < y_max and file_data[y][x] == TREE:
            found_trees += 1
    return found_trees


def main():
    file_data = read_file_data("day03_input.txt")
    x_max, y_max = len(file_data[0]), len(file_data)

    # Part 1
    print(process_slope(file_data, (x_max, y_max), (3, 1)))

    # Part 2
    slopes = {(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)}
    results = [process_slope(file_data, (x_max, y_max), s) for s in slopes]
    print(functools.reduce(lambda a, b: a * b, results))


if __name__ == "__main__":
    main()
