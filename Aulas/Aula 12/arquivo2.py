arquivo = open("Aulas/Aula 12/teste.txt", "r")

for linha in arquivo.readlines():
    print(linha)
arquivo.close()