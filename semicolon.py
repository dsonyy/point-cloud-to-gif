with open("input/stozek2", "r") as inf, \
    open("input/stozek", "w") as ouf:
    data = inf.read()
    data = data.replace(";", "")
    ouf.write(data)

ouf.close()
inf.close()
    