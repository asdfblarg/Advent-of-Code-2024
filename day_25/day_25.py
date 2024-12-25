with open("input.txt") as f:
    lines = f.read().split("\n\n")

schematics = [line.split("\n") for line in lines]

keys = []
locks = []
for schematic in schematics:
    schematic_grid = [list(row) for row in schematic]
    if schematic[0].startswith("#"):
        locks.append(schematic_grid)
    else:
        keys.append(schematic_grid)


lock_heights = []
for lock in locks:
    rows = len(lock)
    cols = len(lock[0])

    heights = [-1] * cols
    for col in range(cols):
        for row in range(rows):
            if lock[row][col] == "#":
                heights[col] += 1
    lock_heights.append(heights)


key_heights = []
for key in keys:
    rows = len(key)
    cols = len(key[0])

    heights = [-1] * cols
    for col in range(cols):
        for row in range(rows):
            if key[row][col] == "#":
                heights[col] += 1
    key_heights.append(heights)


def check_pins(lock_height, key_height, height):
    cols = len(lock_height)
    for i in range(cols):
        if lock_height[i] + key_height[i] > height:
            return False
    return True


height_check = len(locks[0]) - 2

sum_fits = 0
for lock_height in lock_heights:
    for key_height in key_heights:
        pin_check = check_pins(lock_height, key_height, height_check)
        if pin_check:
            sum_fits += 1

print("Part 1:", sum_fits)
