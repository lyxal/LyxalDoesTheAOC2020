from itertools import *
from string import *
from math import *

i = open("input.txt").read().split("\n\n")

row = 0
index = 0

v = 0

for r in i:
    if sum([(x in r) for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]) in [7, 8]: v += 1
print(v)
