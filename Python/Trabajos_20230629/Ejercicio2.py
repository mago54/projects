#ejercitando diccionarioas
#programo F.Equihua Z el 2023/06/29
#

import random

num=random.random()
print("random:", num)

#rand int (a,b)

num=random.randint(1,10)
print("random intervalo de enteros:",num)

#uniform (a,b)
num=random.uniform(1.5,5.5)
print("random intervalo de flotantes:",num)

#Choice (escoje)
frutas=["manzana","platano","naraja","pera"]
fruta_aleatoria=random.choice(frutas)

print("seleccoin de fruta aleatoria:",fruta_aleatoria)

#shuffl  (baraja)
frutas=["manzana","platano","naraja","pera"]
print("lista previa:",frutas)
random.shuffle(frutas)
print("lista despues de shuffle:",frutas)

#sample}
baraja=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
mano=random.sample(baraja,7)
print("muestra de casos de la baraja",mano)

#caso de tirar una moneda
volado=["aguila","sol"]
resultado_volado=random.choice(volado)
print("resultado del volado:",resultado_volado)

#caso tirar un dado
dado=[1,2,3,4,5,6]
resultado_dado=random.choice(dado)
print("resultado del dado:",resultado_dado)



print()
print("termino")