import pygame
import sys
import math
from datetime import datetime


xyz = []
try:
    data = open(sys.argv[1], "r").readlines()
    for line in data:
        line = line.replace("\n", "")
        point = []
        for num in line.split(";"):
            try:
                point.append(float(num))
            except:
                break
        if len(point) == 3:
            xyz.append(point)
except:
     print("Unable to load input point cloud")
     sys.exit()

xyz.sort(key = lambda x: [x[1], x[0], x[2]])

# normalize
min_x = min(i[0] for i in xyz)
min_y = min(i[1] for i in xyz)
min_z = min(i[2] for i in xyz)
if min_x < 0:
    for i in xyz:
        i[0] -= min_x
if min_y < 0:
    for i in xyz:
        i[1] -= min_y
if min_z < 0:
    for i in xyz:
        i[2] -= min_z

# create window
WIDTH = 800
HEIGHT = 600        
window_main = pygame.display.set_mode([WIDTH, HEIGHT])
window_main.fill([0,0,0])
pygame.display.flip()


# render figure
max_x = max(i[0] for i in xyz)
max_y = max(i[1] for i in xyz)
max_z = max(i[2] for i in xyz)
center_x = max_x / 2
center_y = max_y / 2
center_z = max_z / 2

P_WIDTH = 1
P_HEIGHT = 1

def distance(A, B = [center_x, center_y, center_z]):
    return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2)

def add_colors(xyz):
    cxyz = []
    for p in xyz:
        point = [p[0], p[1], p[2], get_color(p)]
        cxyz.append(point)
    return cxyz
    
def get_color(point):
    repeat = 1

    r = math.floor(255 * 1 / (max_x) * point[0] % 510)
    g = math.floor(255 * repeat / (max_y) * point[1] % 510)
    b = math.floor(255 * repeat / (max_z) * point[2] % 510)

    if r <= 255: r = 255 - r
    elif r > 255: r = r - 255

    if g <= 255: g = 255 - g
    elif g > 255: g = g - 255

    if b <= 255: b = 255 - b
    elif b > 255: b = b - 255

    return [r, g, b]
    
def rotate_cloud(xyz, angle, axis):
    rxyz = []
    if axis == 0:
        A = 1
        B = 2
        CA = max_y / 2
        CB = max_z / 2 
    elif axis == 1:
        A = 0
        B = 2
        CA = max_x / 2
        CB = max_z / 2 
    elif axis == 2:
        A = 0
        B = 1
        CA = max_x / 2
        CB = max_y / 2

    for p in xyz:
        s = math.sin(angle)
        c = math.cos(angle)
        p[A] -= CA
        p[B] -= CB
        xnew = p[A] * c - p[B] * s
        ynew = p[A] * s + p[B] * c
        p[A] = xnew + CA
        p[B] = ynew + CB
        rxyz.append(p)

    return rxyz 

def get_pos(point):
    SCALE = 3
    
    x = point[0] * SCALE
    y = point[1] * SCALE
    z = point[2] * SCALE
    X_offset = 0
    Y_offset = 0.3
    
    return [x - y * X_offset + 200,
            z - y * Y_offset + 200]

def get_rect(point):
    pos = get_pos(point)
    return [pos[0], pos[1], P_WIDTH, P_HEIGHT]
    

xyz = add_colors(xyz)
# main loop
running = True
i = 0
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    xyz = rotate_cloud(xyz, 0.1, 0)
    xyz = rotate_cloud(xyz, 0.05, 1)
    xyz = rotate_cloud(xyz, 0.075, 2)
    
    window_main.fill([0,0,0])
    for point in xyz:
        # pygame.draw.rect(window_main, get_color(point), get_rect(point))
        s = pygame.Surface((P_WIDTH, P_HEIGHT))  # the size of your rect
        s.set_alpha(64)                # alpha level
        s.fill(point[3])           # this fills the entire surface
        window_main.blit(s, get_pos(point))    # (0,0) are the top-left coordinates
        
        # pygame.draw.rect(window_main, [255,255,255], get_rect(point), 1)
    pygame.image.save(window_main, "output/"+str(i)+".png")
    i += 1
    pygame.display.flip()

