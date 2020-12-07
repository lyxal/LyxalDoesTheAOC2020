from itertools import *
from string import *
from math import *

i = open("input.txt").read().split("\n")
i = [l.split(" contain ") for l in i]

bags = {}

for line in i:
      bag, rule = line
      bag = bag.replace("bags", "").replace("bag", "")[:-1]
      rule = rule[:-1].split(", ")

      numbers = {}
      for r in rule:
            no, colour = r.split(" ", 1)
            no = int(no) if no != "no" else 0

            colour = colour.replace("bags", "").replace("bag", "")[:-1]
            if no:
                  numbers[colour] = no
      bags[bag] = numbers

tab = -1
      
def contains_gold(name, bag_list):
      global tab
      tab += 1
      contains = True
      #print(" " * tab, name, bag_list)
      
      for bag in bag_list:
            if "shiny gold" in bag_list: tab -= 1; return True
            outs = []
            for b in bag_list:
                  outs.append(contains_gold(b, bags[b]))
            tab -= 1

            return any(outs)
      return False


con = 0
for bag in bags:
      x = contains_gold(bag, bags[bag])
      con += int(contains_gold(bag, bags[bag]))

print(con)
