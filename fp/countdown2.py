def risk(age,sex):
    if age<=10:
        r="a" 
    elif age<=15:
        if sex==True:
            r="a"
        else:
            r="b"
    elif age<=40:
        r="b"
    else:
        r="c"
    return r




def main():
    age=int(input("IDADE: "))
    sex=input("sexo= male/female")
    print(risk(age,sex=="male"))

main()

    