from itertools import *
from string import *
from math import *

i = open("input.txt").read().split("\n\n")

row = 0
index = 0

v = 0

for r in i:
    if sum([(x in r) for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]) in [7, 8]:
        data = r.split()
        Yes = True
        for m in data:
            k, val = m.split(":")
            if k == "byr":
                if not(1920 <= int(val) <= 2002):
                    Yes = False
            if k == "iyr":
                if not(2010 <= int(val) <= 2020):
                    Yes = False
            if k == "eyr":
                if not(2020 <= int(val) <= 2030):
                    Yes = False

            if k == "hgt":
                if "cm" in val:
                    if not(150 <= int(val[:-2]) <= 193):
                        Yes = False
                if "in" in val:
                    if not(59 <= int(val[:-2]) <= 76):
                        Yes = False
                        Yes = False
                if not("in" in val or "cm" in val):
                    Yes = False
                    Yes = False

            if k == "hcl":
                if val[0] == "#":
                    try:
                        x = int(val[1:], 16)
                    except:
                        Yes = False
                    
                else:
                    
                    Yes = False

            if k == "ecl":
                if not(val in ["amb","blu","brn","gry","grn","hzl","oth"]):Yes = False

            if k == "pid":
                if not(len(val) == 9 and val.isnumeric()): Yes = False
                
        if Yes: v += 1;
print(v)
