import re

INSTRUCTION_PATTERN = "([A-Z])([0-9]+)"


def map_instruction(line):
    groups = re.search(INSTRUCTION_PATTERN, line.rstrip()).groups()
    return groups[0], int(groups[1])


def read_file_data(path):
    with open(path) as fp:
        return list(map(map_instruction, fp))


# ----------------- Part 1 -----------------
def move_forward(position, direction, value):
    x, y = position
    pos = {
        0: (x + value, y),
        90: (x, y - value),
        180: (x - value, y),
        270: (x, y + value)
    }.get(direction)
    return pos


def do_instruction_part1(position, direction, instruction):
    action, value = instruction
    x, y = position

    if action in "RL":
        direction = {
            "L": lambda v: (direction + v) % 360,
            "R": lambda v: (direction - v) % 360
        }.get(action)(value)

    else:
        position = {
            "N": lambda v: (x, y - v),
            "S": lambda v: (x, y + v),
            "E": lambda v: (x + v, y),
            "W": lambda v: (x - v, y),
            "F": lambda v: move_forward(position, direction, v)
        }.get(action)(value)
    return position, direction


def part1(instructions):
    position, direction = (0, 0), 0
    for i in instructions:
        position, direction = do_instruction_part1(position, direction, i)

    east, north = position
    print(f"{east}E {north}N = {abs(east) + abs(north)}")


# ----------------- Part 2 -----------------
def update_waypoint(waypoint, value):
    x, y = waypoint
    return {
        90: (y, -x),
        180: (-x, -y),
        270: (-y, x)
    }.get(value % 360)


def do_instruction_part2(position, waypoint, instruction):
    action, value = instruction
    xw, yw = waypoint

    if action == "F":
        x, y = position
        position = x + (xw * value), y + (yw * value)

    else:
        waypoint = {
            "N": lambda v: (xw, yw + v),
            "S": lambda v: (xw, yw - v),
            "E": lambda v: (xw + v, yw),
            "W": lambda v: (xw - v, yw),
            "L": lambda v: update_waypoint(waypoint, -v),
            "R": lambda v: update_waypoint(waypoint, v)
        }.get(action)(value)

    return position, waypoint


def part2(instructions):
    position, waypoint = (0, 0), (10, 1)
    for i in instructions:
        position, waypoint = do_instruction_part2(position, waypoint, i)

    east, north = position
    print(f"{east}E {north}N = {abs(east) + abs(north)}")


def main():
    instructions = read_file_data("day12_input.txt")
    part1(instructions)
    part2(instructions)


if __name__ == "__main__":
    main()
