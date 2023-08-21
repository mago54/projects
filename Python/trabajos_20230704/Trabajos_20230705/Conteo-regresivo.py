#Escribe un program que realice un conteo regresivo del 10 al 1 y en el metodo generar un retrazo 1 segundo
#programo F.Equihua Z el 2023/07/05
#
import time     
cuenta=10

while cuenta>=1:
    print("cuenta: ",cuenta)
    time.sleep(1)
    cuenta-=1

print()
print("termino")
