#Mostrar en pantalla los N primero nimero primos.Se pide por teclado la cantidad de nümeros
#primes que queremos mostrar.
#
#programo F.Equihua Z el 2023/07/13
#
def primos_a_buscar():
    num_primos=input("Numero de primos a buscar: ")
    num_primos1=num_primos
    if num_primos1.rfind("-")!=-1:
        num_primos1=num_primos1.replace("-","")

    if num_primos1.rfind("+")!=-1:
        num_primos1=num_primos1.replace("+","")

    if num_primos1.rfind(".")!=-1:
        num_primos1=num_primos1.replace(".","")
    
    #print(">>>>>>>>",num_primos1)
    if num_primos1.isnumeric()==True:
        num_prim=int(num_primos)
    else:
        num_prim=0
        
    return num_prim 

def es_primo(num1):
    if num1<=2:
        primos.append(num1)
        print("caso inicial de: ",num1)
        return False
    j=1
    while j < num1-1:
        j = j + 1
        print("ciclo de j= ",j)
        if num1 % j==0:
            return False

    print(num1, "es primo")
    primos.append(num1)
    return True

def Calculo_n_primos():
    print("\ncalcula los primos solicitados hasta:",num_p)
    cuenta=0
    while cuenta<num_p:
            cuenta=cuenta+1
            es_primo(cuenta)
                    

    return primos 

print()
primos=[]
num_p=primos_a_buscar()

Calculo_n_primos()

print(primos)    

print()
print("\nTermino")
