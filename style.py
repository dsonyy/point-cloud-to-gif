# style.py
#
# When the main loop renders the point cloud, it calls a function for each point which returns a pygame.Surface. 
# Then every pygame.Surface object is rendered, the furthest ones are rendered first and the closest ones 
# are rendered last. 
# 
# This module contains functions which can be called for each point. Each one must return pygame.Surface 
# and takes a single point as a parameter. A point is represented by a list: [X, Y, Z, [Red, Green, Blue]].
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

# Function which will be called by the main program for every rendered points.
STYLE_FUNCTION = square