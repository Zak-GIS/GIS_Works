some_points = ((1.0, 2.0), (10.0, 5.0), (7.0, 7.0), (8.123, 2.2), (9.023, 3.89))
distance = 0
answer = ()

for dis in some_points:
    current_distance = (dis[0] ** 2 + dis[1] ** 2) ** (1/2)
    if distance <= current_distance:
        distance =  current_distance
        answer = dis

print(f"Расстояние от точки {answer} до точки (0, 0) составляет: {distance}")
