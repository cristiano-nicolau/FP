def fun(lst):
    s1=0
    s2=0
    s3=0   
    h=len(lst)
    for a in range(len(lst)):
        c=int(lst[a])
        if a == h-1:
            break
        else:
            b=int(lst[a+1])
            s1=b+c
        if s2==0:
            s3=s1
        elif  s1>s3:
            s3=s1
        s2=s3
    return s3 

lst=[]
num=input("Num pa lista. Se num=="" STOP")
while num !="":
    lst.append(num)
    num=input("Num pa lista. Se num=="" STOP")
print(fun(lst))