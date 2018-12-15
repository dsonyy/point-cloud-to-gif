import pygame
import sys
import math

xyz = []
#try:
data = open(sys.argv[1], "r").readlines()
for line in data:
    line = line.replace("\n", "")
    point = []
    for num in line.split(";"):
        point.append(float(num))
    xyz.append(point)

# except:
#     print("Unable to load input point cloud")
#     sys.exit()

xyz.sort(key = lambda x: x[2], reverse=True)

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
min_x, max_x = min(i[0] for i in xyz), max(i[0] for i in xyz)
min_y, max_y = min(i[1] for i in xyz), max(i[1] for i in xyz)
min_z, max_z = min(i[2] for i in xyz), max(i[2] for i in xyz)

X = math.fabs(min_x - max_x)
Y = math.fabs(min_y - max_y)
Z = math.fabs(min_z - max_z)

P_WIDTH = 3
P_HEIGHT = 3
K = 3

def get_color(point):
    return [255/X*point[0]%256, 255/Y*point[1]%256, 255/Z*point[2]%256]
    
def get_rect(point):
    x = point[0] * K
    y = point[1] * K 
    z = point[2] * K

    return [y+x*0.2, z+x*0.2, P_WIDTH, P_HEIGHT]
    
for point in xyz:
    pygame.draw.rect(window_main, get_color(point), get_rect(point))
    #pygame.draw.rect(window_main, [0,0,0], get_rect(point), 1)

    
# main loop
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
