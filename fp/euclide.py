a=float(input("Introduza um numero a: "))
b=float(input("Introduza um numero b: "))
r=a%b
if r==0:
    mdc=b
elif r>0:
    mdc=b%r

print(mdc)