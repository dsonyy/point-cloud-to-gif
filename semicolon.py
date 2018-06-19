with open("input/walec2.txt", "r") as inf, \
    open("input/walec2", "w") as ouf:
    data = inf.read()
    data = data.replace(";", "")
    ouf.write(data)

ouf.close()
inf.close()
    