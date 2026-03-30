n = int(input("Digite o tamanho do tabuleiro: "))

for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            print("o", end="")
        else:
            print("*", end="")
    print()