Можно ли в квадратном зале площадью S поместить круглую сцену радиусом R так, чтобы от стены до сцены был проход не менее K?
>>> import math
>>> S = 78
>>> A = math.sqrt(S)
>>> K = 15
>>> R = 7
>>> D = R*2
>>> if A-D > K :
	print("its possible")

	
>>> if A-D <= K :
	print("its impossible")

	
its impossible
