n = int(input("Informe o tamanho da tabela quadrada: "))

for i in range(n):
    for j in range(n):
        if (i>j) %2 == 0:
            print("@", end="")
        else:
            print("$", end="")
    print()