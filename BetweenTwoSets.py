a = [2,4]
b = [16,32,96]

# a = [2,6]
# b = [24,36]

a1= []
a2= []

b1= []


for i in range(len(a)):
    for j in range(max(a), min(b)+1):
        if j % a[i] != 0:
            a1.append(j)

for i in range(max(a), min(b)+1):
    if i not in a1:
        a2.append(i)
    
for i in range(len(b)):
    for j in range(len(a2)):
        if b[i] % a2[j] != 0:
            b1.append(a2[j])

for i in range(len(b1)):
    if b1[i] in a2:
        a2.remove(b1[i])

print(len(a2))
