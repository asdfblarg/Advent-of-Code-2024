from collections import deque

with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0])

for i in range(rows):
    for j in range(cols):
        grid[i][j] = int(grid[i][j]) if grid[i][j] != "." else -1

def get_trailheads(grid):
    trailheads = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                trailheads.add((0, i, j))
    return trailheads

def get_trail_score_and_rating(trailhead):
    queue = deque()
    queue.append(tuple(trailhead))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    count = 0
    peak = set()
    while queue:
        height, x, y = queue.popleft()
        if height == 9:
            peak.add((height, x, y))
            count += 1
            continue
        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]
            if 0 <= new_x < rows and 0 <= new_y < cols:
                new_height = grid[new_x][new_y]
                if new_height == height + 1:
                    queue.append((new_height, new_x, new_y))

    return len(peak), count


trailheads = get_trailheads(grid)

total_score = 0
total_rating = 0
for trailhead in trailheads:
    score, rating = get_trail_score_and_rating(trailhead)
    total_score += score
    total_rating += rating

print("Part 1:", total_score)
print("Part 2:", total_rating)
