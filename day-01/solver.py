data = open('input.txt').read().split('\n')

# Part 1
calories = []
count = 0
for datum in data:
    if datum == '':
        calories.append(count)
        count = 0
    else:
        count += int(datum)

print(max(calories))

# Part 2
print(sum(sorted(calories, reverse=True)[0:3]))
