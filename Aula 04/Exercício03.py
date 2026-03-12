valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
valor3 = float(input("Digite outro valor: "))
if (valor1 >= valor2) and (valor1 >= valor3):
    maior = valor1
elif (valor2 >= valor1) and (valor2 >= valor3):
    maior = valor2
elif (valor3 >= valor1) and (valor3 >= valor2):
    maior = valor3
if (valor1 <= valor2) and (valor1 <= valor3):
    menor = valor1
elif (valor2 <= valor1) and (valor2 <= valor3):
    menor = valor2
elif (valor3 <= valor1) and (valor3 <= valor2):
    menor = valor3
medio = (valor1 + valor2 + valor3 - maior - menor)
print (f"A ordem é: {maior:.2f}, {medio:.2f} e {menor:.2f}")