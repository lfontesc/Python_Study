#========================================
#=============== lfontesc ===============
#========================================

from tkinter import *

janela = Tk()

lb1 = Label(janela,text="SIDE1", bg="white")
lb2 = Label(janela,text="Label 2", bg="red")
lb3 = Label(janela,text="Anchor 1", bg="white")
lb4 = Label(janela,text="Anchor 2", bg="red")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=W)
lb4.pack(anchor=W)

janela["bg"] = "black"
janela.title("Aula_10_TK #Lets GO")
janela.geometry("400x300")
janela.mainloop()

