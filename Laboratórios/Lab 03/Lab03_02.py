a = float(input("Digite o valor do primeiro produto: "))
b = float(input("Digite o valor do segundo produto: "))
c = float(input("Digite o valor do terceiro produto: "))
soma = a+b+c
if soma > 500:
    preço = soma*0.2
else:
    preço = soma*0.1
print(f"Desconto: {preço:.2f}")