#ccaso if, trabajo: Asignar una calificacion a un estudiante segun su puntaje en un examen
#programo F.Equihua Z el 2023/07/04
#
puntaje=int(input("Puntaje obtenido(0-10): "))


if puntaje==10 or puntaje==9:
    print("calificacion: A")
elif puntaje>=7:    
    print("calificacion: B")
elif puntaje>4:    
        print("calificacion: C")
else:
    print("calificacion: D")

print()
print("termino")