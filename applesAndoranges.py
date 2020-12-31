s = 7
t = 10
a = 4
b = 12
m = 3
n = 3

apples = [2,3,-4]
oranges = [3,-2,-4]

fallen_apple = []
fallen_orange = []

for i in apples:
    fallen_apple.append(a+i)
for j in oranges:
    fallen_orange.append(b+j)

a_count = 0
o_count = 0
for ap in fallen_apple:
    if s <= ap <= t:
        a_count += 1

for o in fallen_orange:
    if s <= o <= t:
        o_count += 1

print(a_count,o_count)