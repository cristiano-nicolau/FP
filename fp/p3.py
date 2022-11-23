def factorial(n):
    if n==0:
        return 1
    elif n>0:
        r=0
        x=0
        while n!=0:
            if x==0:
                r=n
                n-=1
                x+=1
            else:
                r*=n
                n=n-1
        return r


a=int(input("Introduza o numero para fazer o factorial: "))
print(factorial(a))