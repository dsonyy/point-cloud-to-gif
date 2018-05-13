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
    w = 1000
    h = 1000
    array = np.zeros((w, h, 3), dtype=np.uint8)
    for point in pc:
        x, y, z = point[0], point[1], point[2]
        array[10 + x, 10 + y + round(0.1 * z)]  = [255 - round(z * 10), 0, 0]
        print(str(10 + x) + " " + str(10 + y + round(0.1 * z)))
        

    return array



def main():
    if len(sys.argv) < 3:
        print("Too few arguments passed. Please try this:")
        print(" " + os.path.basename(__file__) + " <input>  <output>")
        print(" <input>  -- point cloud filename (read only)")
        print(" <output> -- target png filename (for write)")
        return

    pc = file_to_pc(sys.argv[1])
    array = pc_to_array(pc)
    smp.imsave(sys.argv[2], array, format = "png")

if __name__ == "__main__":
	main()

