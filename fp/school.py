
# Complete o programa!

# a)
def loadFile(fname):
    lst = []
    with open(fname, "r") as values:
        for line in values:
            if line[0].isnumeric():
                value_list = line.split("\t")
                value_list[0] = int(value_list[0])
                lst.append(tuple(value_list))
    return lst

# b)
def notaFinal(reg):
    nota1 = float(reg[-1])
    nota2 = float(reg[-2])
    nota3 = float(reg[-3])
    return (nota1 + nota2 + nota3) / 3

# c)
def printPauta(lst):
    print("Numero{:^100}Nota".format("Nome"))
    for reg in lst:
        print("{:>6}{:^100}{:4.1f}".format(reg[0], reg[1], notaFinal(reg)))

# d)
def main():
    # ler o ficheiro
    lst = loadFile("C:/Users/cccri/OneDrive/Documentos/1semestre 1 ano/fp/Aulas/aula06/school1.csv")
    
    # ordenar a lista
    lst.sort()
    # mostrar a pauta
    printPauta(lst)

# Call main function
main()