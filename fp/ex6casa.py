def precofinal(preco,precoliq):
    iva=((preco-precoliq)*100)/preco
    return iva


x=input("Introduza o nome do produto: ")
y=float(input("Introduz o valor do produto: "))
z=float(input("Introduz o valor liquido do produto: "))
precofinal(y,z)
print("O ", x,"custa ", y," e tem iva de", precofinal(y,z)," %")