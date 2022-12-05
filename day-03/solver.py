data = open('input.txt').read().split()

# Part 1
priorities = []
for datum in data:
    val = (set(datum[:len(datum)//2]).intersection(set(datum[len(datum)//2:]))).pop()
    priority = ord(val) - ord('a') + 1
    if priority < 0:
        priority = ord(val) - ord('A') + 27
    priorities.append(priority)

print(sum(priorities))

# Part 2
priorities = []
for i in range(0, len(data), 3):
    val = (set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2]))).pop()
    priority = ord(val) - ord('a') + 1
    if priority < 0:
        priority = ord(val) - ord('A') + 27
    priorities.append(priority)

print(sum(priorities))
