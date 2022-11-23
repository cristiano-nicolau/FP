print("Introduza 2 numeros para ver qual o maior!(Se num1 e num2 e num3 = 0 => STOP")
max1=int(input("Introduza o num1: "))
max2=int(input("Introduza o num2: "))
max3=int(input("Introduza o num3: "))
while max1!=0 and max2 != 0 and max3 != 0:
    
    if max1>max2 and max1>max3:
        print("O numero maior é ", max1)
    elif max2>max1 and max2>max3:
        print("O numero maior é ", max2)
    elif max3>max1 and max3>max2:
        print("O numero maior é ", max3)
    else:
        print(max1," = ", max2," = ",max3)
        
    print("Introduza 2 numeros para ver qual o maior!(Se num1 e num2 e num3 = 0 => STOP")
    max1=int(input("Introduza o num1: "))
    max2=int(input("Introduza o num2: "))
    max3=int(input("Introduza o num3: "))

