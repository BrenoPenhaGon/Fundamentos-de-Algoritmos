from tkinter import *

janela = Tk()
janela.title("Algoritmos")
janela.geometry('400x400')

rotulo = Label(janela, text='Hello GUI!', font=('Arial Bond', 14))
rotulo.place(x=200, y=100, anchor=CENTER)

entrada = Entry(janela, width=14, font=('Arial Bond', 14))
entrada.place(x=200, y=50, anchor=CENTER)

# redefinição na função clique
def clique():
    resposta = entrada.get()
    rotulo['text'] = 'Novo texto!'

# cria o botão na janela com o texto desejado
botao = Button(janela, text='Clique Aqui!', command=clique)

# configura onde o botão deve estar posicionado
botao.place(x=200, y=200, anchor=CENTER)

janela.mainloop()