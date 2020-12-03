from itertools import *
from string import *
from math import *

i = open("input.txt").readlines()
i = [l.strip("\n") * len(i) for l in i]
o = 0

row = 0
x = 0

while row < len(i):
    if i[row][x] == "#":
        o += 1
    x += 3
    row += 1
print(o)     
