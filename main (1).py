import tkinter as tk
from tkinter import messagebox
import random
import turtle

perguntas = [
    "voce gosta de surpresas?",
    "voce sabia que é muito especial pra mim?",
    "voce esta feliz hoje?",
    "voce me ama mesmo?",
    "tu confia em mim?",
    "quer ser a endauldi do meu agrummgit?",
    "voce aceita namorar comigo?"
]

mensagens_negacao = [
    "Tem certeza que quer dizer não?",
    "Poxa... eu achei que a gente tava indo tão bem 😢",
    "Você tem certeza mesmo mesmo mesmo?",
    "Se clicar em sim eu faço um coração 🥺",
    "Não faz isso comigo 😭",
    "Talvez você queira tentar de novo... com SIM 😅",
    "Um não agora pode quebrar meu coração 💔",
    "Certeza? Sim é tão mais bonito 😌",
    "Sim rima com fim... de ser solteira 👀",
    "Diz sim, vai ser fofo 😍"
]

indice_pergunta = 0

def enviar_resposta(resposta):
    global indice_pergunta

    if resposta == "Não":
        mensagem = random.choice(mensagens_negacao)
        confirmacao = messagebox.askyesno("Tem certeza?", mensagem)
        if not confirmacao:
            return
        else:
            return

    if indice_pergunta < len(perguntas) - 1:
        indice_pergunta += 1
        rotulo.config(text=perguntas[indice_pergunta])

        if indice_pergunta == len(perguntas) - 1:
            botao_nao.place(relx=0.65, rely=0.6, anchor=tk.CENTER)
            botao_nao.bind("<Enter>", mover_botao_nao)
        else:
            botao_nao.place(relx=0.65, rely=0.6, anchor=tk.CENTER)
            botao_nao.unbind("<Enter>")
    else:
        if resposta == "Sim":
            messagebox.showinfo("Eba!!!!", "Eu te amo!")
            janela.destroy()
            desenhar_coracao()

def desenhar_coracao():
    pen = turtle.Turtle()

    def curve():
        for i in range(200):
            pen.right(1)
            pen.forward(1)

    def heart():
        pen.fillcolor('red')
        pen.begin_fill()
        pen.left(140)
        pen.forward(113)
        curve()
        pen.left(120)
        curve()
        pen.forward(112)
        pen.end_fill()

    def txt():
        pen.up()
        pen.setpos(-68, 95)
        pen.down()
        pen.color('white')
        pen.write("Eu te amo, meu amor!", font=("Verdana", 8, "bold"))

    window = turtle.Screen()
    window.bgcolor("white")
    pen.color('red')
    pen.begin_fill()
    heart()
    pen.end_fill()
    txt()
    pen.ht()
    turtle.done()

def mover_botao_nao(event):
    x1 = botao_nao.winfo_width() // 2
    y1 = botao_nao.winfo_height() // 2
    x2 = janela.winfo_width() - botao_nao.winfo_width() // 2
    y2 = janela.winfo_height() - botao_nao.winfo_height() // 2
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    botao_nao.place(x=x, y=y)

janela = tk.Tk()
janela.title("Perguntinhas")
janela.attributes("-fullscreen", True)

canvas = tk.Canvas(janela, width=janela.winfo_screenwidth(), height=janela.winfo_screenheight())
canvas.pack()

cor_inicio = "#FFB6C1"
cor_fim = "#FF69B4"
for i in range(canvas.winfo_reqheight()):
    cor = '#{:02x}{:02x}{:02x}'.format(
        int((1 - i / canvas.winfo_reqheight()) * int(cor_inicio[1:3], 16) + (i / canvas.winfo_reqheight()) * int(cor_fim[1:3], 16)),
        int((1 - i / canvas.winfo_reqheight()) * int(cor_inicio[3:5], 16) + (i / canvas.winfo_reqheight()) * int(cor_fim[3:5], 16)),
        int((1 - i / canvas.winfo_reqheight()) * int(cor_inicio[5:7], 16) + (i / canvas.winfo_reqheight()) * int(cor_fim[5:7], 16)))
    canvas.create_line(0, i, canvas.winfo_reqwidth(), i, fill=cor)

for _ in range(100):
    x = random.randint(0, canvas.winfo_reqwidth())
    y = random.randint(0, canvas.winfo_reqheight())
    tamanho = random.randint(10, 25)
    cor = random.choice(["#FF1493", "#FF69B4", "#DB7093", "#FFC0CB"])
    canvas.create_text(x, y, text="❤", fill=cor, font=("Arial", tamanho))

rotulo = tk.Label(janela, text=perguntas[indice_pergunta], font=("Arial", 26, "bold"), fg="white", bg=cor_fim)
rotulo.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

botao_sim = tk.Button(janela, text="Sim", font=("Arial", 20, "bold"), bg=cor_inicio, fg="white", command=lambda: enviar_resposta("Sim"))
botao_sim.place(relx=0.35, rely=0.6, anchor=tk.CENTER)

botao_nao = tk.Button(janela, text="Nao", font=("Arial", 20, "bold"), bg=cor_inicio, fg="white", command=lambda: enviar_resposta("Não"))
botao_nao.place(relx=0.65, rely=0.6, anchor=tk.CENTER)

janela.mainloop()
