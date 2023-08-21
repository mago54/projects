# vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los 
#vsiguientes metodo para la clase
# Un constructor, donde los datos pueden estar vacios
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos
# mostrar: Muestra los datos de la persona
#
#programo F.Equihua Z el 2023/08/15
#

class Persona:
        #Constructor
        def __init__(self, nombre, edad=0, DNi=""):
            self.__nombre = nombre
            self.__edad = edad
            self.__DNi = DNi
        #Setters y getters
        ## getter method to get the properties using an object
        def get_nombre(self):
            return self.__nombre

        ## setter method to change the value 'a' using an object
        def set_nombre(self, nombre):
            if nombre=="": 
                raise ValueError("favor de proporcionar un nombre")   
            print("set_nombre")   

            self.__nombre = nombre
        ## getter method to get the properties using an object
        def get_nombre(self):
            return self.__nombre

        ## setter method to change the value 'a' using an object
        def set_edad(self, edad):
            self.__edad = edad
        ## getter method to get the properties using an object
        def get_edad(self):
            return self.__edad

        ## setter method to change the value 'a' using an object
        def set_DNi(self, DNi):
            self.__DNi = DNi
    
        ## getter method to get the properties using an object
        def get_DNi(self):
            return self.__DNi

        
# ejercitar objeto
print()
P1=Persona("Juan",20,"123456")

print(P1.get_nombre())
print(P1.get_edad())
print(P1.get_DNi())

P1.set_edad(22)
print(P1.get_edad())

P2=Persona("",30,"987654")

print(P2.get_nombre())
print(P2.get_edad())
print(P2.get_DNi())


print()
print("\nTerminó")
