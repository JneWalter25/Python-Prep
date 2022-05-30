#1.
lst = ["Bog","Chicago","Caracas","Medellin","Madrid","Panama"]
print(lst)

#2.
print(lst[1])

#3.
print(lst[1:4])

#4.
print(type(lst))

#5.
print(lst[2:])

#6.
print(lst[:4])

#7. No arroja error
lst.append("Co")
lst.append("Uk")
print(lst)

#8.
lst.insert(3,"Br")
print(lst)

#9.
lst2 = ["Ru","Ur"]
lstf = lst + lst2
print(lstf)

#10.
print(lst.index('Co'))
#Returns:  Returns the lowest index where the element appears.

#11. Error
#print(lst.index('Col'))

#12.
lstf.pop()
print(lstf)

#13. Error
#lstf.remove("Col")

#14. 
x = lstf[-1]
print(x)

#15.
print(lstf*4)

#16.     
tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

#17.
print(tupla[10:16])

#18.
"""n = 0
for i in tupla:
    if i == n:
        print("Existe")
        break
    if i == tupla[-1]:
        print("No existe")"""

#print([item for item in tupla if item == 122]) List comprehension

"""try:
    print("El index del numero",tupla.index(22),"Existe")
except ValueError:
    print("No existe")"""

#19.
n = "Paris"
for i in lst:
    if i == n:
        print("Existe")
        break
    if i == lst[-1]:
        print("No existe")
lst.append("Paris")
print(lst[-1])

#20.
n = "Co"
j = 0
for i in lst:
    if i == n:
        print("Existe")
        j+=1
print(j)

#21.
tuple1 = tuple(lst)

#22.
x,y,a = lstf[:3]
print(x,y,a)

#23.
print(lst)
dict1 = {"Ciudad": lst,
        "Pais" : ["Colombia","Peru"],
        "Continente" : ["America","Europa"]
}

#24.
for i in dict1.keys():
    print(i)

#25.
for i in dict1.get('Ciudad'):
    print(i)
print(dict1.get('Ciudad'))