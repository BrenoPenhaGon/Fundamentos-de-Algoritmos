cod = int(input("Informe o código do produto: "))
if (cod < 1) and (cod > 15):
    if cod == 1:
        print("Alimento não perecível")
    if (cod >= 2) and (cod <= 4):
        print("Alimento perecível")
    if (cod==5) or (cod==6):
        print("Vestário")
    if (cod==7):
        print("Higiene Pessoal")
    if (cod>=8) or (cod<=15):
        print("Limpeza e utensílios domésticos")
else: print ("Código Inválido")