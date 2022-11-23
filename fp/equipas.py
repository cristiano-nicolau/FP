
def adicionarequipa():
    clube=[]
    e=input("Introduza o nome de uma equipa: ")
    while e!="":
        clube.append(e)
        e=input("Introduza o nome de uma equipa: ")
    return clube

def sorteiojogos():
    matches=[]
    for team1 in clube:
        for team2 in clube:
            if team1!=team2:
                matches.append((team1,team2))
    return matches


clube=adicionarequipa()
matches=sorteiojogos()
print(matches)

for team in clube:
    


