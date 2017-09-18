#========================================
#=============== lfontesc ===============
#========================================

from tkinter import *

janela = Tk()

lb1 = Label(janela,text="Label 1", bg="green")
lb2 = Label(janela,text="Label 2", bg="red")
lb3 = Label(janela,text="Label 3", bg="yellow")
lb4 = Label(janela,text="Label 4", bg="blue")

lb1.pack(side=TOP)
lb2.pack(side=LEFT)
lb3.pack(side=RIGHT)
lb4.pack(side=BOTTOM)

janela["bg"] = "black"
janela.title("Aula_10_TK #Lets GO")
janela.geometry("400x300")
janela.mainloop()

