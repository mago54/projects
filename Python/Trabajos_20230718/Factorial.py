#Crea una aplicación que pida un numero y caicule su factorial (El tactorial de un nümero es el
#producto de todos los enteros entre 1 y el proplo nůmero y se representa por el nómero segulde de un signo de
#exclamacion, Por ejemplo 51 1x2x3x4i6- 120).
#
#programo F.Equihua Z el 2023/07/13
#
def factorial_a_buscar():
    num_factorial=input("Numero para factorial: ")
    num_factorial1=num_factorial
    if num_factorial.rfind("-")!=-1:
        num_factorial1=num_factorial1.replace("-","")

    if num_factorial.rfind("+")!=-1:
        num_factorial1=num_factorial1.replace("+","")

    if num_factorial.rfind(".")!=-1:
        num_factorial1=num_factorial1.replace(".","")
    
    #print(">>>>>>>>",num_primos1)
    if num_factorial1.isnumeric()==True:
        num_fact=int(num_factorial)
    else:
        num_fact=0
        
    return num_fact


def Calculo_fatorial_n():
    print("\ncalcula el factorial hastan:",num_f)
    cuenta=0
    factorial=1
    while cuenta<num_f:
            cuenta=cuenta+1
            factorial=factorial*cuenta
            factoriales.append(f"{factorial:,}")        

    return factorial

print()
factoriales=[]
num_f=factorial_a_buscar()

Calculo_fatorial_n()

print(factoriales)    

print()
print("\nTermino")
