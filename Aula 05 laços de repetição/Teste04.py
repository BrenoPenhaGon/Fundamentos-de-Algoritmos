soma = 0
while True:
    ent = int(input("Digite um número a ser somado ou 0 para sair: "))
    if ent == 0:
        break
    else:
        soma = soma + ent
print ("Somatória: ", soma)