#Ejercicio 2. (2 puntos) Crea una clase llamada Cuenta que tendra los siguientes atribulos: 
#       titular (que es una persona) y
#       cantidad (puede tener decimales). 
#   El titular sera obligatorio y la cantidad es opcional. 
#Construye los siguientes metodos para la clase
#Un constructor, donde loa datos pueden estar vacios
#Los setters y gettern para cada uno de los atributos. 
#El atributo no se puede modificar directamente, solo ingresando o retirando dinero
#   mostrar: Muestra los datos de la cuenta
#   ingresacantidad: se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
#       no se hara nada
#   retiracantid: se retira una cantidad a la cuenta. La cueta puede estar en numeros rojos#
#
#programo F.Equihua Z el 2023/09/28
#

class Cuenta:
        #Constructor
        def __init__(self, titular, cantidad=0):
            self.__titular = titular
            self.__cantidad = cantidad
        #Setters y getters
        ## getter method to get the properties using an object
        def get_titular(self):
            return self.__titular

        ## setter method to change the value 'titular' using an object
        def set_nombre(self, titular):
            if titular=="": 
                raise ValueError("favor de proporcionar un titular")   
            print("set_titular")   

            self.__titular = titular
        ## getter method to get the properties using an object
        def get_titular(self):
            return self.__titular
        ## getter method to get the properties using an object
        def get_cantidad(self):
            return self.__cantidad

        ## setter method para ingresar un importe y sumarlo a la cantidad
        def ingresacantidad(self, importe):
            self.__cantidad = self.__cantidad + importe
        ## getter method to get the properties using an object
            return self.__cantidad
        ## setter method para retirar un importe y sumarlo a la cantidad
        def retiracantid(self, importe):
            self.__cantidad = self.__cantidad - importe
        ## getter method to get the properties using an object
            return self.__cantidad

     
        
# ejercitar objeto
print()
P1=Cuenta("Juan",20)

print(P1.get_titular())
print(P1.get_cantidad())
print(P1.get_DNi())

P1.ingresacantidad(32)
print(P1.get_cantidad())

P1.retiracantidad(22)
print(P1.get_cantidad())

P2=Cuenta("",30)

print(P2.get_titular())
print(P2.get_cantidad())


print("\nTerminó")
