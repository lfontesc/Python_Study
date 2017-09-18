#========================================
#=============== lfontesc ===============
#========================================

from tkinter import *

def bt_click():
    print("bt_click")

    if (str(ed1.get()).isnumeric() and str(ed2.get().isnumeric())):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 + num2
    else:
        lb["text"] = "Valores informados inválidos"

janela = Tk()

ed1 = Entry(janela)
ed1.place(x=100,y=100)
ed2 = Entry(janela)
ed2.place(x=100,y=130)
bt1 = Button(janela , width=20,text="SOMA", command=bt_click)
bt1.place(x=100,y=150)
lb = Label(janela, text="Aqui fica a soma")
lb.place(x=100,y=200)
janela.title("Aula 09 TK #Lets GO")
janela.geometry("300x300+200+200")
janela.mainloop()