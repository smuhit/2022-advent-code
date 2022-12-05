raw_data = open('input.txt').read().split()

data = []
for line in raw_data:
    a, b = line.split(',')
    x0, x1 = a.split('-')
    y0, y1 = b.split('-')
    data.append(((int(x0), int(x1)), (int(y0), int(y1))))

# Part 1
wholly_contained = 0
for datum in data:
    x_set = set(range(datum[0][0], datum[0][1] + 1))
    y_set = set(range(datum[1][0], datum[1][1] + 1))
    if x_set - y_set == set() or y_set - x_set == set():
        wholly_contained += 1
print(wholly_contained)

# Part 2
overlaps = 0
for datum in data:
    x_set = set(range(datum[0][0], datum[0][1] + 1))
    y_set = set(range(datum[1][0], datum[1][1] + 1))
    if x_set.intersection(y_set):
        overlaps += 1
print(overlaps)
