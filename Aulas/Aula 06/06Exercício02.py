L = int(input("Informe a quantidade de linhas: "))
C = int(input("Informe a quantidade de colunas: "))

for i in range(1, L+1):
    for j in range(1, C+1):
        if i == 1 or i == L or j == 1 or j == C:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()