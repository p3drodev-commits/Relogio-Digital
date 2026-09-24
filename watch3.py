import tkinter as tk
from datetime import datetime

# ----------------------------
# CONFIGURAÇÕES
# ----------------------------

formato_24h = True
tema_escuro = True

dias_semana = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro"
]


# ----------------------------
# FUNÇÕES
# ----------------------------

def atualizar_relogio():
    agora = datetime.now()

    # Horário em formato 24h ou 12h
    if formato_24h:
        hora = agora.strftime("%H:%M:%S")
    else:
        hora = agora.strftime("%I:%M:%S %p")

    # Dia da semana
    dia_semana = dias_semana[agora.weekday()]

    # Data completa
    data_completa = (
        f"{agora.day} de "
        f"{meses[agora.month - 1]} de "
        f"{agora.year}"
    )

    # Atualiza os textos
    relogio.config(text=hora)
    label_dia.config(text=dia_semana)
    label_data.config(text=data_completa)

    # Atualiza novamente após 1 segundo
    janela.after(1000, atualizar_relogio)


def mudar_formato():
    global formato_24h

    formato_24h = not formato_24h

    if formato_24h:
        botao_formato.config(text="Usar formato 12h")
    else:
        botao_formato.config(text="Usar formato 24h")


def mudar_tema():
    global tema_escuro

    tema_escuro = not tema_escuro

    if tema_escuro:
        fundo = "#0f172a"
        texto = "white"
        destaque = "#38bdf8"

        botao_tema.config(text="Tema Claro")

    else:
        fundo = "#f1f5f9"
        texto = "#0f172a"
        destaque = "#0284c7"

        botao_tema.config(text="Tema Escuro")

    # Altera a cor da janela
    janela.configure(bg=fundo)

    # Altera os componentes
    titulo.config(bg=fundo, fg=texto)
    relogio.config(bg=fundo, fg=destaque)
    label_dia.config(bg=fundo, fg=texto)
    label_data.config(bg=fundo, fg=texto)


# ----------------------------
# JANELA PRINCIPAL
# ----------------------------

janela = tk.Tk()

janela.title("Relógio Digital")
janela.geometry("600x400")
janela.configure(bg="#0f172a")

# Impede redimensionamento
janela.resizable(False, False)


# ----------------------------
# TÍTULO
# ----------------------------

titulo = tk.Label(
    janela,
    text="RELÓGIO DIGITAL",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="white"
)

titulo.pack(pady=(30, 15))


# ----------------------------
# RELÓGIO
# ----------------------------

relogio = tk.Label(
    janela,
    font=("Consolas", 55, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

relogio.pack()


# ----------------------------
# DIA DA SEMANA
# ----------------------------

label_dia = tk.Label(
    janela,
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="white"
)

label_dia.pack(pady=(10, 0))


# ----------------------------
# DATA
# ----------------------------

label_data = tk.Label(
    janela,
    font=("Arial", 16),
    bg="#0f172a",
    fg="white"
)

label_data.pack(pady=(5, 20))


# ----------------------------
# BOTÕES
# ----------------------------

frame_botoes = tk.Frame(
    janela,
    bg="#0f172a"
)

frame_botoes.pack(pady=10)


botao_formato = tk.Button(
    frame_botoes,
    text="Usar formato 12h",
    font=("Arial", 11),
    command=mudar_formato,
    width=18
)

botao_formato.pack(
    side="left",
    padx=10
)


botao_tema = tk.Button(
    frame_botoes,
    text="Tema Claro",
    font=("Arial", 11),
    command=mudar_tema,
    width=18
)

botao_tema.pack(
    side="left",
    padx=10
)


# ----------------------------
# INICIAR RELÓGIO
# ----------------------------

atualizar_relogio()

janela.mainloop()