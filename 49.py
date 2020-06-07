Дан одномерный массив числовых значений, насчитывающий N элементов. Определить, имеются ли в массиве два подряд идущих нуля.

import random
N=random.randint(1,15)
arr=[random.randint(-1,1) for i in range(N)]
print(arr)
for i in range(N):
    if arr[i]==0 and arr[i+1] == 0:
        print("два подряд нуль")
        break
