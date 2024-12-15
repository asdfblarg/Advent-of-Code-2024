from collections import Counter

with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
lines = [line.split(" ") for line in lines]

rows = 103
cols = 101

positions = []
velocities = []
for line in lines:
    pos_split = line[0].split("=")[-1].split(",")
    positions.append((int(pos_split[1]), int(pos_split[0])))
    vel_split = line[1].split("=")[-1].split(",")
    velocities.append((int(vel_split[1]), int(vel_split[0])))


def print_robot_positions(positions, rows, cols):
    position_count = Counter(positions)
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        grid.append(row)

    for i in range(rows):
        for j in range(cols):
            if (i, j) in position_count:
                grid[i][j] = position_count[(i, j)]

    img_str = ""
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] > 0:
                img_str += str(grid[i][j])
            else:
                img_str += "."

        img_str += "\n"
    return img_str


def update_positions(positions, velocities, rows, cols):
    for i in range(len(positions)):
        new_x = (positions[i][0] + velocities[i][0]) % rows
        new_y = (positions[i][1] + velocities[i][1]) % cols
        positions[i] = (new_x, new_y)
    return positions


def calculate_safety(positions, rows, cols):
    mid_x = rows // 2
    mid_y = cols // 2

    quad_1 = 0
    quad_2 = 0
    quad_3 = 0
    quad_4 = 0
    for pos in positions:
        if 0 <= pos[0] < mid_x and 0 <= pos[1] < mid_y:
            quad_1 += 1
        if 0 <= pos[0] < mid_x and mid_y < pos[1] < cols:
            quad_2 += 1
        if mid_x < pos[0] < rows and 0 <= pos[1] < mid_y:
            quad_3 += 1
        if mid_x < pos[0] < rows and mid_y < pos[1] < cols:
            quad_4 += 1

    return quad_1 * quad_2 * quad_3 * quad_4


new_positions = positions.copy()
for i in range(100):
    new_positions = update_positions(new_positions, velocities, rows, cols)
    # img_str = print_robot_positions(new_positions, rows, cols)

part_1_ans = calculate_safety(new_positions, rows, cols)

print("Part 1:", part_1_ans)

# Part 2
#


new_positions = positions.copy()
safetys = []
for i in range(101 * 103):
    new_positions = update_positions(new_positions, velocities, rows, cols)
    img_str = print_robot_positions(new_positions, rows, cols)

    # originally found the tree manually, but programatically,
    # the intuition is that the tree will have the lowest safety
    safety = calculate_safety(new_positions, rows, cols)
    safetys.append((i + 1, safety))

safetys.sort(key=lambda x: x[1])

print("Part 2:", safetys[0][0])
