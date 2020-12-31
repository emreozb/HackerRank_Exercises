k = 3
# k = 2
c = [1,3,5,7,9]
# c = [1,3,5,7,9,45,2,4]
# c = [2,5,6]
c.sort(reverse = True)

counter = 0
sum_cost = 0

for i in range(len(c)):
    sum_cost += ((counter+1)*c[i])
    if ((i+1) % k) == 0 :
        counter += 1
print(sum_cost)