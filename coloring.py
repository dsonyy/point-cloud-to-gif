import math

'''
def dummy(cloud, point) -> list:

    
    return [r, g, b]
'''

def xyzrgb(cloud, point, repeat=1):
    r = math.floor(255 * repeat / (cloud.max_x) * point[0] % 510)
    g = math.floor(255 * repeat / (cloud.max_y) * point[1] % 510)
    b = math.floor(255 * repeat / (cloud.max_z) * point[2] % 510)

    if r <= 255: r = 255 - r
    elif r > 255: r = r - 255

    if g <= 255: g = 255 - g
    elif g > 255: g = g - 255

    if b <= 255: b = 255 - b
    elif b > 255: b = b - 255

    return [r, g, b]

def deep(cloud, point):
    r = 255 / cloud.max_z * point[2]
    g = 255 / cloud.max_x * point[2]
    b = 255 / cloud.max_y * point[2]

    return [r, g, b]

DEFAULT_COLORING = xyzrgb
