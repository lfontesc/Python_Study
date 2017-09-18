#========================================
#=============== lfontesc ===============
#========================================

# PLACE

from tkinter import *

def bt_onclick():
    print(ed.get())
    lb["text"] = ed.get()
janela = Tk()

ed = Entry(janela)
ed.place(x=100,y=100)
lb = Label(janela, text="...")
lb.place(x=100,y=200)
bt = Button(janela,width=20,text="Ok", command=bt_onclick)
bt.place(x=100,y=150)
janela.geometry("300x300+300+300")
janela.mainloop()