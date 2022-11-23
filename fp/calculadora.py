def ffunction(num1,num2,ch):
    if ch=="+":
        resul=num1+num2
    elif ch=="-":
        resul=num1-num2
    elif ch=="*":
        resul=num1*num2
    elif ch==":":
        resul=num1/num2
    return resul

lst=["+","-",":","*"]
ligar=input("Ligar Calculadora? (ON/OFF)")
if ligar=="ON":
    num1=float(input("Introduza num1: "))
    num2=float(input("Introduza num2: "))
    ch=input("Introduza o caracter: (+/-/:/*)(? == Desligar calculadora) ")
    if ch in lst:
        while ch!="?":
            print(num1, ch, num2 ,"=", ffunction(num1,num2,ch))
            num1=float(input("Introduza num1: "))
            num2=float(input("Introduza num2: "))
            ch=input("Introduza o caracter: (+/-/:/*)(? == Desligar calculadora) ")
    else:
        print("Ch invalido")
        ch=input("Introduza o caracter: (+/-/:/*)(? == Desligar calculadora) ")
        while ch!="?":
            print(num1, ch, num2 ,"=", ffunction(num1,num2,ch))
            num1=float(input("Introduza num1: "))
            num2=float(input("Introduza num2: "))
            ch=input("Introduza o caracter: (+/-/:/*)(? == Desligar calculadora) ")
elif ligar=="OFF":
    exit