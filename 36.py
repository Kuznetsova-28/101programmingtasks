Дан одномерный массив числовых значений, насчитывающий N элементов. Вставить группу из M новых элементов, начиная с позиции K.

import array
import random
M = random.randint(1,10)
K = random.randint(1,5)
N = random.randint(1,10)
arr = [random.randint(1,100) for i in range (N)]
print("N=" + str(N))
print("K=" + str (K))
print("M=" + str (M))
print (arr)
arr2 = [random.randint(1,100) for i in range (M)]
print(arr2)
arr.insert(K,arr2)
print (arr)
