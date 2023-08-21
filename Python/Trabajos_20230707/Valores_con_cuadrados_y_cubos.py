#programa   Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)y
#           posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
#programo F.Equihua Z el 2023/07/07
#
import random
numeros=[]
cuarados=[]
cubos=[]

cuenta=1
while cuenta<=10:
    num=int(random.uniform(1,10))
    #print("el numero obtenido es:", num)
    numeros.append(num)
#    cuarados_y_cubos.append(num + ", " + num ** 2, ", " + num ** 3)
    cuarados.append(num**2)
    cubos.append(num**3)

      #  print("el numero ",num," es el par",cuenta, "<<<<<<")
    cuenta+=1

#print("la suma de ",cuenta, " es: ",suma )    
print("numeros obtenidos: ")
print(numeros)    
print()
print("resultado: ")
print("lista de cuadrados")
print(cuarados)
print("lista de cubos")
print(cubos)


print()
print("termino")
