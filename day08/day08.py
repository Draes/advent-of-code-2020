import re

INSTRUCTION_PATTERN = "([a-z]{3}) ([+-][0-9]+)"
accumulator = 0


def read_file_data(path):
    with open(path) as fp:
        return list(map(map_instruction, fp))


def map_instruction(line):
    search = re.search(INSTRUCTION_PATTERN, line.rstrip())
    operation, argument = search.groups()
    return operation, argument


def acc(argument):
    global accumulator
    accumulator += int(argument)
    return 1


def jmp(argument):
    return int(argument)


def nop(_):
    return 1


def run_instruction(operation, argument):
    return {
        "acc": acc,
        "jmp": jmp,
        "nop": nop
    }.get(operation)(argument)


def is_infinite(instructions):
    global accumulator
    position = accumulator = 0
    visited = set()
    while position < len(instructions):
        operation, argument = instructions[position]
        if position not in visited:
            visited.add(position)
            position += run_instruction(operation, argument)
        else:
            return True


def get_indexes_of_operation(instructions, wanted):
    indexes = set()
    for i in range(len(instructions)):
        operation, _ = instructions[i]
        if operation == wanted:
            indexes.add(i)
    return indexes


def find_bug(instructions, original, new):
    swap_instructions = get_indexes_of_operation(instructions, original)
    for swap in swap_instructions:
        aux = instructions.copy()
        _, argument = aux[swap]

        aux[swap] = (new, argument)
        if not is_infinite(aux):
            print(f"swapped {original} {argument} to {new}, accumulator={accumulator}")
            break


def part_1(instructions):
    global accumulator
    is_infinite(instructions)
    print(accumulator)


def part_2(instructions):
    find_bug(instructions, "jmp", "nop")
    find_bug(instructions, "nop", "jmp")


def main():
    instructions = read_file_data("day08_input.txt")

    part_1(instructions)
    part_2(instructions)


if __name__ == "__main__":
    main()
