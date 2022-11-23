import random
def npc():
    lst=["pedra","papel","tesoura"]
    a=random.randrange(0,2)
    pc=lst[a]
    return pc

a = input("pedra; papel; tesoura: (se quiser parar nao escreva nada): ")
b = npc()
x=0
y=0
while a != "":
    if (a=="papel" and b=="papel") or (a=="pedra" and b=="pedra") or (a=="tesoura" and b=="tesoura"):
        print("voce", a, " : ", b," PC")
        print("Empate")
    elif (a=="papel" and b=="pedra") or (a=="pedra" and b=="tesoura") or (a=="tesoura" and b=="papel"):
        print("voce", a, " : ", b," PC")
        print("Voce Ganhou")
        x=x+1
    elif (b=="papel" and a=="pedra") or (b=="pedra" and a=="tesoura") or (b=="tesoura" and a=="papel"):
        print("voce", a, " : ", b," PC")
        print("PC Ganhou")
        y=y+1

    b=npc()
    a= input("Pedra; Papel; Tesoura: (se quiser parar nao escreva nada): ")

print("Resultado final:")
print("Voce: ",x," : ",y," PC")