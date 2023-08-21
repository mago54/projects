#ccaso if, trabajo: Calcular el promedio de los valores en una lista y determinar si es mayo, igual o menor a un valor especifico 
#programo F.Equihua Z el 2023/07/04
#
lista1=[1,4,3,6,7,2,10,15,3]
#limite=8
#limite=4
#limite=sum(lista1)/len(lista1)
limite=3

prom=sum(lista1)/len(lista1)

if prom == limite:
    print(f"El promedio: {prom:.3f} es igual al limite: {limite:.3f}" )
elif prom > limite:
    print(f"El promedio: {prom:.2f} es mayor al limite: {limite:.0f}" )
else:
    print(f"El promedio: {prom:.2f} es menor al limite: {limite:.0f}" )

print()
print("termino")