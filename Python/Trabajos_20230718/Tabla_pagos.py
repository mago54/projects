#Una persona adquinio un preducto para pagar en 20 meses. ti primer mes pago 10 €, el segundo
#20 €, el tercero 40 €y asi sucesivamente Realitar un algoritmo para determinar cuanto debe pagar mensualmente y el total
#de lo que pago después de las 20 meses.
#
#programo F.Equihua Z el 2023/07/18
#


def Calculo_pagos():
    mensualidad=[]
    num_tab=20
    monto_pago=5
    total=0
    print("\nCalcular la tabla de pagos para:",num_tab, "meses")
    cuenta=0
    while cuenta<num_tab:
            cuenta=cuenta+1
            monto_pago=monto_pago*2
            total=total+monto_pago
            mensualidad.append(f"{monto_pago:,}")
    
    print("\nel monto por cada mensualidad es:\n")
    print(mensualidad)
    print(f"y el importe total es: {total:,}")
    return 


print()

Calculo_pagos()

print()
print("\nTermino")
