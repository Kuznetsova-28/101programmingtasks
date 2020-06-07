Дан одномерный массив числовых значений, насчитывающий N элементов.
Подсчитать количество чисел, делящихся на 3 нацело, и среднее арифметическое чисел с чётными значениями.
Поставить полученные величины на первое и последнее места в массиве (увеличив массив на 2 элемента).

import random
N=random.randint(1,15)
arr=[random.randint(-100,100) for i in range(N)]
print(arr)
K=0
T=0
t=0
for i in range (N):
    if arr[i]%2==0:
        K+=1
        print("количество кратных"+str(K))
        for i in range(N):
            if arr[i]%2==0:
                T+=arr[i]
                t+=1
            A=T/t
            print("арифметическое знначение"+str(A))
            arr.insert(0,K)
            arr.append(A)
            print(arr)
