cod = int(input("Digite o código do produto: "))
preço = float(input("Digite o preço do produto: "))
if (cod>=1) and (cod<=30):
    if (cod == 1):
        proc = "Sul"
    if cod == 2:
        proc = "Norte"
    if cod == 3:
        proc = "Leste"
    if cod == 4:
        proc = "Oeste"
    if (cod==5) or (cod==6):
        proc = "Nordeste"
    if (cod>=7) and (cod<=9):
        proc = "Sudeste"
    if (cod>=10) and (cod<=20):
        proc = "Centro Oeste"
    if (cod>=25) and (cod<=30):
        proc = "Noroeste"
    print (f"O preço do seu produto custa R${preço:.2f} e tem procedência de {proc}")
else:
    print("Produto importado")