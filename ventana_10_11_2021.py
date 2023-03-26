from tkinter import *

a=StringVar
raiz=Tk()
def hija():
    segunda=Tk()
    segunda.geometry("400x500+600+200")
    segunda.title("Esta es una ventana secundaria")
    Label1=Label(segunda,text="\nventana hija",width=15,height=1,anchor="center").pack()
    Label2=Label(raiz,text=a.get(),width=20,height=30, ).pack()
    segunda.mainloop()

#ventana principal 
raiz.geometry("400x500+600+300")
raiz.resizable(0,0)
raiz.title("Esta es mi primera ventana")
raiz.iconbitmap("wmp.ico")
raiz.config(background="green",cursor="heart")
etiqueta1=Label(raiz,text="Ventana padre",x=10,y=20,width=15,height=10,anchor="center").pack()

boton1=Button(raiz,text="Click aqui",command=hija,background="red").pack()
entrada=Entry(raiz,textvariable=a).pack()
raiz.mainloop()