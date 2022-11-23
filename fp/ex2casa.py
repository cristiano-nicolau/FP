def precofinal(preco,iva):
    precofinal= preco*iva*preco
    return precofinal


x=input("Introduza o nome do produto: ")
y=float(input("Introduz o valor do produto: "))
z=float(input("Introduz o valor do iva: "))
precofinal(y,z)
print("O ", x,"custa ", precofinal(y,z))