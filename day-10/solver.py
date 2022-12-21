data = open('input.txt').read().split('\n')[:-1]

x = 1
cycles = 1

# Part 1
key_cycles = {20, 60, 100, 140, 180, 220}

strengths = 0
for datum in data:
    if cycles in key_cycles:
        strengths += x * cycles
    cycles += 1
    if y := datum[5:]:
        if cycles in key_cycles:
            strengths += x * cycles
        cycles += 1
        x += int(y)

print(strengths)       

# Part 2
x = 1
cycles = 0
crt = [[' ' for _ in range(40)] for _ in range(6)]

for datum in data:
    if abs(x - (cycles % 40)) <= 1:
        crt[cycles // 40][cycles % 40] = '#'
    cycles += 1
    if y := datum[5:]:
        if abs(x - (cycles % 40)) <= 1:
            crt[cycles // 40][cycles % 40] = '#'
        cycles += 1
        x += int(y)

for line in crt:
    for char in line:
        print(char, end='')
    print()
