x1 = float(input("Litros de combustivel:"))
preço= x1*1.40
if x1>=40:
    preço=preço*0.90
else:
    preço=preço

print("O preço a pagar pelos",x1,"litros de gasolina é de",preço,"$")
