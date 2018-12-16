import pygame
import math

X = 0
Y = 1
Z = 2
COLOR = 3
PLANE_X = X
PLANE_Y = Z
PLANE_Z = Y


def get_pos(point):
    SCALE = 3
    
    x = point[PLANE_X] * SCALE
    y = point[PLANE_Y] * SCALE
    z = point[PLANE_Z] * SCALE
    X_offset = 0
    Y_offset = 0.3
    
    return [x - z * X_offset + 200,
            y - z * Y_offset + 200]


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
        self.cloud.sort(key = lambda x: [ x[PLANE_Z], x[PLANE_X], x[PLANE_Y] ])

    def color(self, coloring):
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
    data = open(filename, "r").readlines()    
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

