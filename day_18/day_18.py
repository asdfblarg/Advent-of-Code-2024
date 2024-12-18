from collections import deque

with open("input.txt") as f:
    lines = f.read().split("\n")

coords = [line.split(",") for line in lines]
coords = [(int(coord[1]), int(coord[0])) for coord in coords]


rows = cols = 70 + 1
grid = [["." for i in range(rows)] for j in range(cols)]


def bfs_shortest_path(grid, rows, cols):
    queue = deque()
    queue.append((0, 0, 0))
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited = {}
    while queue:
        x, y, steps = queue.popleft()
        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]
            new_steps = steps + 1
            if 0 <= new_x < rows and 0 <= new_y < rows and grid[new_x][new_y] != "#":
                if (new_x, new_y) not in visited:
                    visited[(new_x, new_y)] = new_steps
                    queue.append((new_x, new_y, new_steps))

    return visited.get((rows - 1, cols - 1), -1)


mem_space = grid.copy()
for coord in coords[:1024]:
    x, y = coord
    mem_space[x][y] = "#"

shortest_path = bfs_shortest_path(mem_space, rows, cols)
print("Part 1:", shortest_path)

# Part 2
#


def run_coords(num_coords):
    mem_space = [["." for i in range(rows)] for j in range(cols)]
    for coord in coords[:num_coords]:
        x, y = coord
        mem_space[x][y] = "#"

    shortest_path = bfs_shortest_path(mem_space, rows, cols)
    return shortest_path


left = 1
right = len(coords) - 1

while left < right:
    mid = (right + left) // 2
    shortest_path = run_coords(mid)
    if shortest_path == -1:
        right = mid - 1
    else:
        left = mid + 1

last_coord = coords[left]
x, y = last_coord
print("Part 2:", f"{y},{x}")
