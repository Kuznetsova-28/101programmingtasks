Дан одномерный массив числовых значений, насчитывающий N элементов. 
Добавить столько элементов, чтобы элементов с положительными и отрицательными значениями стало бы поровну.

import random
N=random.randint(1,10)
arr=[random.randint(-100,100) for i in range(N)]
print(arr)
plus=0
minus=0
for i in range (N)
if arr[i]>0:
    plus+=1
    elif arr[i]<0:
        minus+=1
if plus>minus:
    for i in range(minus,plus):
        arr.append(random.randint(-100,-1))
    elif plus<minus:
        for i in range(plus,minus):
            arr.append(random.randint(1,10))
print("Number plus:" + str(plus))
print("Number minus:" +str(minus))
print(arr)
