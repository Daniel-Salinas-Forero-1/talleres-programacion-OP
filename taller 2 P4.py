#1
class Datosl:
    año = 2021
    nombre = 'un sol oscuro'
    paginas = 20
    costom1pl = 2150 
    tlibros = 11310

    def valorpl(self):
       print(f"un aeditorial saco un nuevo libro con el nombre de :{self.nombre}")
       print("se realizaran un total de : ",self.tlibros," con un valor de : ",self.costom1pl," en materia prima por libro y un descuento del 5 porciento en todo el pedido ")
       x = self.tlibros*self.costom1pl
       y = (x*5)/100
       print("lo que seria un descuento de :",y)

    def estimadog(self):
        print("segun la cantidad de copias se pretende vender el libro a un costo de 3500 lo que dejaria una ganancia de :")
        x=(11310 * 3500)-(11310 * 2150)
        print(x)

Libro=Datosl()
#Libro.valorpl()
#Libro.estimadog()



 

class Datos2:
    largo = 15
    ancho = 12
    valorc = 125000000
    impuesto = 1100000 
    deuda = 4

    def tamaño(self):
        x = self.ancho*self.largo 
        y = self.valorc/x
        y = int(y)
        print(f"la propiedad tiene un tamaño de", x," metros cuadrados")
        print(f"el valor por metro cuadrado es de {y}")


    def impuestoa(self):
        print("La casa cuenta con una deuda de 4 años en total la deuda por impuestos es de :")
        x = self.impuesto*4
        print(x)

Casa=Datos2()
#Casa.tamaño()
#Casa.impuestoa()

class Datos3: 
    nombre = 'Programacion '
    duracion = '200'
    actores = 'selena gomez y tom cruise'
    tdpelicula = 'terror'
    codpelicula =  '123456789' 

    def cambiar (self):
        print("Los Actores Principales son : ", self.actores)


    def hacer(self):
        print("El genero de la pelicula es : ", self.tdpelicula)

Pelicula=Datos3()
#Pelicula.hacer()
#Pelicula.cambiar()


class Datos4:
    tdtrabajo = 'distribuidor'
    productos = 'aseo'
    seguridad = 'Empresa ssgura '
    diseño = 'espontaneo'
    instalaciones = 'amplias'

    def descargar (self):
        print("La bodega almacena productos de :", self.productos)


    def entrar(self):
        print("La empresa encargada de la seguridad es :", self.seguridad)

Bodega=Datos4()
#Bodega.descargar()
#Bodega.entrar()

class Datos5:
    alumbra = "Si"
    color = "Gris"
    tamaño = 25
    potencia = 15
    botones = "Si"

    def datos(self):
        print("La lampara alumbra: ",self.alumbra)


    def pot(call):
        print("La potencia de la lampara es: ",call.potencia)

Lampara=Datos5()
#Lampara.datos()
#Lampara.pot()



class Datos6:
    sirve = "Si"
    megas = 100
    fibre = "Si"
    color = "Blanco"
    capacidad = 100

    def datos(self):
        print("CAntidad de megas: ",self.megas)


    def colo(call):
        print("Color: ",call.color)

Modem=Datos6()
#Modem.datos()
#Modem.colo()


class Datos7:
    sirve = "Si"
    megas = 100
    fibre = "Si"
    color = "Blanco"
    frecuencia = 100

    def datos(self):
        print("Cantidad de megas que distribuye: ",self.megas)

        
    def frec(call):
        print("Color: ",call.frecuencia)
        
Router=Datos7()
#Router.datos()
#Router.frec()

class Datos8:
    color = "Negro"
    material = "Cuero sintetico"
    capacidad = 15
    nro_bolsillos = 5
    marca = "totto"

    def datos(self):
        print("La marca del maletin es: ",self.marca)


    def cap(call):
        print("La capacidad del maletin es: ",call.capacidad)

Maletin=Datos8()
#Maletin.datos()
#Maletin.cap()



class Datos9:
    sexo = "Masculino"
    edad = 25
    rh = "o positivo"
    eps = "Medimas"
    regimen = "Contributivo"

    def datos(self):
        print("La eps del paciente es: ",self.eps)


    def ed(call):
        print("La edad del paciente es: ",call.edad)

PacienteOncologico=Datos9()
#PacienteOncologico.datos()
#PacienteOncologico.ed()

class Datos10:
    sexo = "Femenino"
    marca_purina = "Whiskas"
    color = "Negro"
    juega = "si"
    raza = "Cruzado"

    def datos(self):
        print("La raza del gato es: ",self.raza)


    def marca(call):
        print("La marca de purina que le gusta es: ",call.marca_purina)

Gato=Datos10
#Gato.datos()
#Gato.marca()

#2-----------------------------------------------------------------------------
class Datos1Ejercicio2:
    base = 5
    altura = 20

    def arear(self):
        a=self.base * self.altura
        print("el area de el rectangulo es:", a)


    def perimetro(self):
        b = (self.base *2) + (self.altura *2)
        print("el perimetro de el rectangulo es:", b)

Rectangulo=Datos1Ejercicio2()
#Rectangulo.arear()
#Rectangulo.perimetro()

#3-------------------------------------------------------------------------------


class Datos1Ejercicio3:
    nombre = "Diego"
    nro_horas = 192
    valor_hora = 4000
    pensionh = 62
    pensionm = 57
    edad = 34
    sexo = "Masculino"
    tiempo_anti = 10

    def ganames(self):
        ga = self.nro_horas * self.valor_hora
        print("El trabajador se gana mensualmente: ",ga)


    def faltapension(self):
        print("El tiempo de antiguedad es: ",self.tiempo_anti)
        if self.sexo == 1:
            f = self.pensionh - self.edad
            print("El tiempo que le falta para pensionarse es: ",f)
        else:
            f = self.pensionm - self.edad
            print("El tiempo que le falta para pensionarse es: ",f)


    def paga(self):
        ga = self.nro_horas * self.valor_hora
        pa_pensionysalud = (4*ga)/100
        print("Lo que paga por pensión es: ",pa_pensionysalud)
        pa_pen_ano = pa_pensionysalud*12
        print("Lo que abona al año es: ",pa_pen_ano)
        print("Lo que paga por salud: ",pa_pensionysalud)

Empleado=Datos1Ejercicio3()
#Empleado.ganames()
#Empleado.faltapension()
#Empleado.paga()



import math
class Datos1Ejercicio4:
    n1 = 5
    n2 = 2

    def suma(self):
        print(self.n1 + self.n2)

    def resta(self):
        print(self.n1 - self.n2)

    def mult(self):
        print(self.n1 * self.n2)

    def divi(self):
        print(self.n1 / self.n2)

    def seno_trigo(self):
        print(math.sin(self.n1))

    def cos_trigo(self):
        print(math.cos(self.n1))

    def tan_trigo(self):
        print(math.tan(self.n1))

    def expo(self):
        print(self.n1**2)

    def raiz(self):
        print(math.sqrt(self.n1))

    def radianes(self):
        print(math.radians(self.n1))

    def grados(self):
        print(math.degrees(self.n1))

    def npi(self):
        print(math.pi)
    

Calculadora=Datos1Ejercicio4()
#Calculadora.suma()
#Calculadora.resta()
#Calculadora.mult()
#Calculadora.divi()
#Calculadora.seno_trigo()
#Calculadora.cos_trigo()
#Calculadora.tan_trigo()
#Calculadora.expo()
#Calculadora.raiz()
#Calculadora.radianes()
#Calculadora.grados()
#Calculadora.npi()






