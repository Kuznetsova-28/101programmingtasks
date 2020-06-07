Даны вещественные числа: X, Y, Z.
Определить, существует ли треугольник с такими длинами сторон и, если существует, будет ли он прямоугольным.

x = input("storona a")
y = input ("storona b")
z = input ("storona c")
if ( X + Y <= Z) or ( Y + Z <= X ) or (Z + X <= Y) :
    print ("treugolnika s takimi storonami net")
else:
    if ( X > Y , X > Z) and ( X ** 2 == Y ** 2 + Z ** 2):
        print("treugolnik pryamougolniy")
    elif ( Y > X , Y > Z ) and (Y ** 2 == X ** 2 + Z ** 2):
        print ("treugolnik pryamougolniy")
    elif (Z > Y , Z > X) and (Z ** 2 == Y ** 2 + X ** 2):
        print("treugolnik pryamougolniy")
    else:
        print ("treugolnik ne pryamougolniy")
