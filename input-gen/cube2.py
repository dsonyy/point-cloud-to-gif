f = open("cube2.txt", "w")
for x in range(0, 100):
    for y in range(0, 100):
        for z in range(0, 100):
            f.write(str(x) + " ; " + str(y) + " ; " + str(z) + "\n")

f.close()