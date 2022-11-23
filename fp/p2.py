def countdown(n):
    while n!=0:
        print (n)
        n-=1
    return ""

n=int(input("Introduza um numero deiferente de 0: "))
print(n)
print(countdown(n))