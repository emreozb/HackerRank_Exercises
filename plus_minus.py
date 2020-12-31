arr = [-4,3,-9,0,4,1]

p = 0
n = 0
z = 0
for i in arr:
    if i > 0:
        p += 1
    elif i < 0:
        n += 1
    else:
        z += 1

print("{:.6f}".format(p/len(arr)))
print ('%.6f'%(n/len(arr))) 
print("{:.6f}".format(z/len(arr)))
