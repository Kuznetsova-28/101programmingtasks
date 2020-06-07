Дан одномерный массив числовых значений, насчитывающий N элементов. 
Поменять местами элементы, стоящие на чётных и нечётных местах: A[1] ↔ A[2]; A[3] ↔ A[4] ...

>>> import random
>>> N=random.randint(1,10)
>>> arr=[random.randint(1,100) for i in range(N)]
>>> print(arr)
[95, 75, 12, 61, 97, 55, 69, 95]
>>> for i in range(0,N,2):
	arr[i],arr[i+1]=arr[i+1],arr[i]
	print(arr)
