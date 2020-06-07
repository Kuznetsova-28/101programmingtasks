Даны двещественные числа X и Y . Вычислить Z. Z = √(X x Y) при X > Y, Z = ln(X + Y ) в противном случае.


import random
import math
X = random.randint(1,28)
Y = random.randint (1,43)
print("X - ", X)
print("Y - ", Y)
if X > Y  :
    Z = math.sqrt(X*Y)
    print("Zqrt - ", Z)
else:
    Z = math.log(X+Y)
    print("Zlog - ", Z)
