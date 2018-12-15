with open("input/stozek", "r") as inf, \
    open("input/stozek2", "w") as ouf:
    data = inf.read()
    data = data.replace(" ", " ; ")
    ouf.write(data)

ouf.close()
inf.close()

with open("input/walec", "r") as inf, \
    open("input/walec2", "w") as ouf:
    data = inf.read()
    data = data.replace(" ", " ; ")
    ouf.write(data)

ouf.close()
inf.close()
        

with open("input/pudelko", "r") as inf, \
    open("input/pudelko2", "w") as ouf:
    data = inf.read()
    data = data.replace(" ", " ; ")
    ouf.write(data)

ouf.close()
inf.close()
        