"""
Use the air pressure sensor as a digital barometer.
Note: Requires the advanced kit interactive add-on.
"""


display.set_all(black)
while True:
    if env_sensor.pressure > 102000:
        display.scroll_text("Fair", yellow)
    elif env_sensor.pressure > 99000:
        display.scroll_text("Change", white)
    else:
        display.scroll_text("Rain", blue)
    time.sleep(20)
