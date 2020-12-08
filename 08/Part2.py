from itertools import *
from string import *
from math import *

d = open("input.txt").read().split("\n")
i = [l.split() for l in d]




prev = 0
brut = [row for row in range(len(i)) if i[row][0] in ["jmp", "nop"]]
for CHANGE in brut:
      i = [l.split() for l in d]
      i[CHANGE][0] = "jmp" if i[CHANGE][0] == "nop" else "nop"
      row = 0
      ind = 0
      out = 0
      val = 0

      rows = []
      terms = True
      while row < len(i):
            if row in rows:
                  terms = False
                  break
            rows.append(row)
            if i[row][0] == "nop":
                  row += 1

            elif i[row][0] == "acc":
                  val += int(i[row][1])
                  row += 1

            elif i[row][0] == "jmp":
                  prev = int(i[row][1])
                  row += int(i[row][1])

      if terms: print(val); print(i); break
