x=float(input("Introduza o seu peso:"))
y=float(input("Introduza a sua altura:"))
imc=(x)/((y)**2)

if imc<18.5:
    mensagem="baixo peso"
elif 18.5<=imc<=25:
    mensagem="normal"
else:
    mensagem="obesidade"

print("O adulto tem um imc de", imc)
print(mensagem)
