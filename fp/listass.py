def funcao(lst):
    a=len(lst)
    d=a-1
    c=lst[0]
    b=lst[d]
    e=b-c
    return e



lst=[]
num=input("Num pa lista. Se num=="" STOP")
c=int(num)
while num !="":
    c=int(num)
    lst.append(c)
    num=input("Num pa lista. Se num=="" STOP")
    
if len(lst)>=2:
    print(lst)
    print("A diferença entre o primeiro e o ultimo elento da lista = ",funcao(lst))
else:
    print("Faltam elementos na lista")
