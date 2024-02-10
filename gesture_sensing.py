"""
Swipe your finger up or down (just below the buttons) to turn the cube red or blue.
Note: Requires the advanced kit gesture sensor module.
"""

while True:
    gesture = light_sensor.get_next_gesture(100)
    if gesture == "up":
        display.set_all(blue)
    elif gesture == "down":
        display.set_all(red)
