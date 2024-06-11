from tkinter import *
from customtkinter import *
set_appearance_mode("dark")

class Login:
    def __init__(self):
        self.master_root = CTk()
        self.master_root.title("INICIO DE SESIÓN")
        self.master_root.geometry("400x300")

        # Llamada al formulario_login
        self.formulario_login()

        # Bucle mainloop()
        self.master_root.mainloop()

    def formulario_login(self):
        CTkLabel(self.master_root, text="INICIO DE SESIÓN").grid(row=0, column=0, columnspan=2)

        CTkLabel(self.master_root, text="Usuario:").grid(row=1, column=0)
        txt_usuario = StringVar()
        usuario_entry = CTkEntry(self.master_root, textvariable=txt_usuario, width=150, height=30)
        usuario_entry.grid(row=1, column=1, padx=6, pady=6)

        CTkLabel(self.master_root, text="Contraseña:").grid(row=2, column=0)
        txt_contrasena = StringVar()
        contrasena_entry = CTkEntry(self.master_root, textvariable=txt_contrasena, width=150, height=30)
        contrasena_entry.grid(row=2, column=1, padx=6, pady=6)

        CTkButton(self.master_root, text="Acceder", width=150, height=30).grid(row=3, column=0, padx=6, pady=6)
        CTkButton(self.master_root, text="Cancelar", width=150, height=30).grid(row=3, column=1, padx=6, pady=6)


ventana = Login()