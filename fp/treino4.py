def funcao(n):
    c=[]
    while n!=0:
        c.append(n)
        n-=1
    return c

n=int(input("num: "))
c=funcao(n)
print(c)