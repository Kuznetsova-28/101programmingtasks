Дан одномерный массив числовых значений, насчитывающий N элементов. Из элементов исходного массива построить два новых. 
В первый должны входить только элементы с положительными значениями, а во второй — только элементы с отрицательными значениями.

import random
N = random.randint(1,10)
arr=[random.randint(-100,100) for i in range(N)]
print(arr)
arrP=[]
arrN=[]
for i in range(N):
    if arr[i]<0:
        arrN.append(arr[i])
    if arr[i]>0:
        arrP.append(arr[i])
print(arrN)
print(arrP)
