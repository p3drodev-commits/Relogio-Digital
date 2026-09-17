import tkinter as tk
from time import strftime


def atualizar_relogio():
    hora = strftime('%H:%M:%S')
    relogio.config(text=hora)
    relogio.after(1000, atualizar_relogio)


janela = tk.Tk()
janela.title('Relógio Digital')
janela.geometry('500x250')
janela.configure(bg='#0f172a')

titulo = tk.Label(
    janela,
    text='RELÓGIO DIGITAL',
    font=('Arial', 18, 'bold'),
    bg='#0f172a',
    fg='white'
)
titulo.pack(pady=25)

relogio = tk.Label(
    janela,
    font=('Consolas', 55, 'bold'),
    bg='#0f172a',
    fg='#38bdf8'
)
relogio.pack()

atualizar_relogio()

janela.mainloop()