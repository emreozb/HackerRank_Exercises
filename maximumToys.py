prices = [1,12,5,111,200,1000,10]
k = 50
counter = 0
sum_toys = 0
prices.sort()
for p in prices:
    sum_toys += p
    if sum_toys < k:
        counter += 1
    else:
        break
print(counter)

