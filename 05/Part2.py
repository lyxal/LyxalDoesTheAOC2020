i = open("input.txt").read().split("\n")

row_up = 128
row_low = 1

col_up = 8
col_low = 1

ids = []

for c in i:
      m = c[0:7].replace("F", '0').replace("B", '1')
  
      p = int(m, 2) * 8
      v = c[7:].replace("R", '1').replace("L", '0')
      p += int(v, 2)
      ids.append(p)

for c in ids:
    if (c + 2) in ids and not((c + 1) in ids):
        print(c + 1)
