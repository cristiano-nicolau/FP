lst=[98,32,53,43]
n=0
for val in lst:
    print(n,val)
    n=n+1

print("------------------")
nn=0
while nn<len(lst):
    print(nn,lst[nn])
    nn=nn+1

print("------------------")

s=0
i=5
while i>=0:
    s+=2*i
    i-=1

print(s)
print(i)
print("------------------")
s=0
for i in range(5):
    s+=2

print(s)
print(i)
print("------------------")


def f1(a,b):
    print(a)
    print(b)
    if a>b:
        return a
    else:
        return b


def f2(k):
    s=0
    for i  in range(k):
        s+=1
    return s
x=2
y=3
z=f1(y,x)
print(z)
print(f2(z))    

print("------------------")


def addem(x,y,z):
    print(x+y+z)


addem(1,2,3)



print("------------------")

lsta=[1,2,3,4,5]
lstb=[6,7,8,9,10]

print(lsta[-2])
print(lsta[2]+lstb[1])
print(len(3*lsta))
lstc=2* lsta[1::3]+lstb[:2]
print(lstc)
for i in lstc:
    print(i,end=",")
print()


