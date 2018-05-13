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
	
def pc_to_array():
    array = np.zeros((1024, 1024, 3), dtype=np.uint8)
    array[512, 512] = [255, 0, 0]

    return array



def main():
    if len(sys.argv) < 3:
        print("Too few arguments passed. Please try this:")
        print(" " + os.path.basename(__file__) + " <input>  <output>")
        print(" <input>  -- point cloud filename (read only)")
        print(" <output> -- target png filename (for write)")
        return

    pc = file_to_pc(sys.argv[1])
    array = pc_to_array()
    smp.imsave(sys.argv[2], array, format = "png")

if __name__ == "__main__":
	main()

