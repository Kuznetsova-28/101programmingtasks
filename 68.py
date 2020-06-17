Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
Найти наибольшее значение среди средних значений для каждой строки матрицы.

import random 
N = 2 
M = 3 
def get_row(column): 
col = [] 
for i in range(0, column): 
col.append(random.randint(0, 9)) 
return col 
def get_matrix(row, column): 
matrix = [] 
for i in range(0, row): 
matrix.append(get_row(column)) 
return matrix 
def print_matrix(matrix): 
i = 0 
while i &lt; len(matrix): 
j = 0 
row = matrix[i] 
while j n: 
n = average 
print("The highest value among the average values for each row " 
"matrixes:", n)
