path = [(0, 0), (3, 4), (6, 8), (10, 8)]
counter = 0

for i in range(len(path) - 1):
    point1 = path[i]
    point2 = path[i + 1]
    segment = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** (1/2)
    counter += segment

print(counter)