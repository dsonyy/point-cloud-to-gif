
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

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


# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for i in xyz:
    xs = i[0]
    ys = i[1]
    zs = i[2]
    ax.scatter(xs, ys, zs, c='b', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()