# coloring.py
#
# When the main loop renders the point cloud, it calls a function for each point which returns its color. 
# Then the point with its color is passed to STYLE_FUNCTION.
# 
# This module contains functions which can be called for each point. Each one must return a list of 3 ints [Red, Green, Blue]
# and takes: a PointCloud object and a XYZ point to analyze.
#
import math

# Converts point's XYZ coordinates to the RGB color.
def xyzrgb(cloud, point):
    REPEAT = 1 # how many times repeat RGB colors spectrum

    r = math.floor(255 * REPEAT / (cloud.max_x) * point[0] % 510)
    g = math.floor(255 * REPEAT / (cloud.max_y) * point[1] % 510)
    b = math.floor(255 * REPEAT / (cloud.max_z) * point[2] % 510)

    if r <= 255: r = 255 - r
    elif r > 255: r = r - 255
    if g <= 255: g = 255 - g
    elif g > 255: g = g - 255
    if b <= 255: b = 255 - b
    elif b > 255: b = b - 255

    return [r, g, b]

# Function which will be called by the main program for every rendered points.
DEFAULT_COLORING = xyzrgb
