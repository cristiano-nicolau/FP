def main(x,y,target):
    distance1=((x-target)**2)**(1/2)
    distance2=((y-target)**2)**(1/2)
    if distance1>distance2:
        return y
    elif distance1<distance2:
        return x
    else:
        if x<y:
            return x
        elif x>y:
            return y
        else:
            return  "x=Y"

x=float(input("x? "))
y=float(input("y? "))
target=float(input("target? "))
print(main(x,y,target))