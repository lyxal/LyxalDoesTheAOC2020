challenge_input = open("input.txt").readlines()
mode = "i"

c = [l.split() for l in challenge_input]
T = 0
for x in c:
    v = list(map(int, x[0].split("-")))
    T +=(x[2][v[0] - 1] == x[1][0]) != (x[2][v[1] - 1] == x[1][0])

print(T)
