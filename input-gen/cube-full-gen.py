f = open("./input/cube-full", "w")
for x in range(0, 100):
    for y in range(0, 100):
        f.write(str(x) + " " + str(y) + " " + "0" + "\n")
        f.write(str(x) + " " + str(y) + " " + "99" + "\n")

for x in range(1, 100):
    for z in range(1, 99):
        f.write(str(x) + " " + "0" + " " + str(z) + "\n")
        f.write(str(x) + " " + "99" + " " + str(z) + "\n")
            
for y in range(1, 99):
    for z in range(1, 99):
        f.write("0" + " " + str(y) + " " + str(z) + "\n")
        f.write("99" + " " + str(y) + " " + str(z) + "\n")


f.close()