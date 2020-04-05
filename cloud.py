import pygame
import math

X = 0
Y = 1
Z = 2
COLOR = 3
PLANE_X = X
PLANE_Y = Y
PLANE_Z = Z

# A class responsible for loading, calculating and transforming point clouds
class PointCloud:

    # Constructor loads point cloud from text file formatted like this:
    #
    #   X; Y; Z
    #   X; Y; Z
    #   X; Y; Z
    #     ...
    #   X; Y; Z
    #
    # where every X, Y and Z is a floating point number.
    def __init__(self, filename):
        self.points = []
        self.max_x, self.max_y, self.max_z = 0, 0, 0
        self.min_x, self.min_y, self.min_z = 0, 0, 0
        self.scale = 3
        self.offset_x, self.offset_y = 0, 0

        data = open(filename, "r").readlines()    
        for line in data:
            if not line.split():
                continue
            line = line.replace("\n", "")
            point = []
            for num in line.split(";"):
                point.append(float(num))
            if len(point) == 3:
                self.points.append(point)
                if point[X] > self.max_x: self.max_x = point[X]
                elif point[X] < self.min_x: self.min_x = point[X]

                if point[Y] > self.max_y: self.max_y = point[Y]
                elif point[Y] < self.min_y: self.min_y = point[Y]

                if point[Z] > self.max_z: self.max_z = point[Z]
                elif point[Z] < self.min_z: self.min_z = point[Z]
        self.normalise()

    # Sorts every point cloud point from the furthest one to the closest.
    def sort(self):
        self.points.sort(key = lambda x: [ x[PLANE_Z], x[PLANE_X], x[PLANE_Y] ])
                    
    # Moves point cloud so that there aren't any negative coordinates.
    #
    # Note: The goal is to move point cloud on the pygame window So this problem could be resolved
    # using pygame.Surfaces and this solution would be incomparably faster.
    def normalise(self):
        self.max_x -= self.min_x
        self.max_y -= self.min_y
        self.max_z -= self.min_z
        for i in range(len(self.points)):
            self.points[i][X] -= self.min_x
            self.points[i][Y] -= self.min_y
            self.points[i][Z] -= self.min_z
        self.min_x = 0
        self.min_y = 0
        self.min_z = 0

    # Moves entire point cloud.
    #
    # Note: The goal is to move point cloud on the pygame window So this problem could be resolved
    # using pygame.Surfaces and this solution would be incomparably faster.
    def move_cloud(self, move_x, move_y, move_z):
        for i in range(len(self.points)):
            self.points[i][X] += move_x
            self.points[i][Y] += move_y
            self.points[i][Z] += move_z

    # Rotates entire point cloud around an axis by a angle in degrees.
    def rotate_cloud(self, angle, axis):
        if not angle:
            return
        angle = math.radians(angle)
        if axis == X:
            A = 1
            B = 2
            CA = self.max_y / 2
            CB = self.max_z / 2 
        elif axis == Y:
            A = 0
            B = 2
            CA = self.max_x / 2
            CB = self.max_z / 2 
        elif axis == Z:
            A = 0
            B = 1
            CA = self.max_x / 2
            CB = self.max_y / 2

        for i in range(len(self.points)):
            s = math.sin(angle)
            c = math.cos(angle)
            self.points[i][A] -= CA
            self.points[i][B] -= CB
            xnew = self.points[i][A] * c - self.points[i][B] * s
            ynew = self.points[i][A] * s + self.points[i][B] * c
            self.points[i][A] = xnew + CA
            self.points[i][B] = ynew + CB

        self.sort()    

    # Converts a 3D point to a 2D point, considers a render scale and offsets
    def get_pos(self, point, width=0, height=0):
        x, y, z = point[PLANE_X] * self.scale, point[PLANE_Y] * self.scale, point[PLANE_Z] * self.scale
        X_offset, Y_offset = 0, 0
        x_p, y_p = x - z * X_offset + self.offset_x, y - z * Y_offset + self.offset_y
        if width: x_p += (width - self.max_x * self.scale) / 2
        if height: y_p += (height - self.max_y * self.scale) / 2
        return (int(x_p), int(y_p))

