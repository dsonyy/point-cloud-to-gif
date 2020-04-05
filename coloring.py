import math

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
    r = math.floor(255 * 2/ cloud.max_y * point[1] % 511)
    g = math.floor(255 * 2/ cloud.max_y * point[1] % 511) 
    b = math.floor(255 * 2/ cloud.max_y * point[1] % 511)

    if r <= 255: r = r
    elif r > 255: r = 255

    if g <= 255: g = g
    elif g > 255: g = g - 255

    if b <= 255: b = b
    elif b > 255: b = b - 255


    return [r, g, b]

def dark(pc, point):
    if pc.has_colors:
        color = point[3]
    else:
        color = [255, 255, 255]

    k = math.floor(255 / pc.max_y * point[1])
    
    return color[0] - k, color[1] - k , color[2] - k


DEFAULT_COLORING = xyzrgb
