a = []
b = []

a.append(input('Enter three values between 0 and 100: '))
b.append(input('Enter three values between 0 and 100: '))

a2 = a[0].split(' ')
b2 = b[0].split(' ')

b3=[]
a3=[]
for i in a2:
    if 100 >= int(i) >= 1:
        a3.append(int(i))
    else:
        print('Unacceptable value')
        a3.append(int(input('Enter a value between 0 and 100: ')))
for j in b2:
    if 100 >= int(j) >= 1:
        b3.append(int(j))
    else:
        print('Unacceptable value')
        b3.append(int(input('Enter a value between 0 and 100: ')))
t=0
z=0
for i in range(len(b3)):
    if a3[i]>b3[i]:
        t += 1
    elif a3[i]==b3[i]:
        continue
    elif a3[i]<b3[i]:
        z +=1 
print(t,z)
    