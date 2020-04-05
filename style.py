# style.py
#
# When the main loop renders a scene, it calls a function for each point which returns a pygame.Surface. 
# Then every pygame.Surface object is rendered, the furthest ones are rendered first, the closest ones 
# are rendered last. 
# 
# This module contains functions which can be called for each point. Each one must return pygame.Surface 
# and takes a single point as a parameter. A point is represented by a list: [X, Y, Z, (Red, Green, Blue)].
#
# STYLE_FUNCTION is a function which will be called by the main program for every rendered points.
#
import pygame

# Draw a point as a colored square
def square(point) -> pygame.Surface:
    size = 2
    alpha = 255
    s = pygame.Surface((size, size))
    s.set_alpha(alpha)
    s.fill(point[3])
    return s

STYLE_FUNCTION = square