with open("test_input.txt") as f:
    lines = f.read().split("\n\n")


def get_combo_operand(combo_operand):
    if 0 <= combo_operand <= 3:
        value = combo_operand
    elif combo_operand == 4:
        value = register["A"]
    elif combo_operand == 5:
        value = register["B"]
    elif combo_operand == 6:
        value = register["C"]
    else:
        return -1
    return value


def get_instruction(op_code, operand, pointer):
    combo_op = get_combo_operand(operand)
    res = None

    if op_code == 0:
        register["A"] = register["A"] // (2**combo_op)
    elif op_code == 1:
        register["B"] = register["B"] ^ operand
    elif op_code == 2:
        register["B"] = combo_op % 8
    elif op_code == 3:
        if register["A"] != 0:
            pointer = operand
            return pointer, None
    elif op_code == 4:
        register["B"] = register["B"] ^ register["C"]
    elif op_code == 5:
        res = combo_op % 8
    elif op_code == 6:
        register["B"] = register["A"] // (2**combo_op)
    elif op_code == 7:
        register["C"] = register["A"] // (2**combo_op)

    return pointer + 2, res


register = lines[0].split("\n")
register = {reg.split(" ")[1].strip(":"): int(reg.split(" ")[2]) for reg in register}

program = lines[1].split(" ")[-1].split(",")
program = [int(instruct) for instruct in program]

i = 0
ouput = []
while i < len(program):
    pointer, res = get_instruction(program[i], program[i + 1], i)
    if not res is None:
        output.append(res)
    i = pointer

print("Part 1:", ",".join(ouput))
