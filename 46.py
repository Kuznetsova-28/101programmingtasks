Дан одномерный массив числовых значений, насчитывающий N элементов. Дано положительное число T.
Разделить это число между положительными элементами массива пропорционально значениям этих элементов и добавить полученные доли 
к соответствующим элементам.

import random
N=random.randint(1,15)
arr=[random.randint(-100,100) for i in range(N)]
print(arr)
T=random.randint(1,10)
print("T= "+str(T))
for i in range (N):
    if arr[i]>0:
        t=arr[i]/T
        arr[i]=t
    print(arr)
