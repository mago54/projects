#que imprima si el número ingresado esta en el rango de 1 a 7.
#
#programo F.Equihua Z el 2023/07/12
#
def esta_en_rango(num1):
    esta_rango=num1>=1 and num1<=7 
        
    return esta_rango

print()
while 1==1:
    entrada=input("numero a probar: ")
    entrada1=entrada
    if entrada1.rfind("-")!=-1:
        entrada1=entrada1.replace("-","")

    if entrada1.rfind("+")!=-1:
        entrada1=entrada1.replace("+","")

    if entrada1.rfind(".")!=-1:
        entrada1=entrada1.replace(".","")
        
    #print(">>>>>>>>",entrada1)
    print()
    if entrada1.isnumeric()==True:
        num=float(entrada)
        resultado=esta_en_rango(num)    
        print("El numero proporcionado esta en el rango: ",resultado)
        break
    elif  entrada=='':
        break
    else:    
        print("favor de proporcionar numeros")
        
 
print()
print("\nTermino")
