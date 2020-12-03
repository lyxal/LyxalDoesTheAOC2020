from itertools import *
from string import *
from math import *

i = open("input.txt").readlines()
i = [l.strip("\n") * len(i) for l in i]
o = 0


slopes = [(1, 1), (5, 1), (3, 1), (7, 1), (1, 2)]

row = 0
x = 0

while row < len(i):
    if i[row][x] == "#":
        o += 1
    x += 3
    row += 1
print(o)     
