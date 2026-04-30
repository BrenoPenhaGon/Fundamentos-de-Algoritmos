from tkinter import *

# cria a janela
janela = Tk()

# titulo para a janela
janela.title("Algoritmos")

# configura o tamanho da janela
janela.geometry('400x400')

#cria um rotulo na janela, adiciona um texto e configura fonte
rotulo = Label(janela, text="Hello GUI!", font=("Arial Bold", 14))

#configura onde a label vai aparecer na janela
rotulo.place(x=200, y=100, anchor=CENTER)

# chama a função mainloop:
# loop infinito para manter a janela aberta
janela.mainloop()