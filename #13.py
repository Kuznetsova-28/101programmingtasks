Можно ли из бревна, имеющего диаметр поперечного сечения D, выпилить квадратный брус шириной A?
>>> import math
>>> D = 18
>>> print("(D) the cross-sectional diametr = " + str(D))
(D) the cross-sectional diametr = 18
>>> A = 5
>>> print("(A) square beam width = " + str(A))
(A) square beam width = 5
>>> d = A * math.sqrt( 5 )
>>> print("(d) diagonal beam = " + str(d))
(d) diagonal beam = 11.180339887498949
>>> if D >= d :
 print("its possible")

	
its possible
>>> if D < d :
 print("its impossible")
