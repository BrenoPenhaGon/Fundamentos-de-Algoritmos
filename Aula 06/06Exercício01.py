qtde = int(input("Digite a quantidade de números a serem testados: "))
i = 1
total_p = 0

while i <= qtde:
    numero = int(input(f"Digite o número {i}: "))
    if numero > 1:
        divisor = 1
        qtde_d = 0
        while divisor <= numero:
            if numero % divisor == 0:
                qtde_d = qtde_d+1
            divisor = divisor+1
        if qtde_d == 2:
            total_p = total_p+1
    i = i+1
print("Você digitou", total_p, "números primos de um total de", qtde, "números.")