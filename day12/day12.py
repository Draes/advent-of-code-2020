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
            "L": (direction + value) % 360,
            "R": (direction - value) % 360
        }.get(action)

    else:
        position = {
            "N": (x, y - value),
            "S": (x, y + value),
            "E": (x + value, y),
            "W": (x - value, y),
            "F": move_forward(position, direction, value)
        }.get(action)
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
            "N": (xw, yw + value),
            "S": (xw, yw - value),
            "E": (xw + value, yw),
            "W": (xw - value, yw),
            "L": update_waypoint(waypoint, -value),
            "R": update_waypoint(waypoint, value)
        }.get(action)

    return position, waypoint


def part2(instructions):
    position, waypoint = (0, 0), (10, 1)
    for i in instructions:
        position, waypoint = do_instruction_part2(position, waypoint, i)

    east, north = position
    print(f"{east}E {north}N = {abs(east) + abs(north)}")


# ----------------- Main -----------------
def main():
    instructions = read_file_data("day12_input.txt")
    part1(instructions)
    part2(instructions)


if __name__ == "__main__":
    main()
