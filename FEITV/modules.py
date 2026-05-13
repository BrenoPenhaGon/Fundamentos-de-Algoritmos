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
    while True:
        hudinicial = int(input("\n" \
        "----- FEITV -----\n" \
        "----> Digite 1 para fazer cadastro.\n" \
        "----> Digite 2 para fazer login.\n"
        "----> Digite 3 para sair\n"
        "----> "))
        if hudinicial == 1:
            cadastro()
        elif hudinicial == 2:
            login()
        elif hudinicial == 3:
            break #por algum motivo essa bosta tá indo pro streaming, sla pq kkkkkkkkkkkkkkkkk (mas é só se eu for pra lá alguma vez (que bglh bizarro do krl))

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

# carrega a lista de usuarios
def lista_cadastro():
    user = []
    arquivo = open("FEITV/user.txt", "r")
    for i in arquivo.readlines():
        i = i.strip()
        if i:
            usuario = ast.literal_eval(i)
            user.append(usuario)
    arquivo.close()
    # print(user) #testar se tá retornando legal
    return user

# -----------LOGIN
def login():
    while True:
        email = str(input("----> Digite seu email: "))
        senha = str(input("----> Digite sua senha: "))
        if not email.strip() or not senha.strip():
            print("Preencha todos os campos!")
            continue
        users = lista_cadastro()

        for user in users:
            if user['email'] == email and user['senha'] == senha:
                print(f"Login realizado! Bem-vindo, {user['nome']}!")
                menu_filmes()
                break
        else:
            ("Email ou senha incorretos. Tente Novamente. \n")

# -----------STREAMING
def menu_filmes():
    while True:
        hud_streaming = input(
            "\n--- Catálogo ---\n"
            "----> Digite 1 para ver todos os filmes\n"
            "----> Digite 2 para buscar filme por título\n"
            "----> Digite 3 para voltar\n"
            "----> "
        )

        if hud_streaming == "1":
            listar_titulos()
        elif hud_streaming == "2":
            termo = input("----> Digite o título (ou parte dele): ")
            buscar_filme(termo)
        elif hud_streaming == "3":
            inicio()
        else:
            print("Opção inválida.")

# carrega a lista de filmes
def carregar_filmes():
    filmes = []
    arquivo = open("FEITV/filmes.txt", "r", encoding="utf-8")
    for linha in arquivo.readlines():
        linha = linha.strip()
        if linha:
            partes = linha.split(";")
            filme = {
                "titulo"   : partes[0],
                "descricao": partes[1],
                "nota"     : partes[2],
                "diretor"  : partes[3]
            }
            filmes.append(filme)
    arquivo.close()
    return filmes

# -----------CATALOGO
def listar_titulos():
    filmes = carregar_filmes()
    print("\n--- Filmes disponíveis ---")
    for i, filme in enumerate(filmes, start=1):
        print(f"{i}. {filme['titulo']} ({filme['nota']}) - Dir: {filme['diretor']}")

# -----------BUSCADOR 2000
def buscar_filme(termo):
    filmes = carregar_filmes()
    termo = termo.lower().strip()
    resultados = [f for f in filmes if termo in f["titulo"].lower()]

    if not resultados:
        print("Nenhum filme encontrado.")
        return

    print(f"\n--- Resultados para '{termo}' ---")
    for filme in resultados:
        exibir_filme(filme)

def exibir_filme(filme):
    print(f"""
  Título    : {filme['titulo']}
  Descrição : {filme['descricao']}
  Nota      : {filme['nota']}
  Diretor   : {filme['diretor']}
    """)

        
start()