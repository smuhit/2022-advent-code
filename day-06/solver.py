data = open('input.txt').read()

# Part 1
for i in range(len(data) - 4):
    if len(set(data[i:i+4])) == 4:
        break

print(i+4)

# Part 2
for i in range(len(data) - 14):
    if len(set(data[i:i+14])) == 14:
        break

print(i+14)
