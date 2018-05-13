import sys

xyz = []
try:
    with open(sys.argv[1], "r") as f:
        for line in f:
            point = []
            for num in line.split(" "):
                point.append(int(num))
            xyz.append(point)

except:
    print("Unable to load input point cloud")
    sys.exit()

xyz.sort(key = lambda x: x[2])

f = open(sys.argv[1] + "-s", "w")
for point in xyz:
    for num in point:
        f.write(str(num) + " ")
    f.write("\n")
