import sys
import os
import png

def main():
    if len(sys.argv) < 3:
        print("Too few arguments passed. Please try this:")
        print(" " + os.path.basename(__file__) + " <input>  <output>")
        print(" <input>  -- point cloud filename (read only)")
        print(" <output> -- target png filename (for write)")
        return
    pc_path = sys.argv[1]
    png_path = sys.argv[2]    

    pc = []
    with open(pc_path, "r") as f:
        for line in f:
            point = []
            for num in line.split():
                point.append(num)
            pc.append(point)                   

    png_file = open(png_path, "wb")
    print(pc)


if __name__ == "__main__":
	main()

