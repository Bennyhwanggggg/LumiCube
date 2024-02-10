"""
Draws a rainbow pattern.
"""

leds = {}
for y in range(16):
    for x in range(16):
        if x < 8 or y < 8:
            leds[x, y] = hsv_colour((x+y)/24, 1, 1)
display.set_leds(leds)
