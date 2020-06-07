Дан одномерный массив числовых значений, насчитывающий N элементов.
Поменять местами группу из M элементов, начинающихся с позиции K с группой из M элементов, начинающихся с позиции P.

>>> import random
>>> M= random.randint(1,5)
>>> K= random.randint(1,5)
>>> P= random.randint(5,10)
>>> N=random.randint(1,15)
>>> arr=[random.randint(1,100) for i in range(N)]
>>> print("N="+str(N))
N=12
>>> print("K="+str(K))
K=3
>>> print("P="+str(P))
P=10
>>> print("M="+str(M))
M=1
>>> print(arr)
[97, 78, 90, 96, 47, 10, 93, 4, 99, 51, 98, 73]
>>> arr[K: M + K + 1], arr[P : M + P + 1]= arr[P : M + P + 1],arr[K : M + K + 1]
>>> print(arr)
[97, 78, 90, 98, 73, 10, 93, 4, 99, 51, 96, 47]
>>> 
