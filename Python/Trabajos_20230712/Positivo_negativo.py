#Programa que imprima si el número es positivo o negativo
#
#programo F.Equihua Z el 2023/07/12
#
def pos_neg(num1):
    es_positivo=num1 >= 0
        
    return es_positivo

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
        resultado=pos_neg(num)    
        print("El numero proporcionado es positivo: ",resultado)
        break
    elif  entrada=='':
        break
    else:    
        print("favor de proporcionar numeros")
        
 
print()
print("\nTermino")
