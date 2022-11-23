def max(x1,x2):
    if x1>x2:
        return(x1)
    elif x2>x1:
        return(x2)
    else:
        return(x1)

def max3(x1,x2,x3):
    return(max(max(x1, x2),x3))
    

x1=float(input("Introduza x1"))
x2=float(input("Introduza x2"))
x3=float(input("Introduza x3"))
max9=max(x1,x2)
max10=max3(x1,x2,x3)
print(max10)


