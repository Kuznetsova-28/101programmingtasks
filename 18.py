Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R. 
Определить, можно ли заполнить жидкостью объёма M первую ёмкость, вторую, обе.

import math
A = input("Rebro kuba")
R = input("Radius osnovania")
H = input("Visota")
M = input("obiem")
Sk = math.pow(A, 3)
print(Sk, "obiem kuba")
Sc = (( math.pi) * (math.pow(r, 2)) * H)
print(Sc, "obiem tsilindra")
if (Sk + Sc <= M ):
    print("zapolneni obe emkosti")
if (Sc <= M) :
    print("zapolnen tsilindr")
If (Sk <= M):
    print("zapolnen kub")
