from tkinter import *
from logica import *
import tkinter as tk

axc= logica()

def ejecutaVal():
    axc.validarCredenciales(var1.get(), var2.get())
    
Ventana= Tk()
Ventana.title("Login")
Ventana.geometry("300x150")


seccion1= Frame (Ventana)    
seccion1.pack(expand= True, fill='both')

titulo= Label(seccion1, text= "Login POO", bg="black", fg="white", font=("Helvetica", 18)).pack()

var1 = tk.StringVar()
lblCorreo= Label(seccion1,text="Correo: ").pack()
txtCorreo= Entry(seccion1,textvariable=var1, takefocus=True).pack()


var2 = tk.StringVar()
lblContra= Label(seccion1,text="Contraseña: ").pack()
txtContra= Entry(seccion1,show="++", textvariable=var2).pack()


botonAcceso= Button(seccion1,text="Acceder", bg="green", command= ejecutaVal)
botonAcceso.pack()


#Main
Ventana.mainloop()
