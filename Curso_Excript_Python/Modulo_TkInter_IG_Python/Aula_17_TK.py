#========================================
#=============== lfontesc ===============
#========================================

from tkinter import *

janela = Tk()

lb1 = Label(janela,text="Login: ")
lb1.grid(row=1,column=1)
lb2 = Label(janela,text="Senha: ")
lb2.grid(row=2,column=1)

ed1 = Entry(janela)
ed1.grid(row=1,column=2)
ed2 = Entry(janela)
ed2.grid(row=2,column=2)

bt1= Button(janela, text="Confirmar")
bt1.grid(row=3,column=2)


janela.title("Aula_17_TK #Lets GO")
janela.geometry("200x100+100+100")
janela.mainloop()

