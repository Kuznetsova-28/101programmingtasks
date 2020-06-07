Дано вещественное число A. 
Вычислить f(A), если f(x) = 0 при x ≤ 0; f(x) = x2 − x при 0 < x < 1, в противном случае f(x) = x2 − sin(πx2).

import random
import math
X =  random.randint(2,7)
if X <= 0:
    f = 0
    print ("f(" + str(X) + ")=" + str (f))
if 0 < X < 1:
    f = X**2-X
    print("f(" + str(X) + ")=" + str (f))
else :
    f=X**2-math.sin(math.pi**2)
    print("f(" + str(X) + ")=" + str (f))
