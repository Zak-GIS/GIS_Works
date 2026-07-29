from functools import reduce
elevations = [120, 150, 110, 180, 200, 190, 140, 210, 95, 175]

#Finding the minimum, maximum, and average height through cycles
min_height = elevations[0]
max_height = elevations[0]
average_height = reduce(lambda x, y: x + y, elevations) / len(elevations)

for value in elevations:
    if min_height > value:
        min_height = value
    if max_height < value:
        max_height = value

print(f"Минимальная высота: {min_height}\nМаксимальная высота: {max_height}\nСредняя высота: {average_height}")
