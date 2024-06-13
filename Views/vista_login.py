import tkinter as tk
from tkinter import messagebox

def Credenciales():
    ventana = tk.Tk()
    ventana.title("LogIn")
    ventana.geometry("800x600")

    lbl_user = tk.Label(ventana, text="Usuario:")
    lbl_user.pack()
    entry_user = tk.Entry(ventana)
    entry_user.pack()

    lbl_pass = tk.Label(ventana, text="Contraseña:")
    lbl_pass.pack()
    entry_pass = tk.Entry(ventana, show="*")
    entry_pass.pack()

    credentials = {}

    def iniciar_sesion():
        usuario = entry_user.get()
        contraseña = entry_pass.get()
        if not usuario or not contraseña:
            messagebox.showerror("Error", "Es necesario rellenar los campos")
            return
        credentials['user'] = usuario
        credentials['password'] = contraseña
        ventana.destroy()

    btn_iniciar = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
    btn_iniciar.pack()
    ventana.mainloop()

    return credentials.get('user'), credentials.get('password')