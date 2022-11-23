Corner={1:["a","h"] , 8:["a","h"]}
Border={"a":[2,3,4,5,6,7],"h":[2,3,4,5,6,7]}
Border2={1:["b","c", "d", "e", "f", "g"],  8:["b","c", "d", "e", "f", "g"]}
a1=int(input("Numero 1-8: "))
a2=input("letra: ")
x=0
for a3,a4 in Corner.items():
    if a1 == a3:
        if a2 in a4:
            print("Corner")
            x+=1
for a3,a4 in Border.items():
    if a2 == a3:
        if a1 in a4:
             print("Border")
             x+=1
for a3,a4 in Border2.items():
    if a1 == a3:
        if a2 in a4:
            print("Border")
            x+=1
if x==0:
    print("Inside")

