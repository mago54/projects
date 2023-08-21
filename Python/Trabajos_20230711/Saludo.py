#programa   Recuperael nombre del usuario y genera un saludo
#programo F.Equihua Z el 2023/07/11
#
#Funcion saludo
def saludo(nombre):
    mensaje=(f"¡hola,{nombre}!")
    return mensaje    

# llamadfa a la funcion
nombre=input("\nIngesa tu nombre: ")
saludo_usuario=saludo(nombre)
print("\n",saludo_usuario)

print("\nTermino")
