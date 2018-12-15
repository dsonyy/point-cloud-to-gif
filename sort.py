import sys

xyz = []
#try:
data = open(sys.argv[1], "r").readlines()
for line in data:
    line = line.replace("\n", "")
    point = []
    for num in line.split(";"):
        point.append(float(num))
    xyz.append(point)

# except:
#     print("Unable to load input point cloud")
#     sys.exit()

xyz.sort(key = lambda x: x[2])

# normalize
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

        
# saving        
f = open(sys.argv[1][0:-4] + "-s.txt", "w")
for point in xyz:
    for num in point:
        f.write(str(num) + " ")
    f.write("\n")
