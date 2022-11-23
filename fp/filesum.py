from tkinter import filedialog
from tkinter.constants import X

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #name = input("File? ")                                  #A
    name = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    # Complete a função para ler números do ficheiro e devolver a sua soma.
    x=0
    with open(filename, "r") as numbers:
        for line in numbers:
            x += float(line)
    return  x



if __name__ == "__main__":
    main()

