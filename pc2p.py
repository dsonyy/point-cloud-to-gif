import sys
import os
from PIL import Image

w = 640
h = 480
offset = 40

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
	
def pc_to_png(filename):
    try:
        image = Image.open(filename)
    except:
        print("Unable to load output image.")
        return
    image.load()





def main():
    if len(sys.argv) < 3:
        print("Too few arguments passed. Please try this:")
        print(" " + os.path.basename(__file__) + " <input>  <output>")
        print(" <input>  -- point cloud filename (read only)")
        print(" <output> -- target png filename (for write)")
        return

    file_to_pc(sys.argv[1])

if __name__ == "__main__":
	main()

