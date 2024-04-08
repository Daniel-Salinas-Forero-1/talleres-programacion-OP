from numpy import char
import os
import numpy as np


#1----------------------------------------------------------------------------------------
'''
class Vehiculo():
    pass
    def __init__(self,T_vehiculo,años,M_llantas,T_combustible):
        self.T_vehiculo = T_vehiculo
        self.años = años
        self.M_llantas = M_llantas
        self.T_combustible = T_combustible

    def mostrar(self):
        print('El tipo de vehiculo es : ',self.T_vehiculo)
        print('La marca de las llantas es : ',self.M_llantas)
        print('Años de duracion : ',self.años)
        print('Tipo de combustible : ',self.T_combustible)


#V = input('Ingrese el tipo del vehiculo \n Camion \n Carro \n moto \n')
#M = input('Ingrese la marca de las llantas: ')
#A = int(input('Ingrese los años aproximados de duracion de las llantas : '))
#tc = input('Ingrese el tipo del vehiculo \n ACPM \n Extra \n Corriente \n')
#Vehiculo1=Vehiculo(V,A,M,tc)
#Vehiculo1.mostrar()


class Coche(Vehiculo):
    pass
    def __init__(self, T_vehiculo, años, M_llantas, T_combustible,tiempo):
        super().__init__(T_vehiculo, años, M_llantas, T_combustible)
        self.tiempo = tiempo
        


    def mostrar2(self):
        x=0
        print('tiempo que demora el vehiculo de Pereira a Medellin : ',self.tiempo)
        if self.T_combustible == 'ACPM':
            print('si el vehiculo recorre 600 km mensual y consume gasolina ACPM tendria un costo de : ',(600/20)*9048)
        elif self.T_combustible == 'Extra':
            print('si el vehiculo recorre 600 km mensual y consume gasolina Extra tendria un costo de : ',15800*(600/37))
        elif self.T_combustible == 'Corriente':
            print('si el vehiculo recorre 600 km mensual y consume gasolina Corriente tendria un costo de : ',9029*(600/32))
        else:
            print("no digito de forma correcta el dato del nombre del tipo de gasolina")

#V = input('Ingrese el tipo del vehiculo \n Camion \n Carro \n moto \n')
#M = input('Ingrese la marca de las llantas: ')
#A = int(input('Ingrese los años aproximados de duracion de las llantas : '))
#T = int(input('Ingrese el tiempo que demora el vehicuclo de Pereira a Medellin : '))
#tc = input('Ingrese el tipo del vehiculo \n ACPM \n Extra \n Corriente \n')
#os.system("cls")
#Vehiculo1=Coche(V,A,M,tc,T)
#Vehiculo1.mostrar()
#Vehiculo1.mostrar2()
'''
#2-----------------------------------------------------------------------------------------------------------


class Vehiculo():
    pass
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def mostrar1(self):
        print('color del vehiculo : ',self.color)
        print('ruedas del vehiculo : ',self.ruedas)
 





class Coche(Vehiculo):
    pass
    def __init__(self, color, ruedas,velocidad,cilindro):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindro = cilindro

    def mostrar2(self):
        print('velocidad maxima de : ',self.velocidad,' km/h')
        print('cilindro de : ',self.cilindro,' cc')
 





class Bici(Vehiculo):
    pass
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


    def mostrar3(self):
        print('tipo : ',self.tipo)

 




class Camioneta(Coche):
    pass
    def __init__(self, color, ruedas, velocidad, cilindro,carga):
        super().__init__(color, ruedas, velocidad, cilindro)
        self.carga = carga

    def mostrar4(self):
        print('puede cargar : ',self.carga,' Kg')
 






class Moto(Bici):
    pass
    def __init__(self, color, ruedas, tipo,velocidad,cilindro):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindro = cilindro

    def mostrar5(self):
        print('velocidad maxima de : ',self.velocidad,' km/h')
        print('cilindro de : ',self.cilindro,' cc')
 
Vehiculo1=Vehiculo('negro',2)
Vehiculo2=Coche('rojo',4,250,200)
Vehiculo3=Bici('blanca',2,'urbana')
Vehiculo4=Camioneta('negra',4,210,1800,20)
Vehiculo5=Moto('azul',2,'deportiva',210,200)







def Catalogar():
    vehiculos = list([Vehiculo1,Vehiculo2,Vehiculo3,Vehiculo4,Vehiculo5])
    z = int(input('ingrese el numero de ruedas :'))
    j=0
    for x in vehiculos :
        if x.ruedas == z :
            print('El nombre de la clase es :',type(x).__name__,"\n")
            print('el nombre de un atributo es ',vars(x),'\n')
            j+=1
    if j == 0 :
        print('No existen vehiculos con esas caracteristicas...')
Catalogar()










