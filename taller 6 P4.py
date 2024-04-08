#1----------------------------------------------------
'''
#area de un Circulo posee encapsulamiento total pero no herencia
class Circulo():
    pass
    def __init__(self,radio):
        self.__radio = radio
        self.__pi = 3.1416

    def circulo(self):
        print('El area de un circulo es pi por radio al cuadrado en este caso el radio es de: ',self.__radio,' el area es de: ',self.__AreaCirculo())
    def __AreaCirculo(self):
        return(self.__pi*(self.__radio)**2)

    def get_radio(self):
        return self.__radio
    def get_pi(self):
        return self.__pi

    def set_radio(self,n_radio):
        if type(n_radio) == int or type(n_radio)==float:
            if n_radio > 0 :
                self.__radio = n_radio
            else:
                print('este valor no puede ser negativo')
        else:
            print('el tipo de dato debe ser numerico')

circulo1=Circulo(4)
circulo1.circulo()

#area de un rectangulo posee encapsulamiento parcial y no tiene herencia

class Rectangulo():
    pass
    def __init__(self,altura,base):
        self.altura = altura
        self.__base = base

    def rectangulo(self):
        print('El area de un rectagulo es base por altura en este caso la base mide: ',self.__base,' y la altura: ',self.altura)
        AR = self.__AreaRectangulo()
        print('El area es de : ',AR)

    def __AreaRectangulo(self):
        return(self.altura*self.__base)
     
    def get_base(self):
        return self.__base

    def set_base(self,n_base):
        if type(n_base) == int or type(n_base)==float:
            if n_base > 0 :
                self.__base = n_base
            else:
                print('este valor no puede ser negativo')
        else:
            print('el tipo de dato debe ser numerico')
    


rectangulo1=Rectangulo(4,6)
rectangulo1.rectangulo()

#area de un circulo posee encapsulamiento parcial y herencia

class Cuadrado(Rectangulo):
    pass
    def __init__(self,altura,base):
        super().__init__(altura,base)
        self.__lado = altura

    def cuadrado(self):
        AC = self.__AreaCuadrado()
        print('El area de un cuadrado es alguno de sus lados al cuadrado en este caso el lado mide: ',self.__lado,' y area es de: ',AC)

    def __AreaCuadrado(self):
       return(self.__lado**2)
     
    def get_lado(self):
        return self.__lado

    def set_lado(self,n_lado):
        if type(n_lado) == int or type(n_lado)==float:
            if n_lado > 0 :
                self.__lado = n_lado
            else:
                print('este valor no puede ser negativo')
        else:
            print('el tipo de dato debe ser numerico')

cuadrado1=Cuadrado(4,6)
cuadrado1.cuadrado()

#area de un triangulo tiene encapsulamiento total y no tiene herencia
class Triangulo():
    pass
    def __init__(self,altura,base):
        self.altura = altura
        self.__base = base

    def triangulo(self):
        print('El area de un Triagulo es base por altura dividido 2 en este caso la base mide: ',self.__base,' y la altura: ',self.altura)
        AR = self.__AreaTriangulo()
        print('El area es de : ',AR)

    def __AreaTriangulo(self):
        return(self.altura*self.__base)
     
    def get_base(self):
        return self.__base

    def set_base(self,n_base):
        if type(n_base) == int or type(n_base)==float:
            if n_base > 0 :
                self.__base = n_base
            else:
                print('este valor no puede ser negativo')
        else:
            print('el tipo de dato debe ser numerico')
    


triangulo1=Triangulo(4,6)
triangulo1.triangulo()
'''
#2----------------------------------------------------------





