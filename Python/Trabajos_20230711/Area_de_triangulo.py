#Escribe una función llamada que reciba la base y la altura de un triángulo como parámetros. La función
#debe calcular y devolver el área del triángulo utilizando la fórmula: área = (base * altura)/2. Luego,
#fuera de la función, solicita al usuario ingresar la base y la altura del triángulo y llama a la función para
#obtener el área calculada. Muestra en pantalla el resultado obtenido.
#
#programo F.Equihua Z el 2023/07/11
#
def area_triangulo(base1, altura1):
    area1=base1*altura1/2
    return area1

print()
while 1==1:
    base=float(input("Base del trinagulo: "))
    if base!=0:
        altura=float(input("Altura del trinagulo: "))

    if base== 0 or altura==0:
        print("trinangulo sin superficie")
        break
    area=area_triangulo(base,altura)    
    print("la superficie del triantulo es: ",area)
    break

print("\nTermino")
