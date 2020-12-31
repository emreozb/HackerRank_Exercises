arr = [23,5,12,23,54,865,23,1,4,34]
arr.sort()

arr_sum = 0
i = 0
while (i < len(arr)):
    arr_sum += arr[i]
    i += 1

arr_4min = arr_sum - arr[-1]
arr_4max = arr_sum - arr[0]
    
print(arr_sum)
print(arr_4min)
print(arr_4max)