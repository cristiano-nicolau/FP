def function(x):
    sigla=""
    for c in x:
        if c.isupper():
            sigla=sigla+c   
    return sigla


a = input("Introduza um nome para criar uma versão abreviada, formada apenas pelas letras maiúsculas: ")
print(function(a))