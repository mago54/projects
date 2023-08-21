#Programa que calcule el interés de una cantidad si es mayor al 30%, sino informa el importe total.
#
#programo F.Equihua Z el 2023/07/12
#
def calcula_interes(num1,porc):
    importe=num1*porc/100
    total=num1+importe    
    if porc <= 30:
        importe=total

    return importe

print()
while 1==1:
    entrada=input("catidad: ")
    entrada1=entrada
    entrada1=entrada1.replace("-","")
    #print(">>>>>>>>",entrada1)
    print()
    if entrada1.isnumeric()==True:
        num=float(entrada)
        por1=input("porcentaje interes: ")
        if por1.isnumeric()==True:
            por=float(por1)
            importe=calcula_interes(num,por)    
            print("El importe es de: ",importe)
            break
        if  por1=='':
            break
        else:    
            print("favor de proporcionar un porcentaje")
            break
    elif  entrada=='':
        break
    else:    
        print("favor de proporcionar un immporte")
        
 
print()
print("\nTermino")
