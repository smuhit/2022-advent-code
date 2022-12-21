data = open('input.txt').read().split('\n')[:-1]

x = 1
cycles = 1

# Part 1
key_cycles = {20, 60, 100, 140, 180, 220}

strengths = 0
for datum in data:
    if cycles in key_cycles:
        strengths += x * cycles
    if datum == 'noop':
        cycles += 1
    else:
        _, y = datum.split(' ')
        if cycles + 1 in key_cycles:
            strengths += x * (cycles + 1)
        cycles += 2
        x += int(y)

print(strengths)       

# Part 2
x = 1
cycles = 0
crt = [[' ' for _ in range(40)] for _ in range(6)]

for datum in data:
    if abs(x - (cycles % 40)) <= 1:
        crt[cycles // 40][cycles % 40] = '#'
    if datum == 'noop':
        cycles += 1
    else:
        _, y = datum.split(' ')
        cycles += 1
        if abs(x - (cycles % 40)) <= 1:
            crt[cycles // 40][cycles % 40] = '#'
        cycles += 1
        x += int(y)

for line in crt:
    for char in line:
        print(char, end='')
    print()
