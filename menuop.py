from tkinter import *
from tkinter import ttk
from tkinter import messagebox
raiz=Tk()
raiz.geometry("600x600")
raiz.title("Menù de opciones")



def saludo():
    messagebox.showinfo(title="Prueba de opciones",message="Hola, que tal")

def respuesta():
    messagebox.askretrycancel(title="Consulta",message="desea continuar?")

barramenu=Menu(raiz)

opcionesmenu=Menu(barramenu,tearoff=0)
opcionesmenu.add_command(label="Nuevo",command=saludo)
opcionesmenu.add_command(label="Abrir",command=respuesta)
opcionesmenu.add_command(label="Grabar")
opcionesmenu.add_command(label="Grabar como...")
opcionesmenu.add_separator()
opcionesmenu.add_command(label="Salir",command=exit)
barramenu.add_cascade(label="Archivo",menu=opcionesmenu)

editarmenu=Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Editar",menu=editarmenu)


Vermenu=Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Ver",menu=Vermenu)





raiz.config(menu=barramenu)




raiz.mainloop()