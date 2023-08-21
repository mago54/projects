#Realizar un ejemplo de menu, donde podemos escoger las distintas opciones hasta que
#seleccionamos la opción de "Salir".
#
#programo F.Equihua Z el 2023/07/13
#
def opcion_a():
    print("\nse ejecutó la opcion A\n")
        
    return 
def opcion_b():
    print("\nse ejecutó la opcion B\n")
        
    return 
def opcion_c():
    print("\nse ejecutó la opcion C\n")
        
    return 
def opcion_d():
    print("\nse ejecutó la opcion D\n")
        
    return 
def opcion_e():
    print("se ejecutó la opcion e\n")
        
    return 

print()

while 1==1:
    opcion=input("Opcion A\nOpcion B\nOpcion C\nOpcion D\nOpcion E\nSalida S\n   Seleccion: ")
    
    if len(opcion)>0:
        c=opcion[0].upper()
    else:
        c="S"
    #print (">>>>>>",c)

    if c=="A":
        opcion_a()
        continue
    elif c=="B":
        opcion_b()
        continue
    elif c=="C":
        opcion_c()
        continue
    elif c=="D":
        opcion_d()
        continue
    elif c=="E":
        opcion_e()
        continue
    elif c=="S":
        break
    else:
        print("favor de seleccionar una de los opciones indicadas")


print()
print("\nTermino")
