#========================================
#=============== lfontesc ===============
#========================================

from tkinter import *

janela = Tk()

lb1 = Label(janela,text="Horizontal", bg="white")
lb2 = Label(janela,text="Label 2", bg="red")
lb3 = Label(janela,text="Anchor 1", bg="white")
# lb4 = Label(janela,text="Anchor 2", bg="red")

lb1.pack(side=TOP, fill=X)
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)
# lb4.pack(anchor=W)

janela["bg"] = "black"
janela.title("Aula_10_TK #Lets GO")
janela.geometry("400x300")
janela.mainloop()

