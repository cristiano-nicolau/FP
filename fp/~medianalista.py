lst=[]
a=input("Introduza numeros para a lista.(STOP="")")
while a!="":
    a=int(a)
    lst.append(a)
    a=input("Introduza numeros para a lista.(STOP="")")
print(lst)
if len(lst)%2==0:
    b=len(lst)//2
    d=b-1
    mediana=float((lst[b]+lst[d])/2)
elif len(lst)%2!=0:
    mediana=lst[(len(lst)//2)]


print(mediana)
