def read_file_data(path):
    with open(path) as fp:
        return list(map(int, map(str.rstrip, fp)))


expense_report = read_file_data("input.txt")
expense_num = len(expense_report)
expected = 2020

print("Part1")
for i in range(expense_num):
    for j in range(i + 1, expense_num):
        n1, n2 = expense_report[i], expense_report[j]
        if n1 + n2 == expected:
            print(f'{n1} x {n2} = {n1 * n2}')
            break

print("Part2")
for i in range(expense_num):
    for j in range(i + 1, expense_num):
        for k in range(j + 1, expense_num):
            n1, n2, n3 = expense_report[i], expense_report[j], expense_report[k]
            if n1 + n2 + n3 == expected:
                print(f'{n1} x {n2} x {n3} = {n1 * n2 * n3}')
                break
