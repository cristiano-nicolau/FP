lst=[1,0.884] #dolar para euro
lst2=[1,1.131]  #euro para dolar
lst3=[1,1.334]  #libras para dolar
lst4=[1,0.75]   #dolar para libras 
lst5=[1,1.179]       #libras euro
lst6=[1,0.848]         #euro libras

def cambio(lst,a):
    valor= lst[1]*a
    return valor

a= input("Introduza o pais da sua moeda:(EURO,USA,UK): ")
b= input("Introduza o pais de cambio:(EURO,USA,UK: ")
z=float(input("Introduza o valor que quer cambiar: "))
if (a=="EURO" or a=="UK" or a=="USA") and(b=="EURO" or b=="UK" or b=="USA"):   
    if a== "EURO":
        if b=="UK":
            c = cambio(lst6,z)
        elif b=="USA":
            c= cambio(lst2,z)
    if a=="USA":
        if b=="EURO":
            c=cambio(lst,z)
        elif b=="UK":
            c=cambio(lst4,z)
    if a=="UK":
        if b=="EURO":
            c=cambio(lst5,z)
        elif b=="USA":
            c=cambio(lst3,z)
else:
    print("ERRO, o pais introduzido nao foi encontrado, tente novamente.")

print("A sua quantia de dinheiro: ", z," do seu pais ", a," equivale a ", c," no pais de cambio escolhido: ",b )


