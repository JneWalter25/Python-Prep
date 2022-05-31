#1.
from cgi import test
from tkinter import Y, simpledialog


lst = []
j = -16
while len(lst) <15:
    lst.append(j+1)
    j+=1
print(lst)

#2.
i = 0
while i < len(lst):
    if lst[i] % 2 == 0:
        print(lst[i],end=",")

    i+=1
print(end='\n')
#3.
for i in lst:
    if i % 2 == 0: print(i, end = ",")
print(end='\n')

#4.
for i in lst[:3]:
    print(i, end = ",")
print(end='\n')

#5.
for i,c in enumerate(lst):
    print("Indice:",i,"Valor:",c, end = ",")
print(end='\n')

#6.
list1 = [1,2,5,7,8,10,13,14,15,17,20]#3,4,6,9,11,12,16,18,19
n = 0
e = 0
while(n<19):
    if list1[n+1] != list1[n] + 1:
        x = list1[n] + 1
        list1.insert(n+1,x)
    n+=1
print(list1)

#7.
#Fibonnaci iterative
lst =[]
y,x,r = 1,0,0
for i in range(30):
    r = x + y
    y = x
    x = r
    lst.append(r)
print(lst)

#8.
print(sum(lst))

#9.
for i in range(5):
    print(lst[-1-i]/lst[-2-i]) 

#10.
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i in range(len(cadena)):
    if cadena[i] == "n":
        print("El index de cada n es:",i)

#11.
dict = {
    "nombres" : ["J","W","S","F"],
    "numeros" : [1,2,3,4]
}
test = iter(dict)
print(next(test))
print(next(test))

#12.
list2 = list(cadena)
test2 = iter(list2)
for i in range(len(list2)):
    print(next(test2))

#13.
a = [1,2]
b = [2,4]
c = zip(a,b)
tupla = tuple(c)
print(tupla)

#14.
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis2 = [x for x in lis if x % 7 == 0]
print(lis2)

#15.
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
print(len(lis))

#16.
for i in range(len(lis)):
    if type(lis[i]) != list:
        lis[i] = list(lis[i])
        print(i)
print(lis)

