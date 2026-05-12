import ast

def start():
    print("\n" \
    "-----------------------------------------Bem Vindo ao FEITV-----------------------------------------\n" \
    "---------Este é um projeto universitário para a disciplina de Fundamento de Algoritmos 2026---------\n" \
    "------------------O projeto busca criar uma plataforma de streaming simplificada,-------------------\n" \
    "--------------------para isso usamos a linguagem de programação python para isso--------------------\n" \
    "\n")

    inicio()

# -----------START
def inicio():
    hudinicial = int(input("\n" \
    "----- FEITV -----\n" \
    "----> Digite 1 para fazer cadastro.\n" \
    "----> Digite 2 para fazer login.\n"))
    if hudinicial == 1:
        cadastro()
    if hudinicial == 2:
        login()

# -----------CADASTRO
def cadastro():
    while True:
        nome = str(input("----> Digite seu nome: "))
        email = str(input("----> Digite seu email: "))
        senha = str(input("----> Digite sua senha: "))
        usuario = {"nome" : nome,
                   "email" : email,
                   "senha" : senha}
        if nome.strip() and email.strip() and senha.strip():
            arquivo = open ("FEITV/user.txt", "a")
            arquivo.write (f"{usuario}\n")
            arquivo.close()
            print("Cadastro realizado!")
            start()
            break
        else:
            print("Preencha todos os campos!\n")
        return usuario

def lista_cadastro():
    user = []
    arquivo = open("FEITV/user.txt", "r")
    for i in arquivo.readlines():
        i = i.strip()
        if i:
            usuario = ast.literal_eval(i)
            user.append(usuario)
    arquivo.close()
    print(user) #testar se tá retornando legal
    return user


# -----------LOGIN
# transformar os users do cadastro de string para lista
def login():
    while True:
        email = str(input("----> Digite seu email: "))
        senha = str(input("----> Digite sua senha: "))
        users = lista_cadastro()
        if not email.strip() or not senha.strip():
            print("Preencha todos os campos!")
            continue
        
lista_cadastro()