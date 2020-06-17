Для вводимых чисел определить процент положительных и отрицательных чисел. 
При вводе числа −65432 закончить работу.

import random
M=random.randint(1,4)
arr=[random.randint(1,10)for i in range(M)]
n=0
m=0
N=-65432
for i in range(M):
    arr[i]=input()
for i in range(M):
    if int(arr[i])>0:
        n+=1
    if int(arr[i])<0:
        m+=1
    if int(arr[i])== -65432:
        print("end")
        break
print("процент положительных чисел: "+str(100/len(arr)*n))
print("процент отрицательных чисел: "+str(100/len(arr)*m))
