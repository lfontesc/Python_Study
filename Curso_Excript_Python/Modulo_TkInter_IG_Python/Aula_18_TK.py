#========================================
#=============== lfontesc ===============
#========================================

from tkinter import *

janela = Tk()

lb1 = Label(janela,text="Espaço ", width=15,height=3,bg="blue")
lb1.grid(row=1,column=1)
lb2 = Label(janela,text="Horizontal ", bg="yellow")
lb2.grid(row=2,column=1,sticky=E)
lb3 = Label(janela,text="Vertical", bg="yellow")
lb3.grid(row=1,column=2,sticky=S)



janela.title("Aula_18_TK #Lets GO")
janela.geometry("200x100+100+100")
janela.mainloop()

