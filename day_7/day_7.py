from itertools import product

with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
lines = [line.split(": ") for line in lines]
lines = [(line[0], line[1].split(" ")) for line in lines]


def calc_possible(line):
    res, nums = line
    num_ops = len(nums) - 1

    op_combs = []

    def backtrack(i, comb):
        if len(comb) >= num_ops:
            op_combs.append(comb.copy())
            return

        comb.append("*")
        backtrack(i + 1, comb)
        comb.pop()

        comb.append("+")
        backtrack(i + 1, comb)
        comb.pop()

    backtrack(0, [])

    for ops in op_combs:
        final_eq = []
        for i, num in enumerate(nums):
            final_eq.append(num)
            final_eq.append(ops[i]) if i < len(ops) else None

        calc = final_eq.copy()
        while len(calc) != 1:
            if calc[1] == "*":
                op_res = [str(int(calc[0]) * int(calc[2]))]
            elif calc[1] == "+":
                op_res = [str(int(calc[0]) + int(calc[2]))]
            calc = op_res + calc[3:]

        if res == calc[0]:
            return True

    return False


possibles = []
for line in lines:
    if calc_possible(line):
        possibles.append(line)

part_1_ans = sum([int(possible[0]) for possible in possibles])
print("Part 1:", part_1_ans)

# Part 2
#


def calc_possible_2(line):
    res, nums = line
    num_ops = len(nums) - 1

    op_combs = []
    for op_comb in product(["||", "*", "+"], repeat=num_ops):
        op_combs.append(op_comb)

    for ops in op_combs:
        final_eq = []
        for i, num in enumerate(nums):
            final_eq.append(num)
            final_eq.append(ops[i]) if i < len(ops) else None

        calc = final_eq.copy()

        while len(calc) != 1:
            if calc[1] == "||":
                op_res = [int(str(calc[0]) + str(calc[2]))]
            elif calc[1] == "*":
                op_res = [int(calc[0]) * int(calc[2])]
            elif calc[1] == "+":
                op_res = [int(calc[0]) + int(calc[2])]

            calc = op_res + calc[3:]

        if int(res) == calc[0]:
            return True

    return False


possibles_2 = []
for line in lines:
    if calc_possible_2(line):
        possibles_2.append(line)

part_2_ans = sum([int(possible[0]) for possible in possibles_2])
print("Part 2:", part_2_ans)
