with open("input.txt") as f:
    lines = f.read().split("\n\n")
lines = [line.split("\n") for line in lines]


machines = []
for line in lines:
    # TODO: clean this up with regex parsing or something
    button_a = line[0].split(": ")[-1].split(", ")
    button_a = [int(pos.split("+")[-1]) for pos in button_a]

    button_b = line[1].split(": ")[-1].split(", ")
    button_b = [int(pos.split("+")[-1]) for pos in button_b]

    prize = line[2].split(": ")[-1].split(", ")
    prize = [int(pos.split("=")[-1]) for pos in prize]

    machines.append((button_a, button_b, prize))


def calc_machine_coins(machine, part_2=False):
    a = machine[0]
    b = machine[1]
    prize = machine[2]
    if part_2:
        prize = 10000000000000 + prize[0], 10000000000000 + prize[1]

    # systems of equations
    b_rounds = ((a[0] * prize[1]) - (a[1] * prize[0])) / ((a[0] * b[1]) - (a[1] * b[0]))
    a_rounds = (prize[0] - (b[0] * b_rounds)) / a[0]

    # if return ints if both a and b rounds are whole numbers
    if a_rounds == int(a_rounds) and b_rounds == int(b_rounds):
        return int(a_rounds), int(b_rounds)

    return 0, 0


total_coins = 0
for machine in machines:
    a_rounds, b_rounds = calc_machine_coins(machine)
    total_coins += 3 * a_rounds + b_rounds

print("Part 1:", total_coins)

# Part 2
#

total_coins_2 = 0
for machine in machines:
    a_rounds, b_rounds = calc_machine_coins(machine, part_2=True)
    total_coins_2 += 3 * a_rounds + b_rounds

print("Part 1:", total_coins_2)
