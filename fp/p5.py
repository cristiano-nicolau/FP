def countlower(lst,v):
    n=0
    for i in lst:
        if v>i:
            n+=1
    return n

def minmax(lst):
    max1=0
    min1=0
    for i in lst: 
        if lst[0]==i:
            min1=i
        if i>max1:
            max1=i
        elif i<min1:
            min1=i
    return max1,min1


def main(lst):
    max1,min1=minmax(lst) 
    media=(max1+min1)/2 
    n=countlower(lst,media)
    return media, n

lst=[]
a=input("Introduza nr para a lista (stop=''): ")
while a!="":
    a=int(a)
    lst.append(a)
    a=input("Introduza nr para a lista (stop=''): ")
b=int(input("Introduza o valor  de v: "))

print("OS numeros escolhidos foram: ")
print(lst)
print("Inseriu ",len(lst)," numeros.")
print()

print(countlower(lst,b), " elementos da lista sao menores que v!")
print()

max1,min1=minmax(lst)
print(max1, " é maximo da lista.")
print(min1, " é minimo da lista.")
print()

media, n= main(lst)
print(media, " é a média entre o maximo e o minimo da lista.")
print(n, " elementos da lista sao menores que a media!")
print()

