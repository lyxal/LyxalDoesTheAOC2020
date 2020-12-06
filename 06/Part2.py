from itertools import *
from string import *
from math import *

i = open("input.txt").read().split("\n\n")

row = 0
index = 0

for l in i:
      c = l.split()
      c = [set(m) for m in c]
      l = c[0]
      for m in c[1:]:
            l = l.intersection(m)
      row += len(l)

print(row)
