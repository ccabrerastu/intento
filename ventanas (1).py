from tkinter import *
raiz=Tk()
a=StringVar
def hija():
    segunda=Tk()
    segunda.geometry("300x300-0-0")
    segunda.grab_set()
    segunda.title("esta es la ventana hija")
    Label(segunda,text="ventana hija",width=100,height=100,anchor=CENTER).pack()
    Label(raiz,text=a,width=25,height=25,anchor=CENTER).pack()
    segunda.mainloop()
a="Hola como estan?"
raiz.geometry("400x500+600+300")
raiz.resizable(0,0)
raiz.title("Esta es mi primera ventana")
raiz.iconbitmap("wmp.ico")
raiz.config(background="green",cursor="heart")
Label(raiz,text="Ventana padre",width=5,height=5,anchor=CENTER).pack()
Entry(raiz,textvariable=a).pack()
Button(raiz,text="aqui",command=hija).pack()

raiz.mainloop()