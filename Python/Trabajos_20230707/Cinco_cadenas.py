#programa   Crea una lista e inicializarla con 5 cadenas de caracteres leidas por teclado, Copia los elementos
#           de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla
#programo F.Equihua Z el 2023/07/07
#
cadena1=[]
cadena2=[]
while 1==1:
    cad=input("Proporcione una cadena: ")
    cadena1.append(cad)
    cadena2.append(cad)

    #print(cadena1)    
    if len(cadena1)==5:
        break

#cadena2=cadena1        
cadena2.reverse()
#print("la suma de ",cuenta, " es: ",suma )    
print("Cadenas proporcionadas: ")
print(cadena1)    
print()
print("resultado, cadena invertida: ")
print(cadena2)

print()
print("termino")
