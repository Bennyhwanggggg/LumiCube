"""
Draw an image with a caption on the screen.
Note: Requires the advanced kit screen module.
"""

screen.resolution_scaling = 1
screen.draw_image("autumn.jpg")
screen.draw_rectangle(0, 150, 320, 52, black)
screen.write_text(96, 158, "Autumn", 2, black, white)
