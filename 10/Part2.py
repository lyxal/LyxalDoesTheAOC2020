from itertools import *
from string import *
from math import *

i = open("input.txt").read().split("\n")
i = [int(l) for l in i]

row = 0
ind = 0
out = 0
val = 0

rows = [0]

rating = max(i) + 3
i.append(rating)
i = sorted(i)
branches = {}
def paths_to_rating(node):
      global branches
      if node == rating:
            return 1

      if node in branches:
            return branches[node]

      paths = filter(lambda x: x in i, [node + 1, node + 2, node + 3])
      out = 0
      for path in paths:
            out += paths_to_rating(path)

      branches[node] = out

      return out

print(paths_to_rating(0))
            
