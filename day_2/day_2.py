import pandas as pd
input_df = pd.read_csv("input.txt", names=["levels"])
input_df["levels"] = input_df["levels"].str.split(" ").apply(lambda x: [int(num) for num in x])

def check_all_increasing_or_decreasing(level):
    all_increasing = True
    all_decreasing = True
    for i in range(1, len(level)):
        if level[i-1] > level[i]:
            all_increasing = False
            
        if level[i-1] < level[i]:
            all_decreasing = False
    return all_increasing or all_decreasing

def check_diff(level):
    for i in range(1, len(level)):
        if not 1 <= abs(level[i-1] - level[i]) <= 3:
            return False
    return True


input_df["all_incr_decre"] = input_df["levels"].apply(check_all_increasing_or_decreasing)
input_df["diff_ok"] = input_df["levels"].apply(check_diff)
input_df["level_safe"] = input_df["all_incr_decre"] & input_df["diff_ok"]

print(len(input_df[input_df["level_safe"]]))

def check_diff_damper(level):
    for i in range(len(level)):
        new_level = level.copy()
        new_level.pop(i)
        all_incr_decre = check_all_increasing_or_decreasing(new_level)
        diff_ok = check_diff(new_level)
        if all_incr_decre and diff_ok:
            return True
    return False

input_df["level_damper_safe"] = input_df["levels"].apply(check_diff_damper)
print(len(input_df[input_df["level_damper_safe"]]))
