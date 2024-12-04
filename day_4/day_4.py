with open("input.txt") as f:
    lines = f.readlines()

graph = [list(line.strip()) for line in lines]

rows = len(graph)
cols = len(graph[0])

horizontal_counts = 0
for row_num in range(rows):
    row = graph[row_num]
    for i in range(cols - 3):
        window = "".join(row[i : i + 4])
        if window in ["XMAS", "SAMX"]:
            horizontal_counts += 1

vertical_counts = 0
for col_num in range(cols):
    col = ""
    for row in range(rows):
        col += graph[row][col_num]

    for i in range(rows - 3):
        window = "".join(col[i : i + 4])
        if window in ["XMAS", "SAMX"]:
            vertical_counts += 1

diagonal_counts = 0
for i in range(rows - 3):
    for j in range(cols - 3):
        window = ""
        window += graph[i][j]
        window += graph[i + 1][j + 1]
        window += graph[i + 2][j + 2]
        window += graph[i + 3][j + 3]

        window_reverse = ""
        window_reverse += graph[i][cols - 1 - j]
        window_reverse += graph[i + 1][cols - 2 - j]
        window_reverse += graph[i + 2][cols - 3 - j]
        window_reverse += graph[i + 3][cols - 4 - j]

        if window in ["XMAS", "SAMX"]:
            diagonal_counts += 1

        if window_reverse in ["XMAS", "SAMX"]:
            diagonal_counts += 1

total_counts = horizontal_counts + vertical_counts + diagonal_counts
print("part 1:", total_counts)

# part 2

x_counts = 0
for i in range(rows - 2):
    for j in range(cols - 2):
        window = ""
        window += graph[i][j]
        window += graph[i + 1][j + 1]
        window += graph[i + 2][j + 2]

        window_reverse = ""

        window_reverse += graph[i][j + 2]
        window_reverse += graph[i + 1][j + 1]
        window_reverse += graph[i + 2][j]

        if window in ["MAS", "SAM"] and window_reverse in ["MAS", "SAM"]:
            x_counts += 1

print("part 2:", x_counts)
