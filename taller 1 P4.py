#1
from tkinter import Y


def SumarDatosD():
    n1 = float(input("nuemero con decimales : "))
    n2 = int(input("nuemero entero : "))
    print("la suma de los dos numeros es: ",n1 + n2)

#SumarDatosD()

#2
def SumaMultiDatosD():
    n1 = int(input("nuemero 1 : "))
    n2 = int(input("nuemero 2 : "))
    print("la suma de los dos numeros es: ",n1 + n2)
    n3 = int(input("nuemero 3 : "))
    print("la multiplicacion entre el resultado de la suma y el numer 3 es : ",(n1+n2)*n3)

#SumaMultiDatosD()

#3
def Descuento():
    n1 = int(input("ingrese el valor : "))
    n2 = int(input("ingrese el descuento 0  a 100%  : "))
    n3 = (n1*n2)/100
    print(f"Con un descuento del {n2} el valor queda {n1-n3}")
        
#Descuento()

#4
def Mayor3():
    print("ingrese 3 numeros")

    n1=int(input("Numero 1: "))
    n2=int(input("Numero 2: "))
    n3=int(input("Numero 3: "))
    if n1>n2:
        if n1>n3:
            print(f"el valor mayor es el numero 1 = {n1}")
    
    if n2>n1:
        if n2>n3:
            print(f"el valor mayor es el numero 2 = {n2}")
    
    if n3>n1:
        if n3>n2:
            print(f"el valor mayor es el numero 3 = {n3}")
    
#Mayor3()

#5
def ParFrase():
    frase=input("introdusca una frase : ")
    x=len(frase)
    if x%2 == 0:
        print("La cantidad de caracteres de la cadena es PAR")
    else:
        print("La cantidad de caracteres de la cadena es INPAR") 
    
#ParFrase()

#6
def MayorFrase():
    frase=input("introdusca palabra 1 : ")
    x=len(frase)
    frase2=input("introdusca palabra 2 : ")
    y=len(frase2)
    if x==y:
        print("Ambos palabras son iguales")
    elif x>y:
        print("la palabra 1 es MAYOR que la palabra 2 ")
    else:
        print("la palabra 1 es MENOR que la palabra 2")

#MayorFrase()

#7
def MenorNum():
    print("ingrese dos numeros")

    n1=int(input("Numero 1: "))
    n2=int(input("Numero 2: "))

    if n1==n2:
        print("Ambos numeros son iguales")
    elif n1>n2:
        print(f"el numero menor es {n2} ")
    else:
        print(f"El numero menor es {n1}  ")

#MenorNum()

#8
def UsuContra():
    x=input("introdusca el usuario : ")
    y=input("introdusca la contraseña : ")
    
    if x=='UTP' and y=='utp123':
        print("Usuario y contraseña correcto")
    else:
        print("ACCESO DENEGADO")

#UsuContra()

#9
def Contador():
    y=100
    for x in range(49,y):
        print(y)
        y-=1

#Contador()

#10
def Contador2():
    for x in range(0,44,4):
        print(x)

#Contador2()

#11
def Contador3():
    for x in range(100,200):
        print(x)

#Contador3()

#12
def Menos1():
    x=int(input("ingrese un numero entero positivo : "))
    y=(x*2)-1
    for i in range(x+1,y):
        print(i)

#Menos1()       

#13
def Vocales():  
    segundo = 0     
    frase = input("Ingrese una palabra/frase: ")
    frase = frase.lower()
    vocales = ["a", "e" , "i" , "o" , "u"]

    for x in vocales:
        veces=0
        for y in frase:
            if x==y:
                veces += 1     
        contar = veces+segundo
        segundo=contar
        if veces != 0:
            print("La vocal ", x ," apearece ",veces," veces")
    print(f"el numero total de volcales es {segundo}")

#Vocales()

#14

def Contador4():
    contador=0
    x=int(input("ingrese el primer numero: "))
    y=int(input("ingrese el segundo numero: "))

    if x==y:
        print("Ambos numeros son iguales")
    elif x<y:
        for i in range(x+1,y):
            z=contador+i
            contador=z
            y-=1
    else:
        for i in range(y+1,x):
            z=contador+i
            contador=z
            x-=1
    print(f"la suma de los numeros del rango es {z}")

#Contador4()

#15
def Triangulo():
    x=int(input("ingrese un numero: "))
    for i in range(x+1):
        print("*"*i)

#Triangulo()







