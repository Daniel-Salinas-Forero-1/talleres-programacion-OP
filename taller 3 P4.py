#1
class Datosl:
    pass
    def __init__(self,nombre,año,tlibros,costom1pl,paginas):
       self.nombre = nombre
       self.año = año
       self.paginas = paginas
       self.costom1pl = costom1pl
       self.tlibros = tlibros


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

Libro=Datosl('La noche',2002,1130,2150,20)
#ibro.valorpl()
#Libro.estimadog()



 

class Datos2:
    pass
    def __init__(self,largo,ancho,valorc,impuesto,deuda):
       self.largo = largo
       self.ancho = ancho
       self.valorc = valorc
       self.impuesto = impuesto
       self.deuda = deuda

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

Casa=Datos2(15,12,125000000,1100000,4)
#Casa.tamaño()
#Casa.impuestoa()

class Datos3: 
    pass
    def __init__(self,nombre,duracion,actores,tdpelicula,codpelicula):
       self.nombre = nombre
       self.duracion = duracion
       self.actores = actores
       self.tdpelicula = tdpelicula
       self.codpelicula = codpelicula

    def cambiar (self):
        print("Los Actores Principales son : ", self.actores)


    def hacer(self):
        print("El genero de la pelicula es : ", self.tdpelicula)

Pelicula=Datos3('los locos',200,'Selena Gomez y Tom Cruise','Terror',12345643)
#Pelicula.hacer()
#Pelicula.cambiar()


class Datos4:

    pass
    def __init__(self,tdtrabajo,productos,seguridad,diseño,instalacion):
       self.tdtrabajo = tdtrabajo
       self.productos = productos
       self.seguridad = seguridad
       self.diseño = diseño
       self.instalaciones = instalacion

    def descargar (self):
        print("La bodega almacena productos de :", self.productos)


    def entrar(self):
        print("La empresa encargada de la seguridad es :", self.seguridad)

Bodega=Datos4('distribuidos','aseo','empresa segura','espontaneo','amplias')
#Bodega.descargar()
#Bodega.entrar()

class Datos5:
    
    pass
    def __init__(self,alumbra,color,tamaño,potencia,botones):
       self.alumbra = alumbra 
       self.color = color
       self.tamaño = tamaño
       self.potencia = potencia
       self.botones = botones

    def datos(self):
        print("La lampara alumbra: ",self.alumbra)


    def pot(call):
        print("La potencia de la lampara es: ",call.potencia)

Lampara=Datos5('si','gris',25,15,'si')
#Lampara.datos()
#Lampara.pot()



class Datos6:
 
    pass
    def __init__(self,sirve,megas,fibre,color,capacidad):
       self.sirve = sirve
       self.megas = megas
       self.fibre = fibre
       self.color = color
       self.capacidad = capacidad

    def datos(self):
        print("CAntidad de megas: ",self.megas)


    def colo(call):
        print("Color: ",call.color)

Modem=Datos6('si',100,'si','Blanco',100)
#Modem.datos()
#Modem.colo()


class Datos7:

    pass
    def __init__(self,sirve,megas,fibre,color,freciencia):
       self.sirve = sirve
       self.megas = megas
       self.fibre = fibre
       self.color = color
       self.frecuencia = freciencia
    def datos(self):
        print("Cantidad de megas que distribuye: ",self.megas)

        
    def frec(self):
        print("Color: ",self.frecuencia)
        
Router=Datos7('si',100,'si','Blanco',100)
#Router.datos()
#Router.frec()

class Datos8:
    
    pass
    def __init__(self,color,material,capacidad,nro_bolsillos,marca):
       self.color = color 
       self.material = material
       self.capacidad = capacidad
       self.nro_bolsillos = nro_bolsillos
       self.marca = marca

    def datos(self):
        print("La marca del maletin es: ",self.marca)


    def cap(call):
        print("La capacidad del maletin es: ",call.capacidad)

Maletin=Datos8('negro','cuero sontetico',15,5,'totto')
#Maletin.datos()
#Maletin.cap()



class Datos9:
    

    pass
    def __init__(self,sexo,edad,rh,eps,regimen):
       self.sexo = sexo
       self.edad = edad
       self.rh = rh
       self.eps = eps
       self.regimen = regimen
    def datos(self):
        print("La eps del paciente es: ",self.eps)


    def ed(self):
        print("La edad del paciente es: ",self.edad)

PacienteOncologico=Datos9('Masculino',21,'A+','medimas','contributivo')
#PacienteOncologico.datos()
#PacienteOncologico.ed()

class Datos10:
    pass
    def __init__(self,sexo,marca_purina,color,juega,raza):
       self.sexo = sexo
       self.marca_purina = marca_purina
       self.color = color
       self.juega = juega
       self.raza = raza
    def datos(self):
        print("La raza del gato es: ",self.raza)


    def marca(self):
        print("La marca de purina que le gusta es: ",self.marca_purina)

Gato=Datos10('femenino','whiskas','negro','si','cruzado')
Gato.datos()
Gato.marca()

Gato2 = getattr(Gato,"sexo","Este atributo no existe ")
print(Gato2)
Gato2 = getattr(Gato,"edad","Este atributo no existe ")
print(Gato2)
Gato2 = hasattr(Gato,"color")
print(Gato2)
Gato2 = hasattr(Gato,"hola")
print(Gato2)
Gato2 = getattr(Gato,"sexo","Este atributo no existe ")
print(Gato2)
setattr(Gato,"edad",15)
Gato2 = getattr(Gato,"edad","Este atributo no existe ")
print(Gato2)
delattr(Gato,"sexo")
Gato2 = getattr(Gato,"sexo","Este atributo no existe ")
print(Gato2)