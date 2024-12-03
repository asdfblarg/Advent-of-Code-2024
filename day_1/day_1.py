from collections import Counter
import pandas as pd

# Part 1

input_df = pd.read_csv("input.txt", sep="\s+", names=["list_1", "list_2"])

list_1 = sorted(input_df["list_1"].to_list())
list_2 = sorted(input_df["list_2"].to_list())

diff = []
for i in range(len(list_1)):
    diff.append(abs(list_1[i] - list_2[i]))

part_1_ans = sum(diff)
print("Part 1:", part_1_ans)

# Part 2

list_2_counts = Counter(list_2)

similarities = []
for i in range(len(list_1)):
    list_id = list_1[i]
    similarities.append(list_id * list_2_counts[list_id])

part_2_ans = sum(similarities)
print("Part 2:", part_2_ans)
