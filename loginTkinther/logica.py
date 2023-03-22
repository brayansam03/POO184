from tkinter import messagebox

class logica:
    
    def __init__(self):
        self.__correoC= "iiguerra@outlook.com"
        self.__contraC= "1a2b3c4d"
        
        def validarCredenciales(self,correo,contra):
            if (correo == "" or contra == ""):
                messagebox.showwarning("Cuidado", "Usuario y Contraseña deben contener algo")
            else: 
                if(self.__correoC == correo and self.__contraC == contra):
                    messagebox.showinfo("Exito", "Bienvenido al Sistema")  
                else:
                    messagebox.showerror("Error", "Revisa tus Credenciales")    
                    