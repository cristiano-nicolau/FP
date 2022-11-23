def function(PF,IMP,SPA,Lucro):
    PC = (PF + Lucro) * (100% + IMP) + SPA
    return PC

PF=float(input("Custo de produção: "))
IMP=float(input("Taxa de iva: "))
SPA=float(input("Taxa para compensar os autores pelas cópias: "))
Lucro= float(input("Lucro por livro: "))
print("Custo de capa do livro: ",function(PF,IMP,SPA,Lucro))