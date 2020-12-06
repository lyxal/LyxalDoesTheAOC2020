from itertools import *
from string import *
from math import *

i = open("input.txt").read().split("\n\n")

row = 0
index = 0

for l in i:
      c = ''.join(l.split())
      row += len(set(c))

print(row)
