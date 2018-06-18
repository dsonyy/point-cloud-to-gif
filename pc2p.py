import sys
import os
import numpy as np
import scipy.misc as smp


def file_to_pc(filename, echo = True):
    pc = []
    try:
        with open(filename, "r") as f:
            for line in f:
                point = []
                for num in line.split():
                    point.append(int(num))
                pc.append(point)
    except:
        print("Unable to load input point cloud")
    if echo == True:
        print(pc)
    return pc
	
def place_point(w, h, x, y, z):
    array_x = w / x
    array_y = h / y
    intensity = 255
    return array_x, array_y, intensity

def pc_to_array(pc):
    min_x, max_x = min(pc[0]), max(pc[0])
    min_y, max_y = min(pc[1]), max(pc[1])
    min_z, max_z = min(pc[2]), max(pc[2])
    w = max(pc[]) - min(pc[]) + 0
    h = max(pc[]) - min(pc[]) + 0
    array = np.zeros((w, h, 3), dtype=np.uint8)
    for point in pc:
        array_x, array_y, intensity = place_point(w, h, point[0], point[1], point[2])
        array[array_x, array_y] = [array_x, array_y, intensity]

    return array

def array_to_file(filename, array):
    smp.imsave(filename, array, format = "png")
    return

def main():
    
    """if len(sys.argv) < 3:
        print("Too few arguments passed. Please try this:")
        print(" " + os.path.basename(__file__) + " <input>  <output>")
        print(" <input>  -- point cloud filename (read only)")
        print(" <output> -- target png filename (for write)")
        return"""
    pc = file_to_pc("./input/cube-s")
    array = pc_to_array(pc)
    array_to_file("./output/testing", array)

if __name__ == "__main__":
	main()

