Известен ГОД. Определить, будет ли этот год високосным, и к какому веку этот год относится.

import random
A = random.randint(1,2019)
print("year: " + str(A))
if A % 4 == 0:
    print(str(A) + "year a leap")
elif not A % 4 == 0:
    print(str(A) + "year not a leap")
V = A/100 + 1
print(str(A) + " year, " + str(V) + " century ")
