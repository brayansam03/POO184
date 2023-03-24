from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD: 
    
    def __init__(self):
        pass 
    
    def conexionBD(self):
          
        try: 
            conexion= sqlite3.connect()
            print("Conectado BD")
            return conexion
        
        
        except sqlite3.OperationalError:    
            print("No se pudo conectar")
            
        #Metodo para insertar
            
            
    def guardarUsuario(self, nom, cor, con):
        #1. Llamar a la conexión
        conx= self.conexionBD()
        
        #2. Revisar parametros vacíos
        
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Revisa tu Formulario")
            conx.close()
        else: 
            #3. Prepara datos y el querySQL
            cursor= conx.cursor() 
            conH= self.encriptarCon(con)  
            datos=(nom, cor, conH) 
            qrInsert="insert into TBRegistrados(nombre, correo, contra) values(?,?,?)"
            
            #4. Proceder a insertar y cerramos la Conx
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Se guardo el Usuario") 
            

   def encriptarCon(self, con):
       conPlana= con
       conPlana= conPlana.encode() #Convertimos con a bytes
       sal= bcrypt.gensalt()
       conHa= bcrypt.hashpw(conPlana, sal) #Contraseña encriptada
       print(conHa)
       return conHa
                
            