import sys
import os
import numpy as np
import scipy.misc as smp


def file_to_pc(filename, echo = False):
    pc = []
    with open(filename, "r") as f:
        for line in f:
            point = []
            for num in line.split():
                point.append(int(num))
            pc.append(point)
    if echo == True:
        print(pc)
    return pc

def pc_to_array(pc):
    min_x, max_x = min(i[0] for i in pc), max(i[0] for i in pc)
    min_y, max_y = min(i[1] for i in pc), max(i[1] for i in pc)
    min_z, max_z = min(i[2] for i in pc), max(i[2] for i in pc)
    min_i, max_i = 50, 255
    a = 0.4
    w = max_x - min_x + max_z - min_z
    h = max_y - min_y + max_z - min_z
    offset = 100
    array = np.zeros((w + 2*offset, h + 2*offset, 3), dtype=np.uint8)
    for point in pc:
        array_x = offset - 1 + w - point[0] - point[2]
        array_y = offset - 1 + h - point[1] - point[2]
        intensity = min_i + (max_i - min_i) / (max_z - min_z) * point[2]
        array[array_x, array_y] = [intensity, intensity, intensity]
    return array

def array_to_file(filename, array):
    smp.imsave(filename, array, format = "png")
    return

def main():
    
    if len(sys.argv) < 3:
        print("Too few arguments passed. Please try this:")
        print(" " + os.path.basename(__file__) + " <input>  <output>")
        print(" <input>  -- point cloud filename (read only)")
        print(" <output> -- target png filename (for write)")
        return
    try:
        pc = file_to_pc(sys.argv[1])
    except:
        print("Unable to load input point cloud")
    
    try:
        array = pc_to_array(pc)
    except:
        print("Unable to generate image array")
    
    try:
        array_to_file(sys.argv[2], array)
    except:
        print("Unable to export output image")
    
if __name__ == "__main__":
	main()

