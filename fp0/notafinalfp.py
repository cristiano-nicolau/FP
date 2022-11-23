ctp=float(input("Introduza a nota da componente teorica:"))
cp=float(input
("Introduza a nota da componente pratica:"))
nota=int((ctp*0.36)+(cp*0.64))
if ctp<6.5 or cp<6.5:
    print("Codigo 66")

if nota<10:
    atpr=float(print("Introduza a nota da componente teorica da epoca de recurso"))
    apr=float(print("Introduza a nota da componente pratica"))
    notarecurso=int(36% max(ctp, atpr) + 64% max(cp, apr))
    print("A nota final de recurso",notarecurso)
elif 10<=nota<=20:
    print("A nota final é de",nota)    
