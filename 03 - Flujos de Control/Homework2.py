#1.
x = 1
print(x>0)

#2.
x,y = 2,3
if type(x) == type(y): print(True)
else: print(False)

#3.
for i in range(1,21):
    if i % 2 == 0:
        print(i)

#4.
for i in range(6):
    print(i**3)
print("----------------------------")

#5.
x = 5
for i in range(x):
    pass
#6.
n = 4
if type(n) == int:
    if n>0:
        i,j = 0,1
        while(i < n):
            j*=i+1
            i+=1
    else:
        print("Numero menor o igual a 0")
else:
    print("Numero de tipo no entero")
print(j)

#7.
i = 0
while(i < 5):
    for i in range(5):
        pass
    i+=1
    
#8.

for i in range(6):
    j = 0
    while(j <= 5):
        j+=1

#9
"""t = 0
j = 2
while(j<30):
    c = 0
    for i in range(1,j+1):
        if j%i == 0:
            c+=1
    if c==2:
        print(j,end=",")
    j+=1"""


#9
tope_rango=10
n = 2
primo = True
contsin = 0
while (n < tope_rango):
    for div in range(2, n):
        contsin+=1
        if (n % div == 0): 
            primo = False
    if (primo):
        print(n,end = ",")
    else:
        primo = True
    n += 1

#10
tope_rango=10
n = 2
contcon = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        contcon+=1
        if (n % div == 0): 
            primo = False
            break
    if (primo):
        print(n,end = ",")
    else:
        primo = True
    n += 1

#11
print(contsin,contcon, end="\n")
print("Un",round((contcon*100)/contsin),"% Mas rapido con respecto a el anterior")

#12
print("Segun mis calculos disminuye")

#13
i = 99
while(i<=300):
    i+=1
    if i % 12 != 0:
        continue
    print(i,end=",")      

#14
print(end="\n")
x = "si"
n= 2
primo = True
i=0
while (x == "si"):
    for div in range(2, n):
        contcon+=1
        if (n % div == 0): 
            primo = False
            break
    if (primo):
        i+=1
        print("Numero primo #",i,"=",n)
    else:
        primo = True
        n+=1
        continue
    x = input("Siguiente numero primo? si|no : ")
    n+=1

#15
n=99
while(n<=300):
    if n%3 == 0 and n%6 == 0:
        print(n)
        break
    n+=1

