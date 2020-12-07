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

tab = 0
def count_bags(bag_list):
      global tab
      tab += 1
      if bag_list == dict(): tab -= 1; return 0
      else:
            count = 0
            for bag in bag_list:
                  count += bag_list[bag]
                  count += bag_list[bag] * count_bags(bags[bag])
            tab -= 1
            return count
      

print(count_bags(bags["shiny gold"]))
