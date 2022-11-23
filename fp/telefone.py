# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    contactopartname = {}
    for num, name in contacts.items():
        if partName.lower() in name.lower():
            contactopartname[num] = name
    return contactopartname


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op=="A":
            a=input("Introduza o nome do novo contacto: ")
            b=input("Introduza o seu numero: ")
            if b in contactos:
                print("Este número já está nos contactos. Responda S para substituir o número atual")
                if input().upper() != "S":
                    return None
            contactos[b]=a
        elif op=="R":
            c=input("Introduza o numero que deseja remover: ")
            if c in contactos:
                contactos.pop(c)
            else:
                print("O numero que deseja remover nao se encontra na lista telefonica.")
        elif op=="N":
            d=input("Introduza o  numero que deseja procurar: ")
            if d in contactos:
                print(contactos.get(d,d))
            else:
                print("Nao existe nenhum contacto com este numero")
        elif op=="P":
            partName = input("Nome: ")
            print()
            print("Correspondências:")
            listContacts(filterPartName(contactos, partName))
        else:
            print("Não implementado!")
            
        
            




    

# O programa começa aqui
main()

