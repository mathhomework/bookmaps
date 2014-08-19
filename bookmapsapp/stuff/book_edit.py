from sys import argv

script, filename = argv

txt = open(filename)

lines = [i for i in txt.readlines()]

for x in lines:
    x = x[:-6]
    .write(x)