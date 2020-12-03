from itertools import *
from string import *
from math import *

i = open("input.txt").readlines()
i = [l.strip("\n") * len(i) for l in i]
o = 0
B = []

slopes = [(1, 1), (3, 1), (5, 1),  (7, 1), (1, 2)]

for slo in slopes:
    row = 0
    x = 0
    o = 0

    while row < len(i):
        if i[row][x] == "#":
            o += 1
        x += slo[0]
        row += slo[1]
        
    B.append(o)

f = B[0]
for m in B[1:]:
    f *= m

print(f)
