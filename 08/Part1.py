from itertools import *
from string import *
from math import *

i = open("input.txt").read().split("\n")
i = [l.split() for l in i]

row = 0
ind = 0
out = 0
val = 0

rows = []

while row < len(i):
      if row in rows:
            print(val)
            break
      rows.append(row)
      if i[row][0] == "nop":
            row += 1

      elif i[row][0] == "acc":
            val += int(i[row][1])
            row += 1

      elif i[row][0] == "jmp":
            row += int(i[row][1])
