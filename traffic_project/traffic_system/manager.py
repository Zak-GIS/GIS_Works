from .sensors import TrafficDensitySensor, SpeedCamera

class TrafficManager:
    def __init__(self, city_name):
        self.city_name = city_name
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def get_speeding_locations(self):
        return [sensor.location for sensor in self.sensors 
                if isinstance(sensor, SpeedCamera) and sensor.is_speeding()]

    def get_congested_sensors(self):
        return [sensor for sensor in self.sensors 
                if isinstance(sensor, TrafficDensitySensor) and sensor.is_congested()]