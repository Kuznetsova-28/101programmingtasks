Дан одномерный массив числовых значений, насчитывающий N элементов. 
Выполнить перемещение элементов массива по кругу вправо, т. е. A[1] → A[2]; A[2] → A[3]; ... A[n] → A[1].

import random
N=random.randint(1,20)
arr=[random.randint(0,100) for i in range(N)]
print(arr)
for i in range(N):
    arr[-i],arr[-i-1]=arr[-i-1],arr[-i]
    arr[0],arr[1]=arr[1],arr[0]
    print(arr)
