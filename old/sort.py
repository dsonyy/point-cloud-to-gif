import sys

xyz = []
#try:
with open(sys.argv[1], "r") as f:
    for line in f:
        point = []
        if not line.strip():
            for num in line.split(" "):
                print("-->" + num)
                point.append(float(num))
            xyz.append(point)

# except:
#     print("Unable to load input point cloud")
#     sys.exit()

xyz.sort(key = lambda x: x[2])

min_x = min(i[0] for i in xyz)
min_y = min(i[1] for i in xyz)
min_z = min(i[2] for i in xyz)
if min_x < 0:
    for i in xyz:
        i[0] -= min_x
if min_y < 0:
    for i in xyz:
        i[1] -= min_y
if min_z < 0:
    for i in xyz:
        i[2] -= min_z

f = open(sys.argv[1] + "-s", "w")
for point in xyz:
    for num in point:
        f.write(str(num) + " ")
    f.write("\n")
