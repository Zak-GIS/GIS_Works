class BaseTrafficSensor:
    def __init__(self, sensor_id, location, is_active):
        self.sensor_id = sensor_id
        self.location = location
        self.is_active = is_active

    def get_info(self):
        return f"Sensor {self.sensor_id} at {self.location} - {self.is_active}"
