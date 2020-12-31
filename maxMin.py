k = 3
arr = [10, 100,300,200,1000,20,30]
# arr = [5,2,1,2,1,2,1]
# arr = [1,2,3,4,10,20,30,40,100,200]

arr.sort()

sub_arr= []
# diff = arr[k-1] - arr[0]
for i in range((len(arr)-k+1)):
    diff = arr[i+k-1] - arr[i]
    sub_arr.append(diff)
    # if arr[i+k-1] - arr[i] < diff:
    #         diff = arr[i+k-1] - arr[i]

print(min(sub_arr))