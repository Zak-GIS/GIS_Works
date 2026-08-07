from traffic_system import SpeedCamera, TrafficDensitySensor, TrafficManager

if __name__ == '__main__':
    # 1. Создаем камеры фиксации скорости
    # Аргументы: sensor_id, location, is_active, speed_limit, current_speed
    cam1 = SpeedCamera("CAM_01", "Shibuya Crossing, Tokyo", True, speed_limit=50, current_speed=68)   # Превышение
    cam2 = SpeedCamera("CAM_02", "Shinjuku Avenue, Tokyo", True, speed_limit=60, current_speed=52)   # Норма
    cam3 = SpeedCamera("CAM_03", "Ginza Dori, Tokyo", False, speed_limit=40, current_speed=75)        # Камера неактивна

    # 2. Создаем датчики плотности трафика
    # Аргументы: sensor_id, location, is_active, cars_per_minute
    density1 = TrafficDensitySensor("DEN_01", "Rainbow Bridge, Tokyo", True, cars_per_minute=82) # Пробка (> 50)
    density2 = TrafficDensitySensor("DEN_02", "Akihabara Main Street, Tokyo", True, cars_per_minute=30) # Норма

    # 3. Инициализируем менеджер города
    manager = TrafficManager("Tokyo")

    # 4. Регистрируем датчики в системе
    manager.add_sensor(cam1)
    manager.add_sensor(cam2)
    manager.add_sensor(cam3)
    manager.add_sensor(density1)
    manager.add_sensor(density2)

    # 5. Проверяем работу фильтров
    print("Speeding locations:", manager.get_speeding_locations())
    # Ожидаемый вывод: ['Shibuya Crossing, Tokyo']

    congested_sensors = manager.get_congested_sensors()
    print("Congested sensor IDs:", [sensor.sensor_id for sensor in congested_sensors])
    # Ожидаемый вывод: ['DEN_01']