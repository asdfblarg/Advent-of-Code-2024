from collections import defaultdict
from itertools import combinations

with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0])


def print_grid(grid):
    for row in grid:
        print("".join(row))


freqs = defaultdict(list)
freqs_list = []
for i in range(rows):
    for j in range(cols):
        if grid[i][j] != ".":
            freqs[grid[i][j]].append((i, j))
            freqs_list.append((i, j))


def generate_antinodes(freq_list):
    antinodes = set()
    for combo in combinations(freq_list, 2):
        a, b = combo

        x_diff = b[0] - a[0]
        y_diff = b[1] - a[1]

        antinodes.add((b[0] + x_diff, b[1] + y_diff))
        antinodes.add((a[0] - x_diff, a[1] - y_diff))

    return antinodes


antinodes = []
for freq in freqs:
    antinodes += generate_antinodes(freqs[freq])

antinode_grid = [list(line) for line in lines]
valid_antinodes = set()
for antinode in antinodes:
    if 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
        antinode_grid[antinode[0]][antinode[1]] = "#"
        valid_antinodes.add(antinode)

print("Part 1:", len(valid_antinodes))

# Part 2
#

def generate_antinodes_2(freq_list):
    antinodes = set()
    for combo in combinations(freq_list, 2):
        a, b = combo

        x_diff = b[0] - a[0]
        y_diff = b[1] - a[1]

        cur = a
        while 0 <= cur[0] < rows and 0 <= cur[1] < cols:
            antinodes.add((cur[0] - x_diff, cur[1] - y_diff))
            cur = (cur[0] - x_diff, cur[1] - y_diff)

        cur = b
        while 0 <= cur[0] < rows and 0 <= cur[1] < cols:
            antinodes.add((cur[0] + x_diff, cur[1] + y_diff))
            cur = (cur[0] + x_diff, cur[1] + y_diff)

    return antinodes


antinodes_2 = []
for freq in freqs:
    antinodes_2 += generate_antinodes_2(freqs[freq])

antinode_grid_2 = [list(line) for line in lines]
valid_antinodes_2 = set()
for antinode in antinodes_2:
    if 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
        antinode_grid_2[antinode[0]][antinode[1]] = "#"
        valid_antinodes_2.add(antinode)

total_antinodes = valid_antinodes_2.union(set(freqs_list))

print("Part 2:", len(total_antinodes))
