Дан одномерный массив числовых значений, насчитывающий N элементов.
Добавить к элементам массива такой новый элемент, чтобы сумма элементов с положительными значениями стала бы 
равна модулю суммы элементов с отрицательными значениями.

import random
N=random.randint(0,15)
arr=[random.randint(-90,90) for i in range(N)]
print(arr)
sum_plus=0
sum_minus=0
for i in range(N):
    if arr[i]>0:
        sum_plus+=arr[i]
    elif arr[i]<0:
        sum_minus +=arr[i]
    print("Сумма,если элементы с положительным значением = "+str(sum_plus))
    print("Суумма,если элементы с отрицательным значением = "+str(sum_minus))
    if sum_plus> -sum_minus:
        arr.append(-(sum_minus+sum_plus))
    elif sum_plus<-sum_minus:
        arr.append(-(sum_plus+sum_minus))
    print(arr)
