#========================================
#=============== lfontesc ===============
#========================================

from tkinter import *

janela = Tk()

lb1 = Label(janela,text="Label 1")
lb1.grid(row=1,column=1)
lb2 = Label(janela,text="Label 2")
lb2.grid(row=1,column=2)
lb3 = Label(janela,text="Label 3")
lb3.grid(row=2,column=1)
lb4 = Label(janela,text="Label 4")
lb4.grid(row=2,column=2)

janela.title("Aula_16_TK #Lets GO")
janela.geometry("400x300")
janela.mainloop()

