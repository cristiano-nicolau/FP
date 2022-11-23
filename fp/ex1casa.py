def anos(ano):
    idade_2030=2021-ano
    return idade_2030


x=input("Introduza o seu nome: ")
y=int(input("Introduza o ano em que nasceu: "))
anos(y)
print(x,"em 2021 terá,", anos(y))
