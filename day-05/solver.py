raw_data = open('input.txt').read().split('\n')[:-1]

crates = {}

line = 0
while raw_data[line][:3] != ' 1 ':
    line += 1

for x in raw_data[line].split():
    crates[int(x)] = []

for i in range(line - 1, -1, -1):
    for j in range(int(x)):
        if raw_data[i][4 * j + 1] != ' ':
            crates[j + 1].append(raw_data[i][4 * j + 1])

# Part 1
from copy import deepcopy
part1_crates = deepcopy(crates)
for k in range(line + 2, len(raw_data)):
    amount, src, dest = [int(s) for s in raw_data[k].split() if s.isdigit()]
    transfer = part1_crates[src][:-amount - 1:-1]
    part1_crates[dest].extend(transfer)
    del part1_crates[src][-amount:]

for j in range(int(x)):
    print(part1_crates[j + 1][-1], end='')

print()
# Part 2
part2_crates = deepcopy(crates)
for k in range(line + 2, len(raw_data)):
    amount, src, dest = [int(s) for s in raw_data[k].split() if s.isdigit()]
    transfer = part2_crates[src][-amount:]
    part2_crates[dest].extend(transfer)
    del part2_crates[src][-amount:]

print(part2_crates)
for j in range(int(x)):
    print(part2_crates[j + 1][-1], end='')
