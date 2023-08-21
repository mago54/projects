#casos break y continue
#programo F.Equihua Z el 2023/07/05
#
#ejercicio 1 uso del break

frutas=["manzana","platano","naranja","kiwi","sandia"]
for fruta in frutas:   
    if fruta == "kiwi":
        break
    print(fruta)

#ejercicio 2 uso del continue
numeros=[1,2,3,4,5]
for numero in numeros:
    if numero %2==0:
        continue
    print(numero)
    
print()
print("termino")