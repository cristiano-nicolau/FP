def countdigits(x):
    a=0
    for c in x:
        if c.isdigit():
            a+=1
    return a        


a=input("Intoduza uma string pra contar os digitos: ")
print(countdigits(a))