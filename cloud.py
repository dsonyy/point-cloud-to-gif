import pygame
import math

X = 0
Y = 1
Z = 2
COLOR = 3
PLANE_X = X
PLANE_Y = Z
PLANE_Z = Y

class PointCloud:
    def sort(self):
        self.points.sort(key = lambda x: [ x[PLANE_Z], x[PLANE_X], x[PLANE_Y] ])
                    
    def normalise(self):        
        if self.min_x < 0:
            self.max_x -= self.min_x
            for i in range(len(self.points)):
                self.points[i][X] -= self.min_x
            self.min_x = 0
     
        if self.min_y < 0:
            self.max_y -= self.min_y
            for i in range(len(self.points)):
                self.points[i][Y] -= self.min_y
            self.min_y = 0
     
        if self.min_z < 0:
            self.max_z -= self.min_z
            for i in range(len(self.points)):
                self.points[i][Z] -= self.min_z
            self.min_z = 0


    def __init__(self, filename):
        self.points = []
        self.has_colors = False

        self.max_x = 0
        self.max_y = 0
        self.max_z = 0
        self.min_x = 0
        self.min_y = 0
        self.min_z = 0

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
                self.points.append(point)
                if point[X] > self.max_x: self.max_x = point[X]
                elif point[X] < self.min_x: self.min_x = point[X]

                if point[Y] > self.max_y: self.max_y = point[Y]
                elif point[Y] < self.min_y: self.min_y = point[Y]

                if point[Z] > self.max_z: self.max_z = point[Z]
                elif point[Z] < self.min_z: self.min_z = point[Z]

        self.sort()
        self.normalise()

def diameter(pc):
    #a = max(pc.min_x, pc.min_y, pc.min_z)
    #return a * math.sqrt(3)   
    return 0

def color(pc, coloring):
    for i in range(len(pc.points)):
        if pc.has_colors:
            pc.points[i][COLOR] = coloring(pc, pc.points[i])
        else:
            pc.points[i].append(coloring(pc, pc.points[i]))
    pc.has_colors = True


def get_pos(point):
    SCALE = 3
    
    x = point[PLANE_X] * SCALE
    y = point[PLANE_Y] * SCALE
    z = point[PLANE_Z] * SCALE
    X_offset = 0
    Y_offset = 0
    
    return [x - z * X_offset,
            y - z * Y_offset]


# def scale_cloud(pc, multiplier):
#     for i in range(len(pc)):
#         pc[i][X] *= multiplier
#         pc[i][Y] *= multiplier
#         pc[i][Z] *= multiplier

def rotate_cloud(pc, angle, axis):
    angle = math.radians(angle)

    if axis == X:
        A = 1
        B = 2
        CA = pc.max_y / 2
        CB = pc.max_z / 2 
    elif axis == Y:
        A = 0
        B = 2
        CA = pc.max_x / 2
        CB = pc.max_z / 2 
    elif axis == Z:
        A = 0
        B = 1
        CA = pc.max_x / 2
        CB = pc.max_y / 2

    for i in range(len(pc.points)):
        s = math.sin(angle)
        c = math.cos(angle)
        pc.points[i][A] -= CA
        pc.points[i][B] -= CB
        xnew = pc.points[i][A] * c - pc.points[i][B] * s
        ynew = pc.points[i][A] * s + pc.points[i][B] * c
        pc.points[i][A] = xnew + CA
        pc.points[i][B] = ynew + CB

    pc.sort()    

# class Cloud:
#     def __init__(self, cloud):
#         self.cloud = cloud
#         self.has_colors = False

#         self.min_x = self.min_axis(X) 
#         self.min_y = self.min_axis(Y)
#         self.min_z = self.min_axis(Z)
#         self.max_x = self.max_axis(X)
#         self.max_y = self.max_axis(Y)
#         self.max_z = self.max_axis(Z)

#         self.sort()
#         self.normalise()

# def import_cloud(filename) -> Cloud:
#     pc = []
#     data = open(filename, "r").readlines()    
#     for line in data:
#         point = []
#         for num in line.split(";"):
#             try:
#                 point.append(float(num))
#             except:
#                 break
#         if len(point) == 3:
#             pc.append(point)

#     return Cloud(pc) 

