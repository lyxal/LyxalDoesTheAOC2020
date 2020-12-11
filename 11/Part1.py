from itertools import *
from string import *
from math import *

i = open("input.txt").read().split("\n")
i = [[m for m in l] for l in i]

row = 0
col = 0
out = 0
val = 0

rows = []
prev = [""]

def get_adjacent(grid, row, col, f=False):
      directions = [(1, 0),    #row then col
                    (0, 1),
                    (-1, 0),
                    (0, -1),
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1)
                  ]

      spaces = []
      for dirt in directions:
            try:
                  new_row = row + dirt[0]
                  new_col = col + dirt[1]

                  if new_row >= 0 and new_col >= 0:
                        spaces.append(grid[new_row][new_col])
            except:
                  pass

      return spaces
      

while i != prev[-1]:
      prev.append([m[:] for m in i[:]])
      for row in range(0, len(i)):
            for col in range(0, len(i[row])):
                  space = prev[-1][row][col]; adjacent = get_adjacent(prev[-1], row, col)
                  
                  if space == ".":
                        continue

                  elif space == "L":
                        if adjacent.count("#") == 0:
                              i[row][col] = "#"

                  elif space == "#":
                        if adjacent.count("#") >= 4:
                              i[row][col] = "L"
for row in i:
      for seat in row:
            val += seat == "#"

print(val)
                        
