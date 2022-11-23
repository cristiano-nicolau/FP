def max(x,y):
    if x==y:
        return x,y
    elif x>y:
        return x
    else:
        return y

def max2(x,y,z): 
    if (x==y) and (x==z):
        return x,y,z
    elif (x>y and x>z):
        return x
    elif (y>x and y>z):
        return y
    elif (z>x and z>y):
        return z


def main():
    a=input("Introduza o numero  de numeros que vai introduzir (2) ou (3) ou (0):")
    if a=="0":
        return ""
    while a!="0":
        if a=="0":
            return ""
        if a=="2":
            x=int(input("Introzuda o 1 numero: "))
            y=int(input("Introzuda o 2 numero; "))
            print (max(x,y)," é o maior numero")
        elif a=="3":
            x=int(input("Introzuda o 1 numero: "))
            y=int(input("Introzuda o 2 numero: "))
            z=int(input("Introzuda o 3 numero: "))
            print (max2(x,y,z)," é o maior numero")
        a=input("Introduza o numero  de numeros que vai introduzir (2) ou (3) ou (0):")

main()

