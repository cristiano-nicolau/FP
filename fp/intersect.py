a1=float(input("Intruduza o limite a1 do 1ºlimite"))
b1=float(input("Intruduza o limite b1 do 1ºlimite"))
a2=float(input("Intruduza o limite a2 do 2ºlimite"))
b2=float(input("Intruduza o limite b2 do 2ºlimite"))

if (a1<=a2<b1):
    m=True
elif a1<b2<b1:
    m=True
elif a2<=a1<b2:
    m=True
elif a2<b1<b2:
    m=True
else:
    m=False


print(m)