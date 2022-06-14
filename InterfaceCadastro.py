# Importações
import tkinter.messagebox
from tkinter import *
import posiciona

# Criação de funções


def login():
    f1.destroy()
    f2.pack()

    lab_login = Label(f2, image=img_log)
    lab_login.pack()

    us = Entry(f2, bd=2, font=("Calibri", 15), justify=CENTER)
    us.place(width=301, height=31, x=602, y=293)

    sh = Entry(f2, bd=2, font=("Calibri", 15), justify=CENTER, show='*')
    sh.place(width=301, height=32, x=600, y=407)

    b3 = Button(f2, bd=0, image=img_bot2)
    b3.place(width=185, height=108, x=662, y=526)


def format_cpf(event=None):
    text = cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for i in range(len(text)):

        if not text[i] in "0123456789":
            continue
        if i in [2, 5]:
            new_text += text[i] + "."
        elif i == 8:
            new_text += text[i] + "-"
        else:
            new_text += text[i]

    cpf.delete(0, "end")
    cpf.insert(0, new_text)


def format_data(event=None):
    text = data.get().replace("/", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for i in range(len(text)):

        if not text[i] in "0123456789":
            continue
        if i in [1, 3]:
            new_text += text[i] + "/"
        else:
            new_text += text[i]

    data.delete(0, "end")
    data.insert(0, new_text)


def format_tel(event=None):
    text = tele.get().replace("(", "").replace(")", "").replace("-", "")[:12]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for i in range(len(text)):

        if not text[i] in "0123456789":
            continue
        if i in [0]:
            new_text += "(" + text[i]
        elif i in [2]:
            new_text += text[i] + ")"
        elif i in [7]:
            new_text += text[i] + "-"
        else:
            new_text += text[i]

    tele.delete(0, "end")
    tele.insert(0, new_text)


def onClick():
    if nome.get() == "" or data.get() == "" or cpf.get() == "" or tele.get() == "" or rua.get() == "" or num.get() == "" or uf. get() == "" or bai.get() == "" or cid.get() == "":
        tkinter.messagebox.showerror("Cadastro", "Preencha todos os campos!")
    else:
        tkinter.messagebox.showinfo("Cadastro",  "Salvo com sucesso!")


# Criação da janela principal e seus parâmetros
cad = Tk()
cad.title('Cadastro')
cad.geometry('1024x768+610+153')
cad.iconbitmap(default="usuario-de-perfil.png")
cad.resizable(width=False, height=False)

# Comandos para encontrar as coordenadas place
cad.bind('<Button-1>', posiciona.inicio_place)
cad.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, cad))
cad.bind('<Button-2>', lambda arg: posiciona.para_geometry(cad))

# Importação de imagens
img_cadas = PhotoImage(file="Layout_cadas.png")
img_log = PhotoImage(file="Layout_login.png")
img_bot1 = PhotoImage(file="entrar.png")
img_bot2 = PhotoImage(file="login.png")
img_bot3 = PhotoImage(file="cadastrar.png")

# Declaração de Frames
f1 = Frame(cad)
f1.pack()
f2 = Frame(cad)

#
lab_cadas = Label(f1, image=img_cadas)
lab_cadas.pack()

nome = Entry(f1, bd=2, font=("Calibri", 15), justify=CENTER)
nome.place(width=585, height=35, x=418, y=191)

data = Entry(f1, bd=2, font=("Calibri", 15), justify=CENTER)
data.place(width=213, height=35, x=468, y=240)
data.bind("<KeyRelease>", format_data)

cpf = Entry(f1, bd=2, font=("Calibri", 15), justify=CENTER)
cpf.place(width=243, height=35, x=760, y=239)
cpf.bind("<KeyRelease>", format_cpf)

tele = Entry(f1, bd=2, font=("Calibri", 15), justify=CENTER)
tele.place(width=234, height=35, x=447, y=289)
tele.bind("<KeyRelease>", format_tel)

rua = Entry(f1, bd=2, font=("Calibri", 15), justify=CENTER)
rua.place(width=494, height=35, x=392, y=438)

num = Entry(f1, bd=2, font=("Calibri", 15), justify=CENTER)
num.place(width=68, height=35, x=936, y=437)

uf = Entry(f1, bd=2, font=("Calibri", 15), justify=CENTER)
uf.place(width=68, height=35, x=937, y=485)

bai = Entry(f1, bd=2, font=("Calibri", 15), justify=CENTER)
bai.place(width=180, height=35, x=415, y=487)

cid = Entry(f1, bd=2, font=("Calibri", 15), justify=CENTER)
cid.place(width=180, height=35, x=706, y=487)

b1 = Button(f1, bd=0, image=img_bot1, command=login)
b1.place(width=183, height=101, x=67, y=549)
b2 = Button(f1, bd=0, image=img_bot3, command=onClick)
b2.place(width=244, height=100, x=559, y=603)

radioVale = tkinter.IntVar()
es = Radiobutton(f1, variable=radioVale, value=1, fg='black', bg='#6BD4CD')
es.place(width=22, height=23, x=785, y=295)
es1 = Radiobutton(f1, variable=radioVale, value=2, fg='black', bg='#6BD4CD')
es1.place(width=22, height=23, x=920, y=294)

cad.mainloop()
