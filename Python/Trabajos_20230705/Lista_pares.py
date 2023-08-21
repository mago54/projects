#Escribe un programa que sume todos los elementos pares de una lista de 20 numeros entre el cero y el cien generados aleatoriamente
#programo F.Equihua Z el 2023/07/05
#
import random
numeros=[]
pares=[]
suma=0
cuenta=1
while cuenta<=20:
    num=int(random.uniform(0,100))
    print("el numero obtenido es:", num)
    numeros.append(num)
    if num % 2 == 0:
        suma=suma + num
      #  print("el numero ",num," es el par",cuenta, "<<<<<<")
        pares.append(num)
        cuenta+=1

#print("la suma de ",cuenta, " es: ",suma )    
print("numeros obtenidos: ")
print(numeros)    
print()
print("lista de pares: ")
print(pares)
print()
print("la suma es: ", suma)

print()
print("termino")
