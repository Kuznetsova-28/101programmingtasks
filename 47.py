Дан одномерный массив числовых значений, насчитывающий N элементов. Исключить из массива элементы, принадлежащие промежутку [B; C].

import random
N=random.randint(1,15)
arr=[random.randint(-100,100) for i in range (N)]
print(arr)
B=random.randint(1,10)
print("B= "+str(B))
C=random.randint(1,10)
print("C= "+str(C))
arr[B:C]=[]
print(arr)
