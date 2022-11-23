def max(a,b):
    if a>b:
        x=a
    elif a<b:
        x=b
    else:
        x=""
    return x

z=int(input("Introduza o primeiro valor: "))
y=int(input("Introduza o segundo valor: "))
x=max(z,y)
print("O maior numero é: ", x)