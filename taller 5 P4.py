'''
#1----------------------------------------------------------------------
from curses.ascii import EM


class PersonalUniversitario:
    pass
    def __init__(self,nombre,apellido,telefono,cc,edad,correo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.cc = cc
        self.edad = edad 
        self.correo = correo

            
class Profesor(PersonalUniversitario):
    pass
    def __init__(self, nombre, apellido, telefono, cc, edad, correo,horas,lleva):
        PersonalUniversitario.__init__(self,nombre, apellido, telefono, cc, edad, correo)
        self.horas = horas
        self.lleva = lleva

    def MostrarTiempo(self):
        print('El docente lleva : ',self.lleva,' años, entonces inicio en el año : ', 2022-self.lleva)

   

proa = Profesor('daniel','salinas',31434,12344,21,'danie@',180,10)
proa.MostrarTiempo()

class Alumno(PersonalUniversitario):
    pass
    def __init__(self, nombre, apellido, telefono, cc, edad, correo,carrera,semestre):
        PersonalUniversitario.__init__(self,nombre, apellido, telefono, cc, edad, correo)   
        self.carrera = carrera
        self.semestre = semestre
    
    def MostrarAntiguedad(self):
        print('El alumno lleva : ',self.semestre/2,' años, entonces inicio en el año : ', 2022-int((self.semestre/2)))

a = Alumno('daniel','salinas',31434,12344,21,'danie@','sistema',6)
a.MostrarAntiguedad()

class ProfesorAyudante(Profesor,Alumno):
    pass
    def __init__(self, nombre, apellido, telefono, cc, edad, correo, horas,lleva,carrera,semestre):
        Profesor.__init__(self,nombre, apellido, telefono, cc, edad, correo, horas,lleva)
        Alumno.__init__(self,nombre, apellido, telefono, cc, edad, correo,carrera,semestre)
                
    
   


profe1 = ProfesorAyudante('daniel','salinas',1,1,21,'danie@',180,15,'sistemas',6)
profe2 = ProfesorAyudante('julian','salin',2,2,22,'danie@',180,15,'sistemas',6)
profe3 = ProfesorAyudante('david','sal',3,3,23,'danie@',180,15,'sistemas',6)
profe4 = Profesor('raul','sa',4,4,24,'danie@',180,10)
profe5 = Profesor('jose','s',5,5,25,'danie@',180,12)

profesores = list([profe1,profe2,profe3,profe4,profe5])



def MostrarSueldo():
    for x in profesores:
        if type(x).__name__ == 'Profesor':
            print(x.nombre,' es un ',type(x).__name__,' por tanto gana 15.000 la hora para un total de :',x.horas*15000,' pesos al mes')
        elif type(x).__name__ == 'ProfesorAyudante':
            print(x.nombre,'es un ',type(x).__name__,' por tanto gana 10.000 la hora para un total de :',x.horas*10000,' pesos al mes')
        else :
            print('Esta mal el tipo de profesor   ...')
           

MostrarSueldo()

def MostrarMaterias():
    for x in profesores:
        if type(x).__name__ == 'Profesor':
            print(x.nombre,' es un ',type(x).__name__,' por tanto las materias que dicta son : Matematicas 4 ,Progrmacion 4 , Electronoca Digital')
        elif type(x).__name__ == 'ProfesorAyudante':
            print(x.nombre,'es un ',type(x).__name__,' por tanto las materias que dicta son : Desarrollo del pensamiento logico ,Comunicacines ,Contitucion politica')
        else :
            print('Esta mal el tipo de profesor  ...') 

MostrarMaterias()                 
'''
#2--------------------------------------------------------------

class Trabajo():
    pass
    def __init__(self, puesto, salario, tiempo, deberes, jefe_directo):
        self.puesto = puesto
        self.salario = salario
        self.tiempo = tiempo
        self.deberes = deberes
        self.jefe_directo = jefe_directo 

Trabajo1=Trabajo('gerente',900,4,'manejar el dinero de la sucursal','gerente regional')


class Empleado():
    pass
    def __init__(self,nombre,apellido,telefono,cc,cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.cc = cc
        self.cargo = cargo

Empleado1=Empleado('Daniel','Salinas',314210,10067,'gerente')


class Sancion(Empleado):
    pass
    def __init__(self,nombre,apellido,telefono,cc,cargo,tipo_sancion,castigo):
        super().__init__(nombre,apellido,telefono,cc,cargo)
        self.tipo_sancion = tipo_sancion
        self.castigo = castigo

    def MostrarSancion(self):
        print('El empleado :',self.nombre,' ',self.apellido)
        print('recibira una sancion de ',self.castigo)
        print('por incurrir en el acto de :',self.tipo_sancion)

Sancion1=Sancion('Daniel','salinas',314210,10067,'gerente','llegada tarde','horas extra')
Sancion1.MostrarSancion()


class Vacaciones(Trabajo):
    pass
    def __init__(self, puesto, salario, tiempo, deberes, jefe_directo,t_de_vacaciones):
        super().__init__(puesto,salario,tiempo,deberes,jefe_directo)
        self.t_de_vacaciones = t_de_vacaciones 


    def MostrarVacaciones(self):
        print('En el Cargo de:',self.puesto,' se debe trabajar ',self.tiempo,' al mes')
        print('donde cada 6 meses se le dara unas vacaciones de ',self.t_de_vacaciones)

Vacaciones1=Vacaciones('gerente',900,4,'manejar el dinero de la sucursal','gerente regional','1 semana')
Vacaciones1.MostrarVacaciones()        


class Traslado(Empleado,Trabajo):
    pass
    def __init__(self, nombre, apellido, telefono, cc, cargo, puesto, salario, tiempo, deberes, jefe_directo, motivo,n_puesto):
        Empleado.__init__(self,nombre,apellido,telefono,cc,cargo)
        Trabajo.__init__(self, puesto, salario, tiempo, deberes, jefe_directo)
        self.motivo = motivo
        self.n_puesto = n_puesto 

    def MostrarTraslado(self):
        print('El empleado: ',self.nombre,' solicita un traslado de puesto de trabajo')
        print('Actualmente esta en el Cargo de: ',self.puesto,' y desea reubicarse en el puesto de: ',self.n_puesto)
        print('argumentando que :',self.motivo)
        
Traslado1=Traslado('Daniel','Salinas',314210,10067,'gerente','gerente',900,4,'manejar el dinero de la sucursal','gerente regional','incompatibilidad con el equipo de trabajo','gerente regional')
Traslado1.MostrarTraslado()


class Renuncia(Traslado):
    pass
    def __init__(self, nombre, apellido, telefono, cc, cargo, puesto, salario, tiempo, deberes, jefe_directo, motivo, n_puesto,liquidacion):
        Traslado.__init__(self, nombre, apellido, telefono, cc, cargo, puesto, salario, tiempo, deberes, jefe_directo, motivo,n_puesto)
        self.liquidacion = liquidacion
       

    def MostrarRenuncia(self):
        print('El empleado: ',self.nombre,' presenta su renuncia formal')
        print('y apartir de este momento dejara sus deberes como ',self.puesto,' los cuales concistian en :',self.deberes)
        print('argumentando que :',self.motivo,' y solicitando su debisda liquidacion de ',self.liquidacion)

Renuncia1=Renuncia('Daniel','Salinas',314210,10067,'gerente','gerente',900,4,'manejar el dinero de la sucursal','gerente regional','incompatibilidad con el equipo de trabajo','gerente regional',1500)
Renuncia1.MostrarRenuncia()


class Aumento(Empleado,Trabajo):
    pass
    def __init__(self, nombre, apellido, telefono, cc, cargo, puesto, salario, tiempo, deberes, jefe_directo,n_salario, n_deberes):
        Empleado.__init__(self,nombre,apellido,telefono,cc,cargo)
        Trabajo.__init__(self, puesto, salario, tiempo, deberes, jefe_directo)
        self.n_salario = n_salario 
        self.n_deberes = n_deberes

    def MostrarAumento(self):
        print('El empleado: ',self.nombre,' solicita un aumento en su salario')
        print('Actualmente recibe un salario de : ',self.salario,' por el puesto de: ',self.puesto)
        print('donde cumple los deberes de  :',self.deberes,'el nuevo salario solicitado es de ',self.n_salario)
        print('ya que en los ultimos meses se le han añadido nuevos deberes a su puesto los cuales son :',self.n_deberes) 

Aumento1=Aumento('Daniel','Salinas',314210,10067,'gerente','gerente',900,4,'manejar el dinero de la sucursal','gerente regional','incompatibilidad con el equipo de trabajo','gerente regional',1000,'manejar el dinero de la sucursal de la region')
Aumento1.MostrarAumento()








