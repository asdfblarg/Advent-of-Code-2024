with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
disk_map = lines[0]

def split_into_ids(disk_map):
    id_space_map = []
    block_id = 0
    for i in range(len(disk_map)):
        # odd digits are files
        num_bytes = int(disk_map[i])
        if i % 2 == 0:
            for j in range(num_bytes):
                id_space_map.append(str(block_id))
            block_id += 1
        # even digits are free blocks
        else:
            for j in range(num_bytes):
                id_space_map.append(".")

    return id_space_map


disk_map_shrink = split_into_ids(disk_map)
left = 0
right = len(disk_map_shrink) - 1

# 2 pointers approach to swapping disks
while left < right:
    # move left to next free block from the front
    while disk_map_shrink[left] != ".":
        left += 1
    # move right next id block from the end
    while disk_map_shrink[right] == ".":
        right -= 1

    # perform swap if pointers are still valid
    if left < right:
        disk_map_shrink[left], disk_map_shrink[right] = disk_map_shrink[right], disk_map_shrink[left]

# calcuate checksum
checksum = 0
for i in range(len(disk_map_shrink)):
    if disk_map_shrink[i] == ".":
        continue
    checksum += i * int(disk_map_shrink[i])
checksum

print("Part 1:", checksum)

# Part 2
#

# get next free block start index and block size up until right index
# returns -1 if not found
def get_next_free_block(disk_map, left_index, right):
    block_size = 0
    while disk_map[left_index] != "." and left_index < right:
        left_index += 1

    if left_index >= right:
        return -1, -1

    start_index = left_index
    while disk_map[left_index] == ".":
        block_size += 1
        left_index += 1
        
    return start_index, block_size

# reset disk_map
disk_map_shrink_2 = split_into_ids(disk_map)

# set up file_ids_map and file_ids_size_map to store
# every file_id and the starting index and block size
file_ids_map = {}
file_ids_size_map = {}

i = 0
cur_id = "0"
cur_count = 0
cur_start = 0
while i < len(disk_map_shrink_2):
    if disk_map_shrink_2[i] != ".":
        if int(disk_map_shrink_2[i]) not in file_ids_map:
            file_ids_map[int(disk_map_shrink_2[i])] = i
            file_ids_size_map[int(disk_map_shrink_2[i])] = 1
        else:
            file_ids_size_map[int(disk_map_shrink_2[i])] += 1
    i += 1

# condense filesystem blocks
for file_id in range(len(file_ids_map) - 1, -1, -1):
    file_id_index = file_ids_map[file_id]
    file_id_size = file_ids_size_map[file_id]
    
    # find next free block space with enough size
    free_index, free_blocks = get_next_free_block(disk_map_shrink_2, 0, file_id_index)
    if free_index != -1:
        # if there are not enough blocks, keep checking further ahead
        while free_blocks < file_id_size:
            free_index, free_blocks = get_next_free_block(
                disk_map_shrink_2, free_index + free_blocks, file_id_index
            )
            if free_index == -1:
                break
    # give up if not enough free blocks exist
    if free_index == -1:
        continue

    # perform swap
    for i in range(file_id_size):
        disk_map_shrink_2[free_index + i] = str(file_id)
        disk_map_shrink_2[file_id_index + i] = "."

# calcuate checksum
checksum = 0
for i in range(len(disk_map_shrink_2)):
    if disk_map_shrink_2[i] == ".":
        continue
    checksum += i * int(disk_map_shrink_2[i])

print("Part 2:", checksum)
