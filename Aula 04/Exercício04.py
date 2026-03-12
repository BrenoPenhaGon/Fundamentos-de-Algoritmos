altura = float(input("Digite sua altura: "))
sexo = str(input("Qual seu sexo? Digite M para masculino e F para feminino: ")).upper()
if (sexo == "M"):
        peso = (72.7 * altura) - 58
else:
        peso = (62.1 * altura) - 44.7
print (f"Seu peso ideal é {peso:.2f}")