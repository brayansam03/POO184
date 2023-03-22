import tkinter as tk
from tkinter import messagebox

# Variables globales
saldo = 1000  # Saldo inicial


def consultar_saldo():
    global saldo
    messagebox.showinfo("Saldo", f"Su saldo actual es: {saldo}")


def ingresar_efectivo():
    global saldo
    monto = float(entry_monto.get())
    saldo += monto
    messagebox.showinfo("Ingreso", f"Se ha ingresado ${monto} a su cuenta. Su saldo actual es: {saldo}")
    entry_monto.delete(0, tk.END)


def retirar_efectivo():
    global saldo
    monto = float(entry_monto.get())
    if saldo >= monto:
        saldo -= monto
        messagebox.showinfo("Retiro", f"Se ha retirado ${monto} de su cuenta. Su saldo actual es: {saldo}")
        entry_monto.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Saldo insuficiente")
        entry_monto.delete(0, tk.END)


def depositar_otra_cuenta():
    global saldo
    monto = float(entry_monto.get())
    cuenta = entry_cuenta.get()
    if cuenta != "":
        saldo -= monto
        messagebox.showinfo("Depósito", f"Se ha depositado ${monto} a la cuenta {cuenta}. Su saldo actual es: {saldo}")
        entry_monto.delete(0, tk.END)
        entry_cuenta.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Debe ingresar el número de cuenta")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Gestión de cuenta bancaria")

# Crear los elementos de la interfaz
label_saldo = tk.Label(ventana, text=f"Saldo actual: ${saldo}")
label_saldo.grid(row=0, column=0, padx=10, pady=10)

btn_consultar = tk.Button(ventana, text="Consultar saldo", command=consultar_saldo)
btn_consultar.grid(row=1, column=0, padx=10, pady=10)

label_monto = tk.Label(ventana, text="Monto:")
label_monto.grid(row=2, column=0, padx=10, pady=10)

entry_monto = tk.Entry(ventana)
entry_monto.grid(row=2, column=1, padx=10, pady=10)

btn_ingresar = tk.Button(ventana, text="Ingresar efectivo", command=ingresar_efectivo)
btn_ingresar.grid(row=3, column=0, padx=10, pady=10)

btn_retirar = tk.Button(ventana, text="Retirar efectivo", command=retirar_efectivo)
btn_retirar.grid(row=3, column=1, padx=10, pady=10)

label_cuenta = tk.Label(ventana, text="Cuenta:")
label_cuenta.grid(row=4, column=0, padx=10, pady=10)

entry_cuenta = tk.Entry(ventana)
entry_cuenta.grid(row=4, column=1, padx=10, pady=10)

btn_depositar = tk.Button(ventana, text="Depositar a otra cuenta", command=depositar_otra_cuenta)
btn_depositar.grid(row=5, column=0, padx=10, pady=10)

# Ejec
ventana.mainloop()
