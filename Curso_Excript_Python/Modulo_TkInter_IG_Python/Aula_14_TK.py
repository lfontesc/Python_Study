#========================================
#=============== lfontesc ===============
#========================================

from tkinter import *

janela = Tk()

lb1 = Label(janela,text="Linha 1", bg="white")
lb2 = Label(janela,text="Linha 2", bg="red")
lb3 = Label(janela,text="Linha 3", bg="white")
lb4 = Label(janela,text="Linha 4", bg="red")

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)

janela["bg"] = "black"
janela.title("Aula_10_TK #Lets GO")
janela.geometry("400x300")
janela.mainloop()

