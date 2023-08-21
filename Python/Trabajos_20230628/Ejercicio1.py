#ejercitando diccionarioas
#programo F.Equihua Z el 2023/06/28
#
diccionario_colores={"Rojo":"#FF0000", "Verde":"#00FF00", "Azul":"0000FF"}

print("diccionario 1", diccionario_colores)

# Acceso a elementos de un diccionario 
print("Valor rojo:", diccionario_colores["Rojo"])

#Modificación de diccionarios

diccionario_colores["Rojo"]="#FF3333"
diccionario_colores["Amarillo"]="FFFF00"

print("diccionario 2",diccionario_colores)

del diccionario_colores["Verde"]

print("diccionario 3",diccionario_colores)

diccionario={"a":1,"b":2,"c":3}
print("diccionario 4",diccionario)

claves=diccionario.keys()
print("claves diccionario", claves)

valores=diccionario.values()
print("claves diccionario", valores)

items1=diccionario.items()
print("items diccionario", items1)

#metodo get
valor=diccionario.get("b")
print("valor de b",valor)

valor=diccionario.get("d",0)
print("valor de d",valor)

#operador in
existe ="b" in diccionario
print("verifica si existe b ",existe)

existe ="d" in diccionario
print("verifica si existe d ",existe)

#metodo pop 
valor1=diccionario.pop("b")
print("valor reccuperado clave b", valor1)
print(diccionario)

#metodo update
diccionario1={"a":1, "b":2}
diccionario2={"c":3,"d":4}
diccionario1.update(diccionario2)
print(diccionario1)

print()
print("termino")