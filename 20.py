Дано число X. Определить, принадлежит ли это число заданному промежутку [a,b].

x = input("введите число для проверки")
a = input("укажите начало промежутка")
b = input("укажите конец промежутка")
if a <= x <= b:
    print("Число ", x, "Принадлежит множеству [",a,",",b,"]")
else:
    print("Число ", x," не принадлежит множеству [",a,",",b,"]")
