from .base import BaseTrafficSensor

class SpeedCamera(BaseTrafficSensor):
    def __init__(self, sensor_id, location, is_active, speed_limit, current_speed):
        super().__init__(sensor_id, location, is_active)
        self.speed_limit = speed_limit
        self.current_speed = current_speed

    def is_speeding(self):
        return (self.current_speed > self.speed_limit) and self.is_active

class TrafficDensitySensor(BaseTrafficSensor):
    def __init__(self, sensor_id, location, is_active, cars_per_minute):
        super().__init__(sensor_id, location, is_active)
        self.cars_per_minute = cars_per_minute

    def is_congested(self):
        return (self.cars_per_minute > 50) and self.is_active

