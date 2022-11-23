
def factorial(n):
    f=1
    while n>0:
      f=f*n
      n=n-1
    return(f)

a=int(input("Introduz o  numero que pretende calcular o fatorial: "))
nf=factorial(a)
print(a,"! =", nf)
