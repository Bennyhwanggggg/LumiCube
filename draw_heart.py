"""
Draws a heart.
"""

r = red
heart = [
    [0,0,0,0,0,0,0,0],
    [0,r,r,0,0,r,r,0],
    [r,r,r,r,r,r,r,r],
    [r,r,r,r,r,r,r,r],
    [0,r,r,r,r,r,r,0],
    [0,0,r,r,r,r,0,0],
    [0,0,0,r,r,0,0,0],
    [0,0,0,0,0,0,0,0],
]
display.set_panel("left", heart)
display.set_panel("right", heart)
display.set_panel("top", heart)