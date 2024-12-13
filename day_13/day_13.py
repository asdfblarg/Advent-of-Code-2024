with open("input.txt") as f:
    lines = f.read().split("\n\n")
lines = [line.split("\n") for line in lines]


machines = []
for line in lines:
    button_a = line[0]
    button_a = button_a.split(": ")[-1].split(", ")
    button_a = [int(pos.split("+")[-1]) for pos in button_a]

    button_b = line[1]
    button_b = button_b.split(": ")[-1].split(", ")
    button_b = [int(pos.split("+")[-1]) for pos in button_b]

    prize = line[2]
    prize = prize.split(": ")[-1].split(", ")
    prize = [int(pos.split("=")[-1]) for pos in prize]
    machines.append((button_a, button_b, prize))


def calc_machine_coins(machine):
    a = machine[0]
    b = machine[1]
    prize = machine[2]

    # systems of equations
    b_rounds = ((a[0] * prize[1]) - (a[1] * prize[0])) / ((a[0] * b[1]) - (a[1] * b[0]))
    a_rounds = (prize[0] - (b[0] * b_rounds)) / a[0]
    if a_rounds == int(a_rounds) and b_rounds == int(b_rounds):
        a_rounds = int(a_rounds)
        b_rounds = int(b_rounds)
        return a_rounds, b_rounds

    return 0, 0


total_coins = 0
for machine in machines:
    a_rounds, b_rounds = calc_machine_coins(machine)
    total_coins += 3 * a_rounds + b_rounds

print("Part 1:", total_coins)

# Part 2
#


def calc_machine_coins_2(machine):
    a = machine[0]
    b = machine[1]
    prize = machine[2]
    prize = 10000000000000 + prize[0], 10000000000000 + prize[1]

    # systems of equations
    b_rounds = ((a[0] * prize[1]) - (a[1] * prize[0])) / ((a[0] * b[1]) - (a[1] * b[0]))
    a_rounds = (prize[0] - (b[0] * b_rounds)) / a[0]
    if a_rounds == int(a_rounds) and b_rounds == int(b_rounds):
        a_rounds = int(a_rounds)
        b_rounds = int(b_rounds)
        return a_rounds, b_rounds

    return 0, 0


total_coins_2 = 0
for machine in machines:
    a_rounds, b_rounds = calc_machine_coins_2(machine)
    total_coins_2 += 3 * a_rounds + b_rounds

print("Part 1:", total_coins_2)
