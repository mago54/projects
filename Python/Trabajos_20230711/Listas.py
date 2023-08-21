#Escribe una función que reciba dos listas como parámetros. La función debe concatenar las dos listas y
#devolver la lista resultante. Luego, fuera de la función, solicita al usuario ingresar los elementos de dos
#listas separados por espacios y llama a la función pasando las dos listas ingresadas. Muestra en pantalla
#la lista concatenada obtenida.
#
#programo F.Equihua Z el 2023/07/11
#
primera=[]
segunda=[]
def concatena_listas(lista1, lista2):
    uno=lista1.split(",")
    dos=lista2.split(",")
    listaf=uno + dos
    return listaf

print()
while 1==1:
    primera=input("Lista 1: ")
    if  len(primera) !=0:
        segunda = input("Lista 2: ")

    if len(primera)== 0 or len(segunda)==0:
        print("las dos listas deben tener datos")
        break
    res=concatena_listas(primera,segunda)    
    print("la lista resultante es: ",res)
    break

print("\nTermino")
