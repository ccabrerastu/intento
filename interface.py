from tkinter import *

 

def send_data():
  username_info = username.get()
  password_info = password.get()
  DNI_info = DNI.get()
  age_info = str(age.get())
  print(username_info,"\t", password_info,"\t", DNI_info,"\t", age_info)
 
#  Open and write data to a file
  file = open("user.txt", "a")
  file.write(username_info)
  file.write("\t")
  file.write(password_info)
  file.write("\t")
  file.write(DNI_info)
  file.write("\t")
  file.write(age_info)
  file.write("\t\n")
  file.close()
  print(" Nuevo paciente registrado. Nombre: {} | DNI: {}   ".format(username_info, DNI_info))
 
#  Delete data from previous event
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  DNI_entry.delete(0, END)
  age_entry.delete(0, END)

# Create new instance - Class Tk()  
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Registration Form - Python + Tkinter")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = " Hospital |  Los Malditos de Programacion 1", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
username_label = Label(text = "Nombre", bg = "#FFEEDD")
username_label.place(x = 22, y = 70)
password_label = Label(text = "Contraseña", bg = "#FFEEDD")
password_label.place(x = 22, y = 130)
DNI_label = Label(text = "DNI", bg = "#FFEEDD")
DNI_label.place(x = 22, y = 190)
age_label = Label(text = "Edad", bg = "#FFEEDD")
age_label.place(x = 22, y = 250)
 
# Get and store data from users 
username = StringVar()
password = StringVar()
DNI = StringVar()
age = StringVar()
 
username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*")
DNI_entry = Entry(textvariable = DNI, width = "40")
age_entry = Entry(textvariable = age, width = "40")
 
username_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)
DNI_entry.place(x = 22, y = 220)
age_entry.place(x = 22, y = 280)
 
# Submit Button
submit_btn = Button(mywindow,text = "Ingresar informacion", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 320)

mywindow.mainloop()