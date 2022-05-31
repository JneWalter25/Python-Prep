#1.
x = 8
def primo(x):
    i = 2
    if x == 2:
        return True
    while(i < x):
        if(x % i) == 0:
            return False
            break
        elif i == x-1:
            return True
        
        i+=1
#2.
y = [2,3,4,5,6,7,8,9,10]
def primolist(y):
    newlist = []
    for i in y:
        if primo(i) == True:
            newlist.append(i)
    return newlist

primos = primolist(y)
print(primos)

#3,4
y = [1,2,3,4,5,5,6,6,1,1,1,6,6,6,7,7,7,7,7,7,0,0,0,0,0,0,0]
def repetido(y,menor):
    y.sort()
    x = y[0]
    c,v,r = 0,0,0
    if menor == True: v=x+1
    for i in y:
        if c >= r:
            if menor == True:
                if x <= v:
                    r = c
                    v = x
            else:
                if x >= v:
                    r = c
                    v = x
        if i == x:
            c += 1
        else:
            x = i
            c = 0
            c +=1
    return r,v

veces, repetido = repetido(y,False)
print("El numeo mas repetido es",repetido,"con",veces,"veces")

#5.
def conversion_grados(valor, origen, destino):
    if (origen == 'celsius'):
        if (destino == 'celsius'):
            valor_destino = valor
        elif (destino == 'farenheit'):
            valor_destino = (valor * 9 / 5) + 32
        elif (destino == 'kelvin'):
            valor_destino = valor + 273.15
        else:
            print('Parámetro de Destino incorrecto')
    elif (origen == 'farenheit'):
        if (destino == 'celsius'):
            valor_destino = (valor - 32) * 5 / 9
        elif (destino == 'farenheit'):
            valor_destino = valor
        elif (destino == 'kelvin'):
            valor_destino = ((valor - 32) * 5 / 9) + 273.15
        else:
            print('Parámetro de Destino incorrecto')
    elif (origen == 'kelvin'):
        if (destino == 'celsius'):
            valor_destino = valor - 273.15
        elif (destino == 'farenheit'):
            valor_destino = ((valor - 273.15) * 9 / 5) + 32
        elif (destino == 'kelvin'):
            valor_destino = valor
        else:
            print('Parámetro de Destino incorrecto')
    else:
        print('Parámetro de Origen incorrecto')
    return valor_destino




#6.

medidas = ['celsius','kelvin','farenheit']
for i in range(0,3):
    for j in range(0,3):
        print("De",medidas[i],"a",medidas[j],"es:",conversion_grados(1,medidas[i],medidas[j]))


#7.
def factorial(n):
    if(type(n) != int):
        return 'El numero debe ser un entero'
    if(n < 0):
        return 'El numero debe ser pisitivo'
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))