Задана строка символов, в которой встречается символ «.». 
Поставить после каждого такого символа системное время ПК.


text = input()
print(text)
A=input("введите системное время ПК: ")
for i in range (len(text)):
    if text[i]=="." :
        text=(text.replace(text[i],A)
              print(text)
