Дан номер места в плацкартном вагоне. Определить, какое это место: верхнее или нижнее, в купе или боковое.

>>> import random
>>> X = random.randint (1,54)
>>> print(X)
24
>>> if X > 35 :
	print("side")

	
>>> if X < 35 :
	print("coupe")

	
coupe
>>> if X % 2 == 0 :
	print("top")

	
top
