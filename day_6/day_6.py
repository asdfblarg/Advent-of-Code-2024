# 2024 day 6

with open("input.txt") as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]

rows = len(grid)
cols = len(grid[0])


def print_grid(grid):
    fin = []
    for row in grid:
        fin.append("".join(row))

    print("\n".join(fin))

# returns guard x and y pos and direction char
def find_guard(grid):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in "^v<>":
                return (i, j, grid[i][j])
    return -1


directions = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}
facings = {
    (-1, 0): "^",
    (1, 0): "v",
    (0, 1): ">",
    (0, -1): "<",
}

next_direction = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}

guard_x, guard_y, facing = find_guard(grid)
direction = directions[facing]
guard_x, guard_y, direction


# simulate guard

while True:
    # get next position
    new_x, new_y = guard_x + direction[0], guard_y + direction[1]

    # end loop if next step is out of bounds
    if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
        grid[guard_x][guard_y] = "X"
        break

    # while next position is a barrier, rotate once
    # keep rotating until you can move forward again tp get out of edge case
    while grid[new_x][new_y] == "#":
        facing = next_direction[facing]
        direction = directions[facing]
        new_x, new_y = guard_x + direction[0], guard_y + direction[1]

    # update grid and move guard to new position
    grid[new_x][new_y] = facings[direction]
    grid[guard_x][guard_y] = "X"
    guard_x, guard_y = new_x, new_y

# count X's left in the final grid
# collect X's pos for part 2
count_x = 0
x_coords = set()
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "X":
            count_x += 1
            x_coords.add((i,j))

part_1_ans = count_x

print("Part 1:", part_1_ans)

# Part 2
#

# reset grid to orig grid to get rid of initial guard position
potential_obstacles = x_coords
grid = [list(line.strip()) for line in lines]
guard_x, guard_y, facing = find_guard(grid)
direction = directions[facing]

potential_obstacles.remove((guard_x, guard_y))


# brute force check for valid obstacles along orig path
valid_obstacles_count = 0
for obstacle in potential_obstacles:
   
    # reset grid
    grid = [list(line.strip()) for line in lines]
    guard_x, guard_y, facing = find_guard(grid)
    direction = directions[facing]

    grid[obstacle[0]][obstacle[1]] = "O"
    
    # keep track of guard path and direct to detect cycle
    cycle_set = set()

    while True:
        # get next position
        new_x, new_y = guard_x + direction[0], guard_y + direction[1]

        # stop and add to count if we find guard in same position and directio
        # this means that the guard has reached a cycle
        if (guard_x, guard_y, direction) in cycle_set:
            valid_obstacles_count += 1
            break

        cycle_set.add((guard_x, guard_y, direction))

        # end loop if next step is out of bounds
        if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
            grid[guard_x][guard_y] = "X"
            break

        # while next position is a barrier, rotate once
        # keep rotating until you can move forward again tp get out of edge case
        while grid[new_x][new_y] == "#" or grid[new_x][new_y] == "O":
            facing = next_direction[facing]
            direction = directions[facing]
            new_x, new_y = guard_x + direction[0], guard_y + direction[1]

        # update grid and move guard to new position
        grid[new_x][new_y] = facings[direction]
        grid[guard_x][guard_y] = "X"
        guard_x, guard_y = new_x, new_y

print("part 2:", valid_obstacles_count)
