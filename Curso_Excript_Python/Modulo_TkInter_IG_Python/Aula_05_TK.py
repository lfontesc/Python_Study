#========================================
#=============== lfontesc ===============
#========================================

# PLACE

from tkinter import *

janela = Tk()
lb = Label(janela, text="Olá Mundo!!")
lb.place(x=10, y=10)


janela.geometry("400x400+200+200")
janela.title("Aprendendo TKInter")
# janela["bg"] = "blue"

#LxA+E+T

janela.mainloop()