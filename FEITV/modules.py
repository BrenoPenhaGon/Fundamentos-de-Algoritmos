# -----------IMPORTS
import ast
import os


# -----------MAIN
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
            break

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
                menu_filmes(user)
                return
        else:
            ("Email ou senha incorretos. Tente Novamente. \n")

# -----------STREAMING
def menu_filmes(user):
    while True:
        hud_streaming = input(
            "\n--- Catálogo ---\n"
            "----> Digite 1 para ver todos os filmes\n"
            "----> Digite 2 para buscar filme por título\n"
            "----> Digite 3 para ver os favoritos\n" \
            "----> Digite 4 para voltar\n"
            "----> "
        )

        if hud_streaming == "1":
            listar_titulos(user)
        elif hud_streaming == "2":
            termo = input("----> Digite o título (ou parte dele): ")
            buscar_filme(termo, user)
        elif hud_streaming == "3":
            listar_favoritos(user)
        elif hud_streaming == "4":
            inicio()
        else:
            print("Opção inválida.")

# -----------CARREGADOR
def lista_cadastro():
    user = []
    arquivo = open("FEITV/user.txt", "r")
    for i in arquivo.readlines():
        i = i.strip()
        if i:
            usuario = ast.literal_eval(i)
            user.append(usuario)
    arquivo.close()
    return user

def carregar_filmes():
    filmes = []
    arquivo = open("FEITV/filmes.txt", "r")
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

def carregar_favoritos(email):
    if not os.path.exists("FEITV/favoritos.txt"):
        return []
    arquivo = open("FEITV/favoritos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in linhas:
        linha = linha.strip()
        if linha:
            entrada = ast.literal_eval(linha)
            if entrada["email"] == email:
                return entrada["favoritos"]
    return []

# -----------CATALOGO
def listar_titulos(user):
    filmes = carregar_filmes()
    print("\n--- Filmes disponíveis ---")
    for i, filme in enumerate(filmes, start=1):
        print(f"{i}. {filme['titulo']} ({filme['nota']}) - Dir: {filme['diretor']}")

    escolha = input("\n----> Digite o número do filme para ver detalhes (0 para voltar): ")

    if not escolha.isdigit():
        print("Opção inválida.")
        return

    escolha = int(escolha)

    if escolha == 0:
        return

    if escolha < 1 or escolha > len(filmes):
        print("Opção inválida.")
        return

    exibir_filme(filmes[escolha - 1], user)

# -----------BUSCADOR 3000
def buscar_filme(termo, user):
    filmes = carregar_filmes()
    resultados = [f for f in filmes if termo.lower().strip() in f["titulo"].lower()]

    if not resultados:
        print("Nenhum filme encontrado.")
        return

    print(f"\n--- Resultados para '{termo}' ---")
    for i, filme in enumerate(resultados, start=1):
        print(f"{i}. {filme['titulo']} ({filme['nota']}) - Dir: {filme['diretor']}")

    escolha = input("\n----> Digite o número do filme para ver detalhes (0 para voltar): ")

    if not escolha.isdigit():
        print("Opção inválida.")
        return

    escolha = int(escolha)

    if escolha == 0:
        return

    if escolha < 1 or escolha > len(resultados):
        print("Opção inválida.")
        return

    exibir_filme(resultados[escolha - 1], user)


# -----------EXIBIR FILMES
def exibir_filme(filme, user):
    favoritos = carregar_favoritos(user["email"])
    ja_favoritado = filme["titulo"] in favoritos

    print(f"""
  Título    : {filme['titulo']}
  Descrição : {filme['descricao']}
  Nota      : {filme['nota']}
  Diretor   : {filme['diretor']}
  Favorito  : {"Sim" if ja_favoritado else "Não"}
    """)

    if ja_favoritado:
        op = input("----> Digite 1 para remover dos favoritos ou 0 para voltar: ")
        if op == "1":
            favoritos.remove(filme["titulo"])
            salvar_favoritos(user["email"], favoritos)
            print(f"'{filme['titulo']}' removido dos favoritos.")
    else:
        op = input("----> Digite 1 para adicionar aos favoritos ou 0 para voltar: ")
        if op == "1":
            favoritos.append(filme["titulo"])
            salvar_favoritos(user["email"], favoritos)
            print(f"'{filme['titulo']}' adicionado aos favoritos!")


# -----------LISTA DE FAVORITOS
def listar_favoritos(user):
    favoritos = carregar_favoritos(user["email"])
    print("\n--- Meus Favoritos ---")
    if not favoritos:
        print("Você ainda não tem filmes favoritos.")
        return
    for i, titulo in enumerate(favoritos, start=1):
        print(f"{i}. {titulo}")

def salvar_favoritos(email, favoritos):
    entradas = []
    if os.path.exists("FEITV/favoritos.txt"):
        arquivo = open("FEITV/favoritos.txt", "r", encoding="utf-8")
        for linha in arquivo.readlines():
            linha = linha.strip()
            if linha:
                entrada = ast.literal_eval(linha)
                if entrada["email"] != email:
                    entradas.append(entrada)
        arquivo.close()

    entradas.append({"email": email, "favoritos": favoritos})
    arquivo = open("FEITV/favoritos.txt", "w", encoding="utf-8")
    for entrada in entradas:
        arquivo.write(f"{entrada}\n")
    arquivo.close()

# ----------------------
# RODAR
# ----------------------
start()