import pygame
import sys
import math

# local:
import coloring
import style

X = 0
Y = 1
Z = 2
COLOR = 3
PLANE_X = X
PLANE_Y = Z
PLANE_Z = Y

class Cloud:
    def diameter(self):
        a = max(self.min_x, self.min_y, self.min_z)
        return a * math.sqrt(3)   

    def min_axis(self, axis):
        if axis in [X, Y, Z]:
            return min(i[axis] for i in self.cloud)
        else:
            raise Exception("Bad axis")

    def max_axis(self, axis):
        if axis in [X, Y, Z]:
            return max(i[axis] for i in self.cloud)
        else:
            raise Exception("Bad axis")

    def normalise(self):        
        if self.min_x < 0:
            self.max_x -= self.min_x
            for i in self.cloud:
                i[X] -= self.min_x
            self.min_x = 0

        if self.min_y < 0:
            self.max_y -= self.min_y
            for i in self.cloud:
                i[Y] -= self.min_y
            self.min_y = 0

        if self.min_z < 0:
            self.max_z -= self.min_z
            for i in self.cloud:
                i[Z] -= self.min_z
            self.min_z = 0

    def sort(self):
        self.cloud.sort(key = lambda x: [ x[1], x[0], x[2] ])

    def color(self, coloring=coloring.DEFAULT_COLORING):
        for i in range(len(self.cloud)):
            if self.has_colors:
                self.cloud[i][COLOR] = coloring(self, self.cloud[i])
            else:
                self.cloud[i].append(coloring(self, self.cloud[i]))
        self.has_colors = True

    def __init__(self, cloud):
        self.cloud = cloud
        self.has_colors = False

        self.min_x = self.min_axis(X) 
        self.min_y = self.min_axis(Y)
        self.min_z = self.min_axis(Z)
        self.max_x = self.max_axis(X)
        self.max_y = self.max_axis(Y)
        self.max_z = self.max_axis(Z)

        self.sort()
        self.normalise()

def import_cloud(filename) -> Cloud:
    pc = []
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
            pc.append(point)

    return Cloud(pc) 

def get_pos(point):
    SCALE = 3
    
    x = point[0] * SCALE
    y = point[1] * SCALE
    z = point[2] * SCALE
    X_offset = 0
    Y_offset = 0.3
    
    return [x - y * X_offset + 200,
            z - y * Y_offset + 200]


def preview(cloud, win_width, win_height, function=None, *args):

    window_main = pygame.display.set_mode([win_width, win_height])
    window_main.fill([0,0,0])
    pygame.display.flip()

    # main loop
    running = True
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False

        window_main.fill([0,0,0])
        for p in cloud.cloud:
            s = style.square(p, cloud)
            window_main.blit(s, get_pos(p))
        pygame.display.flip()

        if function != None:
            function(*args)

        # pygame.image.save(window_main, "output/"+str(i)+".png")
        # i += 1
        
def scale_cloud(xyz, multiplier):
    sxyz = []
    for p in xyz:
        p[0] *= multiplier
        p[1] *= multiplier
        p[2] *= multiplier

# def rotate_cloud(xyz, angle, axis):
#     rxyz = []
#     if axis == 0:
#         A = 1
#         B = 2
#         CA = max_y / 2
#         CB = max_z / 2 
#     elif axis == 1:
#         A = 0
#         B = 2
#         CA = max_x / 2
#         CB = max_z / 2 
#     elif axis == 2:
#         A = 0
#         B = 1
#         CA = max_x / 2
#         CB = max_y / 2

#     for p in xyz:
#         s = math.sin(angle)
#         c = math.cos(angle)
#         p[A] -= CA
#         p[B] -= CB
#         xnew = p[A] * c - p[B] * s
#         ynew = p[A] * s + p[B] * c
#         p[A] = xnew + CA
#         p[B] = ynew + CB
#         rxyz.append(p)

#     return rxyz 


cloud = import_cloud(sys.argv[1])
cloud.color()
preview(cloud, 800, 600)