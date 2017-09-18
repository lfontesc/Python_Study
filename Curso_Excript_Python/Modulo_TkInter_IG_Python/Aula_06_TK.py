#========================================
#=============== lfontesc ===============
#========================================

# PLACE

from tkinter import *

def bt_click():
    print("bt_click")

    lb["text"] = "Funcionou!!"

janela = Tk()

bt = Button(janela, width=20, text="OK", command=bt_click)
bt.place(x=100,y=100)

lb = Label(janela, text="Teste")
lb.place(x=100,y=150)
janela.geometry("400x400+200+200")
janela.title("Aprendendo TKInter")
# janela["bg"] = "blue"

#LxA+E+T

janela.mainloop()