from collections import Counter

with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

stones = lines[0].split(" ")
stones = [int(stone) for stone in stones]


def stone_blink(stones_counter):
    new_stones = Counter()
    for stone in stones_counter:
        if stone == 0:
            new_stones[1] += stones_counter[stone]
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            stone_digit_len = len(stone_str)
            new_stones[int(stone_str[: stone_digit_len // 2])] += stones_counter[stone]
            new_stones[int(stone_str[stone_digit_len // 2 :])] += stones_counter[stone]
        else:
            new_stones[stone * 2024] += stones_counter[stone]

    return new_stones


new_stones = Counter(stones)
for i in range(25):
    new_stones = stone_blink(new_stones)

print("Part 1:", sum(new_stones.values()))

# part 2

new_stones = Counter(stones)
for i in range(75):
    new_stones = stone_blink(new_stones)
print("Part 2:", sum(new_stones.values()))
