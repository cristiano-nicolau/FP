import random


def dado():
    valor = random.randrange(1, 16)
    lst.append(valor)  
    return lst


x=input("Quer rodar um dado de 1 a 16?(sim/nao): ")
lst= []
while x!="nao" or x=="sim":
    if x=="sim":
        lst=dado()
        print("Os valores obtidos ao rodar o dado formam:",lst)
    elif x=="nao":
        print("Pode fechar o programa, ou rodar o dado")
    else:
        print("Erro. opção incorreta. Introduza uma opção correta.")
        print("Os valores obtidos ao rodar o dado formam:",lst)

    x=input("Quer rodar um dado de 1 a 16?(sim/nao): ")










