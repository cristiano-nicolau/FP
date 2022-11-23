import random

def rodaina(min,max):
    valor = random.randrange(min, max)
    return valor

a=int(input("Introduza o numero minimo da rodaina: "))
b=int(input("Introduza o numero maximo da rodaina: "))
num=rodaina(a,b)
x=1
c=int(input("Introduza o seu numero: "))
if c== num:
    print("Acertou na tentativa numero: ",x)
else:
    while c!= num:
        if c<num:
            print("Low")
            x=x+1
        elif c>num:
            print("Hight")
            x=x+1
        c=int(input("Introduza o seu numero: "))
    print("Acertou na tentativa numero: ",x)


