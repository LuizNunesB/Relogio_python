from tkinter import *
import tkinter
from datetime import datetime
import pyglet
pyglet.font.add_file("digital-7.ttf")

##CORES##
cor1 = "#3d3d3d" #preta
cor2 = "#fafcff" #branca
cor3 = "#21c25c" #verde
cor4 = "#eb463b" #vermelha
cor6 = "#dedcdc" #cinza
cor7 = "#3080f0" #azul

fundo = cor1
cor = cor2

#CRIAÇÃO DA JANELA
janela=Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

#FUNÇÃO
def relogio():

    tempo=datetime.now()
    hora=tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia=tempo.day
    mes=tempo.strftime("%b")
    ano=tempo.strftime("%Y")

    print(ano)
    print(mes)
    print(dia_semana)
    print(hora)
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana +"  " + str(dia) + "/" + str(mes) + "/" + str(ano))

#LABEL
l1 = Label(janela, text="", font=("digital-7 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)
l2 = Label(janela, text="", font=("digital-7 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop(False)
