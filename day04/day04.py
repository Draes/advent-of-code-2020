import re


def read_passports():
    lines = [line.replace('\n', ' ') for line in open('day04_input.txt').read().split('\n\n')]
    passports = []
    for line in lines:
        passport = {}
        for x in line.split(" "):
            attribute, value = x.split(":")
            passport[attribute] = value
        passports.append(passport)
    return passports


def pid(value):
    return bool(re.match("^[0-9]{9}$", value))


def ecl(value):
    eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return value in eye_colors


def byr(value):
    if re.match("^[0-9]{4}$", value):
        return 1920 <= int(value) <= 2002


def iyr(value):
    if re.match("^[0-9]{4}$", value):
        return 2010 <= int(value) <= 2020


def hcl(value):
    return bool(re.match("^#[0-9a-f]{6}$", value))


def hgt(value):
    search = re.search("^([0-9]+)(in|cm)$", value)
    if search is not None:
        size = int(search.group(1))
        unit = search.group(2)
        return (unit == "cm" and 150 <= size <= 193) or (unit == "in" and 59 <= size <= 76)


def eyr(value):
    if re.match("^[0-9]{4}$", value):
        return 2020 <= int(value) <= 2030


def validate_passport(passport):
    attribute, value = passport
    return {
        "byr": byr,
        "iyr": iyr,
        "eyr": eyr,
        "hgt": hgt,
        "hcl": hcl,
        "ecl": ecl,
        "pid": pid,
        "cid": lambda _: True
    }.get(attribute)(value)


def validate_all_fields(passport):
    validations = list(map(validate_passport, passport.items()))
    return all(v is True for v in validations)


def contains_all_fields(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return all(f in passport for f in required_fields)


def main():
    passports = read_passports()

    filtered_passports = list(filter(contains_all_fields, passports))
    print(f"Part1: {len(filtered_passports)}")

    valid_passports = len(list(filter(validate_all_fields, filtered_passports)))
    print(f"Part2: {valid_passports}")


if __name__ == "__main__":
    main()
