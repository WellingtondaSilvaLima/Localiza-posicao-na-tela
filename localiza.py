import tkinter as tk
from tkinter import PhotoImage, Label, StringVar, Entry, Button, END
import pyautogui as pa
import time

# -------------Configurações da Tela-----------------
tela = tk.Tk()
largura = 330
altura = 130

icon = PhotoImage(file='imagens/logo.png')

tela.title('Localiza')
tela.iconphoto(False, icon)
tela.geometry(f'{largura}x{altura}')
tela.resizable(False, False)
tela.configure(bg='purple')
# ---------------------------------------------------

def pega_posicao(texto: Entry):
  time.sleep(5)
  x, y = pa.position()
  ponto = f'{x}, {y}'
  texto.delete(0, END)
  texto.insert(0, ponto)

titulo = Label(tela,
               text='Ponto na Tela',
               font=('Helvetica', 14, 'bold'),
               fg='white',
               bg='purple')
titulo.pack(pady=10)

inicio = StringVar(value='Gere as coordenadas...')

coordenadas = Entry(tela,
                    textvariable=inicio,
                    font=('Helvetica', 12),
                    fg='white',
                    bg='purple')
coordenadas.pack(pady=5)

btn_gera = Button(tela,
               text='Gerar',
               command=lambda: pega_posicao(coordenadas),
               font=('Helvetica', 12),
               fg='white',
               bg='purple')
btn_gera.pack(pady=5)


tela.mainloop()