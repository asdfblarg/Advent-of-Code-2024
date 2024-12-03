import re

with open("input.txt") as f:
    lines = f.readlines()
    joined_lines = "".join(lines).replace("\n", "")


def calc_line_mul_sum(line):
    line_mul = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)

    line_res = []
    for mul in line_mul:
        matches = re.search(r"mul\(([0-9]+),([0-9]+)\)", mul)
        line_res.append(int(matches[1]) * int(matches[2]))

    return sum(line_res)


part_1_ans = calc_line_mul_sum(joined_lines)
print("Part 1:", part_1_ans)

cleaned_donts = re.sub(r"don't\(\).+?do\(\)", "", joined_lines)
part_2_ans = calc_line_mul_sum(cleaned_donts)

print("Part 2:", part_2_ans)
