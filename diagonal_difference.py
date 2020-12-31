arr = [[3,5,6],
[9,2,28],
[12,-52,-4]]

p_dig=0
s_dig=0

# # Using For Loop 

for i in range(len(arr)):
    p_dig += arr[i][i]

a = len(arr) - 1
for i in range(len(arr)):
    s_dig += arr[i][a]
    a -= 1

print(p_dig,s_dig)
print(abs(p_dig-s_dig))


# # Using While Loop

# i = 0
# j = len(arr) - 1
# while (i < len(arr)):
#     p_dig += arr[i][i]
#     s_dig += arr[i][j]
#     i += 1
#     j -= 1
# print(p_dig,s_dig)
# print(abs(p_dig-s_dig))
