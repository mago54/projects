#Escribe una función llamada que reciba un número como parámetro. La función debe determinar si el
#número es par o impar y devolver True si es par, o False si es impar. Luego, fuera de la función, solicita al
#usuario ingresar un número entero y llama a la función para verificar si el número ingresado es par a
#impar. Muestra en pantalla un mensaje indicando el resultado.
#
#programo F.Equihua Z el 2023/07/11
#
def par_impar(num1):
    es_par=num1 % 2 == 0
        
    return es_par

print()
while 1==1:
    num=float(input("numero a probar: "))
    if num==0:
        break
    else:    
        resultado=par_impar(num)    
        print("El numero proporcionado es par: ",resultado)
        break

print()


print("\nTermino")
