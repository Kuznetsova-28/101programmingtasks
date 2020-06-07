Дано вещественное число A. Вычислить f(A), если f(x) = 0, при x ≤ 0; f(x) = x при 0 < x < 1, в противном случае f(x) = x4.


import random
A = random.uniform(-3,3)
print("A= " + str(A))
X = A
if X <= 0:
    print("X <= 0")
    f=0
    print("f(A)" + str(f))
elif 0 < X and X < 1:
    print(" 0 < X < 1")
    f = X
    print("f(A)" + str(f))
elif not X <= 0 or not ( 0 < X and X < 1):
    print("other case")f = X**4
    print("f(A)" + str(f))
