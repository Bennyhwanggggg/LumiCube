"""
Autumn animation (tree, moon, and falling leaves).
"""
import random


r = red

sakura_leave = hsv_colour(0.82, 0.3, 1)
sakura_pink = hsv_colour(0.83, 0.1, 1)
flower_pink = hsv_colour(0.94, 0.6, 1)
purple = hsv_colour(0.83, 0.4, 1)
brown = hsv_colour(0.04, 0.7, 0.3)
white = hsv_colour(0, 0, 1)
top = [
    [0, r, 0, r, 0, 0, 0, 0],
    [r, r, r, r, r, 0, 0, 0],
    [0, r, r, r, 0, 0, sakura_pink, purple],
    [0, 0, r, 0, sakura_pink, sakura_pink, sakura_pink, sakura_pink],
    [0, 0, 0, sakura_pink, sakura_pink, purple, sakura_pink, sakura_pink],
    [0, 0, 0, sakura_pink, sakura_pink, sakura_pink, sakura_pink, sakura_pink],
    [0, 0, sakura_pink, sakura_pink, purple, sakura_pink, sakura_leave, sakura_pink],
    [0, 0, sakura_pink, sakura_pink, sakura_pink, sakura_pink, sakura_pink, sakura_pink],
]
left = [
    [0, 0, sakura_pink, sakura_pink, sakura_leave, sakura_pink, purple, sakura_pink],
    [0, 0, 0, purple, sakura_pink, sakura_pink, sakura_pink, sakura_pink],
    [0, 0, 0, 0, 0, sakura_pink, sakura_pink, sakura_leave],
    [0, 0, 0, 0, 0, 0, 0, brown],
    [0, 0, 0, 0, 0, 0, 0, brown],
    [0, 0, 0, 0, 0, 0, 0, brown],
    [0, 0, 0, 0, 0, 0, 0, brown],
    [0, 0, 0, 0, 0, 0, brown, brown],
]
right = [
    [sakura_pink, purple, sakura_pink, sakura_leave, sakura_pink, sakura_pink, 0, 0],
    [sakura_pink, sakura_pink, sakura_pink, sakura_pink, purple, 0, 0, 0],
    [sakura_leave, sakura_pink, sakura_pink, 0, 0, 0, 0, 0],
    [brown, 0, 0, 0, 0, 0, 0, 0],
    [brown, 0, 0, 0, 0, 0, 0, 0],
    [brown, 0, 0, 0, 0, 0, 0, 0],
    [brown, 0, 0, 0, 0, 0, 0, 0],
    [brown, brown, 0, 0, 0, 0, 0, 0],
]
display.set_panel('left', left)
display.set_panel('right', right)
display.set_panel('top', top)

# Animation of leaves falling to the floor
leaves = {}
leaves_color = [flower_pink, sakura_leave, sakura_pink]
while True:
    # 30% chance of creating a new falling leaf
    if random.random() < 0.3:
        # Start at a random point on the tree
        sakura_leave = 7
        x = random.randint(2,6)
        if (random.random() < 0.5):
            x += 8
        leaves[(x, sakura_leave)] = random.choice(leaves_color)

    # Move all the falling leaves
    leds = {}
    new_leaves = {}
    for (x, sakura_leave), colour in leaves.items():
        if sakura_leave > 0:
            # If the leaf has moved, set the LED back to the original image
            if x < 8:
                leds[(x, sakura_leave)] = left[7 - sakura_leave][x]
            else:
                leds[(x, sakura_leave)] = right[7 - sakura_leave][x - 8]
            # Move the leaf side to side as it falls
            if sakura_leave % 2 == 0:
                x = x + 1
            else:
                x = x - 1
            # Move the leaf down
            new_leaves[(x, sakura_leave - 1)] = colour

    leaves = new_leaves
    leds.update(leaves)
    display.set_leds(leds)
    time.sleep(0.2)
