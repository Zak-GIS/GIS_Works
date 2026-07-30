from math import pi

class BaseSpatialObject:
    def __init__(self, object_id, name, x, y):
        self.object_id = object_id
        self.name = name
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

class WeatherStation(BaseSpatialObject):
    def __init__(self, object_id, name, x, y, temperature):
        super().__init__(object_id, name, x, y)
        self.temperature = temperature

class CellTower(BaseSpatialObject):
    def __init__(self, object_id, name, x, y, signal_range_km):
        super().__init__(object_id, name, x, y)
        self.signal_range_km = signal_range_km

class SpatialNetwork:
    def __init__(self, network_name):
        self.network_name = network_name
        self.objects = []

    def add_object(self, spatial_object):
        self.objects.append(spatial_object)

    def get_weather_stations(self):
        return [obj for obj in self.objects if isinstance(obj, WeatherStation)]

    def get_total_coverage_area(self):
        return sum([pi * (obj.signal_range_km ** 2) for obj in self.objects if isinstance(obj, CellTower)])

# Создаём метеостанции
ws1 = WeatherStation("WS01", "Tokyo Central", 35.68, 139.76, 22.5)
ws2 = WeatherStation("WS02", "Kyoto North", 35.01, 135.76, 18.0)

# Создаём вышки связи
ct1 = CellTower("CT01", "Shibuya Station Tower", 35.65, 139.70, signal_range_km=5)
ct2 = CellTower("CT02", "Shinjuku Hub", 35.69, 139.70, signal_range_km=10)

# Собираем сеть
net = SpatialNetwork("Tokyo Metropolitan Network")
net.add_object(ws1)
net.add_object(ws2)
net.add_object(ct1)
net.add_object(ct2)

# Проверяем работу фильтрации
stations = net.get_weather_stations()
print([st.name for st in stations]) 
# Ожидаем: ['Tokyo Central', 'Kyoto North']

# Проверяем расчёт площади (3.14 * 5^2 + 3.14 * 10^2 = 78.5 + 314 = 392.5)
print(net.get_total_coverage_area()) 
# Ожидаем: 392.5