#Границы Bounding Box:

x_min, y_min = float(10), float(10)
x_max, y_max = float(50), float(50)

x_test, y_test = map(float, input("Введите координты:").split())

if (x_min <= x_test <= x_max) and (y_min <= y_test <= y_max):
    print("Точка находится внутри зоны: True")
else:
    print("Точка не находится внутри зоны: False")
