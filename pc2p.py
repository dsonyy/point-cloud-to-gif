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

def pc_to_array(pc):
    min_x, max_x = min(i[0] for i in pc), max(i[0] for i in pc)
    min_y, max_y = min(i[1] for i in pc), max(i[1] for i in pc)
    min_z, max_z = min(i[2] for i in pc), max(i[2] for i in pc)
    w = max_x - min_x 
    h = max_y + min_y
    offset = 300
    array = np.zeros((w + 2*offset, h + 2*offset, 3), dtype=np.uint8)
    for point in pc:
        array_x = point[0]
        array_y = point[1]
        intensity = 255 - 255 / (point[2] + 1)
        array[array_x + offset, array_y + offset] = [intensity, intensity, intensity]
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

