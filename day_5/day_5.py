from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

for i in range(len(lines)):
    if lines[i] == "":
        break_index = i

rules = lines[:break_index]

orders = lines[break_index + 1 :]
orders = [order.split(",") for order in orders]

rules_dict = defaultdict(list)
for rule in rules:
    x, y = rule.split("|")
    rules_dict[x].append(y)
rules_dict


def check(order):
    prev_pages = set()
    for i, page_num in enumerate(order):
        for bad_page in rules_dict[page_num]:
            if bad_page in prev_pages:
                return False
        prev_pages.add(page_num)
    return True


sum_middle = 0
for order in orders:
    if check(order):
        middle_page = len(order) // 2
        sum_middle += int(order[middle_page])

print("Part 1:", sum_middle)


# part 2

bad_orders = []
for order in orders:
    if not check(order):
        bad_orders.append(order)
bad_orders


def get_bad_pages(order):
    prev_pages = {}
    for i, page_num in enumerate(order):
        for bad_page in rules_dict[page_num]:
            if bad_page in prev_pages:
                return (prev_pages[bad_page], i)

        prev_pages[page_num] = i


corrected_bad_orders = []
for order in bad_orders:
    while not check(order):
        x, y = get_bad_pages(order)
        order[x], order[y] = order[y], order[x]
    corrected_bad_orders.append(order)

sum_middle = 0
for order in corrected_bad_orders:
    if check(order):
        middle_page = len(order) // 2
        sum_middle += int(order[middle_page])

print("Part 2:", sum_middle)
