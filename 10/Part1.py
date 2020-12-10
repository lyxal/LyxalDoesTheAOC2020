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

jolts = [0, 0, 0, 0]

while val < rating:
      choices = [val + 1, val + 2, val + 3]
      choice = [m in i for m in choices].index(True)
      jolts[choice + 1] += 1
      val = choices[choice]

print(jolts[1] * jolts[3])

      
