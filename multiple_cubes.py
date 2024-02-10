"""
First configure the IP addresses for a pair of cubes - then you can control the colour of one with the orientation
of the other.
"""

cube1 = LumiCube("192.168.0.11")
cube2 = LumiCube("192.168.0.12")

while True:
    colour1 = hsv_colour(cube2.imu.yaw / 360, 1, 1)
    colour2 = hsv_colour(cube1.imu.yaw / 360, 1, 1)
    cube1.display.set_all(colour1)
    cube2.display.set_all(colour2)
    time.sleep(0.1)
