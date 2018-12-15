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

min_x, max_x = min(i[0] for i in pc), max(i[0] for i in pc)
min_y, max_y = min(i[1] for i in pc), max(i[1] for i in pc)
min_z, max_z = min(i[2] for i in pc), max(i[2] for i in pc)
cen_x = round((max_x - min_x) / 2) + min_x
cen_y = round((max_y - min_y) / 2) + min_y
cen_z = round((max_z - min_z) / 2) + min_z
center = [cen_x, cen_y, cen_z]
a = 0.03

for point in xyz:
