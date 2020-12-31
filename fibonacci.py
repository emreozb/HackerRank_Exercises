n1, n2 = 0, 1

x = []
x.append(n1)
x.append(n2)
for i in range(100):
    n1 = n1 + n2
    x.append(n1)
    n2 = n1 + n2
    x.append(n2)
    if x[-1] > 1000:
        break
print(x)
