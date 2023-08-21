#Escribe un programa que genere la tabla de multiplicar completa del 1 al 10 de un numero dado por el usuario
#programo F.Equihua Z el 2023/07/05
#

numero=int(input("Numero a considerar: "))
cuenta=1

while cuenta<=10:
    valor=numero * cuenta
    print(cuenta,"*",numero,"=",valor )
    cuenta+=1



print()
print("termino")
