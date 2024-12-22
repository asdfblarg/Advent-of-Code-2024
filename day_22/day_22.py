with open("input.txt") as f:
    lines = f.read().split("\n")

secrets = [int(line) for line in lines]


def mix(secret, mix):
    return secret ^ mix


def prune(secret):
    return secret % 16777216


def get_next_secret(secret):
    secret = mix(secret, secret * 64)
    secret = prune(secret)
    secret = mix(secret, secret // 32)
    secret = prune(secret)
    secret = mix(secret, secret * 2048)
    secret = prune(secret)

    return secret


sum_new_secrets = 0
for secret in secrets:
    new_secret = secret
    for i in range(2000):
        new_secret = get_next_secret(new_secret)

    #     print(f"{secret}: {new_secret}")
    sum_new_secrets += new_secret

print("Part 1:", sum_new_secrets)


def gen_differences_list(secret, num_seq):
    bananas_list = []
    for i in range(num_seq):
        bananas_list.append(secret % 10)
        secret = get_next_secret(secret)

    bananas_diff_list = []
    for i in range(len(bananas_list) - 1):
        diff = bananas_list[i + 1] - bananas_list[i]
        bananas_diff_list.append((diff, bananas_list[i + 1]))

    return bananas_diff_list


total_diff_seq = set()
secret_diff_seq_dicts = {}
for secret in secrets:
    bananas_diffs = gen_differences_list(secret, 2000)
    diff_seq_dict = {}
    for i in range(len(bananas_diffs) - 3):
        diff_seq = tuple(diff[0] for diff in bananas_diffs[i : i + 4])
        if diff_seq not in diff_seq_dict:
            diff_seq_dict[diff_seq] = bananas_diffs[i + 3][1]

    for diff_seq in diff_seq_dict.keys():
        total_diff_seq.add(diff_seq)

    secret_diff_seq_dicts[secret] = diff_seq_dict


max_bananas = 0
for diff_seq in total_diff_seq:
    sum_bananas = 0
    for secret in secrets:
        secret_diff_seq_dict = secret_diff_seq_dicts.get(secret, {})
        sum_bananas += secret_diff_seq_dict.get(diff_seq, 0)

    max_bananas = max(max_bananas, sum_bananas)


print("Part 2:", max_bananas)
