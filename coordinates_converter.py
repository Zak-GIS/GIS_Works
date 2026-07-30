import math 

def deg_to_rad(degrees):
    rad = degrees * (math.pi/180)
    return rad

rad1 = math.radians(180)
rad2 = deg_to_rad(180)

print(f'rad1 is {rad1}\nrad2 is {rad2}')
