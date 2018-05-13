import sys

x, y, z = [], [], []
try:
    with open(sys.argv[1], "r") as f:
        for line in f:
            X, Y, Z = line.split()
            x.append(X)
            y.append(Y)
            z.append(Z)
except:
    print("Unable to load input point cloud")
    sys.exit()

    
