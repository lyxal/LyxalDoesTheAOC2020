challenge_input = open("input.txt").readlines()
mode = "i"

c = [l.split() for l in challenge_input]
T = 0
for x in c:
    v = range(int(x[0].split("-")[0]), int(x[0].split("-")[1]) + 1)
    T += x[2].count(x[1][0]) in v

print(T)
