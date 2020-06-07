Дан одномерный массив числовых значений, насчитывающий N элементов. 
Определить, образуют ли элементы массива, расположенные перед первым отрицательным элементом, убывающую последовательность.

import random
>>> N = random.randint(0,15)
>>> arr = [random.randint(-90,90) for i in range (N)]
>>> print(arr)
[42, 61, -26, 20]
>>> K=1
>>> for i in range (0,N):
	if arr[i] <0:
		break
	if arr[i] >= 0 :
		if arr[i]>arr[i+1] and arr[i+1] >= 0:
			K=1
			break
		if arr[i] < arr[i+1]:
			K=2
        if K == 1:
            print("not increasing secuence")
        elif K == 2:
            print("increasing secuence")
