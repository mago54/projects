#programa   Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
#           [comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota mås alta que ha sacado y
#           la menor
#programo F.Equihua Z el 2023/07/07
#
notas1=[]
while 1==1:
    nota=int(input("Proporcione una nota (entre 0 y 10): "))
    if nota>= 0 and nota<=10:
        notas1.append(nota)
    else:    
        print("debe estar entre 0 y 10")

    if len(notas1)==5:
        break

print("Notas proporcionadas: ")
print(notas1, "\n")    
print("resultado")
print("media:", sum(notas1)/len(notas1))
print("la mas alta:", max(notas1) )
print("la mas abja:", min(notas1) )
print()
print("termino")
