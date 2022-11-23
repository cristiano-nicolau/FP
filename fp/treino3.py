a=float(input("Introduza os litros de gota: "))
preco=a*1.1040
if a>=40:
    preco=preco+(preco*0.10)
 
print(preco)