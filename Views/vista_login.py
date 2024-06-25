import tkinter as tk
from tkinter import Entry, Label, Button

class Login:
    def __init__(self, master=None):
        self.master_root = master if master else tk.Tk()
        self.master_root.title("INICIO DE SESIÓN")
        self.master_root.geometry("340x480")

        self.txt_usuario = tk.StringVar()
        self.txt_contrasena = tk.StringVar()
        self.credentials = {}

        self.formulario_login()

        if not master:
            self.master_root.mainloop()

    def formulario_login(self):
        tk.Label(self.master_root, text="INICIO DE SESIÓN").grid(row=0, column=0, columnspan=2)

        tk.Label(self.master_root, text="Usuario:").grid(row=1, column=0)
        usuario_entry = Entry(self.master_root, textvariable=self.txt_usuario, width=30)
        usuario_entry.grid(row=1, column=1, padx=6, pady=6)

        tk.Label(self.master_root, text="Contraseña:").grid(row=2, column=0)
        contrasena_entry = Entry(self.master_root, textvariable=self.txt_contrasena, width=30, show="*")
        contrasena_entry.grid(row=2, column=1, padx=6, pady=6)

        Button(self.master_root, text="Acceder", width=15, command=self.iniciar_sesion).grid(row=3, column=0, padx=6, pady=6)
        Button(self.master_root, text="Cancelar", width=15, command=self.master_root.destroy).grid(row=3, column=1, padx=6, pady=6)

    def iniciar_sesion(self):
        usuario = self.txt_usuario.get()
        contraseña = self.txt_contrasena.get()
        if not usuario or not contraseña:
            self.show_error("Error", "Es necesario rellenar los campos")
            return
        self.credentials['user'] = usuario
        self.credentials['password'] = contraseña
        self.master_root.destroy()

    def show_error(self, title, message):
        top = tk.Toplevel(self.master_root)
        top.title(title)
        tk.Label(top, text=message).pack(padx=20, pady=10)
        Button(top, text="Aceptar", command=top.destroy).pack(pady=10)

    def get_credentials(self):
        return self.credentials.get('user'), self.credentials.get('password')

# Ejemplo de uso:
if __name__ == "__main__":
    login = Login()
    user, password = login.get_credentials()
    if user and password:
        print(f"Usuario: {user}, Contraseña: {password}")
    else:
        print("Inicio de sesión cancelado.")
