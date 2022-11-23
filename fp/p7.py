def jogos(lst):
    matches=[]
    for equipa1 in lst:
        for equipa2 in lst:
            if equipa1!=equipa2:
                matches.append((equipa1,equipa2))
    return matches

def printTable(dic):
    print("{:10} | {} | {} | {} | {} | {} | {} | {}".format("Equipa", "Vitórias", "Empates", "Derrotas", "Golos Marcados", "Golos Sofridos", "Diferença de golos", "Pontos"))
    for team in dic:
        print("{:10} | {:^8} | {:^7} | {:^8} | {:^14} | {:^14} | {:^20} | {:^6}".format(team, dic[team][0], dic[team][1], dic[team][2], dic[team][3], dic[team][4], dic[team][5],dic[team][6]))

def setchampion(dic):
    champion = list(dic)[0]
    for team in dic:
        if dic[team][6] > dic[champion][6]:
            champion = team
        elif dic[team][6] == dic[champion][6] and dic[team][5] > dic[champion][5]:
            champion = team
    return champion

def resultados(jogo,lst):
    resultado={}
    tabela={}
    for team in lst:
        tabela[team] = [0,0,0,0,0,0,0]

    for i in jogo:
        print("Jogo: ")
        print("Equipa 1: ",i," :Equipa 2")
        a=int(input("Golos da equipa 1: "))
        b=int(input("Golos da equipa 2: "))
        d1=a-b
        d2=b-a
        resultado[i]=a,b

        tabela[i[0]][3]+=a
        tabela[i[0]][4]+=b
        tabela[i[0]][5]+=d1

        tabela[i[1]][3]+=b
        tabela[i[1]][4]+=a
        tabela[i[1]][5]+=d2

        if a>b:
            tabela[i[0]][0]+=1
            tabela[i[0]][6]+=3
            tabela[i[1]][2]+=1
        elif b>a:
            tabela[i[1]][0]+=1
            tabela[i[1]][6]+=3
            tabela[i[0]][2]+=1
        elif a==b:
            tabela[i[0]][1]+=1
            tabela[i[0]][6]+=1
            tabela[i[1]][1]+=1
            tabela[i[1]][6]+=1
    return resultado,tabela

#tabela={slb:vitoria,empates,derrotas,gm,gs,dg,pontos}

def main():
    lst=[]
    a=input("Introduza uma equipa para adicionar a lista (stop=''): ")
    while a!="":
        lst.append(a)
        a=input("Introduza uma equipa para adicionar a lista (stop=''): ")
    calendario=jogos(lst)
    resultado,tabela=resultados(calendario,lst)
    campeao=setchampion(tabela)
    print()
    print(calendario)
    print()
    print(resultado)
    print()
    print()
    print("Grande Camapeao: ", campeao)
main()

