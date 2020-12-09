from itertools import *
from string import *
from math import *

i = open("input.txt").read().split("\n")
i = [int(l) for l in i]

row = 0
ind = 0
out = 0
val = 0

rows = []

l = list(map(int, i[:25]))
n = list(map(sum, permutations(l, 2)))

for s in i[25:]:
      if s not in n:
            val = s      
      del l[0]
      l.append(s)
      n = list(map(sum, permutations(l, 2)))

