x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
def multiplo (x, y):
    if x %y == 0 or y %x == 0:
        print(True)
    else: print(False)

multiplo (x,y)